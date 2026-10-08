<?php
/**
 * All product taxonomies (categorie, brand, gen, vârstă, magazin).
 */

get_header();

$term = get_queried_object();

// Pe categorii: lanțul de strămoși (Fete › Îmbrăcăminte) pentru breadcrumb și
// un H1 neambiguu — „Geci & jachete" există și la Fete, și la Băieți, și la Bebe.
$chain = is_tax( 'product_cat' ) ? array_reverse( get_ancestors( $term->term_id, 'product_cat' ) ) : array();
$top   = $chain ? get_term( $chain[0], 'product_cat' ) : null;
$h1    = $term->name;
if ( $top && ! is_wp_error( $top ) ) {
	$h1 = sprintf( __( '%1$s pentru %2$s', 'hainute' ), $term->name, mb_strtolower( $top->name ) );
} elseif ( is_tax( 'product_cat' ) ) {
	$h1 = sprintf( __( 'Haine și încălțăminte pentru %s', 'hainute' ), mb_strtolower( $term->name ) );
}
?>

<div class="container">
	<?php if ( is_tax( 'product_cat' ) ) : ?>
		<nav class="breadcrumbs" aria-label="breadcrumbs">
			<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Acasă', 'hainute' ); ?></a>
			<span>/</span>
			<a href="<?php echo esc_url( get_post_type_archive_link( 'product' ) ); ?>"><?php esc_html_e( 'Produse', 'hainute' ); ?></a>
			<?php foreach ( $chain as $tid ) : ?>
				<?php $t = get_term( $tid, 'product_cat' ); ?>
				<span>/</span><a href="<?php echo esc_url( get_term_link( $t ) ); ?>"><?php echo esc_html( $t->name ); ?></a>
			<?php endforeach; ?>
			<span>/</span><span class="current" aria-current="page"><?php echo esc_html( $term->name ); ?></span>
		</nav>
	<?php endif; ?>

	<header class="page-head">
		<h1><?php echo esc_html( $h1 ); ?></h1>
		<?php if ( ! empty( $term->description ) ) : ?>
			<p class="page-sub"><?php echo esc_html( $term->description ); ?></p>
		<?php endif; ?>
	</header>

	<?php get_template_part( 'template-parts/product-listing' ); ?>
</div>

<?php
get_footer();
