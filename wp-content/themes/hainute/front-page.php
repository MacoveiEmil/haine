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

<?php
$categories = get_terms(
	array(
		'taxonomy'   => 'product_cat',
		'hide_empty' => true,
		'orderby'    => 'count',
		'order'      => 'DESC',
		'number'     => 6,
	)
);

if ( ! is_wp_error( $categories ) && $categories ) :
	?>
	<section class="home-section">
		<div class="container">
			<h2 class="home-title"><?php esc_html_e( 'Categorii populare', 'hainute' ); ?></h2>
			<div class="category-grid">
				<?php foreach ( $categories as $term ) : ?>
					<a class="category-card" href="<?php echo esc_url( get_term_link( $term ) ); ?>">
						<span class="category-name"><?php echo esc_html( hainute_term_path_label( $term ) ); ?></span>
						<span class="category-count"><?php echo esc_html( hainute_ro_count( $term->count, 'produs', 'produse' ) ); ?></span>
					</a>
				<?php endforeach; ?>
			</div>
		</div>
	</section>
<?php endif; ?>

<?php
$latest = new WP_Query(
	array(
		'post_type'      => 'product',
		'posts_per_page' => 8,
	)
);

if ( $latest->have_posts() ) :
	?>
	<section class="home-section">
		<div class="container">
			<div class="home-title-row">
				<h2 class="home-title"><?php esc_html_e( 'Produse noi', 'hainute' ); ?></h2>
				<a class="link-more" href="<?php echo esc_url( get_post_type_archive_link( 'product' ) ); ?>"><?php esc_html_e( 'Vezi toate', 'hainute' ); ?> &rarr;</a>
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
