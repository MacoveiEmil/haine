<?php
/**
 * Verificare status parteneriate pe cele 3 platforme: la ce magazine ești
 * ÎNSCRIS (joined) sau ÎN AȘTEPTARE (pending). Nu scoate produse.
 *
 * Rulare: php -d extension=curl check-partnerships.php
 */

error_reporting( E_ALL & ~E_DEPRECATED );
require __DIR__ . '/lib/common.php';
require __DIR__ . '/lib/twoperformant.php';

$config = require __DIR__ . '/config.php';

fa_log( '===== VERIFICARE PARTENERIATE  ' . date( 'Y-m-d H:i' ) . ' =====' );

/* ---------------- 2Performant ---------------- */
fa_log( "\n### 2Performant ###" );
$auth = fa_2p_signin( $config['2performant']['email'], $config['2performant']['password'] );
if ( isset( $auth['error'] ) ) {
	fa_log( '  ' . $auth['error'] );
} else {
	$seen = array();
	for ( $page = 1; $page <= 20; $page++ ) {
		usleep( 300000 );
		list( $st, $data ) = fa_2p_get( "affiliate/programs.json?page=$page&perpage=50", $auth );
		if ( 200 !== $st ) {
			fa_log( "  programs pagina $page: HTTP $st" );
			break;
		}
		$progs = $data['programs'] ?? array();
		if ( empty( $progs ) ) {
			break;
		}
		foreach ( $progs as $p ) {
			$rel  = $p['relation'] ?? ( $p['status'] ?? '?' );
			$name = $p['name'] ?? '?';
			$seen[ $rel ][] = $name;
		}
		$pg = $data['metadata']['pagination'] ?? array();
		if ( ( (int) ( $pg['pages'] ?? 0 ) && $page >= (int) $pg['pages'] ) || count( $progs ) < 50 ) {
			break;
		}
	}
	foreach ( $seen as $rel => $names ) {
		fa_log( '  [' . $rel . ']: ' . count( $names ) );
		if ( in_array( $rel, array( 'accepted', 'pending', 'approved', 'active' ), true ) ) {
			foreach ( $names as $n ) {
				fa_log( '      - ' . $n );
			}
		}
	}
}

/* ---------------- CJ ---------------- */
fa_log( "\n### CJ Affiliate ###" );
$cj_token = $config['cj']['token'] ?? '';
$cj_cid   = $config['cj']['company_id'] ?? '';
if ( '' === $cj_token ) {
	fa_log( '  lipsă token' );
} else {
	$base = "https://advertiser-lookup.api.cj.com/v3/advertiser-lookup?requestor-cid=$cj_cid";
	foreach ( array( 'joined', 'pending', 'notjoined' ) as $rel ) {
		list( $st, $h, $body ) = fa_http( 'GET', $base . "&advertiser-ids=$rel&records-per-page=100&page-number=1", array( 'Authorization: Bearer ' . $cj_token ) );
		$total = preg_match( '/total-matched="(\d+)"/', $body, $m ) ? (int) $m[1] : 0;
		fa_log( "  [$rel]: $total" );
		if ( in_array( $rel, array( 'joined', 'pending' ), true ) && $total > 0 ) {
			$xml = @simplexml_load_string( $body );
			if ( $xml && isset( $xml->advertisers->advertiser ) ) {
				foreach ( $xml->advertisers->advertiser as $a ) {
					fa_log( '      - ' . (string) $a->{'advertiser-name'} . ' (id ' . (string) $a->{'advertiser-id'} . ')' );
				}
			}
		}
	}
}

/* ---------------- Awin ---------------- */
fa_log( "\n### Awin ###" );
$aw_token = $config['awin']['token'] ?? '';
$aw_pub   = $config['awin']['publisher_id'] ?? '';
if ( '' === $aw_token ) {
	fa_log( '  lipsă token' );
} else {
	foreach ( array( 'joined', 'pending', 'notjoined' ) as $rel ) {
		list( $st, $h, $body ) = fa_http( 'GET', "https://api.awin.com/publishers/$aw_pub/programmes?relationship=$rel", array( 'Authorization: Bearer ' . $aw_token ) );
		$data = json_decode( $body, true );
		$n    = is_array( $data ) ? count( $data ) : 0;
		fa_log( "  [$rel]: $n" );
		if ( in_array( $rel, array( 'joined', 'pending' ), true ) && $n > 0 ) {
			foreach ( $data as $p ) {
				$region = $p['primaryRegion']['countryCode'] ?? '';
				fa_log( '      - ' . ( $p['name'] ?? '?' ) . ( $region ? " [$region]" : '' ) );
			}
		}
	}
}

fa_log( "\n===== gata =====" );
