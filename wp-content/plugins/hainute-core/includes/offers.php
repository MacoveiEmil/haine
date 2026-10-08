<?php
/**
 * Offers CRUD — the custom {prefix}hainute_offers table.
 *
 * One row = one product at one store: price, stock status, affiliate link.
 * Stock status values: 'in_stock' | 'low_stock' | 'out_of_stock'.
 * 'low_stock' is only set when the feed exposes a quantity (see Faza 0 doc).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const HAINUTE_STOCK_IN  = 'in_stock';
const HAINUTE_STOCK_LOW = 'low_stock';
const HAINUTE_STOCK_OUT = 'out_of_stock';

/** Quantity at or below this counts as low stock (when quantity is known). */
function hainute_low_stock_threshold() {
	return (int) apply_filters( 'hainute_low_stock_threshold', 3 );
}

/**
 * Insert or update the offer for a (product, store) pair.
 *
 * @param int   $product_id Product post ID.
 * @param int   $store_id   Store term ID.
 * @param array $data { price, old_price, currency, stock_status, stock_qty,
 *                      affiliate_url, network, external_id }
 * @return bool
 */
function hainute_upsert_offer( $product_id, $store_id, array $data ) {
	global $wpdb;

	$defaults = array(
		'price'         => 0,
		'old_price'     => null,
		'currency'      => 'RON',
		'stock_status'  => HAINUTE_STOCK_IN,
		'stock_qty'     => null,
		'affiliate_url' => '',
		'network'       => '',
		'external_id'   => '',
	);
	$data = array_merge( $defaults, $data );

	// Derive low_stock from quantity when the feed provides one.
	if ( null !== $data['stock_qty'] && HAINUTE_STOCK_OUT !== $data['stock_status'] ) {
		$data['stock_status'] = ( (int) $data['stock_qty'] <= hainute_low_stock_threshold() )
			? HAINUTE_STOCK_LOW
			: HAINUTE_STOCK_IN;
	}

	$table = hainute_offers_table_name();

	$result = $wpdb->query(
		$wpdb->prepare(
			"INSERT INTO {$table}
				(product_id, store_id, network, external_id, price, old_price, currency, stock_status, stock_qty, affiliate_url, updated_at)
			VALUES (%d, %d, %s, %s, %f, %s, %s, %s, %s, %s, %s)
			ON DUPLICATE KEY UPDATE
				network = VALUES(network),
				external_id = VALUES(external_id),
				price = VALUES(price),
				old_price = VALUES(old_price),
				currency = VALUES(currency),
				stock_status = VALUES(stock_status),
				stock_qty = VALUES(stock_qty),
				affiliate_url = VALUES(affiliate_url),
				updated_at = VALUES(updated_at)",
			$product_id,
			$store_id,
			$data['network'],
			$data['external_id'],
			(float) $data['price'],
			$data['old_price'],
			$data['currency'],
			$data['stock_status'],
			$data['stock_qty'],
			$data['affiliate_url'],
			current_time( 'mysql' )
		)
	);

	// Keep the store taxonomy in sync so store archives work.
	if ( false !== $result ) {
		wp_set_object_terms( $product_id, (int) $store_id, 'store', true );
		hainute_refresh_min_price_meta( $product_id );
		hainute_refresh_store_count_meta( $product_id );
	}

	hainute_refresh_buyable( (int) $product_id );

	return false !== $result;
}

/**
 * Cache the product's minimum price as post meta so listings can sort/filter
 * by price without joining the offers table. Prefers in-stock offers,
 * falls back to any offer's price.
 */
function hainute_refresh_min_price_meta( $product_id ) {
	global $wpdb;

	$min = hainute_get_min_price( $product_id );

	if ( null === $min ) {
		$table = hainute_offers_table_name();
		$min   = $wpdb->get_var(
			$wpdb->prepare( "SELECT MIN(price) FROM {$table} WHERE product_id = %d", $product_id )
		);
	}

	if ( null !== $min ) {
		update_post_meta( $product_id, '_hainute_min_price', (float) $min );
	}
}

/**
 * All offers for a product, in-stock first, then by price.
 *
 * @param int $product_id Product post ID.
 * @return array[] Rows as objects, each augmented with ->store (see hainute_get_store()).
 */
function hainute_get_offers( $product_id ) {
	global $wpdb;

	$table = hainute_offers_table_name();

	$rows = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT * FROM {$table}
			WHERE product_id = %d
			ORDER BY FIELD(stock_status, %s, %s, %s), price ASC",
			$product_id,
			HAINUTE_STOCK_IN,
			HAINUTE_STOCK_LOW,
			HAINUTE_STOCK_OUT
		)
	);

	foreach ( $rows as $row ) {
		$row->store = hainute_get_store( (int) $row->store_id );
	}

	return $rows;
}

/**
 * Cheapest available (in stock / low stock) price for a product, or null.
 *
 * @return float|null
 */
