# CLAUDE.md: reguli pentru AI-ul care lucrează pe beestyle.ro

Site-ul se numește **beestyle.ro** (fost hainute.ro; prefixul intern `hainute_` din cod rămâne). Pe server e în **pre-lansare** (încuiat, noindex): nu-l debloca fără acordul proprietarului.

Citește întâi [PROJECT_ROADMAP.md](PROJECT_ROADMAP.md): ce e proiectul, setup, ce urmează.

## Poziționare (obligatoriu, cerința proprietarului)
- beestyle.ro **NU este comparator**. Mesajul: „Găsește mărimea potrivită pentru copilul tău,
  direct la magazinul care o are." Totul se construiește în jurul mărimilor pe stoc.
- Interzis oriunde pe site: „compară", „comparator", „compară prețurile", „cel mai bun preț".
- Interzis în title, meta description, H1, badge-uri și textul linkurilor: preț, reducere,
  ofertă, promoție, cupon, ieftin, „-30%", „cel mai mic preț".
- Prețul rămâne informație secundară: mic, fără preț tăiat, fără procent de reducere.
- Magazinele se ordonează după disponibilitatea mărimii alese, nu după preț.
- Linkurile spre magazine au `rel="sponsored nofollow noopener"`.
- Nu inventa date: o mărime pe care n-am verificat-o e „Mărime neconfirmată", nu „Disponibil".

## Stil
- Limba site-ului: română, cu diacritice corecte (ș, ț cu virgulă).
- **Fără liniuță lungă (em-dash „—")** în texte noi pentru site; folosește virgulă, două puncte sau punct.
- Codul urmează stilul existent (WordPress coding standards în PHP, comentarii în română).
- Descrierile se scriu prin git după `content/prompt-descrieri.md` (fluxul: `content/README.md`);
  serverul aplică orice push în 1–2 minute.

## Git: fiecare modificare ajunge în repo
Proprietarul testează periodic din repo, deci:
1. După fiecare modificare care funcționează: `git add` + `git commit` (mesaj clar, în română) + `git push`.
2. Dacă modificarea a schimbat date în DB (produse, oferte, pagini, setări), exportă și
   snapshot-ul: `bash docker/export-db.sh`, apoi commit `db/hainute.sql`.
3. Nu face force-push și nu rescrie istoria.

## Secrete și date personale (repo PUBLIC)
- Nu comite niciodată: `docker/secrets.env`, `wp-config.php`, `tools/feed-audit/config.php`,
  `secrets.txt`, chei/tokenuri/parole de orice fel (sunt în `.gitignore`; verifică `git status`).
- `db/hainute.sql` se produce DOAR cu `bash docker/export-db.sh` (sanitizează email, parole,
  sesiuni, evenimente). Nu face `mysqldump` direct în `db/`.
- Nu tasta, nu genera și nu cere parole reale. Parola de admin o setează omul cu
  `bash docker/set-admin-password.sh`.
- Valorile din `docker/secrets.env` nu se copiază în cod, documente sau mesaje de commit.

## Mediul local
- Site: http://localhost:8090 (Docker). Tema și pluginul sunt montate din repo, deci editările se
  văd imediat.
- PHP în container: `docker compose exec wp php -r 'require "/var/www/html/wp-load.php"; …'`.
- Crawlerele și worker-ul: `tools/crawler` cu `SITE=http://localhost:8090` și `SECRET` din
  `docker/secrets.env`. Verifică întâi cu `DRYRUN=1` când schimbi un extractor.
- După o modificare de afișare, verifică pagina pe desktop ȘI pe mobil (375px).

## Unde e ce
- Pagina produsului: `wp-content/themes/hainute/single-product.php` +
  `inc/template-tags.php` (`hainute_the_shop_matrix`, `hainute_shop_listings`,
  `hainute_the_product_schema`, `hainute_the_product_intro`) + `assets/js/main.js` (matricea).
- SEO (title, meta, Organization, breadcrumb): `inc/seo.php`. „Cum funcționează" + `/llms.txt`: `inc/how-it-works.php`.
- REST pentru crawlere: `wp-content/plugins/hainute-core/includes/rest.php`, `crosscheck.php`, `recheck.php`.
- Extractoarele per magazin: `tools/crawler/manual.js` (`pageExtract`, `preparePage`).
