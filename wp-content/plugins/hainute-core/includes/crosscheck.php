<?php
/**
 * Cross-check pe alte magazine (URL-uri găsite cu Google Lens și validate manual).
 *
 * Fluxul: lista {produs, URL} → /cross-import (curăță URL-ul, sare magazinele pe
 * care produsul le are deja, salvează în _hainute_manual_offers) → crawler-ul
 * tools/crawler/manual.js încarcă fiecare URL cu Chrome real și trimite la
 * /manual-result prețul, stocul și mărimile disponibile/epuizate → ofertă în
 * comparator. Același crawler rulează din cron (pe live) ca datele să rămână proaspete.
 *
 * Magazinele care sunt parteneri de afiliere (Fashion Days, Answear, Sportisimo,
 * various-brands) primesc link afiliat, nu URL brut.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Host fără www, lowercase. */
function hainute_cross_host( $url ) {
	return preg_replace( '/^www\./', '', strtolower( (string) wp_parse_url( (string) $url, PHP_URL_HOST ) ) );
}

/**
 * „Familia" magazinului (answear.hu și answear.ro = answear): același retailer
 * în altă țară e același magazin, nu un cross.
 */
function hainute_cross_family( $host ) {
	$host  = preg_replace( '/^(en|fr|de|it|es)\./', '', (string) $host );
	$parts = explode( '.', $host );
	return count( $parts ) >= 2 ? $parts[ count( $parts ) - 2 ] : $host;
}

/**
 * Hosturile (magazinele) pe care produsul le are deja: oferte + variante.
 * Linkurile afiliate sunt despachetate (CJ ?url=, 2P redirect_to=, Profitshare redirect=).
 */
function hainute_cross_existing_hosts( $product_id ) {
	$urls = array();
	if ( function_exists( 'hainute_get_offers' ) ) {
		foreach ( hainute_get_offers( $product_id ) as $o ) {
			if ( 0 === strpos( (string) $o->network, 'manual' ) ) {
				continue; // ofertele cross nu blochează re-importul aceluiași URL
			}
			$urls[] = (string) $o->affiliate_url;
		}
	}
	$variants = get_post_meta( $product_id, '_hainute_variant_offers', true );
	if ( is_array( $variants ) ) {
		foreach ( $variants as $v ) {
			$urls[] = (string) ( $v['url'] ?? '' );
		}
	}
	$hosts = array();
	foreach ( $urls as $u ) {
		if ( preg_match( '#[?&](?:url|redirect|redirect_to)=([^&]+)#', $u, $m ) ) {
			$u = rawurldecode( $m[1] );
		}
		$h = hainute_cross_host( $u );
		if ( $h ) {
			$hosts[ $h ] = hainute_cross_family( $h );
		}
	}
	return $hosts;
}

/**
 * URL curat de produs: fără parametri de tracking/cupon/consimțământ și fără
 * fragment. Farfetch pe varianta românească (/ro/), nu pe țara găsită de Lens.
 */
function hainute_cross_normalize_url( $url ) {
	$url = trim( (string) $url );
	$p   = wp_parse_url( $url );
	if ( empty( $p['host'] ) ) {
		return '';
	}
	$host = strtolower( $p['host'] );
	$path = $p['path'] ?? '/';
	if ( false !== strpos( $host, 'farfetch.com' ) ) {
		$path = preg_replace( '#^/[a-z]{2}(?=/shopping/)#', '/ro', $path );
	}
	// Păstrăm doar parametrii care identifică produsul (nu e cazul la magazinele de azi).
	return 'https://' . $host . $path;
}

/**
 * Magazinul (termen `store`) pentru un URL cross. Magazinele cunoscute au nume
 * fixe (ca să nu apară „Fashiondays.ro" lângă „FashionDays.ro"); restul primesc
 * numele din domeniu. Meta-ul unui magazin EXISTENT nu se atinge (altfel un
 * partener de afiliere ar fi marcat greșit ca „manual").
 *
 * @return array{0:int,1:string,2:string} [store_id, nume, slug] sau [0,'',''] la eroare.
 */
