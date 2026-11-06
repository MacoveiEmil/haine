<?php
/**
 * Pagină de campanie: Black Friday (adresa /black-friday/, aceeași în fiecare an).
 *
 * Conținutul stă aici, în cod, ca să fie versionat. De actualizat în fiecare an / la fiecare campanie nouă:
 * $bf_date, $bf_checked și lista $campaigns (doar ce afișează magazinul în momentul verificării, fără date inventate).
 * Poziționare: titlu și H1 fără preț/ofertă/reducere; campaniile sunt atribuite magazinelor.
 */

// ---- De actualizat ----
$bf_date    = '2026-11-27';              // vinerea Black Friday
$bf_checked = '6 noiembrie 2026';        // data ultimei verificări a campaniilor
$bf_year    = '2026';
$campaigns  = array(
	array(
		'store' => 'Answear.ro',
		'tag'   => 'Campanie dedicată copiilor',
		'text'  => 'Secțiunea „Magic Black Friday pentru copii" e deja activă. Magazinul anunță reduceri de până la 50%, iar la comenzi de minimum 499 RON o reducere suplimentară în coș. Unele produse au reducerea aplicată doar în coș, iar regulamentul lor listează excluderile.',
		'url'   => 'https://answear.ro/s/black-friday-kids',
		'cta'   => 'Vezi campania pentru copii',
	),
	array(
		'store' => 'FashionDays.ro',
		'tag'   => 'Campanie pe tot site-ul',
		'text'  => 'FashionDays anunță Black Friday cu peste un milion de produse. Campania nu e dedicată copiilor, așa că intră în secțiunea pentru copii și filtrează după mărime.',
		'url'   => 'https://www.fashiondays.ro/',
		'cta'   => 'Mergi la FashionDays',
	),
	array(
		'store' => 'Sportisimo.ro',
		'tag'   => 'Pagină de Black Friday',
		'text'  => 'Sportisimo are o pagină proprie de Black Friday, iar la „Tot pentru copii" găsești încălțăminte și îmbrăcăminte sport pentru cei mici. Detaliile campaniei sunt pe pagina lor.',
		'url'   => 'https://www.sportisimo.ro/black-friday/',
		'cta'   => 'Vezi pagina de Black Friday',
	),
);
// -----------------------

/** Link către un magazin: afiliat unde există rețea, mereu prin redirecționarea site-ului. */
function hainute_bf_link( $url ) {
	$aff = function_exists( 'hainute_cross_affiliate_url' ) ? hainute_cross_affiliate_url( $url ) : $url;
	return function_exists( 'hainute_out_url' ) ? hainute_out_url( $aff ) : $aff;
}

$faq = array(
	array( 'Când e Black Friday în ' . $bf_year . '?', 'Vinerea Black Friday este pe 27 noiembrie ' . $bf_year . ', cu weekendul de Black Friday pe 28 și 29 noiembrie. Unele magazine încep campaniile mai devreme și le țin o săptămână întreagă.' ),
	array( 'Cum aleg mărimea potrivită pentru copil?', 'Măsoară înălțimea copilului fără pantofi și compar-o cu tabelul de pe această pagină, apoi verifică tabelul de mărimi al magazinului, pentru că diferă de la brand la brand. Pe beestyle.ro vezi pe fiecare produs ce mărimi au magazinele pe stoc.' ),
	array( 'Pot returna produsele cumpărate în campanie?', 'La comenzile online ai, conform legii, dreptul de a returna produsele în 14 zile. Magazinele pot avea condiții proprii pentru produsele din campanii și pot exclude anumite categorii, deci citește regulamentul campaniei înainte de comandă.' ),
	array( 'De ce nu vedeți prețurile aici?', 'beestyle.ro nu compară prețuri. Te ajutăm să găsești mărimea potrivită, la magazinul care o are pe stoc, iar prețul și condițiile campaniei le vezi direct la magazin.' ),
	array( 'Cum câștigă beestyle.ro bani?', 'Unele linkuri către magazine sunt afiliate: dacă cumperi prin ele, primim un mic comision, fără cost suplimentar pentru tine. Asta nu schimbă ordinea în care îți arătăm magazinele.' ),
);

