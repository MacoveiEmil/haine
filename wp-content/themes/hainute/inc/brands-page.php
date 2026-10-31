<?php
/**
 * Pagina „Branduri" (/branduri/): toate brandurile cu produse publicate, grupate
 * alfabetic, cu link spre pagina fiecărui brand. E o rută virtuală (nu o pagină din
 * baza de date), deci ajunge pe server doar prin git; regulile de rewrite se
 * reîmprospătează singure o dată, când se schimbă HAINUTE_BRANDS_REWRITE_V.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'HAINUTE_BRANDS_REWRITE_V', '1' );

add_action(
	'init',
	function () {
		add_rewrite_rule( '^branduri/?$', 'index.php?hainute_brands=1', 'top' );
		if ( get_option( 'hainute_brands_rewrite_v' ) !== HAINUTE_BRANDS_REWRITE_V ) {
			flush_rewrite_rules( false );
			update_option( 'hainute_brands_rewrite_v', HAINUTE_BRANDS_REWRITE_V, false );
		}
	}
);

add_filter(
	'query_vars',
	function ( $vars ) {
		$vars[] = 'hainute_brands';
		return $vars;
	}
);

function hainute_is_brands_page() {
	return (bool) get_query_var( 'hainute_brands' );
}

/** Ruta nu are nimic în baza de date: nu e 404, iar șablonul e al nostru. */
add_action(
	'template_redirect',
	function () {
		if ( ! hainute_is_brands_page() ) {
			return;
		}
		global $wp_query;
		$wp_query->is_404 = false;
		$wp_query->is_home = false;
		status_header( 200 );
	},
	1
);

add_filter(
	'template_include',
	function ( $template ) {
		return hainute_is_brands_page() ? HAINUTE_THEME_DIR . '/brands-page.php' : $template;
	}
);

/**
 * Brandurile cu produse publicate, cu numărul de produse. Cache 1h.
 *
 * @return array[] { slug, name, count, url }
 */
function hainute_all_brands() {
	$cached = get_transient( 'hainute_all_brands_v2' );
	if ( is_array( $cached ) ) {
		return $cached;
	}
	global $wpdb;
	$rows = $wpdb->get_results(
		"SELECT t.term_id, t.slug, t.name, COUNT(DISTINCT p.ID) AS n
		 FROM {$wpdb->posts} p
		 INNER JOIN {$wpdb->term_relationships} rb ON rb.object_id = p.ID
		 INNER JOIN {$wpdb->term_taxonomy} tb ON tb.term_taxonomy_id = rb.term_taxonomy_id AND tb.taxonomy = 'product_brand'
		 INNER JOIN {$wpdb->terms} t ON t.term_id = tb.term_id
		 WHERE p.post_type = 'product' AND p.post_status = 'publish'
		 GROUP BY t.term_id, t.slug, t.name
		 ORDER BY t.name ASC"
	);
	$brands = array();
	foreach ( (array) $rows as $r ) {
		$link = get_term_link( (int) $r->term_id, 'product_brand' );
		if ( is_wp_error( $link ) ) {
			continue;
		}
		$brands[] = array( 'slug' => $r->slug, 'name' => html_entity_decode( $r->name ), 'count' => (int) $r->n, 'url' => $link, 'img' => hainute_brand_image( (int) $r->term_id ) );
	}
	set_transient( 'hainute_all_brands_v2', $brands, HOUR_IN_SECONDS );
	return $brands;
}

/** Poza brandului = poza produsului cel mai nou al brandului care are poză. */
function hainute_brand_image( $term_id ) {
	$ids = get_posts(
		array(
			'post_type'        => 'product',
			'post_status'      => 'publish',
			'posts_per_page'   => 8,
			'fields'           => 'ids',
			'no_found_rows'    => true,
			'suppress_filters' => true,
			'tax_query'        => array( array( 'taxonomy' => 'product_brand', 'terms' => $term_id ) ),
		)
	);
	foreach ( $ids as $id ) {
		$img = hainute_product_image( $id, 'medium' );
		if ( $img ) {
			return $img;
		}
	}
	return '';
}

