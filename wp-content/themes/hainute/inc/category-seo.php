<?php
/**
 * Text și linkuri interne pe homepage și pe paginile de categorie.
 *
 * Textele stau în data/categorii-seo.json (le poate edita oricine, prin git), cu
 * locuri care se completează din date, ca să nu se învechească:
 *   {produse}   numărul de produse din categorie („138 de produse”)
 *   {magazine}  numărul de magazine verificate („12 magazine”)
 *   {ore}       la câte ore se verifică stocul
 *   {branduri}  primele 3 branduri din categorie, cu link („Geox, Primigi și Biomecanics”)
 * Pe paginile de fete/băieți, numerele includ și produsele unisex (apar și ele în listă).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Textele din data/categorii-seo.json (cheie = slugul categoriei sau „acasa”). */
function hainute_seo_texts() {
	static $texts = null;
	if ( null === $texts ) {
		$f     = HAINUTE_THEME_DIR . '/data/categorii-seo.json';
		$texts = file_exists( $f ) ? (array) json_decode( (string) file_get_contents( $f ), true ) : array(); // phpcs:ignore WordPress.WP.AlternativeFunctions
	}
	return $texts;
}

/** Categoria corespondentă de la Unisex (pentru fete/băieți), sau null. */
function hainute_cat_unisex_twin( $term ) {
	if ( ! function_exists( 'hainute_cat_path_names' ) ) {
		return null;
	}
	list( $top, $names ) = hainute_cat_path_names( $term->term_id );
	if ( ! in_array( $top, array( 'fete', 'baieti' ), true ) ) {
		return null;
	}
	$eq = $names ? hainute_cat_by_path( 'unisex', $names ) : get_term_by( 'slug', 'unisex', 'product_cat' );
	return ( $eq && ! is_wp_error( $eq ) ) ? $eq : null;
}

/**
 * Numărul de produse și brandurile unei categorii, exact ca în listarea ei
 * (fete/băieți includ unisex). Cache 12 ore.
 * @return array{count:int,brands:array<int,array{name:string,url:string,count:int}>}
 */
function hainute_cat_stats( $term ) {
	$key   = 'hnt_catstats_' . $term->term_id;
	$cache = get_transient( $key );
	if ( is_array( $cache ) ) {
		return $cache;
	}
	$terms = array( (int) $term->term_id );
	$twin  = hainute_cat_unisex_twin( $term );
	if ( $twin ) {
		$terms[] = (int) $twin->term_id;
	}
	$ids    = get_posts( array( 'post_type' => 'product', 'post_status' => 'publish', 'numberposts' => -1, 'fields' => 'ids',
		'tax_query' => array( array( 'taxonomy' => 'product_cat', 'terms' => $terms, 'include_children' => true ) ) ) );
	$brands = array();
	update_object_term_cache( $ids, 'product' );
	foreach ( $ids as $id ) {
		$bt = get_the_terms( $id, 'product_brand' );
		if ( $bt && ! is_wp_error( $bt ) ) {
			$b = $bt[0];
			if ( ! isset( $brands[ $b->term_id ] ) ) {
				$brands[ $b->term_id ] = array( 'name' => html_entity_decode( $b->name ), 'url' => get_term_link( $b ), 'count' => 0 );
			}
			$brands[ $b->term_id ]['count']++;
		}
	}
	usort( $brands, function ( $a, $b ) { return $b['count'] - $a['count']; } );
	$out = array( 'count' => count( $ids ), 'brands' => $brands );
	set_transient( $key, $out, 12 * HOUR_IN_SECONDS );
	return $out;
}

/** Categoriile cu mai puțin de 3 produse sunt pagini subțiri: noindex și în afara sitemap-ului. */
function hainute_cat_is_thin( $term ) {
	return hainute_cat_stats( $term )['count'] < 3;
}

