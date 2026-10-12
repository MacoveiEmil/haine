<?php
/**
 * Engagement + freshness layer.
 *
 * Trei roluri:
 *  1. „Verificat ultima dată" — un singur timestamp per produs, actualizat de
 *     ORICE crawl de disponibilitate (Answear/FD/various-brands/extern).
 *  2. Popularitate — numărăm vizualizările (all-time + fereastră recentă) ca să
 *     știm care produse sunt „fierbinți" → recrawl prioritar.
 *  3. Vizualizări reale recente ale produsului (fără valori inventate)
 *     (nu exagerat, variază puțin la refresh), înlocuit automat de datele reale
 *     pe măsură ce audiența crește.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Fereastra (secunde) în care o vizualizare contează drept „recentă". */
function hainute_view_window() {
	return (int) hainute_config( 'HAINUTE_VIEW_WINDOW', 900 ); // 15 min
}

/** Câte vizualizări recente fac un produs „fierbinte" (recrawl mai des). */
function hainute_hot_threshold() {
	return (int) hainute_config( 'HAINUTE_HOT_VIEWS', 8 );
}

/**
 * Marchează „disponibilitate verificată acum" pentru un produs. Apelat din
 * toate endpoint-urile de rezultat crawl → un timestamp unic, ușor de afișat.
 */
function hainute_mark_stock_checked( $pid ) {
	update_post_meta( (int) $pid, '_hainute_stock_checked', time() );
}

/**
 * Ultima verificare de disponibilitate (int timestamp). Cade înapoi pe
 * timestamp-urile vechi per-sursă pentru produsele crawluite înainte de unificare.
 */
function hainute_stock_checked_time( $pid ) {
	$pid  = (int) $pid;
	$keys = array( '_hainute_stock_checked', '_hainute_size_crawled', '_hainute_vb_crawled' );
	$max  = 0;
	foreach ( $keys as $k ) {
		$v = (int) get_post_meta( $pid, $k, true );
		if ( $v > $max ) {
			$max = $v;
		}
	}
	return $max;
}

/**
 * Înregistrează o vizualizare: contor all-time + fereastră recentă (transient)
 * pentru „fierbinte" și pentru viitoarea dovadă socială reală.
 */
function hainute_track_view( $pid ) {
	$pid = (int) $pid;
	if ( ! $pid ) {
		return;
	}
	// Total all-time (semnal de reach/priority).
	$total = (int) get_post_meta( $pid, '_hainute_views', true );
	update_post_meta( $pid, '_hainute_views', $total + 1 );

	// Fereastră recentă: listă de timestamp-uri, curățată la fiecare hit.
	$key  = 'hainute_rv_' . $pid;
	$now  = time();
	$win  = hainute_view_window();
	$list = get_transient( $key );
	if ( ! is_array( $list ) ) {
		$list = array();
	}
	$list[] = $now;
	$list   = array_values( array_filter( $list, function ( $t ) use ( $now, $win ) {
		return ( $now - (int) $t ) <= $win;
	} ) );
	if ( count( $list ) > 200 ) {
		$list = array_slice( $list, -200 );
	}
	set_transient( $key, $list, $win * 2 );
}

/** Vizualizări în fereastra recentă (concurență aproximativă). */
function hainute_recent_views( $pid ) {
	$list = get_transient( 'hainute_rv_' . (int) $pid );
	if ( ! is_array( $list ) ) {
		return 0;
	}
	$now = time();
	$win = hainute_view_window();
	$n   = 0;
	foreach ( $list as $t ) {
		if ( ( $now - (int) $t ) <= $win ) {
			$n++;
		}
	}
	return $n;
}

/** Produs „fierbinte" = destule vizualizări recente → merită recrawl rapid. */
function hainute_is_hot( $pid ) {
	return hainute_recent_views( $pid ) >= hainute_hot_threshold();
}

/**
 * „X utilizatori se uită acum". Dummy realist (nu exagerat): o bază stabilă pe
 * ferestre de 10 min, deterministă per produs, plus o mică variație la refresh.
 * Când traficul real depășește dummy-ul, preia valoarea reală.
 */
function hainute_viewers_now( $pid ) {
	// DOAR date reale: un număr inventat de vizitatori e practică comercială
	// înșelătoare (Legea 363/2007). Fără trafic real, elementul nu se afișează.
	return hainute_recent_views( (int) $pid );
}
