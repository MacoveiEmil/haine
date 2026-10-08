<?php
/**
 * Shared listing body: filter bar + grid + pagination.
 * Used by archive-product.php, taxonomy pages and product search.
 */
?>

<?php hainute_the_filter_bar(); ?>

<?php if ( have_posts() ) : ?>
	<div class="product-grid">
		<?php while ( have_posts() ) : the_post(); ?>
			<?php get_template_part( 'template-parts/product-card' ); ?>
		<?php endwhile; ?>
	</div>

	<?php
	the_posts_pagination(
		array(
			'prev_text'          => '&larr;<span class="screen-reader-text"> ' . esc_html__( 'Pagina anterioară', 'hainute' ) . '</span>',
			'next_text'          => '<span class="screen-reader-text">' . esc_html__( 'Pagina următoare', 'hainute' ) . ' </span>&rarr;',
			'screen_reader_text' => __( 'Paginare produse', 'hainute' ),
			'aria_label'         => __( 'Paginare produse', 'hainute' ),
			'before_page_number' => '<span class="screen-reader-text">' . esc_html__( 'Pagina', 'hainute' ) . ' </span>',
		)
	);
	?>
<?php else : ?>
	<div class="empty-state">
		<p><?php esc_html_e( 'Niciun produs nu se potrivește filtrelor alese.', 'hainute' ); ?></p>
		<a class="btn btn-ghost" href="<?php echo esc_url( get_post_type_archive_link( 'product' ) ); ?>"><?php esc_html_e( 'Vezi toate produsele', 'hainute' ); ?></a>
	</div>
<?php endif; ?>
