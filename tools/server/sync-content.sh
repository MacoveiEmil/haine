#!/usr/bin/env bash
# Rulează la fiecare minut pe server (cron /etc/cron.d/beestyle-content).
# Aplică pe server ORICE push în GitHub (decizia proprietarului: colaboratorii au mână liberă):
#  - cod temă/plugin: imediat (sunt montate în container);
#  - docker-compose.prod.yml / docker/: repornește containerele;
#  - tools/crawler/: reinstalează dependențele și repornește worker-ul;
#  - content/descrieri/*.json: le publică pe site; verificarea (tools/descrieri.py) NU
#    blochează, doar scrie problemele în content/raport-publicare.md.
# Revenire: `git revert <commit>` + push (se aplică la fel, în 1–2 minute).
set -uo pipefail
cd /opt/beestyle
LOG=/var/log/beestyle-content.log
REPORT=content/raport-publicare.md
COMPOSE="docker compose -f docker-compose.prod.yml"
exec 9>/var/lock/beestyle-content.lock; flock -n 9 || exit 0
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }

git fetch -q origin main || { log "fetch eșuat"; exit 1; }
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] && exit 0
OLD=$(git rev-parse HEAD)
git merge -q --ff-only origin/main || { git rebase -q origin/main || { git rebase --abort; log "merge/rebase eșuat"; exit 1; }; }
CHANGED=$(git diff --name-only "$OLD" HEAD)
log "aplicat $(git rev-parse --short HEAD): $(echo "$CHANGED" | wc -l) fișiere"
RAP="## $(date '+%F %H:%M') ($(git rev-parse --short HEAD), $(git log -1 --format=%an))"$'\n'

if echo "$CHANGED" | grep -qE '^(docker-compose\.prod\.yml|docker/)'; then
  $COMPOSE up -d >> "$LOG" 2>&1 && RAP+="- containerele au fost repornite (configurație Docker modificată)"$'\n'
fi
if echo "$CHANGED" | grep -q '^tools/crawler/'; then
  chown -R crawler:crawler tools/crawler
  (cd tools/crawler && sudo -u crawler npm install --silent --no-audit --no-fund >> "$LOG" 2>&1)
  systemctl restart beestyle-worker && RAP+="- worker-ul de verificare a stocului a fost repornit"$'\n'
fi

DESC=$(echo "$CHANGED" | grep -E '^content/descrieri/[0-9]+\.json$' | while read -r f; do [ -f "$f" ] && echo "$f"; done)
if [ -n "$DESC" ]; then
  C=$($COMPOSE ps -q wp)
  docker exec "$C" sh -c 'rm -rf /tmp/desc && mkdir -p /tmp/desc'
  while read -r f; do
    docker cp "$f" "$C:/tmp/desc/"
    out=$(python3 tools/descrieri.py check "$f" 2>&1)
    if [ $? -eq 0 ]; then RAP+="- PUBLICAT, verificare OK: ${out}"$'\n'; else RAP+="- PUBLICAT, cu probleme la verificare: ${out}"$'\n'; fi
  done <<< "$DESC"
  docker cp tools/server/apply-descriere.php "$C:/tmp/apply-descriere.php"
  docker exec "$C" sh -c 'php /tmp/apply-descriere.php /tmp/desc/*.json' >> "$LOG" 2>&1
  log "descrieri publicate: $(echo "$DESC" | wc -l)"
fi
echo "$CHANGED" | grep -qvE '^content/' && RAP+="- cod/configurație actualizate: $(echo "$CHANGED" | grep -vE '^content/' | head -8 | tr '\n' ' ')"$'\n'

# Raportul (cele mai noi sus) se trimite înapoi în git, ca autorul să vadă rezultatul.
{ echo "# Raport publicare"; echo; echo "$RAP"; [ -f "$REPORT" ] && tail -n +3 "$REPORT"; } > "$REPORT.tmp" && mv "$REPORT.tmp" "$REPORT"
head -c 200000 "$REPORT" > "$REPORT.tmp" && mv "$REPORT.tmp" "$REPORT"
git add "$REPORT" && git commit -q -m "Raport publicare" && git push -q origin HEAD:main || log "push raport eșuat"
