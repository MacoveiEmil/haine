<?php
/**
 * WP-CLI command — the alternative cron entry point on hosts with wp-cli:
 *
 *   wp hainute sync
 *
 * (crontab: 0 * * * * cd /path/to/site && wp hainute sync --quiet)
 */

if ( ! defined( 'ABSPATH' ) || ! defined( 'WP_CLI' ) || ! WP_CLI ) {
	return;
}

WP_CLI::add_command(
	'hainute sync',
	function () {
		$results = hainute_run_sync();

		foreach ( $results as $source => $summary ) {
			WP_CLI::log(
				sprintf(
					'%s: %d produse noi, %d match-uri, %d oferte, %d erori%s',
					$source,
					$summary['created'],
					$summary['matched'],
					$summary['offers'],
					$summary['errors'],
					! empty( $summary['skipped_new'] ) ? sprintf( ', %d amânate', $summary['skipped_new'] ) : ''
				)
			);
		}

		WP_CLI::success( 'Sincronizare încheiată.' );
	}
);
