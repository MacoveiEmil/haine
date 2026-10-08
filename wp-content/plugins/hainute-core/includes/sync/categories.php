<?php
/**
 * Category normalization — maps the messy, store-specific category paths
 * (e.g. "Sandale Nike Copii", "Copii/Băieți/Accesorii/Genţi") to a small set
 * of clean canonical categories, by matching keywords against the category
 * path + product title. This is what makes navigation and SEO consistent
 * across stores.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Ordered keyword → canonical category map. First match wins, so more specific
 * entries come first. Keywords are matched diacritic-insensitive as substrings.
 *
 * @return array[] Each: [ canonical_name, [keywords...] ]
 */
function hainute_category_rules() {
	return apply_filters(
		'hainute_category_rules',
		array(
			// --- Încălțăminte ---
			array( 'Sandale', array( 'sandale', 'sanda' ) ),
			array( 'Papuci și șlapi', array( 'papuci', 'slapi', 'flip flop', 'saboti' ) ),
			array( 'Ghete și cizme', array( 'ghete', 'cizme', 'bocanci', 'apreschi' ) ),
			array( 'Mocasini și balerini', array( 'mocasin', 'loafer', 'balerin' ) ),
			array( 'Botoșei', array( 'botosei', 'botosel' ) ),
			array( 'Pantofi sport', array( 'pantofi sport', 'sneaker', 'adidasi', 'tenisi', 'running', 'runner', 'air force', 'air max', 'jordan' ) ),
			array( 'Pantofi', array( 'pantofi', 'pantof' ) ),
			// --- Îmbrăcăminte ---
			array( 'Geci și jachete', array( 'geaca', 'geci', 'jacheta', 'palton', 'parka', 'windbreaker', 'canadiana', 'fas' ) ),
			array( 'Treninguri', array( 'trening', 'compleu sport', 'set trening' ) ),
			array( 'Hanorace și pulovere', array( 'hanorac', 'sweatshirt', 'pulover', 'cardigan', 'bluza cu gluga', 'gluga' ) ),
			array( 'Salopete', array( 'salopeta', 'salopete', 'overall' ) ),
			array( 'Rochii', array( 'rochie', 'rochii', 'rochita' ) ),
			array( 'Fuste', array( 'fusta', 'fuste' ) ),
			array( 'Șorturi', array( 'sort', 'sorturi', 'pantaloni scurti', 'bermude', 'shorts' ) ),
			array( 'Pantaloni și blugi', array( 'blug', 'jeans', 'pantalon', 'chino', 'leggings', 'colanti', 'treninguri' ) ),
			array( 'Cămăși', array( 'camasa', 'camasi', 'shirt' ) ),
			array( 'Tricouri și topuri', array( 'tricou', 'tricouri', 'polo', 'maiou', 'top ', 'bluza' ) ),
			array( 'Pijamale', array( 'pijama', 'pijamale' ) ),
			array( 'Body-uri', array( 'body' ) ),
			array( 'Costume de baie', array( 'costum de baie', 'slip de baie', 'bikini', 'costum baie', 'inot' ) ),
			array( 'Lenjerie', array( 'lenjerie', 'chilot', 'boxeri' ) ),
			// --- Accesorii ---
			array( 'Șepci și căciuli', array( 'sapca', 'caciula', 'palarie', 'bereta', 'fes', 'panama' ) ),
			array( 'Genți și rucsacuri', array( 'geanta', 'rucsac', 'ghiozdan', 'gentuta', 'borseta', 'penar', 'valiz' ) ),
			array( 'Șosete și ciorapi', array( 'sosete', 'ciorapi', 'dresuri', 'sosetes' ) ),
			array( 'Fulare și eșarfe', array( 'fular', 'esarfa', 'cache' ) ),
			array( 'Mănuși', array( 'manusi', 'manusa' ) ),
			array( 'Curele', array( 'curea', 'curele' ) ),
		)
	);
}

/**
 * Culori recunoscute (RO) — folosite la extragerea variantei de culoare din
 * titlu, comun tuturor surselor.
 */
function hainute_color_words() {
	return apply_filters(
		'hainute_color_words',
		array(
			'negru', 'alb', 'rosu', 'albastru', 'verde', 'roz', 'galben', 'gri', 'maro',
			'bleumarin', 'bej', 'mov', 'portocaliu', 'turcoaz', 'crem', 'bordo', 'kaki',
			'multicolor', 'visiniu', 'oliv', 'coral', 'fucsia', 'lila', 'argintiu', 'auriu',
			'grena', 'indigo', 'bleu', 'nude', 'somon', 'petrol', 'antracit', 'violet',
			'mustar', 'camel', 'ecru', 'lavanda', 'mentol', 'piersica', 'ciocolatiu', 'lime',
		)
	);
}

