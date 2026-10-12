<?php
/**
 * Reusable display helpers.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Human label + CSS class for a stock status.
 *
 * @param string $status in_stock | low_stock | out_of_stock.
 * @return array { label, class }
 */
function hainute_stock_badge( $status ) {
	switch ( $status ) {
		case 'low_stock':
			return array( 'label' => __( 'Stoc critic', 'hainute' ), 'class' => 'stock-low' );
		case 'out_of_stock':
			return array( 'label' => __( 'Indisponibil', 'hainute' ), 'class' => 'stock-out' );
		default:
			return array( 'label' => __( 'Disponibil', 'hainute' ), 'class' => 'stock-in' );
	}
}

/**
 * Format a price for display.
 */
function hainute_format_price( $price, $currency = 'RON' ) {
	$formatted = number_format( (float) $price, 2, ',', '.' );
	$suffix    = 'RON' === $currency ? 'lei' : $currency;
	return $formatted . '&nbsp;' . esc_html( $suffix );
}

/**
 * First brand term name for a product, or ''.
 */
function hainute_get_brand( $product_id ) {
	$terms = get_the_terms( $product_id, 'product_brand' );
	return ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '';
}

/**
 * Price block for the product page: best price + old price + discount badge,
 * based on the cheapest in-stock offer.
 */
function hainute_the_price_block( $product_id ) {
	$sum = hainute_offer_summary( $product_id );
	if ( ! $sum['best'] ) {
		return;
	}
	$best = $sum['best'];

	// Prețul e informație secundară (site-ul arată unde e mărimea pe stoc):
	// mic, fără preț tăiat și fără procent de reducere.
	echo '<div class="price-block">';
	echo '<span class="price-from">' . esc_html( $sum['stores'] > 1 ? __( 'Preț în magazine de la', 'hainute' ) : __( 'Preț în magazin', 'hainute' ) ) . '</span> ';
	echo '<span class="price-current">' . hainute_format_price( $best->price, $best->currency ) . '</span>';
	echo '</div>';

	// Rezumat imediat sub preț: unde se găsește + salt direct la magazine.
	echo '<p class="price-summary">';
	if ( $sum['stores'] > 1 ) {
		echo esc_html( 'Disponibil în ' . hainute_ro_count( $sum['stores'], 'magazin', 'magazine' ) ) . ' · ';
		echo '<a href="#magazine" class="jump-offers">' . esc_html__( 'Vezi mărimile disponibile', 'hainute' ) . ' &darr;</a>';
	} elseif ( $sum['stores'] === 1 ) {
		echo esc_html( sprintf( __( 'Disponibil la %s', 'hainute' ), $sum['store_name'] ) ) . ' · ';
		echo '<a href="#magazine" class="jump-offers">' . esc_html__( 'Vezi mărimile disponibile', 'hainute' ) . ' &darr;</a>';
	} else {
		esc_html_e( 'Momentan indisponibil', 'hainute' );
	}
	echo '</p>';
}

/**
 * Cel mai mic preț cu stoc + numărul de magazine cu stoc, din ofertele AFIȘATE
 * (fără magazine ascunse și fără oferte externe expirate / verificate ca alt produs).
 * @return array{best:?object,stores:int,store_name:string}
 */
function hainute_offer_summary( $product_id ) {
	static $cache = array();
	if ( isset( $cache[ $product_id ] ) ) {
		return $cache[ $product_id ];
	}
	$hidden = get_post_meta( $product_id, '_hainute_hidden_stores', true );
	$hidden = is_array( $hidden ) ? array_map( 'intval', $hidden ) : array();
	$best   = null;
	$any    = null;
	$stores = array();
	foreach ( function_exists( 'hainute_get_offers' ) ? hainute_get_offers( $product_id ) : array() as $o ) {
		if ( in_array( (int) $o->store_id, $hidden, true ) || (float) $o->price <= 0 ) {
			continue;
		}
		if ( function_exists( 'hainute_offer_is_stale' ) && hainute_offer_is_stale( $product_id, $o ) ) {
			continue;
		}
		$any = $any ? $any : $o;
		if ( 'out_of_stock' === $o->stock_status ) {
			continue;
		}
		$stores[ (int) $o->store_id ] = $o->store ? $o->store->name : '';
		if ( ! $best || (float) $o->price < (float) $best->price ) {
			$best = $o;
		}
	}
	// Variantele de culoare cu stoc (aceeași pagină de produs, altă culoare) contează
	// și ele: produsul se poate cumpăra chiar dacă culoarea principală e epuizată.
	$variants = get_post_meta( $product_id, '_hainute_variant_offers', true );
	foreach ( is_array( $variants ) ? $variants : array() as $v ) {
		$sid = (int) ( $v['store_id'] ?? 0 );
		$pr  = (float) ( $v['price'] ?? 0 );
		if ( empty( $v['in_stock'] ) || $pr <= 0 || in_array( $sid, $hidden, true ) ) {
			continue;
		}
		$st = $sid && function_exists( 'hainute_get_store' ) ? hainute_get_store( $sid ) : null;
		$stores[ $sid ] = $stores[ $sid ] ?? ( $st ? $st->name : '' );
		if ( ! $best || $pr < (float) $best->price ) {
			$best = (object) array( 'price' => $pr, 'old_price' => 0, 'currency' => (string) ( $v['currency'] ?? 'RON' ), 'store' => $st, 'store_id' => $sid, 'stock_status' => 'in_stock' );
		}
	}
	$cache[ $product_id ] = array(
		'best'       => $best ? $best : $any,
		'stores'     => count( $stores ),
		'store_name' => $stores ? reset( $stores ) : '',
	);
	return $cache[ $product_id ];
}

/** Bară fixă jos pe mobil: prețul minim + salt la magazine (apare la scroll). */
function hainute_the_sticky_cta( $product_id ) {
	$sum = hainute_offer_summary( $product_id );
	if ( ! $sum['best'] || ! $sum['stores'] ) {
		return;
	}
	echo '<div class="sticky-cta" data-sticky-cta aria-hidden="true">';
	echo '<div class="sticky-cta-text"><strong>' . ( $sum['stores'] > 1 ? esc_html__( 'de la', 'hainute' ) . ' ' : '' ) . hainute_format_price( $sum['best']->price, $sum['best']->currency ) . '</strong>';
	echo '<span>' . esc_html( $sum['stores'] > 1 ? 'în ' . hainute_ro_count( $sum['stores'], 'magazin', 'magazine' ) : $sum['store_name'] ) . '</span></div>';
	echo '<a href="#magazine" class="btn btn-primary sticky-cta-btn" tabindex="-1">' . esc_html__( 'Vezi mărimile disponibile', 'hainute' ) . '</a>';
	echo '</div>';
}

/**
 * Internal links: alte produse de la ACELAȘI brand (aceeași categorie prioritar).
 * Sub descriere → navigare + SEO (internal linking pe brand).
 */
function hainute_the_brand_links( $product_id ) {
	$brand = function_exists( 'hainute_get_brand' ) ? hainute_get_brand( $product_id ) : '';
	if ( '' === $brand ) {
		return;
	}
	$cats = get_the_terms( $product_id, 'product_cat' );
	$base = array(
		'post_type'      => 'product',
		'post_status'    => 'publish',
		'posts_per_page' => 4,
		'post__not_in'   => array( $product_id ),
		'orderby'        => 'rand',
		'fields'         => 'ids',
		'no_found_rows'  => true,
	);
	$brand_tq = array( 'taxonomy' => 'product_brand', 'field' => 'name', 'terms' => $brand );

	$ids = array();
	// Întâi același brand + aceeași categorie.
	if ( $cats && ! is_wp_error( $cats ) ) {
		$ids = get_posts( $base + array( 'tax_query' => array( 'relation' => 'AND', $brand_tq, array( 'taxonomy' => 'product_cat', 'field' => 'term_id', 'terms' => wp_list_pluck( $cats, 'term_id' ) ) ) ) );
	}
	// Completează cu același brand (orice categorie).
	if ( count( $ids ) < 4 ) {
		$more = get_posts( $base + array( 'post__not_in' => array_merge( array( $product_id ), $ids ), 'tax_query' => array( $brand_tq ) ) );
		$ids  = array_slice( array_merge( $ids, $more ), 0, 4 );
	}
	if ( empty( $ids ) ) {
		return;
	}

	echo '<p class="brand-links">' . esc_html( sprintf( __( 'Vezi și alte produse %s pentru copii:', 'hainute' ), $brand ) ) . ' ';
	$parts = array();
	foreach ( $ids as $id ) {
		$parts[] = '<a href="' . esc_url( get_permalink( $id ) ) . '">' . esc_html( get_the_title( $id ) ) . '</a>';
	}
	echo wp_kses_post( implode( ', ', $parts ) ) . '.</p>';
}

/**
 * Etichetă „acum X" în română (relativ, scurt).
 */
function hainute_ago_ro( $ts ) {
	$d = time() - (int) $ts;
	if ( $d < 90 ) {
		return __( 'chiar acum', 'hainute' );
	}
	if ( $d < 3600 ) {
		return 'acum ' . hainute_ro_count( max( 1, (int) round( $d / 60 ) ), 'minut', 'minute' );
	}
	if ( $d < 86400 ) {
		return 'acum ' . hainute_ro_count( (int) round( $d / 3600 ), 'oră', 'ore' );
	}
	return 'acum ' . hainute_ro_count( (int) round( $d / 86400 ), 'zi', 'zile' );
}

