<?php
/**
 * Theme supports, menus, image sizes.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_theme_setup() {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
	add_theme_support( 'automatic-feed-links' );

	register_nav_menus(
		array(
			'primary' => __( 'Meniu principal', 'hainute' ),
			'footer'  => __( 'Meniu footer', 'hainute' ),
		)
	);

	// Product card thumbnail (listing pages).
	add_image_size( 'product-card', 400, 400, true );
}
add_action( 'after_setup_theme', 'hainute_theme_setup' );

/**
 * Primary menu fallback: top product categories, until a menu is assigned.
 */
function hainute_nav_fallback() {
	$terms = get_terms(
		array(
			'taxonomy'   => 'product_cat',
			'hide_empty' => true,
			'orderby'    => 'count',
			'order'      => 'DESC',
			'number'     => 6,
		)
	);

	if ( is_wp_error( $terms ) || empty( $terms ) ) {
		return;
	}

	echo '<ul>';
	echo '<li><a href="' . esc_url( get_post_type_archive_link( 'product' ) ) . '">' . esc_html__( 'Toate produsele', 'hainute' ) . '</a></li>';
	foreach ( $terms as $term ) {
		echo '<li><a href="' . esc_url( get_term_link( $term ) ) . '">' . esc_html( $term->name ) . '</a></li>';
	}
	echo '</ul>';
}

/**
 * Linkurile din meniu salvate ca URL absolute pe domeniul de dezvoltare
 * (hainutero.local) → pe domeniul curent. Așa meniul merge pe localhost, pe
 * linkul public de test și după mutarea pe live, fără search-replace.
 */
add_filter(
	'nav_menu_link_attributes',
	function ( $atts ) {
		if ( ! empty( $atts['href'] ) && preg_match( '#^https?://hainutero\.local(/.*)?$#i', $atts['href'], $m ) ) {
			$atts['href'] = home_url( $m[1] ?? '/' );
		}
		return $atts;
	}
);
