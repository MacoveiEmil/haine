<?php
/**
 * Product archive (/produse/).
 */

get_header();
?>

<div class="container">
	<header class="page-head">
		<h1><?php esc_html_e( 'Toate produsele', 'hainute' ); ?></h1>
		<p class="page-sub"><?php esc_html_e( 'Haine și încălțăminte pentru copii, cu disponibilitatea din magazinele partenere.', 'hainute' ); ?></p>
	</header>

	<?php get_template_part( 'template-parts/product-listing' ); ?>
</div>

<?php
get_footer();
