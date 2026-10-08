# hainute.ro

Găsește mărimea potrivită pentru copilul tău, direct la magazinul care o are. Site WordPress
afiliat pentru haine și încălțăminte de copii: pentru fiecare produs arată ce mărimi sunt pe
stoc și în ce magazin. **Nu este comparator de prețuri.**

- Pornire, setup local, stare și pașii următori: [PROJECT_ROADMAP.md](PROJECT_ROADMAP.md)
- Reguli pentru AI / contributori: [CLAUDE.md](CLAUDE.md)

## Structură

```
wp-content/
  plugins/hainute-core/    ← stratul de date (CPT, taxonomii, tabel oferte, sync)
    hainute-core.php       ← bootstrap
    includes/
      config.php           ← citire chei API din wp-config.php / env
      install.php          ← creare tabel {prefix}hainute_offers la activare
      post-types.php       ← CPT product + taxonomii (categorie, brand, gen, vârstă, magazin)
      stores.php           ← helpers pentru magazine (termeni + term meta)
      offers.php           ← CRUD oferte (tabel custom, indexat)
      admin/offers-metabox.php ← metabox read-only cu ofertele pe ecranul produsului
      admin/sync-page.php  ← ecran „Sincronizare" (rulare manuală + log rulări)
      sync/matching.php    ← matching cross-store (cheie normalizată + fuzzy fallback)
      sync/importer.php    ← transformă item-uri normalizate în produse + oferte
      sync/log.php         ← log-ul rulărilor de sincronizare
      sync/sources/mock.php ← sursă mock (citește mock-feeds/*.json)
    mock-feeds/            ← 3 feed-uri simulate (Modivo, Fashion Days, Nichiduta)
  themes/hainute/          ← stratul de afișare (temă custom, fără page builder)
docs/
  faza0-discovery.md       ← deciziile din Faza 0
```

## Instalare (Local by Flywheel / orice WP local)

1. Creează un site WordPress nou în Local.
2. Copiază `wp-content/plugins/hainute-core` și `wp-content/themes/hainute` în `wp-content`-ul site-ului.
3. În admin: activează plugin-ul **Hainute Core** (creează tabelul de oferte), apoi tema **Hainute**.
4. Setări → Permalinkuri → alege „Nume articol" și salvează (necesare pentru URL-urile `/produs/...`).

## Configurare chei API

În `wp-config.php`, deasupra liniei `/* That's all, stop editing! */`:

```php
define( 'HAINUTE_2P_EMAIL', '...' );      // email cont afiliat 2Performant
define( 'HAINUTE_2P_PASSWORD', '...' );   // parolă 2Performant
define( 'HAINUTE_CJ_TOKEN', '...' );      // personal access token CJ Affiliate
define( 'HAINUTE_CJ_COMPANY_ID', '...' ); // company id publisher CJ
define( 'HAINUTE_SYNC_SECRET', '...' );   // secret pentru endpoint-ul de sincronizare
define( 'DISABLE_WP_CRON', true );        // sincronizarea rulează prin cron real, nu WP-Cron
```

Niciodată nu pune aceste valori în cod versionat.

## Cum funcționează datele

- **Produs** = post de tip `product` (titlu, descriere SEO, imagini, taxonomii: categorie / brand / gen / vârstă).
- **Ofertă** = un rând în tabelul custom `{prefix}hainute_offers`: produs + magazin + preț + status stoc (`in_stock` / `low_stock` / `out_of_stock`) + link afiliat + data actualizării. Un produs are 1–3 oferte (câte una per magazin).
- **Magazin** = termen în taxonomia `store`, cu meta: rețea (`2performant` / `cj`), id program afiliere, logo, website.
- „Stoc critic" (`low_stock`) se setează doar când feed-ul expune cantitatea; pragul implicit e ≤ 3 (filtrabil prin `hainute_low_stock_threshold`).

## Sincronizare

Sursele active se decid automat (`includes/sync/runner.php`):
- **2performant** — activă când `HAINUTE_2P_EMAIL` + `HAINUTE_2P_PASSWORD` sunt definite în `wp-config.php`.
- **mock** — activă doar cât timp nu există nicio sursă reală (sau forțat, cu `define( 'HAINUTE_USE_MOCK', true )`).

