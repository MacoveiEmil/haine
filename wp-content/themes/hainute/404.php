<?php
/**
 * 404: mesaj clar + drumuri utile (căutare, categorii), nu o pagină goală.
 */

get_header();
?>

<div class="container page-404">
	<header class="page-head">
		<h1><?php esc_html_e( 'Pagina nu a fost găsită', 'hainute' ); ?></h1>
		<p><?php esc_html_e( 'Produsul sau pagina nu mai există. Caută altceva sau alege o categorie:', 'hainute' ); ?></p>
	</header>
	<?php get_search_form(); ?>
	<ul class="stores-list">
		<?php foreach ( get_terms( array( 'taxonomy' => 'product_cat', 'parent' => 0, 'hide_empty' => true ) ) as $t ) : ?>
			<li><a href="<?php echo esc_url( get_term_link( $t ) ); ?>"><?php echo esc_html( $t->name ); ?></a></li>
		<?php endforeach; ?>
		<li><a href="<?php echo esc_url( get_post_type_archive_link( 'product' ) ); ?>"><?php esc_html_e( 'Toate produsele', 'hainute' ); ?></a></li>
	</ul>
</div>

<?php
get_footer();