/** „Geox, Primigi și Biomecanics”, cu linkuri. */
function hainute_brand_links_text( array $brands, $n = 3 ) {
	$links = array();
	foreach ( array_slice( $brands, 0, $n ) as $b ) {
		$links[] = '<a href="' . esc_url( $b['url'] ) . '">' . esc_html( $b['name'] ) . '</a>';
	}
	if ( count( $links ) < 2 ) {
		return implode( '', $links );
	}
	$last = array_pop( $links );
	return implode( ', ', $links ) . ' și ' . $last;
}

/** Înlocuiește {produse}, {magazine}, {ore}, {branduri} în textul unei categorii. */
function hainute_seo_fill( $html, $count, array $brands ) {
	return strtr(
		(string) $html,
		array(
			'{produse}'  => hainute_ro_count( $count, 'produs', 'produse' ),
			'{magazine}' => hainute_ro_count( count( hainute_active_store_names() ), 'magazin', 'magazine' ),
			'{ore}'      => (string) hainute_refresh_hours(),
			'{branduri}' => hainute_brand_links_text( $brands ),
		)
	);
}

/** Subcategoriile cu produse ale unei categorii. @return WP_Term[] */
function hainute_cat_children( $term ) {
	$kids = get_terms( array( 'taxonomy' => 'product_cat', 'parent' => $term->term_id, 'hide_empty' => false, 'orderby' => 'name' ) );
	return array_values( array_filter( is_wp_error( $kids ) ? array() : $kids, function ( $t ) { return hainute_cat_stats( $t )['count'] > 0; } ) );
}

/** Aceeași categorie la celelalte genuri (Geci & jachete: fete, băieți, bebe, unisex). @return WP_Term[] */
function hainute_cat_other_genders( $term ) {
	if ( ! function_exists( 'hainute_cat_path_names' ) ) {
		return array();
	}
	list( $top, $names ) = hainute_cat_path_names( $term->term_id );
	$out = array();
	foreach ( array( 'fete', 'baieti', 'bebe', 'unisex' ) as $g ) {
		if ( $g === $top ) {
			continue;
		}
		$t = $names ? hainute_cat_by_path( $g, $names ) : get_term_by( 'slug', $g, 'product_cat' );
		if ( $t && ! is_wp_error( $t ) && hainute_cat_stats( $t )['count'] > 0 ) {
			$out[] = $t;
		}
	}
	return $out;
}

/** Eticheta unei categorii pentru link: „Geci & jachete pentru băieți”, „Adidași unisex”. */
function hainute_cat_link_label( $term ) {
	$anc = get_ancestors( $term->term_id, 'product_cat' );
	if ( ! $anc ) {
		return 'unisex' === $term->slug ? __( 'Unisex', 'hainute' ) : html_entity_decode( $term->name );
	}
	$top = get_term( end( $anc ), 'product_cat' );
	$who = array( 'fete' => 'pentru fete', 'baieti' => 'pentru băieți', 'bebe' => 'pentru bebeluși', 'unisex' => 'unisex' );
	return html_entity_decode( $term->name ) . ' ' . ( $who[ $top->slug ] ?? mb_strtolower( $top->name ) );
}

function hainute_cat_chip( $term, $label = null ) {
	return '<a class="cat-chip" href="' . esc_url( get_term_link( $term ) ) . '">' . esc_html( $label ?? html_entity_decode( $term->name ) ) . '</a>';
}

