<?php
/**
 * Cross-store product matching.
 *
 * The affiliate feeds do NOT populate GTIN/EAN, and each store uses its own
 * SKU, so there is no shared hard identifier. We match on brand + name:
 *
 * 1. Normalized match key = name tokens, lowercased, no diacritics, filler
 *    words removed, deduped and sorted (robust to word reordering).
 * 2. Exact key match (same normalized brand) → same aggregated product.
 * 3. Fuzzy fallback GATED ON SAME BRAND: brand is reliable in the feeds, so
 *    requiring an exact brand match lets us use a looser name threshold safely
 *    (a Calvin Klein "set trening" and "compleu trening" merge; a Calvin Klein
 *    and a Nike never do). Similarity = max(character similarity, token
 *    overlap) so synonyms/word swaps still score high.
 * 4. Brandless products fall back to the old stricter all-keys fuzzy.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

const HAINUTE_MATCH_META_KEY   = '_hainute_match_key';
const HAINUTE_MATCH_META_BRAND = '_hainute_match_brand';

/** Same-brand fuzzy threshold (%) — safe to keep low thanks to the brand gate. */
const HAINUTE_MATCH_BRANDED = 78;
/** Brandless fuzzy threshold (%) — stricter, no brand gate to protect us. */
const HAINUTE_MATCH_AUTO    = 85;
/** Below-threshold band worth logging as an "almost match". */
const HAINUTE_MATCH_NEAR    = 70;

/**
 * Words that differ between retailers without changing product identity.
 */
function hainute_match_stopwords() {
	return apply_filters(
		'hainute_match_stopwords',
		array(
			'pentru', 'copii', 'copil', 'bebe', 'bebelusi', 'bebelus', 'fete', 'fetite',
			'baieti', 'baietei', 'baiat', 'fata', 'unisex', 'de', 'cu', 'si', 'la', 'din', 'in',
			'model', 'nou', 'noua', 'original', 'originala', 'set',
		)
	);
}

/**
 * Product-TYPE words — the "what it is" (shoe, jacket…), removed from the match
 * key so what remains is essentially brand + model. Two stores describe the
 * same shoe with different type words ("pantofi sport" vs "adidasi"), but the
 * model name ("Runfalcon 3.0") is the same — that is what we match on.
 * Removing types is also what makes the distinctive-anchor rule safe: after
 * this, a shared long token is a model name, not a category word.
 */
function hainute_type_words() {
	return apply_filters(
		'hainute_type_words',
		array(
			// încălțăminte
			'pantofi', 'pantof', 'sport', 'sneakers', 'sneaker', 'adidasi', 'adidas',
			'tenisi', 'sandale', 'sanda', 'ghete', 'gheata', 'cizme', 'cizma', 'papuci',
			'slapi', 'mocasini', 'balerini', 'botine', 'botosei', 'espadrile', 'incaltaminte',
			// îmbrăcăminte
			'geaca', 'jacheta', 'palton', 'parka', 'hanorac', 'pulover', 'cardigan',
			'bluza', 'tricou', 'camasa', 'rochie', 'rochita', 'fusta', 'pantaloni',
			'pantalon', 'blugi', 'jeans', 'sort', 'sorturi', 'bermude', 'trening',
			'salopeta', 'compleu', 'pijama', 'pijamale', 'body', 'costum', 'lenjerie',
			'leggings', 'colanti', 'maiou', 'top', 'vesta', 'sacou', 'combinezon',
			// accesorii
			'sapca', 'caciula', 'palarie', 'fular', 'esarfa', 'manusi', 'sosete',
			'ciorapi', 'geanta', 'gentuta', 'rucsac', 'ghiozdan', 'borseta', 'curea',
			'ochelari', 'palarie',
			// materiale/culori frecvente (nu identifică modelul)
			'bumbac', 'piele', 'ecologica', 'textil', 'impermeabil', 'impermeabile',
		)
	);
}

/** Tokenizează o cheie de potrivire. */
function hainute_key_tokens( $key ) {
	return array_values( array_filter( explode( ' ', (string) $key ) ) );
}

/**
 * „Ancoră distinctivă": cele două chei împart cel puțin un cuvânt de model
 * (≥4 caractere, deci nume de model precum „runfalcon", nu „air"/„1"/„v2").
 * Fără o astfel de ancoră, refuzăm potrivirea, oricât de asemănătoare ar fi.
 *
 * @return array [ shared_count, has_anchor ]
 */
