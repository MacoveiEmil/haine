<?php
/**
 * Assets — optimizat pentru viteză (Core Web Vitals).
 *
 * - Fontul Nunito Sans e găzduit local (assets/fonts): fără conexiuni la Google
 *   (mai rapid + fără transfer de IP către Google, relevant GDPR). Font variabil:
 *   un fișier per subset acoperă toate grosimile 400-800.
 * - CSS-ul (~6KB gzip) e inline în <head> → zero cereri care blochează randarea.
 * - JS cu `defer`.
 * - Scriptul de emoji WordPress e scos (inutil, o cerere în plus).
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Fonturile, preîncărcate (latin = textul de bază; latin-ext = ă â î ș ț) +
 * preconnect spre CDN-urile de poze (hotlink): conexiunea TLS se deschide în
 * paralel cu HTML-ul, nu abia când browserul dă de primul <img>.
 */
function hainute_font_preload() {
	// Clasa `js` pe <html> înainte de prima randare: CSS-ul poate plia elemente
	// care au nevoie de JS (filtrele de pe mobil) fără salt de layout, iar fără JS
	// ele rămân vizibile.
	echo '<script>document.documentElement.classList.add("js")</script>' . "\n";
	foreach ( array( 'https://img2.ans-media.com', 'https://i.sportisimo.com' ) as $origin ) {
		echo '<link rel="preconnect" href="' . esc_url( $origin ) . '">' . "\n";
	}
	$base = HAINUTE_THEME_URL . '/assets/fonts/';
	echo '<link rel="preload" href="' . esc_url( $base . 'nunito-sans-latin.woff2' ) . '" as="font" type="font/woff2" crossorigin>' . "\n";
	echo '<link rel="preload" href="' . esc_url( $base . 'nunito-sans-latin-ext.woff2' ) . '" as="font" type="font/woff2" crossorigin>' . "\n";
}
add_action( 'wp_head', 'hainute_font_preload', 0 );

/** @font-face + CSS-ul temei, inline. */
function hainute_inline_css() {
	$file = HAINUTE_THEME_DIR . '/assets/css/main.css';
	if ( ! file_exists( $file ) ) {
		return;
	}

	$css = (string) file_get_contents( $file ); // phpcs:ignore WordPress.WP.AlternativeFunctions
	// Minificare ușoară: comentarii + spații redundante.
	$css = preg_replace( '#/\*.*?\*/#s', '', $css );
	$css = preg_replace( '/\s+/', ' ', $css );
	$css = str_replace( array( ' {', '{ ', ' }', '; ', ': ', ', ' ), array( '{', '{', '}', ';', ':', ',' ), $css );

	$base  = HAINUTE_THEME_URL . '/assets/fonts/';
	$range = array(
		'latin-ext' => 'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C4,U+2113,U+2C60-2C7F,U+A720-A7FF',
		'latin'     => 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD',
	);
	// `optional`: dacă fontul (preîncărcat) nu ajunge până la prima randare, pagina rămâne pe
	// fontul de sistem, fără să sară textul la schimbare (CLS); din cache e folosit imediat.
	$faces = '';
	foreach ( $range as $subset => $unicode ) {
		$faces .= '@font-face{font-family:"Nunito Sans";font-style:normal;font-weight:400 800;font-display:optional;'
			. 'src:url(' . esc_url( $base . 'nunito-sans-' . $subset . '.woff2' ) . ') format("woff2");'
			. 'unicode-range:' . $unicode . '}';
	}

	echo '<style id="hainute-css">' . $faces . trim( $css ) . '</style>' . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput -- CSS din tema proprie
}
add_action( 'wp_head', 'hainute_inline_css', 7 );

function hainute_enqueue_assets() {
	// Versiune = filemtime → cache-bust automat la fiecare editare.
	$js = HAINUTE_THEME_DIR . '/assets/js/main.js';

	wp_enqueue_script(
		'hainute-main',
		HAINUTE_THEME_URL . '/assets/js/main.js',
		array(),
		file_exists( $js ) ? (string) filemtime( $js ) : HAINUTE_THEME_VERSION,
		array(
			'in_footer' => true,
			'strategy'  => 'defer',
		)
	);
}
add_action( 'wp_enqueue_scripts', 'hainute_enqueue_assets' );

/** Fără emoji WordPress (script + CSS + DNS prefetch la s.w.org). */
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
remove_action( 'admin_print_scripts', 'print_emoji_detection_script' );
remove_action( 'admin_print_styles', 'print_emoji_styles' );
add_filter( 'emoji_svg_url', '__return_false' );

/** Fără CSS-ul de blocuri Gutenberg pe front (tema nu folosește blocuri). */
add_action(
	'wp_enqueue_scripts',
	function () {
		if ( is_admin() ) {
			return;
		}
		wp_dequeue_style( 'wp-block-library' );
		wp_dequeue_style( 'wp-block-library-theme' );
		wp_dequeue_style( 'global-styles' );
		wp_dequeue_style( 'classic-theme-styles' );
	},
	100
);
