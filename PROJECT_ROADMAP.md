# hainute.ro: project roadmap

Ultima actualizare: 2026-10-08. Documentul de pornire pentru oricine (om sau AI) preia
proiectul pe alt laptop. Regulile de lucru pentru AI sunt în [CLAUDE.md](CLAUDE.md).

## 1. Ce este

Site WordPress afiliat pentru haine și încălțăminte de copii. **Nu este comparator de
prețuri.** Valoarea lui: *„Găsește mărimea potrivită pentru copilul tău, direct la
magazinul care o are."* Pentru fiecare produs arătăm ce mărimi sunt pe stoc și în ce
magazin, cu link (afiliat) spre pagina produsului din magazin.

Stare date (2026-10-08): 1374 produse publicate, 1186 cumpărabile acum. 12 magazine
active: Answear, Sportisimo, FashionDays, various-brands (rețele proprii) + About You,
Zalando, Modivo, epantofi, Sportano, Magicstep, giraffe-shoes, 4kidspoint (oferte „cross",
verificate prin crawler).

## 2. Arhitectura

| Componentă | Unde | Rol |
|---|---|---|
| Plugin `hainute-core` | `wp-content/plugins/hainute-core` | CPT `product`, taxonomii (`product_cat`, `product_brand`, `product_gender`, `product_age`, `store`), tabel `wp_hainute_offers`, import feed-uri, REST API pentru crawlere, recheck la cerere, proxy poze http |
| Tema `hainute` | `wp-content/themes/hainute` | Pagina produsului (matrice mărimi × magazine), listări, filtre, SEO, schema, „Cum funcționează", `/llms.txt` |
| Crawlere | `tools/crawler` (Node + puppeteer-core + Chrome instalat) | Verifică pe paginile magazinelor stocul pe mărimi, prețul, culoarea, poza |
| Worker | `tools/crawler/worker.js` | Rulează permanent: reverificări la cerere (butonul din pagina produsului) + ciclu complet la `CYCLE_HOURS` |
| Docker | `docker-compose.yml` | MySQL 8 + WordPress PHP 8.2 pe `localhost:8090`, tunel Cloudflare opțional |
| Snapshot DB | `db/hainute.sql` | Toate produsele/ofertele/descrierile, **sanitizat** (fără email/parolă admin, fără sesiuni/evenimente) |

### Date cheie
- `wp_hainute_offers`: o ofertă = (product_id, store_id) unică; `network` = `cj` (Answear,
  Sportisimo), `profitshare` (FashionDays), `2performant` (various-brands), `manual:{slug}`
  (cross, găsite de crawler), `external:{slug}` (vechi).
- Meta produs: `_hainute_sizes_available` / `_hainute_sizes_unavailable` (magazinul propriu),
  `_hainute_store_sizes` / `_hainute_store_sizes_unavail` (per magazin cross),
  `_hainute_variant_offers` (alte culori/pagini la același magazin, cu `sizes`, `unavail`,
  `checked`), `_hainute_cross_match` (ean / codculoare / cod / diferit / nesigur),
  `_hainute_buyable`, `_hainute_stock_checked`.
- Ofertele cross neverificate de 7 zile sau marcate `diferit` sunt ascunse
  (`hainute_offer_is_stale`). Variantele neverificate de 7 zile au mărimi „neconfirmate".

### Crawlere (`tools/crawler`)
| Script | Ce face |
|---|---|
| `manual.js` | implicit: ofertele cross (toate magazinele cross). `OWN=1`: ofertele Answear proprii (mărimi + epuizate din `__REACT_QUERY_STATE__`). `VARIANTS=1`: variantele de culoare. `IMAGES=1`: poze variante. `DRYRUN=1`: nu scrie nimic |
| `sportisimo.js` | stoc/mărimi Sportisimo (oferte proprii, `network=cj`) |
| `refresh.js fd` | FashionDays |
| `vb.js` | various-brands |
| `worker.js` | orchestrator: reverificări la cerere + ciclu complet la `CYCLE_HOURS`, lanurile PE RÂND (un singur Chrome odată, prioritate scăzută; în paralel blocau site-ul) |
| `CRON.md` | cum se programează pe server (systemd) |

