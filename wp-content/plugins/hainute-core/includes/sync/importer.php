<?php
/**
 * Feed importer — takes normalized feed items and turns them into
 * products + offers. Source-agnostic: mock, 2Performant and CJ sources
 * all produce the same item shape.
 *
 * Normalized item shape (one item = one product AT one store):
 * array(
 *   'network'     => '2performant' | 'cj' | 'mock',
 *   'program_id'  => string,   // advertiser/program id in that network
 *   'store_name'  => string,   // display name, e.g. 'Modivo'
 *   'external_id' => string,   // merchant's own product id / SKU
 *   'name'        => string,
 *   'description' => string,
 *   'brand'       => string,
 *   'category'    => string,
 *   'gender'      => string,   // optional
 *   'age'         => string,   // optional
 *   'price'       => float,
 *   'old_price'   => float|null,
 *   'currency'    => 'RON',
 *   'in_stock'    => bool,
 *   'stock_qty'   => int|null, // optional — enables 'low_stock'
 *   'url'         => string,   // affiliate link
 *   'images'      => string[],
 *   'material'    => string,   // optional
 *   'sizes'       => string,   // optional, comma-separated
 * )
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Import a batch of normalized items.
 *
 * @param array[] $items   Normalized items (see shape above).
 * @param int     $max_new Cap on new products created this run (0 = unlimited).
 *                         Items needing creation beyond the cap are skipped and
 *                         picked up by the next run — keeps hourly runs short.
 * @return array Summary: { created, matched, offers, errors, skipped_new, notes[] }
 */
function hainute_import_items( array $items, $max_new = 0 ) {
	$summary = array(
		'created'     => 0, // new products created
		'matched'     => 0, // items attached to an existing product
		'offers'      => 0, // offers inserted/updated
		'errors'      => 0,
		'skipped_new' => 0, // deferred to the next run (max_new cap)
		'notes'       => array(),
	);

	$store_cache = array();

	foreach ( $items as $item ) {
		try {
			hainute_import_single_item( $item, $summary, $store_cache, (int) $max_new );
		} catch ( Exception $e ) {
			$summary['errors']++;
			$summary['notes'][] = sprintf( 'Eroare la "%s": %s', $item['name'] ?? '?', $e->getMessage() );
		}
	}

	if ( $summary['skipped_new'] > 0 ) {
		$summary['notes'][] = sprintf(
			'%d produse noi amânate pentru rulările următoare (limita e %d produse noi/rulare).',
			$summary['skipped_new'],
			$max_new
		);
	}

	return $summary;
}

/**
 * @param array $item        Normalized item.
 * @param array $summary     By-ref run summary.
 * @param array $store_cache By-ref cache: "network:program_id" => store term id.
 * @param int   $max_new     Cap on new products this run (0 = unlimited).
 */
