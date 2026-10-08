# Cron de re-verificare a disponibilității

Feed-urile ne dau stocul rar/deloc, iar la afiliere „ultima bucată" se poate epuiza între
două verificări. De aceea reîmprospătăm stocul/mărimile periodic, cu **produsele populare
prioritizate** și cu un **timestamp „verificat ultima dată"** afișat pe pagină.

## Cum funcționează

- `refresh.js cj|fd` cere din `/recrawl-queue` produsele **cele mai vechi verificate**, cu
  cele **fierbinți** (multe vizualizări recente) puse în față. Le re-verifică și marchează
  „verificat acum" (meta `_hainute_stock_checked`).
- Cadență: un produs e scadent după `HAINUTE_RECRAWL_HOURS` (implicit **12h** → de 2x/zi);
  unul fierbinte, după `HAINUTE_RECRAWL_HOT_HOURS` (implicit **2h**).
- `cron.ps1 -Mode daily` rulează ambele surse (rulat de 2x/zi). `-Mode hot` doar produsele
  fierbinți (rulat orar — ieftin, puține produse).

## Programare pe Windows (Local / server Windows)

```powershell
# de 2 ori pe zi (03:30 și 15:30) — catalogul complet
schtasks /Create /TN "hainute-refresh-daily" /SC DAILY /ST 03:30 /RU SYSTEM `
  /TR "powershell -NoProfile -File C:\Users\macov\Documents\Sites\hainute.ro\tools\crawler\cron.ps1 -Mode daily"
schtasks /Change /TN "hainute-refresh-daily" /RI 720 /DU 24:00   # repetă la 12h

# orar — doar produsele fierbinți
schtasks /Create /TN "hainute-refresh-hot" /SC HOURLY /RU SYSTEM `
  /TR "powershell -NoProfile -File C:\Users\macov\Documents\Sites\hainute.ro\tools\crawler\cron.ps1 -Mode hot"
```

## Programare pe Linux (producție)

```cron
# /etc/crontab  (SITE + SECRET setate în mediu sau editate în refresh.js)
30 3,15 * * *  user  cd /var/www/hainute/tools/crawler && SITE=https://hainute.ro node refresh.js cj && node refresh.js fd
17 *   * * *  user  cd /var/www/hainute/tools/crawler && SITE=https://hainute.ro HOT=1 node refresh.js cj hot && node refresh.js fd hot
# cross-check pe alte magazine: la 6h, doar URL-urile neverificate de 10h
45 */6 * * *  user  cd /var/www/hainute/tools/crawler && SITE=https://hainute.ro OLDER=10 node manual.js >> cross.log 2>&1
# ordinea din listări (produsele cu stoc primele): recalcul după crawl-uri
55 */6 * * *  user  curl -s "https://hainute.ro/wp-json/hainute/v1/recompute-buyable?secret=$SECRET" > /dev/null
```

## Reglaje (wp-config.php)

| Constantă | Implicit | Ce face |
|---|---|---|
| `HAINUTE_RECRAWL_HOURS` | 12 | vârsta după care un produs e re-verificat |
| `HAINUTE_RECRAWL_HOT_HOURS` | 2 | idem, pentru produse fierbinți |
| `HAINUTE_HOT_VIEWS` | 8 | vizualizări recente ca să fie „fierbinte" |
| `HAINUTE_VIEW_WINDOW` | 900 | fereastra (sec) în care contează o vizualizare |

Plafon per rulare: env `MAX` (implicit 1200/sursă la `daily`, 150 la `hot`).

## Cross-check pe alte magazine (`manual.js`)

Produsele noastre (din feed-urile de afiliere) au și URL-uri pe alte magazine, găsite
cu Google Lens și validate manual. `manual.js` le verifică periodic cu Chrome real și
actualizează pentru fiecare magazin **prețul, stocul și mărimile disponibile / epuizate**.

