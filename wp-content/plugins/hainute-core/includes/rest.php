<?php
/**
 * REST endpoint for the real server cron:
 *
 *   POST/GET https://site.ro/wp-json/hainute/v1/sync?secret=XXX
 *
 * Protected by the HAINUTE_SYNC_SECRET constant from wp-config.php.
 * The hourly server cron just curls this URL — no WP-Cron involved.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_register_rest_routes() {
	register_rest_route(
		'hainute/v1',
		'/sync',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_sync',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	register_rest_route(
		'hainute/v1',
		'/export',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_export',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	register_rest_route(
		'hainute/v1',
		'/dedup',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_dedup',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	register_rest_route(
		'hainute/v1',
		'/regroup',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_regroup',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	register_rest_route(
		'hainute/v1',
		'/regroup-names',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_regroup_names',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	register_rest_route(
		'hainute/v1',
		'/enrich',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_enrich',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	register_rest_route(
		'hainute/v1',
		'/cj-diag',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_cj_diag',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	// Comparator magazine externe (preț + disponibilitate, matchuit pe cod model).
	register_rest_route(
		'hainute/v1',
		'/compare-queue',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_compare_queue',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/external-offer',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_external_offer',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	register_rest_route(
		'hainute/v1',
		'/wipe-fd',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_wipe_fd',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	// Verificare various-brands (2Performant): URL mort → fără stoc; mărimi reale.
	register_rest_route(
		'hainute/v1',
		'/crawl-queue-vb',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_crawl_queue_vb',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/crawl-vb-result',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_crawl_vb_result',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/vb-backfill-variants',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_vb_backfill_variants',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	// Verificare disponibilitate VARIANTE (culori dispărute de la magazin).
	register_rest_route(
		'hainute/v1',
		'/crawl-queue-variants',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_crawl_queue_variants',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/crawl-variant-result',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_crawl_variant_result',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	// Crawl Fashion Days: mărimi disponibile + stoc din pagina produsului.
	register_rest_route(
		'hainute/v1',
		'/crawl-queue-fd',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_crawl_queue_fd',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/crawl-fd-result',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_crawl_fd_result',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	// Crawler îmbogățire (mărimi/disponibilitate din paginile magazinelor).
	register_rest_route(
		'hainute/v1',
		'/crawl-queue',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_crawl_queue',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/crawl-result',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_crawl_result',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);

	// Re-verificare disponibilitate (cron): produse deja crawluite, cele mai
	// vechi/fierbinți întâi. Sursă cj (Answear) sau fd (Fashion Days).
	register_rest_route(
		'hainute/v1',
		'/recrawl-queue',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_recrawl_queue',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/gen-descriptions',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_gen_descriptions',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/recategorize',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_recategorize',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	// Cross-check manual: URL-uri lipite în admin, extrase headless (site-uri cu
	// anti-bot ce blochează fetch-ul server-side: Farfetch, Modivo etc.).
	register_rest_route(
		'hainute/v1',
		'/manual-queue',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_manual_queue',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/manual-result',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_manual_result',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	// Import cross-check (lista validată din Google Lens) → _hainute_manual_offers.
	register_rest_route(
		'hainute/v1',
		'/cross-import',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_cross_import',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	// Poza variantei per magazin extern (backfill + crawler).
	register_rest_route(
		'hainute/v1',
		'/ext-image-queue',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_ext_image_queue',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/ext-image',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_ext_image',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	// Recalcul „are stoc" + preț minim pe toate produsele publicate (cron).
	register_rest_route(
		'hainute/v1',
		'/recompute-buyable',
		array(
			'methods'             => 'GET',
			'callback'            => function () {
				global $wpdb;
				$ids = $wpdb->get_col( "SELECT ID FROM {$wpdb->posts} WHERE post_type='product' AND post_status='publish'" );
				$buy = 0;
				foreach ( $ids as $id ) {
					$buy += hainute_refresh_buyable( (int) $id );
				}
				return rest_ensure_response( array( 'ok' => true, 'produse' => count( $ids ), 'cu_stoc' => $buy ) );
			},
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/clean-titles',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_clean_titles',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/reslug',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_reslug',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/social-plan',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_social_plan',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/export-migrate',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_export_migrate',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/bulk-status',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_bulk_status',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/image-list',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_image_list',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/trash-drafts',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_trash_drafts',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/apply-taxonomy',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_apply_taxonomy',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/merge-sportisimo',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_merge_sportisimo',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/sportisimo-queue',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_sportisimo_queue',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/sportisimo-result',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_sportisimo_result',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/set-description',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_set_description',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/cj-rewrap',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_cj_rewrap',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/gen-titles',
		array(
			'methods'             => array( 'GET', 'POST' ),
			'callback'            => 'hainute_rest_gen_titles',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/specs-queue',
		array(
			'methods'             => 'GET',
			'callback'            => 'hainute_rest_specs_queue',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
	register_rest_route(
		'hainute/v1',
		'/specs-result',
		array(
			'methods'             => 'POST',
			'callback'            => 'hainute_rest_specs_result',
			'permission_callback' => 'hainute_rest_sync_permission',
		)
	);
}

/** URL brut al magazinului din orice link (dezambalează deep-link-ul CJ ?url=). */
function hainute_raw_store_url( $u ) {
	$u = (string) $u;
	$q = wp_parse_url( $u, PHP_URL_QUERY );
	if ( $q ) {
		parse_str( $q, $p );
		if ( ! empty( $p['url'] ) ) { return $p['url']; }
	}
	return $u;
}

/**
 * Coada de extragere specs: produse PUBLICATE cu ofertă, cele mai vechi extrase întâi.
 * Returnează id, url (brut magazin), store. GET /specs-queue?secret=XXX[&limit=120][&store=answear]
 */
function hainute_rest_specs_queue( WP_REST_Request $request ) {
	global $wpdb;
	$limit  = max( 1, min( 800, (int) $request->get_param( 'limit' ) ?: 150 ) );
	$only   = sanitize_key( (string) $request->get_param( 'store' ) );
	$offers = hainute_offers_table_name();
	$rows = $wpdb->get_results( $wpdb->prepare(
		"SELECT o.product_id AS pid, MIN(o.affiliate_url) AS url,
		        COALESCE(MAX(pm.meta_value+0),0) AS extracted
		 FROM {$offers} o
		 JOIN {$wpdb->posts} p ON p.ID=o.product_id AND p.post_status='publish'
		 LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id=o.product_id AND pm.meta_key='_hainute_extract_date'
		 GROUP BY o.product_id
		 ORDER BY extracted ASC
		 LIMIT %d",
		$limit * 3
	) );
	$queue = array();
	foreach ( $rows as $r ) {
		$raw = hainute_raw_store_url( $r->url );
		$store = '';
		if ( false !== strpos( $raw, 'answear' ) ) { $store = 'answear'; }
		elseif ( false !== strpos( $raw, 'sportisimo' ) ) { $store = 'sportisimo'; }
		elseif ( false !== strpos( $raw, 'fashiondays' ) ) { $store = 'fd'; }
		elseif ( false !== strpos( $raw, 'various-brands' ) ) { $store = 'vb'; }
		else { continue; }
		if ( $only && $only !== $store ) { continue; }
		$queue[] = array( 'product_id' => (int) $r->pid, 'url' => $raw, 'store' => $store );
		if ( count( $queue ) >= $limit ) { break; }
	}
	return rest_ensure_response( array( 'ok' => true, 'total' => count( $queue ), 'queue' => $queue ) );
}

/**
 * Rezultat extragere specs: stochează material + caracteristici + tot ce s-a extras.
 * POST /specs-result?secret=XXX  body { product_id, material, features:[], specs:{}, raw:{} }
 */
function hainute_rest_specs_result( WP_REST_Request $request ) {
	$b   = $request->get_json_params();
	$pid = isset( $b['product_id'] ) ? (int) $b['product_id'] : 0;
	if ( ! $pid ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă product_id' ) );
	}
	// Specs structurate: nu suprascrie ce e deja completat manual (cele 4).
	if ( 'manual' !== get_post_meta( $pid, '_hainute_desc_generated', true ) ) {
		$specs = get_post_meta( $pid, '_hainute_specs', true );
		$specs = is_array( $specs ) ? $specs : array();
		if ( ! empty( $b['material'] ) ) {
			$specs['Material'] = sanitize_text_field( (string) $b['material'] );
			update_post_meta( $pid, '_hainute_material', $specs['Material'] );
		}
		if ( isset( $b['specs'] ) && is_array( $b['specs'] ) ) {
			foreach ( $b['specs'] as $k => $v ) {
				$k = sanitize_text_field( (string) $k ); $v = sanitize_text_field( (string) $v );
				if ( '' !== $k && '' !== $v ) { $specs[ $k ] = $v; }
			}
		}
		if ( $specs ) { update_post_meta( $pid, '_hainute_specs', $specs ); }
	}
	if ( isset( $b['features'] ) && is_array( $b['features'] ) ) {
		$feat = array_values( array_filter( array_map( 'sanitize_text_field', $b['features'] ) ) );
		if ( $feat ) { update_post_meta( $pid, '_hainute_features', array_slice( $feat, 0, 12 ) ); }
	}
	if ( isset( $b['raw'] ) ) {
		update_post_meta( $pid, '_hainute_extract', wp_json_encode( $b['raw'], JSON_UNESCAPED_UNICODE ) );
	}
	update_post_meta( $pid, '_hainute_extract_date', time() );
	return rest_ensure_response( array( 'ok' => true, 'product_id' => $pid, 'material' => ! empty( $b['material'] ), 'features' => isset( $b['features'] ) ? count( (array) $b['features'] ) : 0 ) );
}

/**
 * Detectează tipul de produs (Geacă, Adidași, Pantaloni...) din titlu, cu fallback
 * pe categoria-frunză.
 */
function hainute_detect_type( $leafname, $title ) {
	$t = ' ' . mb_strtolower( wp_strip_all_tags( $title ) ) . ' ';
	$words = array(
		'combinezon' => 'Combinezon', 'salopet' => 'Salopetă', 'jachet' => 'Geacă', 'geac' => 'Geacă',
		'palton' => 'Palton', 'hanorac' => 'Hanorac', 'pulover' => 'Pulover', 'vest' => 'Vestă',
		'cămaș' => 'Cămașă', 'camas' => 'Cămașă', 'tricou' => 'Tricou', 'bluz' => 'Bluză',
		'trening' => 'Trening', 'pantalon' => 'Pantaloni', 'blug' => 'Blugi', 'short' => 'Pantaloni scurți',
		'rochi' => 'Rochie', 'fust' => 'Fustă', 'body' => 'Body',
		'adidas' => 'Adidași', 'sneaker' => 'Adidași', 'ghet' => 'Ghete', 'cizm' => 'Cizme',
		'bocanc' => 'Bocanci', 'sandal' => 'Sandale', 'papuc' => 'Papuci', 'șlap' => 'Șlapi',
		'balerin' => 'Balerini', 'mocasin' => 'Mocasini', 'pantof' => 'Pantofi',
		'căciul' => 'Căciulă', 'caciul' => 'Căciulă', 'mănuș' => 'Mănuși', 'manus' => 'Mănuși',
		'fular' => 'Fular', 'șapc' => 'Șapcă', 'sapc' => 'Șapcă', 'căciol' => 'Căciulă',
	);
	foreach ( $words as $w => $T ) {
		if ( false !== mb_strpos( $t, $w ) ) {
			return $T;
		}
	}
	$map = array(
		'Geci & jachete' => 'Geacă', 'Bluze, tricouri & hanorace' => 'Bluză',
		'Pantaloni & treninguri' => 'Pantaloni', 'Salopete & compleuri' => 'Salopetă',
		'Rochii & fuste' => 'Rochie', 'Adidași' => 'Adidași', 'Ghete & cizme' => 'Ghete',
		'Pantofi' => 'Pantofi', 'Sandale' => 'Sandale', 'Papuci' => 'Papuci',
		'Căciuli, mănuși & alte accesorii' => 'Accesorii',
	);
	return $map[ $leafname ] ?? '';
}

/**
 * Compune un titlu query-style: {Tip} {Brand} {Gen} {model/atribut} {Culoare}.
 */
function hainute_compose_title( $product_id ) {
	$cats = get_the_terms( $product_id, 'product_cat' );
	$leaf = null; $gen = '';
	if ( $cats && ! is_wp_error( $cats ) ) {
		$leaf = $cats[0];
		foreach ( $cats as $c ) {
			if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
				$leaf = $c;
			}
		}
		$anc = get_ancestors( $leaf->term_id, 'product_cat' );
		$top = $anc ? get_term( end( $anc ), 'product_cat' ) : $leaf;
		if ( $top && ! is_wp_error( $top ) ) {
			$gen = html_entity_decode( $top->name );
		}
	}
	$leafname = $leaf ? html_entity_decode( $leaf->name ) : '';
	$orig = html_entity_decode( get_the_title( $product_id ) );
	$tip  = hainute_detect_type( $leafname, $orig );
	$brand = hainute_get_brand( $product_id );
	$colors = array_filter( array_map( 'trim', explode( ',', (string) get_post_meta( $product_id, '_hainute_colors', true ) ) ) );
	$color  = $colors ? $colors[0] : '';

	// Salvage: cuvinte distinctive (model) din titlul original, fără brand/tip/generic/coduri.
	$junk = array( $brand, 'pentru copii', 'de copii', 'copii', 'copil', 'baieti', 'băieți', 'fete', 'fetite', 'unisex', 'bebe', 'bebelusi', 'iarna', 'iarnă', 'mărime', 'marime', 'culoarea', 'culoare', 'încălțăminte', 'incaltaminte', 'textil', 'material', 'model', 'articol' );
	$salv = ' ' . $orig . ' ';
	// scoate tot de la „mărime" încolo
	$salv = preg_replace( '/,?\s*m[ăa]rime.*$/iu', ' ', $salv );
	foreach ( $junk as $j ) {
		if ( $j ) {
			$salv = preg_replace( '/\b' . preg_quote( $j, '/' ) . '\b/iu', ' ', $salv );
		}
	}
	// scoate tipurile (toate variantele de mai sus) ca să nu se dubleze
	foreach ( array( 'jachet\w*', 'geac\w*', 'pantalon\w*', 'bluz\w*', 'tricou\w*', 'hanorac\w*', 'pulover\w*', 'salopet\w*', 'combinezon\w*', 'rochi\w*', 'fust\w*', 'adidas\w*', 'sneaker\w*', 'ghet\w*', 'cizm\w*', 'sandal\w*', 'papuc\w*', 'pantof\w*', 'vest\w*', 'body' ) as $rt ) {
		$salv = preg_replace( '/\b' . $rt . '\b/iu', ' ', $salv );
	}
	$salv = trim( preg_replace( '/\s+/', ' ', $salv ) );
	// păstrează doar cuvinte „citibile" (≥4 litere, fără cifre), max 2.
	$keep = array();
	foreach ( preg_split( '/\s+/', $salv ) as $w ) {
		$w = trim( $w, " ,.-" );
		if ( mb_strlen( $w ) >= 4 && ! preg_match( '/\d/', $w ) && preg_match( '/^[\p{L}]+$/u', $w ) ) {
			$keep[] = $w;
		}
		if ( count( $keep ) >= 2 ) {
			break;
		}
	}
	$salv = implode( ' ', $keep );

	$parts = array( $tip, $brand, $gen, $salv, $color );
	$out = array(); $seen = array();
	foreach ( $parts as $p ) {
		$p = trim( (string) $p );
		if ( '' === $p ) { continue; }
		$k = mb_strtolower( $p );
		if ( isset( $seen[ $k ] ) ) { continue; }
		$seen[ $k ] = 1;
		$out[] = $p;
	}
	$title = trim( implode( ' ', $out ) );
	return $title !== '' ? $title : $orig;
}

/**
 * Generează titluri query-style pentru catalog. Sare produsele cu titlu/descriere
 * MANUALĂ (_hainute_desc_generated=manual) și cele blocate. NU schimbă slug-ul.
 *   POST /gen-titles?secret=XXX[&dry_run=1][&limit=N]
 */
function hainute_rest_gen_titles( WP_REST_Request $request ) {
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$dry   = (bool) $request->get_param( 'dry_run' );
	$limit = (int) $request->get_param( 'limit' );
	$ids   = get_posts( array( 'post_type' => 'product', 'post_status' => 'publish', 'numberposts' => $limit > 0 ? $limit : -1, 'fields' => 'ids', 'orderby' => 'rand' ) );

	$done = 0; $skipped = 0; $sample = array();
	foreach ( $ids as $pid ) {
		if ( 'manual' === get_post_meta( $pid, '_hainute_desc_generated', true ) || get_post_meta( $pid, '_hainute_locked', true ) ) {
			$skipped++;
			continue;
		}
		$new = hainute_compose_title( $pid );
		$old = html_entity_decode( get_the_title( $pid ) );
		if ( $new === $old || '' === $new ) {
			continue;
		}
		if ( count( $sample ) < 25 ) {
			$sample[] = array( 'id' => $pid, 'old' => $old, 'new' => $new );
		}
		if ( ! $dry ) {
			wp_update_post( array( 'ID' => $pid, 'post_title' => $new ) );
			update_post_meta( $pid, '_hainute_title_generated', 1 );
		}
		$done++;
	}
	return rest_ensure_response( array( 'ok' => true, 'dry_run' => $dry, 'generate' => $done, 'sarite_manual' => $skipped, 'exemple' => $sample ) );
}

/**
 * Re-împachetează link-urile CJ EXISTENTE (Answear + Sportisimo) în deep-link-uri de
 * tracking CJ cu PID-ul din config, fără reimport. Idempotent (sare cele deja împachetate).
 *   POST /cj-rewrap?secret=XXX[&dry_run=1]
 */
