# Import de drafturi pentru un brand nou (Next, En Fant)

Folosit pentru brandurile găsite la magazinele partenere, fără feed afiliat: produsele se creează ca **draft**,
cu ofertele „cross" (`manual:{magazin}`) potrivite de proprietar după poză (Google Lens) sau EAN.
Proprietarul le publică din wp-admin (Produse → Ciorne) după verificare.

## Fluxul (ce rulează unde)

| Pas | Unealta | Rezultat |
|---|---|---|
| 1. Căutare în magazine | `tools/crawler/brand-search.js` (`BRAND="next"`) | `brand-<slug>.json` |
| 2. Citirea paginilor de produs | `brand-scan.js` | `brand-<slug>-produse.json` |
| 3. EAN + lista tuturor produselor | `brand-cross.js` | `brand-<slug>-cross.csv`, `brand-<slug>-produse.csv` |
| 4. Potriviri după poză | `lens.js` (`IN_CSV=…`) + `brand-pick.js` | `brand-<slug>-lens-bifat.csv` (proprietarul bifează `bifa`) |
| 5. Date pentru import | `brand-drafts-build.py` | `wp-content/plugins/hainute-core/data/drafts-brand-v1.json` |
| 6. Fapte pentru descrieri | `brand-desc-extract.js` | `tools/crawler/brand-surse/*.json` (local, nu în git) |
| 7. Descrieri (v7) | `brand-desc-gen.py` + `brand-desc-check.py` | `brand-drafts-desc.json`, intră în fișierul de la pasul 5 |

După pasul 7 se rulează din nou `brand-drafts-build.py` (include descrierile care au trecut verificarea).

## Cum ajunge pe site

`wp-content/plugins/hainute-core/includes/draft-import.php`:
- `hainute_drafts_import_files()` listează fișierele de date; la prima cerere după deploy, o singură dată,
  programează importul în cron-ul WordPress (blocare prin opțiune, expiră după 30 de minute);
- importul e idempotent (cheia `_hainute_import_key`): rulat din nou, sare produsele existente;
- ce creează: produs `draft`, brand (termen nou dacă lipsește), categorie, gen, poze (hotlink), mărimi,
  oferte `manual:{magazin}` cu `_hainute_manual_checked` setat la momentul importului;
- ofertele cross neverificate de 7 zile se ascund (`hainute_offer_is_stale`): worker-ul le reverifică doar după
  publicare, deci un draft publicat după mai mult de 7 zile arată magazinele abia după prima reverificare;
- produsele cu cel mult 2 magazine primesc `_hainute_partner_block`: pe pagină apare „Cauți alte variante?",
  cu linkuri afiliate către pagina principală a magazinelor partenere (apar doar dacă linkul trece prin rețeaua
  de afiliere configurată; fără ea, blocul nu se afișează).

Pentru un lot nou: fișier nou (`drafts-<nume>-v1.json`), adăugat în `hainute_drafts_import_files()`.
Descrieri adăugate ulterior: `hainute_drafts_desc_files()` (fișier `cheie => {html, specs, versiune}`).

## Verificare

- local: `docker compose exec -T wp php -r 'require "/var/www/html/wp-load.php"; print_r(hainute_import_drafts_file("/var/www/html/wp-content/plugins/hainute-core/data/drafts-brand-v1.json"));'`
- pe live: paginile de draft nu se văd public; brandul nou are pagină la `/brand/<slug>/` (200 după import).
