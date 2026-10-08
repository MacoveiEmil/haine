<?php
/**
 * Search results — product search uses the shared listing.
 */

get_header();
?>

<div class="container">
	<header class="page-head">
		<h1><?php printf( esc_html__( 'Rezultate pentru „%s”', 'hainute' ), esc_html( get_search_query() ) ); ?></h1>
	</header>

	<?php
	if ( 'product' === get_query_var( 'post_type' ) ) {
		get_template_part( 'template-parts/product-listing' );
	} elseif ( have_posts() ) {
		while ( have_posts() ) {
			the_post();
			?>
			<article <?php post_class(); ?>>
				<h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
				<?php the_excerpt(); ?>
			</article>
			<?php
		}
		the_posts_pagination(
			array(
				'prev_text'          => '&larr;<span class="screen-reader-text"> ' . esc_html__( 'Pagina anterioară', 'hainute' ) . '</span>',
				'next_text'          => '<span class="screen-reader-text">' . esc_html__( 'Pagina următoare', 'hainute' ) . ' </span>&rarr;',
				'screen_reader_text' => __( 'Paginare rezultate', 'hainute' ),
				'aria_label'         => __( 'Paginare rezultate', 'hainute' ),
			)
		);
	} else {
		echo '<p>' . esc_html__( 'Nu am găsit nimic.', 'hainute' ) . '</p>';
	}
	?>
</div>

<?php
get_footer();
