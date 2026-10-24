<?php
/**
 * Rank Math: categoriile, brandurile și magazinele în sitemap-ul lui (setarea de
 * taxonomii e oprită implicit). Aici, în plugin, nu în temă: Rank Math își citește
 * setările înainte să se încarce tema. Ce termeni intră: filtrele din tema/inc/seo.php.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_filter(
	'option_rank-math-options-sitemap',
	function ( $opt ) {
		$opt = is_array( $opt ) ? $opt : array();
		foreach ( array( 'product_cat', 'product_brand', 'store' ) as $tax ) {
			$opt[ 'tax_' . $tax . '_sitemap' ] = 'on';
		}
		return $opt;
	}
);