function hainute_rest_cj_rewrap( WP_REST_Request $request ) {
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	global $wpdb;
	$dry = (bool) $request->get_param( 'dry_run' );
	$pid = trim( (string) hainute_config( 'HAINUTE_CJ_WEBSITE_ID' ) );
	if ( '' === $pid ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'HAINUTE_CJ_WEBSITE_ID nesetat' ) );
	}
	$aids = json_decode( (string) hainute_config( 'HAINUTE_CJ_AIDS' ), true );
	if ( ! is_array( $aids ) || empty( $aids ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'HAINUTE_CJ_AIDS nesetat' ) );
	}
	// Extrage URL-ul RAW al magazinului din orice formă (raw / type-dlg vechi stricat).
	$rawurl = function ( $u ) {
		$u = (string) $u;
		if ( preg_match( '#/type/dlg/(.+)$#', $u, $m ) ) {
			return urldecode( $m[1] );
		}
		return $u;
	};
	// Link corect CJ: click-{PID}-{AID}?url={magazin}. AID după advertiser (domeniu).
	$wrap = function ( $raw ) use ( $pid, $aids ) {
		$aid = '';
		foreach ( $aids as $needle => $a ) {
			if ( false !== stripos( $raw, (string) $needle ) ) { $aid = (string) $a; break; }
		}
		if ( '' === $aid ) {
			return $raw;
		}
		return 'https://www.tkqlhce.com/click-' . rawurlencode( $pid ) . '-' . rawurlencode( $aid ) . '?url=' . rawurlencode( $raw );
	};
	$offers = hainute_offers_table_name();

	// 1) Orice ofertă a cărei DESTINAȚIE e un advertiser CJ (Answear/Sportisimo),
	// indiferent de eticheta de rețea (prinde și external:sportisimo din compare.js).
	$rows = $wpdb->get_results(
		"SELECT id, affiliate_url FROM {$offers}
		 WHERE affiliate_url LIKE '%answear.%' OR affiliate_url LIKE '%sportisimo.%'"
	);
	$wrapped = 0; $skipped = 0;
	foreach ( $rows as $r ) {
		$u = (string) $r->affiliate_url;
		if ( '' === $u || false !== strpos( $u, '/click-' ) ) { $skipped++; continue; } // deja corect
		$new = $wrap( $rawurl( $u ) );
		if ( $new === $u ) { $skipped++; continue; }
		if ( ! $dry ) {
			$wpdb->update( $offers, array( 'affiliate_url' => $new ), array( 'id' => (int) $r->id ) );
		}
		$wrapped++;
	}

	// 2) Variante same-store (variant_offers) pe URL-uri CJ (answear/sportisimo).
	$meta = $wpdb->get_results( "SELECT post_id, meta_value FROM {$wpdb->postmeta} WHERE meta_key='_hainute_variant_offers'" );
	$vwrapped = 0;
	foreach ( $meta as $m ) {
		$v = maybe_unserialize( $m->meta_value );
		if ( ! is_array( $v ) ) { continue; }
		$changed = false;
		foreach ( $v as $k => $vo ) {
			$u = (string) ( $vo['url'] ?? '' );
			if ( '' === $u || false !== strpos( $u, '/click-' ) ) { continue; }
			$raw = $rawurl( $u );
			if ( ! preg_match( '#answear\.|sportisimo\.#i', $raw ) ) { continue; }
			$new = $wrap( $raw );
			if ( $new === $u ) { continue; }
			$v[ $k ]['url'] = $new;
			$changed = true; $vwrapped++;
		}
		if ( $changed && ! $dry ) {
			update_post_meta( (int) $m->post_id, '_hainute_variant_offers', $v );
		}
	}

	return rest_ensure_response( array(
		'ok'              => true,
		'dry_run'         => $dry,
		'pid'             => $pid,
		'oferte_impachetate' => $wrapped,
		'oferte_deja_ok'  => $skipped,
		'variante_impachetate' => $vwrapped,
	) );
}

/**
 * Setează descrierea (post_content) pentru unul sau mai multe produse — descrieri
 * scrise manual, de calitate. Marchează `_hainute_desc_generated`=manual (gen-descriptions
 * oricum sare conținutul ne-gol). POST /set-description?secret=XXX
 *   body { items:[{id, html}] }
 */
