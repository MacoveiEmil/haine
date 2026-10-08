<?php
/**
 * Cross-check MANUAL + protecția editărilor, pe pagina de editare produs.
 *
 * 1. Lipești linkuri de produs de pe orice magazin (Modivo, Farfetch, eMAG...).
 *    La salvare, codul încarcă fiecare pagină și extrage nume/preț/disponibilitate
 *    (JSON-LD Product + meta og:price). Devin oferte în comparator (network manual:).
 * 2. Bifezi „Protejează editările mele" → sync-urile viitoare NU mai suprascriu
 *    titlul/categoria/descrierea (dar mărimile/culorile/linkul/stocul rămân live).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** EUR→RON pentru afișare consecventă (magazinele externe dau uneori EUR). */
function hainute_eur_ron() {
	return (float) hainute_config( 'HAINUTE_EUR_RON', 4.97 );
}

/** Convertește un preț în RON din moneda dată (Modivo .ro=EUR, .pl=PLN, .hu=HUF). */
function hainute_to_ron( $price, $currency ) {
	$rates = array(
		'RON' => 1.0,
		'EUR' => hainute_eur_ron(),
		'PLN' => (float) hainute_config( 'HAINUTE_PLN_RON', 1.17 ),
		'HUF' => (float) hainute_config( 'HAINUTE_HUF_RON', 0.0126 ),
		'BGN' => (float) hainute_config( 'HAINUTE_BGN_RON', 2.54 ),
		'CZK' => (float) hainute_config( 'HAINUTE_CZK_RON', 0.21 ),
	);
	$cur = strtoupper( (string) $currency );
	$r   = $rates[ $cur ] ?? 1.0;
	return round( (float) $price * $r, 2 );
}

/** Mapează un cuvânt-culoare EN→RO (numele externe sunt adesea în engleză). */
function hainute_color_to_ro( $c ) {
	$c   = mb_strtolower( trim( (string) $c ) );
	$map = array(
		'black' => 'negru', 'white' => 'alb', 'red' => 'rosu', 'blue' => 'albastru', 'navy' => 'bleumarin',
		'green' => 'verde', 'pink' => 'roz', 'yellow' => 'galben', 'grey' => 'gri', 'gray' => 'gri',
		'brown' => 'maro', 'beige' => 'bej', 'purple' => 'mov', 'violet' => 'violet', 'orange' => 'portocaliu',
		'cream' => 'crem', 'gold' => 'auriu', 'silver' => 'argintiu', 'turquoise' => 'turcoaz',
		'burgundy' => 'bordo', 'khaki' => 'kaki', 'multicolor' => 'multicolor', 'neutrals' => '', 'neutral' => '',
		// sinonime / nuanțe frecvente pe Zalando, AboutYou, Modivo
		'roșu' => 'rosu', 'coniac' => 'maro', 'caramel' => 'maro', 'chestnut' => 'maro', 'camel' => 'maro',
		'lila' => 'mov', 'lavender' => 'mov', 'lavandă' => 'mov', 'bleu' => 'albastru', 'marine' => 'bleumarin',
		'ivory' => 'crem', 'ecru' => 'crem', 'olive' => 'kaki', 'oliv' => 'kaki', 'fucsia' => 'roz', 'rose' => 'roz',
		'antracit' => 'gri', 'anthracite' => 'gri', 'charcoal' => 'gri', 'taupe' => 'bej', 'sand' => 'bej', 'nisip' => 'bej',
	);
	// „albastru marin" / „navy blue" = bleumarin (nu albastru).
	if ( preg_match( '/albastru[\s-]+marin|navy|bleumarin/u', $c ) ) {
		return 'bleumarin';
	}
	if ( isset( $map[ $c ] ) ) {
		return $map[ $c ];
	}
	// Compuse: „black/negru", „chestnut/coniac", „maro caramel", „mov orhidee" →
	// prima culoare de BAZĂ recunoscută. Necunoscut → '' (fără restricție de culoare,
	// nu inventăm o culoare nouă care ar despărți magazinul de produs).
	$base = array( 'negru', 'alb', 'rosu', 'albastru', 'bleumarin', 'verde', 'roz', 'galben', 'gri', 'maro', 'bej', 'mov', 'violet', 'portocaliu', 'crem', 'auriu', 'argintiu', 'turcoaz', 'bordo', 'kaki', 'multicolor' );
	foreach ( preg_split( '/[\s\/,\-+&]+/u', $c ) as $tok ) {
		$tok = $map[ $tok ] ?? $tok;
		if ( in_array( $tok, $base, true ) ) {
			return $tok;
		}
	}
	return in_array( $c, $base, true ) ? $c : '';
}