Fiecare rulare: importă produse noi (max. 150/rulare — restul se amână pentru rulările următoare, filtrabil prin `hainute_max_new_products`), actualizează preț/stoc pentru ofertele existente, face matching cross-store și loghează totul în **Produse → Sincronizare**.

### 2Performant — pași

1. Definește în `wp-config.php`: `HAINUTE_2P_EMAIL`, `HAINUTE_2P_PASSWORD`.
2. În admin, **Produse → Sincronizare → „Testează conexiunea 2Performant"** — nu importă nimic, doar verifică autentificarea, listează feed-urile și pune în log structura brută a primului produs (pentru verificarea mapării).
3. Opțional, tot în `wp-config.php`:
   - `HAINUTE_2P_FEEDS` — coduri de feed de importat, separate prin virgulă (implicit: toate);
   - `HAINUTE_2P_CATEGORIES` — filtru global de categorii: fragmente de nume acceptate din calea de categorie (ex: `copii,fete,baieti`), diacritic-insensibil — restul produselor se sar;
   - `HAINUTE_2P_CATEGORIES_{cod_feed}` — același filtru, dar doar pentru un feed anume (are prioritate față de cel global). Util când un feed e „all products" și vrei doar copiii din el.
4. „Rulează sincronizarea acum" pentru primul import.

**Configurație pentru feed-urile actuale** (Answear Copii = tot; Various Brands = doar copii):

```php
define( 'HAINUTE_2P_FEEDS', '2085,4272' );          // Answear Copii + Various Brands
define( 'HAINUTE_2P_CATEGORIES_4272', 'copii,fete,baieti,baietei,bebe' ); // Various Brands: doar copii
// feed-ul 2085 (Answear Copii) e deja integral de copii — fără filtru
```

### Profitshare (Fashion Days) — bază copii

Sursă activată când `HAINUTE_PS_USER` + `HAINUTE_PS_KEY` sunt în `wp-config.php`:

```php
define( 'HAINUTE_PS_USER', '<utilizator-profitshare>' );
define( 'HAINUTE_PS_KEY', '...' );
define( 'HAINUTE_PS_ADVERTISERS', '88736' ); // Fashion Days (implicit)
define( 'HAINUTE_PS_MAX_PAGES', 200 );        // pagini ×20 scanate/rulare
```

Fashion Days are ~107k produse (toate categoriile); produsele de copii (~3000) sunt filtrate client-side pe termeni univoci (fără „fata"), excluzând cosmeticele. Un **cursor** (`hainute_ps_cursor`) avansează cu `HAINUTE_PS_MAX_PAGES` pagini la fiecare rulare, ca în timp să acopere tot catalogul (limită API: 60 apeluri/60s). Categoriile Fashion Days sunt neîncrezute → normalizate cu `hainute_canonical_category`. Fără câmp de stoc (în feed = disponibil). Brandurile sport (adidas/Nike/Puma/Vans/Skechers) se suprapun cu various-brands → matching cross-store real.

**Variații:** part_number Fashion Days = `{model}-{codCuloare}_{codMarime}`. Sursa grupează după `{model}` → toate culorile+mărimile unui produs = un singur produs (nu rânduri separate). Se acumulează: culorile (`_hainute_colors`), mărimile (`_hainute_sizes`), plus codurile (`_hainute_color_codes`, `_hainute_size_codes`) pentru numărare sigură fără titlu. Dicționarul global `hainute_size_dict` învață cod-mărime → etichetă din titluri și le aplică la toate produsele cu același cod.

### Cron real (producție)

WP-Cron e dezactivat (`DISABLE_WP_CRON`) pentru că depinde de trafic. În panoul de hosting (cPanel → Cron Jobs) se adaugă un cron orar care lovește endpoint-ul REST:

```
0 * * * * curl -s "https://site.ro/wp-json/hainute/v1/sync?secret=SECRETUL_DIN_WPCONFIG" > /dev/null
```

Endpoint-ul e protejat de `HAINUTE_SYNC_SECRET` (403 fără secret corect, 503 dacă secretul nu e definit). Alternativ, pe hosting cu WP-CLI:

```
0 * * * * cd /home/user/public_html && wp hainute sync --quiet
```

## Cum adaugi un magazin nou (după Faza 2)

Se va face programatic prin `hainute_upsert_store( 'Nume', [ 'network' => '...', 'program_id' => '...' ] )` + configurarea feed-ului în modulul de sync — detalii concrete după implementarea integrărilor.
