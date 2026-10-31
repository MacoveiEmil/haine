<?php
/**
 * Listing filters & sorting (Faza 4) — plain GET params on archive pages:
 *   gen, varsta, categorie, brand, pret_min, pret_max, sortare (pret-asc | pret-desc | nou)
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Is this a product listing query we should touch?
 */
function hainute_is_product_listing( $query ) {
	if ( is_admin() || ! $query->is_main_query() ) {
		return false;
	}

	return $query->is_post_type_archive( 'product' )
		|| $query->is_tax( array( 'product_cat', 'product_brand', 'product_gender', 'product_age', 'store' ) )
		|| ( $query->is_search() && 'product' === $query->get( 'post_type' ) );
}

function hainute_apply_listing_filters( $query ) {
	if ( ! hainute_is_product_listing( $query ) ) {
		return;
	}

	$query->set( 'posts_per_page', 24 );

	// --- Taxonomy filters ---------------------------------------------------
	$tax_query = (array) $query->get( 'tax_query' );

	$tax_params = array(
		'categorie' => 'product_cat',
		'gen'       => 'product_gender',
		'varsta'    => 'product_age',
	);
	if ( ! $query->is_tax( 'product_brand' ) ) { // pe pagina unui brand filtrul de brand nu are sens
		$tax_params['brand'] = 'product_brand';
	}
	foreach ( $tax_params as $param => $taxonomy ) {
		if ( ! empty( $_GET[ $param ] ) ) {
			$tax_query[] = array(
				'taxonomy' => $taxonomy,
				'field'    => 'slug',
				'terms'    => sanitize_title( wp_unslash( $_GET[ $param ] ) ),
			);
		}
	}

	if ( ! empty( $tax_query ) ) {
		$query->set( 'tax_query', $tax_query );
	}

	// --- Price range (uses the cached _hainute_min_price meta) ---------------
	$meta_query = (array) $query->get( 'meta_query' );
	$pret_min   = isset( $_GET['pret_min'] ) ? (float) $_GET['pret_min'] : 0;
	$pret_max   = isset( $_GET['pret_max'] ) ? (float) $_GET['pret_max'] : 0;

	if ( $pret_min > 0 || $pret_max > 0 ) {
		$range = array(
			'key'  => '_hainute_min_price',
			'type' => 'NUMERIC',
		);
		if ( $pret_min > 0 && $pret_max > 0 ) {
			$range['value']   = array( $pret_min, $pret_max );
			$range['compare'] = 'BETWEEN';
		} elseif ( $pret_min > 0 ) {
			$range['value']   = $pret_min;
			$range['compare'] = '>=';
		} else {
			$range['value']   = $pret_max;
			$range['compare'] = '<=';
		}
		$meta_query[] = $range;
	}

	// --- Doar produse cross-store (disponibile în 2+ magazine) ---------------
	if ( ! empty( $_GET['cross'] ) ) {
		$meta_query[] = array(
			'key'     => '_hainute_store_count',
			'value'   => 2,
			'type'    => 'NUMERIC',
			'compare' => '>=',
		);
	}

	// --- Filtru mărime: eticheta EXACTĂ din lista _hainute_sizes ("a, b, c") ---
	// (LIKE găsea subșiruri: „24" prindea „124", „M" prindea „158 CM").
	if ( ! empty( $_GET['marime'] ) ) {
		$size = sanitize_text_field( wp_unslash( $_GET['marime'] ) );
		// Doar produsele care au mărimea PE STOC la un magazin (vezi
		// hainute_refresh_instock_sizes); formatul „, 28, 30," permite LIKE simplu.
		$meta_query[] = array(
			'key'     => '_hainute_sizes_instock',
			'value'   => ', ' . $size . ',',
			'compare' => 'LIKE',
		);
	}

	// Produsele cu stoc primele, în orice sortare (cele fără stoc rămân, la final).
	// Un singur JOIN pe cheie (indexat). Varianta cu „OR NOT EXISTS" făcea un JOIN pe
	// toate meta-urile și dura ~2s pe listare; toate produsele publicate au cheia
	// (o scrie hainute_refresh_buyable la fiecare ofertă).
	$meta_query['hainute_buyable'] = array( 'key' => '_hainute_buyable', 'type' => 'NUMERIC' );

	// --- Sorting --------------------------------------------------------------
	$sort = isset( $_GET['sortare'] ) ? sanitize_key( wp_unslash( $_GET['sortare'] ) ) : '';

	if ( 'pret-asc' === $sort || 'pret-desc' === $sort ) {
		$meta_query['hainute_pret'] = array( 'key' => '_hainute_min_price', 'type' => 'DECIMAL(10,2)' );
		$query->set( 'orderby', array( 'hainute_buyable' => 'DESC', 'hainute_pret' => 'pret-asc' === $sort ? 'ASC' : 'DESC' ) );
	} else {
		// Implicit: produsele găsite în mai multe magazine primele (scopul site-ului:
		// mărimea la magazinul care o are), apoi cele noi. _hainute_store_count există
		// pe toate produsele publicate (îl scrie hainute_refresh_buyable).
		$meta_query['hainute_magazine'] = array( 'key' => '_hainute_store_count', 'type' => 'NUMERIC' );
		$query->set( 'orderby', array( 'hainute_buyable' => 'DESC', 'hainute_magazine' => 'DESC', 'date' => 'DESC' ) );
	}
	$query->set( 'meta_query', $meta_query );
}
add_action( 'pre_get_posts', 'hainute_apply_listing_filters' );