/**
 * Numeral + substantiv în română: „1 zi", „5 zile", „20 de zile", „101 zile".
 * „de" apare la 0 și când ultimele două cifre sunt 00 sau ≥ 20.
 */
function hainute_ro_count( $n, $singular, $plural ) {
	$n = (int) $n;
	if ( 1 === $n ) {
		return '1 ' . $singular;
	}
	$r = $n % 100;
	return $n . ( ( 0 === $r || $r >= 20 ) ? ' de ' : ' ' ) . $plural;
}

/**
 * Dovadă socială: „X persoane se uită la acest produs acum". Dummy realist la
 * început (nu exagerat, variază puțin la refresh), înlocuit de datele reale când
 * crește audiența — vezi hainute_viewers_now() în plugin.
 */
function hainute_the_social_proof( $product_id ) {
	if ( ! function_exists( 'hainute_viewers_now' ) ) {
		return;
	}
	// Vizualizări reale ale paginii în ultimele 15 minute (afișate de la 3 în sus).
	$n = (int) hainute_viewers_now( $product_id );
	if ( $n < 3 ) {
		return;
	}
	echo '<p class="social-proof" aria-live="polite">';
	echo '<span class="social-proof-dot" aria-hidden="true"></span>';
	echo esc_html( hainute_ro_count( $n, 'vizualizare', 'vizualizări' ) . ' în ultimele 15 minute' );
	echo '</p>';
}

/**
 * Fâșie de „prospețime": când a fost verificată ultima dată disponibilitatea +
 * disclaimer discret că stocul se poate schimba. Elementul-cheie de încredere:
 * arătăm clar cât de proaspete sunt datele.
 */
function hainute_the_freshness( $product_id ) {
	$checked = function_exists( 'hainute_stock_checked_time' ) ? hainute_stock_checked_time( $product_id ) : 0;

	// Afișăm „verificat acum X" doar când e proaspăt (≤ 3 zile). O dată veche
	// („acum 43 de zile") ar scădea încrederea; atunci rămâne doar nota de stoc.
	$fresh = $checked > 0 && ( time() - $checked ) <= 3 * DAY_IN_SECONDS;

	echo '<div class="freshness">';
	if ( $fresh ) {
		echo '<span class="freshness-live"><span class="freshness-dot" aria-hidden="true"></span>';
		echo esc_html__( 'Disponibilitate verificată', 'hainute' ) . ' <strong>' . esc_html( hainute_ago_ro( $checked ) ) . '</strong>';
		echo '</span>';
	}
	echo '<span class="freshness-note">' . esc_html__( 'Stocul se poate schimba rapid, așa că verifică pe site-ul magazinului înainte de comandă.', 'hainute' ) . '</span>';
	echo '</div>';
}

/**
 * Sizes — chips with labels when known (from title / learned dictionary),
 * otherwise a reliable count derived from the part_number size codes.
 */
function hainute_the_sizes( $product_id ) {
	// Prefer the code-aware resolver (plugin); fall back to raw meta.
	if ( function_exists( 'hainute_resolve_sizes' ) ) {
		$data   = hainute_resolve_sizes( $product_id );
		$count  = (int) $data['count'];
		$labels = $data['labels'];
	} else {
		$raw    = (string) get_post_meta( $product_id, '_hainute_sizes', true );
		$labels = '' !== $raw ? array_filter( array_map( 'trim', explode( ',', $raw ) ) ) : array();
		$count  = count( $labels );
	}

	if ( $count < 1 && empty( $labels ) ) {
		return;
	}

	echo '<div class="product-sizes" data-size-display>';
	echo '<h2 class="section-label">' . esc_html__( 'Mărimi disponibile', 'hainute' ) . '</h2>';

	if ( ! empty( $labels ) ) {
		echo '<ul class="size-chips" data-size-chips>';
		foreach ( $labels as $size ) {
			echo '<li class="size-chip">' . esc_html( $size ) . '</li>';
		}
		echo '</ul>';
		// Dacă avem mai multe coduri decât etichete, spune câte în total.
		if ( $count > count( $labels ) ) {
			echo '<p class="variation-note">' . esc_html( hainute_ro_count( $count, 'mărime', 'mărimi' ) . ' în total' ) . '</p>';
		}
	} else {
		echo '<p class="variation-count">' . esc_html( hainute_ro_count( $count, 'mărime disponibilă', 'mărimi disponibile' ) ) . '</p>';
	}

	echo '</div>';
}

/**
 * Colors — chips with names when known (from title), otherwise a count
 * derived from the part_number colour codes.
 */
function hainute_the_colors( $product_id ) {
	// Dacă există selector de variante (swatch-uri cu poze), acela e UI-ul de
	// culoare → nu mai dublăm cu chips simple.
	$variants = get_post_meta( $product_id, '_hainute_variant_offers', true );
	if ( is_array( $variants ) && ! empty( $variants ) ) {
		return;
	}

	$labels = (string) get_post_meta( $product_id, '_hainute_colors', true );
	$labels = '' !== $labels ? array_filter( array_map( 'trim', explode( ',', $labels ) ) ) : array();

	$codes = (string) get_post_meta( $product_id, '_hainute_color_codes', true );
	$codes = '' !== $codes ? array_filter( array_map( 'trim', explode( ',', $codes ) ) ) : array();
	$count = ! empty( $codes ) ? count( $codes ) : count( $labels );

	if ( $count < 1 && empty( $labels ) ) {
		return;
	}

	echo '<div class="product-colors">';
	echo '<h2 class="section-label">' . esc_html__( 'Culori disponibile', 'hainute' ) . '</h2>';

	if ( ! empty( $labels ) ) {
		echo '<ul class="size-chips">';
		foreach ( $labels as $color ) {
			echo '<li class="size-chip">' . esc_html( $color ) . '</li>';
		}
		echo '</ul>';
		if ( $count > count( $labels ) ) {
			echo '<p class="variation-note">' . esc_html( hainute_ro_count( $count, 'culoare', 'culori' ) . ' în total' ) . '</p>';
		}
	} else {
		echo '<p class="variation-count">' . esc_html( hainute_ro_count( $count, 'culoare disponibilă', 'culori disponibile' ) ) . '</p>';
	}

	echo '</div>';
}

/**
 * Set CANONIC de specificații — aceeași ordine la toate produsele, ca tabelul și
 * structured data (schema) să fie consistente (nu 6 câmpuri la unul, 9 la altul).
 * Returnează [label => value], doar câmpurile cu valoare. Genul se derivă din
 * nivelul 1 al categoriei (Fete/Băieți/Bebe) dacă taxonomia product_gender e goală.
 */
function hainute_product_specs( $product_id ) {
	$out   = array();
	$specs = get_post_meta( $product_id, '_hainute_specs', true );
	$specs = is_array( $specs ) ? $specs : array();

	$brand = hainute_get_brand( $product_id );
	if ( $brand ) {
		$out['Brand'] = $brand;
	}
	if ( ! empty( $specs['Model'] ) ) {
		$out['Model'] = $specs['Model'];
	}
	$material = ! empty( $specs['Material'] ) ? $specs['Material'] : get_post_meta( $product_id, '_hainute_material', true );
	if ( $material ) {
		$out['Material'] = $material;
	}
	if ( ! empty( $specs['Caracteristici'] ) ) {
		$out['Caracteristici'] = $specs['Caracteristici'];
	}

	// Categorie (frunza) + Gen (nivel 1) — mereu prezente pentru consistență.
	$cats = get_the_terms( $product_id, 'product_cat' );
	if ( $cats && ! is_wp_error( $cats ) ) {
		$leaf = $cats[0];
		foreach ( $cats as $c ) {
			if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
				$leaf = $c;
			}
		}
		$out['Categorie'] = $leaf->name;
		$anc              = get_ancestors( $leaf->term_id, 'product_cat' );
		$top              = $anc ? get_term( end( $anc ), 'product_cat' ) : $leaf;
		if ( $top && ! is_wp_error( $top ) ) {
			$out['Gen'] = $top->name;
		}
	}
	$gt = get_the_terms( $product_id, 'product_gender' );
	if ( $gt && ! is_wp_error( $gt ) ) {
		$out['Gen'] = $gt[0]->name;
	}
	if ( ! empty( $specs['Cod produs'] ) ) {
		$out['Cod produs'] = $specs['Cod produs'];
	}
	return $out;
}

/**
 * Tabelul de specificații tehnice (SEO-friendly, consistent cu structured data).
 */
function hainute_the_specs( $product_id ) {
	$rows = hainute_product_specs( $product_id );

	if ( empty( $rows ) ) {
		return;
	}

	echo '<div class="product-specs">';
	echo '<h2 class="section-label">' . esc_html__( 'Specificații tehnice', 'hainute' ) . '</h2>';
	echo '<table class="specs-table"><tbody>';
	foreach ( $rows as $label => $value ) {
		echo '<tr><th>' . esc_html( $label ) . '</th><td>' . esc_html( $value ) . '</td></tr>';
	}
	echo '</tbody></table>';
	echo '</div>';
}

/** GTIN valid (8/12/13/14 cifre + cifră de control corectă) sau ''. */
function hainute_valid_gtin( $code ) {
	$code = preg_replace( '/\D/', '', (string) $code );
	$len  = strlen( $code );
	if ( ! in_array( $len, array( 8, 12, 13, 14 ), true ) || ! (int) ltrim( $code, '0' ) ) {
		return '';
	}
	$sum = 0;
	for ( $i = $len - 2, $w = 3; $i >= 0; $i--, $w = 4 - $w ) {
		$sum += (int) $code[ $i ] * $w;
	}
	return ( ( 10 - $sum % 10 ) % 10 ) === (int) $code[ $len - 1 ] ? $code : '';
}

