<?php
/**
 * Homepage: hero + categories + latest products + how it works.
 */

get_header();
?>

<section class="hero">
	<div class="container hero-inner">
		<div class="hero-copy">
			<h1><?php esc_html_e( 'Găsește mărimea potrivită pentru copilul tău, direct la magazinul care o are.', 'hainute' ); ?></h1>
			<p><?php
			printf(
				/* translators: 1: number of stores, 2: hours */
				esc_html__( 'Haine și încălțăminte pentru copii: alegi mărimea și vezi pe loc în care dintre cele %1$d magazine e pe stoc. Verificăm stocul pe mărimi la fiecare %2$d ore.', 'hainute' ),
				(int) count( hainute_active_store_names() ),
				(int) hainute_refresh_hours()
			);
			?></p>
			<div class="hero-actions">
				<a class="btn btn-primary" href="<?php echo esc_url( get_post_type_archive_link( 'product' ) ); ?>"><?php esc_html_e( 'Vezi produsele', 'hainute' ); ?></a>
			</div>
		</div>
	</div>
</section>

<section class="home-section">
	<div class="container">
		<h2 class="home-title"><?php esc_html_e( 'Categorii', 'hainute' ); ?></h2>
		<?php hainute_the_home_categories(); ?>
	</div>
</section>

<?php
// Produsele găsite în mai multe magazine (cu stoc), cele mai noi primele;
// _hainute_store_count = magazinele cu stoc, ca pe pagina produsului.
$latest = new WP_Query(
	array(
		'post_type'      => 'product',
		'posts_per_page' => 8,
		'meta_query'     => array(
			'hainute_magazine' => array(
				'key'     => '_hainute_store_count',
				'value'   => 2,
				'type'    => 'NUMERIC',
				'compare' => '>=',
			),
		),
		'orderby'        => 'date', // nu după numărul de magazine: ar ieși 8 produse ale aceluiași brand
	)
);
// Prea puține (ex. după un crawl ratat): completăm cu cele mai noi produse cu stoc.
if ( $latest->post_count < 8 ) {
	$fill   = get_posts(
		array(
			'post_type'      => 'product',
			'posts_per_page' => 8 - $latest->post_count,
			'post__not_in'   => wp_list_pluck( $latest->posts, 'ID' ),
			'meta_key'       => '_hainute_buyable', // phpcs:ignore WordPress.DB.SlowDBQuery
			'meta_value'     => 1, // phpcs:ignore WordPress.DB.SlowDBQuery
		)
	);
	$latest->posts      = array_merge( $latest->posts, $fill );
	$latest->post_count = count( $latest->posts );
}

if ( $latest->have_posts() ) :
	?>
	<section class="home-section">
		<div class="container">
			<div class="home-title-row">
				<h2 class="home-title"><?php esc_html_e( 'Pe stoc în mai multe magazine', 'hainute' ); ?></h2>
				<a class="link-more" href="<?php echo esc_url( add_query_arg( 'cross', 1, get_post_type_archive_link( 'product' ) ) ); ?>"><?php esc_html_e( 'Vezi toate', 'hainute' ); ?> &rarr;</a>
			</div>
			<div class="product-grid">
				<?php
				while ( $latest->have_posts() ) {
					$latest->the_post();
					get_template_part( 'template-parts/product-card' );
				}
				wp_reset_postdata();
				?>
			</div>
		</div>
	</section>
<?php endif; ?>

<section class="home-section how-it-works">
	<div class="container">
		<h2 class="home-title"><?php esc_html_e( 'Cum funcționează', 'hainute' ); ?></h2>
		<div class="steps-grid">
			<div class="step">
				<span class="step-num">1</span>
				<h3><?php esc_html_e( 'Găsești produsul', 'hainute' ); ?></h3>
				<p><?php esc_html_e( 'Cauți sau filtrezi după categorie, gen, mărime și preț. O singură dată, nu în cinci magazine.', 'hainute' ); ?></p>
			</div>
			<div class="step">
				<span class="step-num">2</span>
				<h3><?php esc_html_e( 'Alegi magazinul', 'hainute' ); ?></h3>
				<p><?php esc_html_e( 'Vezi dintr-o privire în ce magazine e mărimea ta pe stoc.', 'hainute' ); ?></p>
			</div>
			<div class="step">
				<span class="step-num">3</span>
				<h3><?php esc_html_e( 'Cumperi de la magazin', 'hainute' ); ?></h3>
				<p><?php esc_html_e( 'Comanzi direct pe site-ul magazinului ales. Noi doar te ducem la raftul potrivit.', 'hainute' ); ?></p>
			</div>
		</div>
	</div>
</section>

<section class="home-section">
	<div class="container">
		<h2 class="home-title"><?php esc_html_e( 'Branduri populare', 'hainute' ); ?></h2>
		<?php hainute_the_home_brands(); ?>
		<?php hainute_the_home_text(); ?>
	</div>
</section>

<?php
// Doar magazinele cu oferte active (cele din „Cum funcționează"), câte unul per
// nume afișat (ex. „Sportisimo Europe" de la CJ = Sportisimo.ro).
$stores = hainute_store_terms_active();
if ( $stores ) :
	?>
	<section class="home-section stores-strip">
		<div class="container">
			<h2 class="home-title"><?php esc_html_e( 'Magazine partenere', 'hainute' ); ?></h2>
			<ul class="stores-list">
				<?php foreach ( $stores as $store ) : ?>
					<li><a href="<?php echo esc_url( get_term_link( $store ) ); ?>"><?php echo esc_html( hainute_store_display_name( $store->name ) ); ?></a></li>
				<?php endforeach; ?>
			</ul>
		</div>
	</section>
<?php endif; ?>

<?php
get_footer();
