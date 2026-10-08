<?php
/**
 * Store helpers — a store is a term in the 'store' taxonomy, with term meta:
 *   network     — '2performant' | 'cj'
 *   program_id  — affiliate program/advertiser id inside that network
 *   logo_url    — store logo
 *   website     — store homepage URL
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Create or update a store term.
 *
 * @param string $name Store display name, e.g. 'Modivo'.
 * @param array  $meta { network, program_id, logo_url, website } — all optional.
 * @return int|WP_Error Term ID.
 */
function hainute_upsert_store( $name, array $meta = array() ) {
	$term = get_term_by( 'name', $name, 'store' );

	if ( $term ) {
		$term_id = (int) $term->term_id;
	} else {
		$result = wp_insert_term( $name, 'store' );
		if ( is_wp_error( $result ) ) {
			return $result;
		}
		$term_id = (int) $result['term_id'];
	}

	foreach ( array( 'network', 'program_id', 'logo_url', 'website' ) as $key ) {
		if ( isset( $meta[ $key ] ) ) {
			update_term_meta( $term_id, $key, $meta[ $key ] );
		}
	}

	return $term_id;
}

/**
* Numele afișat al magazinului: unele rețele dau numele firmei, nu al site-ului
* („Sportisimo Europe" la CJ). Termenul rămâne neschimbat (importerul îl caută
* după nume), doar afișarea folosește numele magazinului.
*/
function hainute_store_display_name( $name ) {
	$map = apply_filters( 'hainute_store_display_names', array( 'Sportisimo Europe' => 'Sportisimo.ro' ) );
	return $map[ $name ] ?? $name;
}

/**
* Get a store term with its meta as a flat object.
 *
 * @param int $term_id Store term ID.
 * @return object|null { term_id, name, slug, network, program_id, logo_url, website }
 */
function hainute_get_store( $term_id ) {
	$term = get_term( $term_id, 'store' );
	if ( ! $term || is_wp_error( $term ) ) {
		return null;
	}

	return (object) array(
		'term_id'    => (int) $term->term_id,
		'name'       => hainute_store_display_name( $term->name ),
		'slug'       => $term->slug,
		'network'    => get_term_meta( $term->term_id, 'network', true ),
		'program_id' => get_term_meta( $term->term_id, 'program_id', true ),
		'logo_url'   => get_term_meta( $term->term_id, 'logo_url', true ),
		'website'    => get_term_meta( $term->term_id, 'website', true ),
	);
}

/**
 * Find a store term id by network + program id (used by sync jobs).
 *
 * @return int|null
 */
function hainute_find_store_by_program( $network, $program_id ) {
	$terms = get_terms(
		array(
			'taxonomy'   => 'store',
			'hide_empty' => false,
			'meta_query' => array(
				array( 'key' => 'network', 'value' => $network ),
				array( 'key' => 'program_id', 'value' => $program_id ),
			),
		)
	);

	if ( is_wp_error( $terms ) || empty( $terms ) ) {
		return null;
	}

	return (int) $terms[0]->term_id;
}
