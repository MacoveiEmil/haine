<?php
/**
 * Feed audit — scoate inventarul și produsele disponibile din 2Performant, CJ
 * și Awin într-un set de CSV-uri. Standalone, fără WordPress.
 *
 * Rulare:
 *   php audit.php
 *
 * Ieșire (folderul output/):
 *   inventory.csv           — toate advertiserii/feed-urile + nr. produse
 *   products-all.csv        — toate produsele, combinate
 *   products-<platforma>.csv — produsele fiecărei platforme separat
 */

error_reporting( E_ALL & ~E_DEPRECATED );

if ( ! function_exists( 'curl_init' ) ) {
	fwrite( STDERR, "Lipsește extensia PHP curl. Rulează cu:\n  php -d extension=curl audit.php\n" );
	exit( 1 );
}

$dir = __DIR__;
require $dir . '/lib/common.php';
require $dir . '/lib/twoperformant.php';
require $dir . '/lib/cj.php';
require $dir . '/lib/awin.php';

$config_file = $dir . '/config.php';
if ( ! file_exists( $config_file ) ) {
	fwrite( STDERR, "Nu există config.php. Copiază config.example.php în config.php și completează cheile.\n" );
	exit( 1 );
}
$config = require $config_file;

fa_log( '=== Feed Audit — start ' . date( 'Y-m-d H:i' ) . ' ===' );
fa_log( 'Limită per feed: ' . ( (int) $config['per_feed_limit'] ?: 'toate' ) );
fa_log( '' );

$all_inventory = array();
$all_products  = array();

$runners = array(
	'2performant' => 'fa_2p_run',
	'cj'          => 'fa_cj_run',
	'awin'        => 'fa_awin_run',
);

foreach ( $runners as $name => $fn ) {
	if ( empty( $config[ $name ] ) ) {
		continue;
	}
	fa_log( "--- $name ---" );
	$res = $fn( $config[ $name ], $config );

	foreach ( $res['notes'] as $note ) {
		fa_log( '  ' . $note );
	}

	$all_inventory = array_merge( $all_inventory, $res['inventory'] );
	$all_products  = array_merge( $all_products, $res['products'] );

	// CSV per platformă.
	if ( ! empty( $res['products'] ) ) {
		fa_write_csv(
			"$dir/output/products-$name.csv",
			fa_product_columns(),
			$res['products']
		);
	}
	fa_log( '' );
}

// Inventar combinat.
fa_write_csv(
	"$dir/output/inventory.csv",
	array( 'platforma', 'advertiser', 'feed', 'feed_id', 'produse_total', 'status' ),
	$all_inventory
);

// Toate produsele combinate.
fa_write_csv(
	"$dir/output/products-all.csv",
	fa_product_columns(),
	$all_products
);

fa_log( '=== Gata ===' );
fa_log( 'Inventar : ' . count( $all_inventory ) . ' feed-uri/advertiseri  → output/inventory.csv' );
fa_log( 'Produse  : ' . count( $all_products ) . ' rânduri              → output/products-all.csv' );