function hainute_rest_set_description( WP_REST_Request $request ) {
	$b     = $request->get_json_params();
	$items = isset( $b['items'] ) ? (array) $b['items'] : array();
	if ( empty( $items ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă items' ) );
	}
	$done = array();
	foreach ( $items as $it ) {
		$id    = isset( $it['id'] ) ? (int) $it['id'] : 0;
		$html  = isset( $it['html'] ) ? wp_kses_post( (string) $it['html'] ) : '';
		$title = isset( $it['title'] ) ? sanitize_text_field( (string) $it['title'] ) : '';
		$has_specs = isset( $it['specs'] ) && is_array( $it['specs'] );
		if ( ! $id || ( '' === $html && '' === $title && ! $has_specs ) ) {
			continue;
		}
		if ( '' !== $html && ! empty( $it['append'] ) ) {
			$existing = get_post_field( 'post_content', $id );
			$html     = $existing . "\n" . $html;
		}
		// Titlu query-style (H1) — NU schimbă slug-ul (post_name existent rămâne).
		$update = array( 'ID' => $id );
		if ( '' !== $html ) {
			$update['post_content'] = $html;
		}
		if ( '' !== $title ) {
			$update['post_title'] = $title;
		}
		wp_update_post( $update );
		if ( '' !== $html ) {
			update_post_meta( $id, '_hainute_desc_generated', 'manual' );
		}
		// Specificații structurate (label => value) pentru tabelul de specs.
		if ( isset( $it['specs'] ) && is_array( $it['specs'] ) ) {
			$clean = array();
			foreach ( $it['specs'] as $k => $v ) {
				$k = sanitize_text_field( (string) $k );
				$v = sanitize_text_field( (string) $v );
				if ( '' !== $k && '' !== $v ) {
					$clean[ $k ] = $v;
				}
			}
			if ( $clean ) {
				update_post_meta( $id, '_hainute_specs', $clean );
			}
		}
		$done[] = array( 'id' => $id, 'url' => get_permalink( $id ) );
	}
	return rest_ensure_response( array( 'ok' => true, 'actualizate' => count( $done ), 'produse' => $done ) );
}

/**
 * Coada de recheck Sportisimo: produse PUBLICATE cu o ofertă sportisimo.ro, cele mai
 * vechi verificate întâi. GET /sportisimo-queue?secret=XXX[&limit=80]
 */
function hainute_rest_sportisimo_queue( WP_REST_Request $request ) {
	global $wpdb;
	$limit  = max( 1, min( 500, (int) $request->get_param( 'limit' ) ?: 120 ) );
	$offers = hainute_offers_table_name();
	// DOAR produsele Sportisimo PROPRII (feed CJ): rezultatul scrie mărimile la
	// nivel de produs. Ofertele cross Sportisimo (manual:) au lanul lor (manual.js),
	// altfel ar suprascrie mărimile Answear ale produsului cu cele Sportisimo.
	$ids  = array_filter( array_map( 'intval', explode( ',', (string) $request->get_param( 'ids' ) ) ) );
	$only = $ids ? ' AND o.product_id IN (' . implode( ',', $ids ) . ')' : '';
	$rows = $wpdb->get_results( $wpdb->prepare(
		"SELECT o.product_id AS pid, o.store_id, o.affiliate_url AS url,
		        COALESCE(MAX(pm.meta_value+0),0) AS checked
		 FROM {$offers} o
		 JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status='publish'
		 LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id=o.product_id AND pm.meta_key='_hainute_stock_checked'
		 WHERE o.affiliate_url LIKE %s AND o.network = 'cj'{$only}
		 GROUP BY o.product_id
		 ORDER BY checked ASC
		 LIMIT %d",
		'%sportisimo.ro%',
		$limit
	) );
	$queue = array();
	foreach ( $rows as $r ) {
		$queue[] = array( 'product_id' => (int) $r->pid, 'store_id' => (int) $r->store_id, 'url' => (string) $r->url );
	}
	return rest_ensure_response( array( 'ok' => true, 'total' => count( $queue ), 'queue' => $queue ) );
}

/**
 * Rezultat recheck Sportisimo: actualizează preț/stoc oferta + mărimile disponibile/
 * indisponibile ale produsului. POST /sportisimo-result?secret=XXX
 *   body { product_id, store_id, price, in_stock, sizes:[], sizes_unavailable:[] }
 */
function hainute_rest_sportisimo_result( WP_REST_Request $request ) {
	global $wpdb;
	$b   = $request->get_json_params();
	$pid = isset( $b['product_id'] ) ? (int) $b['product_id'] : 0;
	if ( ! $pid ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă product_id' ) );
	}
	$offers   = hainute_offers_table_name();
	$in_stock = ! empty( $b['in_stock'] );
	$price    = isset( $b['price'] ) ? (float) $b['price'] : 0;
	$avail    = array_values( array_filter( array_map( 'sanitize_text_field', (array) ( $b['sizes'] ?? array() ) ) ) );
	$unavail  = array_values( array_filter( array_map( 'sanitize_text_field', (array) ( $b['sizes_unavailable'] ?? array() ) ) ) );

	// Actualizează oferta Sportisimo (preț + stoc).
	$set = array( 'stock_status' => $in_stock ? 'in_stock' : 'out_of_stock' );
	if ( $price > 0 ) {
		$set['price'] = round( $price, 2 );
	}
	$where = array( 'product_id' => $pid );
	if ( ! empty( $b['store_id'] ) ) {
		$where['store_id'] = (int) $b['store_id'];
	}
	$wpdb->update( $offers, $set, $where );

	// Mărimi: disponibile (afișate) + indisponibile (tăiate în matrice).
	if ( $avail ) {
		update_post_meta( $pid, '_hainute_sizes_available', $avail );
		update_post_meta( $pid, '_hainute_sizes', implode( ', ', $avail ) );
	}
	update_post_meta( $pid, '_hainute_sizes_unavailable', $unavail );

	if ( function_exists( 'hainute_mark_stock_checked' ) ) {
		hainute_mark_stock_checked( $pid );
	}
	return rest_ensure_response( array( 'ok' => true, 'product_id' => $pid, 'disponibile' => count( $avail ), 'indisponibile' => count( $unavail ), 'in_stock' => $in_stock ) );
}

/**
 * Unește produsele Sportisimo sparte pe mărime (același model = mai multe produse,
 * fiecare cu o mărime în titlu) într-un singur produs cu disponibilitate per mărime.
 * Gruparea = calea de model din URL-ul Sportisimo (/brand/model/{spid}/), spid=culoare,
 * versiune=mărime. Păstrează un produs canonic, mută restul ca variante (culoare×mărime×link),
 * curăță titlul (scoate „, culoare, mărime X"), trimite duplicatele la coș.
 *   POST /merge-sportisimo?secret=XXX[&dry_run=1]
 */
function hainute_rest_merge_sportisimo( WP_REST_Request $request ) {
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	global $wpdb;
	$dry    = (bool) $request->get_param( 'dry_run' );
	$offers = hainute_offers_table_name();

	$rows = $wpdb->get_results(
		"SELECT o.product_id AS pid, o.store_id, o.price, o.stock_status, o.affiliate_url AS url
		 FROM {$offers} o
		 JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status='publish'
		 WHERE o.affiliate_url LIKE '%sportisimo.ro%'"
	);

	$groups = array();
	foreach ( $rows as $r ) {
		$pid   = (int) $r->pid;
		$title = get_the_title( $pid );
		$path  = (string) wp_parse_url( $r->url, PHP_URL_PATH );
		$segs  = array_values( array_filter( explode( '/', $path ) ) );
		while ( ! empty( $segs ) && ctype_digit( (string) end( $segs ) ) ) {
			array_pop( $segs ); // scoate spid-ul numeric (și eventuale id-uri)
		}
		$base = implode( '/', $segs ); // ex. loap/uranix
		if ( '' === $base ) {
			continue;
		}
		$color = '';
		$size  = '';
		if ( preg_match( '/,\s*([^,]+),\s*m[ăa]rime\s+(.+)$/iu', $title, $m ) ) {
			$color = trim( $m[1] );
			$size  = trim( $m[2] );
		} elseif ( preg_match( '/,\s*m[ăa]rime\s+(.+)$/iu', $title, $m ) ) {
			$size = trim( $m[1] );
		}
		if ( '' === $color ) {
			$cc    = (string) get_post_meta( $pid, '_hainute_colors', true );
			$parts = array_filter( array_map( 'trim', explode( ',', $cc ) ) );
			$color = $parts ? reset( $parts ) : '';
		}
		$base_title = preg_replace( '/,\s*[^,]*,\s*m[ăa]rime\s+.+$/iu', '', $title );
		$base_title = trim( preg_replace( '/,\s*m[ăa]rime\s+.+$/iu', '', $base_title ) );
		$groups[ $base ][] = array(
			'pid'        => $pid,
			'store_id'   => (int) $r->store_id,
			'price'      => (float) $r->price,
			'in_stock'   => ( 'out_of_stock' !== $r->stock_status ),
			'url'        => (string) $r->url,
			'color'      => $color,
			'size'       => $size,
			'base_title' => $base_title,
			'image'      => (string) get_post_meta( $pid, '_hainute_image_url', true ),
		);
	}

	$report = array();
	$merged = 0; $cleaned = 0; $trashed = 0;
	foreach ( $groups as $base => $list ) {
		usort( $list, function ( $a, $b ) { return $a['pid'] - $b['pid']; } );
		$canon = $list[0];
		$cid   = $canon['pid'];
		$report[] = array(
			'model'     => $base,
			'canonic'   => $cid,
			'titlu_nou' => $canon['base_title'],
			'membri'    => array_map( function ( $x ) { return $x['pid'] . ':' . $x['color'] . ':' . $x['size']; }, $list ),
		);
		if ( $dry ) {
			continue;
		}
		// Un singur produs FĂRĂ mărime în titlu → nimic de curățat, nu-l atinge.
		if ( count( $list ) === 1 && '' === $canon['size'] ) {
			continue;
		}

		// Culori (canonic prima), unic, case-insensitive.
		$colors = array();
		foreach ( $list as $x ) {
			$c = $x['color'];
			if ( '' !== $c && ! in_array( strtolower( $c ), array_map( 'strtolower', $colors ), true ) ) {
				$colors[] = $c;
			}
		}
		// Titlu curat + culori + mărimea proprie a canonicului (oferta primară).
		wp_update_post( array( 'ID' => $cid, 'post_title' => $canon['base_title'] ) );
		update_post_meta( $cid, '_hainute_colors', implode( ', ', $colors ) );
		if ( '' !== $canon['size'] ) {
			update_post_meta( $cid, '_hainute_sizes', $canon['size'] );
		}
		// Variante = toți membrii non-canonici (culoare×mărime×link propriu).
		$variants = array();
		foreach ( $list as $x ) {
			if ( $x['pid'] === $cid ) {
				continue;
			}
			$variants[ 'spz:' . $x['pid'] ] = array(
				'store_id'  => $x['store_id'],
				'url'       => $x['url'],
				'image'     => $x['image'] ?: $canon['image'],
				'price'     => $x['price'],
				'old_price' => null,
				'currency'  => 'RON',
				'in_stock'  => $x['in_stock'],
				'color'     => $x['color'],
				'sizes'     => $x['size'],
			);
		}
		if ( ! empty( $variants ) ) {
			update_post_meta( $cid, '_hainute_variant_offers', $variants );
		}
		// Trimite la coș duplicatele + curăță ofertele lor orfane.
		foreach ( $list as $x ) {
			if ( $x['pid'] === $cid ) {
				continue;
			}
			$wpdb->delete( $offers, array( 'product_id' => $x['pid'] ) );
			wp_trash_post( $x['pid'] );
			$trashed++;
		}
		if ( count( $list ) > 1 ) {
			$merged++;
		} else {
			$cleaned++;
		}
	}

	return rest_ensure_response( array(
		'ok'            => true,
		'dry_run'       => $dry,
		'grupuri'       => count( $groups ),
		'modele_unite'  => $merged,
		'singure_curatate' => $cleaned,
		'produse_la_cos'   => $trashed,
		'detalii'       => $report,
	) );
}

/**
 * Reconstruiește taxonomia product_cat pe 3 niveluri (Gen > Grupă > Subcategorie),
 * atribuie fiecare produs la frunza lui și șterge categoriile vechi nefolosite.
 *   POST /apply-taxonomy?secret=XXX
 *   body { tree:[{id,parent,level,name,slug}], assign:{product_id:leaf_tree_id},
 *          delete_unused:bool, dry_run:bool }
 */
function hainute_rest_apply_taxonomy( WP_REST_Request $request ) {
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$body   = $request->get_json_params();
	$tree   = isset( $body['tree'] ) ? (array) $body['tree'] : array();
	$assign = isset( $body['assign'] ) ? (array) $body['assign'] : array();
	$del    = ! empty( $body['delete_unused'] );
	$dry    = ! empty( $body['dry_run'] );
	if ( empty( $tree ) || empty( $assign ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă tree sau assign' ) );
	}

	// 1) Construiește termenii, mapând id-ul din arbore -> term_id WP (nivel crescător).
	usort( $tree, function ( $a, $b ) { return (int) $a['level'] - (int) $b['level']; } );
	$map = array();
	$created = 0; $reused = 0;
	foreach ( $tree as $node ) {
		$nid    = (string) $node['id'];
		$name   = (string) $node['name'];
		$slug   = sanitize_title( (string) $node['slug'] );
		$parent = 0;
		if ( ! empty( $node['parent'] ) && isset( $map[ (string) $node['parent'] ] ) ) {
			$parent = (int) $map[ (string) $node['parent'] ];
		}
		// Reutilizează dacă există deja același NUME sub același părinte.
		$exists = term_exists( $name, 'product_cat', $parent );
		if ( $exists ) {
			$map[ $nid ] = (int) ( is_array( $exists ) ? $exists['term_id'] : $exists );
			$reused++;
			continue;
		}
		if ( $dry ) { $map[ $nid ] = 0; $created++; continue; }
		$args = array( 'parent' => $parent );
		// Slug unic global: prefixează cu părintele dacă slug-ul e deja luat.
		if ( get_term_by( 'slug', $slug, 'product_cat' ) && $parent ) {
			$pterm = get_term( $parent, 'product_cat' );
			$slug  = ( $pterm && ! is_wp_error( $pterm ) ? $pterm->slug . '-' : '' ) . $slug;
		}
		$args['slug'] = $slug;
		$res = wp_insert_term( $name, 'product_cat', $args );
		$map[ $nid ] = is_wp_error( $res ) ? 0 : (int) $res['term_id'];
		$created++;
	}

	// 2) Atribuie fiecare produs la termenul-frunză (înlocuiește categoriile vechi).
	$assigned = 0; $missing = array();
	foreach ( $assign as $pid => $leaf ) {
		$tid = isset( $map[ (string) $leaf ] ) ? (int) $map[ (string) $leaf ] : 0;
		if ( ! $tid ) { $missing[] = (int) $pid; continue; }
		if ( ! $dry ) {
			wp_set_object_terms( (int) $pid, array( $tid ), 'product_cat', false );
		}
		$assigned++;
	}

	// 3) Șterge categoriile product_cat care nu fac parte din arborele nou.
	$deleted = 0; $to_delete = 0;
	if ( $del ) {
		$keep = array_values( array_filter( array_map( 'intval', $map ) ) );
		$all  = get_terms( array( 'taxonomy' => 'product_cat', 'hide_empty' => false, 'fields' => 'ids' ) );
		if ( ! is_wp_error( $all ) ) {
			foreach ( $all as $t ) {
				if ( in_array( (int) $t, $keep, true ) ) { continue; }
				$to_delete++;
				if ( ! $dry ) { wp_delete_term( (int) $t, 'product_cat' ); $deleted++; }
			}
		}
	}

	return rest_ensure_response( array(
		'ok'            => true,
		'dry_run'       => $dry,
		'termeni_creati' => $created,
		'termeni_refolositi' => $reused,
		'produse_atribuite'  => $assigned,
		'produse_fara_frunza' => $missing,
		'categorii_vechi_de_sters' => $to_delete,
		'categorii_sterse'   => $deleted,
	) );
}

/**
 * Trimite la coșul de gunoi (recuperabil) TOATE produsele pe draft. Atinge exclusiv
 * post_status='draft' — cele publicate nu sunt afectate. Opțional le și șterge definitiv.
 *   POST /trash-drafts?secret=XXX[&dry_run=1][&force_delete=1]
 */
function hainute_rest_trash_drafts( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$dry   = (bool) $request->get_param( 'dry_run' );
	$force = (bool) $request->get_param( 'force_delete' );

	$ids = array_map( 'intval', $wpdb->get_col(
		"SELECT ID FROM {$wpdb->posts} WHERE post_type='product' AND post_status='draft'"
	) );
	$total = count( $ids );
	if ( $dry ) {
		return rest_ensure_response( array( 'ok' => true, 'dry_run' => true, 'draft_gasite' => $total, 'mod' => $force ? 'delete definitiv' : 'coș (recuperabil)' ) );
	}

	$done = 0;
	foreach ( $ids as $id ) {
		if ( $force ) {
			wp_delete_post( $id, true );
		} else {
			wp_trash_post( $id );
		}
		$done++;
	}
	wp_cache_flush();
	return rest_ensure_response( array( 'ok' => true, 'procesate' => $done, 'mod' => $force ? 'delete definitiv' : 'coș (recuperabil)' ) );
}

/**
 * Listează produsele publicate cu URL-ul imaginii (pentru reverse image search).
 *   GET /image-list?secret=XXX[&status=publish][&limit=0][&offset=0]
 * Returnează: id, title, brand, image, url (permalink).
 */
function hainute_rest_image_list( WP_REST_Request $request ) {
	global $wpdb;
	$status = (string) ( $request->get_param( 'status' ) ?: 'publish' );
	$status = preg_replace( '/[^a-z]/', '', strtolower( $status ) );
	if ( ! in_array( $status, array( 'publish', 'draft', 'any' ), true ) ) {
		$status = 'publish';
	}
	$limit  = (int) $request->get_param( 'limit' );
	$offset = (int) $request->get_param( 'offset' );

	$where = "post_type='product'";
	if ( 'any' !== $status ) {
		$where .= $wpdb->prepare( ' AND post_status=%s', $status );
	} else {
		$where .= " AND post_status<>'trash'";
	}
	$sql = "SELECT ID, post_title FROM {$wpdb->posts} WHERE $where ORDER BY ID ASC";
	if ( $limit > 0 ) {
		$sql .= $wpdb->prepare( ' LIMIT %d OFFSET %d', $limit, max( 0, $offset ) );
	}
	$rows = $wpdb->get_results( $sql );

	$out = array();
	foreach ( $rows as $r ) {
		$pid   = (int) $r->ID;
		$image = (string) get_post_meta( $pid, '_hainute_image_url', true );
		if ( ! $image ) {
			$thumb = get_the_post_thumbnail_url( $pid, 'full' );
			$image = $thumb ? (string) $thumb : '';
		}
		$brands = wp_get_post_terms( $pid, 'product_brand', array( 'fields' => 'names' ) );
		$out[]  = array(
			'id'    => $pid,
			'title' => (string) $r->post_title,
			'brand' => ! is_wp_error( $brands ) && $brands ? (string) $brands[0] : '',
			'image' => $image,
			'url'   => (string) get_permalink( $pid ),
		);
	}
	return rest_ensure_response( array( 'ok' => true, 'count' => count( $out ), 'items' => $out ) );
}

/**
 * Trece TOATE produsele pe draft, cu excepția listei `keep` (care rămâne/devine
 * publish). Refuză dacă lista e goală (ca să nu draftezi tot din greșeală).
 *   POST /bulk-status?secret=XXX  body { keep:[id,...] }  (sau ?keep=1,2,3&dry_run=1)
 */
function hainute_rest_bulk_status( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$raw = $request->get_param( 'keep' );
	if ( is_string( $raw ) ) {
		$raw = preg_split( '/[\s,]+/', $raw );
	}
	$keep = array_values( array_unique( array_filter( array_map( 'intval', (array) $raw ) ) ) );
	$dry  = (bool) $request->get_param( 'dry_run' );

	if ( empty( $keep ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lista `keep` e goală — refuz să draftez tot' ) );
	}
	$in = implode( ',', $keep );

	// Verifică ce ID-uri din listă chiar există (ca produse).
	$exist = $wpdb->get_col( "SELECT ID FROM {$wpdb->posts} WHERE post_type='product' AND ID IN ($in)" );
	$exist = array_map( 'intval', $exist );
	$missing = array_values( array_diff( $keep, $exist ) );

	$to_draft = (int) $wpdb->get_var( "SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='product' AND post_status='publish' AND ID NOT IN ($in)" );

	if ( ! $dry ) {
		$wpdb->query( "UPDATE {$wpdb->posts} SET post_status='draft' WHERE post_type='product' AND post_status IN ('publish') AND ID NOT IN ($in)" );
		$wpdb->query( "UPDATE {$wpdb->posts} SET post_status='publish' WHERE post_type='product' AND post_status<>'trash' AND ID IN ($in)" );
		wp_cache_flush();
	}

	return rest_ensure_response( array(
		'ok'             => true,
		'dry_run'        => $dry,
		'de_publicat'    => count( $exist ),
		'de_draftat'     => $to_draft,
		'id_inexistente' => $missing,
	) );
}

/**
 * Export de MIGRARE: un rând per produs (publish + draft), cu SLUG-ul curent
 * (ca URL-urile să iasă identice la import, fără redirect), toate datele + coloane
 * EDITABILE (categorie, taguri, status) pe care le completezi înainte de import.
 *   GET /export-migrate?secret=XXX
 */
function hainute_rest_export_migrate( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$offers = hainute_offers_table_name();
	$ids    = $wpdb->get_col( "SELECT ID FROM {$wpdb->posts} WHERE post_type='product' AND post_status IN ('publish','draft') ORDER BY ID" );

	header( 'Content-Type: text/csv; charset=utf-8' );
	header( 'Content-Disposition: attachment; filename="produse-migrare.csv"' );
	echo "\xEF\xBB\xBF";
	$out = fopen( 'php://output', 'w' );
	fputcsv( $out, array( 'id', 'slug', 'url', 'status', 'titlu', 'brand', 'cod_produs', 'categorie', 'taguri', 'gen', 'varsta', 'pret_min', 'nr_magazine', 'magazine', 'culori', 'nr_marimi', 'marimi', 'imagine', 'descriere' ) );

	$term = function ( $pid, $tax ) {
		$t = get_the_terms( $pid, $tax );
		return ( $t && ! is_wp_error( $t ) ) ? implode( ', ', wp_list_pluck( $t, 'name' ) ) : '';
	};

	foreach ( $ids as $pid ) {
		$pid   = (int) $pid;
		$p     = get_post( $pid );
		$sizes = function_exists( 'hainute_resolve_sizes' ) ? hainute_resolve_sizes( $pid ) : array( 'count' => 0, 'labels' => array() );

		$stores = array();
		$min    = 0;
		if ( function_exists( 'hainute_get_offers' ) ) {
			foreach ( hainute_get_offers( $pid ) as $o ) {
				if ( $o->store ) {
					$stores[ $o->store->name ] = 1;
				}
				if ( 'out_of_stock' !== $o->stock_status && $o->price > 0 && ( 0 === $min || $o->price < $min ) ) {
					$min = (float) $o->price;
				}
			}
		}
		list( , $code ) = function_exists( 'hainute_search_code_for_product' ) ? hainute_search_code_for_product( $pid ) : array( '', '' );

		fputcsv(
			$out,
			array(
				$pid,
				$p->post_name,
				wp_make_link_relative( get_permalink( $pid ) ), // relativ „/produs/slug/" — independent de domeniu
				$p->post_status,
				html_entity_decode( get_the_title( $pid ), ENT_QUOTES, 'UTF-8' ),
				$term( $pid, 'product_brand' ),
				$code,
				$term( $pid, 'product_cat' ),
				'', // taguri — de completat
				$term( $pid, 'product_gender' ),
				$term( $pid, 'product_age' ),
				$min ? number_format( $min, 2, '.', '' ) : '',
				count( $stores ),
				implode( ', ', array_keys( $stores ) ),
				(string) get_post_meta( $pid, '_hainute_colors', true ),
				(int) $sizes['count'],
				implode( ', ', (array) $sizes['labels'] ),
				function_exists( 'hainute_product_image' ) ? hainute_product_image( $pid, 'large' ) : '',
				wp_strip_all_tags( (string) $p->post_content ),
			)
		);
	}
	fclose( $out );
	exit;
}

/**
 * Plan de postări FB/Instagram: alege produse (cross-store întâi, apoi branduri
 * populare, doar cu stoc + poză) și generează caption + poză + link. CSV, o
 * postare pe zi. Îl încarci în Meta Business Suite (programare nativă gratuită).
 *   GET /social-plan?secret=XXX&limit=30&start=2026-08-15
 */
function hainute_rest_social_plan( WP_REST_Request $request ) {
	global $wpdb;
	$limit = max( 1, min( 200, (int) $request->get_param( 'limit' ) ?: 30 ) );
	$start = strtotime( (string) ( $request->get_param( 'start' ) ?: 'tomorrow' ) ) ?: ( time() + DAY_IN_SECONDS );
	$t     = hainute_offers_table_name();

	// Prioritate: produse cross-store (2+ magazine), cu stoc.
	$cross = $wpdb->get_col( "SELECT o.product_id FROM $t o INNER JOIN {$wpdb->posts} p ON p.ID=o.product_id AND p.post_status='publish' GROUP BY o.product_id HAVING COUNT(DISTINCT o.store_id)>=2 ORDER BY RAND() LIMIT " . ( $limit * 2 ) );
	// Completează cu produse cu stoc + poză.
	$fill = $wpdb->get_col( "SELECT DISTINCT o.product_id FROM $t o INNER JOIN {$wpdb->posts} p ON p.ID=o.product_id AND p.post_status='publish' WHERE o.stock_status='" . HAINUTE_STOCK_IN . "' ORDER BY RAND() LIMIT " . ( $limit * 3 ) );
	$ids = array_values( array_unique( array_merge( array_map( 'intval', $cross ), array_map( 'intval', $fill ) ) ) );

	$rows = array();
	$day  = 0;
	foreach ( $ids as $pid ) {
		if ( count( $rows ) >= $limit ) {
			break;
		}
		$img = function_exists( 'hainute_product_image' ) ? hainute_product_image( $pid, 'large' ) : '';
		if ( '' === $img ) {
			continue; // fără poză nu postăm
		}
		$rows[] = array(
			gmdate( 'Y-m-d', $start + $day * DAY_IN_SECONDS ),
			get_the_title( $pid ),
			$img,
			function_exists( 'hainute_social_caption' ) ? hainute_social_caption( $pid ) : '',
			get_permalink( $pid ),
		);
		$day++;
	}

	// Output CSV direct (nu prin serializarea JSON a REST-ului).
	header( 'Content-Type: text/csv; charset=utf-8' );
	header( 'Content-Disposition: attachment; filename="plan-social.csv"' );
	echo "\xEF\xBB\xBF"; // BOM UTF-8 (diacritice corecte în Excel)
	$out = fopen( 'php://output', 'w' );
	fputcsv( $out, array( 'data', 'produs', 'imagine', 'caption', 'link' ) );
	foreach ( $rows as $r ) {
		fputcsv( $out, $r );
	}
	fclose( $out );
	exit;
}

/**
 * Înlocuiește sufixele -2/-3 din slug cu CODUL de produs → slug-uri unice și
 * stabile (ex. „...-clog-k-3" → „...-clog-k-209464"). Păstrează slug-ul vechi în
 * `_wp_old_slug` → WordPress face 301 automat. Respectă `_hainute_locked`.
 *   GET /reslug?secret=XXX&dry_run=1&limit=10000
 */
function hainute_rest_reslug( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$dry   = (bool) $request->get_param( 'dry_run' );
	$limit = max( 1, min( 10000, (int) $request->get_param( 'limit' ) ?: 10000 ) );

	$rows = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT ID, post_name FROM {$wpdb->posts}
			 WHERE post_type='product' AND post_status IN ('publish','draft') AND post_name REGEXP '-[0-9]+$'
			 LIMIT %d",
			$limit
		)
	);
	$changed = 0;
	$skipped = 0;
	$samples = array();
	foreach ( $rows as $r ) {
		$pid = (int) $r->ID;
		if ( get_post_meta( $pid, '_hainute_locked', true ) ) {
			continue;
		}
		list( , $code ) = hainute_search_code_for_product( $pid );
		$code = preg_replace( '/[^a-z0-9]/', '', strtolower( (string) $code ) );
		if ( strlen( $code ) < 4 ) {
			$skipped++;
			continue; // fără cod utilizabil → păstrăm slug-ul cu sufix
		}
		$base    = preg_replace( '/-[0-9]+$/', '', $r->post_name );
		$newslug = sanitize_title( $base . '-' . $code );
		if ( $newslug === $r->post_name || '' === $newslug ) {
			continue;
		}
		$exists = $wpdb->get_var( $wpdb->prepare( "SELECT ID FROM {$wpdb->posts} WHERE post_name=%s AND ID<>%d LIMIT 1", $newslug, $pid ) );
		if ( $exists ) {
			$skipped++;
			continue; // coliziune → păstrăm
		}
		if ( count( $samples ) < 12 ) {
			$samples[] = $r->post_name . '  →  ' . $newslug;
		}
		if ( ! $dry ) {
			add_post_meta( $pid, '_wp_old_slug', $r->post_name );
			$wpdb->update( $wpdb->posts, array( 'post_name' => $newslug ), array( 'ID' => $pid ), array( '%s' ), array( '%d' ) );
			clean_post_cache( $pid );
		}
		$changed++;
	}
	return rest_ensure_response( array( 'ok' => true, 'schimbate' => $changed, 'sărite' => $skipped, 'candidați' => count( $rows ), 'dry_run' => $dry, 'exemple' => $samples ) );
}

/**
 * Curăță titlurile produselor dintr-un magazin (implicit Sportisimo): scoate
 * „culoarea/marime" din coadă, extrage culoarea în _hainute_colors, respectă lock.
 *   GET /clean-titles?secret=XXX&store=sportisimo&dry_run=1
 */
function hainute_rest_clean_titles( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$store = sanitize_text_field( $request->get_param( 'store' ) ?: 'sportisimo' );
	$dry   = (bool) $request->get_param( 'dry_run' );
	$terms = $wpdb->get_col( $wpdb->prepare( "SELECT term_id FROM {$wpdb->terms} WHERE name LIKE %s", '%' . $wpdb->esc_like( $store ) . '%' ) );
	if ( empty( $terms ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'magazin negăsit' ) );
	}
	$offers = hainute_offers_table_name();
	$ids    = $wpdb->get_col( 'SELECT DISTINCT product_id FROM ' . $offers . ' WHERE store_id IN (' . implode( ',', array_map( 'intval', $terms ) ) . ')' );

	$changed = 0;
	$samples = array();
	foreach ( $ids as $pid ) {
		$pid = (int) $pid;
		if ( get_post_meta( $pid, '_hainute_locked', true ) ) {
			continue;
		}
		$title = html_entity_decode( get_the_title( $pid ), ENT_QUOTES, 'UTF-8' );
		$color = function_exists( 'hainute_extract_color' ) ? hainute_extract_color( $title ) : '';
		// Format Sportisimo: „{Brand} {Model} {Tip} copii, {culoare}, mărime".
		$clean = $title;
		$clean = preg_replace( '/,\s*[^,]{1,20},\s*m[ăa]rim[ei]+\s*$/iu', '', $clean ); // „, culoare, mărime"
		$clean = preg_replace( '/,?\s*m[ăa]rim[ei]+\s*$/iu', '', $clean );               // „, mărime" rămas
		$colors_re = implode( '|', array_map( 'preg_quote', hainute_color_words() ) );
		$clean = preg_replace( '/,\s*(' . $colors_re . ')\s*$/iu', '', $clean );          // „, culoare" rămasă
		$clean = rtrim( trim( preg_replace( '/\s{2,}/', ' ', $clean ) ), ' ,' );

		if ( '' !== $clean && $clean !== $title ) {
			if ( count( $samples ) < 12 ) {
				$samples[] = "$title  →  $clean";
			}
			if ( ! $dry ) {
				$wpdb->update( $wpdb->posts, array( 'post_title' => $clean ), array( 'ID' => $pid ), array( '%s' ), array( '%d' ) );
				clean_post_cache( $pid );
			}
			$changed++;
		}
		if ( ! $dry && $color ) {
			hainute_add_list_meta( $pid, '_hainute_colors', $color );
		}
	}
	return rest_ensure_response( array( 'ok' => true, 'schimbate' => $changed, 'total' => count( $ids ), 'dry_run' => $dry, 'exemple' => $samples ) );
}

