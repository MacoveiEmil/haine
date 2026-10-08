<?php
/**
 * Product CPT + taxonomies.
 *
 * Product meta keys (set by the sync jobs, not edited manually):
 *   _hainute_material   — string
 *   _hainute_sizes      — comma-separated list of available sizes
 *   _hainute_match_key  — normalized brand+name key used for cross-store matching
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_register_post_types() {

	register_post_type(
		'product',
		array(
			'labels'       => array(
				'name'          => __( 'Produse', 'hainute' ),
				'singular_name' => __( 'Produs', 'hainute' ),
				'add_new_item'  => __( 'Adaugă produs', 'hainute' ),
				'edit_item'     => __( 'Editează produsul', 'hainute' ),
			),
			'public'       => true,
			'has_archive'  => 'produse',
			'rewrite'      => array( 'slug' => 'produs', 'with_front' => false ),
			'menu_icon'    => 'dashicons-tag',
			'supports'     => array( 'title', 'editor', 'excerpt', 'thumbnail' ),
			'show_in_rest' => true,
		)
	);

	register_taxonomy(
		'product_cat',
		'product',
		array(
			'labels'       => array(
				'name'          => __( 'Categorii', 'hainute' ),
				'singular_name' => __( 'Categorie', 'hainute' ),
			),
			'hierarchical' => true,
			'rewrite'      => array( 'slug' => 'categorie', 'with_front' => false ),
			'show_in_rest' => true,
		)
	);

	register_taxonomy(
		'product_brand',
		'product',
		array(
			'labels'       => array(
				'name'          => __( 'Branduri', 'hainute' ),
				'singular_name' => __( 'Brand', 'hainute' ),
			),
			'hierarchical' => false,
			'rewrite'      => array( 'slug' => 'brand', 'with_front' => false ),
			'show_in_rest' => true,
		)
	);

	register_taxonomy(
		'product_gender',
		'product',
		array(
			'labels'       => array(
				'name'          => __( 'Gen', 'hainute' ),
				'singular_name' => __( 'Gen', 'hainute' ),
			),
			'hierarchical' => false,
			'rewrite'      => array( 'slug' => 'gen', 'with_front' => false ),
			'show_in_rest' => true,
		)
	);

	register_taxonomy(
		'product_age',
		'product',
		array(
			'labels'       => array(
				'name'          => __( 'Vârstă', 'hainute' ),
				'singular_name' => __( 'Vârstă', 'hainute' ),
			),
			'hierarchical' => false,
			'rewrite'      => array( 'slug' => 'varsta', 'with_front' => false ),
			'show_in_rest' => true,
		)
	);

	// Stores as a taxonomy: cheap "products available at store X" archives,
	// while offer details (price/stock/link) live in the custom offers table.
	register_taxonomy(
		'store',
		'product',
		array(
			'labels'       => array(
				'name'          => __( 'Magazine', 'hainute' ),
				'singular_name' => __( 'Magazin', 'hainute' ),
			),
			'hierarchical' => false,
			'rewrite'      => array( 'slug' => 'magazin', 'with_front' => false ),
			'show_in_rest' => true,
			'show_ui'      => true,
		)
	);
}
add_action( 'init', 'hainute_register_post_types' );
