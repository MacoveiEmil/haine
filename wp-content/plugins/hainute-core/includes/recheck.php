<?php
/**
 * Reverificare la cerere a disponibilității unui produs (butonul de pe pagina
 * produsului, vizibil doar pentru editori logați).
 *
 * Fluxul: butonul → POST /recheck (coadă) → tools/crawler/worker.js (Node +
 * Chrome, rulează permanent pe server) ia produsul din /recheck-queue, rulează
 * crawlerele pentru TOATE magazinele lui (proprii + cross) și raportează la
 * /recheck-done → pagina se reîncarcă singură cu datele noi.
 * WordPress nu poate rula Chrome, de aceea e nevoie de worker.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const HAINUTE_RECHECK_OPTION = 'hainute_recheck_queue';

/** Cine poate cere o reverificare: editorii logați. */
function hainute_recheck_can() {
	return current_user_can( 'edit_posts' );
}

/** Ce lanuri trebuie rulate pentru produs (după rețelele ofertelor lui). */
function hainute_recheck_lanes( $product_id ) {
	$lanes = array();
	foreach ( hainute_get_offers( $product_id ) as $o ) {
		$u = (string) $o->affiliate_url;
		if ( 'cj' === $o->network ) {
			$lanes[ false !== stripos( $u, 'sportisimo' ) ? 'sportisimo' : 'answear' ] = 1;
		} elseif ( 'profitshare' === $o->network ) {
			$lanes['fd'] = 1;
		} elseif ( '2performant' === $o->network ) {
			$lanes['vb'] = 1;
		} else {
			$lanes['cross'] = 1; // manual: / external: → manual.js
		}
	}
	return array_keys( $lanes );
}

add_action(
	'rest_api_init',
	function () {
		// Cerere din pagina produsului (cookie de login + nonce wp_rest).
		register_rest_route(
			'hainute/v1',
			'/recheck',
			array(
				'methods'             => 'POST',
				'permission_callback' => 'hainute_recheck_can',
				'callback'            => function ( WP_REST_Request $r ) {
					$id = (int) $r->get_param( 'id' );
					if ( 'product' !== get_post_type( $id ) ) {
						return new WP_Error( 'hainute_bad_id', 'Produs invalid', array( 'status' => 400 ) );
					}
					$q        = get_option( HAINUTE_RECHECK_OPTION, array() );
					$q        = is_array( $q ) ? $q : array();
					$q[ $id ] = time();
					update_option( HAINUTE_RECHECK_OPTION, $q, false );
					return rest_ensure_response( array( 'ok' => true, 'queued' => $q[ $id ] ) );
				},
			)
		);
		// Starea, pentru reîncărcarea automată a paginii.
		register_rest_route(
			'hainute/v1',
			'/recheck-status',
			array(
				'methods'             => 'GET',
				'permission_callback' => 'hainute_recheck_can',
				'callback'            => function ( WP_REST_Request $r ) {
					$id = (int) $r->get_param( 'id' );
					$q  = get_option( HAINUTE_RECHECK_OPTION, array() );
					return rest_ensure_response(
						array(
							'queued' => is_array( $q ) && isset( $q[ $id ] ),
							'done'   => (int) get_post_meta( $id, '_hainute_recheck_done', true ),
							'worker' => (int) get_option( 'hainute_worker_seen', 0 ),
						)
					);
				},
			)
		);
		// Pentru worker (secret): produsele cerute + lanurile de rulat.
		register_rest_route(
			'hainute/v1',
			'/recheck-queue',
			array(
				'methods'             => 'GET',
				'permission_callback' => 'hainute_rest_sync_permission',
				'callback'            => function () {
					update_option( 'hainute_worker_seen', time(), false );
					$q   = get_option( HAINUTE_RECHECK_OPTION, array() );
					$out = array();
					foreach ( ( is_array( $q ) ? $q : array() ) as $id => $ts ) {
						$out[] = array( 'id' => (int) $id, 'requested' => (int) $ts, 'lanes' => hainute_recheck_lanes( (int) $id ) );
					}
					return rest_ensure_response( array( 'ok' => true, 'queue' => $out ) );
				},
			)
		);
		register_rest_route(
			'hainute/v1',
			'/recheck-done',
			array(
				'methods'             => 'POST',
				'permission_callback' => 'hainute_rest_sync_permission',
				'callback'            => function ( WP_REST_Request $r ) {
					$id = (int) $r->get_param( 'id' );
					$q  = get_option( HAINUTE_RECHECK_OPTION, array() );
					if ( is_array( $q ) ) {
						unset( $q[ $id ] );
						update_option( HAINUTE_RECHECK_OPTION, $q, false );
					}
					update_post_meta( $id, '_hainute_recheck_done', time() );
					if ( function_exists( 'hainute_refresh_buyable' ) ) {
						hainute_refresh_buyable( $id );
					}
					return rest_ensure_response( array( 'ok' => true ) );
				},
			)
		);
	}
);
