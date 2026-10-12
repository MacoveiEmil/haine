<?php
/**
 * Genul produsului după MAGAZIN (sursa de adevăr), nu după feed.
 *
 * Feed-urile dau des genul greșit sau deloc (ex. sneakerși de fete importați la
 * „Băieți"). Crawlerul citește genul de pe pagina magazinului (Answear: `sex`
 * G = fete, B = băieți, K = unisex) și îl trimite la /crawl-result. Aici:
 *  - fete / băieți diferit de categoria noastră → mutăm produsul în categoria
 *    echivalentă din celălalt arbore (Băieți › Încălțăminte › Adidași →
 *    Fete › Încălțăminte › Adidași), corectăm titlul, genul și linkurile din descriere;
 *  - unisex → produsul primește ambele genuri (apare la filtrele Fete și Băieți),
 *    categoria rămâne;
 *  - produsele din „Bebe" nu se mută (acolo contează vârsta, nu genul).
 * Fiecare mutare se notează în `_hainute_gender_fix` (de unde, când), pentru audit.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Codul de gen al magazinului → genul nostru. */
function hainute_merchant_gender_from_code( $code ) {
	$map = array( 'G' => 'fete', 'B' => 'baieti', 'K' => 'unisex', 'U' => 'unisex' );
	$code = strtoupper( trim( (string) $code ) );
	return $map[ $code ] ?? '';
}

/** Lanțul de nume de sub categoria de top: [Încălțăminte, Adidași]. */
function hainute_cat_path_names( $term_id ) {
	$anc   = array_reverse( get_ancestors( $term_id, 'product_cat' ) );
	$top   = $anc ? get_term( array_shift( $anc ), 'product_cat' ) : get_term( $term_id, 'product_cat' );
	$names = array();
	foreach ( $anc as $a ) {
		$names[] = html_entity_decode( get_term( $a, 'product_cat' )->name );
	}
	if ( $top && (int) $top->term_id !== (int) $term_id ) {
		$names[] = html_entity_decode( get_term( $term_id, 'product_cat' )->name );
	}
	return array( $top ? $top->slug : '', $names );
}

/** Categoria cu același lanț de nume sub alt top (fete / baieti), sau null. */
function hainute_cat_by_path( $top_slug, array $names ) {
	$top = get_term_by( 'slug', $top_slug, 'product_cat' );
	if ( ! $top ) {
		return null;
	}
	$parent = (int) $top->term_id;
	foreach ( $names as $name ) {
		$found = null;
		foreach ( get_terms( array( 'taxonomy' => 'product_cat', 'parent' => $parent, 'hide_empty' => false ) ) as $t ) {
			if ( mb_strtolower( html_entity_decode( $t->name ) ) === mb_strtolower( $name ) ) {
				$found = $t;
				break;
			}
		}
		if ( ! $found ) {
			return null;
		}
		$parent = (int) $found->term_id;
	}
	return get_term( $parent, 'product_cat' );
}

/**
 * Aplică genul magazinului pe produs. Întoarce ce s-a schimbat (pentru log).
 */