/**
 * Distinct size labels present on PUBLISHED products (for the size dropdown).
 * Draft-urile (ascunse) nu intră: altfel lista ar avea mărimi fără niciun produs.
 * Cached 1h in a transient; invalidated naturally on expiry.
 */
function hainute_available_sizes() {
	$cached = get_transient( 'hainute_available_sizes_v3' );
	if ( is_array( $cached ) ) {
		return $cached;
	}

	global $wpdb;
	$rows = $wpdb->get_col(
		"SELECT pm.meta_value FROM {$wpdb->postmeta} pm
		 INNER JOIN {$wpdb->posts} p ON p.ID = pm.post_id
		 WHERE pm.meta_key = '_hainute_sizes_instock' AND pm.meta_value <> ''
		   AND p.post_type = 'product' AND p.post_status = 'publish'"
	);

	$sizes = array();
	foreach ( $rows as $r ) {
		foreach ( array_map( 'trim', explode( ',', $r ) ) as $s ) {
			if ( '' !== $s ) {
				$sizes[ $s ] = true;
			}
		}
	}
	$sizes = array_keys( $sizes );
	natcasesort( $sizes );
	$sizes = array_values( $sizes );

	set_transient( 'hainute_available_sizes_v3', $sizes, HOUR_IN_SECONDS );
	return $sizes;
}

/**
 * Grupează etichetele de mărime pentru dropdown (optgroup) și le sortează numeric:
 * încălțăminte EU (≤46), înălțime cm (≥50), litere, vârstă, restul.
 * Doar afișare: valoarea trimisă rămâne eticheta exactă din feed.
 */
function hainute_group_sizes( array $sizes ) {
	$letters = array( 'XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL' );
	$groups  = array(
		'shoe'   => array(),
		'height' => array(),
		'letter' => array(),
		'age'    => array(),
		'other'  => array(),
	);
	foreach ( $sizes as $s ) {
		$u = strtoupper( trim( $s ) );
		if ( in_array( $u, $letters, true ) ) {
			$groups['letter'][ $s ] = array_search( $u, $letters, true );
		} elseif ( preg_match( '/(ANI|^\d+\s*Y$)/', $u ) ) {
			$groups['age'][ $s ] = (float) $u;
		} elseif ( preg_match( '/^(\d+(?:[.,]\d+)?)(?:\s*CM)?(?:\s*-\s*\d+(?:\s*CM)?)?$/', $u, $m ) ) {
			$n = (float) str_replace( ',', '.', $m[1] );
			$groups[ $n <= 46 ? 'shoe' : 'height' ][ $s ] = $n;
		} else {
			$groups['other'][ $s ] = (float) $u;
		}
	}
	$labels = array(
		'shoe'   => __( 'Încălțăminte (EU)', 'hainute' ),
		'height' => __( 'Haine: înălțime (cm)', 'hainute' ),
		'letter' => __( 'Haine: litere', 'hainute' ),
		'age'    => __( 'Vârstă', 'hainute' ),
		'other'  => __( 'Altele', 'hainute' ),
	);
	$out = array();
	foreach ( $groups as $key => $items ) {
		if ( $items ) {
			uksort(
				$items,
				function ( $a, $b ) use ( $items ) {
					return ( $items[ $a ] <=> $items[ $b ] ) ?: strnatcasecmp( $a, $b );
				}
			);
			$out[ $labels[ $key ] ] = array_keys( $items );
		}
	}
	return $out;
}

