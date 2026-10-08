<?php
/**
 * Copiază acest fișier în `config.php` și completează cheile.
 * config.php NU se pune în git (conține secrete).
 *
 * Lasă gol ('') o platformă pe care nu o folosești încă — scriptul o sare.
 */

return array(

	// Câte produse să scoată per feed/advertiser (0 = toate). Pune un număr
	// mic (ex. 200) ca să vezi rapid ce e disponibil fără să tragi tot.
	'per_feed_limit' => 200,

	// Filtru pe categorie/titlu — păstrează doar produsele care conțin unul
	// dintre aceste fragmente (diacritic-insensibil). Gol = tot.
	'keywords'       => array( 'copii', 'copil', 'baiat', 'baieti', 'fata', 'fete', 'bebe', 'kids', 'junior' ),

	// --- 2Performant ---
	'2performant' => array(
		'email'    => 'emailul-tau@exemplu.ro',
		'password' => 'parola-ta',
		// Coduri de feed de scos (gol = toate feed-urile contului).
		'feeds'    => array(),
	),

	// --- CJ Affiliate (Commission Junction) ---
	// PAT: developers.cj.com → Authentication. CID: members.cj.com → Account.
	'cj' => array(
		'token'      => '',   // Personal Access Token
		'company_id' => '',   // Company ID (CID), ~7 cifre
		'keyword'    => 'copii',
	),

	// --- Awin ---
	// Token: ui.awin.com → Toolbox → API. Publisher ID: din contul tău.
	'awin' => array(
		'token'        => '',  // OAuth2 API token
		'publisher_id' => '',
	),
);
