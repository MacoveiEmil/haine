<?php
/**
 * „Cum funcționează": cifrele reale ale site-ului (câte magazine verificăm, la
 * câte ore), pagina explicativă și /llms.txt (rezumatul site-ului pentru
 * asistenții AI). Totul pornește din aceleași date ca paginile de produs.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** La câte ore reverificăm stocul (ciclul worker-ului; vezi tools/crawler/CRON.md). */
function hainute_refresh_hours() {
	return max( 1, (int) get_option( 'hainute_refresh_hours', 6 ) );
}

/** Magazinele care au cel puțin o ofertă la un produs publicat. */
function hainute_active_store_names() {
	$cached = get_transient( 'hainute_active_stores' );
	if ( is_array( $cached ) ) {
		return $cached;
	}
	global $wpdb;
	$names = array();
	// Numele afișate pe paginile de produs (hainute_get_offers rezolvă magazinul
	// real din URL), doar din ofertele cu stoc și neexpirate.
	if ( function_exists( 'hainute_offers_table_name' ) && function_exists( 'hainute_get_offers' ) ) {
		$t   = hainute_offers_table_name();
		$ids = $wpdb->get_col( "SELECT DISTINCT o.product_id FROM {$t} o INNER JOIN {$wpdb->posts} p ON p.ID = o.product_id AND p.post_status = 'publish' WHERE o.stock_status <> 'out_of_stock'" );
		foreach ( $ids as $pid ) {
			foreach ( hainute_get_offers( (int) $pid ) as $o ) {
				if ( 'out_of_stock' === $o->stock_status || empty( $o->store->name ) ) {
					continue;
				}
				if ( function_exists( 'hainute_offer_is_stale' ) && hainute_offer_is_stale( (int) $pid, $o ) ) {
					continue;
				}
				$names[ $o->store->name ] = 1;
			}
		}
	}
	$names = array_keys( $names );
	natcasesort( $names );
	$names = array_values( $names );
	set_transient( 'hainute_active_stores', $names, 6 * HOUR_IN_SECONDS );
	return $names;
}

/** [hainute_cifre tip="magazine|ore|produse"] — cifrele din textul paginii. */
add_shortcode(
	'hainute_cifre',
	function ( $atts ) {
		$a = shortcode_atts( array( 'tip' => 'magazine' ), $atts );
		switch ( $a['tip'] ) {
			case 'ore':
				return (string) hainute_refresh_hours();
			case 'produse':
				$c = wp_count_posts( 'product' );
				return number_format_i18n( (int) ( $c->publish ?? 0 ) );
			case 'lista':
				return esc_html( implode( ', ', hainute_active_store_names() ) );
			default:
				return (string) count( hainute_active_store_names() );
		}
	}
);

/** Conținutul paginii „Cum funcționează" (folosit la crearea ei). */
function hainute_how_it_works_content() {
	return <<<'HTML'
<!-- wp:paragraph -->
<p>hainute.ro te ajută să găsești <strong>mărimea potrivită pentru copilul tău, direct la magazinul care o are</strong>. Nu vindem nimic și nu facem clasamente de prețuri: îți arătăm, pentru fiecare produs, ce mărimi sunt pe stoc și în ce magazin.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>1. Alegi produsul și mărimea</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Pe pagina fiecărui produs vezi toate mărimile lui, cu vârsta orientativă. Mărimile tăiate sunt epuizate peste tot în acest moment. Când alegi o mărime, magazinele care o au pe stoc urcă primele în listă.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>2. Verificăm stocul pe mărimi la [hainute_cifre tip="magazine"] magazine</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Urmărim [hainute_cifre tip="produse"] produse pentru copii la aceste magazine: [hainute_cifre tip="lista"]. Pentru fiecare produs verificăm direct pe pagina magazinului ce mărimi sunt disponibile și care s-au epuizat, nu doar dacă produsul există.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>3. Actualizăm datele la fiecare [hainute_cifre tip="ore"] ore</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Stocul se reverifică automat, la fiecare [hainute_cifre tip="ore"] ore. Pe pagina produsului scrie când a fost verificată ultima dată disponibilitatea. Dacă pentru un magazin nu am putut confirma mărimea, scrie „Mărime neconfirmată”, nu „Disponibil”.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>4. Cumperi direct de la magazin</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Butonul „Vezi în magazin” te duce pe pagina produsului din magazin, unde finalizezi comanda. Prețul, livrarea și retururile sunt ale magazinului. Unele linkuri sunt afiliate: dacă cumperi prin ele, primim un mic comision, fără niciun cost în plus pentru tine.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Dacă mărimea nu e pe stoc</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Când mărimea aleasă e epuizată peste tot, îți arătăm alte produse din aceeași categorie, în aceeași mărime, care sunt pe stoc acum.</p>
<!-- /wp:paragraph -->
HTML;
}

