<?php
/**
 * 2Performant source.
 *
 * Auth: POST /users/sign_in with { user: { email, password } } → the response
 * headers carry access-token / client / uid. The access-token ROTATES: every
 * response returns a fresh one that must be used on the next request, so all
 * calls are sequential and share the $auth array by reference.
 *
 * Products: GET /affiliate/product_feeds.json → list of feeds the affiliate
 * can use; GET /affiliate/product_feeds/{code}/products.json?page=N → items.
 * These endpoints are not in the public docs, so the field mapping is
 * defensive — use the "Test 2Performant" admin button to inspect the real
 * payload shape and refine.
 *
 * Optional wp-config.php constants:
 *   HAINUTE_2P_FEEDS      — comma-separated feed codes to import (default: all)
 *   HAINUTE_2P_CATEGORIES — comma-separated category name fragments to keep
 *                           (default: everything)
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_2p_api_base() {
	return 'https://api.2performant.com/';
}

/**
 * Sign in. Returns auth array (headers + affiliate unique code) or WP_Error.
 */
function hainute_2p_sign_in() {
	$response = wp_remote_post(
		hainute_2p_api_base() . 'users/sign_in.json',
		array(
			'timeout' => 30,
			'headers' => array( 'Content-Type' => 'application/json' ),
			'body'    => wp_json_encode(
				array(
					'user' => array(
						'email'    => hainute_config( 'HAINUTE_2P_EMAIL' ),
						'password' => hainute_config( 'HAINUTE_2P_PASSWORD' ),
					),
				)
			),
		)
	);

	if ( is_wp_error( $response ) ) {
		return $response;
	}

	$code = wp_remote_retrieve_response_code( $response );
	if ( 200 !== $code ) {
		return new WP_Error(
			'hainute_2p_auth',
			sprintf( 'Autentificare 2Performant eșuată (HTTP %d): %s', $code, substr( wp_remote_retrieve_body( $response ), 0, 200 ) )
		);
	}

	$body = json_decode( wp_remote_retrieve_body( $response ), true );

	return array(
		'access-token' => wp_remote_retrieve_header( $response, 'access-token' ),
		'client'       => wp_remote_retrieve_header( $response, 'client' ),
		'uid'          => wp_remote_retrieve_header( $response, 'uid' ),
		'unique_code'  => $body['user']['unique_code'] ?? '',
	);
}

/**
 * Authenticated GET. Rotates the access token from each response.
 *
 * @param string $path  Path relative to the API base, e.g. 'affiliate/product_feeds.json'.
 * @param array  $query Query args.
 * @param array  $auth  By-ref auth array from hainute_2p_sign_in().
 * @return array|WP_Error Decoded JSON.
 */
function hainute_2p_get( $path, array $query, array &$auth ) {
	$response = wp_remote_get(
		add_query_arg( $query, hainute_2p_api_base() . $path ),
		array(
			'timeout' => 60,
			'headers' => array(
				'access-token' => $auth['access-token'],
				'client'       => $auth['client'],
				'uid'          => $auth['uid'],
				'token-type'   => 'Bearer',
			),
		)
	);

	if ( is_wp_error( $response ) ) {
		return $response;
	}

	$fresh_token = wp_remote_retrieve_header( $response, 'access-token' );
	if ( $fresh_token ) {
		$auth['access-token'] = $fresh_token;
	}

	$code = wp_remote_retrieve_response_code( $response );
	if ( 200 !== $code ) {
		return new WP_Error(
			'hainute_2p_http',
			sprintf( '%s → HTTP %d: %s', $path, $code, substr( wp_remote_retrieve_body( $response ), 0, 200 ) )
		);
	}

	$decoded = json_decode( wp_remote_retrieve_body( $response ), true );
	if ( ! is_array( $decoded ) ) {
		return new WP_Error( 'hainute_2p_json', $path . ' → răspuns non-JSON' );
	}

	return $decoded;
}

/**
 * List the affiliate's product feeds (normalized to a flat array).
 *
 * @return array|WP_Error Each: { code, name, program_name, program_id, program_unique }
 */
