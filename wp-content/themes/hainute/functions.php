<?php
/**
 * Hainute theme bootstrap — each concern lives in its own file under inc/.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'HAINUTE_THEME_VERSION', '0.2.0' );
define( 'HAINUTE_THEME_DIR', get_template_directory() );
define( 'HAINUTE_THEME_URL', get_template_directory_uri() );

require_once HAINUTE_THEME_DIR . '/inc/setup.php';
require_once HAINUTE_THEME_DIR . '/inc/enqueue.php';
require_once HAINUTE_THEME_DIR . '/inc/template-tags.php';
require_once HAINUTE_THEME_DIR . '/inc/seo.php';
require_once HAINUTE_THEME_DIR . '/inc/filters.php';
require_once HAINUTE_THEME_DIR . '/inc/how-it-works.php';
require_once HAINUTE_THEME_DIR . '/inc/category-seo.php';
