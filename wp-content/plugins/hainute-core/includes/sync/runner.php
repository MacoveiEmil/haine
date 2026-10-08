<?php
/**
 * Sync orchestration — decides which sources are active and runs them all.
 * Called from: the admin button, the REST endpoint (server cron) and WP-CLI.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Active sources: name => callable returning { items: array[], notes: string[] }.
 *
 * 2Performant activates itself when credentials are configured. The mock
 * source stays active only while no real source exists (or when forced
 * via HAINUTE_USE_MOCK in wp-config.php).
 */
function hainute_get_sources() {
	$sources = array();

	if ( hainute_config( 'HAINUTE_2P_EMAIL' ) && hainute_config( 'HAINUTE_2P_PASSWORD' ) ) {
		$sources['2performant'] = 'hainute_2p_fetch_items';
	}

	if ( hainute_config( 'HAINUTE_PS_USER' ) && hainute_config( 'HAINUTE_PS_KEY' ) ) {
		$sources['profitshare'] = 'hainute_profitshare_fetch_items';
	}

	if ( hainute_config( 'HAINUTE_CJ_TOKEN' ) && hainute_config( 'HAINUTE_CJ_COMPANY_ID' ) ) {
		$sources['cj'] = 'hainute_cj_fetch_items';
	}

	if ( empty( $sources ) || hainute_config( 'HAINUTE_USE_MOCK' ) ) {
		$sources['mock'] = 'hainute_mock_fetch_items';
	}

	return apply_filters( 'hainute_sync_sources', $sources );
}

/**
 * Run a full sync across all active sources. Each source is imported and
 * logged separately, so a failing source never hides the others.
 *
 * @return array name => summary.
 */
function hainute_run_sync( $only = '' ) {
	// Image sideloading makes big first imports slow — allow long runs.
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 0 );
	}
	ignore_user_abort( true );

	// Cap on newly created products per run: keeps each hourly run short;
	// the next runs pick up where this one left off. Override with the
	// HAINUTE_MAX_NEW_PRODUCTS constant (e.g. a high value for the initial seed).
	$default_max = (int) hainute_config( 'HAINUTE_MAX_NEW_PRODUCTS', 150 );
	$max_new     = (int) apply_filters( 'hainute_max_new_products', $default_max );

	$results = array();

	$sources = hainute_get_sources();
	if ( '' !== $only ) {
		$sources = isset( $sources[ $only ] ) ? array( $only => $sources[ $only ] ) : array();
	}

	foreach ( $sources as $name => $callback ) {
		try {
			$feed    = call_user_func( $callback );
			$summary = hainute_import_items( $feed['items'], $max_new );
			$summary['notes'] = array_merge( $feed['notes'], $summary['notes'] );
		} catch ( \Throwable $e ) {
			$summary = array(
				'created' => 0,
				'matched' => 0,
				'offers'  => 0,
				'errors'  => 1,
				'notes'   => array( 'Sursa a eșuat: ' . $e->getMessage() . ' @ ' . basename( $e->getFile() ) . ':' . $e->getLine() ),
			);
		}

		hainute_log_sync_run( $name, $summary );
		$results[ $name ] = $summary;
	}

	return $results;
}
