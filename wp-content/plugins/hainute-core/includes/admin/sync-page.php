<?php
/**
 * Admin page: "Sincronizare" under the Products menu.
 * Manual run button (needed on Local, where there is no real cron)
 * + the log of recent runs.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function hainute_register_sync_page() {
	add_submenu_page(
		'edit.php?post_type=product',
		__( 'Sincronizare feed-uri', 'hainute' ),
		__( 'Sincronizare', 'hainute' ),
		'manage_options',
		'hainute-sync',
		'hainute_render_sync_page'
	);
}
add_action( 'admin_menu', 'hainute_register_sync_page' );

function hainute_handle_sync_action() {
	if ( ! current_user_can( 'manage_options' ) ) {
		wp_die( esc_html__( 'Nu ai permisiunea necesară.', 'hainute' ) );
	}

	check_admin_referer( 'hainute_run_sync' );

	hainute_run_sync();

	wp_safe_redirect( add_query_arg( 'hainute_synced', '1', wp_get_referer() ) );
	exit;
}
add_action( 'admin_post_hainute_run_sync', 'hainute_handle_sync_action' );

/**
 * "Test 2Performant" button: connectivity + raw payload dump into the log,
 * without importing anything.
 */
function hainute_handle_test_2p_action() {
	if ( ! current_user_can( 'manage_options' ) ) {
		wp_die( esc_html__( 'Nu ai permisiunea necesară.', 'hainute' ) );
	}

	check_admin_referer( 'hainute_test_2p' );

	$result = hainute_2p_run_diagnostic();

	hainute_log_sync_run(
		'2performant-test',
		array(
			'created' => 0,
			'matched' => 0,
			'offers'  => 0,
			'errors'  => $result['ok'] ? 0 : 1,
			'notes'   => $result['notes'],
		)
	);

	wp_safe_redirect( add_query_arg( 'hainute_synced', '1', wp_get_referer() ) );
	exit;
}
add_action( 'admin_post_hainute_test_2p', 'hainute_handle_test_2p_action' );

function hainute_render_sync_page() {
	$log = hainute_get_sync_log();
	?>
	<div class="wrap">
		<h1><?php esc_html_e( 'Sincronizare feed-uri', 'hainute' ); ?></h1>

		<?php if ( isset( $_GET['hainute_synced'] ) ) : ?>
			<div class="notice notice-success is-dismissible">
				<p><?php esc_html_e( 'Sincronizarea a rulat. Vezi rezultatul în tabelul de mai jos.', 'hainute' ); ?></p>
			</div>
		<?php endif; ?>

		<h2><?php esc_html_e( 'Surse active', 'hainute' ); ?></h2>
		<ul>
			<?php
			$has_2p_creds = hainute_config( 'HAINUTE_2P_EMAIL' ) && hainute_config( 'HAINUTE_2P_PASSWORD' );
			foreach ( array_keys( hainute_get_sources() ) as $source_name ) {
				echo '<li><code>' . esc_html( $source_name ) . '</code></li>';
			}
			if ( ! $has_2p_creds ) {
				echo '<li style="color:#b35c00;">' . esc_html__( '2Performant inactiv — definește HAINUTE_2P_EMAIL și HAINUTE_2P_PASSWORD în wp-config.php.', 'hainute' ) . '</li>';
			}
			if ( ! hainute_config( 'HAINUTE_SYNC_SECRET' ) ) {
				echo '<li style="color:#b35c00;">' . esc_html__( 'Endpoint-ul de cron e dezactivat — definește HAINUTE_SYNC_SECRET în wp-config.php.', 'hainute' ) . '</li>';
			}
			?>
		</ul>

		<p><?php esc_html_e( 'În producție, sincronizarea rulează automat, o dată pe oră, prin cron real care apelează endpoint-ul REST. Butoanele de mai jos sunt pentru rulare manuală și diagnoză.', 'hainute' ); ?></p>

		<div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
			<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
				<input type="hidden" name="action" value="hainute_run_sync">
				<?php wp_nonce_field( 'hainute_run_sync' ); ?>
				<?php submit_button( __( 'Rulează sincronizarea acum', 'hainute' ), 'primary', 'submit', false ); ?>
			</form>

			<?php if ( $has_2p_creds ) : ?>
				<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
					<input type="hidden" name="action" value="hainute_test_2p">
					<?php wp_nonce_field( 'hainute_test_2p' ); ?>
					<?php submit_button( __( 'Testează conexiunea 2Performant', 'hainute' ), 'secondary', 'submit', false ); ?>
				</form>
			<?php endif; ?>
		</div>

		<h2><?php esc_html_e( 'Ultimele rulări', 'hainute' ); ?></h2>

		<?php if ( empty( $log ) ) : ?>
			<p><?php esc_html_e( 'Nicio rulare încă.', 'hainute' ); ?></p>
		<?php else : ?>
			<table class="widefat striped">
				<thead>
					<tr>
						<th><?php esc_html_e( 'Data', 'hainute' ); ?></th>
						<th><?php esc_html_e( 'Sursă', 'hainute' ); ?></th>
						<th><?php esc_html_e( 'Produse noi', 'hainute' ); ?></th>
						<th><?php esc_html_e( 'Match-uri cross-store', 'hainute' ); ?></th>
						<th><?php esc_html_e( 'Oferte actualizate', 'hainute' ); ?></th>
						<th><?php esc_html_e( 'Erori', 'hainute' ); ?></th>
						<th><?php esc_html_e( 'Detalii', 'hainute' ); ?></th>
					</tr>
				</thead>
				<tbody>
					<?php foreach ( $log as $run ) : ?>
						<tr>
							<td><?php echo esc_html( $run['time'] ); ?></td>
							<td><?php echo esc_html( $run['source'] ); ?></td>
							<td><?php echo esc_html( $run['created'] ); ?></td>
							<td><?php echo esc_html( $run['matched'] ); ?></td>
							<td><?php echo esc_html( $run['offers'] ); ?></td>
							<td><?php echo esc_html( $run['errors'] ); ?></td>
							<td>
								<?php if ( ! empty( $run['notes'] ) ) : ?>
									<details>
										<summary><?php echo esc_html( count( $run['notes'] ) ); ?> <?php esc_html_e( 'note', 'hainute' ); ?></summary>
										<ul>
											<?php foreach ( $run['notes'] as $note ) : ?>
												<li><?php echo esc_html( $note ); ?></li>
											<?php endforeach; ?>
										</ul>
									</details>
								<?php endif; ?>
							</td>
						</tr>
					<?php endforeach; ?>
				</tbody>
			</table>
		<?php endif; ?>
	</div>
	<?php
}
