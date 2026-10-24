<?php
/**
 * Plugin Name: Hainute Core
 * Description: Data layer for the beestyle.ro aggregator — product CPT, taxonomies, per-store offers table, affiliate feed sync.
 * Version: 0.7.0
 * Author: beestyle.ro
 * Text Domain: hainute
 * Requires PHP: 7.4
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'HAINUTE_CORE_VERSION', '0.1.0' );
define( 'HAINUTE_CORE_DIR', plugin_dir_path( __FILE__ ) );
define( 'HAINUTE_CORE_URL', plugin_dir_url( __FILE__ ) );

require_once HAINUTE_CORE_DIR . 'includes/config.php';
require_once HAINUTE_CORE_DIR . 'includes/login-guard.php';
require_once HAINUTE_CORE_DIR . 'includes/seo-compat.php';
require_once HAINUTE_CORE_DIR . 'includes/install.php';
require_once HAINUTE_CORE_DIR . 'includes/post-types.php';
require_once HAINUTE_CORE_DIR . 'includes/stores.php';
require_once HAINUTE_CORE_DIR . 'includes/offers.php';
require_once HAINUTE_CORE_DIR . 'includes/engagement.php';
require_once HAINUTE_CORE_DIR . 'includes/descriptions.php';
require_once HAINUTE_CORE_DIR . 'includes/analytics.php';
require_once HAINUTE_CORE_DIR . 'includes/admin/manual-metabox.php';
require_once HAINUTE_CORE_DIR . 'includes/crosscheck.php';
require_once HAINUTE_CORE_DIR . 'includes/recheck.php';
require_once HAINUTE_CORE_DIR . 'includes/img-proxy.php';
require_once HAINUTE_CORE_DIR . 'includes/gender.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/matching.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/categories.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/importer.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/log.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/runner.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/sources/mock.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/sources/2performant.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/sources/profitshare.php';
require_once HAINUTE_CORE_DIR . 'includes/sync/sources/cj.php';
require_once HAINUTE_CORE_DIR . 'includes/rest.php';
require_once HAINUTE_CORE_DIR . 'includes/cli.php';

if ( is_admin() ) {
	require_once HAINUTE_CORE_DIR . 'includes/admin/offers-metabox.php';
	require_once HAINUTE_CORE_DIR . 'includes/admin/sync-page.php';
}

register_activation_hook( __FILE__, 'hainute_core_activate' );
