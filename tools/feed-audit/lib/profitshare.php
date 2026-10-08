<?php
/**
 * Conector Profitshare (rețeaua eMAG).
 * Auth: HMAC-SHA1. Semnătura =
 *   hash_hmac('sha1', METHOD + endpoint + '/?' + query + '/' + user + date, key)
 * cu query = urldecode(http_build_query(params)), date = gmdate('D, d M Y H:i:s T').
 * Headers: X-PS-Client, X-PS-Auth, X-PS-Accept: json, Date.
 * Limită: 60 apeluri / 60 secunde (respectată de fa_ps_throttle).
 */

define( 'FA_PS_BASE', 'https://api.profitshare.ro' );

$GLOBALS['fa_ps_calls'] = array();

/** Ține sub 60 apeluri/60s (marjă la 55). */
function fa_ps_throttle() {
	$now                    = microtime( true );
	$GLOBALS['fa_ps_calls'] = array_filter(
		$GLOBALS['fa_ps_calls'],
		function ( $t ) use ( $now ) {
			return $t > $now - 60;
		}
	);
	if ( count( $GLOBALS['fa_ps_calls'] ) >= 55 ) {
		$oldest = min( $GLOBALS['fa_ps_calls'] );
		$wait   = (int) ceil( 61 - ( $now - $oldest ) );
		if ( $wait > 0 ) {
			fa_log( "  Profitshare: pauză {$wait}s (limită de rată)..." );
			sleep( $wait );
		}
		$GLOBALS['fa_ps_calls'] = array();
	}
	$GLOBALS['fa_ps_calls'][] = microtime( true );
}

function fa_ps_get( $user, $key, $api, $params = array() ) {
	fa_ps_throttle();
	$qs   = $params ? urldecode( http_build_query( $params ) ) : '';
	$date = gmdate( 'D, d M Y H:i:s T', time() );
	$auth = hash_hmac( 'sha1', 'GET' . $api . '/?' . $qs . '/' . $user . $date, $key );

	list( $st, $h, $b ) = fa_http(
		'GET',
		FA_PS_BASE . '/' . $api . '/?' . $qs,
		array( "Date: {$date}", "X-PS-Client: {$user}", 'X-PS-Accept: json', "X-PS-Auth: {$auth}" ),
		null,
		40
	);
	return array( $st, json_decode( $b, true ) );
}

/**
 * Mapează un produs Profitshare la formatul normalizat al tool-ului.
 */
function fa_ps_map( array $p ) {
	$price = (float) ( $p['price_vat'] ?? $p['price'] ?? 0 );
	$disc  = ( '' !== ( $p['price_discounted'] ?? '' ) ) ? (float) $p['price_discounted'] : 0;
	if ( $disc > 0 && $disc < $price ) {
		$old   = $price;
		$price = $disc;
	} else {
		$old = '';
	}

	return array(
		'platforma'   => 'profitshare',
		'advertiser'  => (string) ( $p['advertiser_name'] ?? '' ),
		'external_id' => (string) ( $p['part_number'] ?? '' ),
		'titlu'       => (string) ( $p['name'] ?? '' ),
		'brand'       => (string) ( $p['brand_name'] ?? '' ),
		'categorie'   => (string) ( $p['category_name'] ?? '' ),
		'pret'        => $price,
		'pret_vechi'  => $old,
		'moneda'      => 'RON',
		'disponibil'  => 'da', // feed-ul Profitshare listează produse active
		'gtin'        => '',
		'url_afiliat' => 'https:' . ltrim( (string) ( $p['affiliate_link'] ?? '' ), ':' ),
		'imagine'     => (string) ( $p['image_original'] ?? $p['image'] ?? '' ),
	);
}

/**
 * @return array { inventory, products, notes }
 */
function fa_ps_run( array $cfg, array $global ) {
	$out  = array( 'inventory' => array(), 'products' => array(), 'notes' => array() );
	$user = $cfg['user'] ?? '';
	$key  = $cfg['key'] ?? '';
	if ( '' === $user || '' === $key ) {
		$out['notes'][] = 'Profitshare: sărit (lipsă user/key).';
		return $out;
	}

	// Inventar: toți advertiserii.
	list( $st, $d ) = fa_ps_get( $user, $key, 'affiliate-advertisers' );
	if ( 200 !== $st || ! isset( $d['result'] ) ) {
		$out['notes'][] = "Profitshare: nu pot lista advertiserii (HTTP $st)";
		return $out;
	}
	$advertisers = $d['result'];
	foreach ( $advertisers as $a ) {
		$out['inventory'][] = array(
			'platforma'     => 'profitshare',
			'advertiser'    => (string) ( $a['name'] ?? '' ),
			'feed'          => (string) ( $a['category'] ?? '' ),
			'feed_id'       => (string) ( $a['id'] ?? '' ),
			'produse_total' => '',
			'status'        => 'joined',
		);
	}
	$out['notes'][] = 'Profitshare: ' . count( $advertisers ) . ' advertiseri.';

	// Produse: doar de la advertiserii țintă (implicit Fashion Days 88736).
	$targets   = ! empty( $cfg['advertisers'] ) ? (array) $cfg['advertisers'] : array( 88736 );
	$max_pages = (int) ( $cfg['max_pages'] ?? 200 );
	$limit     = (int) ( $global['per_feed_limit'] ?? 0 );
	$keywords  = (array) ( $global['keywords'] ?? array() );

	foreach ( $targets as $adv_id ) {
		$adv_id = (int) $adv_id;
		$name   = $advertisers[ $adv_id ]['name'] ?? ( 'advertiser ' . $adv_id );
		$taken  = 0;
		$scanned = 0;

		for ( $page = 1; $page <= $max_pages; $page++ ) {
			list( $pst, $pd ) = fa_ps_get( $user, $key, 'affiliate-products', array( 'filters' => array( 'advertiser' => $adv_id ), 'page' => $page ) );

			// Limită de rată → așteaptă și reîncearcă aceeași pagină.
			if ( 429 === $pst || ( isset( $pd['error']['code'] ) && 'TOO_MANY_REQUESTS' === $pd['error']['code'] ) ) {
				$out['notes'][] = "Profitshare: limită de rată la pagina $page — aștept 60s...";
				sleep( 60 );
				$GLOBALS['fa_ps_calls'] = array();
				$page--;
				continue;
			}

			if ( 200 !== $pst || ! isset( $pd['result']['products'] ) ) {
				$out['notes'][] = "Profitshare: $name pagina $page — răspuns neașteptat, stop";
				break;
			}
			$products = $pd['result']['products'];
			if ( empty( $products ) ) {
				break;
			}
			$scanned += count( $products );

			foreach ( $products as $p ) {
				$haystack = ( $p['category_name'] ?? '' ) . ' ' . ( $p['name'] ?? '' );
				if ( ! fa_keyword_ok( $keywords, $haystack ) ) {
					continue;
				}
				if ( fa_excluded( (array) ( $global['exclude'] ?? array() ), $haystack ) ) {
					continue; // cosmetice/îngrijire care conțin totuși „copii"
				}
				$out['products'][] = fa_ps_map( (array) $p );
				$taken++;
				if ( $limit > 0 && $taken >= $limit ) {
					break 2;
				}
			}

			$total_pages = (int) ( $pd['result']['total_pages'] ?? 0 );
			if ( $total_pages && $page >= $total_pages ) {
				break;
			}
		}

		$out['notes'][] = "Profitshare: $name → $taken produse relevante (din $scanned scanate)";
	}

	return $out;
}
