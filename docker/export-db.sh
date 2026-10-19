#!/usr/bin/env bash
# Exportă DB-ul local în db/hainute.sql, SANITIZAT pentru repo-ul public:
# fără email/parolă admin, fără sesiuni, fără evenimente (sesiuni/referer), fără
# comentarii și transiente. Baza de date locală NU se modifică (lucrăm pe o copie).
#   bash docker/export-db.sh
set -euo pipefail
cd "$(dirname "$0")/.."
docker compose exec -T db sh -c '
set -e
M="mysql -uroot -proot"
$M -e "DROP DATABASE IF EXISTS hn_export; CREATE DATABASE hn_export CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci" 2>/dev/null
mysqldump -uroot -proot --single-transaction --no-tablespaces local 2>/dev/null | $M hn_export 2>/dev/null
$M hn_export 2>/dev/null <<SQL
UPDATE wp_users SET user_email="admin@example.invalid", user_pass="", user_activation_key="", user_url="";
DELETE FROM wp_usermeta WHERE meta_key IN ("session_tokens","community-events-location","wp_dashboard_quick_press_last_post_id");
UPDATE wp_options SET option_value="admin@example.invalid" WHERE option_name IN ("admin_email","new_admin_email");
DELETE FROM wp_options WHERE option_name LIKE "\_transient\_%" OR option_name LIKE "\_site\_transient\_%";
DELETE FROM wp_options WHERE option_name IN ("hainute_recheck_queue","hainute_worker_seen");
TRUNCATE wp_hainute_events;
DELETE FROM wp_comments; DELETE FROM wp_commentmeta;
SQL
mysqldump -uroot -proot --single-transaction --no-tablespaces --skip-dump-date hn_export 2>/dev/null > /tmp/hainute.sql
$M -e "DROP DATABASE hn_export" 2>/dev/null
'
docker compose cp db:/tmp/hainute.sql db/hainute.sql
# Plasă de siguranță: nu lăsăm să plece hash-uri de parolă.
if grep -qE "\\\$(P|wp)\\\$" db/hainute.sql; then echo "EROARE: hash de parolă în dump. Nu comita."; exit 1; fi
echo "OK: db/hainute.sql ($(du -h db/hainute.sql | cut -f1)), sanitizat."