/**
 * Coadă cross-check: fiecare URL cross al fiecărui produs publicat, cele
 * verificate cel mai demult primele (cele niciodată verificate = primele dintre ele).
 *   GET /manual-queue?secret=XXX[&host=zalando.ro][&ids=1,2][&limit=100][&older=HOURS]
 * `older`: doar URL-urile neverificate de cel puțin atâtea ore (pt cron).
 */
function hainute_rest_manual_queue( WP_REST_Request $request ) {
	global $wpdb;
	$only_host = strtolower( (string) $request->get_param( 'host' ) );
	$ids       = array_filter( array_map( 'intval', explode( ',', (string) $request->get_param( 'ids' ) ) ) );
	$limit     = (int) $request->get_param( 'limit' );
	$older     = (float) $request->get_param( 'older' );

	$rows = $wpdb->get_col(
		"SELECT pm.post_id FROM {$wpdb->postmeta} pm
		 JOIN {$wpdb->posts} p ON p.ID = pm.post_id
		 WHERE pm.meta_key='_hainute_manual_offers' AND p.post_status='publish'"
	);
	$queue = array();
	foreach ( $rows as $pid ) {
		$pid = (int) $pid;
		if ( $ids && ! in_array( $pid, $ids, true ) ) {
			continue;
		}
		$urls    = get_post_meta( $pid, '_hainute_manual_offers', true );
		$checked = get_post_meta( $pid, '_hainute_manual_checked', true );
		$checked = is_array( $checked ) ? $checked : array();
		if ( ! is_array( $urls ) ) {
			continue;
		}
		foreach ( $urls as $url ) {
			$host = function_exists( 'hainute_cross_host' ) ? hainute_cross_host( $url ) : '';
			if ( $only_host && $host !== $only_host ) {
				continue;
			}
			$ts = (int) ( $checked[ md5( $url ) ] ?? 0 );
			if ( $older > 0 && $ts && ( time() - $ts ) < $older * HOUR_IN_SECONDS ) {
				continue;
			}
			$queue[] = array( 'product_id' => $pid, 'url' => $url, 'host' => $host, 'checked' => $ts );
		}
	}
	// Ofertele vechi din comparatorul extern (compare.js, network external:*) nu au
	// alt lan de refresh → le verificăm aici, ca pe orice cross (altfel rămân „în
	// stoc" la nesfârșit, chiar dacă produsul a dispărut de la magazin).
	global $wpdb;
	$table = hainute_offers_table_name();
	$ext   = $wpdb->get_results(
		"SELECT o.product_id, o.affiliate_url FROM {$table} o
		 JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status = 'publish'
		 WHERE o.network LIKE 'external:%'"
	);
	$seen = array();
	foreach ( $queue as $q ) {
		$seen[ $q['product_id'] . '|' . $q['url'] ] = 1;
	}
	foreach ( $ext as $r ) {
		$pid = (int) $r->product_id;
		$url = (string) $r->affiliate_url;
		if ( isset( $seen[ $pid . '|' . $url ] ) || ( $ids && ! in_array( $pid, $ids, true ) ) ) {
			continue;
		}
		$host = hainute_cross_host( $url );
		if ( $only_host && $host !== $only_host ) {
			continue;
		}
		$checked = get_post_meta( $pid, '_hainute_manual_checked', true );
		$ts      = is_array( $checked ) ? (int) ( $checked[ md5( $url ) ] ?? 0 ) : 0;
		if ( $older > 0 && $ts && ( time() - $ts ) < $older * HOUR_IN_SECONDS ) {
			continue;
		}
		$queue[] = array( 'product_id' => $pid, 'url' => $url, 'host' => $host, 'checked' => $ts );
	}
	// Ordinea: cel mai vechi „atins" întâi = max(verificat, încercat). Un magazin
	// care ne blochează e „încercat" (fără să devină „verificat"), deci nu mai
	// ocupă capul cozii la fiecare rulare.
	$ids_cache = array();
	foreach ( $queue as &$q ) {
		if ( ! isset( $ids_cache[ $q['product_id'] ] ) ) {
			$ids_cache[ $q['product_id'] ] = hainute_cross_ids( $q['product_id'] );
		}
		$q['ids']   = $ids_cache[ $q['product_id'] ];
		$att        = get_post_meta( $q['product_id'], '_hainute_manual_attempt', true );
		$q['touch'] = max( $q['checked'], is_array( $att ) ? (int) ( $att[ md5( $q['url'] ) ] ?? 0 ) : 0 );
	}
	unset( $q );
	usort( $queue, function ( $a, $b ) { return $a['touch'] <=> $b['touch']; } );
	if ( $limit > 0 ) {
		$queue = array_slice( $queue, 0, $limit );
	}
	return rest_ensure_response( array( 'ok' => true, 'total' => count( $queue ), 'queue' => $queue ) );
}

/**
 * Rezultatul crawler-ului pentru un URL cross → oferta magazinului în comparator.
 *   POST /manual-result?secret=XXX
 *   body { product_id, url, price, currency, in_stock, sizes[], sizes_unavailable[], color, name }
 *     sau { product_id, url, gone: true }  (produsul nu mai există la magazin)
 * Prețul e convertit în RON. Magazinele partenere primesc link afiliat.
 */
function hainute_rest_manual_result( WP_REST_Request $request ) {
	$b   = $request->get_json_params();
	$pid = isset( $b['product_id'] ) ? (int) $b['product_id'] : 0;
	$url = isset( $b['url'] ) ? esc_url_raw( (string) $b['url'] ) : '';
	if ( ! $pid || '' === $url ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă product_id/url' ) );
	}
	if ( ! empty( $b['blocked'] ) ) {
		// Blocat de anti-bot: notăm doar încercarea (ordinea cozii), nu „verificat".
		$att                = get_post_meta( $pid, '_hainute_manual_attempt', true );
		$att                = is_array( $att ) ? $att : array();
		$att[ md5( $url ) ] = time();
		update_post_meta( $pid, '_hainute_manual_attempt', $att );
		return rest_ensure_response( array( 'ok' => true, 'blocked' => true ) );
	}
	list( $store_id, $name, $slug ) = hainute_cross_store( $url );
	if ( ! $store_id ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'magazin invalid' ) );
	}

	$checked                = get_post_meta( $pid, '_hainute_manual_checked', true );
	$checked                = is_array( $checked ) ? $checked : array();
	$checked[ md5( $url ) ] = time();
	update_post_meta( $pid, '_hainute_manual_checked', $checked );

	$sizes_map   = get_post_meta( $pid, '_hainute_store_sizes', true );
	$sizes_map   = is_array( $sizes_map ) ? $sizes_map : array();
	$unavail_map = get_post_meta( $pid, '_hainute_store_sizes_unavail', true );
	$unavail_map = is_array( $unavail_map ) ? $unavail_map : array();
	$clean       = function ( $list ) {
		return array_values( array_unique( array_filter( array_map( 'sanitize_text_field', is_array( $list ) ? $list : array() ) ) ) );
	};

	// Produs dispărut (404 / redirect pe listă): oferta existentă devine indisponibilă.
	if ( ! empty( $b['gone'] ) ) {
		$existing = function_exists( 'hainute_get_offer_for_store' ) ? hainute_get_offer_for_store( $pid, $store_id ) : null;
		if ( $existing && ( 0 === strpos( (string) $existing->network, 'manual' ) || 0 === strpos( (string) $existing->network, 'external' ) ) ) {
			hainute_upsert_offer( $pid, $store_id, array( 'network' => $existing->network, 'external_id' => $existing->external_id, 'price' => (float) $existing->price, 'currency' => 'RON', 'stock_status' => HAINUTE_STOCK_OUT, 'affiliate_url' => $existing->affiliate_url ) );
			$sizes_map[ $store_id ] = array();
			update_post_meta( $pid, '_hainute_store_sizes', $sizes_map );
		}
		return rest_ensure_response( array( 'ok' => true, 'store' => $name, 'gone' => true ) );
	}

	if ( ! isset( $b['price'] ) || (float) $b['price'] <= 0 ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă preț' ) );
	}
	$currency = strtoupper( sanitize_text_field( $b['currency'] ?? 'RON' ) );
	$price    = hainute_to_ron( (float) $b['price'], $currency );
	$sizes    = $clean( $b['sizes'] ?? array() );
	$unavail  = array_values( array_diff( $clean( $b['sizes_unavailable'] ?? array() ), $sizes ) );
	// Stoc: dacă știm mărimile, decid ele; altfel disponibilitatea paginii.
	$in_stock = ( $sizes || $unavail ) ? (bool) $sizes : ! empty( $b['in_stock'] );

	hainute_upsert_offer(
		$pid,
		$store_id,
		array(
			'network'       => 'manual:' . $slug,
			'external_id'   => $slug . ':' . substr( md5( $url ), 0, 16 ),
			'price'         => round( $price, 2 ),
			'currency'      => 'RON',
			'stock_status'  => $in_stock ? HAINUTE_STOCK_IN : HAINUTE_STOCK_OUT,
			'affiliate_url' => hainute_cross_affiliate_url( $url ),
		)
	);
	// Mărimile per magazin (cheia matricei din pagina produsului). Listă goală =
	// necunoscute (site fără mărimi citibile), NU „nicio mărime".
	if ( isset( $b['sizes'] ) ) {
		$sizes_map[ $store_id ]   = $sizes;
		$unavail_map[ $store_id ] = $unavail;
		update_post_meta( $pid, '_hainute_store_sizes', $sizes_map );
		update_post_meta( $pid, '_hainute_store_sizes_unavail', $unavail_map );
	}
	// Verificarea „același produs?" făcută de crawler (EAN / cod producător).
	$match = sanitize_key( (string) ( $b['match'] ?? '' ) );
	if ( $match ) {
		$mm              = get_post_meta( $pid, '_hainute_cross_match', true );
		$mm              = is_array( $mm ) ? $mm : array();
		$mm[ $store_id ] = $match;
		update_post_meta( $pid, '_hainute_cross_match', $mm );
	}
	if ( in_array( $match, array( 'ean', 'codculoare' ), true ) ) {
		// Același produs ȘI aceeași culoare → fără opțiune de culoare separată
		// (ex. „albastru" la Answear și „navy" la Sportano = aceeași geacă).
		$ec = get_post_meta( $pid, '_hainute_ext_color', true );
		if ( is_array( $ec ) && isset( $ec[ $store_id ] ) ) {
			unset( $ec[ $store_id ] );
			update_post_meta( $pid, '_hainute_ext_color', $ec );
		}
	} else {
		hainute_set_ext_color( $pid, $store_id, (string) ( $b['color'] ?? '' ) );
	}
	hainute_set_ext_image( $pid, $store_id, (string) ( $b['image'] ?? '' ) );
	// NU marcăm produsul ca „verificat" (_hainute_stock_checked): marcajul ăla
	// conduce coada de refresh a partenerilor (Answear/FD) — un cross proaspăt ar
	// amâna fals refresh-ul lor. Cross-ul are marcaj propriu per URL (mai sus).
	update_post_meta( $pid, '_hainute_store_count', count( array_unique( array_map( function ( $o ) { return (int) $o->store_id; }, hainute_get_offers( $pid ) ) ) ) );

	return rest_ensure_response( array( 'ok' => true, 'store' => $name, 'price' => round( $price, 2 ), 'in_stock' => $in_stock, 'sizes' => count( $sizes ), 'unavailable' => count( $unavail ) ) );
}

/**
 * Recalculează categoria canonică din TITLU (după fix-ul „tip din titlu") și
 * reasignează product_cat. Repară hainele clasate greșit ca încălțăminte.
 *   GET /recategorize?secret=XXX&limit=5000&dry_run=1
 */
function hainute_rest_recategorize( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$limit = max( 1, min( 10000, (int) $request->get_param( 'limit' ) ?: 5000 ) );
	$dry   = (bool) $request->get_param( 'dry_run' );

	$ids     = $wpdb->get_col( $wpdb->prepare( "SELECT ID FROM {$wpdb->posts} WHERE post_type='product' AND post_status='publish' ORDER BY ID LIMIT %d", $limit ) );
	$changed = 0;
	$samples = array();
	foreach ( $ids as $pid ) {
		$pid = (int) $pid;
		if ( get_post_meta( $pid, '_hainute_locked', true ) ) {
			continue; // produs protejat manual → nu-i atingem categoria
		}
		$title  = get_the_title( $pid );
		$brands = get_the_terms( $pid, 'product_brand' );
		$brand  = ( $brands && ! is_wp_error( $brands ) ) ? $brands[0]->name : '';
		$new    = hainute_canonical_category( '', $title, $brand );
		if ( '' === $new || 'Diverse' === $new ) {
			continue;
		}
		$cur      = get_the_terms( $pid, 'product_cat' );
		$cur_name = ( $cur && ! is_wp_error( $cur ) ) ? $cur[0]->name : '';
		if ( 0 === strcasecmp( $cur_name, $new ) ) {
			continue;
		}
		if ( count( $samples ) < 15 ) {
			$samples[] = "#{$pid} [{$cur_name} → {$new}] {$title}";
		}
		if ( ! $dry ) {
			$term = get_term_by( 'name', $new, 'product_cat' );
			if ( $term ) {
				$term_id = (int) $term->term_id;
			} else {
				$t       = wp_insert_term( $new, 'product_cat' );
				$term_id = is_wp_error( $t ) ? 0 : (int) $t['term_id'];
			}
			if ( $term_id ) {
				wp_set_object_terms( $pid, $term_id, 'product_cat', false );
			}
		}
		$changed++;
	}
	return rest_ensure_response( array( 'ok' => true, 'schimbate' => $changed, 'total' => count( $ids ), 'dry_run' => $dry, 'exemple' => $samples ) );
}

/**
 * Generează descrieri din datele structurate, DOAR unde lipsește descriere reală
 * (post_content gol sau foarte scurt) — nu suprascrie feed-ul. Idempotent.
 *   GET /gen-descriptions?secret=XXX&limit=500&force=0&min_score=0
 */
function hainute_rest_gen_descriptions( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$limit = max( 1, min( 5000, (int) $request->get_param( 'limit' ) ?: 500 ) );
	$force = (bool) $request->get_param( 'force' ); // rescrie și cele generate anterior
	$force_all = (bool) $request->get_param( 'force_all' ); // rescrie ORICE (și feed-ul urât), mai puțin manual/locked

	$cond = $force_all
		? '1=1'
		: '( CHAR_LENGTH( TRIM( p.post_content ) ) < 40 ' . ( $force ? 'OR g.meta_id IS NOT NULL' : '' ) . ' )';
	$ids = $wpdb->get_col(
		$wpdb->prepare(
			"SELECT p.ID FROM {$wpdb->posts} p
			LEFT JOIN {$wpdb->postmeta} g ON g.post_id = p.ID AND g.meta_key = '_hainute_desc_generated'
			WHERE p.post_type='product' AND p.post_status='publish' AND {$cond}
			ORDER BY p.ID LIMIT %d",
			$limit
		)
	);

	$written = 0;
	$skipped = 0;
	foreach ( $ids as $pid ) {
		$pid = (int) $pid;
		if ( get_post_meta( $pid, '_hainute_locked', true ) ) {
			$skipped++;
			continue; // produs protejat manual → nu-i atingem descrierea
		}
		if ( 'manual' === get_post_meta( $pid, '_hainute_desc_generated', true ) ) {
			$skipped++;
			continue; // descriere hand-made → nu o atingem
		}
		// Nu atinge descrierile reale din feed (doar goale sau cele generate de noi).
		$existing = trim( (string) get_post_field( 'post_content', $pid ) );
		$is_ours  = get_post_meta( $pid, '_hainute_desc_generated', true );
		if ( mb_strlen( $existing ) >= 40 && ! $is_ours && ! $force && ! $force_all ) {
			$skipped++;
			continue;
		}
		$desc = hainute_compose_description( $pid );
		if ( '' === $desc ) {
			$skipped++;
			continue;
		}
		// SQL direct: rapid, fără revizii/hook-uri (doar conținutul, sigur).
		$wpdb->update( $wpdb->posts, array( 'post_content' => $desc ), array( 'ID' => $pid ), array( '%s' ), array( '%d' ) );
		clean_post_cache( $pid );
		update_post_meta( $pid, '_hainute_desc_generated', time() );
		$written++;
	}

	$remaining = (int) $wpdb->get_var(
		"SELECT COUNT(*) FROM {$wpdb->posts} p
		WHERE p.post_type='product' AND p.post_status='publish' AND CHAR_LENGTH( TRIM( p.post_content ) ) < 40"
	);

	return rest_ensure_response( array( 'ok' => true, 'scrise' => $written, 'sărite' => $skipped, 'rămase_goale' => $remaining ) );
}

