<?php
/**
 * CJ Affiliate (Commission Junction) source.
 *
 * GraphQL: POST https://ads.api.cj.com/query, header Authorization: Bearer <PAT>.
 * `shoppingProducts(companyId, keywords, limit, offset)` întoarce produse DOAR
 * de la advertiserii la care contul (publisher-ul cu acel companyId) e înscris —
 * pentru noi Answear.ro și ceilalți advertiseri „joined". Fiecare advertiser
 * devine un „magazin", deci se aliniază natural cu logica cross-store.
 *
 * Activă când în wp-config.php sunt definite:
 *   HAINUTE_CJ_TOKEN        — Personal Access Token (Bearer)
 *   HAINUTE_CJ_COMPANY_ID   — companyId al publisher-ului
 * Opționale:
 *   HAINUTE_CJ_KEYWORD      — cuvânt de căutare (default: 'copii')
 *   HAINUTE_CJ_ADVERTISERS  — listă advertiserId permise (default: toți)
 *   HAINUTE_CJ_MAX          — plafon produse/rulare (default: 1000)
 *
 * NOTĂ tracking: folosim câmpul `link` întors de CJ ca link afiliat. La prima
 * rulare, click-testează un link și confirmă în CJ că vânzarea se atribuie
 * Website-ului tău (PID). Dacă CJ cere explicit un Website ID, îl adăugăm apoi.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_cj_endpoint() {
	return 'https://ads.api.cj.com/query';
}

/**
 * Execută o interogare GraphQL. Rotație de token nu există (PAT fix).
 *
 * @return array [ int $http_status, array|null $decoded, string $raw ]
 */
function hainute_cj_query( $token, $query ) {
	$response = wp_remote_post(
		hainute_cj_endpoint(),
		array(
			'timeout' => 60,
			'headers' => array(
				'Authorization' => 'Bearer ' . $token,
				'Content-Type'  => 'application/json',
			),
			'body'    => wp_json_encode( array( 'query' => $query ) ),
		)
	);

	if ( is_wp_error( $response ) ) {
		return array( 0, null, $response->get_error_message() );
	}

	$raw     = wp_remote_retrieve_body( $response );
	$status  = (int) wp_remote_retrieve_response_code( $response );
	$decoded = json_decode( $raw, true );

	return array( $status, is_array( $decoded ) ? $decoded : null, $raw );
}

/** Lista de advertiserId permiși (din HAINUTE_CJ_ADVERTISERS), sau []. */
function hainute_cj_advertiser_ids() {
	$allowed = hainute_config( 'HAINUTE_CJ_ADVERTISERS' );
	if ( ! $allowed ) {
		return array();
	}
	return array_values( array_filter( array_map( 'trim', explode( ',', $allowed ) ) ) );
}

/**
 * Construiește interogarea shoppingProducts. Când avem o listă de advertiseri,
 * o trimitem ca `partnerIds` (filtrare SERVER-side) — altfel fereastra de 10.000
 * de rezultate a CJ s-ar consuma pe advertiserii nedoriți, prinzând puține din
 * magazinul țintă.
 */
function hainute_cj_build_query( $company_id, $keyword, $limit, $offset, array $partner_ids = array() ) {
	$partners = '';
	if ( ! empty( $partner_ids ) ) {
		$quoted   = array_map( function ( $id ) { return '"' . addslashes( $id ) . '"'; }, $partner_ids );
		$partners = ', partnerIds: [' . implode( ', ', $quoted ) . ']';
	}

	return sprintf(
		'{ shoppingProducts(companyId: %s%s, keywords: ["%s"], limit: %d, offset: %d) {
			totalCount count
			resultList {
				advertiserId advertiserName title brand
				price { amount currency }
				salePrice { amount currency }
				link imageLink availability gtin
			}
		} }',
		(int) $company_id,
		$partners,
		addslashes( (string) $keyword ),
		(int) $limit,
		(int) $offset
	);
}

/**
 * E un produs de copii? (termeni univoci + excludere cosmetice), reutilizând
 * dicționarele de la sursa Profitshare pentru consistență.
 */
function hainute_cj_is_kids( $text ) {
	if ( ! function_exists( 'hainute_ps_text_match' ) ) {
		return true; // fără dicționar, nu filtrăm
	}
	if ( hainute_ps_text_match( hainute_ps_exclude_words(), $text ) ) {
		return false;
	}
	return hainute_ps_text_match( hainute_ps_kids_words(), $text );
}

/**
 * Advertiserul e permis, per HAINUTE_CJ_ADVERTISERS (listă de advertiserId)?
 */
