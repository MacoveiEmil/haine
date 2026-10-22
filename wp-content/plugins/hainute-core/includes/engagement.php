<?php
/**
 * Engagement + freshness layer.
 *
 * Trei roluri:
 *  1. „Verificat ultima dată" — un singur timestamp per produs, actualizat de
 *     ORICE crawl de disponibilitate (Answear/FD/various-brands/extern).
 *  2. Popularitate — numărăm vizualizările (all-time + fereastră recentă) ca să
 *     știm care produse sunt „fierbinți" → recrawl prioritar.
 *  3. Dovada socială pe pagina produsului, doar din vizite reale (fără roboți):
 *     persoanele din ultimele 15 minute sau vizualizările din ultimele 24 de ore.
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

/** Robot / crawler / previzualizare de link: nu e o vizită reală. */
function hainute_is_bot_request() {
	$ua = isset( $_SERVER['HTTP_USER_AGENT'] ) ? (string) $_SERVER['HTTP_USER_AGENT'] : '';
	return '' === $ua || (bool) preg_match( '/bot|crawl|spider|slurp|preview|facebookexternalhit|headless|lighthouse|curl|wget|python|node-fetch|axios|playwright|puppeteer/i', $ua );
}

/**
 * Vizitatorul curent, anonim: hash scurt din IP + browser cu o sare care se
 * schimbă zilnic (nu se poate lega de o persoană și nu se păstrează peste 2 zile).
 * Folosit doar ca un refresh să nu fie numărat drept altă persoană.
 */
function hainute_visitor_hash() {
	$ip = isset( $_SERVER['HTTP_CF_CONNECTING_IP'] ) ? (string) $_SERVER['HTTP_CF_CONNECTING_IP'] : (string) ( $_SERVER['REMOTE_ADDR'] ?? '' );
	$ua = (string) ( $_SERVER['HTTP_USER_AGENT'] ?? '' );
	return substr( hash_hmac( 'sha256', $ip . '|' . $ua, wp_salt( 'nonce' ) . gmdate( 'Y-m-d' ) ), 0, 12 );
}

/**
 * Înregistrează o vizualizare: contor all-time + vizitele din ultimele 24 de ore
 * (transient, [timestamp, hash anonim]) pentru „fierbinte" și dovada socială reală.
 */
function hainute_track_view( $pid ) {
	$pid = (int) $pid;
	if ( ! $pid || hainute_is_bot_request() ) {
		return;
	}
	// Total all-time (semnal de reach/priority).
	$total = (int) get_post_meta( $pid, '_hainute_views', true );
	update_post_meta( $pid, '_hainute_views', $total + 1 );

	// Ultimele 24 de ore: listă curățată la fiecare hit.
	$key    = 'hainute_rv_' . $pid;
	$now    = time();
	$list   = hainute_view_log( $pid );
	$list[] = array( $now, hainute_visitor_hash() );
	if ( count( $list ) > 3000 ) {
		$list = array_slice( $list, -3000 );
	}
	set_transient( $key, $list, 2 * DAY_IN_SECONDS );
}

/** Vizitele din ultimele 24 de ore: [[timestamp, hash], ...]. */
function hainute_view_log( $pid ) {
	$list = get_transient( 'hainute_rv_' . (int) $pid );
	$now  = time();
	$out  = array();
	foreach ( is_array( $list ) ? $list : array() as $v ) {
		$v = is_array( $v ) ? $v : array( (int) $v, '' ); // format vechi: doar timestamp
		if ( ( $now - (int) $v[0] ) <= DAY_IN_SECONDS ) {
			$out[] = $v;
		}
	}
	return $out;
}

/** Vizualizări în ultimele $seconds secunde (implicit fereastra recentă, 15 min). */
function hainute_recent_views( $pid, $seconds = 0 ) {
	$win = $seconds ? (int) $seconds : hainute_view_window();
	$now = time();
	$n   = 0;
	foreach ( hainute_view_log( $pid ) as $v ) {
		if ( ( $now - (int) $v[0] ) <= $win ) {
			$n++;
		}
	}
	return $n;
}

/** Persoane diferite (hash anonim distinct) în fereastra recentă (15 min). */
function hainute_recent_visitors( $pid ) {
	$win  = hainute_view_window();
	$now  = time();
	$seen = array();
	foreach ( hainute_view_log( $pid ) as $v ) {
		if ( ( $now - (int) $v[0] ) <= $win ) {
			$seen[ '' !== (string) $v[1] ? (string) $v[1] : 't' . $v[0] ] = 1;
		}
	}
	return count( $seen );
}

/** Produs „fierbinte" = destule vizualizări recente → merită recrawl rapid. */
function hainute_is_hot( $pid ) {
	return hainute_recent_views( $pid ) >= hainute_hot_threshold();
}

/**
 * Dovada socială, DOAR din date reale (un număr inventat de vizitatori e practică
 * comercială înșelătoare, Legea 363/2007):
 *  - minim 5 persoane diferite în ultimele 15 minute → „X persoane în ultimele 15 minute";
 *  - altfel, vizualizările din ultimele 24 de ore → „X vizualizări în ultimele 24 de ore".
 *
 * @return array{n:int,type:string} type = 'acum' | 'zi' | '' (nimic de afișat)
 */
function hainute_viewers_now( $pid ) {
	$now = hainute_recent_visitors( (int) $pid );
	if ( $now >= 5 ) {
		return array( 'n' => $now, 'type' => 'acum' );
	}
	$day = hainute_recent_views( (int) $pid, DAY_IN_SECONDS );
	return array( 'n' => $day, 'type' => $day > 0 ? 'zi' : '' );
}