/**
 * Coadă various-brands: oferte 2performant încă neverificate, cu URL-ul real.
 *   GET /crawl-queue-vb?secret=XXX&limit=60
 */
function hainute_rest_crawl_queue_vb( WP_REST_Request $request ) {
	global $wpdb;
	$limit  = max( 1, min( 300, (int) $request->get_param( 'limit' ) ?: 60 ) );
	$offers = hainute_offers_table_name();
	// `ids=1,2` → re-verifică exact acele produse (și dacă au mai fost crawluite).
	$ids = array_filter( array_map( 'intval', explode( ',', (string) $request->get_param( 'ids' ) ) ) );
	// Fără ids: neverificate + cele verificate acum mai mult de `older` ore (implicit 6),
	// cele mai vechi primele, ca stocul să nu rămână înghețat după prima verificare.
	$older = max( 1, (int) ( $request->get_param( 'older' ) ?: 6 ) );
	$where = $ids ? 'o.product_id IN (' . implode( ',', $ids ) . ')' : '( pm.meta_id IS NULL OR CAST( pm.meta_value AS UNSIGNED ) < ' . ( time() - $older * HOUR_IN_SECONDS ) . ' )';
	$rows   = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT o.product_id, o.store_id, o.affiliate_url
			FROM {$offers} o
			INNER JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status='publish'
			LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id = o.product_id AND pm.meta_key='_hainute_vb_crawled'
			WHERE o.network='2performant' AND {$where}
			GROUP BY o.product_id ORDER BY MIN( CAST( COALESCE( pm.meta_value, 0 ) AS UNSIGNED ) ) LIMIT %d",
			$limit
		)
	);
	$queue = array();
	foreach ( $rows as $r ) {
		$url = hainute_enrich_real_url( $r->affiliate_url );
		if ( false !== strpos( $url, 'various-brands' ) ) {
			$queue[] = array( 'product_id' => (int) $r->product_id, 'store_id' => (int) $r->store_id, 'url' => $url );
		} else {
			update_post_meta( (int) $r->product_id, '_hainute_vb_crawled', 0 );
		}
	}
	return rest_ensure_response( array( 'ok' => true, 'queue' => $queue ) );
}

/**
 * Rezultat various-brands: URL mort (redirect la home) sau fără mărimi → oferta
 * 2p devine fără stoc; altfel stochează mărimile magazinului.
 *   POST /crawl-vb-result?secret=XXX  body { product_id, store_id, sizes:[], alive }
 */
function hainute_rest_crawl_vb_result( WP_REST_Request $request ) {
	global $wpdb;
	$b   = $request->get_json_params();
	$pid = isset( $b['product_id'] ) ? (int) $b['product_id'] : 0;
	$sid = isset( $b['store_id'] ) ? (int) $b['store_id'] : 0;
	if ( ! $pid ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă product_id' ) );
	}
	$sizes    = isset( $b['sizes'] ) && is_array( $b['sizes'] ) ? array_values( array_filter( array_map( 'sanitize_text_field', $b['sizes'] ) ) ) : array();
	$in_stock = ! empty( $b['alive'] );

	if ( $sid ) {
		$map = get_post_meta( $pid, '_hainute_store_sizes', true );
		if ( ! is_array( $map ) ) { $map = array(); }
		$map[ $sid ] = $sizes;
		update_post_meta( $pid, '_hainute_store_sizes', $map );
	}
	$wpdb->update(
		hainute_offers_table_name(),
		array( 'stock_status' => $in_stock ? HAINUTE_STOCK_IN : HAINUTE_STOCK_OUT ),
		array( 'product_id' => $pid, 'network' => '2performant' ),
		array( '%s' ),
		array( '%d', '%s' )
	);

	// Variantele aceluiași magazin (various-brands a listat produsul sub mai multe
	// URL-uri de culoare/mărime → _hainute_variant_offers, store_id identic) urmează
	// starea magazinului: dacă e mort, devin fără stoc → excluse din afișaj, altfel
	// ar arăta mărimi vechi din feed pentru un produs dispărut.
	if ( $sid ) {
		$vs = get_post_meta( $pid, '_hainute_variant_offers', true );
		if ( is_array( $vs ) ) {
			$changed = false;
			foreach ( $vs as $k => $v ) {
				if ( (int) ( $v['store_id'] ?? 0 ) === $sid && (bool) ( $v['in_stock'] ?? true ) !== $in_stock ) {
					$vs[ $k ]['in_stock'] = $in_stock;
					$changed             = true;
				}
			}
			if ( $changed ) {
				update_post_meta( $pid, '_hainute_variant_offers', $vs );
			}
		}
	}
	update_post_meta( $pid, '_hainute_vb_crawled', time() );
	hainute_mark_stock_checked( $pid );
	return rest_ensure_response( array( 'ok' => true, 'product_id' => $pid, 'alive' => $in_stock, 'sizes' => count( $sizes ) ) );
}

/**
 * Backfill: pentru produsele unde oferta primară various-brands (2p) e deja
 * fără stoc (marcată de crawler), aliniază și variantele aceluiași magazin la
 * fără stoc. Repară produsele crawluite ÎNAINTE de logica din crawl-vb-result.
 *   GET /vb-backfill-variants?secret=XXX
 */
function hainute_rest_vb_backfill_variants( WP_REST_Request $request ) {
	global $wpdb;
	$offers = hainute_offers_table_name();
	$rows   = $wpdb->get_results(
		"SELECT DISTINCT product_id, store_id FROM {$offers}
		 WHERE network='2performant' AND stock_status='" . HAINUTE_STOCK_OUT . "'"
	);
	$touched = 0;
	foreach ( $rows as $r ) {
		$pid = (int) $r->product_id;
		$sid = (int) $r->store_id;
		$vs  = get_post_meta( $pid, '_hainute_variant_offers', true );
		if ( ! is_array( $vs ) ) {
			continue;
		}
		$changed = false;
		foreach ( $vs as $k => $v ) {
			if ( (int) ( $v['store_id'] ?? 0 ) === $sid && ! empty( $v['in_stock'] ) ) {
				$vs[ $k ]['in_stock'] = false;
				$changed              = true;
			}
		}
		if ( $changed ) {
			update_post_meta( $pid, '_hainute_variant_offers', $vs );
			$touched++;
		}
	}
	return rest_ensure_response( array( 'ok' => true, 'produse_reparate' => $touched, 'oferte_moarte' => count( $rows ) ) );
}

/**
 * Coadă: fiecare VARIANTĂ de culoare (din _hainute_variant_offers) cu URL-ul ei,
 * pt verificarea că mai există/e pe stoc la magazin (culorile dispărute rămân
 * altfel stocate ca „disponibile" — freshness).
 *   GET /crawl-queue-variants?secret=XXX&limit=100
 */
function hainute_rest_crawl_queue_variants( WP_REST_Request $request ) {
	$limit = max( 1, min( 5000, (int) $request->get_param( 'limit' ) ?: 100 ) );
	$only  = sanitize_key( (string) $request->get_param( 'source' ) ); // '' | answear | fd | vb
	$ids   = array_filter( array_map( 'intval', preg_split( '/[\s,]+/', (string) $request->get_param( 'ids' ) ) ) );

	if ( ! empty( $ids ) ) {
		$products = $ids;
	} else {
		$products = get_posts( array( 'post_type' => 'product', 'post_status' => 'publish', 'numberposts' => -1, 'fields' => 'ids' ) );
	}
	$queue    = array();
	foreach ( $products as $pid ) {
		$variants = get_post_meta( $pid, '_hainute_variant_offers', true );
		if ( ! is_array( $variants ) ) {
			continue;
		}
		foreach ( $variants as $key => $v ) {
			$url  = hainute_enrich_real_url( (string) ( $v['url'] ?? '' ) );
			$host = '';
			if ( false !== strpos( $url, 'answear' ) ) {
				$host = 'answear';
			} elseif ( false !== strpos( $url, 'fashiondays' ) ) {
				$host = 'fd';
			} elseif ( false !== strpos( $url, 'various-brands' ) ) {
				$host = 'vb';
			} elseif ( false !== strpos( $url, 'sportisimo' ) ) {
				$host = 'sportisimo';
			}
			if ( $host && ( '' === $only || $only === $host ) ) {
				$queue[] = array( 'product_id' => (int) $pid, 'key' => (string) $key, 'url' => $url, 'host' => $host );
				if ( count( $queue ) >= $limit ) {
					break 2;
				}
			}
		}
	}
	return rest_ensure_response( array( 'ok' => true, 'queue' => $queue ) );
}

/**
 * Rezultat verificare variantă: actualizează in_stock (sau o marchează dispărută
 * dacă pagina nu mai există / n-are stoc).
 *   POST /crawl-variant-result?secret=XXX  body { product_id, key, in_stock }
 */
function hainute_rest_crawl_variant_result( WP_REST_Request $request ) {
	$b   = $request->get_json_params();
	$pid = isset( $b['product_id'] ) ? (int) $b['product_id'] : 0;
	$key = isset( $b['key'] ) ? (string) $b['key'] : '';
	if ( ! $pid || '' === $key ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă product_id/key' ) );
	}
	$variants = get_post_meta( $pid, '_hainute_variant_offers', true );
	if ( ! is_array( $variants ) || ! isset( $variants[ $key ] ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'variantă negăsită' ) );
	}
	$variants[ $key ]['in_stock'] = ! empty( $b['in_stock'] );
	// Mărimile REALE ale acestei culori (crawluite din URL-ul ei) — dau
	// disponibilitate PER CULOARE în matrice, nu agregat pe produs. Când crawlerul
	// trimite lista (chiar goală), o înlocuim: mărimile vechi NU rămân.
	$nsizes = null;
	if ( isset( $b['sizes'] ) && is_array( $b['sizes'] ) ) {
		$sizes  = hainute_norm_sizes( array_map( 'sanitize_text_field', $b['sizes'] ) );
		$unav   = hainute_norm_sizes( array_map( 'sanitize_text_field', (array) ( $b['unavailable'] ?? array() ) ) );
		$variants[ $key ]['sizes']   = implode( ', ', $sizes );
		$variants[ $key ]['unavail'] = implode( ', ', array_diff( $unav, $sizes ) );
		$nsizes = count( $sizes );
	}
	if ( ! empty( $b['checked'] ) ) {
		$variants[ $key ]['checked'] = time();
	}
	update_post_meta( $pid, '_hainute_variant_offers', $variants );
	hainute_mark_stock_checked( $pid );
	return rest_ensure_response( array( 'ok' => true, 'product_id' => $pid, 'key' => $key, 'in_stock' => ! empty( $b['in_stock'] ), 'sizes' => $nsizes ) );
}

/**
 * Coada de crawl Fashion Days: produse FD (ofertă profitshare) încă ne-crawluite,
 * cu URL-ul REAL al paginii FD. Crawler-ul ia mărimile disponibile + stocul.
 *   GET /wp-json/hainute/v1/crawl-queue-fd?secret=XXX&limit=40
 */
function hainute_rest_crawl_queue_fd( WP_REST_Request $request ) {
	global $wpdb;
	$limit  = max( 1, min( 200, (int) $request->get_param( 'limit' ) ?: 40 ) );
	$offers = hainute_offers_table_name();

	$rows = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT o.product_id, MIN(o.affiliate_url) AS url
			FROM {$offers} o
			INNER JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status = 'publish'
			LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id = o.product_id AND pm.meta_key = '_hainute_fd_crawled'
			WHERE o.network = 'profitshare' AND pm.meta_id IS NULL
			GROUP BY o.product_id
			LIMIT %d",
			$limit
		)
	);

	$queue = array();
	foreach ( $rows as $r ) {
		$url = hainute_enrich_real_url( $r->url ); // scoate URL-ul fashiondays.ro din linkul afiliat
		if ( false !== strpos( $url, 'fashiondays' ) ) {
			$queue[] = array( 'product_id' => (int) $r->product_id, 'url' => $url );
		} else {
			update_post_meta( (int) $r->product_id, '_hainute_fd_crawled', 0 );
		}
	}

	$remaining = (int) $wpdb->get_var(
		"SELECT COUNT(*) FROM (
			SELECT o.product_id FROM {$offers} o
			INNER JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status = 'publish'
			LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id = o.product_id AND pm.meta_key = '_hainute_fd_crawled'
			WHERE o.network = 'profitshare' AND pm.meta_id IS NULL GROUP BY o.product_id
		) t"
	);

	return rest_ensure_response( array( 'ok' => true, 'queue' => $queue, 'remaining' => $remaining ) );
}

/**
 * Rezultat crawl FD: stochează mărimile disponibile + actualizează STOCUL ofertei
 * Fashion Days (feed-ul FD n-are stoc → îl luăm din pagină). Fără mărimi
 * disponibile → produsul e fără stoc.
 *   POST /crawl-fd-result?secret=XXX   body { product_id, sizes:[], in_stock }
 */
function hainute_rest_crawl_fd_result( WP_REST_Request $request ) {
	global $wpdb;
	$b   = $request->get_json_params();
	$pid = isset( $b['product_id'] ) ? (int) $b['product_id'] : 0;
	if ( ! $pid || 'product' !== get_post_type( $pid ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'product_id invalid' ) );
	}

	$sizes    = isset( $b['sizes'] ) && is_array( $b['sizes'] ) ? array_values( array_filter( array_map( 'sanitize_text_field', $b['sizes'] ) ) ) : array();
	$unavail  = isset( $b['unavailable'] ) && is_array( $b['unavailable'] ) ? array_values( array_filter( array_map( 'sanitize_text_field', $b['unavailable'] ) ) ) : array();
	$in_stock = ! empty( $b['in_stock'] ) && ! empty( $sizes );

	if ( ! empty( $sizes ) || ! empty( $unavail ) ) {
		update_post_meta( $pid, '_hainute_sizes', implode( ', ', $sizes ) );
		update_post_meta( $pid, '_hainute_sizes_available', $sizes );
		update_post_meta( $pid, '_hainute_sizes_unavailable', $unavail );
	}

	// Stoc real în oferta FD (nu-l aveam din feed).
	$wpdb->update(
		hainute_offers_table_name(),
		array( 'stock_status' => $in_stock ? HAINUTE_STOCK_IN : HAINUTE_STOCK_OUT ),
		array( 'product_id' => $pid, 'network' => 'profitshare' ),
		array( '%s' ),
		array( '%d', '%s' )
	);

	update_post_meta( $pid, '_hainute_fd_crawled', time() );
	hainute_mark_stock_checked( $pid );
	return rest_ensure_response( array( 'ok' => true, 'product_id' => $pid, 'sizes' => count( $sizes ), 'in_stock' => $in_stock ) );
}

/**
 * Ștergere ȚINTITĂ Fashion Days (Profitshare): șterge ofertele profitshare;
 * produsele rămase fără nicio ofertă (FD-only) se șterg; cele cross-store
 * (au și alt magazin) se păstrează, doar reîmprospătate. Resetează cursorul FD
 * și dicționarul de mărimi stricat. Pregătește un re-import curat.
 *   GET /wp-json/hainute/v1/wipe-fd?secret=XXX
 */
function hainute_rest_wipe_fd( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$offers = hainute_offers_table_name();

	$fd_products = $wpdb->get_col( "SELECT DISTINCT product_id FROM {$offers} WHERE network = 'profitshare'" );
	$wpdb->query( "DELETE FROM {$offers} WHERE network = 'profitshare'" );

	$deleted = 0;
	$kept    = 0;
	foreach ( $fd_products as $pid ) {
		$pid       = (int) $pid;
		$remaining = (int) $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(*) FROM {$offers} WHERE product_id = %d", $pid ) );
		if ( 0 === $remaining ) {
			wp_delete_post( $pid, true );
			$deleted++;
		} else {
			hainute_refresh_min_price_meta( $pid );
			hainute_refresh_store_count_meta( $pid );
			$kept++;
		}
	}

	delete_option( 'hainute_ps_cursor' );  // re-import de la pagina 1
	delete_option( 'hainute_size_dict' );  // dicționarul stricat

	return rest_ensure_response( array(
		'ok'                    => true,
		'produse_fd_sterse'     => $deleted,
		'produse_cross_pastrate'=> $kept,
	) );
}

/**
 * Codul de model „căutabil" al unui produs (pt căutare pe magazinele externe):
 * CJ → primul segment din sku crawluit (ex. B6563A); altfel → derivat din URL.
 * Întoarce [ brand, code ] sau ['',''] dacă n-avem cod utilizabil.
 */
function hainute_search_code_for_product( $pid ) {
	$brand = (string) get_post_meta( $pid, '_hainute_match_brand', true );
	if ( '' === $brand ) {
		// Fallback pe brandul din taxonomie (match_brand e setat doar la matching).
		$t     = get_the_terms( $pid, 'product_brand' );
		$brand = ( $t && ! is_wp_error( $t ) ) ? $t[0]->name : '';
	}
	$mc    = (string) get_post_meta( $pid, '_hainute_model_code', true );
	$code  = hainute_model_base_code( $mc );

	if ( '' === $code ) {
		global $wpdb;
		$url = $wpdb->get_var( $wpdb->prepare( "SELECT affiliate_url FROM " . hainute_offers_table_name() . " WHERE product_id = %d LIMIT 1", $pid ) );
		$code = hainute_model_base_code( hainute_model_code_from_url( hainute_enrich_real_url( (string) $url ) ) );
	}

	// Prea scurt / pur numeric foarte scurt → nedistinctiv pt căutare.
	if ( strlen( $code ) < 5 && ! preg_match( '/[a-z]/', $code ) ) {
		$code = '';
	}
	return array( $brand, $code );
}

