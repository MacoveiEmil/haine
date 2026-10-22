# Descrieri v7 scrise de Claude, în volum

Cerința proprietarului: descrieri v7 (după `content/prompt-descrieri.md` + `content/reguli-descrieri.json`)
pe TOATE produsele publicate, inclusiv cele care au deja v5/v6. Scrise de Claude, nu de Gemini.

## Fluxul (din rădăcina repo-ului)

```bash
PYTHONIOENCODING=utf-8 python3 tools/descrieri-claude/desc_tools.py next 10   # următoarele 10 din todo.txt, cu rezumatul sursei
# scrii tools/descrieri-claude/loturi/bNNN.py (vezi b022.py, b023.py ca model), apoi:
python3 tools/descrieri-claude/loturi/bNNN.py
PYTHONIOENCODING=utf-8 python3 tools/descrieri.py check content/descrieri/ID.json ...   # repari până e totul OK
tools/descrieri-claude/pub.sh "Descrieri v7: lotul NN (branduri)" ID1 ID2 ...           # commit + push în main
```

Push în `main` = publicare automată pe server în 1-2 minute (`tools/server/sync-content.sh`), raport în
`content/raport-publicare.md`. Nu se face niciodată force-push. Repo-ul e public: niciun secret.

- `todo.txt`: ordinea produselor (în stoc întâi), fără duplicatele canonice. `next` sare peste cele deja v7 și peste `sari.txt`.
- `sari.txt`: produse sărite (adulți etc.). Le adaugi aici și scrii motivul în `probleme-catalog.txt`.
- `probleme-catalog.txt`: nepotriviri de catalog (culoare/categorie greșită, produse de adulți) de raportat proprietarului la final.
- Sursele (`content/surse/{id}.json`) sunt extrase deja. Lipsesc doar pentru 5063, 5075, 5123 (stoc epuizat).

## Reguli învățate (pe lângă prompt)

- Fiecare fapt are un fragment copiat EXACT din sursă (după normalizarea spațiilor). Din MAT folosește doar
  compoziția („100% Poliester”), nu prefixul („Material de bază: …”); atenție la ţ/ț, la „Interior:Material textil” fără spațiu.
- Mărimile: prima și ultima din produse.json, scrise exact (ex. „28-40”). Vârsta cu hedge variat (aproximativ, cam, în jur de,
  pe la, de obicei, în general, de regulă, cu aproximație, în mare, undeva între); „orientativ” rar.
- Listă obligatorie 3-6 puncte, introdusă de o frază care se termină cu „:”. Paragraf despre cum vine pe copil (croială,
  reglaj, picior plin/îngust, copil slab/plinuț) dedus doar din fapte.
- p1 25-66 cuvinte, total 80-240. Linkuri: categoria cu ancora de gen în p1 + brandul (+ opțional o categorie complementară).
- Culoarea: forma de bază („albastru”, nu „albaștri”). Fără: —, preț, stoc, reduceri, magazine, „compară”, !, ?, cuvintele
  interzise din reguli (perfect, ideal, stabilitate, aderență, amortiz, respiră, se simte etc.), dimensiuni în cm.
- Verificarea de repetiție (n-grame de 6 cuvinte între descrieri): variază formulările, nu folosi șabloane.
- Produse de adulți (ex. Tommy Jeans DW0DW, mărimi W/L) → `sari.txt` + `probleme-catalog.txt`.
- Cizme/sandale listate la „Pantofi”: descrie produsul real și notează în `probleme-catalog.txt`.

## La final

Raportează proprietarului: „gata”, câte descrieri v7 sunt, lista din `probleme-catalog.txt`, produsele sărite
(5390, 8668, 9443 adulți; 5063, 5075, 5123 fără sursă) și cele 55 de duplicate canonice nescrise.