/**
 * Extrage eticheta de culoare dintr-un titlu (primul cuvânt-culoare, cu compuse
 * simple gen „alb murdar"). Întoarce '' dacă nu găsește.
 */
function hainute_extract_color( $name ) {
	$h = strtolower( remove_accents( wp_strip_all_tags( (string) $name ) ) );
	// „albastru marin" = bleumarin (altfel ar fi prins „albastru").
	if ( preg_match( '/albastru[\s-]+marin/', $h ) ) {
		return 'Bleumarin';
	}
	foreach ( hainute_color_words() as $c ) {
		if ( preg_match( '/\b' . preg_quote( $c, '/' ) . '\b/', $h ) ) {
			if ( preg_match( '/\b' . preg_quote( $c, '/' ) . '\s+(murdar|inchis|deschis|prafuit)\b/', $h, $m ) ) {
				return ucfirst( $c ) . ' ' . $m[1];
			}
			return ucfirst( $c );
		}
	}
	// Forme flexionate (plural/feminin), frecvente în URL-uri și titluri:
	// „sneakers albi", „cizme negre", „geaca albastra".
	$forms = array(
		'albi' => 'alb', 'albe' => 'alb', 'alba' => 'alb',
		'negri' => 'negru', 'negre' => 'negru', 'neagra' => 'negru',
		'rosii' => 'rosu', 'rosie' => 'rosu',
		'albastri' => 'albastru', 'albastre' => 'albastru', 'albastra' => 'albastru',
		'verzi' => 'verde',
		'galbeni' => 'galben', 'galbene' => 'galben', 'galbena' => 'galben',
		'argintii' => 'argintiu', 'argintie' => 'argintiu',
		'aurii' => 'auriu', 'aurie' => 'auriu',
		'portocalii' => 'portocaliu', 'portocalie' => 'portocaliu',
	);
	foreach ( $forms as $f => $base ) {
		if ( preg_match( '/\b' . $f . '\b/', $h ) ) {
			return ucfirst( $base );
		}
	}
	return '';
}

/**
 * Map a raw category path + product title to a clean canonical category.
 *
 * @param string $path  Store category path, e.g. "Sandale Nike Copii".
 * @param string $title Product title (helps when the path is unhelpful).
 * @return string Canonical category, or a cleaned leaf as fallback.
 */
function hainute_canonical_category( $path, $title = '', $brand = '' ) {
	$title_l = strtolower( remove_accents( wp_strip_all_tags( (string) $title ) ) );

	// Semnal PRIMAR: tipul din PRIMELE cuvinte ale titlului (produsele au forma
	// „{Tip} {Brand} {Model}" sau „{Brand} {Tip} {Model}"). Scoatem întâi BRANDUL,
	// altfel branduri ca „Calvin Klein Jeans" / „Polo Ralph Lauren" duc greșit
	// bocancii la „Pantaloni" / geaca la „Tricouri". Așa „Tricou Puma LITTLE RUNNERS"
	// rămâne tricou (nu „Pantofi sport" din cauza lui „runners" din model).
	$type_src = $title_l;
	$brand_l  = strtolower( remove_accents( wp_strip_all_tags( (string) $brand ) ) );
	if ( '' !== $brand_l ) {
		$type_src = trim( preg_replace( '/\s+/', ' ', str_replace( $brand_l, ' ', $title_l ) ) );
	}
	$lead = implode( ' ', array_slice( explode( ' ', trim( $type_src ) ), 0, 3 ) );
	if ( '' !== $lead ) {
		foreach ( hainute_category_rules() as $rule ) {
			list( $canonical, $keywords ) = $rule;
			foreach ( $keywords as $kw ) {
				if ( false !== strpos( $lead, $kw ) ) {
					return $canonical;
				}
			}
		}
	}

	// Fallback: haystack complet (titlu + path) — model + categorie magazin.
	$haystack = $title_l . ' ' . strtolower( remove_accents( (string) $path ) );

	foreach ( hainute_category_rules() as $rule ) {
		list( $canonical, $keywords ) = $rule;
		foreach ( $keywords as $kw ) {
			if ( false !== strpos( $haystack, $kw ) ) {
				return $canonical;
			}
		}
	}

	// Fallback: cleaned leaf of the path (strip brand noise and "copii" markers).
	$segments = array_values( array_filter( array_map( 'trim', explode( '/', (string) $path ) ) ) );
	$leaf     = $segments ? end( $segments ) : '';

	$leaf = preg_replace( '/\b(copii|copil|fete|baieti|baietei|unisex|bebe|bebelusi)\b/iu', '', $leaf );
	$leaf = trim( preg_replace( '/\s+/', ' ', $leaf ) );

	return '' !== $leaf ? $leaf : __( 'Diverse', 'hainute' );
}
