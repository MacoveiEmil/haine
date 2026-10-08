<?php
/**
 * Poze servite doar pe http:// (ex. profitsmart.ro, feed-ul FD/Profitshare):
 * pe un site https browserul le blochează (mixed content) → icon de poză lipsă.
 *
 * Soluția: le copiem o dată în uploads/hainute-img/ și le servim de la noi, pe
 * https. Rescrierea se face la CITIREA meta-urilor de poză, deci acoperă tot
 * site-ul (carduri, galerie, schema, og:image) fără să schimbăm datele din feed.
 * Poza încă necopiată → /wp-json/hainute/v1/img?u=… o descarcă la prima cerere.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/** Hosturile http-only acceptate (nu suntem proxy deschis). */
function hainute_img_proxy_hosts() {
	return apply_filters( 'hainute_img_proxy_hosts', array( 'profitsmart.ro', 'www.profitsmart.ro', '4kidspoint.ro', 'www.4kidspoint.ro' ) );
}

function hainute_img_proxy_allowed( $url ) {
	if ( ! is_string( $url ) || 0 !== strpos( $url, 'http://' ) ) {
		return false;
	}
	return in_array( strtolower( (string) wp_parse_url( $url, PHP_URL_HOST ) ), hainute_img_proxy_hosts(), true );
}

/** Calea + URL-ul copiei locale. */
function hainute_img_proxy_file( $url ) {
	$up  = wp_upload_dir( null, false );
	$ext = strtolower( pathinfo( (string) wp_parse_url( $url, PHP_URL_PATH ), PATHINFO_EXTENSION ) );
	$ext = in_array( $ext, array( 'jpg', 'jpeg', 'png', 'webp', 'gif' ), true ) ? $ext : 'jpg';
	$name = md5( $url ) . '.' . $ext;
	return array( $up['basedir'] . '/hainute-img/' . $name, $up['baseurl'] . '/hainute-img/' . $name );
}

/** Descarcă poza în cache-ul local; întoarce true dacă există copia. */
function hainute_img_proxy_fetch( $url ) {
	list( $path ) = hainute_img_proxy_file( $url );
	if ( file_exists( $path ) ) {
		return true;
	}
	$res = wp_remote_get( $url, array( 'timeout' => 15, 'redirection' => 3 ) );
	if ( is_wp_error( $res ) || 200 !== wp_remote_retrieve_response_code( $res ) ) {
		return false;
	}
	$type = (string) wp_remote_retrieve_header( $res, 'content-type' );
	$body = wp_remote_retrieve_body( $res );
	if ( 0 !== strpos( $type, 'image/' ) || '' === $body || strlen( $body ) > 8 * MB_IN_BYTES ) {
		return false;
	}
	wp_mkdir_p( dirname( $path ) );
	return false !== file_put_contents( $path, $body );
}

/** URL-ul https pentru o poză http-only (copia locală sau endpoint-ul care o creează). */
function hainute_img_secure( $url ) {
	if ( ! hainute_img_proxy_allowed( $url ) ) {
		return $url;
	}
	list( $path, $public ) = hainute_img_proxy_file( $url );
	if ( file_exists( $path ) ) {
		return $public;
	}
	return add_query_arg( 'u', rawurlencode( $url ), rest_url( 'hainute/v1/img' ) );
}

/** Rescrie recursiv (string / array) URL-urile http-only. */
function hainute_img_secure_deep( $v ) {
	if ( is_array( $v ) ) {
		return array_map( 'hainute_img_secure_deep', $v );
	}
	return is_string( $v ) ? hainute_img_secure( $v ) : $v;
}

add_filter(
	'get_post_metadata',
	function ( $value, $object_id, $meta_key, $single ) {
		static $busy = false;
		if ( $busy || is_admin() || ! in_array( $meta_key, array( '_hainute_image_url', '_hainute_gallery', '_hainute_ext_image' ), true ) ) {
			return $value;
		}
		$busy = true;
		$raw  = get_post_meta( $object_id, $meta_key, $single );
		$busy = false;
		$out = hainute_img_secure_deep( maybe_unserialize( $raw ) );
		return $single ? array( $out ) : $out; // filtrul așteaptă array pt $single
	},
	10,
	4
);

add_action(
	'rest_api_init',
	function () {
		register_rest_route(
			'hainute/v1',
			'/img',
			array(
				'methods'             => 'GET',
				'permission_callback' => '__return_true',
				'callback'            => function ( WP_REST_Request $r ) {
					$url = (string) $r->get_param( 'u' );
					if ( ! hainute_img_proxy_allowed( $url ) || ! hainute_img_proxy_fetch( $url ) ) {
						return new WP_Error( 'hainute_img', 'Poză indisponibilă', array( 'status' => 404 ) );
					}
					list( , $public ) = hainute_img_proxy_file( $url );
					wp_safe_redirect( $public, 302 );
					exit;
				},
			)
		);
	}
);
