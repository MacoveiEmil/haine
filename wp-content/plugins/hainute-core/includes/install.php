<?php
/**
 * Activation: create the custom offers table and flush rewrite rules.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'HAINUTE_DB_VERSION', '1' );

function hainute_offers_table_name() {
	global $wpdb;
	return $wpdb->prefix . 'hainute_offers';
}

function hainute_core_activate() {
	hainute_core_create_tables();

	// CPT/taxonomies must exist before flushing so their rules are included.
	hainute_register_post_types();
	flush_rewrite_rules();

	update_option( 'hainute_db_version', HAINUTE_DB_VERSION );
}

function hainute_core_create_tables() {
	global $wpdb;

	require_once ABSPATH . 'wp-admin/includes/upgrade.php';

	$table   = hainute_offers_table_name();
	$charset = $wpdb->get_charset_collate();

	$sql = "CREATE TABLE {$table} (
		id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
		product_id BIGINT UNSIGNED NOT NULL,
		store_id BIGINT UNSIGNED NOT NULL,
		network VARCHAR(32) NOT NULL DEFAULT '',
		external_id VARCHAR(191) NOT NULL DEFAULT '',
		price DECIMAL(10,2) NOT NULL DEFAULT 0,
		old_price DECIMAL(10,2) NULL DEFAULT NULL,
		currency CHAR(3) NOT NULL DEFAULT 'RON',
		stock_status VARCHAR(20) NOT NULL DEFAULT 'in_stock',
		stock_qty INT NULL DEFAULT NULL,
		affiliate_url TEXT NOT NULL,
		updated_at DATETIME NOT NULL,
		PRIMARY KEY  (id),
		UNIQUE KEY product_store (product_id, store_id),
		KEY store_id (store_id),
		KEY stock_status (stock_status),
		KEY network_external (network, external_id)
	) {$charset};";

	dbDelta( $sql );
}

/**
 * Upgrade path for later schema changes (compares stored vs current version).
 */
function hainute_core_maybe_upgrade() {
	if ( get_option( 'hainute_db_version' ) !== HAINUTE_DB_VERSION ) {
		hainute_core_create_tables();
		update_option( 'hainute_db_version', HAINUTE_DB_VERSION );
	}
}
add_action( 'admin_init', 'hainute_core_maybe_upgrade' );
