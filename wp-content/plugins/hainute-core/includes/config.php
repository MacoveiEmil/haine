<?php
/**
 * Config access — API keys and secrets come from wp-config.php constants
 * (or environment variables), never hardcoded here.
 *
 * Expected constants, defined in wp-config.php:
 *   HAINUTE_2P_EMAIL      — 2Performant account email
 *   HAINUTE_2P_PASSWORD   — 2Performant account password
 *   HAINUTE_CJ_TOKEN      — CJ Affiliate personal access token
 *   HAINUTE_CJ_COMPANY_ID — CJ publisher company id
 *   HAINUTE_SYNC_SECRET   — shared secret for the sync REST endpoint
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Read a config value: constant first, then environment variable.
 *
 * @param string $key     Constant / env var name, e.g. 'HAINUTE_2P_EMAIL'.
 * @param mixed  $default Fallback when not configured.
 * @return mixed
 */
function hainute_config( $key, $default = null ) {
	if ( defined( $key ) ) {
		return constant( $key );
	}

	$env = getenv( $key );
	if ( false !== $env ) {
		return $env;
	}

	return $default;
}