function hainute_shared_anchor( $key_a, $key_b ) {
	$shared    = array_intersect( hainute_key_tokens( $key_a ), hainute_key_tokens( $key_b ) );
	$has_anchor = false;
	foreach ( $shared as $t ) {
		if ( strlen( $t ) >= 4 ) {
			$has_anchor = true;
			break;
		}
	}
	return array( count( $shared ), $has_anchor );
}

/**
 * Normalize a brand for the match gate (lowercase, no diacritics, alnum only).
 */
function hainute_norm_brand( $brand ) {
	$brand = remove_accents( wp_strip_all_tags( (string) $brand ) );
	$brand = strtolower( $brand );
	$brand = preg_replace( '/[^a-z0-9 ]+/', ' ', $brand );
	return trim( preg_replace( '/\s+/', ' ', $brand ) );
}

/**
 * Two brands count as the same when equal or one is a prefix of the other
 * (handles "Calvin Klein" vs "Calvin Klein Jeans").
 */
function hainute_brands_match( $a, $b ) {
	if ( '' === $a || '' === $b ) {
		return false;
	}
	if ( $a === $b ) {
		return true;
	}
	return 0 === strpos( $a, $b . ' ' ) || 0 === strpos( $b, $a . ' ' );
}

/**
 * Build the normalized match key from the product name.
 *
 * Brand tokens are stripped from the name too (not just excluded from the
 * gate): stores often repeat the brand in the title, so a generic title like
 * "BOSS pentru copii" would otherwise reduce to just "boss" and wrongly match
 * every other generic BOSS item. With brand + filler removed it becomes an
 * empty key → treated as "cannot confidently match" → kept separate.
 */
function hainute_match_key( $brand, $name ) {
	$text = remove_accents( wp_strip_all_tags( (string) $name ) );
	$text = strtolower( $text );
	$text = preg_replace( '/[^a-z0-9 ]+/', ' ', $text );

	$brand_tokens = array_filter( explode( ' ', hainute_norm_brand( $brand ) ) );
	// Culorile se scot din cheie → variantele de culoare ale aceluiași model au
	// cheie identică și se unesc într-un produs (Gazelle negru + roz).
	$color_words = function_exists( 'hainute_color_words' ) ? hainute_color_words() : array();

	$tokens = array_filter( explode( ' ', $text ) );
	$tokens = array_diff( $tokens, hainute_match_stopwords(), hainute_type_words(), $color_words, $brand_tokens );
	$tokens = array_unique( $tokens );
	sort( $tokens );

	return implode( ' ', $tokens );
}

/**
 * Token overlap coefficient (%) between two space-separated keys:
 * |A ∩ B| / min(|A|,|B|). Robust to a single swapped/added word.
 */
function hainute_token_overlap( $a, $b ) {
	$ta = array_filter( explode( ' ', $a ) );
	$tb = array_filter( explode( ' ', $b ) );
	if ( empty( $ta ) || empty( $tb ) ) {
		return 0;
	}
	$common = count( array_intersect( $ta, $tb ) );
	return $common / min( count( $ta ), count( $tb ) ) * 100;
}

/**
 * Combined similarity (%) = max of character similarity and token overlap.
 */
function hainute_similarity( $a, $b ) {
	similar_text( $a, $b, $pct );
	return max( $pct, hainute_token_overlap( $a, $b ) );
}

/**
 * Find an existing product matching this one.
 *
 * @param string $key              Match key from hainute_match_key().
 * @param string $brand            Raw brand (normalized internally).
 * @param int    $exclude_store_id Store the incoming item belongs to. Products
 *                                 that already have an offer from this store are
 *                                 never matched — aggregation is cross-store
 *                                 only, so two items from one store are always
 *                                 distinct products.
 * @param array  $near_misses      By-ref: near-threshold cases for logging.
 * @return int|null Product post ID, or null when no confident match exists.
 */
