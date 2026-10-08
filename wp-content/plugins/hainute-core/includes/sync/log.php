<?php
/**
 * Minimal sync run log, stored as an option (last 20 runs).
 * Surfaced in the admin sync page so runs can be checked without touching code.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const HAINUTE_SYNC_LOG_OPTION = 'hainute_sync_log';
const HAINUTE_SYNC_LOG_MAX    = 20;

/**
 * Record one sync run.
 *
 * @param string $source  Human label, e.g. 'mock', '2performant', 'cj'.
 * @param array  $summary From hainute_import_items().
 */
function hainute_log_sync_run( $source, array $summary ) {
	$log = get_option( HAINUTE_SYNC_LOG_OPTION, array() );

	array_unshift(
		$log,
		array(
			'time'    => current_time( 'mysql' ),
			'source'  => $source,
			'created' => (int) $summary['created'],
			'matched' => (int) $summary['matched'],
			'offers'  => (int) $summary['offers'],
			'errors'  => (int) $summary['errors'],
			'notes'   => array_slice( (array) $summary['notes'], 0, 50 ),
		)
	);

	update_option( HAINUTE_SYNC_LOG_OPTION, array_slice( $log, 0, HAINUTE_SYNC_LOG_MAX ), false );
}

/**
 * @return array[] Latest runs, newest first.
 */
function hainute_get_sync_log() {
	return get_option( HAINUTE_SYNC_LOG_OPTION, array() );
}
