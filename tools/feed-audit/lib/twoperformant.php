<?php
/**
 * Conector 2Performant. Auth cu token rotativ (fiecare răspuns dă un token
 * nou). Întoarce: rânduri de inventar (feed-uri) + rânduri de produse.
 */

define( 'FA_2P_BASE', 'https://api.2performant.com/' );

function fa_2p_signin( $email, $password ) {
	$attempts = 0;
	do {
		list( $st, $h, $b ) = fa_http(
			'POST',
			FA_2P_BASE . 'users/sign_in.json',
			array( 'Content-Type: application/json' ),
			json_encode( array( 'user' => array( 'email' => $email, 'password' => $password ) ) )
		);
		if ( 429 === $st && $attempts < 6 ) {
			fa_log( '  2Performant: limită de rată la login — aștept 60s (penalizarea durează ~5 min)...' );
			sleep( 60 );
			$attempts++;
			continue;
		}
		break;
	} while ( true );

	if ( 200 !== $st ) {
		return array( 'error' => "Autentificare eșuată (HTTP $st): " . substr( $b, 0, 150 ) );
	}
	$body = json_decode( $b, true );
	return array(
		'access-token' => $h['access-token'] ?? '',
		'client'       => $h['client'] ?? '',
		'uid'          => $h['uid'] ?? '',
		'unique_code'  => $body['user']['unique_code'] ?? '',
	);
}

function fa_2p_get( $path, array &$auth ) {
	list( $st, $h, $b ) = fa_http(
		'GET',
		FA_2P_BASE . $path,
		array(
			'access-token: ' . $auth['access-token'],
			'client: ' . $auth['client'],
			'uid: ' . $auth['uid'],
			'token-type: Bearer',
		)
	);
	if ( ! empty( $h['access-token'] ) ) {
		$auth['access-token'] = $h['access-token'];
	}
	return array( $st, json_decode( $b, true ), $b );
}

/**
 * @return array { inventory: array[], products: array[], notes: string[] }
 */
function fa_2p_run( array $cfg, array $global ) {
	$out = array( 'inventory' => array(), 'products' => array(), 'notes' => array() );

	$auth = fa_2p_signin( $cfg['email'], $cfg['password'] );
	if ( isset( $auth['error'] ) ) {
		$out['notes'][] = '2Performant: ' . $auth['error'];
		return $out;
	}
	$out['notes'][] = '2Performant: autentificat (cod afiliat ' . $auth['unique_code'] . ')';

	list( $st, $data ) = fa_2p_get( 'affiliate/product_feeds.json?page=1&perpage=100', $auth );
	if ( 200 !== $st ) {
		$out['notes'][] = "2Performant: nu pot lista feed-urile (HTTP $st)";
		return $out;
	}
	$feeds = $data['product_feeds'] ?? $data['feeds'] ?? array();

	$only     = array_map( 'strval', (array) ( $cfg['feeds'] ?? array() ) );
	$limit    = (int) ( $global['per_feed_limit'] ?? 0 );
	$keywords = (array) ( $global['keywords'] ?? array() );

	foreach ( $feeds as $feed ) {
		$code    = (string) ( $feed['id'] ?? '' );
		$program = $feed['program'] ?? array();
		$adv     = trim( (string) ( $program['name'] ?? $feed['name'] ?? '' ) );
		$adv_uni = $program['unique_code'] ?? '';

		$out['inventory'][] = array(
			'platforma'      => '2performant',
			'advertiser'     => $adv,
			'feed'           => (string) ( $feed['name'] ?? '' ),
			'feed_id'        => $code,
			'produse_total'  => (int) ( $feed['products_count'] ?? 0 ),
			'status'         => 'disponibil',
		);

		if ( ! empty( $only ) && ! in_array( $code, $only, true ) ) {
			continue;
		}

		$max_pages = (int) ( $global['max_pages_per_feed'] ?? 25 );
		$taken     = 0;
		$scanned   = 0;
		for ( $page = 1; $page <= $max_pages; $page++ ) {
			usleep( 300000 ); // ~3 cereri/sec, ca să nu lovim limita de rată
			list( $pst, $pdata ) = fa_2p_get( "affiliate/product_feeds/$code/products.json?page=$page&perpage=40", $auth );

			if ( 429 === $pst ) {
				$out['notes'][] = "2Performant: limită de rată (429) la $adv — aștept 60s...";
				sleep( 60 );
				$page--; // reîncearcă aceeași pagină
				continue;
			}
			if ( 200 !== $pst ) {
				$out['notes'][] = "2Performant: feed $code pagina $page HTTP $pst";
				break;
			}
			$products = $pdata['products'] ?? array();
			if ( empty( $products ) ) {
				break;
			}
			$scanned += count( $products );

			// Feed irelevant pentru cuvintele-cheie: dacă după 5 pagini n-am
			// găsit nimic, îl sar (evită scanarea a sute de pagini de adulți).
			if ( 0 === $taken && $page >= 5 && ! empty( $keywords ) ) {
				$out['notes'][] = "2Performant: $adv → sărit (0 potriviri în primele $scanned produse)";
				break;
			}

			foreach ( $products as $p ) {
				$cat = (string) ( $p['category'] ?? '' );
				if ( ! fa_keyword_ok( $keywords, ( $p['title'] ?? '' ) . ' ' . $cat ) ) {
					continue;
				}

				$price = (float) str_replace( ',', '.', (string) ( $p['price'] ?? 0 ) );
				$aff   = 'https://event.2performant.com/events/click?ad_type=quicklink'
					. '&aff_code=' . rawurlencode( $auth['unique_code'] )
					. '&unique=' . rawurlencode( (string) $adv_uni )
					. '&redirect_to=' . rawurlencode( (string) ( $p['url'] ?? '' ) );

				$out['products'][] = array(
					'platforma'   => '2performant',
					'advertiser'  => $adv,
					'external_id' => (string) ( $p['prid'] ?? $p['id'] ?? '' ),
					'titlu'       => (string) ( $p['title'] ?? '' ),
					'brand'       => (string) ( $p['brand'] ?? '' ),
					'categorie'   => $cat,
					'pret'        => $price,
					'pret_vechi'  => $p['old_price'] ?? '',
					'moneda'      => strtoupper( (string) ( $p['currency'] ?? 'RON' ) ),
					'disponibil'  => ! empty( $p['active'] ) ? 'da' : 'nu',
					'gtin'        => (string) ( $p['gtin'] ?? '' ),
					'url_afiliat' => $adv_uni ? $aff : (string) ( $p['url'] ?? '' ),
					'imagine'     => (string) ( $p['structured_image_urls'][0] ?? '' ),
				);

				$taken++;
				if ( $limit > 0 && $taken >= $limit ) {
					break 2;
				}
			}

			if ( count( $products ) < 40 ) {
				break;
			}
		}
		$out['notes'][] = "2Performant: $adv → $taken produse scoase";
	}

	return $out;
}
