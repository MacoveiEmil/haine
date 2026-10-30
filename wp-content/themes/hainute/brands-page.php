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

	<div class="brands-search">
		<label class="screen-reader-text" for="brands-q"><?php esc_html_e( 'Caută un brand', 'hainute' ); ?></label>
		<input type="search" id="brands-q" placeholder="<?php esc_attr_e( 'Caută un brand…', 'hainute' ); ?>" autocomplete="off">
	</div>

	<?php if ( $popular ) : ?>
		<section class="brands-popular" id="brands-popular" aria-labelledby="brands-popular-h">
			<h2 id="brands-popular-h"><?php esc_html_e( 'Cele mai căutate', 'hainute' ); ?></h2>
			<div class="brand-cards">
				<?php foreach ( $popular as $b ) : hainute_brand_card( $b ); endforeach; ?>
			</div>
		</section>
	<?php endif; ?>

	<nav class="brands-letters" id="brands-letters" aria-label="<?php esc_attr_e( 'Brandurile după literă', 'hainute' ); ?>">
		<?php foreach ( array_keys( $by_letter ) as $l ) : ?>
			<a href="#litera-<?php echo esc_attr( '#' === $l ? 'alte' : strtolower( $l ) ); ?>"><?php echo esc_html( $l ); ?></a>
		<?php endforeach; ?>
	</nav>

	<?php foreach ( $by_letter as $l => $list ) : ?>
		<section class="brands-group" id="litera-<?php echo esc_attr( '#' === $l ? 'alte' : strtolower( $l ) ); ?>">
			<h2><?php echo esc_html( $l ); ?></h2>
			<div class="brand-cards">
				<?php foreach ( $list as $b ) : hainute_brand_card( $b ); endforeach; ?>
			</div>
		</section>
	<?php endforeach; ?>

	<p class="brands-empty" id="brands-empty" hidden><?php esc_html_e( 'Niciun brand cu acest nume.', 'hainute' ); ?></p>
</div>

<script>
(function () {
	var q = document.getElementById('brands-q');
	if (!q) { return; }
	var norm = function (t) { return t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); };
	var cards = document.querySelectorAll('.brands-group .brand-card');
	var groups = document.querySelectorAll('.brands-group');
	var hide = [document.getElementById('brands-popular'), document.getElementById('brands-letters')];
	q.addEventListener('input', function () {
		var v = norm(q.value.trim()), shown = 0;
		cards.forEach(function (c) {
			var ok = !v || norm(c.getAttribute('data-name')).indexOf(v) !== -1;
			c.hidden = !ok;
			if (ok) { shown++; }
		});
		groups.forEach(function (g) { g.hidden = !g.querySelector('.brand-card:not([hidden])'); });
		hide.forEach(function (e) { if (e) { e.hidden = !!v; } });
		document.getElementById('brands-empty').hidden = shown > 0;
	});
})();
</script>

<?php
get_footer();