/**
 * Schema.org (JSON-LD): ProductGroup cu o variantă per mărime (variesBy size),
 * fiecare cu ofertele magazinelor (seller = magazinul) și stocul acelei mărimi;
 * fără mărimi cunoscute → Product cu câte o ofertă per magazin. Google cere ca datele să corespundă
 * cu ce vede vizitatorul, așa că pornim din aceleași oferte principale ca prețul
 * afișat („de la X" = cea mai mică ofertă cu stoc), fără magazinele ascunse.
 * Identificatori reali doar: GTIN (EAN din feed, validat) și codul producătorului.
 */
function hainute_the_product_schema( $product_id ) {
	if ( ! function_exists( 'hainute_get_offers' ) ) {
		return;
	}
	$hidden = get_post_meta( $product_id, '_hainute_hidden_stores', true );
	$hidden = is_array( $hidden ) ? array_map( 'intval', $hidden ) : array();

	// O ofertă per magazin (oferta principală a magazinului, ca în matrice).
	$by_store = array();
	foreach ( hainute_get_offers( $product_id ) as $o ) {
		$store = $o->store ? $o->store->name : '';
		if ( (float) $o->price <= 0 || '' === $store || in_array( (int) $o->store_id, $hidden, true ) ) {
			continue;
		}
		if ( function_exists( 'hainute_offer_is_stale' ) && hainute_offer_is_stale( $product_id, $o ) ) {
			continue;
		}
		$by_store[ $store ] = array(
			'price'    => (float) $o->price,
			'in_stock' => 'out_of_stock' !== $o->stock_status,
		);
	}
	if ( ! $by_store ) {
		return;
	}
	// Intervalul de preț = cel afișat: doar ofertele cu stoc (dacă există vreuna).
	$in_stock = array_filter( $by_store, function ( $l ) { return $l['in_stock']; } );
	$prices   = array_column( $in_stock ? $in_stock : $by_store, 'price' );

	$schema = array(
		'@context' => 'https://schema.org',
		'@type'    => 'Product',
		'@id'      => get_permalink( $product_id ) . '#product',
		'name'     => wp_strip_all_tags( get_the_title( $product_id ) ),
		'url'      => get_permalink( $product_id ),
	);

	// Toate pozele din galerie (Google alege; mai multe unghiuri = eligibil Images).
	$images = array_filter( array_merge( array( hainute_product_image( $product_id, 'large' ) ), (array) get_post_meta( $product_id, '_hainute_gallery', true ) ) );
	if ( $images ) {
		$schema['image'] = array_values( array_unique( array_map( 'strval', $images ) ) );
	}

	// Descrierea fără blocul de navigare internă („Vezi mai multe: ...").
	$content = (string) get_post_field( 'post_content', $product_id );
	$content = preg_replace( '#<p[^>]*class="[^"]*product-interlinks[^"]*"[^>]*>.*?</p>#s', '', $content );
	$desc    = trim( preg_replace( '/\s+/', ' ', wp_strip_all_tags( $content ) ) );
	if ( $desc ) {
		$schema['description'] = mb_strlen( $desc ) > 700 ? rtrim( mb_substr( $desc, 0, 697 ) ) . '…' : $desc;
	}

	$brand = hainute_get_brand( $product_id );
	if ( $brand ) {
		$schema['brand'] = array( '@type' => 'Brand', 'name' => $brand );
	}

	// GTIN: EAN-ul real vine în external_id-ul ofertei CJ (Answear: „{advertiser}:{ean}").
	if ( function_exists( 'hainute_get_offers' ) ) {
		foreach ( hainute_get_offers( $product_id ) as $o ) {
			$parts = explode( ':', (string) $o->external_id );
			$gtin  = 'cj' === $o->network ? hainute_valid_gtin( end( $parts ) ) : '';
			if ( $gtin ) {
				$schema['gtin'] = $gtin;
				break;
			}
		}
	}
	// Codul producătorului (ex. Geox B6563A): primul segment al codului de model.
	$model = (string) get_post_meta( $product_id, '_hainute_model_code', true );
	$mpn   = $model ? strtok( $model, '.' ) : '';
	if ( $mpn && preg_match( '/^(?=.*\d)[A-Z0-9-]{4,20}$/i', $mpn ) ) {
		$schema['mpn'] = strtoupper( $mpn );
	}

	$specs = hainute_product_specs( $product_id );
	if ( ! empty( $specs['Material'] ) ) {
		$schema['material'] = $specs['Material'];
	}
	$colors = array_filter( array_map( 'trim', explode( ',', (string) get_post_meta( $product_id, '_hainute_colors', true ) ) ) );
	if ( 1 === count( $colors ) ) {
		$schema['color'] = reset( $colors ); // mai multe culori = variante, nu o proprietate
	}
	$sizes = function_exists( 'hainute_resolve_sizes' ) ? hainute_resolve_sizes( $product_id )['labels'] : array();
	if ( $sizes ) {
		$schema['size'] = array_values( $sizes );
	}

	// Categoria completă + publicul (gen/vârstă) din arborele de categorii.
	$cats = get_the_terms( $product_id, 'product_cat' );
	if ( $cats && ! is_wp_error( $cats ) ) {
		$leaf = $cats[0];
		foreach ( $cats as $c ) {
			if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
				$leaf = $c;
			}
		}
		$chain = array_reverse( get_ancestors( $leaf->term_id, 'product_cat' ) );
		$names = array_map( function ( $id ) { return get_term( $id, 'product_cat' )->name; }, $chain );
		$names[] = $leaf->name;
		$schema['category'] = implode( ' > ', $names );

		$top    = mb_strtolower( $names[0] );
		$gender = array( 'fete' => 'female', 'băieți' => 'male', 'baieti' => 'male' );
		$aud    = array( '@type' => 'PeopleAudience' );
		if ( isset( $gender[ $top ] ) ) {
			$aud['suggestedGender'] = $gender[ $top ];
		} elseif ( 'bebe' === $top ) {
			$aud['suggestedGender'] = 'unisex';
			$aud['suggestedMaxAge'] = 3;
		}
		if ( count( $aud ) > 1 ) {
			$schema['audience'] = $aud;
		}
	}

	// Ofertele listate = cele cumpărabile acum (ca intervalul de preț să fie coerent
	// cu ele); fără stoc nicăieri → le listăm pe toate, marcate OutOfStock.
	$offer_items = array();
	foreach ( ( $in_stock ? $in_stock : $by_store ) as $store => $l ) {
		$offer_items[] = array(
			'@type'         => 'Offer',
			'price'         => round( $l['price'], 2 ),
			'priceCurrency' => 'RON',
			'availability'  => $l['in_stock'] ? 'https://schema.org/InStock' : 'https://schema.org/OutOfStock',
			'itemCondition' => 'https://schema.org/NewCondition',
			'seller'        => array( '@type' => 'Organization', 'name' => $store ),
		);
	}
	// Ofertele direct (câte una per magazin), fără AggregateOffer cu interval de
	// preț: pagina e despre unde găsești mărimea, nu despre preț.
	$schema['offers'] = $offer_items;

	// Cu mărimi cunoscute → ProductGroup: o variantă per mărime, fiecare cu
	// ofertele magazinelor care o au (InStock) sau au epuizat-o (OutOfStock).
	$variants = hainute_schema_size_variants( $product_id, $schema['name'], $by_store );
	if ( $variants ) {
		unset( $schema['offers'], $schema['size'], $schema['gtin'] );
		$schema['@type']          = 'ProductGroup';
		$schema['productGroupID'] = ! empty( $schema['mpn'] ) ? $schema['mpn'] : (string) $product_id;
		$schema['variesBy']       = array( 'https://schema.org/size' );
		$schema['hasVariant']     = $variants;
	}

	// Restul specificațiilor (cele care n-au proprietate dedicată mai sus).
	$props = array();
	foreach ( $specs as $label => $value ) {
		if ( in_array( $label, array( 'Brand', 'Material', 'Categorie' ), true ) ) {
			continue;
		}
		$props[] = array( '@type' => 'PropertyValue', 'name' => $label, 'value' => $value );
	}
	if ( $props ) {
		$schema['additionalProperty'] = $props;
	}

	echo '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n";
}