function hainute_cross_store( $url ) {
	$host  = hainute_cross_host( $url );
	$known = array(
		'answear.ro'       => 'Answear.ro',
		'fashiondays.ro'   => 'FashionDays.ro',
		'sportisimo.ro'    => 'Sportisimo.ro',
		'various-brands.ro' => 'various-brands.ro',
		'giraffe-shoes.ro' => 'giraffe-shoes.ro',
		'modivo.ro'        => 'Modivo.ro',
		'epantofi.ro'      => 'epantofi.ro',
		'zalando.ro'       => 'Zalando.ro',
		'aboutyou.ro'      => 'About You',
		'farfetch.com'     => 'Farfetch.com',
		'sportano.ro'      => 'Sportano.ro',
		'sportvision.ro'   => 'SportVision.ro',
		'mytheresa.com'    => 'Mytheresa',
	);
	$slug = sanitize_key( hainute_cross_family( $host ) );
	$name = $known[ $host ] ?? ( ucfirst( $slug ) . strstr( $host, '.' ) );

	$term = get_term_by( 'name', $name, 'store' );
	if ( $term ) {
		return array( (int) $term->term_id, $term->name, $slug );
	}
	$id = hainute_upsert_store( $name, array( 'network' => 'manual', 'program_id' => $slug, 'website' => 'https://' . $host . '/' ) );
	return is_wp_error( $id ) ? array( 0, '', '' ) : array( (int) $id, $name, $slug );
}

/**
 * Link afiliat pentru magazinele partenere; altfel URL-ul brut.
 * - Fashion Days → Profitshare (același format ca linkurile din feed)
 * - Answear, Sportisimo → CJ click-{PID}-{AID}?url=
 * - various-brands → 2Performant quicklink
 */
function hainute_cross_affiliate_url( $url ) {
	$host = hainute_cross_host( $url );
	if ( 'fashiondays.ro' === $host ) {
		return 'https://app.profitshare.ro/lps/ofx/oDC/?redirect=' . rawurlencode( $url );
	}
	if ( in_array( $host, array( 'answear.ro', 'sportisimo.ro' ), true ) && function_exists( 'hainute_cj_affiliate_link' ) ) {
		$link = hainute_cj_affiliate_link( $url );
		return $link ? $link : $url;
	}
	if ( 'various-brands.ro' === $host ) {
		return 'https://event.2performant.com/events/click?ad_type=quicklink&aff_code=b229f3020&unique=8bc6d7111&redirect_to=' . rawurlencode( $url );
	}
	return $url;
}

/**
 * Importă lista de cross-uri validate.
 *   POST /cross-import?secret=XXX  body { items:[{id,url}], dry_run }
 * Sare: produse inexistente/nepublicate, magazinul pe care produsul îl are deja
 * (inclusiv aceeași rețea în altă țară), duplicatele. Adaugă (nu înlocuiește).
 */
function hainute_rest_cross_import( WP_REST_Request $request ) {
	$b     = $request->get_json_params();
	$items = isset( $b['items'] ) && is_array( $b['items'] ) ? $b['items'] : array();
	$dry   = ! empty( $b['dry_run'] );
	$stats = array( 'primite' => count( $items ), 'adaugate' => 0, 'acelasi_magazin' => 0, 'deja_existente' => 0, 'produs_invalid' => 0, 'url_invalid' => 0 );
	$by    = array();

	foreach ( $items as $it ) {
		$pid = (int) ( $it['id'] ?? 0 );
		$url = hainute_cross_normalize_url( $it['url'] ?? '' );
		if ( ! $pid || 'product' !== get_post_type( $pid ) || 'publish' !== get_post_status( $pid ) ) {
			$stats['produs_invalid']++;
			continue;
		}
		if ( '' === $url ) {
			$stats['url_invalid']++;
			continue;
		}
		$by[ $pid ][] = $url;
	}

	foreach ( $by as $pid => $urls ) {
		$existing = hainute_cross_existing_hosts( $pid );
		$families = array_flip( array_values( $existing ) );
		$current  = get_post_meta( $pid, '_hainute_manual_offers', true );
		$current  = is_array( $current ) ? $current : array();
		$changed  = false;
		foreach ( $urls as $url ) {
			$host = hainute_cross_host( $url );
			if ( isset( $existing[ $host ] ) || isset( $families[ hainute_cross_family( $host ) ] ) ) {
				$stats['acelasi_magazin']++;
				continue;
			}
			if ( in_array( $url, $current, true ) ) {
				$stats['deja_existente']++;
				continue;
			}
			$current[] = $url;
			$changed   = true;
			$stats['adaugate']++;
		}
		if ( $changed && ! $dry ) {
			update_post_meta( $pid, '_hainute_manual_offers', array_values( $current ) );
		}
	}
	$stats['produse'] = count( $by );
	$stats['dry_run'] = $dry;
	return rest_ensure_response( array( 'ok' => true ) + $stats );
}

/**
 * Poza variantei de la un magazin extern (altă culoare = altă poză). Doar URL-uri
 * http(s) de imagine; goale nu suprascriu o poză bună.
 */
function hainute_set_ext_image( $pid, $store_id, $image ) {
	$image = esc_url_raw( trim( (string) $image ) );
	if ( ! $store_id || ! preg_match( '#^https?://#', $image ) ) {
		return;
	}
	$map = get_post_meta( (int) $pid, '_hainute_ext_image', true );
	$map = is_array( $map ) ? $map : array();
	$map[ (int) $store_id ] = $image;
	update_post_meta( (int) $pid, '_hainute_ext_image', $map );
}

