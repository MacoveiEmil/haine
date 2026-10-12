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

/**
 * Genul produsului din categoria de top (Fete › … / Băieți › …): feed-urile rar
 * dau genul separat, dar categoria îl are mereu. Fără asta filtrul „gen" și
 * linkurile „Vezi … fete în mărimea X" găseau doar câteva produse.
 * Rulează la orice schimbare de categorii (import, editare manuală).
 */
function hainute_sync_gender_from_categories( $object_id, $terms = array(), $tt_ids = array(), $taxonomy = 'product_cat' ) {
	if ( 'product_cat' !== $taxonomy || 'product' !== get_post_type( $object_id ) ) {
		return;
	}
	$genders = array();
	foreach ( wp_get_object_terms( $object_id, 'product_cat' ) as $cat ) {
		$anc = get_ancestors( $cat->term_id, 'product_cat' );
		$top = $anc ? get_term( end( $anc ), 'product_cat' ) : $cat;
		if ( $top && ! is_wp_error( $top ) && in_array( $top->slug, array( 'fete', 'baieti' ), true ) ) {
			$genders[ $top->slug ] = $top->name;
		} elseif ( $top && ! is_wp_error( $top ) && 'unisex' === $top->slug ) {
			$genders['fete']   = 'Fete'; // unisex: apare la ambele genuri
			$genders['baieti'] = 'Băieți';
		}
	}
	foreach ( $genders as $slug => $name ) {
		if ( ! term_exists( $slug, 'product_gender' ) ) {
			wp_insert_term( $name, 'product_gender', array( 'slug' => $slug ) );
		}
	}
	if ( $genders ) {
		wp_set_object_terms( $object_id, array_keys( $genders ), 'product_gender', true );
	}
}
add_action( 'set_object_terms', 'hainute_sync_gender_from_categories', 10, 4 );
