<?php
/**
 * Listă prioritizată produse COPII Fashion Days, sortată după:
 *   1) cross-availability — apare și la alte platforme (various-brands, answear,
 *      incaltamintelamoda pe 2P; SHEIN etc. pe CJ). Modivo NU (fără acces).
 *   2) reach — tier de popularitate brand + cerere pe categorie (euristică
 *      justificată, NU volume Google reale).
 *
 * Ieșire: output/fd-prioritate-copii.csv
 * Rulare: php -d extension=curl fd-priority-list.php
 */

error_reporting( E_ALL & ~E_DEPRECATED );
require __DIR__ . '/lib/common.php';
require __DIR__ . '/lib/profitshare.php';
require __DIR__ . '/lib/twoperformant.php';
require __DIR__ . '/lib/cj.php';

$config = require __DIR__ . '/config.php';

/* ---------- matching brand+model (portat din plugin) ---------- */
function pk_norm_brand( $b ) {
	$b = strtolower( @iconv( 'UTF-8', 'ASCII//TRANSLIT//IGNORE', (string) $b ) );
	return trim( preg_replace( '/\s+/', ' ', preg_replace( '/[^a-z0-9 ]+/', ' ', $b ) ) );
}
function pk_key( $brand, $name ) {
	$stop = array( 'pentru', 'copii', 'copil', 'baietel', 'baieti', 'baiat', 'fetita', 'fetite', 'fete', 'bebe', 'bebelus', 'unisex', 'de', 'cu', 'si', 'la', 'din', 'in', 'model', 'nou', 'set' );
	$type = array( 'pantofi', 'pantof', 'sport', 'sneakers', 'sneaker', 'adidasi', 'adidas', 'tenisi', 'sandale', 'ghete', 'cizme', 'papuci', 'geaca', 'jacheta', 'hanorac', 'pulover', 'bluza', 'tricou', 'camasa', 'rochie', 'fusta', 'pantaloni', 'blugi', 'jeans', 'sort', 'trening', 'salopeta', 'pijama', 'body', 'sapca', 'caciula', 'geanta', 'rucsac', 'sosete', 'material', 'bumbac', 'piele', 'textil', 'adidasi' );
	$t = strtolower( @iconv( 'UTF-8', 'ASCII//TRANSLIT//IGNORE', (string) $name ) );
	$t = preg_replace( '/[^a-z0-9 ]+/', ' ', $t );
	$tokens = array_filter( explode( ' ', $t ) );
	$bt     = array_filter( explode( ' ', pk_norm_brand( $brand ) ) );
	$tokens = array_diff( $tokens, $stop, $type, $bt );
	$tokens = array_unique( $tokens );
	sort( $tokens );
	return implode( ' ', $tokens );
}
function pk_brands_match( $a, $b ) {
	if ( '' === $a || '' === $b ) {
		return false;
	}
	return $a === $b || 0 === strpos( $a, $b . ' ' ) || 0 === strpos( $b, $a . ' ' );
}
function pk_match( $brandA, $keyA, $brandB, $keyB ) {
	if ( '' === $keyA || '' === $keyB ) {
		return false;
	}
	if ( count( array_filter( explode( ' ', $keyA ) ) ) < 2 ) {
		return false;
	}
	if ( ! pk_brands_match( pk_norm_brand( $brandA ), pk_norm_brand( $brandB ) ) ) {
		return false;
	}
	$shared = array_intersect( array_filter( explode( ' ', $keyA ) ), array_filter( explode( ' ', $keyB ) ) );
	$anchor = false;
	foreach ( $shared as $x ) {
		if ( strlen( $x ) >= 4 ) {
			$anchor = true;
			break;
		}
	}
	return $anchor && count( $shared ) >= 2;
}