/** Stochează culoarea reală a unei oferte externe/manuale (normalizată RO). */
function hainute_set_ext_color( $pid, $store_id, $color ) {
	$color = hainute_color_to_ro( trim( (string) $color ) );
	if ( '' === $color || ! $store_id ) {
		return;
	}
	$map = get_post_meta( (int) $pid, '_hainute_ext_color', true );
	if ( ! is_array( $map ) ) {
		$map = array();
	}
	$map[ (int) $store_id ] = ucfirst( $color );
	update_post_meta( (int) $pid, '_hainute_ext_color', $map );
}

/** Slug + nume magazin din domeniul unui URL. */
function hainute_store_from_url( $url ) {
	$host = strtolower( (string) wp_parse_url( $url, PHP_URL_HOST ) );
	$host = preg_replace( '/^www\./', '', $host );
	$slug = sanitize_key( preg_replace( '/\..*$/', '', $host ) );
	$name = ucfirst( $slug ) . strstr( $host, '.' ); // ex. modivo.ro → „Modivo.ro"
	return array( $slug, $name ?: $host );
}

/**
 * Descarcă o pagină de produs și extrage oferta (nume/preț/monedă/stoc) din
 * JSON-LD Product, cu fallback pe meta og/product. Întoarce array sau null.
 */
function hainute_extract_offer_from_url( $url ) {
	$resp = wp_remote_get(
		$url,
		array(
			'timeout'     => 20,
			'redirection' => 5,
			'headers'     => array(
				'User-Agent'      => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
				'Accept'          => 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language' => 'ro-RO,ro;q=0.9,en;q=0.8',
			),
		)
	);
	if ( is_wp_error( $resp ) ) {
		return null;
	}
	$code = wp_remote_retrieve_response_code( $resp );
	if ( $code < 200 || $code >= 400 ) {
		return null;
	}
	$html = wp_remote_retrieve_body( $resp );
	$out  = array( 'name' => '', 'price' => 0.0, 'currency' => 'RON', 'in_stock' => true );

	// JSON-LD Product.
	if ( preg_match_all( '#<script[^>]+application/ld\+json[^>]*>(.*?)</script>#is', $html, $m ) ) {
		foreach ( $m[1] as $json ) {
			$data = json_decode( trim( $json ), true );
			if ( ! is_array( $data ) ) {
				continue;
			}
			$stack = array( $data );
			while ( $stack ) {
				$o = array_pop( $stack );
				if ( ! is_array( $o ) ) {
					continue;
				}
				$type = $o['@type'] ?? '';
				$type = is_array( $type ) ? implode( ' ', $type ) : $type;
				if ( false !== stripos( (string) $type, 'Product' ) ) {
					if ( ! empty( $o['name'] ) && ! $out['name'] ) {
						$out['name'] = is_string( $o['name'] ) ? $o['name'] : '';
					}
					$offers = $o['offers'] ?? array();
					if ( isset( $offers['@type'] ) || isset( $offers['price'] ) ) {
						$offers = array( $offers );
					}
					$of = is_array( $offers ) ? ( $offers[0] ?? array() ) : array();
					if ( ! empty( $of['price'] ) && ! $out['price'] ) {
						$out['price'] = (float) str_replace( ',', '.', (string) $of['price'] );
					}
					if ( ! empty( $of['priceCurrency'] ) ) {
						$out['currency'] = strtoupper( (string) $of['priceCurrency'] );
					}
					if ( ! empty( $of['availability'] ) ) {
						$out['in_stock'] = (bool) preg_match( '/InStock/i', (string) $of['availability'] );
					}
				}
				foreach ( $o as $v ) {
					if ( is_array( $v ) ) {
						$stack[] = $v;
					}
				}
			}
		}
	}

	// Fallback pe meta (multe SPA-uri pun prețul aici: Farfetch, Modivo etc.).
	if ( ! $out['price'] && preg_match( '#<meta[^>]+(?:property|name)=["\'](?:product:price:amount|og:price:amount)["\'][^>]+content=["\']([\d.,]+)#i', $html, $mm ) ) {
		$out['price'] = (float) str_replace( ',', '.', $mm[1] );
	}
	if ( preg_match( '#<meta[^>]+(?:property|name)=["\'](?:product:price:currency|og:price:currency)["\'][^>]+content=["\']([A-Za-z]{3})#i', $html, $mc ) ) {
		$out['currency'] = strtoupper( $mc[1] );
	}
	if ( ! $out['name'] && preg_match( '#<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)#i', $html, $mt ) ) {
		$out['name'] = html_entity_decode( $mt[1] );
	}
	if ( preg_match( '#<meta[^>]+(?:property|name)=["\'](?:product:availability|og:availability)["\'][^>]+content=["\']([^"\']+)#i', $html, $ma ) ) {
		$out['in_stock'] = (bool) preg_match( '/in.?stock/i', $ma[1] );
	}

	if ( $out['price'] <= 0 ) {
		return null; // fără preț nu e ofertă utilă
	}
	// Normalizează în RON (EUR/PLN/HUF... → RON).
	$out['price']    = hainute_to_ron( $out['price'], $out['currency'] );
	$out['currency'] = 'RON';
	return $out;
}

