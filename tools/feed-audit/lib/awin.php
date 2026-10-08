<?php
/**
 * Conector Awin.
 *
 * Awin nu are un API „live" de produse per-cerere ca 2P/CJ. Fluxul e:
 *  1. GET https://api.awin.com/publishers/{pubId}/programmes?relationshipStatus=joined
 *     → advertiserii la care ești înscris (inventar).
 *  2. Product data = feed-uri descărcabile (CSV/JSONL) generate din UI
 *     ("Create-a-Feed"). Lista de feed-uri disponibile se ia din UI sau din
 *     fișierul de feed-uri Awin; URL-ul de download îl pui în config ca să-l
 *     tragem și parsăm.
 *
 * NETESTAT fără credențiale.
 */

define( 'FA_AWIN_BASE', 'https://api.awin.com/' );

function fa_awin_get( $token, $path ) {
	list( $st, $h, $b ) = fa_http(
		'GET',
		FA_AWIN_BASE . $path,
		array( 'Authorization: Bearer ' . $token )
	);
	return array( $st, json_decode( $b, true ), $b );
}

/**
 * @return array { inventory: array[], products: array[], notes: string[] }
 */
function fa_awin_run( array $cfg, array $global ) {
	$out = array( 'inventory' => array(), 'products' => array(), 'notes' => array() );

	$token = trim( (string) ( $cfg['token'] ?? '' ) );
	$pub   = trim( (string) ( $cfg['publisher_id'] ?? '' ) );
	if ( '' === $token || '' === $pub ) {
		$out['notes'][] = 'Awin: sărit (lipsesc token/publisher_id în config).';
		return $out;
	}

	// 1. Advertiseri: doar cei relevanți (înscris / în așteptare). Parametrul
	// corect e `relationship` (nu relationshipStatus). Produsele se pot lua doar
	// de la advertiserii JOINED.
	$counts = array();
	foreach ( array( 'joined', 'pending', 'notjoined' ) as $rel ) {
		list( $st, $data ) = fa_awin_get( $token, "publishers/$pub/programmes?relationship=$rel" );
		if ( 200 !== $st ) {
			$out['notes'][] = "Awin: nu pot lista programele ($rel, HTTP $st)";
			continue;
		}
		$programmes    = is_array( $data ) ? $data : array();
		$counts[ $rel ] = count( $programmes );

		// Listăm în inventar doar joined + pending (notjoined = doar număr).
		if ( 'notjoined' !== $rel ) {
			foreach ( $programmes as $prog ) {
				$region = $prog['primaryRegion']['countryCode'] ?? '';
				$out['inventory'][] = array(
					'platforma'     => 'awin',
					'advertiser'    => (string) ( $prog['name'] ?? '' ) . ( $region ? " [$region]" : '' ),
					'feed'          => 'relationship: ' . $rel,
					'feed_id'       => (string) ( $prog['id'] ?? '' ),
					'produse_total' => '',
					'status'        => $rel,
				);
			}
		}
	}

	$out['notes'][] = sprintf(
		'Awin: %d înscris, %d în așteptare, %d disponibili de aplicat.',
		$counts['joined'] ?? 0,
		$counts['pending'] ?? 0,
		$counts['notjoined'] ?? 0
	);
	if ( empty( $counts['joined'] ) ) {
		$out['notes'][] = 'Awin: NU ești înscris la niciun advertiser încă → nu poți scoate produse/câștiga până nu ești aprobat.';
	}

	// 2. Produse dintr-un feed descărcabil, dacă ai pus URL-ul în config.
	if ( ! empty( $cfg['feed_url'] ) ) {
		$out['notes'][] = 'Awin: descarc feed-ul din feed_url...';
		list( $fst, $fh, $fbody ) = fa_http( 'GET', $cfg['feed_url'], array(), null, 180 );
		if ( 200 === $fst && $fbody ) {
			$keywords = (array) ( $global['keywords'] ?? array() );
			$limit    = (int) ( $global['per_feed_limit'] ?? 0 );
			$taken    = 0;
			$lines    = preg_split( '/\r\n|\n/', $fbody );
			$header   = str_getcsv( array_shift( $lines ) );
			$idx      = array_flip( $header );
			foreach ( $lines as $line ) {
				if ( '' === trim( $line ) ) {
					continue;
				}
				$c = str_getcsv( $line );
				$get = function ( $name ) use ( $c, $idx ) {
					return isset( $idx[ $name ] ) && isset( $c[ $idx[ $name ] ] ) ? $c[ $idx[ $name ] ] : '';
				};
				$title = $get( 'product_name' );
				$cat   = $get( 'merchant_category' );
				if ( ! fa_keyword_ok( $keywords, $title . ' ' . $cat ) ) {
					continue;
				}
				$out['products'][] = array(
					'platforma'   => 'awin',
					'advertiser'  => $get( 'merchant_name' ),
					'external_id' => $get( 'merchant_product_id' ),
					'titlu'       => $title,
					'brand'       => $get( 'brand_name' ),
					'categorie'   => $cat,
					'pret'        => $get( 'search_price' ),
					'pret_vechi'  => $get( 'rrp_price' ),
					'moneda'      => $get( 'currency' ),
					'disponibil'  => $get( 'in_stock' ),
					'gtin'        => $get( 'ean' ),
					'url_afiliat' => $get( 'aw_deep_link' ),
					'imagine'     => $get( 'aw_image_url' ),
				);
				$taken++;
				if ( $limit > 0 && $taken >= $limit ) {
					break;
				}
			}
			$out['notes'][] = "Awin: $taken produse scoase din feed.";
		} else {
			$out['notes'][] = "Awin: nu am putut descărca feed_url (HTTP $fst).";
		}
	}

	return $out;
}