function hainute_cj_advertiser_allowed( $advertiser_id ) {
	$allowed = hainute_config( 'HAINUTE_CJ_ADVERTISERS' );
	if ( ! $allowed ) {
		return true;
	}
	$ids = array_map( 'trim', explode( ',', $allowed ) );
	return in_array( (string) $advertiser_id, $ids, true );
}

/**
 * Interpretează câmpul `availability` al CJ, care variază între magazine:
 * „in stock", „in_stock", „InStock", „http://schema.org/InStock", „out of
 * stock", „OutOfStock" etc. Normalizăm la doar-litere și comparăm.
 */
function hainute_cj_in_stock( $availability ) {
	$a = strtolower( trim( (string) $availability ) );
	if ( '' === $a ) {
		return true; // fără info → magazinul listează doar produse vandabile
	}
	$norm = preg_replace( '/[^a-z]/', '', $a ); // „in_stock"/„in stock" → „instock"

	if ( false !== strpos( $norm, 'outofstock' ) || in_array( $norm, array( 'unavailable', 'soldout', 'notavailable', 'discontinued', 'preorder', 'backorder' ), true ) ) {
		return false;
	}
	if ( false !== strpos( $norm, 'instock' ) || 'available' === $norm ) {
		return true;
	}
	return true; // necunoscut → presupunem vandabil
}

/**
 * Împachetează URL-ul magazinului într-un deep-link de tracking CJ, ca să se
 * atribuie comisionul. Formatul „automatic deep link":
 *   https://www.anrdoezrs.net/links/{websiteId}/type/dlg/{URL destinație codat}
 * Fără Website ID (PID) în config, întoarcem '' → produsul se sare (nu importăm
 * linkuri care nu monetizează), la fel ca la 2Performant fără cod de tracking.
 */
function hainute_cj_affiliate_link( $destination ) {
	$destination = trim( (string) $destination );
	if ( '' === $destination ) {
		return '';
	}

	$pid  = trim( (string) hainute_config( 'HAINUTE_CJ_WEBSITE_ID' ) );
	$aids = json_decode( (string) hainute_config( 'HAINUTE_CJ_AIDS' ), true );
	$aid  = '';
	if ( is_array( $aids ) ) {
		foreach ( $aids as $needle => $a ) {
			if ( false !== stripos( $destination, (string) $needle ) ) { $aid = (string) $a; break; }
		}
	}
	if ( '' === $pid || '' === $aid ) {
		// Fără PID/AID: în modul test (HAINUTE_CJ_ALLOW_RAW) lăsăm URL-ul brut ca să
		// poți vedea produsele; altfel îl sărim (link nemonetizabil).
		return hainute_config( 'HAINUTE_CJ_ALLOW_RAW' ) ? $destination : '';
	}

	// Deep-link CJ care aduce comision: click-{PID}-{AID}?url={URL magazin}.
	return 'https://www.tkqlhce.com/click-' . rawurlencode( $pid ) . '-' . rawurlencode( $aid )
		. '?url=' . rawurlencode( $destination );
}

/**
 * Culoarea din slug-ul URL-ului magazinului. Answear pune culoarea în link
 * (nu în titlu): „.../adidas-geaca-copii-culoarea-negru-jl7402-1594090".
 * Extragem porțiunea de după „culoarea-" și o trecem prin dicționarul de culori.
 */
function hainute_cj_color_from_url( $link ) {
	$path = strtolower( (string) ( parse_url( (string) $link, PHP_URL_PATH ) ?: $link ) );
	if ( ! function_exists( 'hainute_extract_color' ) ) {
		return '';
	}
	// Format 1: culoarea explicită („...culoarea-negru-jl7402-...").
	if ( preg_match( '/culoarea-(.+?)-\d{4,}/', $path, $m ) ) {
		$c = hainute_extract_color( str_replace( '-', ' ', $m[1] ) );
		if ( '' !== $c ) {
			return $c;
		}
	}
	// Format 2: culoarea ca adjectiv în slug („...pentru-copii-maro-kq6169-...").
	return hainute_extract_color( str_replace( '-', ' ', $path ) );
}

/**
 * Mapează un produs CJ la item-ul normalizat al importer-ului.
 */