/**
* Variantele per mărime pentru ProductGroup: pentru fiecare mărime, câte o ofertă
* per magazin (din aceleași listări ca matricea de pe pagină).
*/
function hainute_schema_size_variants( $product_id, $name, $by_store ) {
	$stores   = array(); // magazin => [ have => [mărime=>preț], out => [mărime=>1] ]
	$listings = hainute_shop_listings( $product_id );
	// Doar culoarea produsului (prima listare = oferta noastră principală): o altă
	// culoare e alt produs, cu mărimile ei.
	// Dacă ea e epuizată, culoarea afișată implicit pe pagină = prima cu stoc.
	$first = $listings ? $listings[0] : null;
	foreach ( $listings as $l ) {
		if ( ! empty( $l['in_stock'] ) && ( ! empty( $l['sizes'] ) ) ) {
			$first = empty( $first['in_stock'] ) ? $l : $first;
			break;
		}
	}
	$primary = $first ? hainute_ascii( mb_strtolower( trim( (string) $first['color'] ) ) ) : '';
	foreach ( $listings as $l ) {
		$st = (string) $l['store'];
		$c  = hainute_ascii( mb_strtolower( trim( (string) $l['color'] ) ) );
		if ( '' === $st || ! isset( $by_store[ $st ] ) || ( '' !== $primary && '' !== $c && $c !== $primary ) ) {
			continue;
		}
		$stores[ $st ] = $stores[ $st ] ?? array( 'have' => array(), 'out' => array() );
		foreach ( (array) $l['sizes'] as $x ) {
			$x = trim( (string) $x );
			if ( '' === $x ) {
				continue;
			}
			if ( ! empty( $l['in_stock'] ) ) {
				$stores[ $st ]['have'][ $x ] = (float) $l['price'] > 0 ? (float) $l['price'] : $by_store[ $st ]['price'];
			} else {
				$stores[ $st ]['out'][ $x ] = 1;
			}
		}
		foreach ( (array) ( $l['unavail'] ?? array() ) as $x ) {
			$stores[ $st ]['out'][ trim( (string) $x ) ] = 1;
		}
	}
	$sizes = array();
	foreach ( $stores as $d ) {
		$sizes += array_fill_keys( array_merge( array_keys( $d['have'] ), array_keys( $d['out'] ) ), 1 );
	}
	unset( $sizes[''] );
	$keys = array_map( 'strval', array_keys( $sizes ) );
	natcasesort( $keys );
	$url = get_permalink( $product_id );
	$out = array();
	foreach ( $keys as $sz ) {
		$offers = array();
		foreach ( $stores as $st => $d ) {
			$has = isset( $d['have'][ $sz ] );
			if ( ! $has && ! isset( $d['out'][ $sz ] ) ) {
				continue; // mărimea necunoscută la acest magazin → nu afirmăm nimic
			}
			$offers[] = array(
				'@type'         => 'Offer',
				'price'         => round( $has ? $d['have'][ $sz ] : $by_store[ $st ]['price'], 2 ),
				'priceCurrency' => 'RON',
				'availability'  => $has ? 'https://schema.org/InStock' : 'https://schema.org/OutOfStock',
				'itemCondition' => 'https://schema.org/NewCondition',
				'seller'        => array( '@type' => 'Organization', 'name' => $st ),
			);
		}
		if ( ! $offers ) {
			continue;
		}
		$out[] = array(
			'@type'  => 'Product',
			'@id'    => $url . '#marime-' . sanitize_title( $sz ),
			'name'   => $name . ', mărimea ' . $sz,
			'size'   => $sz,
			'url'    => $url,
			'offers' => $offers,
		);
	}
	return $out;
}

/**
* Toate „listările" cumpărabile ale unui produs: fiecare = un (magazin, culoare,
 * interval de mărimi) cu linkul, prețul și mărimile lui. Answear împarte adesea
 * același model în mai multe pagini (per culoare ȘI per interval de mărimi), plus
 * magazinele externe → aici le adunăm pe toate ca opțiuni de cumpărare.
 */
function hainute_shop_listings( $product_id ) {
	static $cache = array();
	if ( isset( $cache[ $product_id ] ) ) {
		return $cache[ $product_id ];
	}
	$cache[ $product_id ] = hainute_shop_listings_build( $product_id );
	return $cache[ $product_id ];
}

/**
* Brand / model / tip / gen / culoare din titlul produsului („Geacă Calvin Klein
* Jeans Fete Negru"): tipul e înaintea brandului, genul și culoarea după.
* @return array{brand:string,model:string,type:string,gender:string,color:string}
*/
function hainute_product_name_parts( $product_id ) {
	$title = html_entity_decode( get_the_title( $product_id ), ENT_QUOTES, 'UTF-8' );
	$brand = hainute_get_brand( $product_id );
	$out   = array( 'brand' => $brand, 'model' => '', 'type' => '', 'gender' => '', 'color' => '' );
	$pos   = $brand ? mb_stripos( $title, $brand ) : false;
	if ( false === $pos ) {
		$out['model'] = $title;
		return $out;
	}
	$out['type'] = trim( mb_substr( $title, 0, $pos ) );
	$rest        = preg_split( '/\s+/u', trim( mb_substr( $title, $pos + mb_strlen( $brand ) ) ), -1, PREG_SPLIT_NO_EMPTY );
	$colors      = array_map( 'hainute_ascii', array_map( 'mb_strtolower', array_filter( array_map( 'trim', explode( ',', (string) get_post_meta( $product_id, '_hainute_colors', true ) ) ) ) ) );
	$model       = array();
	foreach ( $rest as $w ) {
		$lw = mb_strtolower( $w );
		if ( preg_match( '/^(fete|băieți|baieti|copii|bebeluși|bebelusi|unisex)$/u', $lw ) ) {
			$out['gender'] = $lw;
		} elseif ( in_array( hainute_ascii( $lw ), $colors, true ) || preg_match( '/^(negru|alb|roșu|rosu|roz|albastru|bleumarin|verde|gri|bej|maro|galben|mov|portocaliu|multicolor|argintiu|auriu|kaki|turcoaz|crem|bordo|inchis|închis|deschis|bleu|navy|lila|corai|mustar|muștar|khaki|nude|petrol|camel)$/u', $lw ) ) {
			$out['color'] = trim( $out['color'] . ' ' . $lw );
		} else {
			$model[] = $w;
		}
	}
	$out['model'] = implode( ' ', $model );
	return $out;
}

function hainute_ascii( $s ) {
	return strtr( $s, array( 'ă' => 'a', 'â' => 'a', 'î' => 'i', 'ș' => 's', 'ş' => 's', 'ț' => 't', 'ţ' => 't' ) );
}

/** Vârsta orientativă (luni) pentru o mărime: înălțime (cm) sau număr de încălțăminte (EU). */
function hainute_size_age_months( $size ) {
	if ( ! preg_match( '/(\d+(?:[.,]\d+)?)/', (string) $size, $m ) ) {
		return null;
	}
	$n = (float) str_replace( ',', '.', $m[1] );
	if ( $n >= 44 && $n <= 190 ) { // înălțime în cm
		$map = array( 50 => 0, 56 => 1, 62 => 3, 68 => 6, 74 => 9, 80 => 12, 86 => 18, 92 => 24, 98 => 36, 104 => 48, 110 => 60, 116 => 72, 122 => 84, 128 => 96, 134 => 108, 140 => 120, 146 => 132, 152 => 144, 158 => 156, 164 => 168, 170 => 180, 176 => 192, 182 => 204, 188 => 216 );
	} elseif ( $n >= 15 && $n <= 43 ) { // încălțăminte EU
		$map = array( 15 => 0, 17 => 6, 19 => 12, 21 => 18, 22 => 24, 23 => 30, 25 => 36, 26 => 48, 27 => 54, 28 => 60, 29 => 66, 30 => 72, 31 => 84, 32 => 96, 33 => 108, 34 => 114, 35 => 120, 36 => 132, 37 => 144, 38 => 156, 39 => 168, 40 => 180, 41 => 192, 42 => 204 );
	} else {
		return null;
	}
	$best = null;
	foreach ( $map as $k => $months ) {
		if ( $k <= $n ) {
			$best = $months;
		}
	}
	return $best;
}

function hainute_age_label( $months ) {
	if ( $months < 24 ) {
		return $months . ' luni';
	}
	$y = (int) floor( $months / 12 );
	return $y . ' ani';
}

/**
* Intervalul de mărimi al produsului + vârsta orientativă („128-176", „8-16 ani").
* @return array{interval:string,age:string}
*/
function hainute_size_range( $product_id ) {
	$all = array();
	foreach ( hainute_shop_listings( $product_id ) as $l ) {
		foreach ( array_merge( (array) $l['sizes'], (array) ( $l['unavail'] ?? array() ) ) as $x ) {
			$all[ trim( (string) $x ) ] = 1;
		}
	}
	$u = get_post_meta( $product_id, '_hainute_sizes_unavailable', true );
	foreach ( is_array( $u ) ? $u : array() as $x ) {
		$all[ trim( (string) $x ) ] = 1;
	}
	unset( $all[''] );
	$keys = array_keys( $all );
	if ( ! $keys ) {
		return array( 'interval' => '', 'age' => '' );
	}
	natcasesort( $keys );
	$keys     = array_values( $keys );
	$first    = (string) $keys[0];
	$last     = (string) $keys[ count( $keys ) - 1 ];
	// Mărimi-interval („88-93", „124-134"): primul număr al primei, ultimul al ultimei.
	if ( preg_match( '/^\d+/', $first, $m1 ) && preg_match( '/(\d+)\D*$/', $last, $m2 ) ) {
		$first = $m1[0];
		$last  = $m2[1];
	}
	$interval = $first === $last ? $first : $first . '-' . $last;
	$a1       = hainute_size_age_months( $first );
	$a2       = hainute_size_age_months( $last );
	$age      = '';
	if ( null !== $a1 && null !== $a2 ) {
		if ( $a2 < 24 ) {
			$age = $a1 === $a2 ? hainute_age_label( $a1 ) : $a1 . '-' . $a2 . ' luni';
		} elseif ( $a1 >= 24 ) {
			$y1  = (int) floor( $a1 / 12 );
			$y2  = (int) floor( $a2 / 12 );
			$age = $y1 === $y2 ? hainute_age_label( $a2 ) : $y1 . '-' . $y2 . ' ani';
		} else {
			$age = hainute_age_label( $a1 ) . ' - ' . hainute_age_label( $a2 );
		}
	}
	return array( 'interval' => $interval, 'age' => $age );
}