function hainute_import_single_item( array $item, array &$summary, array &$store_cache, $max_new = 0 ) {
	foreach ( array( 'network', 'program_id', 'store_name', 'external_id', 'name', 'price', 'url' ) as $required ) {
		if ( empty( $item[ $required ] ) ) {
			throw new Exception( "câmp lipsă în feed: {$required}" );
		}
	}

	// 1. Store (cached per run).
	$store_key = $item['network'] . ':' . $item['program_id'];
	if ( ! isset( $store_cache[ $store_key ] ) ) {
		$store_id = hainute_find_store_by_program( $item['network'], $item['program_id'] );
		if ( ! $store_id ) {
			$store_id = hainute_upsert_store(
				$item['store_name'],
				array( 'network' => $item['network'], 'program_id' => $item['program_id'] )
			);
			if ( is_wp_error( $store_id ) ) {
				throw new Exception( $store_id->get_error_message() );
			}
		}
		$store_cache[ $store_key ] = $store_id;
	}
	$store_id = $store_cache[ $store_key ];

	// 2. Existing offer for this exact (network, external_id)? Then we already
	// know the product — hourly price/stock update path, no matching needed.
	$existing_offer = hainute_find_offer_by_external_id( $item['network'], $item['external_id'] );

	// Guard against stale offers whose product was truly deleted/trashed:
	// drop the orphan rows and fall through to the create path.
	//
	// IMPORTANT: 'draft' și 'pending' NU sunt orfane — sunt produse pe care
	// adminul le-a scos INTENȚIONAT de pe live. Le respectăm: actualizăm oferta
	// (preț/stoc rămân proaspete) dar NU recreăm și NU republicăm produsul.
	if ( $existing_offer ) {
		$product     = get_post( (int) $existing_offer->product_id );
		$kept_states = array( 'publish', 'draft', 'pending', 'private' );
		if ( ! $product || 'product' !== $product->post_type || ! in_array( $product->post_status, $kept_states, true ) ) {
			// trash / auto-draft / șters de tot → chiar e orfan.
			hainute_delete_offers_for_product( (int) $existing_offer->product_id );
			$existing_offer = null;
		}
	}

	if ( $existing_offer ) {
		$product_id = (int) $existing_offer->product_id;
	} else {
		// 3. Cross-store matching (brand-gated). Unirea EXACTĂ din același magazin
		// e mereu permisă: două rânduri cu același model din același magazin sunt
		// variante (culori) ale aceluiași produs — le unim într-un singur produs și
		// păstrăm oferta suplimentară ca variantă (vezi mai jos), ca să nu mai apară
		// produse „duplicat" cu titlu identic. Fuzzy same-store rămâne blocat.
		$key              = hainute_match_key( $item['brand'] ?? '', $item['name'] );
		$near_misses      = array();
		$allow_same_store = true;
		$product_id       = hainute_find_matching_product( $key, $item['brand'] ?? '', $store_id, $allow_same_store, $near_misses );

		foreach ( $near_misses as $miss ) {
			$summary['notes'][] = sprintf(
				'Aproape-match (%s%%): "%s" vs produs #%d ("%s") — tratat ca produs separat.',
				$miss['similarity'],
				$miss['key'],
				$miss['product_id'],
				$miss['existing_key']
			);
		}

		if ( $product_id ) {
			$summary['matched']++;
		} else {
			if ( $max_new > 0 && $summary['created'] >= $max_new ) {
				$summary['skipped_new']++;
				return; // deferred: created on a future run
			}
			$product_id = hainute_create_product_from_item( $item, $key );
			$summary['created']++;
		}
	}

	// 4. Ofertă primară vs. variantă same-store.
	// Un magazin are O SINGURĂ ofertă primară per produs (product_id, store_id).
	// Dacă magazinul are deja o ofertă primară cu ALT external_id, rândul curent e
	// o variantă same-store (altă culoare, fără etichetă în feed) → o păstrăm în
	// meta _hainute_variant_offers (cu linkul și poza ei), fără să suprascriem
	// oferta primară. Așa nu mai apar produse duplicate și nu pierdem niciun link.
	$primary = hainute_get_offer_for_store( $product_id, $store_id );

	if ( $primary && $primary->external_id !== $item['external_id'] ) {
		hainute_upsert_variant_offer( $product_id, $store_id, $item );
	} else {
		$ok = hainute_upsert_offer(
			$product_id,
			$store_id,
			array(
				'network'       => $item['network'],
				'external_id'   => $item['external_id'],
				'price'         => (float) $item['price'],
				'old_price'     => isset( $item['old_price'] ) && $item['old_price'] ? (float) $item['old_price'] : null,
				'currency'      => $item['currency'] ?? 'RON',
				'stock_status'  => ! empty( $item['in_stock'] ) ? HAINUTE_STOCK_IN : HAINUTE_STOCK_OUT,
				'stock_qty'     => isset( $item['stock_qty'] ) && null !== $item['stock_qty'] ? (int) $item['stock_qty'] : null,
				'affiliate_url' => $item['url'],
			)
		);

		if ( ! $ok ) {
			throw new Exception( 'upsert ofertă eșuat' );
		}
	}

	// Images — hotlinked from the merchant (aggregator pattern): store the feed
	// URLs and display them directly. No download, so imports stay fast, avoid
	// avif/webp processing failures, and images always reflect the merchant.
	// Refreshed each run so a changed feed image updates on site.
	// DOAR din oferta PRIMARĂ: altfel o variantă same-store (altă culoare) ar
	// suprascrie poza principală cu poza ei → prima culoare ar arăta poza alteia.
	$is_variant_row = ( $primary && $primary->external_id !== $item['external_id'] );
	if ( ! $is_variant_row && ! empty( $item['images'] ) ) {
		$urls = array_values( array_filter( array_map( 'hainute_resolve_feed_image_url', $item['images'] ) ) );
		if ( ! empty( $urls ) ) {
			update_post_meta( $product_id, '_hainute_image_url', $urls[0] );
			if ( count( $urls ) > 1 ) {
				update_post_meta( $product_id, '_hainute_gallery', array_slice( $urls, 1 ) );
			}
		}
	}

	// Variații — fiecare rând cu același external_id (grup) e o variantă. Adunăm:
	//  - CODURILE din part_number (culoare/mărime) → numărare sigură, fără titlu;
	//  - ETICHETELE din titlu când există (culoare, „3 luni") + dicționar învățat.
	if ( ! empty( $item['color'] ) ) {
		hainute_add_list_meta( $product_id, '_hainute_colors', $item['color'] );
	}
	if ( ! empty( $item['color_code'] ) ) {
		hainute_add_list_meta( $product_id, '_hainute_color_codes', $item['color_code'] );
	}
	if ( ! empty( $item['size_code'] ) ) {
		hainute_add_list_meta( $product_id, '_hainute_size_codes', $item['size_code'] );
		// Dicționar învățat: dacă avem și eticheta (din titlu), o legăm de cod
		// global și o folosim la toate produsele cu același cod.
		if ( ! empty( $item['size'] ) ) {
			hainute_learn_size_label( $item['size_code'], $item['size'] );
		}
	}
	if ( ! empty( $item['size'] ) ) {
		hainute_add_list_meta( $product_id, '_hainute_sizes', $item['size'] );
	}
	if ( ! empty( $item['sizes'] ) ) {
		foreach ( array_map( 'trim', explode( ',', (string) $item['sizes'] ) ) as $sz ) {
			hainute_add_list_meta( $product_id, '_hainute_sizes', $sz );
		}
	}

	$summary['offers']++;
}

