<?php
/**
 * Login-ul WordPress e public (fără cheia din docker/gate.php), deci limităm
 * încercările greșite: după 5 parole greșite de pe același IP în 15 minute, IP-ul
 * nu se mai poate loga 15 minute. Utilizatorul corect, de pe alt IP, nu e afectat.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * IP-ul real al vizitatorului. Pe server, WordPress e în spatele lui Caddy
 * (REMOTE_ADDR = containerul Caddy, adresă privată), care pune IP-ul clientului în
 * X-Forwarded-For (și înlocuiește ce trimite clientul, fiindcă nu are proxy-uri de
 * încredere configurate). Antetul se citește DOAR când cererea vine din rețea privată.
 */
function hainute_client_ip() {
	$ip = (string) ( $_SERVER['REMOTE_ADDR'] ?? '' );
	$private = ! filter_var( $ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE );
	if ( $private && ! empty( $_SERVER['HTTP_X_FORWARDED_FOR'] ) ) {
		$first = trim( explode( ',', (string) $_SERVER['HTTP_X_FORWARDED_FOR'] )[0] );
		if ( filter_var( $first, FILTER_VALIDATE_IP ) ) {
			return $first;
		}
	}
	return $ip;
}

function hainute_login_guard_key() {
	return 'hainute_lg_' . md5( hainute_client_ip() );
}

// IP blocat → nici nu verificăm parola.
add_filter(
	'authenticate',
	function ( $user ) {
		$st = get_transient( hainute_login_guard_key() );
		if ( is_array( $st ) && ! empty( $st['until'] ) && $st['until'] > time() ) {
			$min = (int) ceil( ( $st['until'] - time() ) / 60 );
			return new WP_Error( 'hainute_login_blocked', sprintf( 'Prea multe încercări greșite. Încearcă din nou peste %d minute.', $min ) );
		}
		return $user;
	},
	30
);

add_action(
	'wp_login_failed',
	function () {
		$key = hainute_login_guard_key();
		$st  = get_transient( $key );
		$st  = is_array( $st ) ? $st : array( 'n' => 0, 'until' => 0 );
		$st['n']++;
		if ( $st['n'] >= 5 ) {
			$st['until'] = time() + 15 * MINUTE_IN_SECONDS;
		}
		set_transient( $key, $st, 15 * MINUTE_IN_SECONDS );
	}
);

add_action(
	'wp_login',
	function () {
		delete_transient( hainute_login_guard_key() );
	}
);

// Mesaj generic la login greșit: nu spunem dacă utilizatorul există (ajută ghicirea).
add_filter(
	'login_errors',
	function ( $msg ) {
		return false !== strpos( (string) $msg, 'Prea multe încercări' ) ? $msg : 'Utilizator sau parolă greșită.';
	}
);