/** Numele scurt pentru texte: „Columbia Youth Snowtrot" sau, fără model, „geacă Calvin Klein Jeans". */
function hainute_product_short_name( $product_id ) {
	$n = hainute_product_name_parts( $product_id );
	if ( '' === $n['model'] && '' !== $n['type'] ) {
		return mb_strtolower( $n['type'] ) . ' ' . $n['brand'];
	}
	return trim( $n['brand'] . ' ' . $n['model'] );
}

/** Intro-ul de sub H1: ce face pagina (mărime → magazine cu stoc), fără preț. */
function hainute_the_product_intro( $product_id ) {
	$r   = hainute_size_range( $product_id );
	$who = hainute_product_short_name( $product_id );
	if ( '' === $r['interval'] ) {
		$txt = sprintf( __( 'Vezi direct ce magazine au pe stoc %s și în ce mărimi.', 'hainute' ), $who );
	} else {
		$txt = sprintf(
			__( 'Alege mărimea %1$s%2$s și vezi direct ce magazine o au pe stoc pentru %3$s.', 'hainute' ),
			$r['interval'],
			$r['age'] ? ' (orientativ ' . $r['age'] . ')' : '',
			$who
		);
	}
	echo '<p class="product-intro">' . esc_html( $txt ) . '</p>';
}

function hainute_shop_listings_build( $product_id ) {
	$out         = array();
	// Îmbrăcăminte → mărimile pe vârstă (8Y) se convertesc în cm (128), ca la restul.
	$clothing    = false;
	foreach ( (array) wp_get_post_terms( $product_id, 'product_cat', array( 'fields' => 'ids' ) ) as $cid ) {
		foreach ( array_merge( array( $cid ), get_ancestors( $cid, 'product_cat' ) ) as $a ) {
			$t = get_term( $a, 'product_cat' );
			if ( $t && ! is_wp_error( $t ) && 0 === strpos( $t->slug, 'imbracaminte' ) ) {
				$clothing = true;
			}
		}
	}
	$store_sizes = get_post_meta( $product_id, '_hainute_store_sizes', true );
	if ( ! is_array( $store_sizes ) ) {
		$store_sizes = array();
	}
	$colors     = array_filter( array_map( 'trim', explode( ',', (string) get_post_meta( $product_id, '_hainute_colors', true ) ) ) );
	$prim_color = $colors ? $colors[0] : '';
	// Fără culoare salvată: Answear o pune în URL („...sneakers-pentru-copii-albi-...").
	if ( '' === $prim_color && function_exists( 'hainute_cj_color_from_url' ) && function_exists( 'hainute_get_offers' ) ) {
		foreach ( hainute_get_offers( $product_id ) as $o ) {
			if ( 'cj' === $o->network ) {
				$u = (string) $o->affiliate_url;
				if ( preg_match( '#[?&]url=([^&]+)#', $u, $m ) ) {
					$u = rawurldecode( $m[1] );
				}
				$prim_color = ucfirst( (string) hainute_cj_color_from_url( $u ) );
				break;
			}
		}
	}
	// Culoarea reală a fiecărei oferte EXTERNE/manuale (captată de crawler din
	// numele produsului lor) — leagă magazinul de culoarea corectă în comparator.
	$ext_color = get_post_meta( $product_id, '_hainute_ext_color', true );
	$ext_color = is_array( $ext_color ) ? $ext_color : array();
	// Magazine ascunse manual din admin (chiar dacă cross-check-ul e automat).
	$hidden = get_post_meta( $product_id, '_hainute_hidden_stores', true );
	$hidden = is_array( $hidden ) ? array_map( 'intval', $hidden ) : array();
	$prim_sizes = function_exists( 'hainute_resolve_sizes' ) ? hainute_resolve_sizes( $product_id )['labels'] : array();
	// Mărimi EPUIZATE (există la magazin, dar fără stoc): proprii (Answear/FD) și
	// per magazin extern (crawler-ul de cross-check).
	$prim_unavail  = get_post_meta( $product_id, '_hainute_sizes_unavailable', true );
	$prim_unavail  = is_array( $prim_unavail ) ? array_values( $prim_unavail ) : array();
	$store_unavail = get_post_meta( $product_id, '_hainute_store_sizes_unavail', true );
	$store_unavail = is_array( $store_unavail ) ? $store_unavail : array();
	$prim_img   = hainute_product_image( $product_id, 'large' );
	// Poza variantei de la fiecare magazin extern (crawluită de pe pagina lui):
	// altă culoare = altă poză, nu poza produsului nostru.
	$ext_image = get_post_meta( $product_id, '_hainute_ext_image', true );
	$ext_image = is_array( $ext_image ) ? $ext_image : array();

	if ( function_exists( 'hainute_get_offers' ) ) {
		foreach ( hainute_get_offers( $product_id ) as $o ) {
			if ( in_array( (int) $o->store_id, $hidden, true ) ) {
				continue; // magazin ascuns manual
			}
			if ( function_exists( 'hainute_offer_is_stale' ) && hainute_offer_is_stale( $product_id, $o ) ) {
				continue; // ofertă externă neverificată de prea mult timp
			}
			$ext = 0 === strpos( (string) $o->network, 'external' ) || 0 === strpos( (string) $o->network, 'manual' );
			// Mărimile „produsului" (crawluite) sunt ale magazinelor NOASTRE de
			// bază (Answear=cj, Fashion Days=profitshare). various-brands (2p) și
			// externii au mărimile LOR (crawluite separat) — altfel various-brands
			// ar moșteni fals toate mărimile Answear.
			$own = ( 'cj' === $o->network || 'profitshare' === $o->network );
			$out[] = array(
				'store'    => $o->store ? $o->store->name : '',
				'color'    => $own ? $prim_color : (string) ( $ext_color[ (int) $o->store_id ] ?? '' ),
				'sizes'    => hainute_norm_sizes( $own ? $prim_sizes : (array) ( $store_sizes[ (int) $o->store_id ] ?? array() ), $clothing ),
				'unavail'  => hainute_norm_sizes( $own ? $prim_unavail : (array) ( $store_unavail[ (int) $o->store_id ] ?? array() ), $clothing ),
				'url'      => $o->affiliate_url,
				'price'    => (float) $o->price,
				'in_stock' => 'out_of_stock' !== $o->stock_status,
				'image'    => $ext ? (string) ( $ext_image[ (int) $o->store_id ] ?? '' ) : $prim_img,
				'external' => $ext,
			);
		}
	}

	$variants = get_post_meta( $product_id, '_hainute_variant_offers', true );
	if ( is_array( $variants ) ) {
		foreach ( $variants as $v ) {
			// Variantă de culoare fără stoc (dispărută de la magazin) → o excludem
			// complet: nu mai e o opțiune reală (spre deosebire de un MAGAZIN fără
			// stoc, pe care-l arătăm pt comparație).
			if ( isset( $v['in_stock'] ) && empty( $v['in_stock'] ) ) {
				continue;
			}
			$st = ! empty( $v['store_id'] ) && function_exists( 'hainute_get_store' ) ? hainute_get_store( (int) $v['store_id'] ) : null;
			// Mărimile unei variante neverificate de 7 zile nu mai sunt de încredere →
			// „necunoscute" (nu le arătăm ca disponibile).
			$fresh = ! empty( $v['checked'] ) && ( time() - (int) $v['checked'] ) < 7 * DAY_IN_SECONDS;
			$out[] = array(
				'store'    => $st ? $st->name : ( $prim_img ? 'Answear.ro' : '' ),
				'color'    => (string) ( $v['color'] ?? '' ),
				'sizes'    => $fresh ? hainute_norm_sizes( explode( ',', (string) ( $v['sizes'] ?? '' ) ), $clothing ) : array(),
				'unavail'  => $fresh ? hainute_norm_sizes( explode( ',', (string) ( $v['unavail'] ?? '' ) ), $clothing ) : array(),
				'url'      => (string) ( $v['url'] ?? '' ),
				'price'    => (float) ( $v['price'] ?? 0 ),
				'in_stock' => ! empty( $v['in_stock'] ),
				'image'    => (string) ( $v['image'] ?? '' ),
				'external' => false,
			);
		}
	}

	// Partenerii afiliați (non-external) primii. Restul păstrează ordinea de
	// inserare (oferta PRIMARĂ înaintea variantelor) — usort e stabil în PHP 8+,
	// deci linkul implicit al unui magazin = varianta principală (culoarea
	// produsului), nu cea mai ieftină variantă întâmplătoare.
	usort(
		$out,
		function ( $a, $b ) {
			return ( $a['external'] ? 1 : 0 ) - ( $b['external'] ? 1 : 0 );
		}
	);

	return $out;
}

/** Categoria-frunză (cea mai adâncă) a produsului, sau null. */
function hainute_product_leaf_cat( $product_id ) {
	$cats = get_the_terms( $product_id, 'product_cat' );
	if ( ! $cats || is_wp_error( $cats ) ) {
		return null;
	}
	$leaf = $cats[0];
	foreach ( $cats as $c ) {
		if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
			$leaf = $c;
		}
	}
	return $leaf;
}

/**
 * Link „Vezi alte {categorie} {gen} în mărimea X" — ascuns implicit, arătat de JS
 * când mărimea aleasă e epuizată peste tot; vizibil direct dacă nu e nimic pe stoc.
 */