/**
 * Aplică ofertele MANUALE ale unui produs: pentru fiecare URL din lista dată,
 * extrage și face upsert; șterge ofertele manuale pentru URL-uri scoase.
 * @return array raport [url => stare].
 */
function hainute_apply_manual_offers( $pid, array $urls ) {
	$report   = array();
	$existing = get_post_meta( $pid, '_hainute_manual_offers', true );
	$existing = is_array( $existing ) ? $existing : array();

	$new_urls = array();
	foreach ( $urls as $url ) {
		$url = esc_url_raw( trim( $url ) );
		if ( '' === $url || ! preg_match( '#^https?://#i', $url ) ) {
			continue;
		}
		$new_urls[] = $url;
		list( $slug, $name ) = hainute_store_from_url( $url );
		$data = hainute_extract_offer_from_url( $url );
		if ( ! $data ) {
			$report[ $url ] = __( '⚠ nu am putut extrage preț (poate necesită browser / pagina blochează)', 'hainute' );
			continue;
		}
		$store_id = hainute_upsert_store( $name, array( 'network' => 'manual', 'program_id' => $slug, 'website' => $url ) );
		if ( is_wp_error( $store_id ) ) {
			$report[ $url ] = 'eroare magazin';
			continue;
		}
		hainute_upsert_offer(
			$pid,
			(int) $store_id,
			array(
				'network'       => 'manual:' . $slug,
				'external_id'   => $slug . ':' . substr( md5( $url ), 0, 16 ),
				'price'         => (float) $data['price'],
				'currency'      => $data['currency'],
				'stock_status'  => $data['in_stock'] ? HAINUTE_STOCK_IN : HAINUTE_STOCK_OUT,
				'affiliate_url' => $url,
			)
		);
		$report[ $url ] = sprintf( '✓ %s — %.2f %s (%s)', $name, $data['price'], $data['currency'], $data['in_stock'] ? __( 'disponibil', 'hainute' ) : __( 'indisponibil', 'hainute' ) );
	}

	// Șterge ofertele manuale pentru URL-uri care nu mai sunt în listă.
	global $wpdb;
	$removed = array_diff( $existing, $new_urls );
	foreach ( $removed as $url ) {
		list( $slug ) = hainute_store_from_url( $url );
		$wpdb->delete(
			hainute_offers_table_name(),
			array( 'product_id' => $pid, 'network' => 'manual:' . $slug, 'external_id' => $slug . ':' . substr( md5( $url ), 0, 16 ) ),
			array( '%d', '%s', '%s' )
		);
	}

	update_post_meta( $pid, '_hainute_manual_offers', $new_urls );
	update_post_meta( $pid, '_hainute_manual_report', $report );
	return $report;
}