/** Sub H1: intro + linkuri spre subcategorii (sau spre categoriile-soră și celelalte genuri). */
function hainute_the_cat_top( $term ) {
	$texts = hainute_seo_texts();
	$stats = hainute_cat_stats( $term );
	if ( ! empty( $texts[ $term->slug ]['intro'] ) && ! is_paged() ) {
		echo '<p class="page-sub">' . wp_kses_post( hainute_seo_fill( $texts[ $term->slug ]['intro'], $stats['count'], $stats['brands'] ) ) . '</p>';
	}
	$kids = hainute_cat_children( $term );
	if ( $kids ) {
		echo '<nav class="cat-chips" aria-label="' . esc_attr__( 'Subcategorii', 'hainute' ) . '">';
		foreach ( $kids as $k ) {
			$grand = hainute_cat_children( $k );
			if ( $grand ) { // Fete: direct spre Adidași, Geci & jachete…, nu doar spre „Încălțăminte”
				foreach ( $grand as $g ) {
					echo hainute_cat_chip( $g ); // phpcs:ignore WordPress.Security.EscapeOutput
				}
			} else {
				echo hainute_cat_chip( $k ); // phpcs:ignore WordPress.Security.EscapeOutput
			}
		}
		echo '</nav>';
		return;
	}
	$parent = $term->parent ? get_term( $term->parent, 'product_cat' ) : null;
	$sibs   = $parent ? array_filter( hainute_cat_children( $parent ), function ( $t ) use ( $term ) { return (int) $t->term_id !== (int) $term->term_id; } ) : array();
	if ( $sibs ) {
		echo '<nav class="cat-chips" aria-label="' . esc_attr__( 'Categorii apropiate', 'hainute' ) . '">';
		foreach ( $sibs as $s ) {
			echo hainute_cat_chip( $s ); // phpcs:ignore WordPress.Security.EscapeOutput
		}
		echo '</nav>';
	}
}

/** Sub produse (doar pe pagina 1): textul categoriei, brandurile și aceeași categorie la alte genuri. */
function hainute_the_cat_bottom( $term ) {
	if ( is_paged() ) {
		return;
	}
	$texts = hainute_seo_texts();
	$stats = hainute_cat_stats( $term );
	$t     = $texts[ $term->slug ] ?? array();
	echo '<section class="cat-seo">';
	if ( ! empty( $t['text'] ) ) {
		if ( ! empty( $t['titlu'] ) ) {
			echo '<h2>' . esc_html( $t['titlu'] ) . '</h2>';
		}
		echo wp_kses_post( wpautop( hainute_seo_fill( $t['text'], $stats['count'], $stats['brands'] ) ) );
	}
	if ( count( $stats['brands'] ) > 1 ) {
		echo '<h3>' . esc_html( sprintf( __( 'Branduri în %s', 'hainute' ), mb_strtolower( hainute_cat_link_label( $term ) ) ) ) . '</h3><p class="cat-links">';
		foreach ( array_slice( $stats['brands'], 0, 12 ) as $b ) {
			echo '<a class="cat-chip" href="' . esc_url( $b['url'] ) . '">' . esc_html( $b['name'] ) . '</a>';
		}
		echo '</p>';
	}
	$other = hainute_cat_other_genders( $term );
	if ( $other ) {
		echo '<h3>' . esc_html( sprintf( __( '%s și pentru alte vârste sau genuri', 'hainute' ), html_entity_decode( $term->parent ? $term->name : __( 'Haine și încălțăminte', 'hainute' ) ) ) ) . '</h3><p class="cat-links">';
		foreach ( $other as $o ) {
			echo hainute_cat_chip( $o, hainute_cat_link_label( $o ) ); // phpcs:ignore WordPress.Security.EscapeOutput
		}
		echo '</p>';
	}
	echo '</section>';
}

