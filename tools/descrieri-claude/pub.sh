#!/usr/bin/env bash
# pub.sh "mesaj" id1 id2 ... : verifică, adaugă și publică descrierile date (push în main → serverul le publică în 1-2 min)
cd "$(dirname "$0")/../.." || exit 1
msg="$1"; shift
files=""; for i in "$@"; do files="$files content/descrieri/$i.json"; done
PYTHONIOENCODING=utf-8 python3 tools/descrieri.py check $files | grep -v " OK$"
for i in "$@"; do git add "content/descrieri/$i.json" "content/surse/$i.json" 2>/dev/null; done
git add tools/descrieri-claude 2>/dev/null
git commit -q -m "$msg

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git pull -q --rebase --autostash origin main && git push -q origin HEAD:main 2>&1 | grep -v "^warning" | tail -2
echo "publicat: $# | total v7: $(grep -l '"versiune": "v7"' content/descrieri/*.json | wc -l)"
