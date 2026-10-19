#!/usr/bin/env bash
# Rulează la fiecare minut pe server (cron /etc/cron.d/beestyle-content).
# Ia din GitHub DOAR descrierile (content/), le verifică și le publică.
# Dacă în git apar modificări de cod (orice în afara content/), NU le aplică
# automat: așteaptă aprobarea proprietarului (deploy manual, vezi PROJECT_ROADMAP.md).
set -uo pipefail
cd /opt/beestyle
LOG=/var/log/beestyle-content.log
REPORT=content/raport-publicare.md
COMPOSE="docker compose -f docker-compose.prod.yml"
exec 9>/var/lock/beestyle-content.lock; flock -n 9 || exit 0
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }

git fetch -q origin main || { log "fetch eșuat"; exit 1; }
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] && exit 0

CHANGED=$(git diff --name-only HEAD origin/main)
if echo "$CHANGED" | grep -qv '^content/'; then
  log "în git sunt modificări de cod (în afara content/): aștept aprobare. $(echo "$CHANGED" | grep -v '^content/' | head -5 | tr '\n' ' ')"
  exit 0
fi
git merge -q --ff-only origin/main || { log "merge eșuat (istorie divergentă)"; exit 1; }

DESC=$(echo "$CHANGED" | grep -E '^content/descrieri/[0-9]+\.json$' | while read -r f; do [ -f "$f" ] && echo "$f"; done)
[ -z "$DESC" ] && { log "actualizat content/ (fără descrieri noi)"; exit 0; }

OK=(); RAP="## $(date '+%F %H:%M') ($(git rev-parse --short HEAD))"$'\n'
while read -r f; do
  out=$(python3 tools/descrieri.py check "$f" 2>&1)
  if [ $? -eq 0 ]; then OK+=("$f"); RAP+="- PUBLICAT: ${out}"$'\n'; else RAP+="- RESPINS: ${out}"$'\n'; fi
done <<< "$DESC"

if [ ${#OK[@]} -gt 0 ]; then
  C=$($COMPOSE ps -q wp)
  docker exec "$C" sh -c 'rm -rf /tmp/desc && mkdir -p /tmp/desc'
  for f in "${OK[@]}"; do docker cp "$f" "$C:/tmp/desc/"; done
  docker cp tools/server/apply-descriere.php "$C:/tmp/apply-descriere.php"
  docker exec "$C" sh -c 'php /tmp/apply-descriere.php /tmp/desc/*.json' >> "$LOG" 2>&1
fi
log "descrieri: ${#OK[@]} publicate din $(echo "$DESC" | wc -l)"

# Raportul (cele mai noi sus) se trimite înapoi în git, ca autorul să vadă ce s-a publicat/respins.
{ echo "# Raport publicare descrieri"; echo; echo "$RAP"; [ -f "$REPORT" ] && tail -n +3 "$REPORT"; } > "$REPORT.tmp" && mv "$REPORT.tmp" "$REPORT"
head -c 200000 "$REPORT" > "$REPORT.tmp" && mv "$REPORT.tmp" "$REPORT"
git add "$REPORT" && git commit -q -m "Raport publicare descrieri" && git push -q origin HEAD:main || log "push raport eșuat"
