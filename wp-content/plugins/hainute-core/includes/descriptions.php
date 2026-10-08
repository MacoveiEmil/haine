<?php
/**
 * Generator de descrieri din datele structurate ale produsului.
 *
 * Multe produse (mai ales various-brands) n-au descriere în feed → pagina „Descriere"
 * e goală, slab pt SEO. Aici compunem o descriere UNICĂ per produs din brand,
 * categorie, gen, culori, mărimi, material, preț și magazine — cu variație (șabloane
 * rotite după ID) ca să nu fie boilerplate identic (risc de conținut duplicat).
 * Se scrie DOAR unde lipsește descriere reală, ca să nu suprascriem feed-ul.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Caption pentru Facebook/Instagram dintr-un produs (brand, tip, preț, magazine,
 * link, hashtag-uri). Pentru planul automat de postări.
 */
function hainute_social_caption( $pid ) {
	$pid   = (int) $pid;
	$brand = hainute_desc_term( $pid, 'product_brand' );
	$title = get_the_title( $pid );
	$type  = '';
	if ( $brand && false !== mb_stripos( $title, $brand ) ) {
		$type = trim( mb_substr( $title, 0, mb_stripos( $title, $brand ) ), " -–,·|" );
	}
	if ( '' === $type ) {
		$type = hainute_desc_term( $pid, 'product_cat' );
	}

	$stores = array();
	$min    = 0;
	if ( function_exists( 'hainute_get_offers' ) ) {
		foreach ( hainute_get_offers( $pid ) as $o ) {
			if ( $o->store ) {
				$stores[ $o->store->name ] = 1;
			}
			if ( 'out_of_stock' !== $o->stock_status && $o->price > 0 && ( 0 === $min || $o->price < $min ) ) {
				$min = (float) $o->price;
			}
		}
	}
	$n = count( $stores );

	$emoji = array( 'incalt' => '👟', 'pantof' => '👟', 'sandal' => '👡', 'ghet' => '🥾', 'tricou' => '👕', 'bluz' => '👕', 'geac' => '🧥', 'rochi' => '👗', 'pantalon' => '👖', 'sapc' => '🧢', 'geant' => '🎒' );
	$ico = '🧒';
	foreach ( $emoji as $k => $e ) {
		if ( false !== mb_stripos( $type . $title, $k ) ) {
			$ico = $e;
			break;
		}
	}

	$lines   = array();
	$lines[] = $ico . ' ' . trim( ucfirst( mb_strtolower( $type ) ) . ( $brand ? ' ' . $brand : '' ) ) . ' pentru copii';
	if ( $n >= 2 ) {
		$lines[] = '📏 Mărimi disponibile la ' . $n . ' magazine' . ( $min ? ' · de la ' . number_format_i18n( $min, 0 ) . ' lei' : '' );
	} elseif ( $min ) {
		$lines[] = '💰 De la ' . number_format_i18n( $min, 0 ) . ' lei';
	}
	$lines[] = '👉 ' . get_permalink( $pid );
	$tag     = '#hainutecopii #modacopii #copii';
	if ( $brand ) {
		$tag .= ' #' . preg_replace( '/[^a-z0-9]/', '', strtolower( remove_accents( $brand ) ) );
	}
	$lines[] = $tag;
	return implode( "\n", $lines );
}

/** Prima etichetă de taxonomie sau ''. */
function hainute_desc_term( $pid, $tax ) {
	$t = get_the_terms( $pid, $tax );
	return ( $t && ! is_wp_error( $t ) ) ? $t[0]->name : '';
}

/** Alege determinist un element din listă, după ID (variație stabilă). */
function hainute_desc_pick( $pid, $arr ) {
	return $arr[ abs( crc32( 'd' . $pid ) ) % count( $arr ) ];
}

/**
 * Compune o descriere RO din datele produsului. Întoarce '' dacă n-are destule date.
 */
