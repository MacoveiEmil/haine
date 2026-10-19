# content/: descrierile de produs (beestyle.ro)

Aici se scriu descrierile, prin git. Serverul verifică GitHub **la fiecare minut**: ia
descrierile noi sau modificate, le trece prin verificarea automată și le publică pe site
(în 1–2 minute de la push). Nimeni nu are nevoie de acces la server.

## Ce e în folder

| Fișier | Cine îl scrie | Ce conține |
|---|---|---|
| `produse.json` | serverul, zilnic | toate produsele publicate: `id`, titlu, brand + `brand_slug`, magazin, `link_afiliat` (pagina produsului la magazin), `categorie_principala`, mărimi, `cu_stoc`, `descriere_versiune`, `pagina` |
| `categorii.json` | serverul, zilnic | toate categoriile (`slug`, cale, număr de produse): sursa pentru categoria complementară |
| `surse/{id}.json` | tu (unealta de extracție) | ce scrie pe pagina magazinului, extras acum: sursa faptelor |
| `descrieri/{id}.json` | tu (AI-ul) | descrierea, în formatul de mai jos |
| `raport-publicare.md` | serverul | ce s-a publicat și ce s-a respins (cu motivul), cele mai noi sus |

**Nu modifica** `produse.json`, `categorii.json`, `raport-publicare.md` și nimic din afara
`content/`. Serverul publică automat DOAR ce e în `content/`; orice altă modificare
așteaptă aprobarea proprietarului.

## Fluxul pentru un produs

```bash
git pull                                              # mereu întâi
python tools/descrieri.py todo --stoc --limit 10      # ce produse nu au încă descriere v4
node tools/crawler/desc-extract.js --ids 8566,8791    # pagina magazinului → content/surse/{id}.json
# ... AI-ul scrie content/descrieri/{id}.json după docs/prompt-descrieri-v4.md ...
python tools/descrieri.py check content/descrieri/8566.json   # trebuie „OK”
git add content/surse content/descrieri && git commit -m "Descrieri v4: 8566, 8791" && git push
```

După 1–2 minute: descrierea e pe `https://beestyle.ro{pagina}`, iar `git pull` aduce
`content/raport-publicare.md` cu rezultatul. Dacă e „RESPINS”, corectezi și faci din nou push.

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

## Ce verifică `tools/descrieri.py check` (aceeași verificare rulează pe server)

- fiecare `fragment` din `surse` apare pe pagina magazinului (`surse/{id}.json`);
- 170–240 de cuvinte; paragraful 1 are 40–60; lista are 4–7 puncte, ultimul „Potrivit pentru”;
- exact 3 linkuri: `categorie_principala` din `produse.json` (ancora cu „pentru fete/băieți/bebeluși”
  sau „unisex”), `brand_slug`, și o categorie complementară care există în `categorii.json`;
- cuvintele și formulele interzise din prompt, gen neutru, „orientativ” la vârstă;
- fără nume de magazine, preț sau stoc în text.

## Ce instalezi o dată

Git, Python 3, Node 18+ și Google Chrome. Apoi, în `tools/crawler`: `npm install`.
Dacă Chrome nu e în locul standard: variabila `CHROME=/cale/catre/chrome`.
