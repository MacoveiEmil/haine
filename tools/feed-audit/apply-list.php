<?php
/**
 * Listă de aplicare prioritizată: magazine din rețeaua 2Performant (și
 * advertiseri CJ) relevante pentru copii/sport/încălțăminte, care AU feed de
 * produse (deci dau catalog utilizabil imediat după aprobare). Sortate ca să
 * maximizeze suprapunerile cross-store (branduri mainstream comune).
 *
 * Scrie output/lista-aplicare.csv.
 * Rulare: php -d extension=curl apply-list.php
 */

error_reporting( E_ALL & ~E_DEPRECATED );
require __DIR__ . '/lib/common.php';
require __DIR__ . '/lib/twoperformant.php';

$config = require __DIR__ . '/config.php';

// Cuvinte care indică relevanță pentru copii / sport / încălțăminte / modă.
$relevant = array(
	'copil', 'copii', 'bebe', 'baby', 'kid', 'nichiduta', 'chicco', 'noriel',
	'jucar', 'toyz', 'papus', 'sport', 'shoe', 'incaltaminte', 'pantofi', 'zapatos',
	'sneaker', 'decathlon', 'fashion', 'moda', 'haine', 'imbracaminte', 'textil',
	'nike', 'adidas', 'puma',
);

// Cuvinte care indică suprapunere probabilă (branduri mainstream) → prioritate.
$overlap_hint = array( 'sport', 'shoe', 'pantofi', 'sneaker', 'incaltaminte', 'decathlon', 'zapatos' );

function is_relevant( $text, $words ) {
	$h = fa_norm( $text );
	foreach ( $words as $w ) {
		if ( false !== strpos( $h, fa_norm( $w ) ) ) {
			return true;
		}
	}
	return false;
}

$rows = array();

/* ---- 2Performant: programele din rețea cu feed ---- */
$auth = fa_2p_signin( $config['2performant']['email'], $config['2performant']['password'] );
if ( isset( $auth['error'] ) ) {
	fa_log( '2Performant: ' . $auth['error'] );
} else {
	fa_log( '2Performant: extrag programele din rețea...' );
	for ( $page = 1; $page <= 20; $page++ ) {
		usleep( 350000 );
		list( $st, $data ) = fa_2p_get( "affiliate/programs.json?page=$page&perpage=50", $auth );
		if ( 429 === $st ) {
			fa_log( "  429 la pagina $page — aștept 60s..." );
			sleep( 60 );
			$page--;
			continue;
		}
		if ( 200 !== $st ) {
			break;
		}
		$progs = $data['programs'] ?? array();
		if ( empty( $progs ) ) {
			break;
		}
		foreach ( $progs as $p ) {
			$name  = trim( (string) ( $p['name'] ?? '' ) );
			$cat   = (string) ( $p['category']['name'] ?? $p['category'] ?? '' );
			$feeds = (int) ( $p['product_feeds_count'] ?? 0 );
			$prods = (int) ( $p['products_count'] ?? 0 );

			if ( $feeds < 1 ) {
				continue; // fără feed = nu are rost să aplici pt agregator
			}
			if ( ! is_relevant( $name . ' ' . $cat, $relevant ) ) {
				continue;
			}

			$rows[] = array(
				'platforma'   => '2performant',
				'magazin'     => $name,
				'categorie'   => $cat,
				'produse'     => $prods,
				'are_feed'    => 'da',
				'suprapunere' => is_relevant( $name . ' ' . $cat, $GLOBALS['overlap_hint'] ) ? 'RIDICATĂ' : 'medie',
				'actiune'     => 'Aplică pe 2Performant',
			);
		}
		$pg = $data['metadata']['pagination'] ?? array();
		if ( ( (int) ( $pg['pages'] ?? 0 ) && $page >= (int) $pg['pages'] ) || count( $progs ) < 50 ) {
			break;
		}
	}
	fa_log( '2Performant: ' . count( $rows ) . ' magazine relevante cu feed.' );
}

/* ---- CJ: advertiseri relevanți din CSV-ul deja extras ---- */
$cj_csv = __DIR__ . '/output/cj-advertisers.csv';
if ( file_exists( $cj_csv ) ) {
	$fh = fopen( $cj_csv, 'r' );
	fgetcsv( $fh );
	$cj_added = 0;
	while ( ( $r = fgetcsv( $fh ) ) !== false ) {
		// coloane: id, advertiser, status_relatie, status_cont, cat_parinte, cat_copil, epc7z, epc3l, rank, url
		$name = $r[1];
		$cat  = $r[4] . '/' . $r[5];
		$url  = $r[9];
		// RO-friendly + relevant + EPC pozitiv.
		$ro   = ( false !== stripos( $url, '.ro' ) ) || in_array( strtolower( $name ), array( 'shein', 'sportisimo', 'factcool', 'heliumking' ), true );
		if ( ! $ro || ! is_relevant( $name . ' ' . $cat, $GLOBALS['relevant'] ) ) {
			continue;
		}
		$rows[] = array(
			'platforma'   => 'cj',
			'magazin'     => $name,
			'categorie'   => $cat,
			'produse'     => '',
			'are_feed'    => 'da (API)',
			'suprapunere' => is_relevant( $name . ' ' . $cat, $GLOBALS['overlap_hint'] ) ? 'RIDICATĂ' : 'medie',
			'actiune'     => 'Aplică pe CJ',
		);
		$cj_added++;
	}
	fclose( $fh );
	fa_log( "CJ: $cj_added advertiseri relevanți RO-friendly." );
}

// Sortează: suprapunere RIDICATĂ întâi, apoi după nr. produse.
usort(
	$rows,
	function ( $a, $b ) {
		$pa = ( 'RIDICATĂ' === $a['suprapunere'] ) ? 0 : 1;
		$pb = ( 'RIDICATĂ' === $b['suprapunere'] ) ? 0 : 1;
		if ( $pa !== $pb ) {
			return $pa - $pb;
		}
		return (int) $b['produse'] <=> (int) $a['produse'];
	}
);

fa_write_csv(
	__DIR__ . '/output/lista-aplicare.csv',
	array( 'platforma', 'magazin', 'categorie', 'produse', 'are_feed', 'suprapunere', 'actiune' ),
	$rows
);

fa_log( "\n=== TOP magazine de aplicat (suprapunere RIDICATĂ) ===" );
foreach ( $rows as $r ) {
	if ( 'RIDICATĂ' === $r['suprapunere'] ) {
		fa_log( sprintf( '  [%s] %-26s %s produse  [%s]', $r['platforma'], $r['magazin'], $r['produse'] ?: '?', $r['categorie'] ) );
	}
}
fa_log( "\nTotal în listă: " . count( $rows ) . ' → output/lista-aplicare.csv' );