function hainute_the_size_alternative( $product_id, $visible ) {
	$leaf = hainute_product_leaf_cat( $product_id );
	if ( ! $leaf ) {
		return;
	}
	$url    = get_term_link( $leaf );
	$gender = get_the_terms( $product_id, 'product_gender' );
	$g      = ( $gender && ! is_wp_error( $gender ) && 1 === count( $gender ) ) ? $gender[0] : null;
	if ( $g ) {
		$url = add_query_arg( 'gen', $g->slug, $url );
	}
	// Genul din arborele de categorii (ex. Fete › Îmbrăcăminte › Geci), dacă
	// produsul n-are termen de gen.
	$gname = $g ? $g->name : '';
	if ( ! $gname ) {
		$anc = get_ancestors( $leaf->term_id, 'product_cat' );
		$top = $anc ? get_term( end( $anc ), 'product_cat' ) : null;
		if ( $top && ! is_wp_error( $top ) && preg_match( '/^(fete|băieți|baieti|bebeluși|bebelusi|unisex)$/iu', $top->name ) ) {
			$gname = $top->name;
		}
	}
	$label = sprintf(
		/* translators: 1: category, 2: gender */
		__( 'Vezi %1$s%2$s', 'hainute' ), // fără „alte/alți": genul gramatical diferă pe categorii
		mb_strtolower( html_entity_decode( $leaf->name ) ),
		$gname ? ' ' . mb_strtolower( $gname ) : ''
	);
	echo '<div class="sm-alt"' . ( $visible ? '' : ' hidden' ) . ' data-size-alt data-base="' . esc_url( $url ) . '">';
	echo '<p class="sm-alt-msg" data-size-alt-msg>' . esc_html( $visible ? __( 'Produsul nu mai e pe stoc în magazine acum.', 'hainute' ) : '' ) . '</p>';
	echo '<a class="sm-alt-link" href="' . esc_url( $url ) . '" data-label="' . esc_attr( $label ) . '">' . esc_html( $label ) . ' &rarr;</a>';
	echo '</div>';
}

/**
 * Tabelul mărime × magazin (stoc da/nu), în HTML-ul randat pe server: aceeași
 * informație ca selectorul interactiv, citibilă și fără JavaScript.
 */
function hainute_the_size_table( $size_keys, $by_store ) {
	if ( empty( $size_keys ) || empty( $by_store ) ) {
		return;
	}
	$stores = array();
	foreach ( $by_store as $name => $ls ) {
		$have = array();
		$out  = array();
		$known = false;
		foreach ( $ls as $l ) {
			if ( ! empty( $l['sizes'] ) || ! empty( $l['unavail'] ) ) {
				$known = true;
			}
			foreach ( (array) $l['sizes'] as $x ) {
				if ( ! empty( $l['in_stock'] ) ) {
					$have[ trim( $x ) ] = 1;
				} else {
					$out[ trim( $x ) ] = 1;
				}
			}
			foreach ( (array) ( $l['unavail'] ?? array() ) as $x ) {
				$out[ trim( $x ) ] = 1;
			}
		}
		$stores[ $name ] = array( 'have' => $have, 'out' => $out, 'known' => $known );
	}
	echo '<details class="size-table-wrap"><summary>' . esc_html__( 'Tabel: ce mărimi are fiecare magazin', 'hainute' ) . '</summary>';
	echo '<div class="size-table-scroll"><table class="size-table"><thead><tr><th scope="col">' . esc_html__( 'Mărime', 'hainute' ) . '</th>';
	foreach ( array_keys( $stores ) as $name ) {
		echo '<th scope="col">' . esc_html( $name ) . '</th>';
	}
	echo '</tr></thead><tbody>';
	foreach ( $size_keys as $sz ) {
		echo '<tr><th scope="row">' . esc_html( $sz ) . '</th>';
		foreach ( $stores as $st ) {
			if ( isset( $st['have'][ $sz ] ) ) {
				echo '<td class="st-yes">' . esc_html__( 'Pe stoc', 'hainute' ) . '</td>';
			} elseif ( isset( $st['out'][ $sz ] ) || $st['known'] ) {
				echo '<td class="st-no">' . esc_html__( 'Nu', 'hainute' ) . '</td>';
			} else {
				echo '<td class="st-unk">' . esc_html__( 'Neconfirmat', 'hainute' ) . '</td>';
			}
		}
		echo '</tr>';
	}
	echo '</tbody></table></div></details>';
}

/**
 * Componenta integrată de magazin: culori (dedublate, cu poză) + mărimi
 * clickabile + opțiuni de cumpărare per magazin. Click pe mărime → se aprind
 * doar magazinele care au acea mărime (cu linkul corect). Click pe culoare →
 * schimbă poza. Înlocuiește culorile/mărimile/panoul separate.
 */