Env comun: `SITE=http://localhost:8090`, `SECRET=<HAINUTE_SYNC_SECRET>`, `IDS=1,2,3`, `LIMIT`, `DELAY`, `CONCURRENCY`.

## 3. Setup pe un laptop nou

Cerințe: Git, Docker Desktop, Node 18+, Google Chrome.

```bash
git clone https://github.com/MacoveiEmil/haine.git hainute.ro
cd hainute.ro
cp docker/secrets.env.example docker/secrets.env   # apoi completezi valorile (de la proprietar)
docker compose up -d                               # prima pornire importă db/hainute.sql (1-2 min)
bash docker/set-admin-password.sh                  # o rulează OMUL; parola nu ajunge în fișiere
cd tools/crawler && npm install
```

- Site: http://localhost:8090, admin: http://localhost:8090/wp-admin (user `emil`).
- Dacă Chrome nu e în locul standard: `CHROME=/cale/chrome` pentru crawlere.
- Worker (lasă-l pornit cât testezi):
  ```bash
  cd tools/crawler
  SITE=http://localhost:8090 SECRET=$(grep ^HAINUTE_SYNC_SECRET ../../docker/secrets.env | cut -d= -f2) CYCLE_HOURS=6 node worker.js
  ```
  La pornire face imediat un ciclu complet (câteva ore); apoi la fiecare 6 ore.
- Link public de test (Cloudflare quick tunnel, fără cont):
  `docker compose --profile share up -d tunnel` apoi `docker compose logs tunnel` → adresa
  `https://….trycloudflare.com` (se schimbă la fiecare repornire a tunelului). Pe adresa
  publică site-ul are `noindex`, iar wp-admin se deschide doar cu `/?acces=<HAINUTE_ADMIN_KEY>`.
- Resetare completă a DB la snapshot: `docker compose down -v && docker compose up -d`
  (șterge tot ce s-a schimbat local în DB).
- Fișierele temei și pluginului sunt montate direct din repo: editezi, dai refresh.
  Opcache poate servi codul vechi ~2 secunde.

### Snapshot DB (când datele s-au schimbat și vrei să le pui în git)
Comanda e în CLAUDE.md, secțiunea „Snapshot DB". Exportul trebuie sanitizat (repo public).

## 4. Ce s-a făcut (pe scurt)

- Import din feed-uri: CJ (Answear, Sportisimo), Profitshare (FashionDays), 2Performant (various-brands).
- Cross-check: produsele noastre găsite la alte 8 magazine (EAN / cod produs / cod culoare); 548 confirmate, 129 marcate „alt produs" și ascunse.
- Stoc pe mărimi la fiecare magazin, inclusiv mărimile epuizate (tăiate).
- Answear: mărimile citite din starea paginii (`__REACT_QUERY_STATE__`: IN_STOCK / LAST / OUT_OF_STOCK), exacte.
- Variante de culoare per magazin, cu poze proprii; culorile unificate (navy = bleumarin).
- Pagina produsului, mobil-first: H1 + intro cu interval de mărimi și vârstă orientativă, matrice mărimi × magazine, sortare a magazinelor după disponibilitatea mărimii alese, „Mărime neconfirmată" când nu știm, link „Vezi alte {categorie} {gen} în mărimea X" când mărimea e epuizată peste tot, tabel mărime × magazin în HTML, bară sticky pe mobil.
- SEO: titlu `{Brand} {Model} {tip} {gen} {culoare}: vezi ce magazine au mărimea ta`, meta pe mărimi, schema ProductGroup cu `hasVariant` per mărime și oferte per magazin, Organization pe homepage, BreadcrumbList, `/llms.txt`, pagina „Cum funcționează" (în header și footer), `rel="sponsored"` pe linkurile spre magazine. Fără „preț/reducere/ofertă/promoție/cupon/ieftin" în titluri, meta, H1, badge-uri, ancore.
- Prețul e informație secundară (mic, fără preț tăiat, fără procente).
- Descrieri v2 (prompt în `docs/prompt-descrieri-v2.md`).
- Poze `http://` (profitsmart.ro, fără https) servite prin cache local https (`includes/img-proxy.php`); poze moarte → următoarea poză din galerie sau placeholder.
- Reverificare la cerere: buton pe pagina produsului (editori logați) + worker.