/**
 * Dicționar global cod-mărime → etichetă, învățat din titlurile care conțin
 * mărimea. Codurile de mărime sunt globale (aceeași mărime = același cod la
 * produse diferite), deci ce învățăm dintr-un produs se aplică la toate.
 */
function hainute_learn_size_label( $code, $label ) {
	$code  = trim( (string) $code );
	$label = trim( (string) $label );
	if ( '' === $code || '' === $label ) {
		return;
	}
	$dict = get_option( 'hainute_size_dict', array() );
	if ( ! isset( $dict[ $code ] ) ) {
		$dict[ $code ] = $label;
		update_option( 'hainute_size_dict', $dict, false );
	}
}

/**
 * Rezolvă etichetele de mărime pentru un produs: pentru fiecare cod stocat,
 * caută eticheta în dicționarul învățat; combină cu etichetele explicite.
 *
 * @return array { count: int, labels: string[] }
 */
function hainute_resolve_sizes( $product_id ) {
	// Mărimile crawluite din pagina magazinului (Answear) sunt LIZIBILE și
	// autoritative (lista de mărimi disponibile) → au prioritate.
	$avail = get_post_meta( $product_id, '_hainute_sizes_available', true );
	if ( is_array( $avail ) && ! empty( $avail ) ) {
		return array( 'count' => count( $avail ), 'labels' => array_values( $avail ) );
	}

	// DOAR mărimi LIZIBILE (din titlu/URL, ex. „26 EU"). Dicționarul de coduri
	// s-a dovedit nesigur (același cod → mărimi diferite pe produse diferite, ex.
	// „49" pe o sandală de copil) → NU-l mai folosim. Mai bine nicio mărime decât
	// una inventată. Mărimile corecte vin din crawl (Answear) sau URL (FD footwear).
	$labels = (string) get_post_meta( $product_id, '_hainute_sizes', true );
	$labels = '' !== $labels ? array_values( array_unique( array_filter( array_map( 'trim', explode( ',', $labels ) ) ) ) ) : array();

	return array( 'count' => count( $labels ), 'labels' => $labels );
}

/**
 * Stochează o variantă same-store (altă culoare a aceluiași model din același
 * magazin) în meta _hainute_variant_offers — un array indexat după external_id,
 * fiecare intrare cu linkul afiliat, poza, prețul și stocul ei. Idempotent:
 * re-rularea sync-ului actualizează intrarea, nu o dublează.
 */
function hainute_upsert_variant_offer( $product_id, $store_id, array $item ) {
	$variants = get_post_meta( $product_id, '_hainute_variant_offers', true );
	if ( ! is_array( $variants ) ) {
		$variants = array();
	}

	$image = '';
	if ( ! empty( $item['images'] ) ) {
		$urls  = array_values( array_filter( array_map( 'hainute_resolve_feed_image_url', (array) $item['images'] ) ) );
		$image = $urls[0] ?? '';
	}

	$variants[ (string) $item['external_id'] ] = array(
		'store_id'  => (int) $store_id,
		'url'       => (string) $item['url'],
		'image'     => $image,
		'price'     => (float) $item['price'],
		'old_price' => isset( $item['old_price'] ) && $item['old_price'] ? (float) $item['old_price'] : null,
		'currency'  => $item['currency'] ?? 'RON',
		'in_stock'  => ! empty( $item['in_stock'] ),
		'color'     => (string) ( $item['color'] ?? '' ),
	);

	update_post_meta( $product_id, '_hainute_variant_offers', $variants );

	// Prețul minim al produsului trebuie să țină cont și de variante.
	$current_min = (float) get_post_meta( $product_id, '_hainute_min_price', true );
	if ( ! empty( $item['in_stock'] ) && ( $current_min <= 0 || (float) $item['price'] < $current_min ) ) {
		update_post_meta( $product_id, '_hainute_min_price', (float) $item['price'] );
	}
}

