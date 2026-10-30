<?php
/**
 * Pagina „Branduri" (/branduri/): vezi inc/brands-page.php.
 */

get_header();

$brands = hainute_all_brands();

$by_letter = array();
foreach ( $brands as $b ) {
	$by_letter[ hainute_brand_letter( $b['name'] ) ][] = $b;
}
ksort( $by_letter );
if ( isset( $by_letter['#'] ) ) { // simbolurile la sfârșit
	$sym = $by_letter['#'];
	unset( $by_letter['#'] );
	$by_letter['#'] = $sym;
}

$popular = $brands;
usort( $popular, function ( $a, $b ) { return $b['count'] <=> $a['count']; } );
$popular = array_slice( $popular, 0, 12 );
?>

<div class="container">
	<nav class="breadcrumbs" aria-label="breadcrumbs">
		<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Acasă', 'hainute' ); ?></a>
		<span>/</span><span class="current" aria-current="page"><?php esc_html_e( 'Branduri', 'hainute' ); ?></span>
	</nav>

	<header class="page-head">
		<h1><?php echo esc_html( hainute_brands_page_title() ); ?></h1>
		<p class="page-sub"><?php echo esc_html( sprintf( __( '%d de branduri. Alege unul și vezi mărimile disponibile în magazine.', 'hainute' ), count( $brands ) ) ); ?></p>
	</header>

	<?php if ( $popular ) : ?>
		<section class="brands-popular" aria-labelledby="brands-popular-h">
			<h2 id="brands-popular-h"><?php esc_html_e( 'Cele mai multe produse', 'hainute' ); ?></h2>
			<div class="cat-chips">
				<?php foreach ( $popular as $b ) : ?>
					<a class="cat-chip" href="<?php echo esc_url( $b['url'] ); ?>"><?php echo esc_html( $b['name'] ); ?> <span class="brand-count"><?php echo (int) $b['count']; ?></span></a>
				<?php endforeach; ?>
			</div>
		</section>
	<?php endif; ?>

	<nav class="brands-letters" aria-label="<?php esc_attr_e( 'Brandurile după literă', 'hainute' ); ?>">
		<?php foreach ( array_keys( $by_letter ) as $l ) : ?>
			<a href="#litera-<?php echo esc_attr( '#' === $l ? 'alte' : strtolower( $l ) ); ?>"><?php echo esc_html( $l ); ?></a>
		<?php endforeach; ?>
	</nav>

	<?php foreach ( $by_letter as $l => $list ) : ?>
		<section class="brands-group" id="litera-<?php echo esc_attr( '#' === $l ? 'alte' : strtolower( $l ) ); ?>">
			<h2><?php echo esc_html( $l ); ?></h2>
			<ul class="brands-list">
				<?php foreach ( $list as $b ) : ?>
					<li><a href="<?php echo esc_url( $b['url'] ); ?>"><?php echo esc_html( $b['name'] ); ?> <span class="brand-count"><?php echo (int) $b['count']; ?></span></a></li>
				<?php endforeach; ?>
			</ul>
		</section>
	<?php endforeach; ?>
</div>

<?php
get_footer();