/**
 * Brandurile care au produse PUBLICATE în listarea curentă, cu numărul de produse
 * (pentru dropdown-ul de brand). Contextul = categoria / genul / vârsta / magazinul
 * paginii (categoria include subcategoriile); pe arhivă și căutare, toate brandurile.
 * Cache 1h în transient.
 *
 * @return array[] { slug, name, count }
 */
function hainute_listing_brands() {
	$obj = is_tax( array( 'product_cat', 'product_gender', 'product_age', 'store' ) ) ? get_queried_object() : null;
	$key = 'hainute_brands_v1_' . ( $obj ? $obj->taxonomy . '_' . (int) $obj->term_id : 'all' );
	$cached = get_transient( $key );
	if ( is_array( $cached ) ) {
		return $cached;
	}

	global $wpdb;
	$join = '';
	if ( $obj ) {
		$tt_ids = array( (int) $obj->term_taxonomy_id );
		if ( is_taxonomy_hierarchical( $obj->taxonomy ) ) {
			foreach ( get_term_children( $obj->term_id, $obj->taxonomy ) as $child_id ) {
				$child = get_term( $child_id, $obj->taxonomy );
				if ( $child && ! is_wp_error( $child ) ) {
					$tt_ids[] = (int) $child->term_taxonomy_id;
				}
			}
		}
		$join = "INNER JOIN {$wpdb->term_relationships} rc ON rc.object_id = p.ID AND rc.term_taxonomy_id IN (" . implode( ',', array_map( 'intval', $tt_ids ) ) . ')';
	}

	$rows = $wpdb->get_results(
		"SELECT t.slug, t.name, COUNT(DISTINCT p.ID) AS n
		 FROM {$wpdb->posts} p
		 INNER JOIN {$wpdb->term_relationships} rb ON rb.object_id = p.ID
		 INNER JOIN {$wpdb->term_taxonomy} tb ON tb.term_taxonomy_id = rb.term_taxonomy_id AND tb.taxonomy = 'product_brand'
		 INNER JOIN {$wpdb->terms} t ON t.term_id = tb.term_id
		 {$join}
		 WHERE p.post_type = 'product' AND p.post_status = 'publish'
		 GROUP BY t.term_id, t.slug, t.name
		 ORDER BY t.name ASC"
	);

	$brands = array();
	foreach ( (array) $rows as $r ) {
		$brands[] = array( 'slug' => $r->slug, 'name' => $r->name, 'count' => (int) $r->n );
	}

	set_transient( $key, $brands, HOUR_IN_SECONDS );
	return $brands;
}

/**
 * Etichetă de categorie dezambiguizată: „Fete › Geci & jachete".
 * Fiindcă aceeași subcategorie există sub Fete/Băieți/Bebe, numele simplu apare
 * duplicat în liste — prefixăm cu strămoșul de nivel 1 ca să fie distinct.
 */
function hainute_term_path_label( $term, $sep = ' › ' ) {
	if ( ! $term || is_wp_error( $term ) ) {
		return '';
	}
	$anc = get_ancestors( $term->term_id, 'product_cat' );
	if ( empty( $anc ) ) {
		return $term->name;
	}
	$top = get_term( end( $anc ), 'product_cat' ); // nivel 1 (ultimul strămoș)
	return ( $top && ! is_wp_error( $top ) ) ? $top->name . $sep . $term->name : $term->name;
}

/**
 * Categoria curentă e în arborele Fete, Băieți sau Unisex? Atunci genul e deja stabilit
 * de pagină (Bebe rămâne cu filtru de gen: acolo produsele au genuri diferite).
 */
function hainute_gender_fixed_by_category() {
	if ( ! is_tax( 'product_cat' ) || ! function_exists( 'hainute_cat_path_names' ) ) {
		return false;
	}
	$term = get_queried_object();
	if ( ! $term ) {
		return false;
	}
	list( $top ) = hainute_cat_path_names( $term->term_id );
	return in_array( $top, array( 'fete', 'baieti', 'unisex' ), true );
}

/**
 * Render the filter bar (GET form, keeps the current URL as action).
 */
