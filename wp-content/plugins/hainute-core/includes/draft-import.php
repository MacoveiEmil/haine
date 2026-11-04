<?php
/**
 * Import de drafturi din fișiere JSON de date (wp-content/plugins/hainute-core/data/drafts-*.json),
 * pentru produse care nu vin din feed-uri afiliate: ofertele sunt „cross" (manual:{magazin}),
 * găsite de crawler și potrivite de proprietar după poză/EAN (vezi tools/crawler/brand-*.js).
 *
 * Produsele se creează DOAR ca draft (nu apar pe site până nu le publică proprietarul),
 * idempotent: cheia `_hainute_import_key` face ca o rulare repetată să sară produsele existente.
 * Rulează o singură dată pe server, din cron-ul WordPress, după ce fișierul ajunge prin git
 * (vezi hainute_drafts_import_schedule); local: `php tools/import-drafts.php <fișier>`.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Fișierele de date care trebuie importate (nume => versiune; schimbă versiunea ca să rulezi din nou). */
function hainute_drafts_import_files() {
	return array(
		'drafts-brand-v1.json' => '1',
	);
}

/** Creează un produs draft din înregistrarea JSON. @return int|WP_Error id, 0 dacă există deja. */
function hainute_import_draft_product( array $d, $update_existing = false ) {
	global $wpdb;
	$key = (string) $d['key'];

	$existing = (int) $wpdb->get_var( $wpdb->prepare( "SELECT post_id FROM {$wpdb->postmeta} WHERE meta_key='_hainute_import_key' AND meta_value=%s LIMIT 1", $key ) );
	if ( $existing && ! $update_existing ) {
		return 0;
	}

	$postarr = array(
		'post_type'    => 'product',
		'post_status'  => 'draft',
		'post_title'   => $d['title'],
		'post_content' => (string) ( $d['description_html'] ?? '' ),
	);
	if ( $existing ) {
		$postarr['ID'] = $existing;
		unset( $postarr['post_status'] ); // nu republicăm și nu mutăm un produs deja publicat
		$pid = wp_update_post( $postarr, true );
	} else {
		$pid = wp_insert_post( $postarr, true );
	}
	if ( is_wp_error( $pid ) ) {
		return $pid;
	}
	$pid = (int) $pid;

	update_post_meta( $pid, '_hainute_import_key', $key );

	// Brand, categorie, gen.
	$brand = trim( (string) ( $d['brand'] ?? '' ) );
	if ( '' !== $brand ) {
		wp_set_object_terms( $pid, $brand, 'product_brand' );
		update_post_meta( $pid, HAINUTE_MATCH_META_BRAND, hainute_norm_brand( $brand ) );
	}
	$cat = ! empty( $d['cat'] ) ? get_term_by( 'slug', $d['cat'], 'product_cat' ) : null;
	if ( $cat ) {
		wp_set_object_terms( $pid, (int) $cat->term_id, 'product_cat', false );
	}
	$gender = (string) ( $d['gender'] ?? '' );
	if ( in_array( $gender, array( 'fete', 'baieti', 'unisex' ), true ) ) {
		wp_set_object_terms( $pid, 'unisex' === $gender ? array( 'fete', 'baieti' ) : array( $gender ), 'product_gender', false );
		update_post_meta( $pid, '_hainute_merchant_gender', $gender );
		update_post_meta( $pid, '_hainute_gender_source', 'import-brand' );
	}

	// Poze (hotlink, ca la restul produselor).
	if ( ! empty( $d['image'] ) ) {
		update_post_meta( $pid, '_hainute_image_url', esc_url_raw( $d['image'] ) );
	}
	$gallery = array_values( array_filter( array_map( 'esc_url_raw', (array) ( $d['gallery'] ?? array() ) ) ) );
	if ( $gallery ) {
		update_post_meta( $pid, '_hainute_gallery', $gallery );
	}
	if ( ! empty( $d['colors'] ) ) {
		update_post_meta( $pid, '_hainute_colors', sanitize_text_field( $d['colors'] ) );
	}
	if ( ! empty( $d['model_code'] ) ) {
		update_post_meta( $pid, '_hainute_model_code', sanitize_text_field( $d['model_code'] ) );
	}

	// Mărimile produsului = reuniunea celor de pe toate paginile (pe stoc / epuizate peste tot).
	$avail = array_values( array_unique( array_map( 'strval', (array) ( $d['sizes'] ?? array() ) ) ) );
	$unav  = array_values( array_diff( array_unique( array_map( 'strval', (array) ( $d['sizes_unavail'] ?? array() ) ) ), $avail ) );
	update_post_meta( $pid, '_hainute_sizes_available', $avail );
	update_post_meta( $pid, '_hainute_sizes_unavailable', $unav );
	update_post_meta( $pid, '_hainute_size_crawled', 1 );
	update_post_meta( $pid, '_hainute_sizes', implode( ', ', array_merge( $avail, $unav ) ) );

	// Ofertele (câte una per magazin).
	$store_sizes = array();
	$store_unav  = array();
	$ext_color   = array();
	$ext_image   = array();
	$cross_match = array();
	$checked     = array();
	$urls        = array();
	$count       = 0;
	foreach ( (array) ( $d['offers'] ?? array() ) as $o ) {
		$url = esc_url_raw( $o['url'] ?? '' );
		if ( '' === $url ) {
			continue;
		}
		list( $store_id, , $slug ) = hainute_cross_store( $url );
		if ( ! $store_id ) {
			continue;
		}
		$price    = isset( $o['price'] ) ? (float) $o['price'] : 0;
		$in_stock = ! empty( $o['in_stock'] );
		hainute_upsert_offer(
			$pid,
			(int) $store_id,
			array(
				'network'       => 'manual:' . $slug,
				'external_id'   => $slug . ':' . substr( md5( $url ), 0, 16 ),
				'price'         => round( $price, 2 ),
				'currency'      => 'RON',
				'stock_status'  => $in_stock ? HAINUTE_STOCK_IN : HAINUTE_STOCK_OUT,
				'affiliate_url' => hainute_cross_affiliate_url( $url ),
			)
		);
		$sizes = array_values( array_unique( array_map( 'strval', (array) ( $o['sizes'] ?? array() ) ) ) );
		$un    = array_values( array_diff( array_unique( array_map( 'strval', (array) ( $o['unavail'] ?? array() ) ) ), $sizes ) );
		if ( $sizes || $un ) { // listă goală = necunoscute („Mărime neconfirmată"), nu „nicio mărime"
			$store_sizes[ $store_id ] = $sizes;
			$store_unav[ $store_id ]  = $un;
		}
		if ( ! empty( $o['color'] ) ) {
			$ext_color[ $store_id ] = sanitize_text_field( $o['color'] );
		}
		if ( ! empty( $o['image'] ) ) {
			$ext_image[ $store_id ] = esc_url_raw( $o['image'] );
		}
		if ( ! empty( $o['match'] ) ) {
			$cross_match[ $store_id ] = sanitize_key( $o['match'] );
		}
		// Verificat la import: fără asta oferta ar fi ascunsă (hainute_offer_is_stale); crawlerul o reverifică după publicare.
		$checked[ md5( $url ) ] = time();
		$urls[]                 = $url;
		$count++;
	}
	update_post_meta( $pid, '_hainute_store_sizes', $store_sizes );
	update_post_meta( $pid, '_hainute_store_sizes_unavail', $store_unav );
	update_post_meta( $pid, '_hainute_ext_color', $ext_color );
	update_post_meta( $pid, '_hainute_ext_image', $ext_image );
	update_post_meta( $pid, '_hainute_cross_match', $cross_match );
	update_post_meta( $pid, '_hainute_manual_offers', $urls );
	update_post_meta( $pid, '_hainute_manual_checked', $checked );
	update_post_meta( $pid, '_hainute_store_count', $count );
	if ( ! empty( $d['partner_block'] ) ) { // puține magazine: arătăm și linkurile afiliate către magazinele partenere
		update_post_meta( $pid, '_hainute_partner_block', 1 );
	}

	if ( ! empty( $d['description_html'] ) ) {
		update_post_meta( $pid, '_hainute_desc_generated', 'manual' );
		update_post_meta( $pid, '_hainute_desc_version', sanitize_key( $d['desc_version'] ?? 'v7' ) );
		update_post_meta( $pid, '_hainute_desc_published', time() );
	}
	if ( ! empty( $d['specs'] ) && is_array( $d['specs'] ) ) {
		$specs = array_filter( array_map( 'sanitize_text_field', $d['specs'] ) );
		if ( $specs ) {
			update_post_meta( $pid, '_hainute_specs', $specs );
		}
	}
	return $pid;
}