/* ---------- tier popularitate brand ---------- */
function brand_tier( $brand ) {
	$b = pk_norm_brand( $brand );
	$t5 = array( 'nike', 'adidas', 'puma' );
	$t4 = array( 'vans', 'reebok', 'converse', 'new balance', 'crocs', 'skechers', 'levis', 'levi s', 'tommy hilfiger', 'calvin klein', 'guess', 'lacoste', 'under armour' );
	$t3 = array( 'geox', 'timberland', 'columbia', 'champion', 'fila', 'kappa', 'diadora', 'asics', 'jordan', 'napapijri', 'ellesse', 'polo ralph lauren', 'boss', 'hugo' );
	$t2 = array( 'mayoral', 'name it', 'coccodrillo', '4f', 'benetton', 'froddo', 'primigi', 'united colors of benetton', 'ea7', 'karl lagerfeld', 'elisabetta franchi', 'bibi' );
	foreach ( array( 5 => $t5, 4 => $t4, 3 => $t3, 2 => $t2 ) as $tier => $list ) {
		foreach ( $list as $x ) {
			if ( $b === $x || false !== strpos( $b, $x ) ) {
				return $tier;
			}
		}
	}
	return 1; // nișă / brand de magazin / necunoscut
}

/* ---------- cerere pe categorie ---------- */
function cat_demand( $cat, $name ) {
	$h = strtolower( @iconv( 'UTF-8', 'ASCII//TRANSLIT//IGNORE', $cat . ' ' . $name ) );
	$high = array( 'pantofi sport', 'adidasi', 'sneaker', 'pantofi', 'sandale', 'ghete', 'cizme', 'papuci', 'incaltaminte' );
	$mid  = array( 'geaca', 'geci', 'hanorac', 'trening', 'rochie', 'blugi', 'pantaloni', 'salopeta', 'pijama', 'bluza', 'tricou' );
	foreach ( $high as $w ) {
		if ( false !== strpos( $h, $w ) ) {
			return 3;
		}
	}
	foreach ( $mid as $w ) {
		if ( false !== strpos( $h, $w ) ) {
			return 2;
		}
	}
	return 1;
}

/* ================= 1. Fashion Days copii ================= */
fa_log( '1/4 Extrag produsele copii Fashion Days (țintă ~1000)...' );
$config['per_feed_limit']           = 1000;
$config['profitshare']['max_pages'] = 1800;
$fd  = fa_ps_run( $config['profitshare'], $config );
$fdp = $fd['products'];
foreach ( $fd['notes'] as $n ) {
	fa_log( '   ' . $n );
}
fa_log( '   Fashion Days: ' . count( $fdp ) . ' produse copii.' );

/* ================= 2. Pool „alte platforme" ================= */
fa_log( '2/4 Construiesc pool-ul de pe alte platforme (2P + CJ)...' );
$pool = array(); // fiecare: [store, brand, key]

// 2P: various-brands (4272), answear copii (2085), incaltamintelamoda (9157)
$auth = fa_2p_signin( $config['2performant']['email'], $config['2performant']['password'] );
if ( ! isset( $auth['error'] ) ) {
	$feeds = array( '4272' => 'various-brands', '2085' => 'answear', '9157' => 'incaltamintelamoda' );
	$caps  = array( '4272' => 90, '2085' => 25, '9157' => 8 );
	$kids  = array( 'copii', 'copil', 'baietel', 'baieti', 'baiat', 'fetita', 'fetite', 'fete', 'bebe', 'bebelus', 'junior', 'kids' );
	foreach ( $feeds as $code => $store ) {
		$got = 0;
		for ( $page = 1; $page <= $caps[ $code ]; $page++ ) {
			usleep( 320000 );
			list( $st, $d ) = fa_2p_get( "affiliate/product_feeds/$code/products.json?page=$page&perpage=40", $auth );
			if ( 429 === $st ) {
				sleep( 60 );
				$page--;
				continue;
			}
			if ( 200 !== $st || empty( $d['products'] ) ) {
				break;
			}
			foreach ( $d['products'] as $p ) {
				$title = ( $p['title'] ?? '' ) . ' ' . ( $p['category'] ?? '' );
				if ( ! fa_keyword_ok( $kids, $title ) ) {
					continue;
				}
				$brand = $p['brand'] ?? '';
				$pool[] = array( 'store' => $store, 'brand' => $brand, 'key' => pk_key( $brand, $p['title'] ?? '' ) );
				$got++;
			}
			if ( count( $d['products'] ) < 40 ) {
				break;
			}
		}
		fa_log( "   2P $store: $got produse în pool." );
	}
}

