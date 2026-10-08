<?php
/**
 * Sursă Profitshare (rețeaua eMAG) — bază: Fashion Days (id 88736).
 *
 * Feed-ul Profitshare e uriaș (Fashion Days ~107k produse, toate categoriile),
 * iar produsele de copii sunt răspândite. De aceea:
 *  - filtrăm client-side pe termeni UNIVOCI de copii (fără „fata" = și „față"),
 *    excluzând cosmeticele;
 *  - folosim un CURSOR persistent care avansează cu HAINUTE_PS_MAX_PAGES pagini
 *    la fiecare rulare, ca în timp să acoperim tot catalogul (și să reîmprospătăm
 *    prețurile), respectând limita de 60 apeluri/60s.
 *
 * Constante wp-config:
 *   HAINUTE_PS_USER        — API user Profitshare
 *   HAINUTE_PS_KEY         — API key
 *   HAINUTE_PS_ADVERTISERS — id-uri advertiseri, separate prin virgulă (implicit 88736)
 *   HAINUTE_PS_MAX_PAGES   — pagini (×20) scanate pe rulare (implicit 200)
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_ps_base() {
	return 'https://api.profitshare.ro';
}

/** Limitator de rată: max 55 apeluri / 60s (marjă sub 60). */
function hainute_ps_throttle() {
	static $calls = array();
	$now   = microtime( true );
	$calls = array_filter(
		$calls,
		function ( $t ) use ( $now ) {
			return $t > $now - 60;
		}
	);
	if ( count( $calls ) >= 55 ) {
		$oldest = min( $calls );
		$wait   = (int) ceil( 61 - ( $now - $oldest ) );
		if ( $wait > 0 ) {
			sleep( $wait );
		}
		$calls = array();
	}
	$calls[] = microtime( true );
}

/**
 * GET semnat (HMAC-SHA1). Întoarce [status, decoded].
 */
function hainute_ps_get( $user, $key, $api, array $params = array() ) {
	hainute_ps_throttle();

	$qs   = $params ? urldecode( http_build_query( $params ) ) : '';
	$date = gmdate( 'D, d M Y H:i:s T', time() );
	$auth = hash_hmac( 'sha1', 'GET' . $api . '/?' . $qs . '/' . $user . $date, $key );

	$response = wp_remote_get(
		hainute_ps_base() . '/' . $api . '/?' . $qs,
		array(
			'timeout' => 40,
			'headers' => array(
				'Date'         => $date,
				'X-PS-Client'  => $user,
				'X-PS-Accept'  => 'json',
				'X-PS-Auth'    => $auth,
			),
		)
	);

	if ( is_wp_error( $response ) ) {
		return array( 0, null );
	}
	return array(
		(int) wp_remote_retrieve_response_code( $response ),
		json_decode( wp_remote_retrieve_body( $response ), true ),
	);
}

/** Termeni univoci de „copii" (fără „fata" — ambiguu cu „față"). */
function hainute_ps_kids_words() {
	return apply_filters(
		'hainute_ps_kids_words',
		array( 'copii', 'copil', 'baietel', 'baieti', 'baiat', 'fetita', 'fetite', 'fete', 'bebe', 'bebelus', 'nou-nascut', 'junior', 'kids' )
	);
}

/** Termeni de excludere (cosmetice/îngrijire care conțin totuși „copii"). */
function hainute_ps_exclude_words() {
	return apply_filters(
		'hainute_ps_exclude_words',
		array( 'crema', 'ser ', 'cosmetic', ' ten', 'machiaj', 'parfum', 'sampon', 'balsam', 'ingrijire', 'solara', 'lotiune', 'masca', 'gel de', 'sapun', 'deodorant', 'vitamina', 'supliment' )
	);
}

function hainute_ps_text_match( array $words, $text ) {
	$h = strtolower( remove_accents( (string) $text ) );
	foreach ( $words as $w ) {
		$n = strtolower( remove_accents( $w ) );
		if ( '' !== $n && false !== strpos( $h, $n ) ) {
			return true;
		}
	}
	return false;
}

