<?php
/**
 * Publică descrieri din content/descrieri/{id}.json pe site (după ce au trecut
 * verificarea tools/descrieri.py). Rulează în containerul wp:
 *   php apply-descriere.php /tmp/desc/8566.json [/tmp/desc/8791.json ...]
 * Textul vechi se păstrează o dată în _hainute_desc_v2_backup (revenire posibilă).
 */
require '/var/www/html/wp-load.php';

foreach ( array_slice( $argv, 1 ) as $file ) {
	$x  = json_decode( (string) file_get_contents( $file ), true );
	$id = (int) ( $x['id'] ?? 0 );
	if ( ! $id || 'product' !== get_post_type( $id ) || empty( $x['descriere_html'] ) ) {
		echo "SĂRIT $file: id sau descriere lipsă\n";
		continue;
	}
	if ( ! get_post_meta( $id, '_hainute_desc_v2_backup', true ) ) {
		update_post_meta( $id, '_hainute_desc_v2_backup', array( 'content' => get_post_field( 'post_content', $id ), 'specs' => get_post_meta( $id, '_hainute_specs', true ) ) );
	}
	$html = wp_kses_post( $x['descriere_html'] );
	if ( function_exists( 'hainute_fix_content_cat_links' ) ) {
		$html = hainute_fix_content_cat_links( $id, $html ); // linkuri spre categorii mutate între timp
	}
	wp_update_post( array( 'ID' => $id, 'post_content' => $html ) );
	$specs = array_filter( array_map( 'sanitize_text_field', (array) ( $x['specificatii_tehnice'] ?? array() ) ) );
	if ( $specs ) {
		update_post_meta( $id, '_hainute_specs', $specs );
	}
	update_post_meta( $id, '_hainute_desc_version', sanitize_key( $x['versiune'] ?? 'v4' ) ); // din fișier (prompt v5+)
	update_post_meta( $id, '_hainute_desc_file_hash', md5_file( $file ) );
	update_post_meta( $id, '_hainute_desc_published', time() );
	echo "PUBLICAT $id " . wp_make_link_relative( get_permalink( $id ) ) . "\n";
}
