<?php
/**
 * SEO ușor: meta description + OpenGraph + Twitter + BreadcrumbList.
 *
 * Tema n-are plugin SEO. Aici generăm descrieri orientate pe disponibilitate („mărimi disponibile
 * prețuri și mărimi la N magazine") — exact unghiul de căutare al site-ului — plus
 * tag-uri de social sharing și breadcrumb schema. Se dezactivează singur dacă e
 * activ un plugin SEO (Yoast/RankMath), ca să nu dublăm.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Dacă un plugin SEO gestionează head-ul, nu ne băgăm. */
function hainute_seo_active() {
	return defined( 'WPSEO_VERSION' ) || defined( 'RANK_MATH_VERSION' ) || defined( 'AIOSEO_VERSION' ) || class_exists( 'SEOPress' );
}

/** Limba paginii: conținutul e în română, nu engleză. */
add_filter( 'language_attributes', function () { return 'lang="ro-RO"'; } );

/** Robots explicit: index, follow (+ preview mare de imagine deja pus de WP). */
/** Copie de test (link public temporar trycloudflare): niciodată în Google. */
function hainute_is_test_host() {
	return (bool) preg_match( '/\.trycloudflare\.com$/i', (string) ( $_SERVER['HTTP_X_FORWARDED_HOST'] ?? $_SERVER['HTTP_HOST'] ?? '' ) );
}
add_action(
	'send_headers',
	function () {
		if ( hainute_is_test_host() ) {
			header( 'X-Robots-Tag: noindex, nofollow', true );
		}
	}
);

add_filter( 'wp_robots', function ( $robots ) {
	if ( hainute_is_test_host() ) {
		return array( 'noindex' => true, 'nofollow' => true );
	}
	if ( hainute_seo_active() ) {
		return $robots;
	}
	// Căutarea internă și 404 nu au ce căuta în index (conținut subțire/duplicat);
	// `follow` rămâne ca linkurile spre produse să transmită valoare.
	if ( is_search() || is_404() ) {
		unset( $robots['index'], $robots['max-image-preview'] );
		$robots['noindex'] = true;
		$robots['follow']  = true;
		return $robots;
	}
	$robots['index']  = true;
	$robots['follow'] = true;
	return $robots;
} );

/** Canonical îl gestionăm noi (vezi hainute_seo_head), inclusiv pe homepage. */
remove_action( 'wp_head', 'rel_canonical' );

/**
 * Titlu descriptiv pentru homepage (altfel WordPress pune doar numele site-ului).
 * Spune exact ce face site-ul; intră și în <title>, og:title și twitter:title.
 */
add_filter(
	'pre_get_document_title',
	function ( $title ) {
		if ( hainute_seo_active() ) {
			return $title;
		}
		if ( is_front_page() || is_home() ) {
			return 'Găsește mărimea copilului la magazinul care o are pe stoc | ' . get_bloginfo( 'name' );
		}
		return $title;
	},
	20
);

/** Separator „|" în <title> (WP pune implicit o liniuță: „Produse – hainute.ro"). */
add_filter( 'document_title_separator', function () { return '|'; } );

/**
 * Titluri descriptive pentru listări: arhiva („Produse") și paginile de
 * categorie/brand primesc cuvintele după care se caută.
 */
