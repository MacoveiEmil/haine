<?php
/**
 * Verifică, pentru fiecare program 2Performant ACCEPTAT, dacă are feed de
 * produse (product_feeds_count) și câte produse. Scrie:
 *   output/2p-programe-cu-feed.csv   — toate programele acceptate cu feed
 *   consola                          — evidențiază magazinele de copii cu feed
 *
 * Rulare: php -d extension=curl 2p-feeds-check.php
 */

error_reporting( E_ALL & ~E_DEPRECATED );
require __DIR__ . '/lib/common.php';
require __DIR__ . '/lib/twoperformant.php';

$config = require __DIR__ . '/config.php';

// Cuvinte pentru „relevant copii/haine/încălțăminte/jucării".
$kids_kw = array(
	'bebe', 'baby', 'bb', 'kid', 'copil', 'copii', 'nichiduta', 'chicco', 'noriel',
	'papus', 'jolly', 'hippo', 'toyz', 'jucar', 'ludi', 'zurli', 'kinder', 'trotty',
	'nannie', 'bimbo', 'baobao', 'petit', 'minikids', 'xkids', 'littlenest', 'kidsly',
	'babyroll', 'dehaine', 'shoes', 'zapatos', 'zappatos', 'aldo', 'wojas', 'tezyo',
	'sneaker', 'gryxx', 'benvenuti', 'saray', 'ada-shoes', 'decathlon', 'sportdepot',
	'topsport', 'armansport', 'afisport', 'sportmaniac', 'fashion', 'incaltaminte',
);

$auth = fa_2p_signin( $config['2performant']['email'], $config['2performant']['password'] );
if ( isset( $auth['error'] ) ) {
	exit( '2Performant: ' . $auth['error'] . "\n" );
}
fa_log( '2Performant: autentificat. Extrag programele acceptate...' );

$rows = array();
for ( $page = 1; $page <= 20; $page++ ) {
	usleep( 350000 );
	list( $st, $data ) = fa_2p_get( "affiliate/programs.json?page=$page&perpage=50&filter[relation]=accepted", $auth );
	if ( 429 === $st ) {
		fa_log( "  429 la pagina $page — aștept 60s..." );
		sleep( 60 );
		$page--;
		continue;
	}
	if ( 200 !== $st ) {
		fa_log( "  pagina $page: HTTP $st — stop" );
		break;
	}
	$progs = $data['programs'] ?? array();
	if ( empty( $progs ) ) {
		break;
	}
	foreach ( $progs as $p ) {
		$rows[] = array(
			'magazin'       => trim( (string) ( $p['name'] ?? '' ) ),
			'program_id'    => (string) ( $p['id'] ?? '' ),
			'feeds'         => (int) ( $p['product_feeds_count'] ?? 0 ),
			'produse'       => (int) ( $p['products_count'] ?? 0 ),
			'comision'      => (string) ( $p['default_payout'] ?? $p['commission'] ?? '' ),
			'categorie'     => (string) ( $p['category']['name'] ?? $p['category'] ?? '' ),
		);
	}
	$pg = $data['metadata']['pagination'] ?? array();
	if ( ( (int) ( $pg['pages'] ?? 0 ) && $page >= (int) $pg['pages'] ) || count( $progs ) < 50 ) {
		break;
	}
}

fa_log( 'Total programe acceptate: ' . count( $rows ) );

// Programe cu feed.
$with_feed = array_filter( $rows, function ( $r ) {
	return $r['feeds'] > 0;
} );
fa_log( 'Programe cu feed de produse: ' . count( $with_feed ) );

// Salvează toate cele cu feed.
fa_write_csv(
	__DIR__ . '/output/2p-programe-cu-feed.csv',
	array( 'magazin', 'program_id', 'feeds', 'produse', 'comision', 'categorie' ),
	array_values( $with_feed )
);

// Evidențiază magazinele de copii cu feed.
fa_log( "\n=== MAGAZINE DE COPII CU FEED (utilizabile imediat) ===" );
$kids_feed = 0;
foreach ( $with_feed as $r ) {
	$hay = fa_norm( $r['magazin'] . ' ' . $r['categorie'] );
	foreach ( $kids_kw as $kw ) {
		if ( false !== strpos( $hay, fa_norm( $kw ) ) ) {
			fa_log( sprintf( '  %-28s %d feed(uri), %d produse  [%s]', $r['magazin'], $r['feeds'], $r['produse'], $r['categorie'] ) );
			$kids_feed++;
			break;
		}
	}
}
fa_log( "  → $kids_feed magazine de copii cu feed." );

// Și magazinele de copii FĂRĂ feed (ai relația, dar nu poți trage produse).
fa_log( "\n=== magazine de copii ACCEPTATE dar FĂRĂ feed ===" );
$kids_nofeed = 0;
foreach ( $rows as $r ) {
	if ( $r['feeds'] > 0 ) {
		continue;
	}
	$hay = fa_norm( $r['magazin'] . ' ' . $r['categorie'] );
	foreach ( $kids_kw as $kw ) {
		if ( false !== strpos( $hay, fa_norm( $kw ) ) ) {
			fa_log( '  ' . $r['magazin'] );
			$kids_nofeed++;
			break;
		}
	}
}
fa_log( "  → $kids_nofeed magazine de copii fără feed." );
