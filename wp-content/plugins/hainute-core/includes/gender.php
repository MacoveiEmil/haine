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
 * Arborele „Unisex" (oglindă după Băieți/Fete): Unisex › Încălțăminte › Adidași etc.
 * Creat o singură dată; categoriile goale nu apar în listări.
 */
function hainute_ensure_unisex_tree() {
	if ( get_option( 'hainute_unisex_tree_v1' ) ) {
		return;
	}
	if ( ! add_option( 'hainute_unisex_tree_lock', time(), '', false ) ) {
		return; // altă cerere îl creează deja
	}
	$top    = term_exists( 'unisex', 'product_cat' );
	$top_id = $top ? (int) $top['term_id'] : (int) wp_insert_term( 'Unisex', 'product_cat', array( 'slug' => 'unisex' ) )['term_id'];
	foreach ( array( 'fete', 'baieti' ) as $src ) {
		$s = get_term_by( 'slug', $src, 'product_cat' );
		if ( ! $s ) {
			continue;
		}
		foreach ( get_terms( array( 'taxonomy' => 'product_cat', 'parent' => $s->term_id, 'hide_empty' => false ) ) as $l1 ) {
			$base = preg_replace( '/-(fete|baieti)$/', '', $l1->slug );
			$ex   = term_exists( $base . '-unisex', 'product_cat' );
			$l1u  = $ex ? (int) $ex['term_id'] : (int) wp_insert_term( html_entity_decode( $l1->name ), 'product_cat', array( 'slug' => $base . '-unisex', 'parent' => $top_id ) )['term_id'];
			foreach ( get_terms( array( 'taxonomy' => 'product_cat', 'parent' => $l1->term_id, 'hide_empty' => false ) ) as $l2 ) {
				if ( hainute_cat_by_path( 'unisex', array( html_entity_decode( $l1->name ), html_entity_decode( $l2->name ) ) ) ) {
					continue;
				}
				$leaf = preg_replace( '/^(baieti|fete)-(incaltaminte|imbracaminte|accesorii)-|^(incaltaminte|imbracaminte)-/', '', $l2->slug );
				wp_insert_term( html_entity_decode( $l2->name ), 'product_cat', array( 'slug' => 'unisex-' . $base . '-' . $leaf, 'parent' => $l1u ) );
			}
		}
	}
	update_option( 'hainute_unisex_tree_v1', 1 );
}
add_action( 'init', 'hainute_ensure_unisex_tree', 25 );

/** Cuvântul de gen din titlu: „Fete", „Băieți", „Unisex". */
function hainute_gender_word( $g ) {
	$w = array( 'fete' => 'Fete', 'baieti' => 'Băieți', 'unisex' => 'Unisex' );
	return $w[ $g ] ?? '';
}

/**
 * Aplică genul (fete / baieti / unisex) pe produs: categoria în arborele
 * corespunzător, titlul, genul și linkurile din descriere. Întoarce ce s-a mutat.
 * Bebe nu se mută (după vârstă): primește doar genul (unisex = ambele).
 */
