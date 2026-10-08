# Feed Audit — inventar produse din 2Performant, CJ și Awin

Tool standalone (fără WordPress) care se conectează la platformele de afiliere,
scoate ce advertiseri/feed-uri ai disponibile și extrage produsele într-un set
de CSV-uri. Util ca să vezi „ce am și ce pot folosi" înainte de integrare.

## Rulare

Are nevoie de PHP cu extensia `curl`. Pe Windows + Local by Flywheel:

```
cd tools/feed-audit
cp config.example.php config.php     # apoi completează cheile în config.php
"C:/Users/<user>/AppData/Local/Programs/Local/resources/extraResources/lightning-services/php-8.2.29+0/bin/win64/php.exe" -d extension=curl audit.php
```

(sau, dacă ai `php` în PATH: `php -d extension=curl audit.php`)

## Configurare (`config.php`)

- `per_feed_limit` — câte produse să scoată per feed (0 = toate).
- `max_pages_per_feed` — câte pagini (×40 produse) scanează max per feed.
- `keywords` — păstrează doar produsele care conțin unul dintre fragmente
  (diacritic-insensibil). Gol = tot. Implicit: termeni de „copii".

### 2Performant
`email` + `password` (contul tău). `feeds` gol = toate feed-urile. Merge deja.

### CJ Affiliate
- `token` — Personal Access Token de la developers.cj.com → Authentication.
- `company_id` — CID din members.cj.com → Account → Account Information.
- Întoarce produse doar de la advertiserii la care ești **înscris**.

### Awin
- `token` — din ui.awin.com → Toolbox → API.
- `publisher_id` — id-ul tău de publisher.
- `feed_url` (opțional) — URL-ul unui feed de produse Awin (Create-a-Feed, CSV).
  Awin nu are API „live" de produse: inventarul de advertiseri vine din API,
  dar produsele se iau din feed-ul descărcabil configurat aici.

## Ieșire (`output/`)

| Fișier | Conținut |
|--------|----------|
| `inventory.csv` | toți advertiserii/feed-urile + nr. total de produse |
| `products-all.csv` | toate produsele, combinate, coloane normalizate |
| `products-2performant.csv` etc. | produsele fiecărei platforme separat |

Coloane produse: platformă, advertiser, external_id, titlu, brand, categorie,
preț, preț_vechi, monedă, disponibil, gtin, url_afiliat, imagine.

## Note

- CSV-urile au BOM UTF-8 (se deschid corect cu diacritice în Excel).
- Conectorii **CJ și Awin** sunt scriși după documentația publică dar **netestați**
  fără credențiale — verifică primul output și spune-mi dacă vreun câmp e greșit.
- La 2Performant, feed-urile mari de adulți (Dama/Bărbați) sunt sărite automat
  dacă nu conțin produse care trec de `keywords`, ca să nu lovim limita de rată.
- `config.php` conține secrete — nu-l pune în git.