/** Culori recunoscute (pentru extragere din titlu + curățare nume). */
function hainute_ps_colors() {
	return apply_filters(
		'hainute_ps_colors',
		array(
			'negru', 'alb', 'rosu', 'albastru', 'verde', 'roz', 'galben', 'gri', 'maro',
			'bleumarin', 'bej', 'mov', 'portocaliu', 'turcoaz', 'crem', 'bordo', 'kaki',
			'multicolor', 'visiniu', 'oliv', 'coral', 'fucsia', 'lila', 'argintiu', 'auriu',
			'grena', 'indigo', 'bleu', 'ivoire', 'nude', 'somon', 'petrol', 'antracit',
			'violet', 'mustar', 'camel', 'ecru', 'lavanda', 'mentol', 'piersica',
			'ciocolatiu', 'caramiziu', 'fistic', 'lime', 'marsala',
		)
	);
}

/**
 * Grupul de variantă = identitatea produsului în magazin.
 * part_number Fashion Days = „{model}-{culoare}_{marime}"; grupăm după {model}
 * (înainte de primul „-") ca să adunăm TOATE culorile și mărimile într-un produs.
 */
function hainute_ps_variant_group( $part_number ) {
	$pn = (string) $part_number;
	if ( '' === $pn ) {
		return '';
	}
	// înainte de primul „-" (model), fallback înainte de „_".
	if ( false !== strpos( $pn, '-' ) ) {
		return substr( $pn, 0, strpos( $pn, '-' ) );
	}
	if ( false !== strpos( $pn, '_' ) ) {
		return substr( $pn, 0, strpos( $pn, '_' ) );
	}
	return $pn;
}

/**
 * Descompune part_number „{model}-{codCuloare}_{codMarime}" în [cod_culoare,
 * cod_marime]. Codurile permit numărarea variantelor chiar și fără etichete în
 * titlu (codurile de mărime sunt globale, reutilizate între produse).
 */
function hainute_ps_decompose_pn( $part_number ) {
	$pn = (string) $part_number;
	$color_code = '';
	$size_code  = '';
	if ( preg_match( '/^[^-]+-([^_]+)_(.+)$/', $pn, $m ) ) {
		$color_code = $m[1];
		$size_code  = $m[2];
	} elseif ( preg_match( '/^[^_]+_(.+)$/', $pn, $m ) ) {
		$size_code = $m[1];
	} elseif ( preg_match( '/^[^-]+-(.+)$/', $pn, $m ) ) {
		$color_code = $m[1];
	}
	return array( $color_code, $size_code );
}

/** Extrage culoarea din titlu (primul cuvânt-culoare găsit, cu compuse simple). */
function hainute_ps_extract_color( $name ) {
	$h = strtolower( remove_accents( (string) $name ) );
	foreach ( hainute_ps_colors() as $c ) {
		if ( preg_match( '/\b' . preg_quote( $c, '/' ) . '\b/', $h ) ) {
			// compus gen „alb murdar" / „rosu inchis"
			if ( preg_match( '/\b' . preg_quote( $c, '/' ) . '\s+(murdar|inchis|deschis|prafuit)\b/', $h, $m ) ) {
				return ucfirst( $c ) . ' ' . $m[1];
			}
			return ucfirst( $c );
		}
	}
	return '';
}

/** Extrage mărimea LIZIBILĂ din titlu, dacă există (ex. „3 luni", „104", „EU 32"). */
function hainute_ps_extract_size( $name ) {
	$n = (string) $name;
	if ( preg_match( '/(\d+(?:[.,]\d+)?)\s*(luni|ani)\b/iu', $n, $m ) ) {
		return $m[1] . ' ' . strtolower( $m[2] );
	}
	if ( preg_match( '/\b(?:eu|mar(?:imea)?\.?)\s*(\d{2}(?:[.,]\d)?)\b/iu', $n, $m ) ) {
		return 'EU ' . $m[1];
	}
	// mărime „la coadă" gen „- 104" / „- 31"
	if ( preg_match( '/-\s*(\d{2,3})\s*$/u', trim( $n ), $m ) ) {
		return $m[1];
	}
	return '';
}

/**
 * Extrage mărime/culoare/material LIZIBILE din slug-ul URL-ului Fashion Days,
 * care le conține explicit (spre deosebire de titlu). Exemplu:
 *   /p/sandale-baieti-7895422-piele-naturala-26-eu-gri-baieti-primigi-p15760433-8/
 *          → material „Piele naturală", mărime „26 EU", culoare „gri".
 * Structura slug-ului: ...-{material}-{mărime}-eu-{culoare}-{gen}-{brand}-p{id}-{n}
 *
 * @return array { size:string, color:string, material:string }
 */