function hainute_cj_map_product( array $p ) {
	$advertiser_id = (string) ( $p['advertiserId'] ?? '' );
	$title         = trim( (string) ( $p['title'] ?? '' ) );
	$gtin          = trim( (string) ( $p['gtin'] ?? '' ) );

	// Preț: salePrice când e mai mic decât price.
	$price     = (float) ( $p['price']['amount'] ?? 0 );
	$sale      = (float) ( $p['salePrice']['amount'] ?? 0 );
	$old_price = null;
	if ( $sale > 0 && $sale < $price ) {
		$old_price = $price;
		$price     = $sale;
	} elseif ( $sale > 0 && 0 === (int) $price ) {
		$price = $sale;
	}

	// external_id stabil per advertiser: gtin dacă există, altfel hash pe titlu.
	$sku      = '' !== $gtin ? $gtin : substr( md5( $advertiser_id . '|' . $title ), 0, 16 );
	$currency = (string) ( $p['price']['currency'] ?? $p['salePrice']['currency'] ?? 'RON' );

	$in_stock = hainute_cj_in_stock( $p['availability'] ?? '' );

	$image = (string) ( $p['imageLink'] ?? '' );

	return array(
		'network'     => 'cj',
		'program_id'  => $advertiser_id,
		'store_name'  => trim( (string) ( $p['advertiserName'] ?? 'Magazin CJ' ) ),
		'external_id' => $advertiser_id . ':' . $sku,
		'name'        => $title,
		'description' => '',
		'brand'       => trim( (string) ( $p['brand'] ?? '' ) ),
		'category'    => function_exists( 'hainute_canonical_category' ) ? hainute_canonical_category( '', $title, (string) ( $p['brand'] ?? '' ) ) : '',
		'gender'      => function_exists( 'hainute_ps_gender_from' ) ? hainute_ps_gender_from( $title ) : '',
		'age'         => '',
		'price'       => $price,
		'old_price'   => $old_price,
		'currency'    => strtoupper( $currency ?: 'RON' ),
		'in_stock'    => $in_stock,
		'stock_qty'   => null,
		'url'         => hainute_cj_affiliate_link( $p['link'] ?? '' ),
		'images'      => $image ? array( $image ) : array(),
		'material'    => '',
		'sizes'       => '',
		'color'       => hainute_cj_color_from_url( $p['link'] ?? '' )
			?: ( function_exists( 'hainute_extract_color' ) ? hainute_extract_color( $title ) : '' ),
	);
}

/**
 * Punctul de intrare al sursei: preia tot ca item-uri normalizate.
 *
 * @return array { items: array[], notes: string[] }
 */
function hainute_cj_fetch_items() {
	$items = array();
	$notes = array();

	$token   = trim( (string) hainute_config( 'HAINUTE_CJ_TOKEN' ) );
	$company = trim( (string) hainute_config( 'HAINUTE_CJ_COMPANY_ID' ) );

	if ( '' === $token || '' === $company ) {
		return array( 'items' => $items, 'notes' => array( 'CJ: sărit (lipsesc HAINUTE_CJ_TOKEN / HAINUTE_CJ_COMPANY_ID).' ) );
	}

	$keyword = (string) hainute_config( 'HAINUTE_CJ_KEYWORD', 'copii' );
	$max     = (int) hainute_config( 'HAINUTE_CJ_MAX', 1000 );
	if ( $max <= 0 ) {
		$max = 1000;
	}

	$partner_ids = hainute_cj_advertiser_ids();

	$fetched = 0;
	$offset  = 0;
	$skipped = 0;

	while ( $fetched < $max ) {
		$batch = min( 100, $max - $fetched ); // CJ: max ~100/cerere
		if ( $offset + $batch > 10000 ) {
			$batch = 10000 - $offset; // CJ: offset+limit <= 10.000
		}
		if ( $batch < 1 ) {
			$notes[] = 'CJ: atins plafonul de 10.000 rezultate al API-ului.';
			break;
		}
		$query = hainute_cj_build_query( $company, $keyword, $batch, $offset, $partner_ids );

		list( $status, $data, $raw ) = hainute_cj_query( $token, $query );

		if ( 200 !== $status ) {
			$notes[] = "CJ: HTTP $status — " . substr( preg_replace( '/\s+/', ' ', (string) $raw ), 0, 200 );
			break;
		}
		if ( isset( $data['errors'] ) ) {
			$notes[] = 'CJ: eroare GraphQL — ' . substr( wp_json_encode( $data['errors'] ), 0, 250 );
			break;
		}

		$node = $data['data']['shoppingProducts'] ?? array();
		$list = $node['resultList'] ?? array();

		if ( 0 === $offset ) {
			$notes[] = sprintf( 'CJ: %d produse potrivite pe „%s" în total (advertiseri înscriși).', (int) ( $node['totalCount'] ?? 0 ), $keyword );
		}
		if ( empty( $list ) ) {
			break;
		}

		foreach ( $list as $p ) {
			$p = (array) $p;

			if ( ! hainute_cj_advertiser_allowed( $p['advertiserId'] ?? '' ) ) {
				$skipped++;
				continue;
			}

			$hay = ( $p['title'] ?? '' ) . ' ' . ( $p['advertiserName'] ?? '' ) . ' ' . ( $p['brand'] ?? '' );
			if ( ! hainute_cj_is_kids( $hay ) ) {
				$skipped++;
				continue;
			}

			$item = hainute_cj_map_product( $p );
			if ( '' === $item['name'] || '' === $item['url'] ) {
				$skipped++;
				continue;
			}

			$items[] = $item;
			$fetched++;
		}

		$offset += $batch;
		if ( count( $list ) < $batch ) {
			break; // ultima pagină
		}
	}

	$notes[] = sprintf( 'CJ: %d produse copii preluate%s.', $fetched, $skipped ? " ($skipped sărite de filtre)" : '' );

	return array( 'items' => $items, 'notes' => $notes );
}