/**
 * Importă un fișier de date. @return array{creat:int,sarit:int,eroare:string[]}
 */
function hainute_import_drafts_file( $file, $update_existing = false ) {
	$out = array( 'creat' => 0, 'sarit' => 0, 'eroare' => array() );
	$raw = is_readable( $file ) ? json_decode( (string) file_get_contents( $file ), true ) : null;
	if ( ! is_array( $raw ) ) {
		$out['eroare'][] = 'fișier ilizibil: ' . $file;
		return $out;
	}
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	wp_defer_term_counting( true );
	foreach ( $raw as $d ) {
		try {
			$r = hainute_import_draft_product( $d, $update_existing );
		} catch ( Throwable $e ) {
			$out['eroare'][] = ( $d['key'] ?? '?' ) . ': ' . $e->getMessage();
			continue;
		}
		if ( is_wp_error( $r ) ) {
			$out['eroare'][] = ( $d['key'] ?? '?' ) . ': ' . $r->get_error_message();
		} elseif ( $r ) {
			$out['creat']++;
		} else {
			$out['sarit']++;
		}
	}
	wp_defer_term_counting( false );
	return $out;
}

/** Programează o singură dată importul fiecărui fișier nou (cron WordPress), cu blocare prin opțiune. */
function hainute_drafts_import_schedule() {
	foreach ( hainute_drafts_import_files() as $name => $ver ) {
		if ( ! file_exists( HAINUTE_CORE_DIR . 'data/' . $name ) ) {
			continue;
		}
		$opt  = 'hainute_drafts_import_' . md5( $name . $ver );
		$lock = (int) get_option( $opt . '_lock' );
		if ( get_option( $opt ) || ( $lock && time() - $lock < 1800 ) ) {
			continue; // făcut deja, sau pornit acum mai puțin de 30 de minute (altfel reluăm: importul e idempotent)
		}
		update_option( $opt . '_lock', time(), false );
		wp_schedule_single_event( time() + 5, 'hainute_drafts_import_run', array( $name, $ver ) ); // același eveniment programat de două ori într-un interval scurt: WordPress îl ignoră
	}
}
add_action( 'init', 'hainute_drafts_import_schedule', 30 );

