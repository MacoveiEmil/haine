<?php
/**
 * Import local de drafturi (test): php tools/import-drafts.php <fișier.json> [--update]
 * Rulează în containerul wp:
 *   docker compose exec -T wp php /var/www/html/wp-content/plugins/hainute-core/../../../tools/import-drafts.php ...
 * (sau copiază fișierul în container). Pe server importul rulează singur, din cron (draft-import.php).
 */
require '/var/www/html/wp-load.php';
$file = $argv[1] ?? '';
$res  = hainute_import_drafts_file( $file, in_array( '--update', $argv, true ) );
echo json_encode( $res, JSON_UNESCAPED_UNICODE ), "\n";