/**
 * Coada comparatorului: produse cu un cod de model căutabil, încă necomparate
 * cu magazinele externe.
 *   GET /wp-json/hainute/v1/compare-queue?secret=XXX&limit=30
 */
function hainute_rest_compare_queue( WP_REST_Request $request ) {
	global $wpdb;
	$limit = max( 1, min( 100, (int) $request->get_param( 'limit' ) ?: 30 ) );

	// Mod țintit: ?ids=1,2,3 → doar acele produse (pt test/demo), ignoră marcajul.
	$ids_param = (string) $request->get_param( 'ids' );
	if ( '' !== $ids_param ) {
		$want  = array_filter( array_map( 'intval', explode( ',', $ids_param ) ) );
		$queue = array();
		foreach ( $want as $pid ) {
			list( $brand, $code ) = hainute_search_code_for_product( $pid );
			if ( '' !== $code && '' !== $brand ) {
				$queue[] = array( 'product_id' => $pid, 'brand' => $brand, 'code' => $code );
			}
		}
		return rest_ensure_response( array( 'ok' => true, 'queue' => $queue, 'remaining' => 0 ) );
	}

	// Filtru încălțăminte: magazinele externe (giraffe/Sportisimo) sunt de pantofi,
	// deci pt eficiență crawluim doar produsele din categorii de încălțăminte.
	$foot = '';
	if ( $request->get_param( 'footwear' ) ) {
		$foot = " AND p.ID IN (
			SELECT tr.object_id FROM {$wpdb->term_relationships} tr
			INNER JOIN {$wpdb->term_taxonomy} tt ON tt.term_taxonomy_id = tr.term_taxonomy_id AND tt.taxonomy='product_cat'
			INNER JOIN {$wpdb->terms} t ON t.term_id = tt.term_id
			WHERE t.name REGEXP 'pantof|sandal|ghet|adidas|papuc|sneaker|cizm|balerin|slap|incalt|espadril|mocasin|teni'
		)";
	}
	// Filtru lux: pt cross-check pe Farfetch (interogat doar pt brandurile astea).
	if ( $request->get_param( 'luxury' ) ) {
		$foot .= " AND p.ID IN (
			SELECT tr.object_id FROM {$wpdb->term_relationships} tr
			INNER JOIN {$wpdb->term_taxonomy} tt ON tt.term_taxonomy_id = tr.term_taxonomy_id AND tt.taxonomy='product_brand'
			INNER JOIN {$wpdb->terms} t ON t.term_id = tt.term_id
			WHERE t.name REGEXP 'kenzo|boss|hugo|moncler|calvin klein|polo ralph|armani|ea7|karl lagerfeld|diesel|guess|dsquared|fendi|versace|michael kors|dolce|givenchy|balmain|off.white|palm angels|marc jacobs|burberry|stone island'
		)";
	}

	$ids = $wpdb->get_col(
		$wpdb->prepare(
			"SELECT p.ID FROM {$wpdb->posts} p
			LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id = p.ID AND pm.meta_key = '_hainute_compared'
			WHERE p.post_type='product' AND p.post_status='publish' AND pm.meta_id IS NULL {$foot}
			ORDER BY p.ID LIMIT %d",
			$limit
		)
	);

	$queue = array();
	foreach ( $ids as $pid ) {
		list( $brand, $code ) = hainute_search_code_for_product( (int) $pid );
		if ( '' === $code || '' === $brand ) {
			update_post_meta( (int) $pid, '_hainute_compared', 0 ); // fără cod → sărim, dar marcăm
			continue;
		}
		$queue[] = array( 'product_id' => (int) $pid, 'brand' => $brand, 'code' => $code );
	}

	$remaining = (int) $wpdb->get_var(
		"SELECT COUNT(*) FROM {$wpdb->posts} p
		LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id = p.ID AND pm.meta_key = '_hainute_compared'
		WHERE p.post_type='product' AND p.post_status='publish' AND pm.meta_id IS NULL {$foot}"
	);

	return rest_ensure_response( array( 'ok' => true, 'queue' => $queue, 'remaining' => $remaining ) );
}

/**
 * Primește o ofertă de la un magazin EXTERN (non-afiliat) și o bagă în panoul de
 * disponibilitate, sau marchează produsul „comparat".
 *   POST /wp-json/hainute/v1/external-offer?secret=XXX
 *   body: { product_id, store, slug, price, currency, url, in_stock }  (ofertă)
 *      sau { product_id, done:true }                                    (marcaj)
 */
function hainute_rest_external_offer( WP_REST_Request $request ) {
	$b   = $request->get_json_params();
	$pid = isset( $b['product_id'] ) ? (int) $b['product_id'] : 0;
	if ( ! $pid || 'product' !== get_post_type( $pid ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'product_id invalid' ) );
	}

	if ( ! empty( $b['done'] ) ) {
		update_post_meta( $pid, '_hainute_compared', time() );
		return rest_ensure_response( array( 'ok' => true, 'marcat' => true ) );
	}

	$slug = sanitize_key( $b['slug'] ?? '' );
	$url  = esc_url_raw( $b['url'] ?? '' );
	if ( '' === $slug || '' === $url || ! isset( $b['price'] ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'câmpuri lipsă (slug/url/price)' ) );
	}

	$store_id = hainute_upsert_store(
		sanitize_text_field( $b['store'] ?? $slug ),
		array( 'network' => 'external', 'program_id' => $slug, 'website' => $url )
	);
	if ( is_wp_error( $store_id ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => $store_id->get_error_message() ) );
	}

	$ok = hainute_upsert_offer(
		$pid,
		(int) $store_id,
		array(
			'network'       => 'external:' . $slug,
			'external_id'   => $slug . ':' . substr( md5( $url ), 0, 16 ),
			'price'         => (float) $b['price'],
			'currency'      => sanitize_text_field( $b['currency'] ?? 'RON' ),
			'stock_status'  => ! empty( $b['in_stock'] ) ? HAINUTE_STOCK_IN : HAINUTE_STOCK_OUT,
			'affiliate_url' => $url,
		)
	);

	// Mărimile DISPONIBILE la acest magazin (pt comparație per mărime).
	if ( isset( $b['sizes'] ) && is_array( $b['sizes'] ) ) {
		$map = get_post_meta( $pid, '_hainute_store_sizes', true );
		if ( ! is_array( $map ) ) {
			$map = array();
		}
		$map[ (int) $store_id ] = array_values( array_filter( array_map( 'sanitize_text_field', $b['sizes'] ) ) );
		update_post_meta( $pid, '_hainute_store_sizes', $map );
	}

	hainute_set_ext_color( $pid, (int) $store_id, (string) ( $b['color'] ?? '' ) );
	hainute_set_ext_image( $pid, (int) $store_id, (string) ( $b['image'] ?? '' ) );
	hainute_mark_stock_checked( $pid );

	return rest_ensure_response( array( 'ok' => (bool) $ok, 'product_id' => $pid, 'store' => $slug ) );
}

/**
 * Coadă de RE-verificare (cron): produse deja crawluite, cu ofertă în sursă,
 * ordonate cele mai vechi verificate întâi, cu produsele „fierbinți" (multe
 * vizualizări recente) puse în față ca să li se reîmprospăteze stocul rapid.
 *   GET /recrawl-queue?secret=XXX&source=cj|fd&limit=80&brand=nike&hot=1
 *
 * Cadență: un produs e „scadent" dacă a fost verificat acum > HAINUTE_RECRAWL_HOURS
 * (12h → de 2 ori pe zi); unul fierbinte, > HAINUTE_RECRAWL_HOT_HOURS (2h).
 */
function hainute_rest_recrawl_queue( WP_REST_Request $request ) {
	global $wpdb;
	$src    = sanitize_key( $request->get_param( 'source' ) ?: 'cj' );
	$limit  = max( 1, min( 500, (int) $request->get_param( 'limit' ) ?: 80 ) );
	$brand  = sanitize_text_field( (string) $request->get_param( 'brand' ) );
	$hot_only = ! empty( $request->get_param( 'hot' ) );

	$netmap = array( 'cj' => 'cj', 'fd' => 'profitshare', 'vb' => '2performant' );
	if ( ! isset( $netmap[ $src ] ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'source invalid (cj|fd|vb)' ) );
	}
	$network = $netmap[ $src ];
	$offers  = hainute_offers_table_name();
	$now     = time();

	// Țintit: `ids=1,2,3` → exact acele produse, indiferent când au fost verificate.
	$ids = array_filter( array_map( 'intval', explode( ',', (string) $request->get_param( 'ids' ) ) ) );
	if ( $ids ) {
		$in    = implode( ',', $ids );
		$rows  = $wpdb->get_results( $wpdb->prepare( "SELECT product_id, MIN(affiliate_url) AS url FROM {$offers} WHERE network=%s AND product_id IN ({$in}) GROUP BY product_id", $network ) );
		$queue = array();
		foreach ( $rows as $r ) {
			$terms   = get_the_terms( (int) $r->product_id, 'product_brand' );
			$queue[] = array(
				'product_id' => (int) $r->product_id,
				'url'        => function_exists( 'hainute_enrich_real_url' ) ? hainute_enrich_real_url( $r->url ) : $r->url,
				'brand'      => ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '',
				'checked'    => 0,
				'hot'        => false,
			);
		}
		return rest_ensure_response( array( 'ok' => true, 'source' => $src, 'queue' => $queue, 'count' => count( $queue ) ) );
	}
	$normal  = (int) hainute_config( 'HAINUTE_RECRAWL_HOURS', 12 ) * 3600;
	$hot_win = (int) hainute_config( 'HAINUTE_RECRAWL_HOT_HOURS', 2 ) * 3600;

	// Bazin generos ordonat vechi→nou; filtrăm/repriorizăm în PHP.
	$pool = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT o.product_id, MIN(o.affiliate_url) AS url, COALESCE(MAX(pm.meta_value+0),0) AS checked
			FROM {$offers} o
			INNER JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status='publish'
			LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id = o.product_id AND pm.meta_key='_hainute_stock_checked'
			WHERE o.network=%s
			GROUP BY o.product_id
			ORDER BY checked ASC
			LIMIT %d",
			$network,
			$limit * 5
		)
	);

	$hot = array();
	$due = array();
	foreach ( $pool as $r ) {
		$pid = (int) $r->product_id;
		if ( $brand ) {
			$terms = get_the_terms( $pid, 'product_brand' );
			$bname = ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '';
			if ( 0 !== strcasecmp( $bname, $brand ) ) {
				continue;
			}
		}
		$age    = $now - (int) $r->checked;
		$is_hot = function_exists( 'hainute_is_hot' ) && hainute_is_hot( $pid );
		$url    = function_exists( 'hainute_enrich_real_url' ) ? hainute_enrich_real_url( $r->url ) : $r->url;
		if ( 'cj' === $src && false !== stripos( $url, 'sportisimo' ) ) {
			continue; // Sportisimo are lanul lui (sportisimo.js: preț + mărimi)
		}
		$terms  = get_the_terms( $pid, 'product_brand' );
		$item   = array(
			'product_id' => $pid,
			'url'        => $url,
			'brand'      => ( $terms && ! is_wp_error( $terms ) ) ? $terms[0]->name : '',
			'checked'    => (int) $r->checked,
			'hot'        => $is_hot,
		);
		if ( $is_hot && $age >= $hot_win ) {
			$hot[] = $item;
		} elseif ( ! $hot_only && $age >= $normal ) {
			$due[] = $item;
		}
	}

	// Fierbinți întâi; restul grupate pe brand (rulare coerentă + politicoasă).
	usort( $due, function ( $a, $b ) {
		$c = strcasecmp( $a['brand'], $b['brand'] );
		return 0 !== $c ? $c : ( $a['checked'] <=> $b['checked'] );
	} );
	$queue = array_slice( array_merge( $hot, $due ), 0, $limit );

	return rest_ensure_response( array(
		'ok'     => true,
		'source' => $src,
		'hot'    => count( $hot ),
		'total'  => count( $queue ),
		'queue'  => $queue,
	) );
}

/**
 * Coada de crawl: produse Answear (rețea cj) încă ne-îmbogățite, cu URL-ul REAL
 * al paginii. Crawler-ul Node cere loturi de aici până se golește.
 *   GET /wp-json/hainute/v1/crawl-queue?secret=XXX&limit=50
 */
function hainute_rest_crawl_queue( WP_REST_Request $request ) {
	global $wpdb;

	$limit  = max( 1, min( 200, (int) $request->get_param( 'limit' ) ?: 50 ) );
	$offers = hainute_offers_table_name();

	$rows = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT o.product_id, MIN(o.affiliate_url) AS url
			FROM {$offers} o
			INNER JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status = 'publish'
			LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id = o.product_id AND pm.meta_key = '_hainute_size_crawled'
			WHERE o.network = 'cj' AND pm.meta_id IS NULL
			GROUP BY o.product_id
			LIMIT %d",
			$limit
		)
	);

	$queue = array();
	foreach ( $rows as $r ) {
		$url = hainute_enrich_real_url( $r->url );
		if ( false !== strpos( $url, 'answear' ) ) {
			$queue[] = array( 'product_id' => (int) $r->product_id, 'url' => $url );
		} else {
			// URL non-answear (deep-link nedecodabil etc.) → marcăm ca „încercat" ca să nu blocheze coada.
			update_post_meta( (int) $r->product_id, '_hainute_size_crawled', 0 );
		}
	}

	$remaining = (int) $wpdb->get_var(
		"SELECT COUNT(*) FROM (
			SELECT o.product_id FROM {$offers} o
			INNER JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status = 'publish'
			LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id = o.product_id AND pm.meta_key = '_hainute_size_crawled'
			WHERE o.network = 'cj' AND pm.meta_id IS NULL
			GROUP BY o.product_id
		) t"
	);

	return rest_ensure_response( array( 'ok' => true, 'queue' => $queue, 'remaining' => $remaining ) );
}

/**
 * Primește rezultatul unui crawl și-l stochează pe produs.
 *   POST /wp-json/hainute/v1/crawl-result?secret=XXX
 *   body JSON: { product_id, sizes:[], availability, sku }
 */
function hainute_rest_crawl_result( WP_REST_Request $request ) {
	$body = $request->get_json_params();
	$pid  = isset( $body['product_id'] ) ? (int) $body['product_id'] : 0;
	if ( ! $pid || 'product' !== get_post_type( $pid ) ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'product_id invalid' ) );
	}

	$sizes = isset( $body['sizes'] ) && is_array( $body['sizes'] ) ? array_values( array_filter( array_map( 'sanitize_text_field', $body['sizes'] ) ) ) : array();

	// Mărimile de la Answear = mărimile DISPONIBILE (site-ul le listează doar pe
	// cele pe stoc), deci lista e autoritativă pentru acest produs.
	$sizes = function_exists( 'hainute_norm_sizes' ) ? hainute_norm_sizes( $sizes ) : $sizes;
	// Lista completă (dropdown-ul Answear: disponibile + epuizate) → o salvăm și
	// când nu e nicio mărime disponibilă, ca să nu rămână mărimi vechi.
	if ( ! empty( $body['complete'] ) || isset( $body['unavailable'] ) ) {
		$unav = function_exists( 'hainute_norm_sizes' ) ? hainute_norm_sizes( (array) ( $body['unavailable'] ?? array() ) ) : array();
		update_post_meta( $pid, '_hainute_sizes_unavailable', array_values( array_diff( $unav, $sizes ) ) );
		if ( ! empty( $body['complete'] ) && empty( $sizes ) ) {
			update_post_meta( $pid, '_hainute_sizes_available', array() );
		}
	}
	if ( ! empty( $sizes ) ) {
		update_post_meta( $pid, '_hainute_sizes', implode( ', ', $sizes ) );
		update_post_meta( $pid, '_hainute_sizes_available', $sizes ); // pt afișare „disponibil per mărime"
	}
	if ( ! empty( $body['sku'] ) ) {
		update_post_meta( $pid, '_hainute_model_code', sanitize_text_field( $body['sku'] ) );
	}
	if ( ! empty( $body['availability'] ) ) {
		update_post_meta( $pid, '_hainute_crawl_availability', sanitize_text_field( $body['availability'] ) );
	}

	// Actualizează STOCUL ofertei Answear (cj) din realitatea paginii — așa
	// re-crawl-ul reîmprospătează stocul, nu doar mărimile (repară stoc vechi din
	// feed, ex. produse marcate fără stoc dar disponibile pe site). JSON-LD Answear
	// e de încredere; schimbăm doar când semnalul e clar.
	$av  = strtolower( str_replace( ' ', '', (string) ( $body['availability'] ?? '' ) ) );
	$new = null;
	if ( false !== strpos( $av, 'outofstock' ) || false !== strpos( $av, 'soldout' ) ) {
		$new = HAINUTE_STOCK_OUT;
	} elseif ( false !== strpos( $av, 'instock' ) || ! empty( $sizes ) ) {
		$new = HAINUTE_STOCK_IN;
	}
	if ( null !== $new ) {
		global $wpdb;
		$wpdb->update(
			hainute_offers_table_name(),
			array( 'stock_status' => $new ),
			array( 'product_id' => $pid, 'network' => 'cj' ),
			array( '%s' ),
			array( '%d', '%s' )
		);
	}
	// Prețul curent de pe pagina Answear (doar oferta Answear a produsului).
	$price = isset( $body['price'] ) ? (float) $body['price'] : 0;
	if ( $price > 0 ) {
		global $wpdb;
		$t = hainute_offers_table_name();
		$wpdb->query( $wpdb->prepare( "UPDATE {$t} SET price = %f, updated_at = %s WHERE product_id = %d AND network = 'cj' AND affiliate_url LIKE %s", $price, current_time( 'mysql' ), $pid, '%answear%' ) );
	}
	if ( function_exists( 'hainute_refresh_buyable' ) ) {
		hainute_refresh_buyable( $pid );
	}

	update_post_meta( $pid, '_hainute_size_crawled', time() );
	hainute_mark_stock_checked( $pid );

	return rest_ensure_response( array( 'ok' => true, 'product_id' => $pid, 'sizes' => count( $sizes ), 'stock' => $new ) );
}

