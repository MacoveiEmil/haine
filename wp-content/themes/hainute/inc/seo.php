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
/** Copie de test (link trycloudflare) sau site în pre-lansare: niciodată în Google. */
function hainute_is_test_host() {
	if ( defined( 'HAINUTE_PRELAUNCH' ) && HAINUTE_PRELAUNCH ) {
		return true; // vezi docker/gate.php
	}
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
	// Magazine inactive sau dubluri (ex. „Sportisimo Europe" = Sportisimo.ro): noindex.
	if ( is_tax( 'store' ) && ! hainute_store_term_indexable( get_queried_object() ) ) {
		unset( $robots['index'], $robots['max-image-preview'] );
		$robots['noindex'] = true;
		$robots['follow']  = true;
		return $robots;
	}
	// Listare fără niciun produs (brand/categorie golită): pagină subțire, nu în index.
	if ( is_search() || is_404() || ( is_tax() && 0 === (int) $GLOBALS['wp_query']->found_posts ) ) {
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
			return 'Găsește mărimea copilului la magazinul care o are | ' . get_bloginfo( 'name' );
		}
		return $title;
	},
	20
);

/** Separator „|" în <title> (WP pune implicit o liniuță: „Produse – beestyle.ro"). */
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
				$parts['title'] = 'unisex' === $top->slug
					? sprintf( __( '%s unisex pentru copii: mărimi disponibile în magazine', 'hainute' ), $term->name )
					: sprintf( __( '%1$s pentru %2$s: mărimi disponibile în magazine', 'hainute' ), $term->name, mb_strtolower( $top->name ) );
			} else {
				$parts['title'] = 'unisex' === $term->slug ? __( 'Haine și încălțăminte unisex pentru copii: mărimi disponibile în magazine', 'hainute' ) : sprintf( __( 'Haine și încălțăminte pentru %s: mărimi disponibile în magazine', 'hainute' ), mb_strtolower( $term->name ) );
			}
		} elseif ( is_tax( 'store' ) ) {
			$parts['title'] = sprintf( __( 'Haine și încălțăminte copii la %s: mărimi disponibile', 'hainute' ), hainute_store_display_name( single_term_title( '', false ) ) );
		} elseif ( is_tax( 'product_brand' ) ) {
			$parts['title'] = sprintf( __( '%s pentru copii: mărimi disponibile în magazine', 'hainute' ), single_term_title( '', false ) );
		} elseif ( is_singular( 'product' ) && function_exists( 'hainute_product_name_parts' ) ) {
			$pid   = get_queried_object_id();
			$dupes = hainute_seo_title_dupes();
			$parts = array( 'title' => hainute_seo_product_title( $pid, $dupes['code'][ $pid ] ?? '' ) );
		} elseif ( is_search() ) {
			// WP e în engleză („Search Results for"); site-ul e în română.
			$parts['title'] = sprintf( __( 'Rezultate pentru „%s"', 'hainute' ), get_search_query() );
		} elseif ( is_404() ) {
			$parts['title'] = __( 'Pagina nu a fost găsită', 'hainute' );
		}
		return $parts;
	}
);

/**
 * Max ~70 caractere în <title> (altfel Google taie): întâi renunțăm la „| beestyle.ro",
 * apoi la „în magazine" din titlurile de listare.
 */
add_filter(
	'document_title_parts',
	function ( $parts ) {
		$len = function () use ( &$parts ) {
			return mb_strlen( implode( ' | ', array_filter( $parts ) ) );
		};
		if ( $len() > 70 && isset( $parts['site'] ) ) {
			unset( $parts['site'] );
		}
		if ( $len() > 70 && isset( $parts['title'] ) ) {
			$parts['title'] = preg_replace( '/ în magazine$/u', '', $parts['title'] );
		}
		if ( $len() > 70 && isset( $parts['title'] ) ) {
			$parts['title'] = preg_replace( '/: mărimi disponibile$/u', '', $parts['title'] );
		}
		return $parts;
	},
	99
);