function hainute_the_filter_bar() {
	$is_cat_page = is_tax( 'product_cat' );

	$categories = get_terms( array( 'taxonomy' => 'product_cat', 'hide_empty' => true ) );
	$genders    = get_terms( array( 'taxonomy' => 'product_gender', 'hide_empty' => true ) );
	$ages       = get_terms( array( 'taxonomy' => 'product_age', 'hide_empty' => true ) );

	$current = array(
		'categorie' => isset( $_GET['categorie'] ) ? sanitize_title( wp_unslash( $_GET['categorie'] ) ) : '',
		'gen'       => isset( $_GET['gen'] ) ? sanitize_title( wp_unslash( $_GET['gen'] ) ) : '',
		'varsta'    => isset( $_GET['varsta'] ) ? sanitize_title( wp_unslash( $_GET['varsta'] ) ) : '',
		'brand'     => isset( $_GET['brand'] ) ? sanitize_title( wp_unslash( $_GET['brand'] ) ) : '',
		'pret_min'  => isset( $_GET['pret_min'] ) && (float) $_GET['pret_min'] > 0 ? (float) $_GET['pret_min'] : '',
		'pret_max'  => isset( $_GET['pret_max'] ) && (float) $_GET['pret_max'] > 0 ? (float) $_GET['pret_max'] : '',
		'sortare'   => isset( $_GET['sortare'] ) ? sanitize_key( wp_unslash( $_GET['sortare'] ) ) : '',
		'cross'     => ! empty( $_GET['cross'] ),
		'marime'    => isset( $_GET['marime'] ) ? sanitize_text_field( wp_unslash( $_GET['marime'] ) ) : '',
	);

	// Pe categoriile Fete / Băieți / Unisex genul e deja ales de categorie: filtrul de gen n-are sens.
	if ( hainute_gender_fixed_by_category() ) {
		$genders        = array();
		$current['gen'] = '';
	}

	$sizes  = hainute_available_sizes();
	$brands = is_tax( 'product_brand' ) ? array() : hainute_listing_brands();
	if ( is_tax( 'product_brand' ) ) {
		$current['brand'] = '';
	}

	// Câte filtre sunt active (sortarea nu se numără) → afișat pe butonul de pe mobil.
	$active = count( array_filter( array( $current['categorie'], $current['gen'], $current['varsta'], $current['brand'], $current['pret_min'], $current['pret_max'], $current['cross'], $current['marime'] ) ) );
	?>
	<button type="button" class="filter-toggle" aria-expanded="false" aria-controls="filter-bar">
		<?php esc_html_e( 'Filtre și sortare', 'hainute' ); ?>
		<?php if ( $active ) : ?>
			<span class="filter-count"><?php echo (int) $active; ?></span>
		<?php endif; ?>
	</button>
	<form id="filter-bar" class="filter-bar" method="get" data-filter-bar>
		<?php if ( is_search() ) : ?>
			<input type="hidden" name="s" value="<?php echo esc_attr( get_search_query() ); ?>">
			<input type="hidden" name="post_type" value="product">
		<?php endif; ?>

		<?php if ( ! $is_cat_page && ! is_wp_error( $categories ) && $categories ) : ?>
			<select name="categorie" aria-label="<?php esc_attr_e( 'Categorie', 'hainute' ); ?>">
				<option value=""><?php esc_html_e( 'Toate categoriile', 'hainute' ); ?></option>
				<?php foreach ( $categories as $term ) : ?>
					<option value="<?php echo esc_attr( $term->slug ); ?>" <?php selected( $current['categorie'], $term->slug ); ?>>
						<?php echo esc_html( hainute_term_path_label( $term ) ); ?>
					</option>
				<?php endforeach; ?>
			</select>
		<?php endif; ?>

		<?php if ( ! is_wp_error( $genders ) && $genders ) : ?>
			<select name="gen" aria-label="<?php esc_attr_e( 'Gen', 'hainute' ); ?>">
				<option value=""><?php esc_html_e( 'Gen: toate', 'hainute' ); ?></option>
				<?php foreach ( $genders as $term ) : ?>
					<option value="<?php echo esc_attr( $term->slug ); ?>" <?php selected( $current['gen'], $term->slug ); ?>>
						<?php echo esc_html( $term->name ); ?>
					</option>
				<?php endforeach; ?>
			</select>
		<?php endif; ?>

		<?php if ( ! is_wp_error( $ages ) && $ages ) : ?>
			<select name="varsta" aria-label="<?php esc_attr_e( 'Vârstă', 'hainute' ); ?>">
				<option value=""><?php esc_html_e( 'Vârstă: toate', 'hainute' ); ?></option>
				<?php foreach ( $ages as $term ) : ?>
					<option value="<?php echo esc_attr( $term->slug ); ?>" <?php selected( $current['varsta'], $term->slug ); ?>>
						<?php echo esc_html( $term->name ); ?>
					</option>
				<?php endforeach; ?>
			</select>
		<?php endif; ?>

		<?php if ( $brands ) : ?>
			<select name="brand" aria-label="<?php esc_attr_e( 'Brand', 'hainute' ); ?>">
				<option value=""><?php esc_html_e( 'Brand: toate', 'hainute' ); ?></option>
				<?php foreach ( $brands as $b ) : ?>
					<option value="<?php echo esc_attr( $b['slug'] ); ?>" <?php selected( $current['brand'], $b['slug'] ); ?>>
						<?php echo esc_html( $b['name'] . ' (' . $b['count'] . ')' ); ?>
					</option>
				<?php endforeach; ?>
			</select>
		<?php endif; ?>

		<span class="filter-price">
			<input type="number" name="pret_min" min="0" step="1" placeholder="<?php esc_attr_e( 'Preț min', 'hainute' ); ?>" value="<?php echo esc_attr( $current['pret_min'] ); ?>">
			<span aria-hidden="true">-</span>
			<input type="number" name="pret_max" min="0" step="1" placeholder="<?php esc_attr_e( 'Preț max', 'hainute' ); ?>" value="<?php echo esc_attr( $current['pret_max'] ); ?>">
		</span>

		<select name="sortare" aria-label="<?php esc_attr_e( 'Sortare', 'hainute' ); ?>">
			<option value="" <?php selected( $current['sortare'], '' ); ?>><?php esc_html_e( 'Cele mai noi', 'hainute' ); ?></option>
			<option value="pret-asc" <?php selected( $current['sortare'], 'pret-asc' ); ?>><?php esc_html_e( 'Preț crescător', 'hainute' ); ?></option>
			<option value="pret-desc" <?php selected( $current['sortare'], 'pret-desc' ); ?>><?php esc_html_e( 'Preț descrescător', 'hainute' ); ?></option>
		</select>

		<?php if ( $sizes ) : ?>
			<select name="marime" aria-label="<?php esc_attr_e( 'Mărime', 'hainute' ); ?>">
				<option value=""><?php esc_html_e( 'Mărime: toate', 'hainute' ); ?></option>
				<?php foreach ( hainute_group_sizes( $sizes ) as $group_label => $group_sizes ) : ?>
					<optgroup label="<?php echo esc_attr( $group_label ); ?>">
						<?php foreach ( $group_sizes as $size ) : ?>
							<option value="<?php echo esc_attr( $size ); ?>" <?php selected( $current['marime'], $size ); ?>><?php echo esc_html( $size ); ?></option>
						<?php endforeach; ?>
					</optgroup>
				<?php endforeach; ?>
			</select>
		<?php endif; ?>

		<label class="filter-cross">
			<input type="checkbox" name="cross" value="1" <?php checked( $current['cross'] ); ?>>
			<?php esc_html_e( 'Doar în mai multe magazine', 'hainute' ); ?>
		</label>

		<button type="submit" class="btn btn-small"><?php esc_html_e( 'Filtrează', 'hainute' ); ?></button>
	</form>
	<?php
}