function hainute_compose_description( $pid ) {
	$pid    = (int) $pid;
	$title  = get_the_title( $pid );
	$brand  = hainute_desc_term( $pid, 'product_brand' );
	$cat    = hainute_desc_term( $pid, 'product_cat' );
	$gender = hainute_desc_term( $pid, 'product_age' ) ?: hainute_desc_term( $pid, 'product_gender' );
	$mat    = (string) get_post_meta( $pid, '_hainute_materials', true );
	if ( '' === $mat ) {
		$mat = (string) get_post_meta( $pid, '_hainute_material', true );
	}
	$mat    = trim( explode( ',', $mat )[0] );
	$colors = array_filter( array_map( 'trim', explode( ',', (string) get_post_meta( $pid, '_hainute_colors', true ) ) ) );

	$sizes = array();
	if ( function_exists( 'hainute_resolve_sizes' ) ) {
		$sizes = hainute_resolve_sizes( $pid )['labels'];
	}

	// Magazine + preț min.
	$stores = array();
	$min    = 0;
	if ( function_exists( 'hainute_get_offers' ) ) {
		foreach ( hainute_get_offers( $pid ) as $o ) {
			$nm = $o->store ? $o->store->name : '';
			if ( $nm ) {
				$stores[ $nm ] = 1;
			}
			if ( 'out_of_stock' !== $o->stock_status && $o->price > 0 && ( 0 === $min || $o->price < $min ) ) {
				$min = (float) $o->price;
			}
		}
	}
	$stores  = array_keys( $stores );
	$n_store = count( $stores );

	// Tipul articolului: preferă prefixul din TITLU (ex. „Tricou Puma …" → „Tricou"),
	// mai sigur decât categoria (uneori greșită, ex. haine puse în „Pantofi sport").
	$type = '';
	if ( $brand && false !== mb_stripos( $title, $brand ) ) {
		$type = trim( mb_substr( $title, 0, mb_stripos( $title, $brand ) ) );
	}
	$type = trim( $type, " -–,·|" );
	if ( '' === $type || mb_strlen( $type ) > 28 ) {
		$type = $cat; // fallback pe categorie
	}
	$cat_l = $type ? mb_strtolower( $type ) : 'articol';
	$who   = $gender ? mb_strtolower( $gender ) : 'copii';
	if ( false === mb_strpos( $who, 'copii' ) && false === mb_strpos( $who, 'ani' ) && false === mb_strpos( $who, 'bebe' ) && ! in_array( $who, array( 'fete', 'băieți', 'baieti', 'unisex' ), true ) ) {
		$who = 'copii';
	}

	// 1) Fraza de deschidere (variată).
	$openers = array();
	if ( $brand ) {
		$openers[] = sprintf( '%s %s pentru %s, din colecția %s.', ucfirst( $cat_l ), $brand, $who, $brand );
		$openers[] = sprintf( '%s de la %s, pentru %s.', ucfirst( $cat_l ), $brand, $who );
		$openers[] = sprintf( '%s pentru %s, semnat %s.', ucfirst( $cat_l ), $who, $brand );
	} else {
		$openers[] = sprintf( '%s pentru %s.', ucfirst( $cat_l ), $who );
	}
	$out = hainute_desc_pick( $pid, $openers );

	// 2) Material.
	if ( $mat ) {
		$out .= ' ' . hainute_desc_pick( $pid, array(
			sprintf( 'Confecționat din %s.', mb_strtolower( $mat ) ),
			sprintf( 'Material: %s.', mb_strtolower( $mat ) ),
		) );
	}

	// 2b) Caracteristici reale extrase din pagina magazinului (specscrawl).
	$feat = get_post_meta( $pid, '_hainute_features', true );
	if ( is_array( $feat ) && ! empty( $feat ) ) {
		$pick = array_slice( array_map( 'mb_strtolower', $feat ), 0, 3 );
		$out .= ' ' . hainute_desc_pick( $pid, array(
			sprintf( 'Printre atuuri: %s.', implode( ', ', $pick ) ),
			sprintf( 'Are %s.', implode( ', ', $pick ) ),
			sprintf( 'Detalii care contează: %s.', implode( ', ', $pick ) ),
		) );
	}

	// 3) Culori + mărimi.
	$opt = array();
	if ( ! empty( $colors ) ) {
		$opt[] = ( count( $colors ) > 1 ? 'culorile ' : 'culoarea ' ) . mb_strtolower( implode( ', ', array_slice( $colors, 0, 4 ) ) );
	}
	if ( ! empty( $sizes ) ) {
		if ( count( $sizes ) > 1 ) {
			$opt[] = 'mărimile de la ' . $sizes[0] . ' la ' . end( $sizes );
		} else {
			$opt[] = 'mărimea ' . $sizes[0];
		}
	}
	if ( $opt ) {
		$out .= ' ' . sprintf( 'Disponibil în %s.', implode( ' și ', $opt ) );
	}

	// 4) Trimitere spre lista de magazine. FĂRĂ preț, nume sau număr de magazine:
	// se schimbă zilnic și textul ar deveni fals (sunt afișate live în listă).
	$tails = hainute_desc_stable_tails();
	$out  .= ' ' . $tails[ $pid % count( $tails ) ];

	// Nevoie de minim: un titlu/brand + ceva concret.
	if ( '' === $brand && empty( $colors ) && empty( $sizes ) ) {
		return '';
	}
	// Fără em/en-dash oriunde, plus interlink-uri interne (categorie + subcategorie + brand).
	$out = str_replace( array( '—', '–' ), array( ',', '-' ), $out );
	return '<p>' . trim( $out ) . '</p>' . hainute_desc_interlinks( $pid );
}