/** Homepage: toate categoriile cu produse, pe genuri, cu subcategoriile lor. */
function hainute_the_home_categories() {
	$titles = array( 'fete' => __( 'Fete', 'hainute' ), 'baieti' => __( 'Băieți', 'hainute' ), 'bebe' => __( 'Bebeluși', 'hainute' ), 'unisex' => __( 'Unisex', 'hainute' ) );
	echo '<div class="home-cats">';
	foreach ( $titles as $slug => $title ) {
		$top = get_term_by( 'slug', $slug, 'product_cat' );
		if ( ! $top || hainute_cat_stats( $top )['count'] < 1 ) {
			continue;
		}
		echo '<div class="home-cat-col"><h3><a href="' . esc_url( get_term_link( $top ) ) . '">' . esc_html( $title ) . '</a></h3>';
		foreach ( hainute_cat_children( $top ) as $mid ) {
			$leaves = hainute_cat_children( $mid );
			echo '<p class="home-cat-group"><a class="home-cat-mid" href="' . esc_url( get_term_link( $mid ) ) . '">' . esc_html( html_entity_decode( $mid->name ) ) . '</a>';
			foreach ( $leaves as $l ) {
				echo '<a href="' . esc_url( get_term_link( $l ) ) . '">' . esc_html( html_entity_decode( $l->name ) ) . '</a>';
			}
			echo '</p>';
		}
		echo '</div>';
	}
	echo '</div>';
}

/** Homepage: brandurile cu cele mai multe produse publicate. */
function hainute_the_home_brands( $n = 16 ) {
	$terms = get_terms( array( 'taxonomy' => 'product_brand', 'hide_empty' => true, 'orderby' => 'count', 'order' => 'DESC', 'number' => $n ) );
	if ( is_wp_error( $terms ) || ! $terms ) {
		return;
	}
	echo '<p class="cat-links">';
	foreach ( $terms as $t ) {
		echo '<a class="cat-chip" href="' . esc_url( get_term_link( $t ) ) . '">' . esc_html( html_entity_decode( $t->name ) ) . '</a>';
	}
	echo '</p>';
}

/** Homepage: textul din categorii-seo.json („acasa”). */
function hainute_the_home_text() {
	$t = hainute_seo_texts()['acasa'] ?? array();
	if ( empty( $t['text'] ) ) {
		return;
	}
	$top    = get_terms( array( 'taxonomy' => 'product_brand', 'hide_empty' => true, 'orderby' => 'count', 'order' => 'DESC', 'number' => 3 ) );
	$brands = array();
	foreach ( is_wp_error( $top ) ? array() : $top as $b ) {
		$brands[] = array( 'name' => html_entity_decode( $b->name ), 'url' => get_term_link( $b ), 'count' => $b->count );
	}
	$count = (int) wp_count_posts( 'product' )->publish;
	echo '<div class="home-seo">';
	if ( ! empty( $t['titlu'] ) ) {
		echo '<h2 class="home-title">' . esc_html( $t['titlu'] ) . '</h2>';
	}
	echo wp_kses_post( wpautop( hainute_seo_fill( $t['text'], $count, $brands ) ) );
	echo '</div>';
}

/**
 * Meniul de sus: categoriile principale întâi (Fete, Băieți, Bebeluși, Unisex), fără „Acasă”
 * (logo-ul duce acolo). Așa fiecare pagină are linkuri spre categorii.
 */
add_filter(
	'wp_nav_menu_items',
	function ( $items, $args ) {
		if ( 'primary' !== ( $args->theme_location ?? '' ) ) {
			return $items;
		}
		$items = preg_replace( '#<li[^>]*><a[^>]*href="' . preg_quote( home_url( '/' ), '#' ) . '"[^>]*>[^<]*</a></li>#', '', $items );
		$cats  = '';
		foreach ( array( 'fete' => 'Fete', 'baieti' => 'Băieți', 'bebe' => 'Bebeluși', 'unisex' => 'Unisex' ) as $slug => $label ) {
			$t = get_term_by( 'slug', $slug, 'product_cat' );
			if ( $t ) {
				$current = is_tax( 'product_cat' ) && ( (int) get_queried_object_id() === (int) $t->term_id || term_is_ancestor_of( $t, get_queried_object(), 'product_cat' ) );
				$cats   .= '<li class="menu-item menu-cat' . ( $current ? ' current-menu-item' : '' ) . '"><a href="' . esc_url( get_term_link( $t ) ) . '">' . esc_html( $label ) . '</a></li>';
			}
		}
		return $cats . $items;
	},
	10,
	2
);