/**
 * Adaugă o valoare într-un meta de tip listă (comma-separated), deduplicat
 * case-insensitive. Folosit pentru culori/mărimi acumulate din variante.
 */
function hainute_add_list_meta( $post_id, $meta_key, $value ) {
	$value = trim( (string) $value );
	if ( '' === $value ) {
		return;
	}
	$current = (string) get_post_meta( $post_id, $meta_key, true );
	$list    = '' !== $current ? array_map( 'trim', explode( ',', $current ) ) : array();

	foreach ( $list as $existing ) {
		if ( 0 === strcasecmp( $existing, $value ) ) {
			return; // deja prezent
		}
	}
	$list[] = $value;
	update_post_meta( $post_id, $meta_key, implode( ', ', $list ) );
}

/**
 * Create the aggregated product post from a feed item.
 *
 * @param array  $item Normalized item.
 * @param string $key  Match key (stored as meta for future matching).
 * @return int New post ID.
 */
function hainute_create_product_from_item( array $item, $key ) {
	$post_id = wp_insert_post(
		array(
			'post_type'    => 'product',
			'post_status'  => 'publish',
			'post_title'   => $item['name'],
			'post_content' => $item['description'] ?? '',
			'post_excerpt' => wp_trim_words( wp_strip_all_tags( $item['description'] ?? '' ), 30 ),
		),
		true
	);

	if ( is_wp_error( $post_id ) ) {
		throw new Exception( $post_id->get_error_message() );
	}

	update_post_meta( $post_id, HAINUTE_MATCH_META_KEY, $key );
	update_post_meta( $post_id, HAINUTE_MATCH_META_BRAND, hainute_norm_brand( $item['brand'] ?? '' ) );

	if ( ! empty( $item['material'] ) ) {
		update_post_meta( $post_id, '_hainute_material', sanitize_text_field( $item['material'] ) );
	}
	if ( ! empty( $item['sizes'] ) ) {
		update_post_meta( $post_id, '_hainute_sizes', sanitize_text_field( $item['sizes'] ) );
	}

	$tax_map = array(
		'product_cat'    => 'category',
		'product_brand'  => 'brand',
		'product_gender' => 'gender',
		'product_age'    => 'age',
	);
	foreach ( $tax_map as $taxonomy => $field ) {
		if ( ! empty( $item[ $field ] ) ) {
			wp_set_object_terms( $post_id, $item[ $field ], $taxonomy );
		}
	}

	return $post_id;
}

/**
 * Resolve a feed image reference to a browser-usable URL.
 * Mock feeds use paths relative to the plugin's mock-feeds/ folder;
 * real feeds use absolute http(s) URLs.
 */
function hainute_resolve_feed_image_url( $image ) {
	if ( preg_match( '#^https?://#i', $image ) ) {
		return $image;
	}
	return HAINUTE_CORE_URL . 'mock-feeds/' . ltrim( $image, '/' );
}

/**
 * Set the featured image from a feed reference — remote URL or a local
 * mock-feed file. Failures are non-fatal: a product without a photo is
 * better than a lost product.
 */
function hainute_sideload_featured_image( $post_id, $image ) {
	if ( empty( $image ) ) {
		return;
	}

	require_once ABSPATH . 'wp-admin/includes/media.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/image.php';

	if ( preg_match( '#^https?://#i', $image ) ) {
		$attachment_id = media_sideload_image( $image, $post_id, null, 'id' );
	} else {
		// Local mock image: copy it into the media library.
		$path = HAINUTE_CORE_DIR . 'mock-feeds/' . ltrim( $image, '/' );
		if ( ! file_exists( $path ) ) {
			return;
		}

		$tmp = wp_tempnam( basename( $path ) );
		copy( $path, $tmp );

		$attachment_id = media_handle_sideload(
			array( 'name' => basename( $path ), 'tmp_name' => $tmp ),
			$post_id
		);

		if ( is_wp_error( $attachment_id ) ) {
			@unlink( $tmp );
		}
	}

	if ( ! is_wp_error( $attachment_id ) ) {
		set_post_thumbnail( $post_id, $attachment_id );
	}
}
