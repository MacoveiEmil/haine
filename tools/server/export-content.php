<?php
/**
 * Exportă datele de care are nevoie cine scrie descrieri (om sau AI), fără acces
 * la server: content/produse.json și content/categorii.json. Rulează zilnic pe
 * server (tools/server/nightly.sh) și se comite în git.
 *
 * Rulare (în containerul wp): php export-content.php /cale/catre/content
 */
require '/var/www/html/wp-load.php';

$out = rtrim( $argv[1] ?? '/tmp/content', '/' );
if ( ! is_dir( $out ) ) {
	mkdir( $out, 0775, true );
}

/** URL-ul real al produsului la magazin (din linkul afiliat). */
function hn_real_url( $u ) {
	$u = (string) $u;
	$q = (string) parse_url( $u, PHP_URL_QUERY );
	parse_str( $q, $p );
	foreach ( array( 'url', 'redirect_to', 'redirect' ) as $k ) {
		if ( ! empty( $p[ $k ] ) && preg_match( '#^https?://#', $p[ $k ] ) ) {
			return $p[ $k ];
		}
	}
	return $u;
}

function hn_cat_info( $pid ) {
	$cats = wp_get_object_terms( $pid, 'product_cat' );
	if ( ! $cats ) {
		return array( '', '', '', '' );
	}
	$leaf = $cats[0];
	foreach ( $cats as $c ) {
		if ( count( get_ancestors( $c->term_id, 'product_cat' ) ) > count( get_ancestors( $leaf->term_id, 'product_cat' ) ) ) {
			$leaf = $c;
		}
	}
	$anc  = get_ancestors( $leaf->term_id, 'product_cat' );
	$top  = $anc ? get_term( end( $anc ), 'product_cat' ) : $leaf;
	$lvl2 = count( $anc ) >= 2 ? get_term( $anc[ count( $anc ) - 2 ], 'product_cat' ) : $leaf;
	return array( '/categorie/' . $lvl2->slug . '/', '/categorie/' . $leaf->slug . '/', $top->slug, html_entity_decode( $leaf->name ) );
}

$produse = array();
foreach ( get_posts( array( 'post_type' => 'product', 'post_status' => 'publish', 'numberposts' => -1, 'orderby' => 'ID', 'order' => 'ASC' ) ) as $p ) {
	$own = null;
	foreach ( hainute_get_offers( $p->ID ) as $o ) {
		if ( in_array( $o->network, array( 'cj', 'profitshare', '2performant' ), true ) ) {
			$own = $o;
			break;
		}
	}
	if ( ! $own ) {
		continue;
	}
	list( $main, $leaf, $gen, $leafname ) = hn_cat_info( $p->ID );
	$sizes = array();
	foreach ( function_exists( 'hainute_shop_listings' ) ? hainute_shop_listings( $p->ID ) : array() as $l ) {
		if ( empty( $l['external'] ) ) {
			foreach ( array_merge( (array) $l['sizes'], (array) $l['unavail'] ) as $s ) {
				$sizes[ (string) $s ] = 1;
			}
		}
	}
	$sizes = array_keys( $sizes );
	natcasesort( $sizes );
	$bt = get_the_terms( $p->ID, 'product_brand' );
	$produse[] = array(
		'id'                   => $p->ID,
		'titlu'                => html_entity_decode( get_the_title( $p ) ),
		'brand'                => $bt && ! is_wp_error( $bt ) ? html_entity_decode( $bt[0]->name ) : '',
		'brand_slug'           => $bt && ! is_wp_error( $bt ) ? '/brand/' . $bt[0]->slug . '/' : '',
		'magazin'              => $own->store ? $own->store->name : '',
		'link_afiliat'         => hn_real_url( $own->affiliate_url ),
		'categorie_principala' => $main,
		'categorie_frunza'     => $leaf,
		'tip'                  => $leafname,
		'gen'                  => $gen,
		'marimi'               => array_values( $sizes ),
		'cu_stoc'              => '1' === get_post_meta( $p->ID, '_hainute_buyable', true ),
		'descriere_versiune'   => (string) get_post_meta( $p->ID, '_hainute_desc_version', true ),
		'pagina'               => wp_make_link_relative( get_permalink( $p ) ),
	);
}
$categorii = array();
foreach ( get_terms( array( 'taxonomy' => 'product_cat', 'hide_empty' => false ) ) as $t ) {
	$anc  = array_reverse( get_ancestors( $t->term_id, 'product_cat' ) );
	$path = array_map( function ( $a ) { return html_entity_decode( get_term( $a, 'product_cat' )->name ); }, $anc );
	$path[] = html_entity_decode( $t->name );
	$categorii[] = array( 'slug' => '/categorie/' . $t->slug . '/', 'cale' => implode( ' › ', $path ), 'produse' => (int) $t->count );
}
usort( $categorii, function ( $a, $b ) { return strcmp( $a['cale'], $b['cale'] ); } );

$flags = JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES;
file_put_contents( "$out/produse.json", json_encode( $produse, $flags ) . "\n" );
file_put_contents( "$out/categorii.json", json_encode( $categorii, $flags ) . "\n" );
echo 'produse: ' . count( $produse ) . ', categorii: ' . count( $categorii ) . "\n";
