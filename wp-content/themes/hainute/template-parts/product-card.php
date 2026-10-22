<?php
/**
 * One product card in a listing grid.
 */

$product_id = get_the_ID();
$brand      = hainute_get_brand( $product_id );
$offers     = function_exists( 'hainute_get_offers' ) ? hainute_get_offers( $product_id ) : array();

// Magazinele și prețul din același rezumat ca pagina produsului (fără magazine
// ascunse, fără oferte externe expirate sau verificate ca alt produs, cu
// variantele de culoare cu stoc) → cardul nu poate spune altceva decât pagina.
$sum       = hainute_offer_summary( $product_id );
$stores_in = $sum['stores'];
$buyable   = $stores_in > 0;
$min_price = ( $buyable && $sum['best'] && 'out_of_stock' !== $sum['best']->stock_status ) ? (float) $sum['best']->price : null;
$n_sizes   = function_exists( 'hainute_resolve_sizes' ) ? (int) hainute_resolve_sizes( $product_id )['count'] : 0;
?>
<article <?php post_class( 'product-card' ); ?>>
	<a class="card-link" href="<?php the_permalink(); ?>">
		<div class="card-media">
			<?php // Fără badge-uri de reducere: site-ul arată mărimi disponibile, nu prețuri. ?>
			<?php $card_img = function_exists( 'hainute_product_image' ) ? hainute_product_image( $product_id, 'product-card' ) : ''; ?>
			<?php
			// Pe listări (arhivă/categorie/căutare) primele carduri sunt deasupra
			// pliului → încărcate imediat; primele 2 = LCP pe mobil (grilă 2 col).
			// Homepage + „Produse similare" rămân lazy (sunt sub pliu).
			$card_i     = isset( $GLOBALS['hainute_card_i'] ) ? (int) $GLOBALS['hainute_card_i'] : 0;
			$above_fold = ( is_post_type_archive( 'product' ) || is_tax() || is_search() ) && ! is_singular() && $card_i < 4;
			$img_extra  = $above_fold ? ( $card_i < 2 ? ' fetchpriority="high"' : '' ) : ' loading="lazy"';
			$GLOBALS['hainute_card_i'] = $card_i + 1;
			?>
			<?php if ( $card_img ) : ?>
				<img <?php echo hainute_img_attrs( $card_img, array( 320, 428, 540 ), '(max-width: 600px) 50vw, (max-width: 1024px) 33vw, 260px' ); // phpcs:ignore WordPress.Security.EscapeOutput -- escapat în helper ?> alt="<?php the_title_attribute(); ?>" decoding="async"<?php echo $img_extra; // phpcs:ignore ?>>
			<?php else : ?>
				<span class="card-noimg" aria-hidden="true"></span>
			<?php endif; ?>
		</div>

		<div class="card-body">
			<?php if ( $brand ) : ?>
				<span class="card-brand"><?php echo esc_html( $brand ); ?></span>
			<?php endif; ?>

			<h2 class="card-title"><?php the_title(); ?></h2>

			<?php if ( null !== $min_price ) : ?>
				<p class="card-price"><span><?php esc_html_e( 'de la', 'hainute' ); ?></span> <?php echo hainute_format_price( $min_price ); ?></p>
			<?php endif; ?>

			<?php if ( ! empty( $offers ) ) : ?>
				<p class="card-stores <?php echo $buyable ? '' : 'card-stores-out'; ?>">
					<?php
					if ( ! $buyable ) {
						esc_html_e( 'Momentan indisponibil', 'hainute' );
					} elseif ( $stores_in >= 2 ) {
						echo esc_html( 'în ' . hainute_ro_count( $stores_in, 'magazin', 'magazine' ) );
					} elseif ( $n_sizes > 0 ) {
						echo esc_html( hainute_ro_count( $n_sizes, 'mărime disponibilă', 'mărimi disponibile' ) );
					} else {
						esc_html_e( 'Disponibil', 'hainute' );
					}
					?>
				</p>
			<?php endif; ?>
		</div>
	</a>
</article>