function hainute_ps_parse_url( $url ) {
	$out  = array( 'size' => '', 'color' => '', 'material' => '' );
	$path = strtolower( (string) ( parse_url( (string) $url, PHP_URL_PATH ) ?: $url ) );
	if ( '' === $path ) {
		return $out;
	}

	// Material (încălțăminte + textile).
	$materials = array(
		'piele-naturala' => 'Piele naturală',
		'piele-ecologica' => 'Piele ecologică',
		'piele-intoarsa' => 'Piele întoarsă',
		'poliamida' => 'Poliamidă',
		'poliester' => 'Poliester',
		'bumbac' => 'Bumbac',
		'lana' => 'Lână',
		'vascoza' => 'Vâscoză',
		'elastan' => 'Elastan',
		'catifea' => 'Catifea',
		'denim' => 'Denim',
		'blana' => 'Blană',
		'textil' => 'Textil',
		'sintetic' => 'Sintetic',
	);
	foreach ( $materials as $needle => $label ) {
		if ( false !== strpos( $path, $needle ) ) {
			$out['material'] = $label;
			break;
		}
	}

	// Mărime la încălțăminte: „26-eu".
	if ( preg_match( '/-(\d+(?:[.,]\d+)?)-eu(?:-|\/|$)/', $path, $m ) ) {
		$out['size'] = $m[1] . ' EU';
	} elseif ( preg_match( '/-(\d+)-(luni|ani)(?:-|\/|$)/', $path, $m ) ) {
		$out['size'] = $m[1] . ' ' . $m[2];
	}

	// Culoare: segmentul dintre „-eu-" (sau mărime) și marcatorul de gen.
	$gender = '(?:baieti|baietei|fete|fetite|unisex|copii|bebe|bebelusi|barbati|femei)';
	if ( preg_match( '/-eu-(.+?)-' . $gender . '-/', $path, $m ) ) {
		$out['color'] = str_replace( '-', ' ', $m[1] );
	} elseif ( preg_match( '/-' . $gender . '-(.+?)-' . $gender . '-/', $path, $m ) ) {
		// fără mărime-eu: „...-baieti-{material?}-{culoare}-baieti-brand..."
		$seg = str_replace( '-', ' ', $m[1] );
		// păstrăm doar dacă e un cuvânt-culoare cunoscut
		if ( '' !== hainute_ps_extract_color( $seg ) ) {
			$out['color'] = hainute_ps_extract_color( $seg );
		}
	}

	// Curățare culoare: dacă a prins gunoi lung, cade pe lista de culori.
	if ( '' !== $out['color'] ) {
		$c = trim( $out['color'] );
		if ( str_word_count( $c ) > 3 || strlen( $c ) > 22 ) {
			$c = hainute_ps_extract_color( $c );
		}
		$out['color'] = $c ? ucfirst( $c ) : '';
	}

	return $out;
}

/** Numele „de bază" curat: fără SKU/coduri, material, mărime, culoare. */
function hainute_ps_base_name( $name ) {
	$n = ' ' . (string) $name . ' ';

	// Separatorii (-,/) → spațiu întâi, ca să izolăm tokenii de cod.
	$n = preg_replace( '#[-,/]+#', ' ', $n );

	// Coduri/SKU: tokeni cu 3+ cifre consecutive (ex. 7895422, 555501, 103,
	// G3150287). Numele de model reale n-au 3 cifre la rând („Campus 00s",
	// „Air Max 90"), deci sunt în siguranță.
	$n = preg_replace( '/\s[A-Za-z]{0,3}\d{3,}[\dA-Za-z._]*/u', ' ', $n );

	// Coduri ALFANUMERICE lungi (ex. 4FJRMM00FFLIU128, JRSS25TTSHF2644,
	// IG0IG02056): 6+ caractere care conțin ȘI litere ȘI cifre. Cuvintele
	// normale (fără cifre) și cele scurte („00s") rămân.
	$n = preg_replace( '/\s(?=[A-Za-z0-9]*[A-Za-z])(?=[A-Za-z0-9]*\d)[A-Za-z0-9]{6,}\b/u', ' ', $n );

	// Materiale.
	foreach ( array( 'piele naturala', 'piele ecologica', 'piele intoarsa', 'piele', 'textil', 'sintetic', 'poliester', 'poliamida', 'bumbac', 'lana', 'vascoza', 'elastan', 'catifea', 'denim' ) as $mat ) {
		$n = preg_replace( '/\s*[-,]?\s*' . preg_quote( $mat, '/' ) . '\b/iu', ' ', $n );
	}

	// Mărimi (26 EU, 3 luni, 104 cm).
	$n = preg_replace( '/\s*[-,]?\s*\d+(?:[.,]\d+)?\s*(eu|uk|us|cm|luni|ani)\b/iu', ' ', $n );

	// Culori.
	foreach ( hainute_ps_colors() as $c ) {
		$n = preg_replace( '/\s*[-,]?\s*(?:' . $c . ')(\s+(?:murdar|inchis|deschis))?\b/iu', ' ', $n );
	}

	$n = trim( preg_replace( '/\s+/', ' ', $n ) );

	return '' !== $n ? $n : trim( (string) $name );
}