function hainute_2p_list_feeds( array &$auth ) {
	$data = hainute_2p_get( 'affiliate/product_feeds.json', array( 'page' => 1, 'perpage' => 100 ), $auth );
	if ( is_wp_error( $data ) ) {
		return $data;
	}

	$raw   = $data['product_feeds'] ?? $data['feeds'] ?? array();
	$feeds = array();

	foreach ( $raw as $feed ) {
		$program = $feed['program'] ?? $feed['campaign'] ?? array();

		$feeds[] = array(
			'code'           => $feed['unique_code'] ?? $feed['code'] ?? $feed['id'] ?? '',
			'name'           => $feed['name'] ?? '',
			'program_name'   => trim( (string) ( $program['name'] ?? $feed['campaign_name'] ?? $feed['name'] ?? 'Magazin' ) ),
			'program_id'     => (string) ( $program['id'] ?? $feed['campaign_id'] ?? $feed['program_id'] ?? '' ),
			'program_unique' => $program['unique_code'] ?? $feed['campaign_unique'] ?? '',
			'products_count' => (int) ( $feed['products_count'] ?? 0 ),
		);
	}

	return $feeds;
}

/**
 * Build the 2Performant affiliate quicklink for a merchant URL.
 * Documented format:
 *   https://event.2performant.com/events/click?ad_type=quicklink
 *     &aff_code={affiliate unique}&unique={advertiser unique}&redirect_to={url}
 * `unique` must belong to the same advertiser as redirect_to.
 */
function hainute_2p_quicklink( $merchant_url, $program_unique, $affiliate_unique ) {
	if ( ! $program_unique || ! $affiliate_unique ) {
		return ''; // no valid tracking link — caller decides what to do
	}

	// Build manually so redirect_to keeps its own encoded query string intact.
	return 'https://event.2performant.com/events/click?ad_type=quicklink'
		. '&aff_code=' . rawurlencode( $affiliate_unique )
		. '&unique=' . rawurlencode( $program_unique )
		. '&redirect_to=' . rawurlencode( $merchant_url );
}

/**
 * Resolve an advertiser's unique_code (needed for the quicklink `unique`
 * param). Cached per run. Tries the program endpoint defensively.
 *
 * @param string $program_id Advertiser/program id, e.g. '907'.
 * @param array  $auth       By-ref auth array.
 * @param array  $cache      By-ref cache: program_id => unique_code.
 * @return string Advertiser unique code, or '' if unresolved.
 */
function hainute_2p_program_unique( $program_id, array &$auth, array &$cache ) {
	if ( '' === (string) $program_id ) {
		return '';
	}
	if ( isset( $cache[ $program_id ] ) ) {
		return $cache[ $program_id ];
	}

	$unique = '';
	$data   = hainute_2p_get( 'affiliate/programs/' . rawurlencode( $program_id ) . '.json', array(), $auth );

	if ( ! is_wp_error( $data ) ) {
		$program = $data['program'] ?? $data['advertiser_program'] ?? $data;
		$unique  = (string) ( $program['unique_code'] ?? $program['unique'] ?? '' );
	}

	$cache[ $program_id ] = $unique;
	return $unique;
}

/**
 * Parse a hierarchical category path ("Copii/Fete/Încălțăminte/Pantofi sport")
 * into { category, gender, age }. Gender/age are inferred from the segments;
 * category is the most specific (leaf) segment.
 */
function hainute_2p_parse_taxonomy( $path ) {
	$segments = array_values( array_filter( array_map( 'trim', explode( '/', (string) $path ) ) ) );
	if ( empty( $segments ) ) {
		return array( 'category' => '', 'gender' => '', 'age' => '' );
	}

	$gender = '';
	$age    = '';

	foreach ( $segments as $seg ) {
		$norm = strtolower( remove_accents( $seg ) );

		if ( '' === $gender ) {
			if ( 0 === strpos( $norm, 'fete' ) || 0 === strpos( $norm, 'fetit' ) ) {
				$gender = 'Fete';
			} elseif ( 0 === strpos( $norm, 'baiet' ) || 'baieti' === $norm ) {
				$gender = 'Băieți';
			} elseif ( 'unisex' === $norm ) {
				$gender = 'Unisex';
			}
		}

		if ( '' === $age && ( false !== strpos( $norm, 'bebel' ) || false !== strpos( $norm, 'bebe' ) || false !== strpos( $norm, 'nou-nascut' ) || false !== strpos( $norm, 'nou nascut' ) ) ) {
			$age = '0-2 ani';
		}
	}

	// Category: the leaf segment, unless it's just a gender/age marker — then
	// fall back to the previous meaningful segment.
	$skip = array( 'fete', 'baieti', 'baietei', 'unisex', 'copii', 'bebelusi', 'bebe' );
	$category = '';
	for ( $i = count( $segments ) - 1; $i >= 0; $i-- ) {
		$norm = strtolower( remove_accents( $segments[ $i ] ) );
		if ( ! in_array( $norm, $skip, true ) ) {
			$category = $segments[ $i ];
			break;
		}
	}
	if ( '' === $category ) {
		$category = end( $segments );
	}

	return array( 'category' => $category, 'gender' => $gender, 'age' => $age );
}

