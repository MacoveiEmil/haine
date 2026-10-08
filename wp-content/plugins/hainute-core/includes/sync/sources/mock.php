<?php
/**
 * Mock feed source — reads JSON files from the plugin's mock-feeds/ folder.
 * Each file simulates one store's feed and already uses the normalized item
 * shape (see importer.php). Used until real 2Performant / CJ access exists;
 * the real sources will expose the same hainute_*_fetch_items() contract.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Read all mock feeds and return one flat list of normalized items.
 *
 * @return array { items: array[], notes: string[] }
 */
function hainute_mock_fetch_items() {
	$dir   = HAINUTE_CORE_DIR . 'mock-feeds/';
	$files = glob( $dir . '*.json' );
	$items = array();
	$notes = array();

	if ( empty( $files ) ) {
		$notes[] = 'Niciun fișier mock găsit în ' . $dir;
		return array( 'items' => $items, 'notes' => $notes );
	}

	foreach ( $files as $file ) {
		$decoded = json_decode( file_get_contents( $file ), true );

		if ( ! is_array( $decoded ) ) {
			$notes[] = 'JSON invalid, sărit: ' . basename( $file );
			continue;
		}

		$notes[] = sprintf( '%s: %d produse', basename( $file ), count( $decoded ) );
		$items   = array_merge( $items, $decoded );
	}

	return array( 'items' => $items, 'notes' => $notes );
}