/** Gen din titlu (Fashion Days pune „băieți/fete" în nume, nu în categorie). */
function hainute_ps_gender_from( $text ) {
	$h = strtolower( remove_accents( (string) $text ) );
	if ( false !== strpos( $h, 'fete' ) || false !== strpos( $h, 'fetita' ) || false !== strpos( $h, 'fetite' ) ) {
		return 'Fete';
	}
	if ( false !== strpos( $h, 'baiet' ) || false !== strpos( $h, 'baiat' ) ) {
		return 'Băieți';
	}
	return '';
}

/**
 * Mapează un produs Profitshare la item-ul normalizat al importerului.
 */
function hainute_ps_map( array $p, $adv_id, $store ) {
	$price = (float) ( $p['price_vat'] ?? $p['price'] ?? 0 );
	$disc  = ( '' !== ( $p['price_discounted'] ?? '' ) ) ? (float) $p['price_discounted'] : 0;
	$old   = null;
	if ( $disc > 0 && $disc < $price ) {
		$old   = $price;
		$price = $disc;
	}

	$aff = (string) ( $p['affiliate_link'] ?? '' );
	if ( $aff && 0 === strpos( $aff, '//' ) ) {
		$aff = 'https:' . $aff;
	}

	$images = array_values( array_filter( array( (string) ( $p['image_original'] ?? '' ), (string) ( $p['image'] ?? '' ) ) ) );
	$name   = (string) ( $p['name'] ?? '' );

	// Grupare variante: toate culorile+mărimile aceluiași model = un produs.
	$group = hainute_ps_variant_group( $p['part_number'] ?? '' );
	if ( '' === $group ) {
		$group = md5( hainute_ps_base_name( $name ) . '|' . ( $p['brand_name'] ?? '' ) );
	}
	list( $color_code, $size_code ) = hainute_ps_decompose_pn( $p['part_number'] ?? '' );

	// URL-ul Fashion Days conține mărime/culoare/material LIZIBILE (titlul, nu).
	$from_url = hainute_ps_parse_url( (string) ( $p['link'] ?? $aff ) );
	$color    = $from_url['color'] ?: hainute_ps_extract_color( $name );
	$size     = $from_url['size'] ?: hainute_ps_extract_size( $name );

	return array(
		'network'     => 'profitshare',
		'program_id'  => (string) $adv_id,
		'store_name'  => $store,
		'external_id' => (string) $adv_id . ':' . $group,       // identitatea produsului (nu a variantei)
		'variant_id'  => (string) ( $p['part_number'] ?? '' ),  // varianta concretă
		'name'        => hainute_ps_base_name( $name ),          // titlu curat (fără culoare/mărime)
		'description' => (string) ( $p['description'] ?? '' ),
		'brand'       => (string) ( $p['brand_name'] ?? '' ),
		'category'    => hainute_canonical_category( (string) ( $p['category_name'] ?? '' ), $name, (string) ( $p['brand_name'] ?? '' ) ),
		'gender'      => hainute_ps_gender_from( $name . ' ' . ( $p['category_name'] ?? '' ) ),
		'age'         => '',
		'price'       => $price,
		'old_price'   => $old,
		'currency'    => 'RON',
		'in_stock'    => true, // feed-ul listează produse active
		'stock_qty'   => null,
		'url'         => $aff ?: (string) ( $p['link'] ?? '' ),
		'images'      => $images,
		'material'    => $from_url['material'],                  // material (din URL: piele/textil)
		'sizes'       => '',
		'color'       => $color,                                 // culoare (din URL, fallback titlu)
		'size'        => $size,                                  // mărime (din URL, fallback titlu)
		'color_code'  => $color_code,                            // codul de culoare (din part_number)
		'size_code'   => $size_code,                             // codul de mărime (global)
	);
}