function hainute_the_shop_matrix( $product_id ) {
	$listings = hainute_shop_listings( $product_id );
	if ( empty( $listings ) ) {
		return;
	}

	// Culori distincte (după etichetă), fiecare cu o poză. „Principală" = culoarea
	// produsului (prima listare = oferta noastră), nu orice variantă proprie.
	$colors   = array();
	$prim_key = $listings ? strtolower( trim( $listings[0]['color'] ) ) : '';
	foreach ( $listings as $l ) {
		$c = trim( $l['color'] );
		if ( '' === $c ) {
			continue;
		}
		$k = strtolower( $c ); // cheia = cea din ofertele matricei (fără diacritice)
		// Eticheta afișată cu diacritice (culorile se normalizează intern fără: „rosu").
		$c = strtr( ucfirst( $k ), array( 'Rosu' => 'Roșu' ) );
		// Variante în mai multe culori („negru, verde"): „Negru / Verde"; 3+ sau
		// care conțin „multicolor" → „Multicolor" (o etichetă scurtă, lizibilă).
		$parts = array_values( array_filter( array_map( 'trim', explode( ',', $k ) ) ) );
		if ( count( $parts ) > 1 ) {
			$c = ( count( $parts ) > 2 || in_array( 'multicolor', $parts, true ) )
				? 'Multicolor'
				: implode( ' / ', array_map( function ( $p ) { return strtr( ucfirst( $p ), array( 'Rosu' => 'Roșu' ) ); }, $parts ) );
		}
		// O culoare care există doar la magazine fără stoc nu e o opțiune reală.
		if ( ! isset( $colors[ $k ] ) && ! empty( $l['external'] ) && empty( $l['in_stock'] ) ) {
			continue;
		}
		if ( ! isset( $colors[ $k ] ) ) {
			// Culoarea produsului nostru = cea a ofertelor din feed (nu externe).
			$colors[ $k ] = array( 'label' => $c, 'image' => $l['image'], 'primary' => ( $k === $prim_key ), 'stock' => false );
		} elseif ( '' === $colors[ $k ]['image'] && '' !== $l['image'] ) {
			$colors[ $k ]['image'] = $l['image']; // alt magazin are poza acestei culori
		}
	}

	// Culorile cu stoc primele (altfel pagina pornește pe o culoare epuizată și pare
	// „Indisponibil" deși altă culoare se poate cumpăra); între ele, a noastră prima.
	foreach ( $listings as $l ) {
		$k = strtolower( trim( $l['color'] ) );
		if ( isset( $colors[ $k ] ) && ! empty( $l['in_stock'] ) ) {
			$colors[ $k ]['stock'] = true;
		}
	}
	uasort(
		$colors,
		function ( $a, $b ) {
			return ( (int) $b['stock'] - (int) $a['stock'] ) ?: ( (int) ! empty( $b['primary'] ) - (int) ! empty( $a['primary'] ) );
		}
	);

	// Uniunea de mărimi DISPONIBILE (din listări) + INDISPONIBILE (crawluite din
	// pagina magazinului) — pe cele indisponibile le arătăm tăiate.
	// O mărime e disponibilă doar dacă o are un magazin CU STOC; mărimile care apar
	// doar la oferte fără stoc sunt epuizate (tăiate), nu disponibile.
	$sizes   = array();
	$unavail = get_post_meta( $product_id, '_hainute_sizes_unavailable', true );
	$unavail = is_array( $unavail ) ? hainute_norm_sizes( $unavail ) : array(); // „128 CM" = „128"
	foreach ( $listings as $l ) {
		foreach ( $l['sizes'] as $s ) {
			$s = trim( $s );
			if ( '' === $s ) {
				continue;
			}
			if ( ! empty( $l['in_stock'] ) ) {
				$sizes[ $s ] = 1;
			} else {
				$unavail[] = $s;
			}
		}
	}
	foreach ( $listings as $l ) {
		foreach ( (array) ( $l['unavail'] ?? array() ) as $u ) {
			$unavail[] = trim( (string) $u );
		}
	}

	$all_sizes = $sizes;
	foreach ( $unavail as $u ) {
		if ( '' !== $u && ! isset( $all_sizes[ $u ] ) ) {
			$all_sizes[ $u ] = 0; // 0 = indisponibilă
		}
	}
	$size_keys = array_keys( $all_sizes );
	natcasesort( $size_keys );
	$sizes = $size_keys; // pt verificarea „există mărimi"

	echo '<div class="shop-matrix" data-shop-matrix>';

	if ( count( $colors ) > 1 ) {
		echo '<h2 class="section-label">' . esc_html__( 'Culori', 'hainute' ) . '</h2>';
		echo '<ul class="sm-colors">';
		$i = 0;
		foreach ( $colors as $ck => $c ) {
			$act = 0 === $i++ ? ' is-active' : '';
			$prim = ! empty( $c['primary'] ) ? ' data-primary="1"' : '';
			echo '<li><button type="button" class="sm-color' . $act . '" data-color="' . esc_attr( $ck ) . '" data-image="' . esc_url( $c['image'] ) . '" title="' . esc_attr( $c['label'] ) . '"' . $prim . '>';
			if ( $c['image'] ) {
				echo '<span class="sm-color-thumb"><img src="' . esc_url( hainute_img_resize( $c['image'], 120 ) ) . '" alt="' . esc_attr( $c['label'] ) . '" loading="lazy"></span>';
			}
			echo '<span class="sm-color-label">' . esc_html( $c['label'] ) . '</span></button></li>';
		}
		echo '</ul>';
	}

	// Câte magazine distincte → decide dacă e comparator (2+) sau o singură sursă.
	$store_names = array();
	foreach ( $listings as $l ) {
		if ( '' !== trim( (string) $l['store'] ) ) {
			$store_names[ $l['store'] ] = 1;
		}
	}
	$n_stores    = count( $store_names );
	$multi_store = $n_stores > 1;

	if ( ! empty( $sizes ) ) {
		echo '<h2 class="section-label">' . esc_html__( 'Mărimi disponibile', 'hainute' ) . '</h2>';
		$hint = $multi_store
			? __( 'Alege o mărime ca să vezi în ce magazine e disponibilă. Mărimile tăiate sunt indisponibile.', 'hainute' )
			: __( 'Alege mărimea dorită. Mărimile tăiate sunt indisponibile.', 'hainute' );
		echo '<p class="sm-hint">' . esc_html( $hint ) . '</p>';
		echo '<ul class="sm-sizes">';
		foreach ( $size_keys as $s ) {
			$is_unavail = isset( $all_sizes[ $s ] ) && 0 === $all_sizes[ $s ];
			echo '<li><button type="button" class="sm-size' . ( $is_unavail ? ' sm-unavail' : '' ) . '" data-size="' . esc_attr( $s ) . '"' . ( $is_unavail ? ' aria-disabled="true" title="' . esc_attr__( 'Epuizată momentan', 'hainute' ) . '"' : '' ) . '>' . esc_html( $s ) . '</button></li>';
		}
		echo '</ul>';
	}

	// Fără fundătură: când mărimea aleasă nu e pe stoc nicăieri (sau produsul nu
	// mai e pe stoc), trimitem la aceeași categorie, filtrată pe gen + mărime.
	$any_avail = in_array( 1, $all_sizes, true ) || ( empty( $all_sizes ) && get_post_meta( $product_id, '_hainute_buyable', true ) );
	hainute_the_size_alternative( $product_id, ! $any_avail );

	// UN rând per MAGAZIN. Fiecare magazin ține toate „sub-ofertele" lui
	// (culoare × interval de mărimi × link) în data-variants; JS alege dinamic
	// linkul + prețul potrivit culorii/mărimii selectate.
	$by_store = array();
	foreach ( $listings as $l ) {
		$by_store[ $l['store'] ][] = $l;
	}

	$offers_title = $multi_store
		? __( 'Disponibil în aceste magazine', 'hainute' )
		: __( 'De unde cumperi', 'hainute' );
	echo '<h2 class="offers-title" id="magazine">' . esc_html( $offers_title ) . '</h2>';
	hainute_the_freshness( $product_id );
	echo '<ul class="offers-list sm-listings' . ( $multi_store ? '' : ' is-single' ) . '">';
	foreach ( $by_store as $store_name => $ls ) {
		$variants = array();
		foreach ( $ls as $l ) {
			$variants[] = array(
				'color'    => strtolower( $l['color'] ),
				'sizes'    => array_values( array_map( 'trim', $l['sizes'] ) ),
				'unavail'  => array_values( array_map( 'trim', (array) ( $l['unavail'] ?? array() ) ) ),
				'url'      => $l['url'],
				'price'    => $l['price'],
				'in_stock' => (bool) $l['in_stock'],
			);
		}
		// Rândul magazinului pornește pe prima variantă cu stoc (dacă există).
		$def = $ls[0];
		foreach ( $ls as $cand ) {
			if ( ! empty( $cand['in_stock'] ) ) {
				$def = $cand;
				break;
			}
		}
		$ext = ! empty( $ls[0]['external'] );
		echo '<li class="offer ' . ( $def['in_stock'] ? 'stock-in' : 'stock-out' ) . '" data-store-row data-external="' . ( $ext ? '1' : '0' ) . '" data-variants="' . esc_attr( wp_json_encode( $variants ) ) . '">';
		echo '<div class="offer-head"><span class="offer-store">' . esc_html( $store_name );
		// Culoarea specifică magazinului extern (dacă e cunoscută) — ca să fie clar
		// că un magazin are altă culoare decât altul.
		if ( $ext && ! empty( $def['color'] ) ) {
			echo ' <span class="offer-color">· ' . esc_html( ucfirst( $def['color'] ) ) . '</span>';
		}
		echo '</span>';
		echo '<span class="offer-status"><span class="status-dot"></span><span class="offer-status-label">' . esc_html__( 'Disponibil', 'hainute' ) . '</span></span></div>';
		echo '<div class="offer-body">';
		echo '<span class="offer-price">' . hainute_format_price( $def['price'], 'RON' ) . '</span>';
		echo '<a class="offer-cta" href="' . esc_url( $def['url'] ) . '" target="_blank" rel="sponsored nofollow noopener">' . esc_html__( 'Vezi în magazin', 'hainute' ) . ' &rarr;</a>';
		echo '</div></li>';
	}
	echo '</ul>';
	hainute_the_size_table( $size_keys, $by_store );
	echo '<p class="offers-note">' . esc_html__( 'Unele linkuri sunt afiliate: dacă cumperi prin ele, primim un mic comision, fără cost suplimentar pentru tine. Prețurile sunt cele din magazin la ultima verificare și se pot schimba.', 'hainute' ) . '</p>';
	echo '</div>';
}

/**
 * The per-store availability panel — the core of the site.
 */
function hainute_the_offers_panel( $product_id ) {
	if ( ! function_exists( 'hainute_get_offers' ) ) {
		return;
	}

	$offers = hainute_get_offers( $product_id );
	if ( empty( $offers ) ) {
		return;
	}

	echo '<div class="offers-panel">';
	echo '<h2 class="offers-title">' . esc_html__( 'Disponibilitate în magazine', 'hainute' ) . '</h2>';
	echo '<ul class="offers-list">';

	foreach ( $offers as $offer ) {
		$badge      = hainute_stock_badge( $offer->stock_status );
		$store_name = $offer->store ? $offer->store->name : '';
		$is_out     = 'out_of_stock' === $offer->stock_status;

		echo '<li class="offer ' . esc_attr( $badge['class'] ) . '">';

		echo '<div class="offer-head">';
		echo '<span class="offer-store">' . esc_html( $store_name ) . '</span>';
		echo '<span class="offer-status"><span class="status-dot"></span>' . esc_html( $badge['label'] ) . '</span>';
		echo '</div>';

		echo '<div class="offer-body">';
		if ( $is_out ) {
			echo '<span class="offer-price offer-price-muted">-</span>';
			echo '<span class="offer-cta offer-cta-disabled">' . esc_html__( 'Fără stoc', 'hainute' ) . '</span>';
		} else {
			echo '<span class="offer-price">';
			if ( $offer->old_price && (float) $offer->old_price > (float) $offer->price ) {
				echo '<del>' . hainute_format_price( $offer->old_price, $offer->currency ) . '</del> ';
			}
			echo hainute_format_price( $offer->price, $offer->currency );
			echo '</span>';
			echo '<a class="offer-cta" href="' . esc_url( $offer->affiliate_url ) . '" target="_blank" rel="nofollow sponsored noopener">'
				. esc_html__( 'Vezi în magazin', 'hainute' ) . ' &rarr;</a>';
		}
		echo '</div>';

		echo '</li>';
	}

	echo '</ul>';
	echo '<p class="offers-note">' . esc_html__( 'Prețurile și stocul se actualizează automat din feed-urile magazinelor partenere.', 'hainute' ) . '</p>';
	echo '</div>';
}

/**
 * Colour/variant selector. Where we have a photo per colour (same-store variants
 * from the feed), the swatches are clickable: picking one swaps the main product
 * image and updates the "go to store" price + link for that exact colour.
 *
 * Data-backed only: renders when _hainute_variant_offers exists (each carries its
 * own image + affiliate URL). The primary product is the first swatch. Products
 * without per-colour photos keep the plain colour-name chips (hainute_the_colors).
 */
