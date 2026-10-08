<?php
/**
 * Conector CJ Affiliate (Commission Junction).
 * GraphQL: POST https://ads.api.cj.com/query, header Authorization: Bearer <PAT>.
 * `shoppingProducts` întoarce doar produse de la advertiserii la care ești
 * înscris. NETESTAT fără credențiale — verifică output-ul la prima rulare.
 */

define( 'FA_CJ_ENDPOINT', 'https://ads.api.cj.com/query' );

function fa_cj_query( $token, $query ) {
	list( $st, $h, $b ) = fa_http(
		'POST',
		FA_CJ_ENDPOINT,
		array( 'Authorization: Bearer ' . $token, 'Content-Type: application/json' ),
		json_encode( array( 'query' => $query ) )
	);
	return array( $st, json_decode( $b, true ), $b );
}

/**
 * @return array { inventory: array[], products: array[], notes: string[] }
 */
function fa_cj_run( array $cfg, array $global ) {
	$out = array( 'inventory' => array(), 'products' => array(), 'notes' => array() );

	$token = trim( (string) ( $cfg['token'] ?? '' ) );
	$cid   = trim( (string) ( $cfg['company_id'] ?? '' ) );
	if ( '' === $token || '' === $cid ) {
		$out['notes'][] = 'CJ: sărit (lipsesc token/company_id în config).';
		return $out;
	}

	$limit    = (int) ( $global['per_feed_limit'] ?? 0 );
	$page_max = $limit > 0 ? $limit : 1000;
	$keyword  = (string) ( $cfg['keyword'] ?? 'copii' );
	$keywords = (array) ( $global['keywords'] ?? array() );

	$fetched = 0;
	$offset  = 0;

	while ( $fetched < $page_max ) {
		$batch = min( 100, $page_max - $fetched ); // CJ: max ~100/cerere
		$query = sprintf(
			'{ shoppingProducts(companyId: %s, keywords: ["%s"], limit: %d, offset: %d) {
				totalCount count
				resultList {
					advertiserId advertiserName title brand
					price { amount currency }
					salePrice { amount currency }
					link imageLink availability gtin
				}
			} }',
			$cid,
			addslashes( $keyword ),
			$batch,
			$offset
		);

		list( $st, $data, $raw ) = fa_cj_query( $token, $query );

		if ( 200 !== $st ) {
			$out['notes'][] = "CJ: HTTP $st — " . substr( preg_replace( '/\s+/', ' ', $raw ), 0, 200 );
			break;
		}
		if ( isset( $data['errors'] ) ) {
			$out['notes'][] = 'CJ: eroare GraphQL — ' . substr( json_encode( $data['errors'], JSON_UNESCAPED_UNICODE ), 0, 250 );
			break;
		}

		$node = $data['data']['shoppingProducts'] ?? array();
		$list = $node['resultList'] ?? array();
		if ( empty( $list ) ) {
			break;
		}

		if ( 0 === $offset ) {
			$out['inventory'][] = array(
				'platforma'     => 'cj',
				'advertiser'    => 'toți advertiserii înscriși',
				'feed'          => 'shoppingProducts (keyword: ' . $keyword . ')',
				'feed_id'       => '',
				'produse_total' => (int) ( $node['totalCount'] ?? 0 ),
				'status'        => 'disponibil',
			);
		}

		foreach ( $list as $p ) {
			$cat = ''; // shoppingProducts nu întoarce mereu categorie
			if ( ! fa_keyword_ok( $keywords, ( $p['title'] ?? '' ) . ' ' . ( $p['advertiserName'] ?? '' ) ) ) {
				continue;
			}
			$out['products'][] = array(
				'platforma'   => 'cj',
				'advertiser'  => (string) ( $p['advertiserName'] ?? '' ),
				'external_id' => (string) ( $p['gtin'] ?? '' ),
				'titlu'       => (string) ( $p['title'] ?? '' ),
				'brand'       => (string) ( $p['brand'] ?? '' ),
				'categorie'   => $cat,
				'pret'        => (float) ( $p['salePrice']['amount'] ?? $p['price']['amount'] ?? 0 ),
				'pret_vechi'  => $p['price']['amount'] ?? '',
				'moneda'      => (string) ( $p['price']['currency'] ?? '' ),
				'disponibil'  => ( 'in stock' === strtolower( (string) ( $p['availability'] ?? '' ) ) ) ? 'da' : ( $p['availability'] ?? '' ),
				'gtin'        => (string) ( $p['gtin'] ?? '' ),
				'url_afiliat' => (string) ( $p['link'] ?? '' ),
				'imagine'     => (string) ( $p['imageLink'] ?? '' ),
			);
			$fetched++;
		}

		$offset += $batch;
		if ( count( $list ) < $batch ) {
			break;
		}
	}

	$out['notes'][] = "CJ: $fetched produse scoase";
	return $out;
}