/**
 * Punct de intrare al sursei.
 *
 * @return array { items: array[], notes: string[] }
 */
function hainute_profitshare_fetch_items() {
	$items = array();
	$notes = array();

	$user = hainute_config( 'HAINUTE_PS_USER' );
	$key  = hainute_config( 'HAINUTE_PS_KEY' );
	if ( ! $user || ! $key ) {
		return array( 'items' => $items, 'notes' => array( 'Profitshare inactiv (lipsă HAINUTE_PS_USER/HAINUTE_PS_KEY).' ) );
	}

	$advertisers = hainute_config( 'HAINUTE_PS_ADVERTISERS', '88736' ); // Fashion Days
	$advertisers = array_values( array_filter( array_map( 'trim', explode( ',', (string) $advertisers ) ) ) );
	$max_pages   = (int) hainute_config( 'HAINUTE_PS_MAX_PAGES', 200 );

	// Nume advertiseri (pentru afișare/magazin).
	$adv_names          = array();
	list( $ast, $adata ) = hainute_ps_get( $user, $key, 'affiliate-advertisers' );
	if ( 200 === $ast && isset( $adata['result'] ) ) {
		foreach ( $adata['result'] as $a ) {
			$adv_names[ (string) $a['id'] ] = $a['name'];
		}
	}

	$cursor = get_option( 'hainute_ps_cursor', array() );
	$kids   = hainute_ps_kids_words();
	$excl   = hainute_ps_exclude_words();

	foreach ( $advertisers as $adv_id ) {
		$store       = $adv_names[ $adv_id ] ?? ( 'Advertiser ' . $adv_id );
		$start       = max( 1, (int) ( $cursor[ $adv_id ] ?? 1 ) );
		$taken       = 0;
		$total_pages = 0;
		$last        = $start - 1;
		$retries     = 0;

		for ( $page = $start; $page < $start + $max_pages; $page++ ) {
			list( $pst, $pd ) = hainute_ps_get( $user, $key, 'affiliate-products', array( 'filters' => array( 'advertiser' => (int) $adv_id ), 'page' => $page ) );

			// Limită de rată → așteaptă și reîncearcă, cu plafon (ca să nu blocheze
			// cererea peste timeout-ul serverului; cursorul reia de aici data viitoare).
			if ( 429 === $pst || ( isset( $pd['error']['code'] ) && 'TOO_MANY_REQUESTS' === $pd['error']['code'] ) ) {
				if ( ++$retries > 3 ) {
					$notes[] = "Profitshare: prea multe 429 la pagina $page — mă opresc (reiau la rularea următoare)";
					break;
				}
				sleep( 60 );
				$page--; // reîncearcă aceeași pagină
				continue;
			}
			$retries = 0;
			if ( 200 !== $pst || ! isset( $pd['result']['products'] ) ) {
				$notes[] = "Profitshare: $store pagina $page — răspuns neașteptat, stop";
				break;
			}

			$total_pages = (int) ( $pd['result']['total_pages'] ?? 0 );
			$products    = $pd['result']['products'];
			if ( empty( $products ) ) {
				break;
			}

			foreach ( $products as $p ) {
				$hay = ( $p['category_name'] ?? '' ) . ' ' . ( $p['name'] ?? '' );
				if ( ! hainute_ps_text_match( $kids, $hay ) ) {
					continue;
				}
				if ( hainute_ps_text_match( $excl, $hay ) ) {
					continue;
				}
				$items[] = hainute_ps_map( (array) $p, $adv_id, $store );
				$taken++;
			}

			$last = $page;
			if ( $total_pages && $page >= $total_pages ) {
				break;
			}
		}

		// Avansează cursorul (cu wrap la 1 după ce am parcurs tot catalogul).
		$next = $last + 1;
		if ( $total_pages && $next > $total_pages ) {
			$next = 1;
		}
		$cursor[ $adv_id ] = $next;

		$notes[] = sprintf(
			'Profitshare: %s → %d produse copii (pagini %d–%d din %d)',
			$store,
			$taken,
			$start,
			$last,
			$total_pages
		);
	}

	update_option( 'hainute_ps_cursor', $cursor, false );

	return array( 'items' => $items, 'notes' => $notes );
}
