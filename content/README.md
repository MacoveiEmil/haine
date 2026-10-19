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
python tools/descrieri.py todo --stoc --limit 10      # ce produse nu au încă descriere v4
node tools/crawler/desc-extract.js --ids 8566,8791    # pagina magazinului → content/surse/{id}.json
# ... AI-ul scrie content/descrieri/{id}.json după content/prompt-descrieri.md ...
python tools/descrieri.py check content/descrieri/8566.json   # trebuie „OK”
git add content/surse content/descrieri && git commit -m "Descrieri v4: 8566, 8791" && git push
```

După 1–2 minute: descrierea e pe `https://beestyle.ro{pagina}`, iar `git pull` aduce
`content/raport-publicare.md` cu rezultatul verificării. Dacă are probleme, corectezi și faci din nou push.

## Formatul `descrieri/{id}.json`

```json
{
 "id": 8566,
 "descriere_html": "<p>…</p><p>…</p><ul><li><strong>…</strong>: …</li></ul><p>…</p><p>…</p>",
 "surse": [ { "fapt": "plasă ușoară", "url": "answear.ro/p/…", "fragment": "text copiat EXACT de pe pagină" } ],
 "specificatii_tehnice": { "Model": "", "Material": "", "Caracteristici": "", "Cod produs": "" },
 "categorie_complementara": { "slug": "/categorie/ghete-cizme/", "motiv": "…" },
 "varsta_orientativa": "4-11 ani",
 "date_insuficiente": false,
 "confidence_notes": []
}
```

Exemple bune: cele 9 fișiere deja existente în `descrieri/` (sunt live pe site).

## Ce verifică `tools/descrieri.py check` (rulează și pe server; nu blochează publicarea, doar raportează)

- fiecare `fragment` din `surse` apare pe pagina magazinului (`surse/{id}.json`);
- 170–240 de cuvinte; paragraful 1 are 40–60; lista are 4–7 puncte, ultimul „Potrivit pentru”;
- exact 3 linkuri: `categorie_principala` din `produse.json` (ancora cu „pentru fete/băieți/bebeluși”
  sau „unisex”), `brand_slug`, și o categorie complementară care există în `categorii.json`;
- cuvintele și formulele interzise din prompt, gen neutru, „orientativ” la vârstă;
- fără nume de magazine, preț sau stoc în text.

## Ce instalezi o dată

Git, Python 3, Node 18+ și Google Chrome. Apoi, în `tools/crawler`: `npm install`.
Dacă Chrome nu e în locul standard: variabila `CHROME=/cale/catre/chrome`.