/**
 * Coada de backfill pentru poze: ofertele externe/cross (produse publicate) fără
 * poză salvată. Implicit doar cele cu altă culoare decât produsul nostru (acolo
 * se vede poza greșită); `all=1` → toate.
 *   GET /ext-image-queue?secret=XXX[&all=1][&ids=1,2]
 */
function hainute_rest_ext_image_queue( WP_REST_Request $request ) {
	global $wpdb;
	$all   = ! empty( $request->get_param( 'all' ) );
	$ids   = array_filter( array_map( 'intval', explode( ',', (string) $request->get_param( 'ids' ) ) ) );
	$table = hainute_offers_table_name();
	$where = $ids ? ' AND o.product_id IN (' . implode( ',', $ids ) . ')' : '';
	$rows  = $wpdb->get_results(
		"SELECT o.product_id, o.store_id, o.affiliate_url FROM {$table} o
		 JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status = 'publish'
		 WHERE (o.network LIKE 'external:%' OR o.network LIKE 'manual:%'){$where}"
	);
	$queue = array();
	foreach ( $rows as $r ) {
		$pid  = (int) $r->product_id;
		$sid  = (int) $r->store_id;
		$imgs = get_post_meta( $pid, '_hainute_ext_image', true );
		if ( is_array( $imgs ) && ! empty( $imgs[ $sid ] ) ) {
			continue;
		}
		if ( ! $all ) {
			$ext  = get_post_meta( $pid, '_hainute_ext_color', true );
			$ec   = is_array( $ext ) ? strtolower( (string) ( $ext[ $sid ] ?? '' ) ) : '';
			$mine = array_map( 'strtolower', array_filter( array_map( 'trim', explode( ',', (string) get_post_meta( $pid, '_hainute_colors', true ) ) ) ) );
			if ( '' === $ec || in_array( $ec, $mine, true ) ) {
				continue; // aceeași culoare ca produsul nostru → poza noastră e corectă
			}
		}
		$url = (string) $r->affiliate_url;
		if ( preg_match( '#[?&](?:url|redirect|redirect_to)=([^&]+)#', $url, $m ) ) {
			$url = rawurldecode( $m[1] );
		}
		$queue[] = array( 'product_id' => $pid, 'store_id' => $sid, 'url' => $url, 'host' => hainute_cross_host( $url ) );
	}
	return rest_ensure_response( array( 'ok' => true, 'total' => count( $queue ), 'queue' => $queue ) );
}

/**
 * Rezultatul backfill-ului de poze (+ culoarea citită de pe pagină, dacă există).
 *   POST /ext-image?secret=XXX  body { product_id, store_id, image, color }
 */
function hainute_rest_ext_image( WP_REST_Request $request ) {
	$b   = $request->get_json_params();
	$pid = (int) ( $b['product_id'] ?? 0 );
	$sid = (int) ( $b['store_id'] ?? 0 );
	if ( ! $pid || ! $sid ) {
		return rest_ensure_response( array( 'ok' => false, 'error' => 'lipsă product_id/store_id' ) );
	}
	hainute_set_ext_image( $pid, $sid, (string) ( $b['image'] ?? '' ) );
	if ( ! empty( $b['color'] ) ) {
		hainute_set_ext_color( $pid, $sid, (string) $b['color'] );
	}
	$map = get_post_meta( $pid, '_hainute_ext_image', true );
	return rest_ensure_response( array( 'ok' => true, 'image' => is_array( $map ) ? ( $map[ $sid ] ?? '' ) : '' ) );
}

/**
 * O ofertă de pe alt magazin (cross/external) e „expirată" dacă n-a mai fost
 * verificată de HAINUTE_EXT_MAX_AGE_DAYS zile (implicit 7) — de ex. magazinul ne
 * blochează sau cron-ul s-a oprit. Expirată = nu o mai afișăm (nici în schema
 * pentru Google): un „în stoc" vechi de săptămâni ar induce în eroare.
 * Ofertele din feed-urile de afiliere (cj/profitshare/2performant) nu intră aici.
 */
