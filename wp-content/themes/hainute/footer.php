</main>

<footer class="site-footer">
	<div class="container footer-inner">
		<div class="footer-brand">
			<span class="site-logo"><?php bloginfo( 'name' ); ?></span>
			<p><?php esc_html_e( 'Haine și încălțăminte pentru copii. Vezi unde sunt disponibile și cumperi direct de la magazinul partener.', 'hainute' ); ?></p>
		</div>

		<nav class="footer-nav" aria-label="<?php esc_attr_e( 'Meniu footer', 'hainute' ); ?>">
			<h3 class="footer-heading"><?php esc_html_e( 'Informații', 'hainute' ); ?></h3>
			<?php
			wp_nav_menu(
				array(
					'theme_location' => 'footer',
					'container'      => false,
					'fallback_cb'    => false,
				)
			);
			?>
		</nav>
	</div>

	<div class="container footer-note">
		<p class="footer-legal"><?php bloginfo( 'name' ); ?> <?php esc_html_e( 'este administrat de', 'hainute' ); ?> <strong>FAIR CLICK S.R.L.</strong> &middot; CUI 54682438 &middot; J2026031574004 &middot; <?php esc_html_e( 'București, Sector 1, Drumul Pădurea Neagră nr. 24, Corp A, Bl. OX01/1, Etaj 1, Ap. 6.', 'hainute' ); ?></p>
		<p>&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php bloginfo( 'name' ); ?> &middot; <?php esc_html_e( 'Linkurile către magazine sunt afiliate, fără niciun cost în plus pentru tine.', 'hainute' ); ?> <a href="<?php echo esc_url( home_url( '/declaratie-afiliere/' ) ); ?>"><?php esc_html_e( 'Detalii', 'hainute' ); ?></a></p>
	</div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