/** Numele produsului pentru titlu/descriere: „GUESS geacă fete roz" (+ codul modelului, dacă e dat). */
function hainute_seo_product_name( $product_id, $code = '', $with_color = true, $with_gender = true, $model_words = null ) {
	$n     = hainute_product_name_parts( $product_id );
	$model = preg_split( '/\s+/u', trim( $n['model'] ), -1, PREG_SPLIT_NO_EMPTY );
	if ( null !== $model_words ) {
		$model = array_slice( $model, 0, $model_words );
	}
	if ( '' !== $code && '' !== $n['color'] && false !== mb_stripos( $code, $n['color'] ) ) {
		$with_color = false; // culoarea e deja în diferențiator („H4BJ10 122-176 roz")
	}
	return trim( preg_replace( '/\s+/u', ' ', implode( ' ', array( $n['brand'], implode( ' ', $model ), mb_strtolower( $n['type'] ), $with_gender ? $n['gender'] : '', $with_color ? $n['color'] : '', $code ) ) ) );
}

/**
 * „Calvin Klein Jeans geacă fete negru: vezi ce magazine au mărimea ta".
 * Max ~70 caractere: renunțăm pe rând la culoare, gen, apoi la ultimele cuvinte din
 * model (toate, dacă avem codul modelului). Codul (la produsele care altfel ar avea
 * același titlu) rămâne; la nevoie, finalul se scurtează.
 */
function hainute_seo_product_title( $product_id, $code = '' ) {
	$suffix = ': ' . __( 'vezi ce magazine au mărimea ta', 'hainute' );
	$words  = count( preg_split( '/\s+/u', trim( hainute_product_name_parts( $product_id )['model'] ), -1, PREG_SPLIT_NO_EMPTY ) );
	$name   = hainute_seo_product_name( $product_id, $code );
	if ( mb_strlen( $name . $suffix ) > 70 ) {
		$name = hainute_seo_product_name( $product_id, $code, false );
	}
	if ( mb_strlen( $name . $suffix ) > 70 ) {
		$name = hainute_seo_product_name( $product_id, $code, false, false );
	}
	while ( mb_strlen( $name . $suffix ) > 70 && $words > ( '' !== $code ? 0 : 1 ) ) {
		$name = hainute_seo_product_name( $product_id, $code, false, false, --$words );
	}
	if ( mb_strlen( $name . $suffix ) > 70 ) {
		$suffix = ': ' . __( 'vezi unde e mărimea ta', 'hainute' );
	}
	if ( mb_strlen( $name . $suffix ) > 70 ) {
		$suffix = '';
	}
	return $name . $suffix;
}

/**
 * Produsele care ar avea același <title> (ex. 6 × „GUESS geacă fete roz") primesc un
 * diferențiator, ca fiecare pagină să fie unică în Google: codul modelului de la magazin
 * („J5BL22"), apoi și intervalul de mărimi / culoarea (variante ale aceluiași model).
 * Produsele identice (importate de două ori) primesc canonical spre primul.
 * @return array{code:array<int,string>,canon:array<int,int>}
 */
function hainute_seo_title_dupes() {
	$map = get_transient( 'hainute_title_dupes_v2' );
	if ( is_array( $map ) ) {
		return $map;
	}
	$ids    = get_posts( array( 'post_type' => 'product', 'post_status' => 'publish', 'numberposts' => -1, 'fields' => 'ids', 'orderby' => 'ID', 'order' => 'ASC' ) );
	$groups = array();
	update_meta_cache( 'post', $ids );
	update_object_term_cache( $ids, 'product' );
	foreach ( $ids as $id ) {
		$groups[ mb_strtolower( hainute_seo_product_title( $id ) ) ][] = $id;
	}
	$map = array( 'code' => array(), 'canon' => array() );
	foreach ( $groups as $group ) {
		if ( count( $group ) < 2 ) {
			continue;
		}
		$cands = array();
		foreach ( $group as $id ) {
			$seg   = strtoupper( strtok( (string) get_post_meta( $id, '_hainute_model_code', true ), '.' ) );
			$seg   = preg_match( '/^[A-Z0-9-]{3,20}$/', $seg ) ? $seg : '';
			$range = function_exists( 'hainute_size_range' ) ? hainute_size_range( $id )['interval'] : '';
			$color = mb_strtolower( trim( explode( ',', (string) get_post_meta( $id, '_hainute_colors', true ) )[0] ) );
			$cands[ $id ] = array( $seg, trim( "$seg $range" ), trim( "$seg $color" ), trim( "$seg $range $color" ) );
		}
		$pick = 3;
		foreach ( array( 0, 1, 2 ) as $k ) {
			$vals = array_column( $cands, $k );
			if ( ! in_array( '', $vals, true ) && count( array_unique( $vals ) ) === count( $vals ) ) {
				$pick = $k;
				break;
			}
		}
		$first = array();
		foreach ( $group as $id ) {
			$code                = $cands[ $id ][ $pick ];
			$map['code'][ $id ]  = $code;
			if ( isset( $first[ $code ] ) ) {
				$map['canon'][ $id ] = $first[ $code ];
			} else {
				$first[ $code ] = $id;
			}
		}
	}
	// A doua trecere: titlurile scurtate la 70 de caractere (fără culoare/gen) se pot
	// suprapune din nou; acolo intră și al doilea segment al codului („T1X9-35219").
	$final = array();
	foreach ( $ids as $id ) {
		if ( ! isset( $map['canon'][ $id ] ) ) {
			$final[ mb_strtolower( hainute_seo_product_title( $id, $map['code'][ $id ] ?? '' ) ) ][] = $id;
		}
	}
	foreach ( $final as $group ) {
		if ( count( $group ) < 2 ) {
			continue;
		}
		foreach ( $group as $id ) {
			$segs = explode( '.', strtoupper( (string) get_post_meta( $id, '_hainute_model_code', true ) ) );
			if ( count( $segs ) > 1 && preg_match( '/^[A-Z0-9]{2,10}$/', $segs[1] ) ) {
				$map['code'][ $id ] = trim( $segs[0] . '-' . $segs[1] . ' ' . preg_replace( '/^\S+\s*/', '', $map['code'][ $id ] ?? '' ) );
			}
		}
	}
	set_transient( 'hainute_title_dupes_v2', $map, 6 * HOUR_IN_SECONDS );
	return $map;
}