function hainute_find_matching_product( $key, $brand = '', $exclude_store_id = 0, $allow_same_store = false, array &$near_misses = array() ) {
	global $wpdb;

	// Need at least two meaningful tokens to identify a product confidently;
	// a single generic word (or an empty key) is not enough to merge on.
	if ( '' === $key || count( array_filter( explode( ' ', $key ) ) ) < 2 ) {
		return null;
	}

	$norm_brand    = hainute_norm_brand( $brand );
	$offers_table  = hainute_offers_table_name();
	$exclude_store = (int) $exclude_store_id;

	// Candidates = published products, cu magazinele lor (pentru a distinge
	// variantele din același magazin de potrivirile cross-store).
	$candidates = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT p.ID,
				k.meta_value AS match_key,
				COALESCE(b.meta_value, '') AS match_brand,
				(SELECT GROUP_CONCAT(o.store_id) FROM {$offers_table} o WHERE o.product_id = p.ID) AS store_ids
			FROM {$wpdb->posts} p
			INNER JOIN {$wpdb->postmeta} k ON k.post_id = p.ID AND k.meta_key = %s
			LEFT JOIN {$wpdb->postmeta} b ON b.post_id = p.ID AND b.meta_key = %s
			WHERE p.post_type = 'product' AND p.post_status = 'publish'",
			HAINUTE_MATCH_META_KEY,
			HAINUTE_MATCH_META_BRAND
		)
	);

	// 1. Exact key + brand → același produs. Unirea din ACELAȘI magazin (variantă
	// de culoare) e permisă doar când item-ul are o etichetă de culoare
	// ($allow_same_store) — altfel n-am cum s-o disting și e mai bine s-o las
	// produs separat, cu poza/linkul ei (ex. various-brands, fără culoare în titlu).
	foreach ( $candidates as $c ) {
		if ( $c->match_key !== $key ) {
			continue;
		}
		if ( '' !== $norm_brand && ! hainute_brands_match( $norm_brand, $c->match_brand ) ) {
			continue;
		}
		if ( ! $allow_same_store && $exclude_store > 0 && ! empty( $c->store_ids ) ) {
			$stores = array_map( 'intval', explode( ',', $c->store_ids ) );
			if ( in_array( $exclude_store, $stores, true ) ) {
				continue; // același magazin, fără etichetă de culoare → nu unesc
			}
		}
		return (int) $c->ID;
	}

	// 2. Fuzzy fallback — only among candidates that share a distinctive model
	// anchor (a ≥4-char token, i.e. the model name), so "adidas Runfalcon" at
	// two stores merges but "Nike Air Force 1" and "Nike Air Max 1" do not.
	$best_pct = 0;
	$best_id  = null;
	$best_key = '';

	foreach ( $candidates as $c ) {
		$branded = ( '' !== $norm_brand && hainute_brands_match( $norm_brand, $c->match_brand ) );

		// Branded items only compare within the same brand; brandless compare
		// against other brandless items.
		if ( '' !== $norm_brand && ! $branded ) {
			continue;
		}
		if ( '' === $norm_brand && '' !== $c->match_brand ) {
			continue;
		}

		// Potrivirea FUZZY (nu exactă) din același magazin e riscantă → o sărim.
		// (Variantele reale au cheie identică, deci prind pe calea exactă de mai sus.)
		if ( $exclude_store > 0 && ! empty( $c->store_ids ) ) {
			$stores = array_map( 'intval', explode( ',', $c->store_ids ) );
			if ( in_array( $exclude_store, $stores, true ) ) {
				continue;
			}
		}

		list( $shared_count, $has_anchor ) = hainute_shared_anchor( $key, $c->match_key );
		if ( ! $has_anchor || $shared_count < 2 ) {
			continue; // fără nume de model comun → nu e același produs
		}

		$pct = hainute_similarity( $key, $c->match_key );
		if ( $pct > $best_pct ) {
			$best_pct = $pct;
			$best_id  = (int) $c->ID;
			$best_key = $c->match_key;
		}
	}

	$threshold = ( '' !== $norm_brand ) ? HAINUTE_MATCH_BRANDED : HAINUTE_MATCH_AUTO;

	if ( $best_pct >= $threshold ) {
		return $best_id;
	}

	if ( $best_pct >= HAINUTE_MATCH_NEAR ) {
		$near_misses[] = array(
			'key'          => $key,
			'existing_key' => $best_key,
			'similarity'   => round( $best_pct, 1 ),
			'product_id'   => $best_id,
		);
	}

	return null;
}
