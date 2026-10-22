<?php
/**
 * Poarta site-ului: rulează din wp-config.php (WORDPRESS_CONFIG_EXTRA), înaintea
 * WordPress. Aceeași pentru local (localhost:8090) și server (beestyle.ro).
 *
 * 1. Adresa site-ului: HAINUTE_SITE_URL (server, ex. https://beestyle.ro) sau
 *    adresa prin care e accesat (local / tunel). Cererile din server către el
 *    însuși (worker-ul pe 127.0.0.1:8090) folosesc adresa locală.
 * 2. PRE-LANSARE (HAINUTE_PRELAUNCH=1): fără cookie de acces, orice pagină
 *    răspunde „Site în pregătire" (401); robots.txt blochează tot și fiecare
 *    răspuns are „X-Robots-Tag: noindex, nofollow". Acces o dată prin
 *    /?acces=HAINUTE_PRELAUNCH_KEY (cookie 30 de zile). La lansare:
 *    HAINUTE_PRELAUNCH=0 în docker/secrets.env + repornire.
 * 3. wp-admin pe adresa publică: direct, fără cheie (limită de încercări la login în plugin).
 */

$hn_host  = $_SERVER['HTTP_X_FORWARDED_HOST'] ?? ( $_SERVER['HTTP_HOST'] ?? 'localhost:8090' );
$hn_local = (bool) preg_match( '/^(localhost|127\.0\.0\.1|wp)(:\d+)?$/', $hn_host ) || 'cli' === PHP_SAPI;
if ( 'https' === ( $_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '' ) ) {
	$_SERVER['HTTPS'] = 'on';
}
$hn_site = rtrim( (string) getenv( 'HAINUTE_SITE_URL' ), '/' );
if ( '' !== $hn_site && ! $hn_local ) {
	define( 'WP_HOME', $hn_site );
	define( 'WP_SITEURL', $hn_site );
} else {
	$hn_scheme = ( ! empty( $_SERVER['HTTPS'] ) && 'off' !== $_SERVER['HTTPS'] ) ? 'https' : 'http';
	define( 'WP_HOME', $hn_scheme . '://' . $hn_host );
	define( 'WP_SITEURL', $hn_scheme . '://' . $hn_host );
}
$hn_path   = (string) parse_url( $_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH );
$hn_secure = ! empty( $_SERVER['HTTPS'] ) && 'off' !== $_SERVER['HTTPS'];

// --- 2. Pre-lansare ---------------------------------------------------------
define( 'HAINUTE_PRELAUNCH', '1' === (string) getenv( 'HAINUTE_PRELAUNCH' ) );
if ( HAINUTE_PRELAUNCH && ! $hn_local ) {
	header( 'X-Robots-Tag: noindex, nofollow', true );
	if ( '/robots.txt' === $hn_path ) {
		header( 'Content-Type: text/plain; charset=utf-8' );
		echo "User-agent: *\nDisallow: /\n";
		exit;
	}
	$hn_key = (string) getenv( 'HAINUTE_PRELAUNCH_KEY' );
	$hn_sig = '' !== $hn_key ? hash_hmac( 'sha256', 'prelaunch', $hn_key ) : '';
	if ( '' !== $hn_key && isset( $_GET['acces'] ) && hash_equals( $hn_key, (string) $_GET['acces'] ) ) {
		setcookie( 'hnt_pre', $hn_sig, time() + 30 * 86400, '/', '', $hn_secure, true );
		header( 'Location: ' . ( '' !== $hn_path ? $hn_path : '/' ), true, 302 );
		exit;
	}
	if ( '' === $hn_sig || ! hash_equals( $hn_sig, (string) ( $_COOKIE['hnt_pre'] ?? '' ) ) ) {
		http_response_code( 401 );
		header( 'Content-Type: text/html; charset=utf-8' );
		header( 'Cache-Control: no-store' );
		echo '<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="robots" content="noindex, nofollow">'
			. '<meta name="viewport" content="width=device-width,initial-scale=1"><title>Site în pregătire</title>'
			. '<style>body{font-family:system-ui,sans-serif;display:grid;place-items:center;min-height:100vh;margin:0;background:#faf6ef;color:#1d1d1f}'
			. 'main{max-width:420px;padding:24px;text-align:center}h1{font-size:1.4rem}</style></head>'
			. '<body><main><h1>Site în pregătire</h1><p>Revenim în curând.</p></main></body></html>';
		exit;
	}
}

// --- 3. wp-admin pe adresa publică ----------------------------------------
// Fără cheie din 22.10.2026 (decizia proprietarului): login-ul WordPress e direct pe
// /wp-admin/. Împotriva ghicirii parolei: limita de încercări din
// hainute-core/includes/login-guard.php. Linkul vechi /?admin=... duce doar la wp-admin.
if ( isset( $_GET['admin'] ) && '' !== (string) getenv( 'HAINUTE_ADMIN_KEY' ) && hash_equals( (string) getenv( 'HAINUTE_ADMIN_KEY' ), (string) $_GET['admin'] ) ) {
	header( 'Location: /wp-admin/', true, 302 );
	exit;
}