// CJ: produse „copii"
$cj = fa_cj_run( $config['cj'], $config );
foreach ( $cj['products'] as $p ) {
	$pool[] = array( 'store' => 'CJ:' . $p['advertiser'], 'brand' => $p['brand'], 'key' => pk_key( $p['brand'], $p['titlu'] ) );
}
fa_log( '   CJ: ' . count( $cj['products'] ) . ' produse în pool. Total pool: ' . count( $pool ) );

/* ================= 3. Cross-check + scoruri ================= */
fa_log( '3/4 Potrivesc Fashion Days cu pool-ul + calculez scoruri...' );
// index pool pe brand normalizat (accelerează)
$pool_by_brand = array();
foreach ( $pool as $pp ) {
	$pool_by_brand[ pk_norm_brand( $pp['brand'] ) ][] = $pp;
}

$rows = array();
foreach ( $fdp as $p ) {
	$brand = $p['brand'];
	$key   = pk_key( $brand, $p['titlu'] );
	$nb    = pk_norm_brand( $brand );

	$stores = array();
	// compară doar cu produse din pool cu brand potrivit (prefix)
	foreach ( $pool_by_brand as $pb => $list ) {
		if ( ! pk_brands_match( $nb, $pb ) ) {
			continue;
		}
		foreach ( $list as $cand ) {
			if ( pk_match( $brand, $key, $cand['brand'], $cand['key'] ) ) {
				$stores[ $cand['store'] ] = true;
			}
		}
	}
	$cross_stores = array_keys( $stores );
	$cross_score  = count( $cross_stores );

	$bt    = brand_tier( $brand );
	$cd    = cat_demand( $p['categorie'], $p['titlu'] );
	$reach = $bt * 2 + $cd; // 3..13

	$rows[] = array(
		'titlu'         => $p['titlu'],
		'brand'         => $brand,
		'categorie'     => $p['categorie'],
		'pret'          => $p['pret'],
		'tier_brand'    => $bt,
		'cerere_categ'  => $cd,
		'scor_reach'    => $reach,
		'gasit_pe'      => implode( ' | ', $cross_stores ),
		'nr_platforme'  => $cross_score,
		'scor_total'    => $cross_score * 100 + $reach, // cross-availability primează
		'url_afiliat'   => $p['url_afiliat'],
		'imagine'       => $p['imagine'],
	);
}

// sortare: scor_total desc (cross-availability apoi reach)
usort(
	$rows,
	function ( $a, $b ) {
		return $b['scor_total'] <=> $a['scor_total'];
	}
);

/* ================= 4. Scrie CSV ================= */
$cols = array( 'titlu', 'brand', 'categorie', 'pret', 'tier_brand', 'cerere_categ', 'scor_reach', 'nr_platforme', 'gasit_pe', 'scor_total', 'url_afiliat', 'imagine' );
fa_write_csv( __DIR__ . '/output/fd-prioritate-copii.csv', $cols, $rows );

$with_cross = 0;
foreach ( $rows as $r ) {
	if ( $r['nr_platforme'] > 0 ) {
		$with_cross++;
	}
}
fa_log( "4/4 GATA. " . count( $rows ) . " produse → output/fd-prioritate-copii.csv" );
fa_log( "   Din care găsite și pe alte platforme: $with_cross" );
fa_log( "\n=== TOP 15 ===" );
foreach ( array_slice( $rows, 0, 15 ) as $i => $r ) {
	fa_log( sprintf( '%2d. [%s|reach %d] %-42s | %s', $i + 1, $r['nr_platforme'] . ' plat', $r['scor_reach'], substr( $r['titlu'], 0, 40 ), $r['gasit_pe'] ?: '—' ) );
}