/**
 * Interpret the many availability spellings feeds use.
 */
function hainute_2p_in_stock( $product ) {
	foreach ( array( 'availability', 'in_stock', 'stock', 'product_active', 'active', 'status' ) as $key ) {
		if ( ! isset( $product[ $key ] ) ) {
			continue;
		}
		$value = $product[ $key ];

		if ( is_bool( $value ) ) {
			return $value;
		}

		$value = strtolower( trim( (string) $value ) );
		if ( in_array( $value, array( 'in stock', 'instock', 'in_stock', 'available', 'da', 'yes', 'true', '1', 'active' ), true ) ) {
			return true;
		}
		if ( in_array( $value, array( 'out of stock', 'outofstock', 'out_of_stock', 'unavailable', 'indisponibil', 'nu', 'no', 'false', '0', 'inactive' ), true ) ) {
			return false;
		}
	}

	return true; // feeds that omit availability list only sellable products
}

/**
 * Map one raw 2Performant product to the normalized importer item.
 */
function hainute_2p_map_product( array $p, array $feed, array $auth ) {
	// Price: some feeds put the discounted price in sale_price.
	$price     = (float) str_replace( ',', '.', (string) ( $p['price'] ?? 0 ) );
	$old_price = null;

	$sale = isset( $p['sale_price'] ) ? (float) str_replace( ',', '.', (string) $p['sale_price'] ) : 0;
	if ( $sale > 0 && $sale < $price ) {
		$old_price = $price;
		$price     = $sale;
	}

	// Images: 2Performant uses structured_image_urls (array). Keep older
	// field names as fallbacks; accept comma/pipe separated strings too.
	$images = $p['structured_image_urls'] ?? $p['image_urls'] ?? $p['image_url'] ?? $p['image'] ?? array();
	if ( is_string( $images ) ) {
		$images = preg_split( '/[,|]\s*/', $images );
	}
	$images = array_values( array_filter( array_map( 'trim', (array) $images ) ) );

	// Affiliate link: wrap the merchant URL in a 2Performant tracking quicklink.
	// The feed `url` carries only UTM tags, not tracking — without wrapping we
	// earn no commission, so a product without a valid quicklink is skipped
	// upstream (empty url).
	$merchant_url = $p['url'] ?? $p['product_url'] ?? '';
	$aff_link     = hainute_2p_quicklink( $merchant_url, $feed['program_unique'], $auth['unique_code'] );

	// external_id: merchant SKU (prid) scoped to the store, so the same product
	// coming from several of that store's feeds maps to one offer.
	$external = trim( (string) ( $p['prid'] ?? '' ) );
	if ( '' === $external ) {
		$external = (string) ( $p['id'] ?? '' );
	}

	$tax                = hainute_2p_parse_taxonomy( $p['category'] ?? '' );
	$tax['category']    = hainute_canonical_category( $p['category'] ?? '', $p['title'] ?? '', $p['brand'] ?? $p['vendor'] ?? '' );

	return array(
		'network'     => '2performant',
		'program_id'  => $feed['program_id'] ?: $feed['code'],
		'store_name'  => $feed['program_name'],
		'external_id' => ( $feed['program_id'] ?: $feed['code'] ) . ':' . $external,
		'name'        => trim( (string) ( $p['title'] ?? $p['name'] ?? '' ) ),
		'description' => (string) ( $p['description'] ?? '' ),
		'brand'       => trim( (string) ( $p['brand'] ?? $p['vendor'] ?? '' ) ),
		'category'    => $tax['category'],
		'gender'      => $tax['gender'],
		'age'         => $tax['age'],
		'price'       => $price,
		'old_price'   => $old_price,
		'currency'    => strtoupper( (string) ( $p['currency'] ?? 'RON' ) ),
		'in_stock'    => hainute_2p_in_stock( $p ),
		'stock_qty'   => null,
		'url'         => $aff_link,
		'images'      => $images,
		'material'    => '',
		'sizes'       => '',
		'color'       => hainute_extract_color( $p['title'] ?? '' ), // variantă de culoare
	);
}

/**
 * Should this feed / category be imported, per the optional config filters?
 */
function hainute_2p_feed_allowed( array $feed ) {
	$allowed = hainute_config( 'HAINUTE_2P_FEEDS' );
	if ( ! $allowed ) {
		return true;
	}

	$codes = array_map( 'trim', explode( ',', $allowed ) );
	return in_array( (string) $feed['code'], $codes, true );
}

