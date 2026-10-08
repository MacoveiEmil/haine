#!/usr/bin/env bash
# Mărimi per-culoare pentru tot catalogul: various-brands apoi Answear (FD deja făcut).
cd "$(dirname "$0")"
export SECRET='pune-aici-un-sir-lung-aleatoriu-abc123xyz'
export SITE="${SITE:-http://hainutero.local}"
export DELAY="${DELAY:-700}"
echo "===== $(date '+%H:%M') various-brands ====="
node variant-sizes.js vb
echo "===== $(date '+%H:%M') answear ====="
node variant-sizes.js answear
echo "===== $(date '+%H:%M') GATA ====="