add_filter(
	'document_title_parts',
	function ( $parts ) {
		if ( hainute_seo_active() ) {
			return $parts;
		}
		if ( ! empty( $parts['page'] ) ) {
			$parts['page'] = sprintf( __( 'Pagina %d', 'hainute' ), max( 2, (int) get_query_var( 'paged' ), (int) get_query_var( 'page' ) ) );
		}
		if ( is_post_type_archive( 'product' ) ) {
			$parts['title'] = __( 'Haine și încălțăminte copii: mărimi disponibile în magazine', 'hainute' );
		} elseif ( is_tax( 'product_cat' ) ) {
			$term = get_queried_object();
			$anc  = $term ? get_ancestors( $term->term_id, 'product_cat' ) : array();
			$top  = $anc ? get_term( end( $anc ), 'product_cat' ) : null;
			// „Geci & jachete pentru fete: mărimi disponibile în magazine" (genul ajută la căutare).
			if ( $top && ! is_wp_error( $top ) ) {
				$parts['title'] = sprintf( __( '%1$s pentru %2$s: mărimi disponibile în magazine', 'hainute' ), $term->name, mb_strtolower( $top->name ) );
			} else {
				$parts['title'] = sprintf( __( 'Haine și încălțăminte pentru %s: mărimi disponibile în magazine', 'hainute' ), mb_strtolower( $term->name ) );
			}
		} elseif ( is_tax( 'product_brand' ) ) {
			$parts['title'] = sprintf( __( '%s pentru copii: mărimi disponibile în magazine', 'hainute' ), single_term_title( '', false ) );
		} elseif ( is_singular( 'product' ) && function_exists( 'hainute_product_name_parts' ) ) {
			// „Calvin Klein Jeans geacă fete negru: vezi ce magazine au mărimea ta".
			$n     = hainute_product_name_parts( get_queried_object_id() );
			$name  = trim( preg_replace( '/\s+/u', ' ', implode( ' ', array( $n['brand'], $n['model'], mb_strtolower( $n['type'] ), $n['gender'], $n['color'] ) ) ) );
			$parts = array( 'title' => $name . ': ' . __( 'vezi ce magazine au mărimea ta', 'hainute' ) );
		} elseif ( is_search() ) {
			// WP e în engleză („Search Results for"); site-ul e în română.
			$parts['title'] = sprintf( __( 'Rezultate pentru „%s"', 'hainute' ), get_search_query() );
		} elseif ( is_404() ) {
			$parts['title'] = __( 'Pagina nu a fost găsită', 'hainute' );
		}
		return $parts;
	}
);

/** Descriere scurtă pentru un produs, orientată pe mărimi și disponibilitate. */
function hainute_seo_product_description( $product_id ) {
	if ( function_exists( 'hainute_size_range' ) ) {
		// „Alege mărimea copilului (128-176, orientativ 8-16 ani) și vezi pe loc
		// magazinele care o au pe stoc. Calvin Klein Jeans, negru."
		$r   = hainute_size_range( $product_id );
		$n   = hainute_product_name_parts( $product_id );
		$in  = array_filter( array( $r['interval'], $r['age'] ? 'orientativ ' . $r['age'] : '' ) );
		$who = trim( $n['brand'] . ' ' . $n['model'] );
		$desc = 'Alege mărimea copilului' . ( $in ? ' (' . implode( ', ', $in ) . ')' : '' ) . ' și vezi pe loc magazinele care o au pe stoc. '
			. ( '' !== $who ? $who : get_the_title( $product_id ) ) . ( $n['color'] ? ', ' . $n['color'] : '' ) . '.';
		return mb_strlen( $desc ) > 160 ? mb_substr( $desc, 0, 157 ) . '…' : $desc;
	}
	$title = get_the_title( $product_id );
	$brand = function_exists( 'hainute_get_brand' ) ? hainute_get_brand( $product_id ) : '';

	$stores = 0;
	$min    = 0;
	if ( function_exists( 'hainute_get_offers' ) ) {
		$names = array();
		foreach ( hainute_get_offers( $product_id ) as $o ) {
			$nm = $o->store ? $o->store->name : '';
			if ( $nm ) {
				$names[ $nm ] = 1;
			}
			if ( 'out_of_stock' !== $o->stock_status && $o->price > 0 && ( 0 === $min || $o->price < $min ) ) {
				$min = (float) $o->price;
			}
		}
		$stores = count( $names );
	}

	$parts = array();
	if ( $stores >= 2 ) {
		$parts[] = 'Vezi mărimile disponibile la ' . hainute_ro_count( $stores, 'magazin', 'magazine' );
	} else {
		$parts[] = __( 'Vezi disponibilitate, mărimi și preț', 'hainute' );
	}
	$parts[] = $brand ? $title . ' (' . $brand . ')' : $title;
	if ( $min > 0 ) {
		$parts[] = sprintf( __( 'de la %s lei', 'hainute' ), number_format_i18n( $min, 0 ) );
	}

	$desc = implode( ' · ', $parts ) . '.';
	if ( mb_strlen( $desc ) > 160 ) {
		$desc = mb_substr( $desc, 0, 157 ) . '…';
	}
	return $desc;
}