/**
 * Pool de ~50 de formulări pentru trimiterea către categoria-mamă. {cat} = linkul de
 * categorie, {tip} = tipul de produs la plural (geci și jachete, adidași...). Alese
 * determinist după ID → variază produs cu produs, ca să nu se repete la scară.
 */
function hainute_cat_link_pool() {
	return array(
		'Modelul stă în {cat}, alături de alte {tip}.',
		'În {cat} găsești și alte {tip} de sezon.',
		'Face parte din {cat}, lângă modele asemănătoare.',
		'Dacă vrei mai multe opțiuni, vezi toată {cat}.',
		'Apare în {cat}, printre alte {tip} pentru copii.',
		'Răsfoiește {cat} pentru variante apropiate.',
		'Stă bine în {cat}, alături de {tip} similare.',
		'E una dintre piesele din {cat}.',
		'Găsești produsul în {cat}, lângă alte {tip}.',
		'Dacă vrei și alte modele, aruncă un ochi pe {cat}.',
		'Se încadrează în {cat}, printre modele de aceeași factură.',
		'Alte {tip} din aceeași familie sunt în {cat}.',
		'Vezi restul din {cat} dacă vrei să alegi în cunoștință de cauză.',
		'Mai multe {tip} găsești în {cat}.',
		'Dă o tură prin {cat} pentru și mai multe idei.',
		'Modelul completează selecția din {cat}.',
		'În {cat} sunt și alte {tip} de care merită să ții cont.',
		'Se găsește lângă {tip} similare, în {cat}.',
		'Ai și alte variante în {cat}, dacă vrei să mai cauți.',
		'Apare în {cat}, alături de piese pentru sezonul rece.',
		'Vezi ce alte modele găsești în {cat}.',
		'Pentru mai multe {tip}, deschide {cat}.',
		'Stă în {cat}, printre modele din aceeași categorie.',
		'Găsești și alternative în {cat}.',
		'Produsul e listat în {cat}, lângă alte {tip}.',
		'Merită văzut alături de restul din {cat}.',
		'În {cat} descoperi și alte {tip} potrivite.',
		'Aruncă o privire în {cat} pentru variante apropiate.',
		'Se regăsește în {cat}, alături de modele asemănătoare.',
		'Alte alegeri bune sunt în {cat}.',
		'Produsul face parte din {cat}, lângă {tip} de sezon.',
		'Vezi mai multe {tip} în {cat}.',
		'Modelul stă alături de {tip} similare, în {cat}.',
		'Găsești produsul în {cat}, printre alte {tip} pentru copii.',
		'E o opțiune din {cat}, lângă modele apropiate.',
		'Pentru și mai multe variante, deschide {cat}.',
		'Alte {tip} similare te așteaptă în {cat}.',
		'Apare în {cat}, printre piese pentru zilele reci.',
		'Vezi ce alte {tip} sunt în {cat}.',
		'Completează {cat}, lângă modele asemănătoare.',
		'Dacă tot cauți, treci și prin {cat}.',
		'Face parte din selecția de {tip} din {cat}.',
		'Stă în {cat}, aproape de {tip} din aceeași gamă.',
		'Găsești variante și în {cat}.',
		'E listat în {cat}, printre {tip} de sezon.',
		'Pentru mai multe variante, deschide {cat}.',
		'Alte {tip} bune sunt în {cat}, merită o privire.',
		'În {cat} ai de unde alege, dacă vrei să pui față în față mai multe modele.',
		'Se așază firesc în {cat}, lângă alte {tip}.',
		'Îl vezi ușor alături de ce mai e în {cat}.',
		'Găsești produsul, plus alte {tip}, în {cat}.',
		'Rămâne o alegere bună din {cat}.',
	);
}

