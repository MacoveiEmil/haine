<?php
/**
 * Read-only metabox on the product edit screen showing the offers
 * stored in the custom table. Data is managed by the sync jobs,
 * so there is nothing to edit here — this is for visibility/debugging.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_register_offers_metabox() {
	add_meta_box(
		'hainute-offers',
		__( 'Oferte per magazin', 'hainute' ),
		'hainute_render_offers_metabox',
		'product',
		'normal',
		'default'
	);
}
add_action( 'add_meta_boxes', 'hainute_register_offers_metabox' );

function hainute_render_offers_metabox( $post ) {
	$offers = hainute_get_offers( $post->ID );

	if ( empty( $offers ) ) {
		echo '<p>' . esc_html__( 'Nicio ofertă încă. Ofertele apar automat după sincronizarea cu feed-urile de afiliere.', 'hainute' ) . '</p>';
		return;
	}

	$labels = array(
		HAINUTE_STOCK_IN  => __( 'Disponibil', 'hainute' ),
		HAINUTE_STOCK_LOW => __( 'Stoc critic', 'hainute' ),
		HAINUTE_STOCK_OUT => __( 'Indisponibil', 'hainute' ),
	);

	echo '<table class="widefat striped"><thead><tr>';
	echo '<th>' . esc_html__( 'Magazin', 'hainute' ) . '</th>';
	echo '<th>' . esc_html__( 'Preț', 'hainute' ) . '</th>';
	echo '<th>' . esc_html__( 'Stoc', 'hainute' ) . '</th>';
	echo '<th>' . esc_html__( 'Rețea', 'hainute' ) . '</th>';
	echo '<th>' . esc_html__( 'Actualizat', 'hainute' ) . '</th>';
	echo '<th></th>';
	echo '</tr></thead><tbody>';

	foreach ( $offers as $offer ) {
		$store_name = $offer->store ? $offer->store->name : '#' . $offer->store_id;
		$status     = isset( $labels[ $offer->stock_status ] ) ? $labels[ $offer->stock_status ] : $offer->stock_status;

		echo '<tr>';
		echo '<td>' . esc_html( $store_name ) . '</td>';
		echo '<td>' . esc_html( number_format_i18n( (float) $offer->price, 2 ) . ' ' . $offer->currency ) . '</td>';
		echo '<td>' . esc_html( $status ) . '</td>';
		echo '<td>' . esc_html( $offer->network ) . '</td>';
		echo '<td>' . esc_html( $offer->updated_at ) . '</td>';
		echo '<td><a href="' . esc_url( $offer->affiliate_url ) . '" target="_blank" rel="noopener">' . esc_html__( 'Link afiliat', 'hainute' ) . '</a></td>';
		echo '</tr>';
	}

	echo '</tbody></table>';
}
