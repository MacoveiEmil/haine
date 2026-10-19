#!/usr/bin/env bash
# Setează parola contului de admin WordPress în containerul Docker.
# Dump-ul din repo (db/hainute.sql) NU conține parola (repo public), deci după
# primul `docker compose up` contul „emil" nu are parolă până nu rulezi asta.
#
# Rulează-l TU (omul), nu un AI: parola o tastezi doar aici, nu apare în fișiere.
#   bash docker/set-admin-password.sh            (user implicit: emil)
#   bash docker/set-admin-password.sh altuser
set -euo pipefail
USER_LOGIN="${1:-emil}"
read -r -s -p "Parola nouă pentru ${USER_LOGIN}: " PASS; echo
read -r -s -p "Repetă parola: " PASS2; echo
[ "$PASS" = "$PASS2" ] || { echo "Parolele diferă."; exit 1; }
[ ${#PASS} -ge 10 ] || { echo "Minim 10 caractere."; exit 1; }
cd "$(dirname "$0")/.."
docker compose exec -T -e HN_USER="$USER_LOGIN" -e HN_PASS="$PASS" wp php -r '
require "/var/www/html/wp-load.php";
$u = get_user_by( "login", getenv( "HN_USER" ) );
if ( ! $u ) { fwrite( STDERR, "Userul nu există.\n" ); exit( 1 ); }
wp_set_password( getenv( "HN_PASS" ), $u->ID );
echo "Parola a fost setată pentru ", $u->user_login, ". Login: http://localhost:8090/wp-login.php\n";
'