function hainute_offer_is_stale( $product_id, $offer ) {
	$net = (string) $offer->network;
	if ( 0 !== strpos( $net, 'manual' ) && 0 !== strpos( $net, 'external' ) ) {
		return false;
	}
	// Verificat automat ca ALT produs (EAN-urile paginii nu sunt ale noastre și
	// nici codul producătorului nu apare) → nu se afișează.
	if ( 'diferit' === hainute_cross_match( $product_id, (int) $offer->store_id ) ) {
		return true;
	}
	static $cache = array();
	if ( ! isset( $cache[ $product_id ] ) ) {
		$c                      = get_post_meta( $product_id, '_hainute_manual_checked', true );
		$cache[ $product_id ] = is_array( $c ) ? $c : array();
	}
	$url = (string) $offer->affiliate_url;
	if ( preg_match( '#[?&](?:url|redirect|redirect_to)=([^&]+)#', $url, $m ) ) {
		$url = rawurldecode( $m[1] );
	}
	$ts   = (int) ( $cache[ $product_id ][ md5( $url ) ] ?? 0 );
	$days = (float) hainute_config( 'HAINUTE_EXT_MAX_AGE_DAYS', 7 );
	return ! $ts || ( time() - $ts ) > $days * DAY_IN_SECONDS;
}

/**
 * Identificatorii produsului nostru, ca să verificăm că o ofertă cross e ACELAȘI
 * produs: EAN-urile (din feed-ul Answear/CJ) și codul producătorului în mai
 * multe scrieri („T3X9-35233", „T3X9.35233", „T3X9 35233", „T3X935233").
 * @return array{ean:string[],codes:string[],color_code:string}
 */
function hainute_cross_ids( $product_id ) {
	$eans = array();
	if ( function_exists( 'hainute_get_offers' ) ) {
		foreach ( hainute_get_offers( $product_id ) as $o ) {
			if ( 'cj' !== $o->network ) {
				continue;
			}
			$parts = explode( ':', (string) $o->external_id );
			$g     = function_exists( 'hainute_valid_gtin' ) ? hainute_valid_gtin( end( $parts ) ) : preg_replace( '/\D/', '', end( $parts ) );
			if ( $g ) {
				$eans[] = $g;
				$eans[] = ltrim( $g, '0' );
			}
		}
	}
	$specs = get_post_meta( $product_id, '_hainute_specs', true );
	$specs = is_array( $specs ) ? $specs : array();
	// Datele brute extrase de pe pagina Answear păstrează „ID producător" /
	// „Culoare producător" și când fișa tehnică afișată a fost rescrisă manual.
	$ex = json_decode( (string) get_post_meta( $product_id, '_hainute_extract', true ), true );
	if ( is_array( $ex ) && ! empty( $ex['specs'] ) && is_array( $ex['specs'] ) ) {
		$specs += $ex['specs'];
	}
	$raw   = array_filter( array( (string) get_post_meta( $product_id, '_hainute_model_code', true ), (string) ( $specs['Cod produs'] ?? '' ), (string) ( $specs['ID producător'] ?? '' ) ) );
	$codes = array();
	foreach ( $raw as $r ) {
		$seg = preg_split( '/[.\s_\/-]+/', strtoupper( trim( $r ) ) );
		$s1  = $seg[0] ?? '';
		$s2  = $seg[1] ?? '';
		// Primul segment e suficient dacă e distinctiv (≥6 caractere, cu cifre).
		if ( strlen( $s1 ) >= 6 && preg_match( '/\d/', $s1 ) ) {
			$codes[] = $s1;
		}
		if ( $s1 && $s2 && preg_match( '/\d/', $s1 . $s2 ) ) {
			foreach ( array( '-', '.', ' ', '' ) as $j ) {
				$codes[] = $s1 . $j . $s2;
			}
		}
	}
	$color_code = strtoupper( trim( (string) ( $specs['Culoare producător'] ?? '' ) ) );
	// Cel mai distinctiv cuvânt din brand („Calvin Klein Jeans" → CALVIN,
	// „Polo Ralph Lauren" → LAUREN), căutat în titlul/numele produsului de pe pagină.
	$brand = function_exists( 'hainute_get_brand' ) ? (string) hainute_get_brand( $product_id ) : '';
	$words = array_filter( preg_split( '/[\s&.\-]+/', strtoupper( remove_accents( $brand ) ) ), function ( $w ) { return strlen( $w ) >= 3 && ! in_array( $w, array( 'KIDS', 'JEANS', 'JUNIOR', 'SPORT', 'BABY' ), true ); } );
	usort( $words, function ( $a, $b ) { return strlen( $b ) <=> strlen( $a ); } );
	$brand_word = $words ? reset( $words ) : '';
	return array(
		'ean'        => array_values( array_unique( array_filter( $eans ) ) ),
		'codes'      => array_values( array_unique( array_filter( $codes, function ( $c ) { return strlen( $c ) >= 5; } ) ) ),
		'color_code' => strlen( $color_code ) >= 3 ? $color_code : '',
		'brand'      => $brand_word,
	);
}

/** Rezultatul verificării „același produs?" pentru oferta unui magazin. */
function hainute_cross_match( $product_id, $store_id ) {
	$m = get_post_meta( $product_id, '_hainute_cross_match', true );
	return is_array( $m ) ? (string) ( $m[ (int) $store_id ] ?? '' ) : '';
}