/** Creează pagina „Cum funcționează" o singură dată (dacă lipsește) și o pune în meniuri. */
function hainute_ensure_how_it_works_page() {
	if ( get_option( 'hainute_hiw_page_v1' ) ) {
		return;
	}
	// Blocare: două cereri simultane ar crea pagina de două ori. add_option eșuează
	// dacă opțiunea există deja, deci doar prima cerere continuă.
	if ( ! add_option( 'hainute_hiw_page_lock', time(), '', false ) ) {
		return;
	}
	$page = get_page_by_path( 'cum-functioneaza' );
	if ( ! $page ) {
		$id = wp_insert_post(
			array(
				'post_type'    => 'page',
				'post_status'  => 'publish',
				'post_title'   => 'Cum funcționează',
				'post_name'    => 'cum-functioneaza',
				'post_content' => hainute_how_it_works_content(),
			)
		);
		if ( ! $id || is_wp_error( $id ) ) {
			return;
		}
		update_post_meta( $id, '_hainute_meta_desc', 'Cum găsești pe hainute.ro mărimea copilului la magazinul care o are pe stoc: ce verificăm, la câte magazine și cât de des actualizăm datele.' );
	} else {
		$id = $page->ID;
	}
	// În meniul principal (în locul lui „Cum testăm", care rămâne în footer) și în footer.
	$locs = get_nav_menu_locations();
	foreach ( array( 'primary', 'footer' ) as $loc ) {
		if ( empty( $locs[ $loc ] ) ) {
			continue;
		}
		$items = wp_get_nav_menu_items( $locs[ $loc ] );
		$has   = false;
		foreach ( (array) $items as $it ) {
			if ( (int) $it->object_id === (int) $id ) {
				$has = true;
			}
			if ( 'primary' === $loc && 'Cum testăm' === $it->title ) {
				wp_delete_post( $it->ID, true );
			}
		}
		if ( ! $has ) {
			wp_update_nav_menu_item(
				$locs[ $loc ],
				0,
				array(
					'menu-item-title'     => 'Cum funcționează',
					'menu-item-object'    => 'page',
					'menu-item-object-id' => $id,
					'menu-item-type'      => 'post_type',
					'menu-item-status'    => 'publish',
					'menu-item-position'  => 'primary' === $loc ? 3 : 1,
				)
			);
		}
	}
	update_option( 'hainute_hiw_page_v1', 1 );
}
add_action( 'init', 'hainute_ensure_how_it_works_page', 20 );

/** /llms.txt: rezumatul site-ului pentru asistenții AI (format llmstxt.org). */
add_action(
	'parse_request',
	function () {
		$path = trim( (string) wp_parse_url( $_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH ), '/' );
		if ( 'llms.txt' !== $path ) {
			return;
		}
		$home   = home_url( '/' );
		$hiw    = get_page_by_path( 'cum-functioneaza' );
		$lines  = array();
		$lines[] = '# hainute.ro';
		$lines[] = '';
		$lines[] = '> Găsește mărimea potrivită pentru copilul tău, direct la magazinul care o are. hainute.ro arată, pentru haine și încălțăminte de copii, ce mărimi sunt pe stoc și în ce magazin online din România. Nu vinde produse și nu este un site de prețuri.';
		$lines[] = '';
		$lines[] = sprintf( '- Verificăm stocul pe mărimi la %d magazine: %s.', count( hainute_active_store_names() ), implode( ', ', hainute_active_store_names() ) );
		$lines[] = sprintf( '- Datele se actualizează automat la fiecare %d ore; fiecare pagină de produs arată ora ultimei verificări.', hainute_refresh_hours() );
		$lines[] = '- Pe pagina unui produs: mărimile (cu vârsta orientativă), tabelul mărime × magazin cu stocul și linkul spre pagina produsului din magazin.';
		$lines[] = '- Unele linkuri spre magazine sunt afiliate.';
		$lines[] = '';
		$lines[] = '## Pagini principale';
		$lines[] = '';
		if ( $hiw ) {
			$lines[] = '- [Cum funcționează](' . get_permalink( $hiw ) . '): ce verificăm, la câte magazine și cât de des';
		}
		$lines[] = '- [Toate produsele](' . get_post_type_archive_link( 'product' ) . '): haine și încălțăminte pentru copii, cu mărimile disponibile';
		$cats = get_terms( array( 'taxonomy' => 'product_cat', 'hide_empty' => true, 'parent' => 0 ) );
		if ( ! is_wp_error( $cats ) ) {
			foreach ( $cats as $c ) {
				$lines[] = '- [' . html_entity_decode( $c->name ) . '](' . get_term_link( $c ) . ')';
			}
		}
		foreach ( array( 'despre-noi' => 'Despre noi', 'declaratie-afiliere' => 'Declarație de afiliere', 'contact' => 'Contact' ) as $slug => $label ) {
			$pg = get_page_by_path( $slug );
			if ( $pg ) {
				$lines[] = '- [' . $label . '](' . get_permalink( $pg ) . ')';
			}
		}
		$lines[] = '';
		$lines[] = '## Opțional';
		$lines[] = '';
		$lines[] = '- [Sitemap](' . home_url( '/wp-sitemap.xml' ) . ')';
		nocache_headers();
		header( 'Content-Type: text/plain; charset=utf-8' );
		header( 'X-Robots-Tag: noindex' );
		echo implode( "\n", $lines ) . "\n";
		exit;
	},
	0
);

/**
 * Termenii `store` ai magazinelor active, unul per nume afișat (cel cu cele mai
 * multe produse), în ordinea numelor.
 * @return WP_Term[]
 */
function hainute_store_terms_active() {
	$active = hainute_active_store_names();
	$terms  = get_terms( array( 'taxonomy' => 'store', 'hide_empty' => true ) );
	$by     = array();
	foreach ( is_wp_error( $terms ) ? array() : $terms as $t ) {
		$name = hainute_store_display_name( $t->name );
		if ( in_array( $name, $active, true ) && ( ! isset( $by[ $name ] ) || $t->count > $by[ $name ]->count ) ) {
			$by[ $name ] = $t;
		}
	}
	uksort( $by, 'strnatcasecmp' );
	return array_values( $by );
}

/** Pagina unui magazin e indexabilă doar dacă e un magazin activ și termenul principal. */
function hainute_store_term_indexable( $term ) {
	foreach ( hainute_store_terms_active() as $t ) {
		if ( (int) $t->term_id === (int) $term->term_id ) {
			return true;
		}
	}
	return false;
}