function hainute_apply_merchant_gender( $pid ) {
	$g = (string) get_post_meta( $pid, '_hainute_merchant_gender', true );
	if ( ! in_array( $g, array( 'fete', 'baieti', 'unisex' ), true ) ) {
		return '';
	}
	$genders = 'unisex' === $g ? array( 'fete', 'baieti' ) : array( $g );
	$cats    = wp_get_object_terms( $pid, 'product_cat' );
	$tops    = array();
	foreach ( $cats as $c ) {
		list( $top ) = hainute_cat_path_names( $c->term_id );
		$tops[ $top ] = 1;
	}
	if ( isset( $tops['bebe'] ) ) {
		wp_set_object_terms( $pid, $genders, 'product_gender', false );
		return '';
	}

	$new   = array();
	$urls  = array();
	$moved = '';
	foreach ( $cats as $c ) {
		list( $top, $names ) = hainute_cat_path_names( $c->term_id );
		if ( $top === $g || ! in_array( $top, array( 'fete', 'baieti', 'unisex' ), true ) ) {
			$new[] = (int) $c->term_id;
			continue;
		}
		$target = hainute_cat_by_path( $g, $names );
		if ( ! $target ) {
			return ''; // fără echivalent sigur: nu mutăm
		}
		$moved     = $top;
		$new[]     = (int) $target->term_id;
		$old_chain = array_merge( array( $c->term_id ), get_ancestors( $c->term_id, 'product_cat' ) );
		$new_chain = array_merge( array( $target->term_id ), get_ancestors( $target->term_id, 'product_cat' ) );
		foreach ( $old_chain as $i => $oid ) {
			if ( isset( $new_chain[ $i ] ) ) {
				$urls[ wp_make_link_relative( get_term_link( (int) $oid, 'product_cat' ) ) ] = wp_make_link_relative( get_term_link( (int) $new_chain[ $i ], 'product_cat' ) );
			}
		}
	}
	if ( $moved ) {
		wp_set_object_terms( $pid, array_unique( $new ), 'product_cat', false );
	}
	wp_set_object_terms( $pid, $genders, 'product_gender', false );

	// Titlul: cuvântul de gen al categoriei („Fete" / „Băieți" / „Unisex"); dacă
	// lipsește, îl punem după brand („Adidași Geox Unisex …").
	$title = get_the_title( $pid );
	$word  = hainute_gender_word( $g );
	if ( preg_match( '/\b(Fete|Băieți|Unisex)\b/u', $title ) ) {
		$new_t = preg_replace( '/\b(Fete|Băieți|Unisex)\b/u', $word, $title, 1 );
	} else {
		$bt    = get_the_terms( $pid, 'product_brand' );
		$brand = $bt && ! is_wp_error( $bt ) ? html_entity_decode( $bt[0]->name ) : '';
		$pos   = $brand ? mb_stripos( $title, $brand ) : false;
		$new_t = false !== $pos ? mb_substr( $title, 0, $pos + mb_strlen( $brand ) ) . ' ' . $word . mb_substr( $title, $pos + mb_strlen( $brand ) ) : $title;
	}

	$content = (string) get_post_field( 'post_content', $pid );
	$fixed   = hainute_fix_content_cat_links( $pid, $content );
	if ( $new_t !== $title || $fixed !== $content ) {
		wp_update_post( array( 'ID' => $pid, 'post_title' => $new_t, 'post_content' => $fixed ) );
	}
	if ( $moved ) {
		$log   = (array) get_post_meta( $pid, '_hainute_gender_fix', true );
		$log[] = array( 'time' => time(), 'from' => $moved, 'to' => $g, 'title' => $title );
		update_post_meta( $pid, '_hainute_gender_fix', $log );
		return "$moved → $g";
	}
	return '';
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
	if ( ! $tg && 'unisex' !== $g ) {
		$g = 'unisex'; // câmpul magazinului fără confirmare în titlu nu e destul: unisex
	}
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

/**
 * Linkurile spre categorii din descriere urmează arborele produsului (Fete /
 * Băieți / Unisex): un link spre alt arbore se mută la categoria echivalentă, cu
 * ancora corectată („pentru fete" → „unisex"); un link spre o categorie care nu
 * mai există trece la categoria de nivel 2 a produsului (altfel ar fi 404).
 */
function hainute_fix_content_cat_links( $pid, $content ) {
	$cats = wp_get_object_terms( $pid, 'product_cat' );
	if ( ! $cats ) {
		return $content;
	}
	$leaf = $cats[0];
	foreach ( $cats as $c ) {
		if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
			$leaf = $c;
		}
	}
	list( $g ) = hainute_cat_path_names( $leaf->term_id );
	$anc  = get_ancestors( $leaf->term_id, 'product_cat' );
	$lvl2 = count( $anc ) >= 2 ? get_term( $anc[ count( $anc ) - 2 ], 'product_cat' ) : $leaf;
	$gw   = array( 'fete' => 'fete', 'baieti' => 'băieți' );
	return preg_replace_callback(
		'#<a([^>]*?)href="(?:https?://[^/"]+)?/categorie/([^/"]+)/?"([^>]*)>(.*?)</a>#u',
		function ( $m ) use ( $g, $lvl2, $gw ) {
			$term = get_term_by( 'slug', $m[2], 'product_cat' );
			$t    = $m[4];
			if ( ! $term ) {
				$term = $lvl2;
				$t    = preg_replace( '/\b(pentru )?(fete|băieți|unisex)\b/u', 'unisex' === $g ? 'unisex' : 'pentru ' . ( $gw[ $g ] ?? $g ), $t );
			} else {
				list( $top, $names ) = hainute_cat_path_names( $term->term_id );
				if ( $top !== $g && in_array( $top, array( 'fete', 'baieti', 'unisex' ), true ) && in_array( $g, array( 'fete', 'baieti', 'unisex' ), true ) ) {
					$eq = $names ? hainute_cat_by_path( $g, $names ) : get_term_by( 'slug', $g, 'product_cat' );
					if ( ! $eq ) {
						return $m[0];
					}
					$term = $eq;
					if ( 'unisex' === $g ) {
						$t = preg_replace( '/\bpentru (fete|băieți)\b/u', 'unisex', $t );
						$t = preg_replace( '/\b(fete|băieți)\b/u', 'unisex', $t );
					} else {
						$t = preg_replace( '/\bunisex\b/u', 'pentru ' . $gw[ $g ], $t );
						$t = preg_replace( '/\b(fete|băieți)\b/u', $gw[ $g ], $t );
						$t = str_replace( 'pentru pentru ', 'pentru ', $t );
					}
				}
			}
			return '<a' . $m[1] . 'href="' . esc_url( wp_make_link_relative( get_term_link( $term ) ) ) . '"' . $m[3] . '>' . $t . '</a>';
		},
		$content
	);
}

/**
 * Produs fără niciun semnal de gen de la magazin (încă necrawluit, Sportisimo,
 * FD/vb neconfirmat): Unisex, nu genul din feed (feed-ul a greșit la ~275 de
 * produse). Prima verificare Answear care confirmă fete/băieți îl mută.
 */
function hainute_default_unisex( $pid ) {
	if ( get_post_meta( $pid, '_hainute_merchant_gender', true ) || 'publish' !== get_post_status( $pid ) ) {
		return;
	}
	foreach ( wp_get_object_terms( $pid, 'product_cat' ) as $c ) {
		list( $top ) = hainute_cat_path_names( $c->term_id );
		if ( 'bebe' === $top ) {
			return;
		}
	}
	// Numele modelului poate spune genul („FLANFIL GIRL", „… BOYS"): semnal sigur.
	$name = ' ' . mb_strtolower( remove_accents( preg_replace( '/\b(Fete|Băieți|Unisex)\b/u', '', get_the_title( $pid ) ) ) ) . ' ';
	$f    = preg_match( '/\b(girl|girls|fetite|fetita)\b/u', $name );
	$b    = preg_match( '/\b(boy|boys|baietei|baiat)\b/u', $name );
	$g    = $f && ! $b ? 'fete' : ( $b && ! $f ? 'baieti' : 'unisex' );
	update_post_meta( $pid, '_hainute_merchant_gender', $g );
	update_post_meta( $pid, '_hainute_gender_source', 'unisex' === $g ? 'fara-semnal' : 'nume-model' );
	hainute_apply_merchant_gender( $pid );
}