/**
 * Category filter, matched against the RAW category path (e.g.
 * "Copii/Fete/Încălțăminte"). Diacritic-insensitive so "copii" matches
 * "Copii" and "baieti" matches "Băieți". Optionally per-feed via
 * HAINUTE_2P_CATEGORIES_{feedcode}, else the global HAINUTE_2P_CATEGORIES.
 */
function hainute_2p_category_allowed( $category_path, $feed_code = '' ) {
	$filter = $feed_code ? hainute_config( 'HAINUTE_2P_CATEGORIES_' . $feed_code ) : '';
	if ( ! $filter ) {
		$filter = hainute_config( 'HAINUTE_2P_CATEGORIES' );
	}
	if ( ! $filter ) {
		return true;
	}

	$haystack = strtolower( remove_accents( (string) $category_path ) );

	foreach ( array_map( 'trim', explode( ',', $filter ) ) as $fragment ) {
		$needle = strtolower( remove_accents( $fragment ) );
		if ( '' !== $needle && false !== strpos( $haystack, $needle ) ) {
			return true;
		}
	}

	return false;
}

/**
 * Source entry point: fetch everything as normalized items.
 *
 * @return array { items: array[], notes: string[] }
 */
function hainute_2p_fetch_items() {
	$items = array();
	$notes = array();

	$auth = hainute_2p_sign_in();
	if ( is_wp_error( $auth ) ) {
		return array( 'items' => $items, 'notes' => array( $auth->get_error_message() ) );
	}

	$feeds = hainute_2p_list_feeds( $auth );
	if ( is_wp_error( $feeds ) ) {
		return array( 'items' => $items, 'notes' => array( $feeds->get_error_message() ) );
	}

	if ( empty( $feeds ) ) {
		$notes[] = 'Niciun product feed disponibil pe contul 2Performant (programul partener are feed activ?).';
	}

	$per_page      = 40; // 2Performant hard cap: max 40 products per page.
	$max_pages     = (int) apply_filters( 'hainute_2p_max_pages_per_feed', 250 );
	$program_cache = array();

	// Process feeds in the order given by HAINUTE_2P_FEEDS, so the cleanest
	// (kids-only) feeds fill the per-run product budget before mixed "all
	// products" feeds do.
	$order = hainute_config( 'HAINUTE_2P_FEEDS' );
	if ( $order ) {
		$order = array_map( 'trim', explode( ',', $order ) );
		usort(
			$feeds,
			function ( $a, $b ) use ( $order ) {
				$ia = array_search( (string) $a['code'], $order, true );
				$ib = array_search( (string) $b['code'], $order, true );
				$ia = ( false === $ia ) ? PHP_INT_MAX : $ia;
				$ib = ( false === $ib ) ? PHP_INT_MAX : $ib;
				return $ia <=> $ib;
			}
		);
	}

	foreach ( $feeds as $feed ) {
		if ( ! hainute_2p_feed_allowed( $feed ) ) {
			$notes[] = sprintf( 'Feed sărit (nu e în HAINUTE_2P_FEEDS): %s', $feed['name'] ?: $feed['code'] );
			continue;
		}

		// Resolve the advertiser unique code once per feed (for tracking links).
		if ( empty( $feed['program_unique'] ) ) {
			$feed['program_unique'] = hainute_2p_program_unique( $feed['program_id'], $auth, $program_cache );
		}
		if ( empty( $feed['program_unique'] ) ) {
			$notes[] = sprintf(
				'ATENȚIE: nu am putut obține codul de advertiser pentru "%s" — produsele fără link de tracking se sar (nu s-ar câștiga comision).',
				$feed['program_name'] ?: $feed['code']
			);
		}

		$feed_items = 0;
		$skipped    = 0;

		for ( $page = 1; $page <= $max_pages; $page++ ) {
			$data = hainute_2p_get(
				'affiliate/product_feeds/' . rawurlencode( $feed['code'] ) . '/products.json',
				array( 'page' => $page, 'perpage' => $per_page ),
				$auth
			);

			if ( is_wp_error( $data ) ) {
				$notes[] = $data->get_error_message();
				break;
			}

			$products = $data['products'] ?? array();
			if ( empty( $products ) ) {
				break;
			}

			foreach ( $products as $product ) {
				$product = (array) $product;

				// Category filter on the raw path (kids-only for mixed feeds).
				if ( ! hainute_2p_category_allowed( $product['category'] ?? '', $feed['code'] ) ) {
					$skipped++;
					continue;
				}

				$item = hainute_2p_map_product( $product, $feed, $auth );

				if ( '' === $item['name'] || ! $item['url'] ) {
					$skipped++;
					continue;
				}

				$items[]     = $item;
				$feed_items++;
			}

			// Stop when the API says we're on the last page, or the page came back short.
			$pagination = $data['metadata']['pagination'] ?? array();
			$last_page  = (int) ( $pagination['pages'] ?? $pagination['last_page'] ?? 0 );
			if ( ( $last_page && $page >= $last_page ) || count( $products ) < $per_page ) {
				break;
			}
		}

		$notes[] = sprintf(
			'%s: %d produse preluate%s',
			$feed['program_name'] ?: $feed['code'],
			$feed_items,
			$skipped ? sprintf( ' (%d sărite de filtre/câmpuri lipsă)', $skipped ) : ''
		);
	}

	return array( 'items' => $items, 'notes' => $notes );
}

