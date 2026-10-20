# content/: descrierile de produs (beestyle.ro)

Aici se scriu descrierile, prin git. Serverul verifică GitHub **la fiecare minut** și aplică
orice push: descrierile apar pe site în 1–2 minute, iar codul (temă, plugin, crawlere,
configurație) se aplică la fel de repede. Nimeni nu are nevoie de acces la server.

## Ce e în folder

| Fișier | Cine îl scrie | Ce conține |
|---|---|---|
| `produse.json` | serverul, zilnic | toate produsele publicate: `id`, titlu, brand + `brand_slug`, magazin, `link_afiliat` (pagina produsului la magazin), `categorie_principala`, mărimi, `cu_stoc`, `descriere_versiune`, `pagina` |
| `categorii.json` | serverul, zilnic | toate categoriile (`slug`, cale, număr de produse): sursa pentru categoria complementară |
| `surse/{id}.json` | tu (unealta de extracție) | ce scrie pe pagina magazinului, extras acum: sursa faptelor |
| `descrieri/{id}.json` | tu (AI-ul) | descrierea, în formatul de mai jos |
| `prompt-descrieri.md` | oricine îl îmbunătățește | promptul după care se scriu descrierile |
| `reguli-descrieri.json` | odată cu promptul | regulile verificării automate (lungimi, listă, linkuri, fraze interzise) |
| `raport-publicare.md` | serverul | ce s-a aplicat la fiecare push și ce probleme a găsit verificarea, cele mai noi sus |

Poți modifica orice în repo (descrieri, prompt, reguli, cod). `produse.json`, `categorii.json`
și `db/hainute.sql` le rescrie serverul zilnic, deci modificările manuale în ele se pierd.
Orice push ajunge pe site în 1–2 minute: testează înainte. Revenire: `git revert <commit>` + push.

## Prompt nou

Schimbi `content/prompt-descrieri.md` și, ca verificarea să se potrivească, `content/reguli-descrieri.json`
(cuvinte min/max, paragraf 1, puncte în listă, număr de linkuri, fraze interzise în plus).
Crește și `"versiune"` (ex. `"v5"`): `tools/descrieri.py todo` va lista produsele care nu au încă
descriere în noua versiune.

## Fluxul pentru un produs

```bash
git pull                                              # mereu întâi
python tools/descrieri.py todo --stoc --limit 10      # ce produse nu au încă descriere în versiunea curentă
node tools/crawler/desc-extract.js --ids 8566,8791    # pagina magazinului → content/surse/{id}.json
# ... AI-ul scrie content/descrieri/{id}.json după content/prompt-descrieri.md ...
python tools/descrieri.py check content/descrieri/8566.json   # trebuie „OK”
git add content/surse content/descrieri && git commit -m "Descrieri v5: 8566, 8791" && git push
```

După 1–2 minute: descrierea e pe `https://beestyle.ro{pagina}`, iar `git pull` aduce
`content/raport-publicare.md` cu rezultatul verificării. Dacă are probleme, corectezi și faci din nou push.

### Varianta automată, cu Gemini (Google AI Studio, gratuit)

```bash
# cheia: aistudio.google.com → Get API key; se ține DOAR local (repo-ul e public)
echo -n "CHEIA" > ~/.gemini-api-key        # sau variabila GEMINI_API_KEY
node tools/crawler/desc-extract.js --ids 9165,9191
python tools/descrieri-gemini.py 9165 9191  # scrie descrieri/{id}.json, rulează check, corectează (max. 3 încercări)
```

Gemini primește promptul, regulile, un exemplu, categoriile, produsul și sursa. Dacă `check`
găsește probleme, Gemini primește lista și rescrie. Citește textul înainte de push: verificarea
prinde regulile, nu și o frază stângace. Pe planul gratuit, Google poate folosi textele trimise
pentru antrenare (aici sunt doar date publice de pe paginile magazinelor).

## Formatul `descrieri/{id}.json`

```json
{
 "id": 8566,
 "versiune": "v5",
 "descriere_html": "<p>…</p><ul><li><strong>…</strong>: …</li></ul><p>…</p><p>…</p>",
 "surse": [ { "fapt": "plasă ușoară", "url": "answear.ro/p/…", "fragment": "text copiat EXACT de pe pagină" } ],
 "specificatii_tehnice": { "Model": "", "Material": "", "Caracteristici": "", "Cod produs": "" },
 "categorie_complementara": { "slug": "/categorie/ghete-cizme/", "motiv": "…" },
 "varsta_orientativa": "4-11 ani",
 "date_insuficiente": false,
 "confidence_notes": []
}
```

Exemple bune: cele 9 fișiere v5 din `descrieri/` (8566, 8791, 10248, 10749, 11350, 12359, 13584, 14334, 14784).

## Ce verifică `tools/descrieri.py check` (rulează și pe server; nu blochează publicarea, doar raportează)

- fiecare `fragment` din `surse` apare pe pagina magazinului (`surse/{id}.json`);
- pragurile din `reguli-descrieri.json` (v5: 60–200 de cuvinte, paragraful 1 are 20–55, lista 3–6 puncte);
- 2–3 linkuri: categoria produsului (`categorie_frunza` sau `categorie_principala`, în paragraful 1, ancora cu
  „pentru fete/băieți/bebeluși” sau „unisex”), `brand_slug` și, opțional, o categorie complementară din `categorii.json`;
- cuvintele și formulele interzise din prompt, gen neutru, „orientativ” o singură dată;
- `"versiune"` din fișier e cea din `reguli-descrieri.json` (`todo` listează și produsele cu descriere mai veche);
- fără nume de magazine, preț sau stoc în text.

## Ce instalezi o dată

Git, Python 3, Node 18+ și Google Chrome. Apoi, în `tools/crawler`: `npm install`.
Dacă Chrome nu e în locul standard: variabila `CHROME=/cale/catre/chrome`.