/** Meta description + OpenGraph + Twitter, pe pagini de produs și arhive. */
function hainute_seo_head() {
	if ( hainute_seo_active() ) {
		return;
	}

	$desc  = '';
	$title = wp_get_document_title();
	$url   = '';
	$image = '';
	$type  = 'website';

	if ( is_singular( 'product' ) ) {
		$pid   = get_queried_object_id();
		$desc  = hainute_seo_product_description( $pid );
		$url   = get_permalink( $pid );
		$image = function_exists( 'hainute_product_image' ) ? hainute_product_image( $pid, 'large' ) : '';
		$type  = 'product';
	} elseif ( is_tax( array( 'product_cat', 'product_brand', 'product_gender', 'product_age' ) ) ) {
		$term = get_queried_object();
		$desc = $term && ! empty( $term->description )
			? wp_strip_all_tags( $term->description )
			: sprintf( __( 'Vezi în ce magazine găsești mărimea potrivită pentru %s: mărimi disponibile și stoc actualizat, într-un singur loc.', 'hainute' ), $term->name );
		$url  = get_term_link( $term );
	} elseif ( is_post_type_archive( 'product' ) ) {
		$desc = __( 'Haine și încălțăminte pentru copii din mai multe magazine online: vezi mărimile disponibile și stocul actualizat, într-un singur loc.', 'hainute' );
		$url  = get_post_type_archive_link( 'product' );
	} elseif ( is_page() ) {
		$pid  = get_queried_object_id();
		$desc = (string) get_post_meta( $pid, '_hainute_meta_desc', true );
		if ( '' === $desc ) {
			$desc = wp_trim_words( wp_strip_all_tags( (string) get_post_field( 'post_content', $pid ) ), 30 );
		}
		$url = get_permalink( $pid );
	} elseif ( is_front_page() || is_home() ) {
		$desc = sprintf( __( 'Găsește mărimea potrivită pentru copilul tău, direct la magazinul care o are. Stoc pe mărimi la %d magazine, verificat la fiecare %d ore.', 'hainute' ), count( hainute_active_store_names() ), hainute_refresh_hours() );
		$url  = home_url( '/' );
	} else {
		return;
	}

	if ( mb_strlen( $desc ) > 160 ) {
		$desc = mb_substr( $desc, 0, 157 ) . '…';
	}

	// Paginare (/page/2/): canonical propriu, nu spre pagina 1 (recomandarea Google).
	$paged = (int) get_query_var( 'paged' );
	if ( $paged > 1 && ( is_post_type_archive( 'product' ) || is_tax() ) ) {
		$url = get_pagenum_link( $paged );
	}

	echo "\n" . '<meta name="description" content="' . esc_attr( $desc ) . '">' . "\n";
	if ( $url ) {
		echo '<link rel="canonical" href="' . esc_url( $url ) . '">' . "\n";
	}
	echo '<meta property="og:type" content="' . esc_attr( $type ) . '">' . "\n";
	echo '<meta property="og:site_name" content="' . esc_attr( get_bloginfo( 'name' ) ) . '">' . "\n";
	echo '<meta property="og:title" content="' . esc_attr( $title ) . '">' . "\n";
	echo '<meta property="og:description" content="' . esc_attr( $desc ) . '">' . "\n";
	if ( $url ) {
		echo '<meta property="og:url" content="' . esc_url( $url ) . '">' . "\n";
	}
	if ( $image ) {
		echo '<meta property="og:image" content="' . esc_url( $image ) . '">' . "\n";
		echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
	} else {
		echo '<meta name="twitter:card" content="summary">' . "\n";
	}
	echo '<meta name="twitter:title" content="' . esc_attr( $title ) . '">' . "\n";
	echo '<meta name="twitter:description" content="' . esc_attr( $desc ) . '">' . "\n";
	if ( $image ) {
		echo '<meta name="twitter:image" content="' . esc_url( $image ) . '">' . "\n";
	}
}
add_action( 'wp_head', 'hainute_seo_head', 1 );

/**
 * WebSite + Organization (JSON-LD) pe homepage — reprezentarea machine-readable a
 * entității și site-ului pentru Google. URL-urile folosesc home_url() → corecte pe live.
 */