/**
 * Diagnostic used by the admin "Test 2Performant" button: signs in, lists
 * feeds and dumps the first product's raw structure into the sync log so we
 * can verify/refine the field mapping against reality.
 */
function hainute_2p_run_diagnostic() {
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}

	$notes = array();

	try {

	$auth = hainute_2p_sign_in();
	if ( is_wp_error( $auth ) ) {
		return array( 'ok' => false, 'notes' => array( $auth->get_error_message() ) );
	}

	$notes[] = 'Autentificare OK (uid: ' . $auth['uid'] . ', cod afiliat: ' . $auth['unique_code'] . ')';

	$feeds = hainute_2p_list_feeds( $auth );
	if ( is_wp_error( $feeds ) ) {
		$notes[] = $feeds->get_error_message();
		return array( 'ok' => false, 'notes' => $notes );
	}

	$notes[] = 'Feed-uri disponibile: ' . count( $feeds );
	foreach ( $feeds as $feed ) {
		$notes[] = sprintf(
			'Feed "%s" (cod: %s, program: %s #%s, produse: %d)',
			$feed['name'],
			$feed['code'],
			$feed['program_name'],
			$feed['program_id'],
			$feed['products_count']
		);
	}

	if ( ! empty( $feeds ) ) {
		// Prefer a "kids" feed for the sample, else the first one.
		$sample_feed = $feeds[0];
		foreach ( $feeds as $f ) {
			if ( false !== stripos( $f['name'], 'copii' ) ) {
				$sample_feed = $f;
				break;
			}
		}

		// Resolve the advertiser unique code (needed for tracking links).
		$cache = array();
		if ( empty( $sample_feed['program_unique'] ) ) {
			$sample_feed['program_unique'] = hainute_2p_program_unique( $sample_feed['program_id'], $auth, $cache );
		}
		$notes[] = sprintf(
			'Cod advertiser pentru "%s": %s',
			$sample_feed['program_name'],
			$sample_feed['program_unique'] ?: 'NEGĂSIT (linkurile de tracking nu se pot construi!)'
		);

		$data = hainute_2p_get(
			'affiliate/product_feeds/' . rawurlencode( $sample_feed['code'] ) . '/products.json',
			array( 'page' => 1, 'perpage' => 1 ),
			$auth
		);

		if ( is_wp_error( $data ) ) {
			$notes[] = $data->get_error_message();
		} elseif ( ! empty( $data['products'][0] ) ) {
			$sample = (array) $data['products'][0];
			$notes[] = 'Câmpuri produs: ' . implode( ', ', array_keys( $sample ) );
			$notes[] = 'Exemplu produs (trunchiat): ' . substr( wp_json_encode( $sample, JSON_UNESCAPED_UNICODE ), 0, 700 );

			$mapped  = hainute_2p_map_product( $sample, $sample_feed, $auth );
			$notes[] = 'După mapare: ' . substr( wp_json_encode( $mapped, JSON_UNESCAPED_UNICODE ), 0, 700 );
			$notes[] = 'LINK AFILIAT DE TESTAT (dă click să verifici că duce la produs): ' . ( $mapped['url'] ?: 'GOL — link invalid' );
		} else {
			$notes[] = 'Feed-ul de test nu a întors produse. Răspuns: ' . substr( wp_json_encode( $data ), 0, 300 );
		}
	}

	return array( 'ok' => true, 'notes' => $notes );

	} catch ( \Throwable $e ) {
		$notes[] = 'EXCEPȚIE: ' . $e->getMessage() . ' @ ' . basename( $e->getFile() ) . ':' . $e->getLine();
		return array( 'ok' => false, 'notes' => $notes );
	}
}