// ---- Metabox UI -------------------------------------------------------------

function hainute_register_manual_metabox() {
	add_meta_box( 'hainute-manual', __( 'Cross-check manual + protecție', 'hainute' ), 'hainute_render_manual_metabox', 'product', 'normal', 'high' );
}
add_action( 'add_meta_boxes', 'hainute_register_manual_metabox' );

function hainute_render_manual_metabox( $post ) {
	wp_nonce_field( 'hainute_manual_save', 'hainute_manual_nonce' );
	$urls   = get_post_meta( $post->ID, '_hainute_manual_offers', true );
	$urls   = is_array( $urls ) ? $urls : array();
	$locked = get_post_meta( $post->ID, '_hainute_locked', true );
	$report = get_post_meta( $post->ID, '_hainute_manual_report', true );

	echo '<p><label><strong>' . esc_html__( 'Linkuri cross-check (unul pe linie):', 'hainute' ) . '</strong></label></p>';
	echo '<textarea name="hainute_manual_urls" rows="4" style="width:100%" placeholder="https://www.modivo.ro/p/...&#10;https://www.farfetch.com/ro/...">' . esc_textarea( implode( "\n", $urls ) ) . '</textarea>';
	echo '<p class="description">' . esc_html__( 'La salvare, extrag automat prețul și disponibilitatea din fiecare pagină și le adaug ca oferte pe pagina produsului.', 'hainute' ) . '</p>';

	if ( is_array( $report ) && $report ) {
		echo '<ul style="margin:.5em 0;padding-left:1.2em">';
		foreach ( $report as $u => $st ) {
			echo '<li style="font-size:12px">' . esc_html( $st ) . ' — <span style="color:#777">' . esc_html( wp_parse_url( $u, PHP_URL_HOST ) ) . '</span></li>';
		}
		echo '</ul>';
	}

	// Ascunde magazine din comparator (chiar dacă cross-check-ul e automat).
	$hidden = get_post_meta( $post->ID, '_hainute_hidden_stores', true );
	$hidden = is_array( $hidden ) ? array_map( 'intval', $hidden ) : array();
	$offers = function_exists( 'hainute_get_offers' ) ? hainute_get_offers( $post->ID ) : array();
	$seen_s = array();
	if ( $offers ) {
		echo '<hr><p><strong>' . esc_html__( 'Magazine afișate', 'hainute' ) . '</strong> — ' . esc_html__( 'bifează ca să ascunzi un magazin (ex. cross-check nepotrivit):', 'hainute' ) . '</p>';
		foreach ( $offers as $o ) {
			$sid = (int) $o->store_id;
			if ( isset( $seen_s[ $sid ] ) ) {
				continue;
			}
			$seen_s[ $sid ] = 1;
			$nm = $o->store ? $o->store->name : ( '#' . $sid );
			echo '<label style="display:block;margin:2px 0"><input type="checkbox" name="hainute_hide[]" value="' . esc_attr( $sid ) . '" ' . checked( in_array( $sid, $hidden, true ), true, false ) . '> ' . esc_html( $nm ) . ' <span style="color:#777;font-size:12px">(' . esc_html( $o->network ) . ')</span></label>';
		}
	}

	echo '<hr><p><label><input type="checkbox" name="hainute_locked" value="1" ' . checked( $locked, 1, false ) . '> <strong>' . esc_html__( 'Protejează editările mele', 'hainute' ) . '</strong></label></p>';
	echo '<p class="description">' . esc_html__( 'Bifat: sync-urile viitoare NU suprascriu titlul, categoria și descrierea acestui produs. Mărimile, culorile, linkul și disponibilitatea rămân actualizate automat.', 'hainute' ) . '</p>';

	// Buton re-fetch mărimi/culori (marchează produsul → crawlerele îl reiau primul).
	$checked = (int) hainute_stock_checked_time( $post->ID );
	echo '<hr><p><button type="button" class="button" id="hainute-refetch" data-post="' . esc_attr( $post->ID ) . '" data-nonce="' . esc_attr( wp_create_nonce( 'hainute_refetch_' . $post->ID ) ) . '">🔄 ' . esc_html__( 'Re-fetch mărimi/culori', 'hainute' ) . '</button> <span id="hainute-refetch-msg" style="margin-left:8px"></span></p>';
	echo '<p class="description">' . esc_html__( 'Marchează produsul pentru re-crawl prioritar. Apoi rulează crawlerele (answear.js / vb.js / manual.js) și mărimile/culorile se actualizează. Ultima verificare:', 'hainute' ) . ' <strong>' . ( $checked ? esc_html( hainute_ago_ro( $checked ) ) : '—' ) . '</strong></p>';
	?>
	<script>
	(function(){
		var b=document.getElementById('hainute-refetch');
		if(!b)return;
		b.addEventListener('click',function(){
			var msg=document.getElementById('hainute-refetch-msg'); b.disabled=true; msg.textContent='...';
			var fd=new FormData(); fd.append('action','hainute_refetch'); fd.append('post',b.dataset.post); fd.append('nonce',b.dataset.nonce);
			fetch(ajaxurl,{method:'POST',body:fd,credentials:'same-origin'}).then(function(r){return r.json();}).then(function(j){
				msg.textContent=j.data||'gata'; b.disabled=false;
			}).catch(function(){ msg.textContent='eroare'; b.disabled=false; });
		});
	})();
	</script>
	<?php
}

