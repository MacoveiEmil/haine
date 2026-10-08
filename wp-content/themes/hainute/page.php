<?php
/**
 * Pagină statică (Despre Noi, Termeni, Contact etc.).
 */

get_header();
?>

<div class="container">
	<?php while ( have_posts() ) : the_post(); ?>
		<nav class="breadcrumbs" aria-label="breadcrumbs">
			<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Acasă', 'hainute' ); ?></a>
			<span>/</span>
			<span><?php the_title(); ?></span>
		</nav>

		<article <?php post_class( 'static-page' ); ?>>
			<h1 class="page-title"><?php the_title(); ?></h1>
			<div class="page-body">
				<?php the_content(); ?>
			</div>
		</article>
	<?php endwhile; ?>
</div>

<?php
get_footer();