/**
 * Listările Fete / Băieți includ și produsele Unisex din aceeași categorie
 * (Fete › Încălțăminte › Adidași arată și Unisex › Încălțăminte › Adidași):
 * un produs unisex se potrivește ambelor genuri. Pagina rămâne a categoriei cerute.
 */
function hainute_include_unisex_in_listing( $query ) {
	if ( is_admin() || ! $query->is_main_query() || ! $query->is_tax( 'product_cat' ) || ! function_exists( 'hainute_cat_by_path' ) ) {
		return;
	}
	foreach ( $query->tax_query->queries as $i => $clause ) {
		if ( ! is_array( $clause ) || 'product_cat' !== ( $clause['taxonomy'] ?? '' ) ) {
			continue;
		}
		$field = $clause['field'] ?? 'term_id';
		$add   = array();
		foreach ( (array) $clause['terms'] as $t ) {
			$term = get_term_by( 'slug' === $field ? 'slug' : 'id', $t, 'product_cat' );
			if ( ! $term ) {
				continue;
			}
			list( $top, $names ) = hainute_cat_path_names( $term->term_id );
			if ( ! in_array( $top, array( 'fete', 'baieti' ), true ) ) {
				continue;
			}
			$eq = $names ? hainute_cat_by_path( 'unisex', $names ) : get_term_by( 'slug', 'unisex', 'product_cat' );
			if ( $eq && ! is_wp_error( $eq ) ) {
				$add[] = 'slug' === $field ? $eq->slug : (int) $eq->term_id;
			}
		}
		if ( $add ) {
			$query->tax_query->queries[ $i ]['terms'] = array_merge( (array) $clause['terms'], $add );
		}
	}
}
add_action( 'parse_tax_query', 'hainute_include_unisex_in_listing' );