/**
 * Codul de model de BAZĂ (fără sufixele de culoare/mărime): primul segment
 * alfanumeric, ≥4 caractere. „B655WA.08514.20.27" → „b655wa".
 */
function hainute_model_base_code( $code ) {
	$c   = preg_replace( '/[^a-z0-9.]/', '', strtolower( trim( (string) $code ) ) );
	$seg = explode( '.', $c );
	return strlen( $seg[0] ) >= 4 ? $seg[0] : '';
}

/**
 * Codul de model derivat din URL-ul REAL al magazinului (per magazin). Mai de
 * încredere decât meta stocat (care e corect doar la Answear, din crawl).
 * Answear: „...-408801-1843621"; various-brands: „...-397943-02.html";
 * Fashion Days: „...-bb2502-copii-...".
 */
function hainute_model_code_from_url( $url ) {
	$url = strtolower( (string) $url );
	$p   = (string) ( parse_url( $url, PHP_URL_PATH ) ?: $url );
	if ( false !== strpos( $url, 'answear' ) ) {
		return preg_match( '/-([a-z]*\d[a-z0-9]*)-\d{5,}(?:$|[\/?])/', $p, $x ) ? $x[1] : '';
	}
	if ( false !== strpos( $url, 'fashiondays' ) ) {
		return preg_match( '/-([a-z]*\d[a-z0-9]{2,})-[a-z]/', $p, $x ) ? $x[1] : '';
	}
	if ( false !== strpos( $url, 'various-brands' ) ) {
		return preg_match( '/-([a-z]*\d[a-z0-9]*)-\d+\.html/', $p, $x ) ? $x[1] : '';
	}
	return '';
}

/**
 * Comasare pe COD DE MODEL: produsele cu aceeași marcă + cod model de bază sunt
 * același model în culori diferite → un singur produs, cu culorile ca variante
 * (fiecare cu poza, linkul, prețul și MĂRIMILE ei). Modelele cu cod diferit
 * rămân separate (ex. Geox B655WA ≠ B6563A).
 *
 * Implicit rulează în DRY-RUN (doar raportează). Comasare reală: &dry_run=0.
 *   GET /wp-json/hainute/v1/regroup?secret=XXX          (preview)
 *   GET /wp-json/hainute/v1/regroup?secret=XXX&dry_run=0 (comasează)
 *   opțional &limit=N (câte grupuri, pt test)
 */
function hainute_rest_regroup( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}

	$dry_param = (string) $request->get_param( 'dry_run' );
	$dry       = ! ( '0' === $dry_param || 'false' === $dry_param );
	$limit     = max( 0, (int) $request->get_param( 'limit' ) );
	$offers    = hainute_offers_table_name();

	// Marcă + cod crawluit (sku Answear) per produs.
	$pinfo = array();
	$meta  = $wpdb->get_results(
		"SELECT p.ID AS id, COALESCE(b.meta_value,'') AS brand, COALESCE(mc.meta_value,'') AS mc
		FROM {$wpdb->posts} p
		LEFT JOIN {$wpdb->postmeta} b  ON b.post_id  = p.ID AND b.meta_key='_hainute_match_brand'
		LEFT JOIN {$wpdb->postmeta} mc ON mc.post_id = p.ID AND mc.meta_key='_hainute_model_code'
		WHERE p.post_type='product' AND p.post_status='publish'"
	);
	foreach ( $meta as $x ) {
		$pinfo[ (int) $x->id ] = array( 'brand' => $x->brand, 'mc' => $x->mc );
	}

	// Cod per ofertă: CJ → sku crawluit (fiabil pt model), restul → URL.
	// Un produs cu coduri în CONFLICT e comasat greșit de matcher-ul vechi → sărit.
	$by_prod = array();
	foreach ( $wpdb->get_results( "SELECT product_id, network, affiliate_url FROM {$offers}" ) as $o ) {
		$pid = (int) $o->product_id;
		if ( ! isset( $pinfo[ $pid ] ) ) {
			continue;
		}
		if ( 'cj' === $o->network ) {
			$bc = hainute_model_base_code( $pinfo[ $pid ]['mc'] );
		} else {
			$bc = hainute_model_base_code( hainute_model_code_from_url( hainute_enrich_real_url( $o->affiliate_url ) ) );
		}
		if ( '' === $bc ) {
			continue;
		}
		$by_prod[ $pid ]['brand']        = $pinfo[ $pid ]['brand'];
		$by_prod[ $pid ]['codes'][ $bc ] = 1;
	}

	$groups       = array();
	$contaminated = 0;
	foreach ( $by_prod as $pid => $d ) {
		$codes = array_keys( $d['codes'] );
		if ( 1 !== count( $codes ) ) {
			$contaminated++; // 0 sau 2+ coduri → nu grupăm
			continue;
		}
		$groups[ strtolower( $d['brand'] ) . '|' . $codes[0] ][] = $pid;
	}

	$preview     = array();
	$merged      = 0;
	$groups_done = 0;

	foreach ( $groups as $gk => $ids ) {
		if ( count( $ids ) < 2 ) {
			continue;
		}
		if ( $limit && $groups_done >= $limit ) {
			break;
		}
		$groups_done++;

		if ( $dry ) {
			$prods = array();
			foreach ( $ids as $pid ) {
				$col = (string) get_post_meta( $pid, '_hainute_colors', true );
				$prods[] = '#' . $pid . ' ' . get_the_title( $pid ) . ' [' . ( $col ?: '?' ) . ']';
			}
			$preview[] = array( 'grup' => $gk, 'produse' => $prods );
			continue;
		}

		// Canonic = cel cu cele mai multe magazine, tie-break ID minim.
		$sc = array();
		foreach ( $ids as $pid ) {
			$sc[ $pid ] = (int) $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(DISTINCT store_id) FROM {$offers} WHERE product_id=%d", $pid ) );
		}
		usort( $ids, function ( $a, $b ) use ( $sc ) { return $sc[ $a ] !== $sc[ $b ] ? $sc[ $b ] - $sc[ $a ] : $a - $b; } );
		$canon = array_shift( $ids );

		foreach ( $ids as $dup ) {
			$dup_offer = $wpdb->get_row( $wpdb->prepare( "SELECT * FROM {$offers} WHERE product_id=%d ORDER BY price ASC LIMIT 1", $dup ) );

			$variants = get_post_meta( $canon, '_hainute_variant_offers', true );
			if ( ! is_array( $variants ) ) {
				$variants = array();
			}
			$variants[ 'm' . $dup ] = array(
				'store_id' => $dup_offer ? (int) $dup_offer->store_id : 0,
				'url'      => $dup_offer ? (string) $dup_offer->affiliate_url : '',
				'image'    => (string) get_post_meta( $dup, '_hainute_image_url', true ),
				'price'    => $dup_offer ? (float) $dup_offer->price : 0,
				'currency' => $dup_offer ? (string) $dup_offer->currency : 'RON',
				'in_stock' => $dup_offer ? ( 'out_of_stock' !== $dup_offer->stock_status ) : true,
				'color'    => (string) get_post_meta( $dup, '_hainute_colors', true ),
				'sizes'    => (string) get_post_meta( $dup, '_hainute_sizes', true ),
			);
			update_post_meta( $canon, '_hainute_variant_offers', $variants );

			// Mută ofertele din magazine noi la canonic (cross-store); același magazin → rămâne doar în variantă.
			foreach ( $wpdb->get_results( $wpdb->prepare( "SELECT * FROM {$offers} WHERE product_id=%d", $dup ) ) as $o ) {
				if ( hainute_get_offer_for_store( $canon, (int) $o->store_id ) ) {
					$wpdb->delete( $offers, array( 'id' => (int) $o->id ), array( '%d' ) );
				} else {
					$wpdb->update( $offers, array( 'product_id' => $canon ), array( 'id' => (int) $o->id ), array( '%d' ), array( '%d' ) );
				}
			}

			$dcol = (string) get_post_meta( $dup, '_hainute_colors', true );
			if ( '' !== $dcol ) {
				foreach ( array_map( 'trim', explode( ',', $dcol ) ) as $cc ) {
					hainute_add_list_meta( $canon, '_hainute_colors', $cc );
				}
			}

			// Trash (nu ștergere definitivă) — recuperabil dacă ceva nu iese bine.
			// Ofertele au fost deja mutate/șterse, deci hook-ul de trash n-are ce curăța.
			wp_trash_post( $dup );
			$merged++;
		}

		$sids = $wpdb->get_col( $wpdb->prepare( "SELECT DISTINCT store_id FROM {$offers} WHERE product_id=%d", $canon ) );
		if ( $sids ) {
			wp_set_object_terms( $canon, array_map( 'intval', $sids ), 'store', false );
		}
		hainute_refresh_min_price_meta( $canon );
		hainute_refresh_store_count_meta( $canon );
	}

	if ( $dry ) {
		return rest_ensure_response( array(
			'ok'                 => true,
			'mod'                => 'DRY-RUN (nimic modificat)',
			'grupuri_de_comasat' => count( $preview ),
			'produse_contaminate'=> $contaminated,
			'preview'            => array_slice( $preview, 0, $limit ?: 40 ),
		) );
	}

	return rest_ensure_response( array( 'ok' => true, 'mod' => 'COMASAT', 'grupuri' => $groups_done, 'produse_absorbite' => $merged ) );
}

/**
 * Numerele „de versiune" din două chei trebuie să coincidă ca să unim (altfel
 * „Star Runner 4" ≠ „Star Runner 5", „Air Max 90" ≠ „Air Max 97"). Numerele
 * comune sunt ok (ex. ambele „25"); numere DIFERITE = modele diferite.
 */
function hainute_nums_match( $a, $b ) {
	$na = array_values( array_filter( explode( ' ', $a ), 'is_numeric' ) );
	$nb = array_values( array_filter( explode( ' ', $b ), 'is_numeric' ) );
	sort( $na );
	sort( $nb );
	return $na === $nb;
}

/**
 * Grupare FUZZY pe nume (pt cazuri ca adidas Squadra, unde fiecare culoare are
 * cod diferit → gruparea pe cod nu le unește). Clusterizează produsele aceleiași
 * mărci care împart o ancoră distinctivă + similaritate mare (aceeași logică de
 * încredere ca matcher-ul). Implicit DRY-RUN. Real: &dry_run=0.
 */
function hainute_rest_regroup_names( WP_REST_Request $request ) {
	global $wpdb;
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	$dry_param = (string) $request->get_param( 'dry_run' );
	$dry       = ! ( '0' === $dry_param || 'false' === $dry_param );
	$limit     = max( 0, (int) $request->get_param( 'limit' ) );
	$offers    = hainute_offers_table_name();

	$rows = $wpdb->get_results(
		"SELECT p.ID AS id, k.meta_value AS kk, COALESCE(b.meta_value,'') AS brand
		FROM {$wpdb->posts} p
		INNER JOIN {$wpdb->postmeta} k ON k.post_id = p.ID AND k.meta_key = '_hainute_match_key'
		LEFT JOIN {$wpdb->postmeta} b ON b.post_id = p.ID AND b.meta_key = '_hainute_match_brand'
		WHERE p.post_type='product' AND p.post_status='publish' AND k.meta_value <> ''"
	);

	$by_brand = array();
	foreach ( $rows as $r ) {
		$key = trim( $r->kk );
		if ( count( array_filter( explode( ' ', $key ) ) ) < 2 ) {
			continue;
		}
		$by_brand[ strtolower( $r->brand ) ][] = array( 'id' => (int) $r->id, 'key' => $key );
	}

	$clusters = array();
	foreach ( $by_brand as $brand => $prods ) {
		$n = count( $prods );
		if ( '' === $brand || $n < 2 || $n > 400 ) { // sar mărcile uriașe (cost O(n²))
			continue;
		}
		$parent = range( 0, $n - 1 );
		$find   = function ( $x ) use ( &$parent ) {
			while ( $parent[ $x ] !== $x ) { $parent[ $x ] = $parent[ $parent[ $x ] ]; $x = $parent[ $x ]; }
			return $x;
		};
		for ( $i = 0; $i < $n; $i++ ) {
			for ( $j = $i + 1; $j < $n; $j++ ) {
				list( $shared, $anchor ) = hainute_shared_anchor( $prods[ $i ]['key'], $prods[ $j ]['key'] );
				if ( $anchor && $shared >= 2
					&& hainute_similarity( $prods[ $i ]['key'], $prods[ $j ]['key'] ) >= HAINUTE_MATCH_BRANDED
					&& hainute_nums_match( $prods[ $i ]['key'], $prods[ $j ]['key'] ) ) {
					$ri = $find( $i ); $rj = $find( $j );
					if ( $ri !== $rj ) { $parent[ $ri ] = $rj; }
				}
			}
		}
		$groups = array();
		for ( $i = 0; $i < $n; $i++ ) { $groups[ $find( $i ) ][] = $prods[ $i ]['id']; }
		foreach ( $groups as $g ) {
			if ( count( $g ) > 1 ) { $clusters[] = $g; }
		}
	}

	if ( $dry ) {
		$preview = array();
		$total   = 0;
		foreach ( $clusters as $g ) {
			$total += count( $g );
			if ( count( $preview ) < ( $limit ?: 60 ) ) {
				$items = array();
				foreach ( $g as $pid ) { $items[] = '#' . $pid . ' ' . get_the_title( $pid ); }
				$preview[] = $items;
			}
		}
		return rest_ensure_response( array( 'ok' => true, 'mod' => 'DRY-RUN (nimic modificat)', 'grupuri' => count( $clusters ), 'produse_implicate' => $total, 'preview' => $preview ) );
	}

	// Merge real: canonic = cel cu cele mai multe magazine; ceilalți → variante.
	$merged = 0;
	foreach ( $clusters as $ids ) {
		$sc = array();
		foreach ( $ids as $pid ) {
			$sc[ $pid ] = (int) $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(DISTINCT store_id) FROM {$offers} WHERE product_id=%d", $pid ) );
		}
		usort( $ids, function ( $a, $b ) use ( $sc ) { return $sc[ $a ] !== $sc[ $b ] ? $sc[ $b ] - $sc[ $a ] : $a - $b; } );
		$canon = array_shift( $ids );
		foreach ( $ids as $dup ) {
			$dup_offer = $wpdb->get_row( $wpdb->prepare( "SELECT * FROM {$offers} WHERE product_id=%d ORDER BY price ASC LIMIT 1", $dup ) );
			$variants  = get_post_meta( $canon, '_hainute_variant_offers', true );
			if ( ! is_array( $variants ) ) { $variants = array(); }
			$variants[ 'm' . $dup ] = array(
				'store_id' => $dup_offer ? (int) $dup_offer->store_id : 0,
				'url'      => $dup_offer ? (string) $dup_offer->affiliate_url : '',
				'image'    => (string) get_post_meta( $dup, '_hainute_image_url', true ),
				'price'    => $dup_offer ? (float) $dup_offer->price : 0,
				'currency' => $dup_offer ? (string) $dup_offer->currency : 'RON',
				'in_stock' => $dup_offer ? ( 'out_of_stock' !== $dup_offer->stock_status ) : true,
				'color'    => (string) get_post_meta( $dup, '_hainute_colors', true ),
				'sizes'    => (string) get_post_meta( $dup, '_hainute_sizes', true ),
			);
			update_post_meta( $canon, '_hainute_variant_offers', $variants );
			foreach ( $wpdb->get_results( $wpdb->prepare( "SELECT * FROM {$offers} WHERE product_id=%d", $dup ) ) as $o ) {
				if ( hainute_get_offer_for_store( $canon, (int) $o->store_id ) ) {
					$wpdb->delete( $offers, array( 'id' => (int) $o->id ), array( '%d' ) );
				} else {
					$wpdb->update( $offers, array( 'product_id' => $canon ), array( 'id' => (int) $o->id ), array( '%d' ), array( '%d' ) );
				}
			}
			$dcol = (string) get_post_meta( $dup, '_hainute_colors', true );
			if ( '' !== $dcol ) {
				foreach ( array_map( 'trim', explode( ',', $dcol ) ) as $cc ) { hainute_add_list_meta( $canon, '_hainute_colors', $cc ); }
			}
			wp_trash_post( $dup );
			$merged++;
		}
		$sids = $wpdb->get_col( $wpdb->prepare( "SELECT DISTINCT store_id FROM {$offers} WHERE product_id=%d", $canon ) );
		if ( $sids ) { wp_set_object_terms( $canon, array_map( 'intval', $sids ), 'store', false ); }
		hainute_refresh_min_price_meta( $canon );
		hainute_refresh_store_count_meta( $canon );
	}

	return rest_ensure_response( array( 'ok' => true, 'mod' => 'COMASAT', 'grupuri' => count( $clusters ), 'produse_absorbite' => $merged ) );
}