/** AJAX: marchează un produs pentru re-fetch (resetează flag-urile de crawl). */
function hainute_ajax_refetch() {
	$pid = isset( $_POST['post'] ) ? (int) $_POST['post'] : 0;
	if ( ! $pid || ! current_user_can( 'edit_post', $pid ) ) {
		wp_send_json_error( 'neautorizat' );
	}
	if ( ! wp_verify_nonce( sanitize_key( $_POST['nonce'] ?? '' ), 'hainute_refetch_' . $pid ) ) {
		wp_send_json_error( 'nonce invalid' );
	}
	foreach ( array( '_hainute_size_crawled', '_hainute_vb_crawled', '_hainute_fd_crawled', '_hainute_compared', '_hainute_stock_checked' ) as $k ) {
		delete_post_meta( $pid, $k );
	}
	wp_send_json_success( __( '✓ Marcat. Rulează crawlerele și mărimile/culorile se actualizează.', 'hainute' ) );
}
add_action( 'wp_ajax_hainute_refetch', 'hainute_ajax_refetch' );

function hainute_save_manual_metabox( $post_id ) {
	if ( ! isset( $_POST['hainute_manual_nonce'] ) || ! wp_verify_nonce( sanitize_key( $_POST['hainute_manual_nonce'] ), 'hainute_manual_save' ) ) {
		return;
	}
	if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
		return;
	}
	if ( ! current_user_can( 'edit_post', $post_id ) || 'product' !== get_post_type( $post_id ) ) {
		return;
	}

	// Protecție editări.
	update_post_meta( $post_id, '_hainute_locked', empty( $_POST['hainute_locked'] ) ? 0 : 1 );

	// Magazine ascunse din comparator.
	$hide = isset( $_POST['hainute_hide'] ) ? array_values( array_unique( array_map( 'intval', (array) $_POST['hainute_hide'] ) ) ) : array();
	update_post_meta( $post_id, '_hainute_hidden_stores', $hide );

	// Oferte manuale (extrage la salvare).
	$raw  = isset( $_POST['hainute_manual_urls'] ) ? wp_unslash( $_POST['hainute_manual_urls'] ) : '';
	$urls = array_filter( array_map( 'trim', preg_split( '/[\r\n]+/', (string) $raw ) ) );
	if ( function_exists( 'set_time_limit' ) ) {
		@set_time_limit( 60 );
	}
	hainute_apply_manual_offers( $post_id, $urls );
}
add_action( 'save_post_product', 'hainute_save_manual_metabox' );