add_action(
	'hainute_drafts_import_run',
	function ( $name, $ver ) {
		$res = hainute_import_drafts_file( HAINUTE_CORE_DIR . 'data/' . basename( $name ) );
		$opt = 'hainute_drafts_import_' . md5( $name . $ver );
		update_option( $opt, array( 'time' => time(), 'rezultat' => $res ), false );
	},
	10,
	2
);


/** Fișierele de descrieri (cheie import => {html, specs, versiune}); versiune nouă = rulează din nou. */
function hainute_drafts_desc_files() {
	return array();
}

/** Aplică descrierile pe produsele create din import (după cheia `_hainute_import_key`). @return array{aplicat:int,lipsa:int} */
function hainute_apply_drafts_descriptions( $file ) {
	global $wpdb;
	$out = array( 'aplicat' => 0, 'lipsa' => 0 );
	$raw = is_readable( $file ) ? json_decode( (string) file_get_contents( $file ), true ) : null;
	if ( ! is_array( $raw ) ) {
		return $out;
	}
	foreach ( $raw as $key => $x ) {
		$pid = (int) $wpdb->get_var( $wpdb->prepare( "SELECT post_id FROM {$wpdb->postmeta} WHERE meta_key='_hainute_import_key' AND meta_value=%s LIMIT 1", $key ) );
		if ( ! $pid || empty( $x['html'] ) ) {
			$out['lipsa']++;
			continue;
		}
		$html = wp_kses_post( $x['html'] );
		if ( function_exists( 'hainute_fix_content_cat_links' ) ) {
			$html = hainute_fix_content_cat_links( $pid, $html );
		}
		wp_update_post( array( 'ID' => $pid, 'post_content' => $html ) );
		$specs = array_filter( array_map( 'sanitize_text_field', (array) ( $x['specs'] ?? array() ) ) );
		if ( $specs ) {
			update_post_meta( $pid, '_hainute_specs', $specs );
		}
		update_post_meta( $pid, '_hainute_desc_generated', 'manual' );
		update_post_meta( $pid, '_hainute_desc_version', sanitize_key( $x['versiune'] ?? 'v7' ) );
		update_post_meta( $pid, '_hainute_desc_published', time() );
		$out['aplicat']++;
	}
	return $out;
}

/** Programează descrierile; așteaptă ca importul produselor să fie gata. */
function hainute_drafts_desc_schedule() {
	foreach ( hainute_drafts_desc_files() as $name => $ver ) {
		if ( ! file_exists( HAINUTE_CORE_DIR . 'data/' . $name ) ) {
			continue;
		}
		$opt  = 'hainute_drafts_desc_' . md5( $name . $ver );
		$lock = (int) get_option( $opt . '_lock' );
		if ( get_option( $opt ) || ( $lock && time() - $lock < 1800 ) ) {
			continue;
		}
		update_option( $opt . '_lock', time(), false );
		wp_schedule_single_event( time() + 90, 'hainute_drafts_desc_run', array( $name, $ver, 0 ) );
	}
}
add_action( 'init', 'hainute_drafts_desc_schedule', 31 );

add_action(
	'hainute_drafts_desc_run',
	function ( $name, $ver, $try ) {
		$all_imported = true;
		foreach ( hainute_drafts_import_files() as $f => $v ) {
			if ( file_exists( HAINUTE_CORE_DIR . 'data/' . $f ) && ! get_option( 'hainute_drafts_import_' . md5( $f . $v ) ) ) {
				$all_imported = false;
			}
		}
		if ( ! $all_imported && $try < 20 ) { // importul produselor încă rulează: reîncercăm
			wp_schedule_single_event( time() + 60, 'hainute_drafts_desc_run', array( $name, $ver, $try + 1 ) );
			return;
		}
		$res = hainute_apply_drafts_descriptions( HAINUTE_CORE_DIR . 'data/' . basename( $name ) );
		update_option( 'hainute_drafts_desc_' . md5( $name . $ver ), array( 'time' => time(), 'rezultat' => $res ), false );
	},
	10,
	3
);