/**
 * Recuperează URL-ul REAL al magazinului dintr-un link afiliat stocat
 * (Profitshare `?redirect=`, 2Performant `redirect_to=`, deep-link CJ
 * `/type/dlg/{url}`), altfel îl întoarce ca atare (CJ raw).
 */
function hainute_enrich_real_url( $url ) {
	if ( preg_match( '/[?&]redirect=([^&]+)/', $url, $m ) ) {
		return urldecode( $m[1] );
	}
	if ( preg_match( '/redirect_to=([^&]+)/', $url, $m ) ) {
		return urldecode( $m[1] );
	}
	if ( preg_match( '#/type/dlg/(?:sid/[^/]+/)?(.+)$#', $url, $m ) ) {
		return urldecode( $m[1] );
	}
	return (string) $url;
}

/**
 * Backfill: îmbogățește produsele EXISTENTE cu culoare/mărime/material extrase
 * din slug-ul URL-urilor deja stocate (Fashion Days: tot; Answear: culoare).
 * Nu apelează niciun API extern. Pentru mărimile COMPLETE Fashion Days (câte un
 * rând per mărime) e nevoie de re-import; aici prindem ce e în URL-urile stocate.
 *   GET /wp-json/hainute/v1/enrich?secret=XXX
 */
function hainute_rest_enrich( WP_REST_Request $request ) {
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}

	$products = get_posts(
		array(
			'post_type'   => 'product',
			'post_status' => 'publish',
			'numberposts' => -1,
			'fields'      => 'ids',
		)
	);

	$touched = 0;
	$colors  = 0;
	$sizes   = 0;
	$mats    = 0;

	foreach ( $products as $pid ) {
		$urls = array();
		foreach ( hainute_get_offers( $pid ) as $o ) {
			if ( $o->affiliate_url ) {
				$urls[] = $o->affiliate_url;
			}
		}
		$variants = get_post_meta( $pid, '_hainute_variant_offers', true );
		if ( is_array( $variants ) ) {
			foreach ( $variants as $v ) {
				if ( ! empty( $v['url'] ) ) {
					$urls[] = $v['url'];
				}
			}
		}

		$changed = false;

		foreach ( $urls as $u ) {
			$real = hainute_enrich_real_url( $u );
			$host = strtolower( (string) parse_url( $real, PHP_URL_HOST ) );

			if ( false !== strpos( $host, 'fashiondays' ) && function_exists( 'hainute_ps_parse_url' ) ) {
				$d = hainute_ps_parse_url( $real );
				if ( $d['color'] && hainute_enrich_add( $pid, '_hainute_colors', $d['color'] ) ) { $colors++; $changed = true; }
				if ( $d['size'] && hainute_enrich_add( $pid, '_hainute_sizes', $d['size'] ) )   { $sizes++;  $changed = true; }
				if ( $d['material'] && ! get_post_meta( $pid, '_hainute_material', true ) ) {
					update_post_meta( $pid, '_hainute_material', $d['material'] );
					$mats++; $changed = true;
				}
			} elseif ( false !== strpos( $host, 'answear' ) && function_exists( 'hainute_cj_color_from_url' ) ) {
				$c = hainute_cj_color_from_url( $real );
				if ( $c && hainute_enrich_add( $pid, '_hainute_colors', $c ) ) { $colors++; $changed = true; }
			}
		}

		if ( $changed ) {
			$touched++;
		}
	}

	return rest_ensure_response(
		array(
			'ok'              => true,
			'produse_atinse'  => $touched,
			'culori_adaugate' => $colors,
			'marimi_adaugate' => $sizes,
			'materiale'       => $mats,
			'total'           => count( $products ),
		)
	);
}

/**
 * Adaugă o valoare într-un meta-listă doar dacă lipsește; întoarce true dacă a
 * adăugat. (Wrapper subțire peste hainute_add_list_meta, cu detecție de schimbare.)
 */
function hainute_enrich_add( $pid, $key, $value ) {
	$before = (string) get_post_meta( $pid, $key, true );
	if ( function_exists( 'hainute_add_list_meta' ) ) {
		hainute_add_list_meta( $pid, $key, $value );
	}
	return (string) get_post_meta( $pid, $key, true ) !== $before;
}

/**
 * Diagnostic izolat pentru sursa CJ (conectare + mostră produs).
 *   GET /wp-json/hainute/v1/cj-diag?secret=XXX
 */
function hainute_rest_cj_diag( WP_REST_Request $request ) {
	if ( ! function_exists( 'hainute_cj_run_diagnostic' ) ) {
		return rest_ensure_response( array( 'ok' => false, 'notes' => array( 'Sursa CJ nu e încărcată.' ) ) );
	}
	return rest_ensure_response( hainute_cj_run_diagnostic() );
}

/**
 * Curățare unică a duplicatelor existente: produsele publicate care au aceeași
 * marcă + cheie de potrivire (2+ cuvinte) se unesc într-un singur produs
 * canonic. Ofertele din magazine noi se mută la canonic; variantele same-store
 * (altă culoare din același magazin) devin _hainute_variant_offers, ca să nu se
 * piardă niciun link. La final actualizează _hainute_store_count pentru toate.
 *   GET /wp-json/hainute/v1/dedup?secret=XXX
 */
function hainute_rest_dedup( WP_REST_Request $request ) {
	global $wpdb;

	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}

	$offers_table = hainute_offers_table_name();

	// Toate produsele publicate cu cheia + marca lor.
	$rows = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT p.ID,
				k.meta_value AS match_key,
				COALESCE(b.meta_value, '') AS match_brand
			FROM {$wpdb->posts} p
			INNER JOIN {$wpdb->postmeta} k ON k.post_id = p.ID AND k.meta_key = %s
			LEFT JOIN {$wpdb->postmeta} b ON b.post_id = p.ID AND b.meta_key = %s
			WHERE p.post_type = 'product' AND p.post_status = 'publish'",
			HAINUTE_MATCH_META_KEY,
			HAINUTE_MATCH_META_BRAND
		)
	);

	// Grupăm pe marcă|cheie, doar chei cu 2+ cuvinte (la fel ca matcher-ul).
	$groups = array();
	foreach ( $rows as $r ) {
		$key = trim( (string) $r->match_key );
		if ( '' === $key || count( array_filter( explode( ' ', $key ) ) ) < 2 ) {
			continue;
		}
		$gk               = strtolower( $r->match_brand ) . '|' . $key;
		$groups[ $gk ][] = (int) $r->ID;
	}

	$merged  = 0; // produse duplicate absorbite
	$groups_touched = 0;

	foreach ( $groups as $ids ) {
		if ( count( $ids ) < 2 ) {
			continue;
		}
		$groups_touched++;

		// Canonic = cel cu cele mai multe magazine distincte; tie-break ID minim.
		$store_counts = array();
		foreach ( $ids as $pid ) {
			$store_counts[ $pid ] = (int) $wpdb->get_var(
				$wpdb->prepare( "SELECT COUNT(DISTINCT store_id) FROM {$offers_table} WHERE product_id = %d", $pid )
			);
		}
		usort(
			$ids,
			function ( $a, $b ) use ( $store_counts ) {
				if ( $store_counts[ $a ] !== $store_counts[ $b ] ) {
					return $store_counts[ $b ] - $store_counts[ $a ];
				}
				return $a - $b;
			}
		);
		$canonical = array_shift( $ids );

		foreach ( $ids as $dup ) {
			$dup_image = (string) get_post_meta( $dup, '_hainute_image_url', true );
			$dup_offers = $wpdb->get_results(
				$wpdb->prepare( "SELECT * FROM {$offers_table} WHERE product_id = %d", $dup )
			);

			foreach ( $dup_offers as $o ) {
				$canon_has = hainute_get_offer_for_store( $canonical, (int) $o->store_id );
				if ( $canon_has ) {
					// Același magazin ca o ofertă a canonicului → variantă same-store.
					hainute_dedup_store_variant( $canonical, $o, $dup_image );
					$wpdb->delete( $offers_table, array( 'id' => (int) $o->id ), array( '%d' ) );
				} else {
					// Magazin nou pt canonic → mutăm oferta (devine cross-store).
					$wpdb->update(
						$offers_table,
						array( 'product_id' => $canonical ),
						array( 'id' => (int) $o->id ),
						array( '%d' ),
						array( '%d' )
					);
				}
			}

			// Fuzionăm listele de culori/mărimi/coduri.
			foreach ( array( '_hainute_colors', '_hainute_color_codes', '_hainute_size_codes', '_hainute_sizes' ) as $mk ) {
				$vals = (string) get_post_meta( $dup, $mk, true );
				if ( '' !== $vals ) {
					foreach ( array_map( 'trim', explode( ',', $vals ) ) as $val ) {
						hainute_add_list_meta( $canonical, $mk, $val );
					}
				}
			}

			// Fuzionăm variantele deja existente pe duplicat.
			$dup_variants = get_post_meta( $dup, '_hainute_variant_offers', true );
			if ( is_array( $dup_variants ) && $dup_variants ) {
				$canon_variants = get_post_meta( $canonical, '_hainute_variant_offers', true );
				if ( ! is_array( $canon_variants ) ) {
					$canon_variants = array();
				}
				update_post_meta( $canonical, '_hainute_variant_offers', $canon_variants + $dup_variants );
			}

			// Ștergem produsul duplicat (ofertele lui au fost deja mutate/șterse).
			wp_delete_post( $dup, true );
			$merged++;
		}

		// Reîmprospătăm canonicul: taxonomia store, preț minim, nr. magazine.
		$store_ids = $wpdb->get_col(
			$wpdb->prepare( "SELECT DISTINCT store_id FROM {$offers_table} WHERE product_id = %d", $canonical )
		);
		if ( $store_ids ) {
			wp_set_object_terms( $canonical, array_map( 'intval', $store_ids ), 'store', false );
		}
		hainute_refresh_min_price_meta( $canonical );
		hainute_refresh_store_count_meta( $canonical );
	}

	// Backfill _hainute_store_count pt TOATE produsele publicate (pt filtrul cross-store).
	$all = get_posts(
		array(
			'post_type'   => 'product',
			'post_status' => 'publish',
			'numberposts' => -1,
			'fields'      => 'ids',
		)
	);
	foreach ( $all as $pid ) {
		hainute_refresh_store_count_meta( $pid );
	}

	return rest_ensure_response(
		array(
			'ok'             => true,
			'groups_touched' => $groups_touched,
			'merged'         => $merged,
			'total_products' => count( $all ),
		)
	);
}

/**
 * Adaugă o ofertă de duplicat ca variantă same-store pe produsul canonic.
 * Reface forma din _hainute_variant_offers pornind de la rândul ofertei.
 */
function hainute_dedup_store_variant( $canonical, $offer, $image ) {
	$variants = get_post_meta( $canonical, '_hainute_variant_offers', true );
	if ( ! is_array( $variants ) ) {
		$variants = array();
	}
	$variants[ (string) $offer->external_id ] = array(
		'store_id'  => (int) $offer->store_id,
		'url'       => (string) $offer->affiliate_url,
		'image'     => (string) $image,
		'price'     => (float) $offer->price,
		'old_price' => $offer->old_price ? (float) $offer->old_price : null,
		'currency'  => $offer->currency ?: 'RON',
		'in_stock'  => 'out_of_stock' !== $offer->stock_status,
		'color'     => '',
	);
	update_post_meta( $canonical, '_hainute_variant_offers', $variants );
}

/**
 * Exportă toate produsele într-un CSV (descărcabil), cu magazine, prețuri,
 * culori și mărimi. Protejat cu HAINUTE_SYNC_SECRET (același ca sync).
 *   GET /wp-json/hainute/v1/export?secret=XXX
 */
function hainute_rest_export( WP_REST_Request $request ) {
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}

	$products = get_posts(
		array(
			'post_type'      => 'product',
			'post_status'    => 'publish',
			'numberposts'    => -1,
			'fields'         => 'ids',
			'orderby'        => 'title',
			'order'          => 'ASC',
		)
	);

	$fh = fopen( 'php://temp', 'r+' );
	fwrite( $fh, "\xEF\xBB\xBF" ); // BOM pentru Excel
	fputcsv(
		$fh,
		array( 'id', 'scor_prioritate', 'titlu', 'brand', 'cod_cautare', 'categorie', 'gen', 'pret_min', 'culori', 'nr_marimi', 'marimi', 'magazine_afiliate', 'magazine_externe', 'nr_magazine', 'imagine', 'link_produs' )
	);

	foreach ( $products as $pid ) {
		$offers = function_exists( 'hainute_get_offers' ) ? hainute_get_offers( $pid ) : array();

		$aff = array();
		$ext = array();
		foreach ( $offers as $o ) {
			$name  = $o->store ? $o->store->name : '';
			$entry = $name . ' (' . number_format( (float) $o->price, 2 ) . ( 'out_of_stock' === $o->stock_status ? ' fără stoc' : '' ) . ')';
			if ( 0 === strpos( (string) $o->network, 'external' ) ) {
				$ext[] = $entry;
			} else {
				$aff[] = $entry;
			}
		}

		list( , $cod_cautare ) = function_exists( 'hainute_search_code_for_product' ) ? hainute_search_code_for_product( $pid ) : array( '', '' );

		$brand  = '';
		$bt     = get_the_terms( $pid, 'product_brand' );
		if ( $bt && ! is_wp_error( $bt ) ) {
			$brand = $bt[0]->name;
		}
		$cat = '';
		$ct  = get_the_terms( $pid, 'product_cat' );
		if ( $ct && ! is_wp_error( $ct ) ) {
			$cat = $ct[0]->name;
		}
		$gen = '';
		$gt  = get_the_terms( $pid, 'product_gender' );
		if ( $gt && ! is_wp_error( $gt ) ) {
			$gen = $gt[0]->name;
		}

		$colors = (string) get_post_meta( $pid, '_hainute_colors', true );
		$sizes  = function_exists( 'hainute_resolve_sizes' ) ? hainute_resolve_sizes( $pid ) : array( 'count' => 0, 'labels' => array() );
		$img    = (string) get_post_meta( $pid, '_hainute_image_url', true );

		// Scor de prioritate: reach (brand popular, încălțăminte) + verificat
		// (mărimi, culori) + cross-store. Sortezi CSV-ul după el → top produse.
		$in_stock_any = false;
		foreach ( $offers as $o ) {
			if ( 'out_of_stock' !== $o->stock_status ) { $in_stock_any = true; break; }
		}
		$popular = array( 'nike', 'adidas', 'puma', 'reima', 'geox', 'skechers', 'columbia', '4f', 'new balance', 'vans', 'crocs', 'mayoral', 'guess', 'froddo', 'primigi', 'biomecanics', 'coccodrillo', 'calvin klein jeans' );
		$score   = 0;
		if ( count( $offers ) >= 2 ) { $score += 3; }               // cross-store
		if ( (int) $sizes['count'] > 0 ) { $score += 2; }           // mărimi verificate
		if ( '' !== $colors ) { $score += 1; }                      // culori
		if ( in_array( strtolower( $brand ), $popular, true ) ) { $score += 2; } // brand reach
		if ( $in_stock_any ) { $score += 1; }                       // în stoc
		if ( preg_match( '/andale|antofi|neakers|hete|adidasi|papuci/i', (string) get_the_title( $pid ) ) ) { $score += 1; } // încălțăminte

		fputcsv(
			$fh,
			array(
				$pid,
				$score,
				get_the_title( $pid ),
				$brand,
				$cod_cautare,
				$cat,
				$gen,
				hainute_get_min_price( $pid ),
				$colors,
				(int) $sizes['count'],
				! empty( $sizes['labels'] ) ? implode( ', ', $sizes['labels'] ) : '',
				implode( ' | ', $aff ),
				implode( ' | ', $ext ),
				count( $offers ),
				$img,
				get_permalink( $pid ),
			)
		);
	}

	rewind( $fh );
	$csv = stream_get_contents( $fh );
	fclose( $fh );

	// CSV brut (nu prin serializarea JSON a REST-ului).
	if ( ! headers_sent() ) {
		header( 'Content-Type: text/csv; charset=utf-8' );
		header( 'Content-Disposition: attachment; filename="hainute-produse.csv"' );
		header( 'Content-Length: ' . strlen( $csv ) );
	}
	echo $csv;
	exit;
}
add_action( 'rest_api_init', 'hainute_register_rest_routes' );

function hainute_rest_sync_permission( WP_REST_Request $request ) {
	$secret = hainute_config( 'HAINUTE_SYNC_SECRET' );

	if ( ! $secret ) {
		return new WP_Error(
			'hainute_no_secret',
			'HAINUTE_SYNC_SECRET nu e definit în wp-config.php — endpoint dezactivat.',
			array( 'status' => 503 )
		);
	}

	$provided = $request->get_param( 'secret' );
	if ( ! $provided ) {
		$provided = $request->get_header( 'X-Hainute-Sync-Secret' );
	}

	if ( $provided && hash_equals( (string) $secret, (string) $provided ) ) {
		return true;
	}

	return new WP_Error( 'hainute_bad_secret', 'Secret invalid.', array( 'status' => 403 ) );
}

function hainute_rest_sync( WP_REST_Request $request ) {
	$started = microtime( true );
	$only    = sanitize_key( (string) $request->get_param( 'only' ) );

	// Reset cursor Profitshare (Fashion Days) → reia sweep-ul de la pagina 1,
	// ca să re-adune mărimile/culorile din URL-ul fiecărui rând. Folosit pentru
	// un re-import complet de îmbogățire.
	if ( $request->get_param( 'ps_reset' ) ) {
		delete_option( 'hainute_ps_cursor' );
	}

	$results = hainute_run_sync( $only );

	return rest_ensure_response(
		array(
			'ok'       => true,
			'duration' => round( microtime( true ) - $started, 1 ) . 's',
			'results'  => $results,
		)
	);
}
