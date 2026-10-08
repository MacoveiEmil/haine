#!/usr/bin/env bash
# Drenează întreaga coadă various-brands: rulează vb.js în bucle până coada e goală.
cd "$(dirname "$0")"
SECRET='pune-aici-un-sir-lung-aleatoriu-abc123xyz'
SITE="${SITE:-http://hainutero.local}"
export SITE SECRET
export DELAY="${DELAY:-800}"
export LIMIT="${LIMIT:-300}"
round=0
while :; do
  round=$((round+1))
  n=$(curl -s "${SITE}/wp-json/hainute/v1/crawl-queue-vb?secret=${SECRET}&limit=300" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{try{console.log(JSON.parse(s).queue.length)}catch(e){console.log(0)}})')
  echo "=== RUNDA $round: $n în coadă ==="
  if [ "$n" -eq 0 ] 2>/dev/null; then echo "COADĂ GOALĂ — gata."; break; fi
  node vb.js
  if [ "$round" -ge 40 ]; then echo "STOP: prea multe runde."; break; fi
done
echo "TOTAL RUNDE: $round"