function hainute_seo_website_schema() {
	if ( hainute_seo_active() || ! ( is_front_page() || is_home() ) ) {
		return;
	}
	$home = home_url( '/' );
	$name = get_bloginfo( 'name' );
	// Datele firmei = cele din footer (publice). Ajută Google să lege site-ul de o
	// entitate reală (încredere). `sameAs`: de completat cu profilurile sociale.
	$org = array(
		'@type'      => 'Organization',
		'@id'        => $home . '#organization',
		'name'       => $name,
		'url'        => $home,
		'description' => sprintf( 'hainute.ro te ajută să găsești mărimea potrivită pentru copilul tău, direct la magazinul care o are: verifică stocul pe mărimi la %d magazine online din România, la fiecare %d ore.', count( hainute_active_store_names() ), hainute_refresh_hours() ),
		'legalName'  => 'FAIR CLICK S.R.L.',
		'taxID'      => '54682438',
		'identifier' => array(
			'@type'      => 'PropertyValue',
			'propertyID' => 'Nr. Registrul Comerțului',
			'value'      => 'J2026031574004',
		),
		'address'    => array(
			'@type'           => 'PostalAddress',
			'streetAddress'   => 'Drumul Pădurea Neagră nr. 24, Corp A, Bl. OX01/1, Etaj 1, Ap. 6',
			'addressLocality' => 'București',
			'addressRegion'   => 'Sector 1',
			'addressCountry'  => 'RO',
		),
	);
	$contact = get_page_by_path( 'contact' );
	if ( $contact ) {
		$org['contactPoint'] = array(
			'@type'       => 'ContactPoint',
			'contactType' => 'customer support',
			'url'         => get_permalink( $contact ),
			'availableLanguage' => 'ro',
		);
	}
	$logo_id = (int) get_theme_mod( 'custom_logo' );
	if ( $logo_id ) {
		$src = wp_get_attachment_image_src( $logo_id, 'full' );
		if ( $src ) {
			$org['logo'] = array( '@type' => 'ImageObject', 'url' => $src[0] );
		}
	}
	$graph = array(
		'@context' => 'https://schema.org',
		'@graph'   => array(
			array(
				'@type'       => 'WebSite',
				'@id'         => $home . '#website',
				'url'         => $home,
				'name'        => $name,
				'description' => 'Găsește mărimea potrivită pentru copilul tău, direct la magazinul care o are.',
				'inLanguage'  => 'ro-RO',
				'publisher'   => array( '@id' => $home . '#organization' ),
			),
			$org,
		),
	);
	echo '<script type="application/ld+json">' . wp_json_encode( $graph, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n";
}
add_action( 'wp_head', 'hainute_seo_website_schema', 5 );

/**
 * BreadcrumbList (calea din rezultatul Google) — identică cu breadcrumb-ul
 * vizibil: tot lanțul de categorii (Bebe › Încălțăminte › Adidași), pe pagina
 * de produs și pe paginile de categorie.
 */
function hainute_seo_breadcrumb_schema() {
	if ( hainute_seo_active() || ! ( is_singular( 'product' ) || is_tax( 'product_cat' ) ) ) {
		return;
	}
	$items = array();
	$pos   = 1;
	$add   = function ( $name, $url ) use ( &$items, &$pos ) {
		$items[] = array( '@type' => 'ListItem', 'position' => $pos++, 'name' => wp_strip_all_tags( $name ), 'item' => $url );
	};

	$add( __( 'Acasă', 'hainute' ), home_url( '/' ) );
	$add( __( 'Produse', 'hainute' ), get_post_type_archive_link( 'product' ) );

	if ( is_tax( 'product_cat' ) ) {
		$term = get_queried_object();
		foreach ( array_reverse( get_ancestors( $term->term_id, 'product_cat' ) ) as $id ) {
			$t = get_term( $id, 'product_cat' );
			$add( $t->name, get_term_link( $t ) );
		}
		$add( $term->name, get_term_link( $term ) );
	} else {
		$pid  = get_queried_object_id();
		$cats = get_the_terms( $pid, 'product_cat' );
		if ( $cats && ! is_wp_error( $cats ) ) {
			// Frunza cea mai adâncă + strămoșii ei (ca breadcrumb-ul din pagină).
			$leaf = $cats[0];
			foreach ( $cats as $c ) {
				if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
					$leaf = $c;
				}
			}
			foreach ( array_reverse( get_ancestors( $leaf->term_id, 'product_cat' ) ) as $id ) {
				$t = get_term( $id, 'product_cat' );
				$add( $t->name, get_term_link( $t ) );
			}
			$add( $leaf->name, get_term_link( $leaf ) );
		}
		$add( get_the_title( $pid ), get_permalink( $pid ) );
	}

	$schema = array( '@context' => 'https://schema.org', '@type' => 'BreadcrumbList', 'itemListElement' => $items );
	echo "\n" . '<script type="application/ld+json">' . wp_json_encode( $schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n";
}
add_action( 'wp_head', 'hainute_seo_breadcrumb_schema', 2 );
