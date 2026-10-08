<?php
/**
 * Extrage produsele de COPII Fashion Days (și ceilalți advertiseri țintă din
 * config) prin Profitshare, în output/products-profitshare-copii.csv, plus
 * lista de advertiseri în output/profitshare-advertiseri.csv.
 *
 * Rulare: php -d extension=curl profitshare-extract.php
 */

error_reporting( E_ALL & ~E_DEPRECATED );
require __DIR__ . '/lib/common.php';
require __DIR__ . '/lib/profitshare.php';

$config = require __DIR__ . '/config.php';

// Extragere mai amplă pentru a vedea catalogul (nu doar eșantion).
$config['per_feed_limit']            = 1500;
$config['profitshare']['max_pages']  = 900;

fa_log( '=== Profitshare — extragere copii  ' . date( 'Y-m-d H:i' ) . ' ===' );
fa_log( 'Țintă: până la ' . $config['per_feed_limit'] . ' produse copii (poate dura ~15 min din cauza limitei de rată).' );

$res = fa_ps_run( $config['profitshare'], $config );

foreach ( $res['notes'] as $n ) {
	fa_log( '  ' . $n );
}

if ( ! empty( $res['inventory'] ) ) {
	fa_write_csv(
		__DIR__ . '/output/profitshare-advertiseri.csv',
		array( 'platforma', 'advertiser', 'feed', 'feed_id', 'produse_total', 'status' ),
		$res['inventory']
	);
}

fa_write_csv(
	__DIR__ . '/output/products-profitshare-copii.csv',
	fa_product_columns(),
	$res['products']
);

// Rezumat pe categorii și branduri.
$cats   = array();
$brands = array();
foreach ( $res['products'] as $p ) {
	$cats[ $p['categorie'] ] = ( $cats[ $p['categorie'] ] ?? 0 ) + 1;
	if ( '' !== $p['brand'] ) {
		$brands[ $p['brand'] ] = ( $brands[ $p['brand'] ] ?? 0 ) + 1;
	}
}
arsort( $cats );
arsort( $brands );

fa_log( "\n=== " . count( $res['products'] ) . ' produse copii → output/products-profitshare-copii.csv ===' );
fa_log( 'Top categorii:' );
$i = 0;
foreach ( $cats as $c => $n ) {
	if ( $i++ < 10 ) {
		fa_log( "  $c: $n" );
	}
}
fa_log( 'Top branduri:' );
$i = 0;
foreach ( $brands as $b => $n ) {
	if ( $i++ < 12 ) {
		fa_log( "  $b: $n" );
	}
}
