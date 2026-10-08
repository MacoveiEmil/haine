<?php
/**
 * Extrage lista de advertiseri (parteneri) din CJ prin API-ul REST
 * advertiser-lookup (XML), cu status-ul relației (joined/notjoined/pending)
 * și categoria. Scrie output/cj-advertisers.csv.
 *
 * Rulare: php -d extension=curl cj-advertisers.php
 */

error_reporting( E_ALL & ~E_DEPRECATED );
require __DIR__ . '/lib/common.php';

$config = require __DIR__ . '/config.php';
$token  = $config['cj']['token'] ?? '';
$cid    = $config['cj']['company_id'] ?? '';

if ( '' === $token || '' === $cid ) {
	exit( "Lipsesc token/company_id CJ în config.php\n" );
}

$base = "https://advertiser-lookup.api.cj.com/v3/advertiser-lookup?requestor-cid=$cid";
$rows = array();

foreach ( array( 'joined', 'notjoined' ) as $rel ) {
	fa_log( "CJ: extrag advertiserii '$rel'..." );
	for ( $page = 1; $page <= 60; $page++ ) {
		$url = $base . "&advertiser-ids=$rel&records-per-page=100&page-number=$page";
		list( $st, $h, $body ) = fa_http( 'GET', $url, array( 'Authorization: Bearer ' . $token ) );
		if ( 200 !== $st ) {
			fa_log( "  pagina $page: HTTP $st — mă opresc" );
			break;
		}

		$xml = @simplexml_load_string( $body );
		if ( ! $xml || ! isset( $xml->advertisers->advertiser ) ) {
			break;
		}

		$count = 0;
		foreach ( $xml->advertisers->advertiser as $a ) {
			$rows[] = array(
				'advertiser_id'     => (string) $a->{'advertiser-id'},
				'advertiser'        => (string) $a->{'advertiser-name'},
				'status_relatie'    => (string) $a->{'relationship-status'},
				'status_cont'       => (string) $a->{'account-status'},
				'categorie_parinte' => (string) $a->{'primary-category'}->parent,
				'categorie_copil'   => (string) $a->{'primary-category'}->child,
				'epc_7zile'         => (string) $a->{'seven-day-epc'},
				'epc_3luni'         => (string) $a->{'three-month-epc'},
				'network_rank'      => (string) $a->{'network-rank'},
				'url_program'       => (string) $a->{'program-url'},
			);
			$count++;
		}

		$total = (int) $xml->advertisers['total-matched'];
		fa_log( "  pagina $page: +$count (total $rel: $total)" );

		if ( $count < 100 ) {
			break; // ultima pagină
		}
		usleep( 200000 );
	}
}

// scrie CSV
$columns = array(
	'advertiser_id', 'advertiser', 'status_relatie', 'status_cont',
	'categorie_parinte', 'categorie_copil', 'epc_7zile', 'epc_3luni',
	'network_rank', 'url_program',
);
fa_write_csv( __DIR__ . '/output/cj-advertisers.csv', $columns, $rows );

fa_log( "\nGata: " . count( $rows ) . " advertiseri → output/cj-advertisers.csv" );