- Coada: `/manual-queue` (cele mai vechi verificate primele; `OLDER=10` = doar ce n-a fost
  verificat de 10h). Rezultat: `/manual-result` → ofertă `manual:{magazin}` + meta
  `_hainute_store_sizes` (disponibile) și `_hainute_store_sizes_unavail` (epuizate).
- Import listă nouă: `POST /cross-import` cu `{items:[{id,url}]}` (sare magazinele pe care
  produsul le are deja, inclusiv aceeași rețea în altă țară).
- Linkurile către partenerii de afiliere (Fashion Days, Answear, Sportisimo, various-brands)
  devin automat linkuri afiliate.
- Produs dispărut (404, redirect pe listă, „stoc epuizat" fără preț) → oferta devine
  indisponibilă; nu se inventează preț.

| Env | Implicit | Ce face |
|---|---|---|
| `SITE`, `SECRET` | — | URL-ul site-ului, secretul `HAINUTE_SYNC_SECRET` |
| `CHROME` | Chrome din sistem | calea către Google Chrome (`/usr/bin/google-chrome` pe Linux) |
| `OLDER` | 0 | doar URL-urile neverificate de N ore |
| `HOST`, `IDS`, `LIMIT` | — | doar un magazin / anumite produse / maxim N URL-uri |
| `CONCURRENCY` | 4 | câte magazine în paralel (fiecare magazin rămâne secvențial) |
| `DELAY` | 3500 | pauza (ms, + variație) între două pagini ale aceluiași magazin |
| `BLOCK_LIMIT` | 4 | după atâtea blocări la rând, magazinul e lăsat pe rularea următoare |

### Pe serverul live

- Node 18+, `npm install` în `tools/crawler`, **Google Chrome stable** (nu Chromium-ul
  descărcat de Puppeteer): pe Debian/Ubuntu din repo-ul oficial Google
  (`apt install google-chrome-stable`). Rulează headless, nu trebuie ecran.
- RAM: ~1 GB pentru 4-6 magazine în paralel.
- Crawlerele folosesc versiunea **reală** de Chrome în User-Agent (o versiune falsă,
  diferită de Client Hints, e semnal de bot) și nu descarcă poze/fonturi.
- **Farfetch** (Akamai) blochează browserele automatizate de pe IP-ul de dezvoltare; pe un
  IP de server curat poate merge. Dacă e blocat, ofertele lui pur și simplu nu se creează.

## Worker permanent (`worker.js`): butonul „Reverifică disponibilitatea acum" + refresh periodic

Pe pagina produsului, un editor logat vede butonul **„Reverifică disponibilitatea acum"**.
Butonul pune produsul în coadă (`/recheck`), iar `worker.js` îl ia în câteva secunde, rulează
crawlerele pentru toate magazinele produsului (Answear, Sportisimo, Fashion Days,
various-brands, cross) și raportează (`/recheck-done`). Pagina se reîncarcă singură, de
obicei în ~1 minut. WordPress nu poate rula Chrome, de aceea e nevoie de worker.

Cu `CYCLE_HOURS=6`, worker-ul face și reîmprospătarea periodică (cross neverificate de 6h,
Answear scadente, recalcul stoc) și poate înlocui cron-ul de mai sus.

```bash
# test manual
cd /var/www/hainute/tools/crawler && SITE=https://hainute.ro SECRET=... CYCLE_HOURS=6 node worker.js
```

Serviciu systemd (`/etc/systemd/system/hainute-worker.service`):

```ini
[Unit]
Description=hainute.ro crawler worker
After=network-online.target

[Service]
WorkingDirectory=/var/www/hainute/tools/crawler
Environment=SITE=https://hainute.ro
Environment=SECRET=__HAINUTE_SYNC_SECRET__
Environment=CYCLE_HOURS=6
Environment=CHROME=/usr/bin/google-chrome
ExecStart=/usr/bin/node worker.js
Restart=always
RestartSec=10
User=www-data

[Install]
WantedBy=multi-user.target
```

`systemctl enable --now hainute-worker` · log-uri: `journalctl -u hainute-worker -f`