function hainute_get_min_price( $product_id ) {
	// Cea mai mică ofertă cu stoc, ignorând ofertele externe expirate (neverificate
	// de prea mult timp) — același set ca lista de magazine și schema produsului.
	$min = null;
	foreach ( hainute_get_offers( $product_id ) as $o ) {
		if ( HAINUTE_STOCK_OUT === $o->stock_status || (float) $o->price <= 0 ) {
			continue;
		}
		if ( function_exists( 'hainute_offer_is_stale' ) && hainute_offer_is_stale( $product_id, $o ) ) {
			continue;
		}
		if ( null === $min || (float) $o->price < $min ) {
			$min = (float) $o->price;
		}
	}
	return $min;
}

/**
 * The (single) offer row a product already has from a given store, or null.
 * One store = one primary offer; extra same-store variants (colours) live in
 * the _hainute_variant_offers meta, not here.
 *
 * @return object|null
 */
function hainute_get_offer_for_store( $product_id, $store_id ) {
	global $wpdb;

	$table = hainute_offers_table_name();

	return $wpdb->get_row(
		$wpdb->prepare(
			"SELECT * FROM {$table} WHERE product_id = %d AND store_id = %d LIMIT 1",
			(int) $product_id,
			(int) $store_id
		)
	);
}

/**
 * Cache the number of DISTINCT stores a product is available in, as post meta,
 * so listings can filter/sort by "cross-store" without joining the offers table.
 */
function hainute_refresh_store_count_meta( $product_id ) {
	global $wpdb;

	$table = hainute_offers_table_name();
	$count = (int) $wpdb->get_var(
		$wpdb->prepare(
			"SELECT COUNT(DISTINCT store_id) FROM {$table} WHERE product_id = %d",
			(int) $product_id
		)
	);

	update_post_meta( $product_id, '_hainute_store_count', $count );
}

/**
 * Find an offer row by network + the merchant's own product id (sync lookups).
 *
 * @return object|null
 */
function hainute_find_offer_by_external_id( $network, $external_id ) {
	global $wpdb;

	$table = hainute_offers_table_name();

	return $wpdb->get_row(
		$wpdb->prepare(
			"SELECT * FROM {$table} WHERE network = %s AND external_id = %s LIMIT 1",
			$network,
			$external_id
		)
	);
}

/**
 * Delete all offers for a product (used when a product is removed).
 * Hooked on both trash and permanent delete — products are recreated by
 * the sync anyway, so there is nothing to preserve for untrash.
 */
function hainute_delete_offers_for_product( $product_id ) {
	global $wpdb;

	$wpdb->delete( hainute_offers_table_name(), array( 'product_id' => (int) $product_id ), array( '%d' ) );
}
add_action( 'before_delete_post', 'hainute_delete_offers_for_product' );
add_action( 'wp_trash_post', 'hainute_delete_offers_for_product' );

/**
 * „Are stoc acum?" + prețul minim, ca meta pe produs: listările pun produsele
 * disponibile primele și sortează pe preț real. Ține cont de magazinele ascunse,
 * de ofertele externe expirate și de variantele de culoare cu stoc. Recalculat la
 * fiecare scriere de ofertă și complet din cron (/recompute-buyable).
 */
function hainute_refresh_buyable( $product_id ) {
	$hidden = get_post_meta( $product_id, '_hainute_hidden_stores', true );
	$hidden = is_array( $hidden ) ? array_map( 'intval', $hidden ) : array();
	$buy    = 0;
	foreach ( hainute_get_offers( $product_id ) as $o ) {
		if ( HAINUTE_STOCK_OUT === $o->stock_status || in_array( (int) $o->store_id, $hidden, true ) ) {
			continue;
		}
		if ( function_exists( 'hainute_offer_is_stale' ) && hainute_offer_is_stale( $product_id, $o ) ) {
			continue;
		}
		$buy = 1;
		break;
	}
	if ( ! $buy ) {
		$variants = get_post_meta( $product_id, '_hainute_variant_offers', true );
		if ( is_array( $variants ) ) {
			foreach ( $variants as $v ) {
				if ( ! empty( $v['in_stock'] ) ) {
					$buy = 1;
					break;
				}
			}
		}
	}
	update_post_meta( $product_id, '_hainute_buyable', $buy );
	$min = hainute_get_min_price( $product_id );
	if ( null !== $min ) {
		update_post_meta( $product_id, '_hainute_min_price', $min );
	}
	return $buy;
}

/**
 * Eticheta de mărime în formatul comun între magazine: „128 CM" → „128",
 * „110 Mărimi normale" → „110", „36 EU" → „36", „7_8Y" → „7-8Y".
 */
function hainute_norm_size( $s ) {
	$s = trim( preg_replace( '/\s+/u', ' ', (string) $s ) );
	$s = preg_replace( '/\s*(cm|eu|mărimi normale|marimi normale)\.?$/iu', '', $s );
	return str_replace( '_', '-', trim( $s ) );
}

/** Normalizează o listă de mărimi (fără duplicate, ordinea păstrată). */
function hainute_norm_sizes( $list ) {
	$out = array();
	foreach ( (array) $list as $s ) {
		$n = hainute_norm_size( $s );
		if ( '' !== $n && ! in_array( $n, $out, true ) ) {
			$out[] = $n;
		}
	}
	return $out;
}