/**
 * Diagnostic pentru un buton de test: rulează o singură pagină și raportează
 * câmpurile brute + maparea primului produs.
 */
function hainute_cj_run_diagnostic() {
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}

	$notes = array();
	$token   = trim( (string) hainute_config( 'HAINUTE_CJ_TOKEN' ) );
	$company = trim( (string) hainute_config( 'HAINUTE_CJ_COMPANY_ID' ) );

	if ( '' === $token || '' === $company ) {
		return array( 'ok' => false, 'notes' => array( 'CJ: lipsesc HAINUTE_CJ_TOKEN / HAINUTE_CJ_COMPANY_ID în wp-config.php.' ) );
	}

	$keyword = (string) hainute_config( 'HAINUTE_CJ_KEYWORD', 'copii' );
	list( $status, $data, $raw ) = hainute_cj_query( $token, hainute_cj_build_query( $company, $keyword, 100, 0 ) );

	if ( 200 !== $status ) {
		return array( 'ok' => false, 'notes' => array( "CJ: HTTP $status — " . substr( preg_replace( '/\s+/', ' ', (string) $raw ), 0, 300 ) ) );
	}
	if ( isset( $data['errors'] ) ) {
		return array( 'ok' => false, 'notes' => array( 'CJ: eroare GraphQL — ' . substr( wp_json_encode( $data['errors'] ), 0, 400 ) ) );
	}

	$node    = $data['data']['shoppingProducts'] ?? array();
	$list    = $node['resultList'] ?? array();
	$notes[] = 'CJ OK. Total produse pe „' . $keyword . '": ' . (int) ( $node['totalCount'] ?? 0 );

	// Advertiserii prezenți în primele 100 rezultate (ca să poți alege în
	// HAINUTE_CJ_ADVERTISERS). Marcăm cei care trec de filtrul de copii.
	$adv = array();
	foreach ( $list as $p ) {
		$id = (string) ( $p['advertiserId'] ?? '' );
		if ( '' === $id ) {
			continue;
		}
		if ( ! isset( $adv[ $id ] ) ) {
			$adv[ $id ] = array( 'name' => (string) ( $p['advertiserName'] ?? '' ), 'n' => 0 );
		}
		$adv[ $id ]['n']++;
	}
	arsort( $adv );
	$notes[] = 'Advertiseri în primele 100 rezultate (id → nume × count):';
	foreach ( $adv as $id => $info ) {
		$notes[] = sprintf( '  %s → %s × %d', $id, $info['name'], $info['n'] );
	}

	$sample = $list[0] ?? null;
	if ( $sample ) {
		$mapped  = hainute_cj_map_product( (array) $sample );
		$notes[] = 'Exemplu mapat: ' . substr( wp_json_encode( $mapped, JSON_UNESCAPED_UNICODE ), 0, 500 );
		$has_pid = '' !== trim( (string) hainute_config( 'HAINUTE_CJ_WEBSITE_ID' ) );
		$notes[] = $has_pid
			? 'LINK AFILIAT (deep-link CJ, click să verifici): ' . ( $mapped['url'] ?: 'GOL' )
			: 'ATENȚIE: HAINUTE_CJ_WEBSITE_ID (PID) nu e setat → linkurile CJ NU aduc comision. Setează-l în wp-config ca să monetizezi.';
	}

	return array( 'ok' => true, 'notes' => $notes );
}
