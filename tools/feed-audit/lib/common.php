<?php
/**
 * Helpers comune: HTTP (curl), CSV, normalizare, filtrare pe cuvinte-cheie.
 */

/**
 * Cerere HTTP. Întoarce [status, headers_assoc_lowercase, body_string].
 */
function fa_http( $method, $url, array $headers = array(), $body = null, $timeout = 60 ) {
	$ch = curl_init();
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_URL            => $url,
			CURLOPT_CUSTOMREQUEST  => $method,
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_HEADER         => true,
			CURLOPT_TIMEOUT        => $timeout,
			CURLOPT_HTTPHEADER     => $headers,
			CURLOPT_SSL_VERIFYPEER => false,
			CURLOPT_ENCODING       => '', // acceptă gzip
		)
	);
	if ( null !== $body ) {
		curl_setopt( $ch, CURLOPT_POSTFIELDS, $body );
	}

	$raw = curl_exec( $ch );
	if ( false === $raw ) {
		$err = curl_error( $ch );
		curl_close( $ch );
		return array( 0, array(), 'CURL ERROR: ' . $err );
	}

	$hsize   = curl_getinfo( $ch, CURLINFO_HEADER_SIZE );
	$status  = curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	$hblock  = substr( $raw, 0, $hsize );
	$bodystr = substr( $raw, $hsize );
	curl_close( $ch );

	$hassoc = array();
	foreach ( explode( "\r\n", $hblock ) as $line ) {
		if ( false !== strpos( $line, ':' ) ) {
			list( $k, $v ) = explode( ':', $line, 2 );
			$hassoc[ strtolower( trim( $k ) ) ] = trim( $v );
		}
	}

	return array( $status, $hassoc, $bodystr );
}

/** Fără diacritice, lowercase (pentru filtrare). */
function fa_norm( $s ) {
	$s = @iconv( 'UTF-8', 'ASCII//TRANSLIT//IGNORE', (string) $s );
	return strtolower( (string) $s );
}

/**
 * Produsul trece de filtrul de cuvinte-cheie? (caută în titlu + categorie)
 */
function fa_keyword_ok( array $keywords, $haystack ) {
	if ( empty( $keywords ) ) {
		return true;
	}
	$h = fa_norm( $haystack );
	foreach ( $keywords as $kw ) {
		$k = fa_norm( $kw );
		if ( '' !== $k && false !== strpos( $h, $k ) ) {
			return true;
		}
	}
	return false;
}

/**
 * Produsul e EXCLUS? (conține un termen din lista de excludere — ex. cosmetice)
 */
function fa_excluded( array $exclude, $haystack ) {
	if ( empty( $exclude ) ) {
		return false;
	}
	$h = fa_norm( $haystack );
	foreach ( $exclude as $ex ) {
		$e = fa_norm( $ex );
		if ( '' !== $e && false !== strpos( $h, $e ) ) {
			return true;
		}
	}
	return false;
}

/**
 * Coloanele CSV normalizate — aceleași pentru toate platformele.
 */
function fa_product_columns() {
	return array(
		'platforma', 'advertiser', 'external_id', 'titlu', 'brand',
		'categorie', 'pret', 'pret_vechi', 'moneda', 'disponibil',
		'gtin', 'url_afiliat', 'imagine',
	);
}

/**
 * Scrie un array de rânduri asociative într-un CSV (cu BOM pentru Excel).
 *
 * @param string   $path    Fișierul de ieșire.
 * @param string[] $columns Ordinea coloanelor.
 * @param array[]  $rows    Rânduri asociative.
 */
function fa_write_csv( $path, array $columns, array $rows ) {
	$dir = dirname( $path );
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}

	$fh = fopen( $path, 'w' );
	fwrite( $fh, "\xEF\xBB\xBF" ); // UTF-8 BOM
	fputcsv( $fh, $columns );
	foreach ( $rows as $row ) {
		$line = array();
		foreach ( $columns as $col ) {
			$line[] = isset( $row[ $col ] ) ? $row[ $col ] : '';
		}
		fputcsv( $fh, $line );
	}
	fclose( $fh );
}

/** Log în consolă. */
function fa_log( $msg ) {
	echo $msg . "\n";
}