/** Descriere scurtă pentru un produs, orientată pe mărimi și disponibilitate. */
function hainute_seo_product_description( $product_id ) {
	if ( function_exists( 'hainute_size_range' ) ) {
		// „Alege mărimea copilului (128-176, orientativ 8-16 ani) și vezi pe loc
		// magazinele care o au pe stoc. Calvin Klein Jeans, negru."
		// Numele produsului întâi (unic, cu codul modelului la dubluri), ca descrierile să difere între ele.
		$r     = hainute_size_range( $product_id );
		$in    = array_filter( array( $r['interval'], $r['age'] ? 'orientativ ' . $r['age'] : '' ) );
		$dupes = hainute_seo_title_dupes();
		$who   = hainute_seo_product_name( $product_id, $dupes['code'][ $product_id ] ?? '' );
		$who   = '' !== $who ? $who : get_the_title( $product_id );
		$desc  = mb_strtoupper( mb_substr( $who, 0, 1 ) ) . mb_substr( $who, 1 ) . ': alege mărimea copilului' . ( $in ? ' (' . implode( ', ', $in ) . ')' : '' ) . ' și vezi pe loc magazinele care o au pe stoc.';
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
		$dupes = hainute_seo_title_dupes();
		$url   = get_permalink( $dupes['canon'][ $pid ] ?? $pid ); // produs importat de două ori: canonical spre primul
		$image = function_exists( 'hainute_product_image' ) ? hainute_product_image( $pid, 'large' ) : '';
		$type  = 'product';
	} elseif ( is_tax( array( 'product_cat', 'product_brand', 'product_gender', 'product_age' ) ) ) {
		$term = get_queried_object();
		$desc = $term && ! empty( $term->description )
			? wp_strip_all_tags( $term->description )
			: sprintf( __( 'Vezi în ce magazine găsești mărimea potrivită pentru %s: mărimi disponibile și stoc actualizat, într-un singur loc.', 'hainute' ), $term->name );
		$url  = get_term_link( $term );
	} elseif ( is_tax( 'store' ) ) {
		$term = get_queried_object();
		$desc = sprintf( __( 'Haine și încălțăminte pentru copii de la %1$s: vezi ce mărimi sunt pe stoc, verificat la fiecare %2$d ore.', 'hainute' ), hainute_store_display_name( $term->name ), hainute_refresh_hours() );
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
		'description' => sprintf( 'beestyle.ro te ajută să găsești mărimea potrivită pentru copilul tău, direct la magazinul care o are: verifică stocul pe mărimi la %d magazine online din România, la fiecare %d ore.', count( hainute_active_store_names() ), hainute_refresh_hours() ),
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
	$src     = $logo_id ? wp_get_attachment_image_src( $logo_id, 'full' ) : false;
	$org['logo'] = array( '@type' => 'ImageObject', 'url' => $src ? $src[0] : get_site_icon_url( 512 ) );
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
	echo "\n" . '<script type="application/ld+json">' . wp_json_encode( hainute_schema_decode( $schema ), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . '</script>' . "\n";
}
add_action( 'wp_head', 'hainute_seo_breadcrumb_schema', 2 );

// XML-RPC nu e folosit (fără aplicații externe de publicare): închis, ca suprafață de atac mai mică.
add_filter( 'xmlrpc_enabled', '__return_false' );
remove_action( 'wp_head', 'rsd_link' );

// Versiunea WordPress nu se afișează (nici în head, nici în feed-uri).
remove_action( 'wp_head', 'wp_generator' );
add_filter( 'the_generator', '__return_empty_string' );
remove_action( 'wp_head', 'wp_shortlink_wp_head' );
// Site-ul n-are blog: fără linkuri spre feed-urile de articole/comentarii.
remove_action( 'wp_head', 'feed_links', 2 );
remove_action( 'wp_head', 'feed_links_extra', 3 );

/**
 * Sitemap doar cu paginile utile: produse, categorii, branduri, magazine active, pagini.
 * Fără utilizatori (ar expune numele contului de admin), articole sau categorii de blog.
 */
add_filter( 'wp_sitemaps_add_provider', function ( $provider, $name ) {
	return 'users' === $name ? false : $provider;
}, 10, 2 );
add_filter( 'wp_sitemaps_post_types', function ( $types ) {
	unset( $types['post'] );
	return $types;
} );
add_filter( 'wp_sitemaps_taxonomies', function ( $taxes ) {
	unset( $taxes['category'], $taxes['post_tag'], $taxes['post_format'], $taxes['product_gender'] );
	return $taxes;
} );
// Produsele importate de două ori au canonical spre primul: în sitemap doar originalul.
add_filter( 'wp_sitemaps_posts_query_args', function ( $args, $post_type ) {
	if ( 'product' === $post_type ) {
		$args['post__not_in'] = array_keys( hainute_seo_title_dupes()['canon'] );
	}
	return $args;
}, 10, 2 );

// Magazinele inactive/dublurile sunt noindex (vezi wp_robots), deci nici în sitemap.
add_filter( 'wp_sitemaps_taxonomies_query_args', function ( $args, $taxonomy ) {
	if ( 'store' === $taxonomy ) {
		$args['include'] = wp_list_pluck( hainute_store_terms_active(), 'term_id' ) ?: array( 0 );
	}
	return $args;
}, 10, 2 );

// Arhivele de autor/blog (/author/emil/, /?author=1, /category/…) și feed-urile nu au
// conținut: acasă. Prioritatea 1 = înaintea redirect_canonical, care ar arăta numele contului.
add_action( 'template_redirect', function () {
	if ( isset( $_GET['author'] ) || is_author() || is_category() || is_tag() || is_date() || is_feed() || ( is_singular( 'post' ) && ! is_user_logged_in() ) ) {
		wp_safe_redirect( home_url( '/' ), 301 );
		exit;
	}
	// /gen/fete/ dublează /categorie/fete/ (filtrul ?gen= din listări rămâne).
	if ( preg_match( '#^/gen/([a-z0-9-]+)/?$#', (string) wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH ), $m ) ) {
		$cat = get_term_by( 'slug', $m[1], 'product_cat' );
		wp_safe_redirect( $cat ? get_term_link( $cat ) : home_url( '/' ), 301 );
		exit;
	}
}, 1 );

/** Favicon / iconița din Google și de pe telefon: assets/img (altfel WordPress pune logo-ul lui). */
add_filter( 'get_site_icon_url', function ( $url, $size ) {
	if ( get_option( 'site_icon' ) ) { // iconiță setată din Customizer: are prioritate
		return $url;
	}
	$file = $size <= 32 ? 'favicon-32.png' : ( $size <= 180 ? 'apple-touch-icon.png' : 'icon-512.png' );
	return get_template_directory_uri() . '/assets/img/' . $file;
}, 10, 2 );

// Lista de utilizatori din REST API (/wp-json/wp/v2/users) doar pentru cine e logat.
add_filter( 'rest_endpoints', function ( $endpoints ) {
	if ( ! is_user_logged_in() ) {
		unset( $endpoints['/wp/v2/users'], $endpoints['/wp/v2/users/(?P<id>[\d]+)'] );
	}
	return $endpoints;
} );
