#!/usr/bin/env bash
# Rulează zilnic pe server (cron /etc/cron.d/beestyle-content, 04:10):
# regenerează content/produse.json + content/categorii.json și snapshot-ul DB
# sanitizat (db/hainute.sql), apoi le trimite în GitHub. Așa git are mereu datele
# la zi, iar cine scrie descrieri lucrează pe lista actuală de produse.
set -uo pipefail
cd /opt/beestyle
LOG=/var/log/beestyle-content.log
COMPOSE="docker compose -f docker-compose.prod.yml"
exec 9>/var/lock/beestyle-content.lock; flock 9
log() { echo "$(date '+%F %T') nightly: $*" >> "$LOG"; }

git fetch -q origin main && git merge -q --ff-only origin/main 2>/dev/null || log "fără merge (modificări de cod în așteptare sau divergență)"

C=$($COMPOSE ps -q wp)
docker cp tools/server/export-content.php "$C:/tmp/export-content.php"
docker exec "$C" sh -c 'rm -rf /tmp/content-out && php /tmp/export-content.php /tmp/content-out' >> "$LOG" 2>&1
docker cp "$C:/tmp/content-out/produse.json" content/produse.json
docker cp "$C:/tmp/content-out/categorii.json" content/categorii.json

# Snapshot DB sanitizat (aceeași logică ca docker/export-db.sh, cu parola de pe server)
sed 's/-uroot -proot/-uroot -p"$MYSQL_ROOT_PASSWORD"/g' docker/export-db.sh > docker/.export-prod.sh
COMPOSE_FILE=docker-compose.prod.yml bash docker/.export-prod.sh >> "$LOG" 2>&1
rm -f docker/.export-prod.sh

git add content/produse.json content/categorii.json db/hainute.sql
git diff --cached --quiet && { log "nimic nou"; exit 0; }
git commit -q -m "Date zilnice de pe server: produse, categorii, snapshot DB" && git push -q origin HEAD:main && log "trimis în git" || log "push eșuat"