## 5. Ce urmează (în ordinea priorității)

1. **Verificare după primul ciclu complet al worker-ului**: produsele raportate (#8488 Geox
   Kalispera, #8566 Geox Sprintye, #12684 Tommy, #8791 Calvin Klein, #11929 Columbia) arată
   mărimile reale? Rulează un eșantion cu `DRYRUN=1` și compară cu magazinele.
2. **Pagini fără stoc** (~230 produse fără niciun magazin cu stoc): decizie de luat
   (rămân indexate cu linkul spre alternative, sau noindex după X zile fără stoc).
3. **Producție**: hosting, domeniu, HTTPS, `HAINUTE_SYNC_SECRET` nou, worker ca serviciu
   systemd (`tools/crawler/CRON.md`), import feed-uri programat, `noindex` scos, sitemap în
   Search Console. Opțiunea `hainute_refresh_hours` (implicit 6) trebuie să corespundă cu
   `CYCLE_HOURS` al worker-ului, pentru că apare în textul site-ului.
4. **Validare schema** în Rich Results Test pe câteva produse (ProductGroup).
5. **Magazine noi** (mai multă acoperire de mărimi): 2Performant are ~550 programe
   disponibile; CJ și Awin la fel. Fiecare magazin nou = extractor în `manual.js` (`pageExtract`).
6. **Descrieri**: nu se regenerează toate fără acordul proprietarului.
7. **Analytics**: tabelul `wp_hainute_events` (click-uri spre magazine) e golit în snapshot;
   de conectat la un raport simplu.

### Reguli de date (de știut când modifici)
- O mărime e „disponibilă" doar dacă o are un magazin CU STOC; restul apar tăiate.
- `_hainute_sizes_instock` („, 28, 30,") = mărimile pe stoc la orice magazin, recalculat de
  `hainute_refresh_buyable` (și la finalul fiecărui ciclu prin `/recompute-buyable`); pe el
  merge filtrul `?marime=`.
- **Genul vine de la magazin, nu din feed** (feed-ul greșea la ~275 de produse), în `includes/gender.php`:
  Answear `sex` G/B/K (sigur); FashionDays și various-brands doar dacă titlul magazinului confirmă
  (la conflict câmp ↔ titlu decide titlul); numele modelului („GIRL", „BOYS", Nike „G"/„B").
  **Fără semnal sigur → Unisex** (arborele „Unisex", oglindă după Fete/Băieți). Mutarea schimbă
  categoria, titlul („Fete" / „Băieți" / „Unisex"), genul (unisex = ambele) și linkurile din
  descriere; jurnal în `_hainute_gender_fix`, sursa în `_hainute_gender_source`. Bebe nu se mută.
- Listările Fete / Băieți includ și produsele Unisex din aceeași categorie (`hainute_include_unisex_in_listing`).
- Linkurile spre categorii din descrieri urmează mereu arborele produsului; linkurile spre categorii
  inexistente se repară automat (`hainute_fix_content_cat_links`).
- Pe pagina produsului, culorile cu stoc vin primele; pagina pornește pe prima culoare cu stoc.

## 6. Probleme cunoscute

- About You / Zalando pot bloca crawlerul (anti-bot) → oferta rămâne cu ultima verificare;
  după 7 zile se ascunde automat.
- Answear împarte uneori același model în mai multe pagini (intervale de mărimi): de aceea
  o mărime poate fi „pe stoc la Answear" prin a doua pagină. E corect.
- Butonul „Sync" din wp-admin nu scrie log (nonce); sync-ul merge prin REST
  `/wp-json/hainute/v1/sync?secret=…`.