$sizes = array(
	'56' => '0-2 luni', '62' => '2-3 luni', '68' => '4-6 luni', '74' => '6-9 luni', '80' => '9-12 luni', '86' => '12-18 luni',
	'92' => '18-24 luni', '98' => '2-3 ani', '104' => '3-4 ani', '110' => '4-5 ani', '116' => '5-6 ani', '122' => '6-7 ani',
	'128' => '7-8 ani', '134' => '8-9 ani', '140' => '9-10 ani', '146' => '10-11 ani', '152' => '11-12 ani', '158' => '12-13 ani', '164' => '13-14 ani',
);

$brand_chips = array( 'geox' => 'Geox', 'tommy-hilfiger' => 'Tommy Hilfiger', 'reima' => 'Reima', 'next' => 'Next', 'en-fant' => 'En Fant' );

get_header();
$shop_url = get_post_type_archive_link( 'product' );
?>

<div class="bf-lp">

	<section class="bf-hero">
		<div class="container bf-hero-inner">
			<span class="bf-kicker">Black Friday <?php echo esc_html( $bf_year ); ?></span>
			<h1><?php echo esc_html( 'Black Friday ' . $bf_year . ': găsește mărimea potrivită pentru copilul tău' ); ?></h1>
			<p class="bf-sub">În campanii mărimile mijlocii se termină primele. Vezi ce campanii au magazinele partenere și află, înainte să comanzi, la ce magazin e pe stoc mărimea copilului.</p>
			<div class="bf-actions">
				<a class="btn btn-primary bf-btn" href="#campanii">Vezi campaniile</a>
				<a class="btn bf-btn bf-btn-light" href="<?php echo esc_url( $shop_url ); ?>">Alege mărimea copilului</a>
			</div>
			<div class="bf-count" id="bf-count" data-date="<?php echo esc_attr( $bf_date ); ?>" hidden>
				<span class="bf-count-num" id="bf-count-num">0</span>
				<span class="bf-count-label" id="bf-count-label">zile până la Black Friday</span>
			</div>
			<ul class="bf-chips">
				<li>Verificat pe <?php echo esc_html( $bf_checked ); ?></li>
				<li>Stoc pe mărimi, nu doar pe produs</li>
				<li>Mergi direct la magazin</li>
			</ul>
		</div>
	</section>

	<section class="bf-section" id="campanii">
		<div class="container">
			<h2 class="bf-title">Campanii găsite la magazinele partenere</h2>
			<p class="bf-lead">Am citit paginile magazinelor pe <?php echo esc_html( $bf_checked ); ?>. Procentele, condițiile și datele sunt ale magazinelor și se pot schimba, așa că citește regulamentul campaniei înainte de comandă.</p>
			<div class="bf-cards">
				<?php foreach ( $campaigns as $c ) : ?>
					<article class="bf-card">
						<span class="bf-card-tag"><?php echo esc_html( $c['tag'] ); ?></span>
						<h3><?php echo esc_html( $c['store'] ); ?></h3>
						<p><?php echo esc_html( $c['text'] ); ?></p>
						<a class="btn btn-primary bf-card-cta" href="<?php echo esc_url( hainute_bf_link( $c['url'] ) ); ?>" target="_blank" rel="sponsored nofollow noopener"><?php echo esc_html( $c['cta'] ); ?> &rarr;</a>
					</article>
				<?php endforeach; ?>
			</div>
			<p class="bf-note">Unele linkuri sunt afiliate: dacă cumperi prin ele, primim un mic comision, fără cost suplimentar pentru tine.</p>
		</div>
	</section>

	<section class="bf-section bf-alt">
		<div class="container">
			<h2 class="bf-title">Cum eviți retururile de mărime</h2>
			<div class="bf-steps">
				<div class="bf-step"><span class="bf-num">1</span><h3>Măsoară acum</h3><p>Înălțimea copilului, fără pantofi, o iei înainte de campanie, nu în ziua ei, când se termină stocul.</p></div>
				<div class="bf-step"><span class="bf-num">2</span><h3>Verifică stocul pe mărime</h3><p>Pe beestyle.ro alegi mărimea și vezi ce magazine o au pe stoc, ca să nu descoperi la coș că a dispărut.</p></div>
				<div class="bf-step"><span class="bf-num">3</span><h3>Comandă devreme</h3><p>Mărimile mijlocii se epuizează primele. La hainele de iarnă ia în calcul o mărime peste, pentru un strat gros dedesubt.</p></div>
			</div>
			<p class="bf-center"><a class="btn btn-primary bf-btn" href="<?php echo esc_url( $shop_url ); ?>">Caută după mărime</a></p>
		</div>
	</section>

	<section class="bf-section">
		<div class="container">
			<h2 class="bf-title">Ce mărime să cauți</h2>
			<p class="bf-lead">Tabel orientativ, după înălțime. Copiii cresc în ritmuri diferite, deci înălțimea măsurată contează mai mult decât vârsta.</p>
			<ul class="bf-sizes">
				<?php foreach ( $sizes as $cm => $age ) : ?>
					<li><strong><?php echo esc_html( $cm ); ?> cm</strong><span><?php echo esc_html( $age ); ?></span></li>
				<?php endforeach; ?>
			</ul>
			<div class="bf-tips">
				<p><strong>Încălțăminte:</strong> măsoară talpa în centimetri și lasă aproximativ un centimetru în plus.</p>
				<p><strong>Branduri diferite, mărimi diferite:</strong> verifică tabelul magazinului înainte de comandă.</p>
			</div>
		</div>
	</section>

	<?php
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
			'orderby'        => 'rand',
		)
	);
	if ( $latest->have_posts() ) :
		?>
		<section class="bf-section bf-alt">
			<div class="container">
				<div class="home-title-row">
					<h2 class="bf-title">Produse găsite în mai multe magazine</h2>
					<a class="link-more" href="<?php echo esc_url( add_query_arg( 'cross', 1, $shop_url ) ); ?>">Vezi toate &rarr;</a>
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

	<section class="bf-section">
		<div class="container">
			<h2 class="bf-title">Începe de la brandul copilului tău</h2>
			<div class="bf-brands">
				<?php
				foreach ( $brand_chips as $slug => $label ) {
					$t = get_term_by( 'slug', $slug, 'product_brand' );
					if ( $t && ! is_wp_error( $t ) ) {
						echo '<a class="bf-brand" href="' . esc_url( get_term_link( $t ) ) . '">' . esc_html( $label ) . '</a>';
					}
				}
				?>
				<a class="bf-brand bf-brand-all" href="<?php echo esc_url( home_url( '/branduri/' ) ); ?>">Toate brandurile &rarr;</a>
			</div>
		</div>
	</section>

	<section class="bf-section bf-alt">
		<div class="container bf-faq-wrap">
			<h2 class="bf-title">Întrebări frecvente</h2>
			<?php foreach ( $faq as $q ) : ?>
				<details class="bf-faq">
					<summary><?php echo esc_html( $q[0] ); ?></summary>
					<p><?php echo esc_html( $q[1] ); ?></p>
				</details>
			<?php endforeach; ?>
		</div>
	</section>

	<section class="bf-final">
		<div class="container">
			<h2>Nu pierde mărimea copilului</h2>
			<p>Alege mărimea și vezi pe loc la ce magazin e pe stoc.</p>
			<a class="btn btn-primary bf-btn" href="<?php echo esc_url( $shop_url ); ?>">Vezi produsele pe stoc</a>
		</div>
	</section>

</div>

<script type="application/ld+json"><?php
echo wp_json_encode(
	array(
		'@context'   => 'https://schema.org',
		'@type'      => 'FAQPage',
		'mainEntity' => array_map(
			function ( $q ) {
				return array(
					'@type'          => 'Question',
					'name'           => $q[0],
					'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $q[1] ),
				);
			},
			$faq
		),
	),
	JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);
?></script>
<script>
(function () {
	var box = document.getElementById('bf-count');
	if (!box) { return; }
	var d = new Date(box.getAttribute('data-date') + 'T00:00:00');
	var days = Math.ceil((d - new Date()) / 86400000);
	if (isNaN(days) || days < 0) { return; }
	var num = document.getElementById('bf-count-num'), lab = document.getElementById('bf-count-label');
	if (days === 0) { num.textContent = 'Azi'; lab.textContent = 'e Black Friday'; }
	else { num.textContent = days; lab.textContent = days === 1 ? 'zi până la Black Friday' : 'zile până la Black Friday'; }
	box.hidden = false;
})();
</script>

<?php
get_footer();