function hainute_the_variant_offers( $product_id ) {
	$variants = get_post_meta( $product_id, '_hainute_variant_offers', true );
	if ( ! is_array( $variants ) || empty( $variants ) ) {
		return;
	}

	// Primary swatch = the product itself (main image + cheapest offer link).
	$offers  = function_exists( 'hainute_get_offers' ) ? hainute_get_offers( $product_id ) : array();
	$primary = ! empty( $offers ) ? $offers[0] : null;

	$colors      = (string) get_post_meta( $product_id, '_hainute_colors', true );
	$colors      = '' !== $colors ? array_map( 'trim', explode( ',', $colors ) ) : array();
	$prim_label  = $colors ? $colors[0] : __( 'Varianta principală', 'hainute' );
	$prim_image  = hainute_product_image( $product_id, 'large' );
	$prim_url    = $primary ? $primary->affiliate_url : '';
	$prim_price  = $primary ? hainute_format_price( $primary->price, $primary->currency ) : '';

	// Build the swatch list: primary first, then each variant with a photo.
	// Mărimile produsului principal (canonic).
	$prim_sizes = '';
	if ( function_exists( 'hainute_resolve_sizes' ) ) {
		$rs         = hainute_resolve_sizes( $product_id );
		$prim_sizes = ! empty( $rs['labels'] ) ? implode( ', ', $rs['labels'] ) : '';
	}

	$swatches = array();
	if ( $prim_image ) {
		$swatches[] = array( 'label' => $prim_label, 'image' => $prim_image, 'url' => $prim_url, 'price' => $prim_price, 'sizes' => $prim_sizes );
	}
	$i = 0;
	foreach ( $variants as $v ) {
		$i++;
		if ( empty( $v['image'] ) ) {
			continue; // fără poză nu putem face swap — o sărim aici
		}
		$swatches[] = array(
			'label' => ! empty( $v['color'] ) ? $v['color'] : sprintf( __( 'Varianta %d', 'hainute' ), $i + 1 ),
			'image' => $v['image'],
			'url'   => $v['url'] ?? '',
			'price' => ( isset( $v['price'] ) && (float) $v['price'] > 0 ) ? hainute_format_price( $v['price'], $v['currency'] ?? 'RON' ) : '',
			'sizes' => (string) ( $v['sizes'] ?? '' ),
		);
	}

	if ( count( $swatches ) < 2 ) {
		return; // o singură imagine → nimic de selectat
	}

	echo '<div class="variant-selector" data-variant-selector>';
	echo '<h2 class="section-label">' . esc_html__( 'Culori / variante', 'hainute' ) . '</h2>';
	echo '<ul class="variant-swatches">';
	foreach ( $swatches as $idx => $s ) {
		$active = 0 === $idx ? ' is-active' : '';
		echo '<li>';
		echo '<button type="button" class="variant-swatch' . $active . '"'
			. ' data-image="' . esc_url( $s['image'] ) . '"'
			. ' data-url="' . esc_url( $s['url'] ) . '"'
			. ' data-price="' . esc_attr( $s['price'] ) . '"'
			. ' data-label="' . esc_attr( $s['label'] ) . '"'
			. ' data-sizes="' . esc_attr( $s['sizes'] ) . '"'
			. ' title="' . esc_attr( $s['label'] ) . '">';
		echo '<span class="swatch-thumb"><img src="' . esc_url( hainute_img_resize( $s['image'], 120 ) ) . '" alt="' . esc_attr( $s['label'] ) . '" loading="lazy"></span>';
		echo '<span class="swatch-label">' . esc_html( $s['label'] ) . '</span>';
		echo '</button>';
		echo '</li>';
	}
	echo '</ul>';
	echo '</div>';
}

/**
 * Main product image URL (hotlinked from the merchant feed), with a
 * sideloaded thumbnail as fallback for any legacy products.
 */
function hainute_product_image( $product_id, $size = 'large' ) {
	$url = get_post_meta( $product_id, '_hainute_image_url', true );
	if ( $url ) {
		return $url;
	}
	if ( has_post_thumbnail( $product_id ) ) {
		return get_the_post_thumbnail_url( $product_id, $size );
	}
	return '';
}

/**
 * Pozele sunt hotlink. Unele CDN-uri de magazin servesc și variante mai mici, deci
 * cerem cât se afișează (un card nu are nevoie de 855x1290):
 * - Answear  img*.ans-media.com/i/{W}x{H}/...  folosim DOAR dimensiunile din site-ul
 *   lor (2:3): sunt deja în cache-ul CDN și vin în AVIF (400x600 ≈ 17KB). O dimensiune
 *   „nouă" o generează pe loc (~1s) și o dă în JPEG (de 2x mai mare);
 * - Sportisimo i.sportisimo.com/.../{N}x{N}/... doar 100/180/200/450/600 (pătrat).
 * Întoarce [lățime_originală, lățimi_disponibile, callback(lățime)=>url] sau null.
 */
function hainute_img_cdn( $url ) {
	$url = (string) $url;
	if ( preg_match( '#^(https?://img\d*\.ans-media\.com/i/)(\d+)x(\d+)(/.*)$#', $url, $m ) ) {
		$std = array( 200 => 300, 300 => 450, 400 => 600, 600 => 900, 800 => 1200 );
		return array(
			(int) $m[2],
			array_keys( $std ),
			function ( $width ) use ( $m, $std ) {
				return $m[1] . $width . 'x' . $std[ $width ] . $m[4];
			},
		);
	}
	if ( preg_match( '#^(https?://i\.sportisimo\.com/products/images/\d+/\d+/)(\d+)x\2(/.*)$#', $url, $m ) ) {
		return array(
			(int) $m[2],
			array( 100, 180, 200, 450, 600 ),
			function ( $width ) use ( $m ) {
				return $m[1] . $width . 'x' . $width . $m[3];
			},
		);
	}
	return null;
}

/** Varianta de cel puțin $width px (sau originalul, dacă CDN-ul nu permite). */
function hainute_img_resize( $url, $width ) {
	$cdn = hainute_img_cdn( $url );
	if ( ! $cdn || $width >= $cdn[0] ) {
		return $url;
	}
	list( $orig, $allowed, $make ) = $cdn;
	if ( null === $allowed ) {
		return $make( $width );
	}
	foreach ( $allowed as $a ) {
		if ( $a >= $width && $a < $orig ) {
			return $make( $a );
		}
	}
	return $url;
}

/**
 * Atributele src/srcset/sizes pentru o poză hotlink (gata escapate).
 * $widths crescător; src = lățimea din mijloc (fallback pt browsere fără srcset).
 */
function hainute_img_attrs( $url, array $widths, $sizes ) {
	$cdn = hainute_img_cdn( $url );
	if ( ! $cdn ) {
		return 'src="' . esc_url( $url ) . '"';
	}
	list( $orig, $allowed, $make ) = $cdn;
	$cands = null === $allowed ? $widths : array_filter( $allowed, function ( $a ) { return $a >= 180; } );
	$set   = array();
	foreach ( $cands as $w ) {
		if ( $w < $orig ) {
			$set[ $w ] = esc_url( $make( $w ) ) . ' ' . $w . 'w';
		}
	}
	$set[ $orig ] = esc_url( $url ) . ' ' . $orig . 'w';
	$src          = hainute_img_resize( $url, $widths[ intdiv( count( $widths ), 2 ) ] );
	return 'src="' . esc_url( $src ) . '" srcset="' . implode( ', ', $set ) . '" sizes="' . esc_attr( $sizes ) . '"';
}

/**
 * Product gallery: main image + extra URLs from the feed.
 */
function hainute_the_gallery( $product_id ) {
	$images = array();

	$main = hainute_product_image( $product_id, 'large' );
	if ( $main ) {
		$images[] = $main;
	}

	$extra = get_post_meta( $product_id, '_hainute_gallery', true );
	if ( is_array( $extra ) ) {
		$images = array_merge( $images, $extra );
	}
	$images = array_values( array_unique( array_filter( $images ) ) );

	if ( empty( $images ) ) {
		echo '<div class="gallery gallery-empty"></div>';
		return;
	}

	echo '<div class="gallery" data-gallery>';
	// Poza principală = LCP pe pagina de produs: fără lazy, prioritate mare.
	echo '<div class="gallery-main"><img ' . hainute_img_attrs( $images[0], array( 428, 640, 855 ), '(max-width: 820px) 100vw, 560px' ) . ' alt="' . esc_attr( get_the_title( $product_id ) ) . '" fetchpriority="high" decoding="async"></div>';

	if ( count( $images ) > 1 ) {
		echo '<div class="gallery-thumbs">';
		foreach ( $images as $i => $url ) {
			echo '<button type="button" class="gallery-thumb' . ( 0 === $i ? ' is-active' : '' ) . '" data-full="' . esc_url( $url ) . '">';
			echo '<img src="' . esc_url( hainute_img_resize( $url, 160 ) ) . '" alt="" loading="lazy" decoding="async">';
			echo '</button>';
		}
		echo '</div>';
	}

	echo '</div>';
}

/**
 * Doar pentru editori logați: „Reverifică disponibilitatea acum" (toate magazinele
 * produsului). Rulează prin worker-ul de crawlere; pagina se reîncarcă singură.
 */
function hainute_the_recheck_box( $product_id ) {
	if ( ! function_exists( 'hainute_recheck_can' ) || ! hainute_recheck_can() ) {
		return;
	}
	$done = (int) get_post_meta( $product_id, '_hainute_recheck_done', true );
	echo '<div class="admin-recheck" data-recheck="' . (int) $product_id . '" data-nonce="' . esc_attr( wp_create_nonce( 'wp_rest' ) ) . '" data-api="' . esc_url( rest_url( 'hainute/v1/' ) ) . '">';
	echo '<button type="button" class="btn btn-small admin-recheck-btn">&#8635; ' . esc_html__( 'Reverifică disponibilitatea acum', 'hainute' ) . '</button>';
	echo '<span class="admin-recheck-status">' . ( $done ? esc_html( 'Ultima reverificare: ' . hainute_ago_ro( $done ) ) : esc_html__( 'Vizibil doar pentru administratori.', 'hainute' ) ) . '</span>';
	echo '</div>';
}
