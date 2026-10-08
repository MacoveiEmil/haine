# Faza 0 — Discovery (decizii, fără cod)

Data: 2026-07-06

## 1. Feed-uri / API-uri

### 2Performant
- API REST JSON (nu doar CSV static). Autentificare: `POST /users/sign_in` (email+parolă de cont afiliat) → token de sesiune folosit apoi ca header pe restul request-urilor.
- Endpoint relevant pentru noi (cont de afiliat): `GET /affiliate/product_feeds` → listă de feed-uri disponibile (câte unul per advertiser/program la care ești acceptat) și `GET /affiliate/product_feeds/{id}/products` → produsele efective, paginat.
- Câmpuri standard per produs: nume, descriere, mesaj scurt (opțional), preț (poate veni ca `preț_vechi/preț_nou`), categorie + subcategorie, url produs, url-uri imagine (array), id produs (SKU-ul advertiser-ului), brand (opțional), **„în stoc" — flag binar 0/1**, plus un câmp liber „alte date" în JSON/YAML unde unii advertiseri pot pune extra info (ex. cantitate stoc, dacă aleg să o trimită — nu e garantat).
- Nu există rate-limit public documentat clar; presupunem un prag rezonabil (câteva sute de request-uri/oră) — de confirmat empiric după ce avem cont de afiliat aprobat.

### CJ Affiliate (Commission Junction)
- API modern e GraphQL, endpoint `https://ads.api.cj.com/query`, autentificare cu Personal Access Token (Bearer).
- Două moduri relevante: **Product Feed** (tot catalogul unui advertiser, pentru sincronizare bulk) și **Product Search / Product Detail Search** (interogări punctuale, recomandate pentru actualizări aproape în timp real pe un set mic de produse — perfect pentru job-ul orar de re-verificare stoc/preț pe produsele deja importate).
- Feed-urile CJ urmează structura standard de „shopping feed" (similară cu Google Merchant): id, title, description, link, image_link, price, sale_price, **availability** (valori tipice: in_stock / out_of_stock / preorder / backorder), brand, category, condition etc.
- Rate limit-urile exacte (query caps) depind de tier-ul de cont CJ și nu sunt publice fără login în Developer Portal — de confirmat după înscriere ca publisher.

### Concluzie comună — limitare importantă de flagat
**Niciuna dintre cele două rețele nu oferă nativ un status pe 3 nivele (disponibil / stoc critic / indisponibil).** Ambele expun în principal un boolean in-stock/out-of-stock. „Stoc critic" așa cum apare în cerință (ex. pe Nichiduta) nu e un câmp standard de feed nicăieri — de obicei e afișat direct pe site-ul magazinului (JS/HTML), nu în feed.

**Decizie propusă:** tratăm „stoc critic" ca stare **derivată, opțională, per-magazin**, nu ca un câmp garantat din feed:
- Dacă advertiser-ul trimite cantitate în câmpul liber „alte date" (2Performant) sau printr-un câmp non-standard în feed-ul CJ → îl folosim ca să calculăm stoc critic (ex. cantitate ≤ prag configurabil).
- Dacă nu trimite → afișăm doar 2 stări reale: disponibil / indisponibil.
- Nu propun scraping pentru stoc în faza de automatizare completă (ToS risk + fragil), dar rămâne o opțiune punctuală, doar dacă tu decizi explicit pentru un magazin anume, discutată separat.

Asta înseamnă că exemplul din brief („stoc critic pe Nichiduta") va funcționa doar dacă Nichiduta expune acea informație în feed-ul lor prin 2Performant — de verificat de îndată ce avem acces la un feed real.

## 2. Strategie de matching produs cross-store

Pentru că SKU-urile diferă între retaileri, matching-ul se face la nivel de **produs (brand + model), nu de variantă exactă (mărime/culoare)** — panoul de oferte e per magazin, nu per mărime.

Cheie de matching propusă:
1. Normalizare: slugify (fără diacritice, lowercase, fără cuvinte de umplutură tip „pentru copii", „fete", unități de măsură).
2. Cheie primară = `brand_normalizat + nume_normalizat`. Match exact pe cheie → aceeași ofertă agregată.
3. Pentru variații mici de denumire între retaileri → fallback pe similaritate text (ex. trigram/Levenshtein) cu prag de încredere (~0.85). Peste prag → auto-match. Sub prag → tratat ca produs separat (nu blocăm pipeline-ul pentru revizuire manuală, cum ai cerut automatizare completă), dar logăm cazurile „aproape de prag" într-un ecran de admin pentru vizibilitate, fără să opreacă importul.
4. Risc acceptat: vor exista fals-negative (același produs dublat ca 2 intrări separate) mai des decât fals-pozitive — e alegerea mai sigură pentru un site public (nu vrem să amestecăm produse diferite sub aceeași fișă).

Acest task rămâne detaliat separat la Faza 2 (implementare reală a algoritmului), aici doar fixăm direcția.

## 3. Cron — WP-Cron vs cron real

**Decizie: cron real la nivel de server, nu WP-Cron implicit.**
- Dezactivăm pseudo-cron-ul din WordPress (`DISABLE_WP_CRON = true` în `wp-config.php`), ca sincronizarea să nu depindă de trafic pe site.
- Expunem un REST endpoint dedicat (ex. `POST /wp-json/hainute/v1/sync`) protejat printr-un secret/token trimis ca header, nu prin URL public ghicibil.
- Pe hostingul final (odată ales), configurăm un cron job real (cPanel/Plesk cron, sau alternativ un serviciu extern gratuit tip cron-job.org care lovește endpoint-ul HTTPS o dată pe oră) care execută `curl` către endpoint sau, dacă hostingul oferă acces SSH, apelăm direct `wp cron event run` / un script WP-CLI custom — de ales concret când știm hostingul.
- Pentru testare locală (Local by Flywheel): nu există cron real; simulăm rularea job-ului printr-un buton manual în admin (`Rulează sincronizarea acum`) plus, dacă vrei, un `wp-cli` scheduled task local doar pentru dezvoltare.

## 4. Ce rămâne deschis / de confirmat mai târziu
- Rate limits exacte 2Performant/CJ — abia după obținerea conturilor de afiliat reale.
- Ce hosting alegi (afectează exact cum montăm cron-ul real).
- Lista finală de magazine relevante RO pentru haine/încălțăminte copii disponibile prin 2Performant/CJ (Modivo, Fashion Days, Nichiduta menționate — de verificat una câte una dacă rulează prin una din cele două rețele sau alta).

---

Aștept confirmarea ta pe aceste decizii înainte de Faza 1 (scheletul temei WordPress).