function hainute_apply_merchant_gender( $pid ) {
	$g = (string) get_post_meta( $pid, '_hainute_merchant_gender', true );
	if ( ! in_array( $g, array( 'fete', 'baieti', 'unisex' ), true ) ) {
		return '';
	}
	$cats = wp_get_object_terms( $pid, 'product_cat' );
	$tops = array();
	foreach ( $cats as $c ) {
		list( $top ) = hainute_cat_path_names( $c->term_id );
		$tops[ $top ] = 1;
	}
	if ( isset( $tops['bebe'] ) ) {
		return ''; // Bebe: după vârstă, nu după gen
	}
	if ( 'unisex' === $g ) {
		wp_set_object_terms( $pid, array( 'fete', 'baieti' ), 'product_gender', false );
		return '';
	}
	$from = 'fete' === $g ? 'baieti' : 'fete';
	if ( ! isset( $tops[ $from ] ) ) {
		wp_set_object_terms( $pid, array( $g ), 'product_gender', false );
		return ''; // deja în arborele corect
	}

	// Mutarea categoriilor + harta linkurilor vechi → noi (pentru descriere).
	$new  = array();
	$urls = array();
	foreach ( $cats as $c ) {
		list( $top, $names ) = hainute_cat_path_names( $c->term_id );
		if ( $top !== $from ) {
			$new[] = (int) $c->term_id;
			continue;
		}
		$target = hainute_cat_by_path( $g, $names );
		if ( ! $target ) {
			return ''; // fără echivalent sigur: nu mutăm (rămâne pentru verificare manuală)
		}
		$new[] = (int) $target->term_id;
		// toți strămoșii: /categorie/incaltaminte-baieti/ → /categorie/incaltaminte-fete/ etc.
		$old_chain = array_merge( array( $c->term_id ), get_ancestors( $c->term_id, 'product_cat' ) );
		$new_chain = array_merge( array( $target->term_id ), get_ancestors( $target->term_id, 'product_cat' ) );
		foreach ( $old_chain as $i => $oid ) {
			if ( isset( $new_chain[ $i ] ) ) {
				$urls[ wp_make_link_relative( get_term_link( (int) $oid, 'product_cat' ) ) ] = wp_make_link_relative( get_term_link( (int) $new_chain[ $i ], 'product_cat' ) );
			}
		}
	}
	wp_set_object_terms( $pid, array_unique( $new ), 'product_cat', false );
	wp_set_object_terms( $pid, array( $g ), 'product_gender', false );

	// Titlul: „Adidași Geox Băieți …" → „Adidași Geox Fete …".
	$words = array( 'baieti' => 'Băieți', 'fete' => 'Fete' );
	$title = get_the_title( $pid );
	$new_t = preg_replace( '/\b' . preg_quote( $words[ $from ], '/' ) . '\b/u', $words[ $g ], $title );

	// Descrierea: linkurile spre categorii + ancorele lor („băieți" → „fete").
	$content = (string) get_post_field( 'post_content', $pid );
	$content = strtr( $content, $urls );
	$content = preg_replace_callback(
		'#(<a[^>]+href="/categorie/[^"]*"[^>]*>)(.*?)(</a>)#u',
		function ( $m ) use ( $from, $g ) {
			$swap = 'fete' === $g ? array( 'băieți' => 'fete', 'Băieți' => 'Fete' ) : array( 'fete' => 'băieți', 'Fete' => 'Băieți' );
			return $m[1] . strtr( $m[2], $swap ) . $m[3];
		},
		$content
	);
	wp_update_post( array( 'ID' => $pid, 'post_title' => $new_t, 'post_content' => $content ) );

	$log   = (array) get_post_meta( $pid, '_hainute_gender_fix', true );
	$log[] = array( 'time' => time(), 'from' => $from, 'to' => $g, 'title' => $title );
	update_post_meta( $pid, '_hainute_gender_fix', $log );
	return "$from → $g";
}

/** Genul din titlul de la magazin („… pentru băieți", Nike „G NSW …"), sau ''. */
function hainute_gender_from_title( $title ) {
	$t = ' ' . mb_strtolower( remove_accents( (string) $title ) ) . ' ';
	$f = preg_match( '/\b(fete|fetite|fetita|girls?)\b/u', $t );
	$b = preg_match( '/\b(baieti|baietei|baiat|boys?)\b/u', $t );
	// Nike / Jordan: „G NSW", „JDG" = fete; „B NSW", „JDB" = băieți.
	if ( ! $f && ! $b && preg_match( '/\b(nike|jordan)\b/u', $t ) ) {
		$f = preg_match( '/\s(g|jdg)\s/u', $t );
		$b = preg_match( '/\s(b|jdb)\s/u', $t );
	}
	if ( $f && ! $b ) {
		return 'fete';
	}
	if ( $b && ! $f ) {
		return 'baieti';
	}
	return '';
}

/**
* Din rezultatele FashionDays / various-brands: câmpul de gen al magazinului NU e
* de încredere singur (am găsit „Gen: Baieti" la o jachetă Nike „G" de fete și
* calea „FETE" la o vestă „pentru băieți"). Mutăm doar dacă titlul confirmă;
* dacă se contrazic, notăm conflictul pentru verificare manuală.
*/
function hainute_take_merchant_gender( $pid, $b ) {
	$g = strtolower( remove_accents( (string) ( $b['gender'] ?? '' ) ) );
	if ( ! in_array( $g, array( 'fete', 'baieti', 'unisex' ), true ) ) {
		return;
	}
	$tg = hainute_gender_from_title( $b['title'] ?? '' );
	if ( 'unisex' === $g || ( $tg && $tg === $g ) ) {
		update_post_meta( $pid, '_hainute_merchant_gender', $g );
		delete_post_meta( $pid, '_hainute_gender_conflict' );
		hainute_apply_merchant_gender( $pid );
	} elseif ( $tg && $tg !== $g ) {
		// Conflict câmp ↔ titlu: titlul produsului e mai specific („Geacă pentru
		// băieți" vs. calea „FETE"), deci el decide. Notăm conflictul pentru audit.
		update_post_meta( $pid, '_hainute_gender_conflict', array( 'camp' => $g, 'titlu' => $tg, 'title' => (string) $b['title'], 'time' => time() ) );
		update_post_meta( $pid, '_hainute_merchant_gender', $tg );
		hainute_apply_merchant_gender( $pid );
	}
}

