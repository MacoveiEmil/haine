<?php
/**
 * Single product — gallery left, info + store comparison right
 * (layout follows the reference mockup, with the affiliate offers
 * panel where a shop would have its add-to-cart column).
 */

get_header();
?>

<div class="container">
	<?php while ( have_posts() ) : the_post(); ?>
		<?php $product_id = get_the_ID(); ?>
		<?php if ( function_exists( 'hainute_track_view' ) ) { hainute_track_view( $product_id ); } ?>
		<?php hainute_the_product_schema( $product_id ); ?>

		<nav class="breadcrumbs" aria-label="breadcrumbs">
			<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Acasă', 'hainute' ); ?></a>
			<span>/</span>
			<a href="<?php echo esc_url( get_post_type_archive_link( 'product' ) ); ?>"><?php esc_html_e( 'Produse', 'hainute' ); ?></a>
			<?php
			// Breadcrumb pe tot lanțul: Gen › Grupă › Subcategorie (frunza + strămoșii ei).
			$cats = get_the_terms( $product_id, 'product_cat' );
			if ( $cats && ! is_wp_error( $cats ) ) {
				// Alege frunza (termenul cu cei mai mulți strămoși) ca să pornim de jos.
				$leaf = $cats[0];
				foreach ( $cats as $c ) {
					if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
						$leaf = $c;
					}
				}
				$chain     = array_reverse( get_ancestors( $leaf->term_id, 'product_cat' ) );
				$chain[]   = $leaf->term_id;
				foreach ( $chain as $tid ) {
					$term = get_term( $tid, 'product_cat' );
					if ( $term && ! is_wp_error( $term ) ) {
						echo '<span>/</span><a href="' . esc_url( get_term_link( $term ) ) . '">' . esc_html( $term->name ) . '</a>';
					}
				}
			}
			?>
		</nav>

		<article <?php post_class( 'product-single' ); ?>>
			<div class="product-layout">

				<div class="product-media">
					<?php hainute_the_gallery( $product_id ); ?>
				</div>

				<div class="product-info">
					<?php
					$brand_terms = get_the_terms( $product_id, 'product_brand' );
					$brand_term  = ( $brand_terms && ! is_wp_error( $brand_terms ) ) ? $brand_terms[0] : null;
					?>
					<?php if ( $brand_term ) : ?>
						<p class="product-brand"><a href="<?php echo esc_url( get_term_link( $brand_term ) ); ?>"><?php echo esc_html( $brand_term->name ); ?></a></p>
					<?php endif; ?>

					<h1 class="product-title"><?php the_title(); ?></h1>
					<?php hainute_the_product_intro( $product_id ); ?>

					<?php hainute_the_price_block( $product_id ); ?>

					<?php hainute_the_social_proof( $product_id ); ?>

					<?php hainute_the_recheck_box( $product_id ); ?>

					<?php hainute_the_shop_matrix( $product_id ); ?>
				</div>

			</div>

			<div class="product-details">
				<div class="product-description">
					<h2 class="section-label"><?php esc_html_e( 'Descriere', 'hainute' ); ?></h2>
					<?php the_content(); ?>
				</div>

				<?php hainute_the_specs( $product_id ); ?>
			</div>
		</article>
		<?php hainute_the_sticky_cta( $product_id ); ?>

		<?php
		// Produse similare — relevanță în trepte: aceeași categorie + ACELAȘI BRAND
		// întâi (ex. bluză Kenzo → alte topuri Kenzo), apoi categorie+gen, categorie,
		// și brand ca fallback (când categoria e „Diverse"/prea largă). Exclude
		// „Diverse" din potrivirea pe categorie ca să nu apară articole nepotrivite.
		$cats     = get_the_terms( $product_id, 'product_cat' );
		$cat_ids  = array();
		if ( $cats && ! is_wp_error( $cats ) ) {
			foreach ( $cats as $c ) {
				if ( 0 !== strcasecmp( $c->name, 'Diverse' ) ) {
					$cat_ids[] = (int) $c->term_id;
				}
			}
		}
		$brands     = get_the_terms( $product_id, 'product_brand' );
		$brand_ids  = ( $brands && ! is_wp_error( $brands ) ) ? wp_list_pluck( $brands, 'term_id' ) : array();
		$genders    = get_the_terms( $product_id, 'product_gender' );
		$gender_ids = ( $genders && ! is_wp_error( $genders ) ) ? wp_list_pluck( $genders, 'term_id' ) : array();

		$tiers = array();
		if ( $cat_ids && $brand_ids ) {
			$tiers[] = array( 'relation' => 'AND', array( 'taxonomy' => 'product_cat', 'field' => 'term_id', 'terms' => $cat_ids ), array( 'taxonomy' => 'product_brand', 'field' => 'term_id', 'terms' => $brand_ids ) );
		}
		if ( $cat_ids && $gender_ids ) {
			$tiers[] = array( 'relation' => 'AND', array( 'taxonomy' => 'product_cat', 'field' => 'term_id', 'terms' => $cat_ids ), array( 'taxonomy' => 'product_gender', 'field' => 'term_id', 'terms' => $gender_ids ) );
		}
		if ( $cat_ids ) {
			$tiers[] = array( array( 'taxonomy' => 'product_cat', 'field' => 'term_id', 'terms' => $cat_ids ) );
		}
		if ( $brand_ids ) {
			$tiers[] = array( array( 'taxonomy' => 'product_brand', 'field' => 'term_id', 'terms' => $brand_ids ) );
		}

		$related_ids = array();
		foreach ( $tiers as $tq ) {
			if ( count( $related_ids ) >= 12 ) {
				break;
			}
			$q = new WP_Query( array( 'post_type' => 'product', 'post_status' => 'publish', 'posts_per_page' => 12, 'fields' => 'ids', 'orderby' => 'rand', 'post__not_in' => array_merge( array( $product_id ), $related_ids ), 'tax_query' => $tq ) );
			$related_ids = array_values( array_unique( array_merge( $related_ids, $q->posts ) ) );
		}
		$related_ids = array_slice( $related_ids, 0, 12 );

		if ( $related_ids ) {
			$related = new WP_Query( array( 'post_type' => 'product', 'post__in' => $related_ids, 'orderby' => 'post__in', 'posts_per_page' => 12 ) );

			if ( $related->have_posts() ) {
				echo '<section class="related-products carousel" data-carousel>';
				echo '<div class="carousel-head">';
				echo '<h2>' . esc_html__( 'Produse similare', 'hainute' ) . '</h2>';
				echo '<div class="carousel-nav">';
				echo '<button type="button" class="carousel-btn carousel-prev" aria-label="' . esc_attr__( 'Înapoi', 'hainute' ) . '">&larr;</button>';
				echo '<button type="button" class="carousel-btn carousel-next" aria-label="' . esc_attr__( 'Înainte', 'hainute' ) . '">&rarr;</button>';
				echo '</div>';
				echo '</div>';
				echo '<div class="carousel-track" data-carousel-track>';
				while ( $related->have_posts() ) {
					$related->the_post();
					echo '<div class="carousel-item">';
					get_template_part( 'template-parts/product-card' );
					echo '</div>';
				}
				echo '</div>';
				echo '</section>';
				wp_reset_postdata();
			}
		}
		?>

	<?php endwhile; ?>
</div>

<?php
get_footer();
