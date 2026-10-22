<?php
/**
 * Audit: numărul de magazine cu stoc trebuie să fie același peste tot unde apare
 * (cardul din listări, rezumatul de pe pagina produsului, matricea de mărimi,
 * meta-ul pentru filtrul „Doar în mai multe magazine").
 *
 *   docker compose exec -T wp php /var/www/html/tools/audit-magazine.php
 *   (cu -e WORDPRESS_DB_NAME=srv pentru snapshot-ul de pe server importat separat)
 *
 * Afișează doar produsele cu nepotriviri; ultimul rând = totalul.
 */
require '/var/www/html/wp-load.php';

global $wpdb;
$ids = $wpdb->get_col( "SELECT ID FROM {$wpdb->posts} WHERE post_type='product' AND post_status='publish' ORDER BY ID" );
$bad = 0;
foreach ( $ids as $id ) {
	$id = (int) $id;

	// Cardul (cum îl randează template-parts/product-card.php).
	ob_start();
	$GLOBALS['post'] = get_post( $id );
	setup_postdata( $GLOBALS['post'] );
	get_template_part( 'template-parts/product-card' );
	$html = ob_get_clean();
	$card = '';
	if ( preg_match( '#<p class="card-stores[^"]*">\s*(.*?)\s*</p>#s', $html, $m ) ) {
		$card = trim( html_entity_decode( $m[1] ) );
	}
	$card_n = preg_match( '/^în (\d+) magazine/u', $card, $mm ) ? (int) $mm[1] : ( 'Momentan indisponibil' === $card || '' === $card ? 0 : 1 );

	// Pagina produsului: rezumatul de sub preț.
	$sum = hainute_offer_summary( $id );

	// Pagina produsului: magazinele din matrice care au stoc (grupate după nume, ca pe pagină).
	$matrix = array();
	foreach ( hainute_shop_listings( $id ) as $l ) {
		if ( ! empty( $l['in_stock'] ) && '' !== $l['store'] ) {
			$matrix[ $l['store'] ] = 1;
		}
	}
	$matrix_n = count( $matrix );

	$meta_n = (int) get_post_meta( $id, '_hainute_store_count', true );

	$ok = $card_n === $matrix_n && $sum['stores'] === $matrix_n && ( $meta_n >= 2 ) === ( $matrix_n >= 2 );
	if ( ! $ok ) {
		$bad++;
		printf( "%d\tcard=%s\tpagină=%d\tmatrice=%d (%s)\tmeta=%d\t%s\n", $id, '' === $card ? '-' : $card, $sum['stores'], $matrix_n, implode( ', ', array_keys( $matrix ) ), $meta_n, get_post_field( 'post_name', $id ) );
	}
}
wp_reset_postdata();
printf( "TOTAL: %d produse, %d cu nepotriviri\n", count( $ids ), $bad );