/** Pool pentru linkul de brand. {brand} = linkul de brand. */
function hainute_brand_link_pool() {
	return array(
		'Vezi și restul modelelor {brand}.',
		'{brand} are și alte piese pentru copii.',
		'Descoperă toată gama {brand}.',
		'Mai multe modele {brand} sunt pe pagina brandului.',
		'Aruncă un ochi și pe restul gamei {brand}.',
		'{brand} vine cu mai multe variante, merită văzute.',
		'Restul colecției {brand} e la un click distanță.',
		'Dacă îți place brandul, vezi tot ce are {brand}.',
		'Mai multe de la {brand} găsești aici.',
		'Explorează și celelalte modele {brand}.',
		'Vezi ce mai propune {brand} pentru cei mici.',
		'Toată gama {brand} e pe pagina de brand.',
	);
}

/**
 * Trimitere naturală către categoria-mamă (grupă + gen) + brand, cu formulare
 * aleasă din pool după ID (variază la scară). Exact două linkuri (v2).
 */
function hainute_desc_interlinks( $pid ) {
	$cats = get_the_terms( $pid, 'product_cat' );
	if ( ! $cats || is_wp_error( $cats ) ) {
		return '';
	}
	$leaf = $cats[0];
	foreach ( $cats as $c ) {
		if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
			$leaf = $c;
		}
	}
	$anc   = get_ancestors( $leaf->term_id, 'product_cat' );
	$grupa = ! empty( $anc ) ? get_term( $anc[0], 'product_cat' ) : null;
	$gen   = ! empty( $anc ) ? get_term( end( $anc ), 'product_cat' ) : null;
	if ( ! $grupa || is_wp_error( $grupa ) ) {
		return '';
	}
	$anchor  = mb_strtolower( html_entity_decode( $grupa->name ) ) . ( $gen && ! is_wp_error( $gen ) ? ' pentru ' . mb_strtolower( html_entity_decode( $gen->name ) ) : '' );
	$cat_html = '<a href="' . esc_url( get_term_link( $grupa ) ) . '">' . esc_html( $anchor ) . '</a>';
	$leafname = mb_strtolower( str_replace( ' & ', ' și ', html_entity_decode( $leaf->name ) ) );
	$tip = $leafname ? 'modele de ' . $leafname : 'modele';

	$cpool = hainute_cat_link_pool();
	$cat_sentence = str_replace( array( '{cat}', '{tip}' ), array( $cat_html, $tip ), $cpool[ $pid % count( $cpool ) ] );

	$out = $cat_sentence;
	$brand = hainute_desc_term( $pid, 'product_brand' );
	if ( $brand ) {
		$bt = get_term_by( 'name', $brand, 'product_brand' );
		if ( $bt && ! is_wp_error( $bt ) ) {
			$brand_html = '<a href="' . esc_url( get_term_link( $bt ) ) . '">' . esc_html( $brand ) . '</a>';
			$bpool = hainute_brand_link_pool();
			$out  .= ' ' . str_replace( '{brand}', $brand_html, $bpool[ $pid % count( $bpool ) ] );
		}
	}
	return '<p class="product-interlinks">' . $out . '</p>';
}

/** Fraze stabile (nu se învechesc) care trimit spre lista de magazine. */
function hainute_desc_stable_tails() {
	return array(
		'Mărimile disponibile și stocul la fiecare magazin le vezi mai sus, actualizate periodic.',
		'În lista de magazine de mai sus vezi pe ce mărimi e disponibil acum.',
		'Alege mărimea de mai sus și vezi imediat la ce magazin o găsești.',
		'Disponibilitatea pe fiecare mărime o găsești în lista de magazine de mai sus.',
		'Pe ce mărimi e în stoc și unde, vezi mai sus, în lista de magazine.',
		'Selectează mărimea copilului mai sus și vezi unde e pe stoc.',
	);
}