/** Cardul unui brand: poza, numele, numărul de produse. */
function hainute_brand_card( $b ) {
	?>
	<a class="brand-card" href="<?php echo esc_url( $b['url'] ); ?>" data-name="<?php echo esc_attr( $b['name'] ); ?>">
		<span class="brand-card-img">
			<?php if ( ! empty( $b['img'] ) ) : ?>
				<img src="<?php echo esc_url( hainute_img_resize( $b['img'], 300 ) ); ?>" alt="" loading="lazy" decoding="async" referrerpolicy="no-referrer">
			<?php else : ?>
				<span class="brand-card-ph"><?php echo esc_html( hainute_brand_letter( $b['name'] ) ); ?></span>
			<?php endif; ?>
		</span>
		<span class="brand-card-name"><?php echo esc_html( $b['name'] ); ?></span>
		<span class="brand-count"><?php echo esc_html( sprintf( _n( '%d produs', '%d produse', $b['count'], 'hainute' ), $b['count'] ) ); ?></span>
	</a>
	<?php
}

/** Litera de grupare: fără diacritice, majusculă; cifrele și simbolurile merg la „#". */
function hainute_brand_letter( $name ) {
	$l = strtoupper( substr( remove_accents( trim( $name ) ), 0, 1 ) );
	return ( '' !== $l && ctype_alpha( $l ) ) ? $l : '#';
}

function hainute_brands_page_title() {
	return __( 'Branduri de haine și încălțăminte pentru copii', 'hainute' );
}

function hainute_brands_page_desc() {
	return sprintf(
		/* translators: %d: numărul de branduri */
		__( 'Cele %d de branduri de haine și încălțăminte pentru copii de pe beestyle.ro: alege brandul și vezi mărimile disponibile în magazine.', 'hainute' ),
		count( hainute_all_brands() )
	);
}

/* Titlu, descriere și canonical (cu sau fără plugin SEO). */
add_filter(
	'pre_get_document_title',
	function ( $title ) {
		return hainute_is_brands_page() ? hainute_brands_page_title() . ' | ' . get_bloginfo( 'name' ) : $title;
	},
	99
);
add_filter( 'rank_math/frontend/title', function ( $t ) { return hainute_is_brands_page() ? hainute_brands_page_title() : $t; } );
add_filter( 'rank_math/frontend/description', function ( $d ) { return hainute_is_brands_page() ? hainute_brands_page_desc() : $d; } );
add_filter( 'rank_math/frontend/canonical', function ( $c ) { return hainute_is_brands_page() ? home_url( '/branduri/' ) : $c; } );
add_action(
	'wp_head',
	function () {
		if ( ! hainute_is_brands_page() || hainute_seo_active() ) {
			return; // cu plugin SEO, meta-urile vin din filtrele de mai sus
		}
		echo "\n" . '<meta name="description" content="' . esc_attr( hainute_brands_page_desc() ) . '">' . "\n";
		echo '<link rel="canonical" href="' . esc_url( home_url( '/branduri/' ) ) . '">' . "\n";
	},
	2
);

/** Linkul „Branduri" în meniul principal (după „Produse") și în cel din footer, fără a edita meniul din baza de date. */
add_filter(
	'wp_nav_menu_items',
	function ( $items, $args ) {
		if ( ! in_array( $args->theme_location ?? '', array( 'primary', 'footer' ), true ) || false !== strpos( $items, '/branduri' ) ) {
			return $items;
		}
		$cur  = hainute_is_brands_page() ? ' current-menu-item' : '';
		$li   = '<li class="menu-item menu-item-brands' . $cur . '"><a href="' . esc_url( home_url( '/branduri/' ) ) . '">' . esc_html__( 'Branduri', 'hainute' ) . '</a></li>';
		$prod = preg_replace( '#(<li[^>]*>\s*<a[^>]*href="[^"]*/produse/?"[^>]*>.*?</a>\s*</li>)#s', '$1' . $li, $items, 1, $n );
		return $n ? $prod : $items . $li;
	},
	10,
	2
);
