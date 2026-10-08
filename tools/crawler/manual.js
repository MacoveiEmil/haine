/**
 * Cross-check pe alte magazine pentru hainute.ro.
 *
 * Ia URL-urile cross (din /manual-queue: importate din lista Lens validată sau
 * lipite în admin), le încarcă cu Chrome real și extrage prețul, stocul și
 * MĂRIMILE (disponibile + epuizate), apoi le trimite la /manual-result →
 * oferte în comparator. Rulează și din cron (pe live), ca datele să fie proaspete.
 *
 * Extracție, în ordinea încrederii:
 *  1. JSON-LD ProductGroup / câte un Product per mărime (Zalando, epantofi,
 *     Modivo, AboutYou): disponibilitate exactă pe fiecare mărime.
 *  2. Pagina, pe site-uri care țin mărimile în HTML: Fashion Days (data-gtm-size),
 *     Sportisimo (.p-select), giraffe-shoes (select option), Answear (JSON-LD size).
 *  3. Generic: butoane/pastile de mărime (disabled / tăiate = epuizate).
 *
 * Fiecare magazin e vizitat secvențial, cu pauză + variație; mai multe magazine
 * merg în paralel. După BLOCK_LIMIT blocări la rând, un magazin e lăsat pentru
 * rularea următoare (nu insistăm). Bannerele de cookie nu se acceptă.
 *
 * Rulare:  node manual.js
 * Moduri: implicit = ofertele cross; OWN=1 = ofertele Answear proprii (mărimi din starea paginii); VARIANTS=1 = variantele de culoare; IMAGES=1 = pozele variantelor.
 * Env: SITE, SECRET, HOST=zalando.ro, IDS=1,2,3, LIMIT=200, OLDER=12 (ore, pt cron),
 *      CONCURRENCY=4, DELAY=3500, BLOCK_LIMIT=4, HEADFUL=1, REPORT=fișier.json
 */
const puppeteer = require('puppeteer-core');
const fs = require('fs');

const SITE = process.env.SITE || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const CHROME = process.env.CHROME || (process.platform === 'win32' ? 'C:/Program Files/Google/Chrome/Application/chrome.exe' : '/usr/bin/google-chrome');
const CONCURRENCY = parseInt(process.env.CONCURRENCY || '4', 10);
const DELAY = parseInt(process.env.DELAY || '3500', 10);
const BLOCK_LIMIT = parseInt(process.env.BLOCK_LIMIT || '4', 10);
const RESTART_EVERY = parseInt(process.env.RESTART_EVERY || '20', 10);
const IMAGES = !!process.env.IMAGES; // backfill: doar poza variantei pt ofertele existente
const VARIANTS = !!process.env.VARIANTS; // variantele produselor proprii (crawl-queue-variants)
const OWN = !!process.env.OWN; // ofertele PROPRII Answear (recrawl-queue?source=cj) → crawl-result
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const jitter = (ms) => ms + Math.floor(Math.random() * ms * 0.4);

const COLORS = ['bleumarin', 'negru', 'alb', 'rosu', 'roșu', 'albastru', 'verde', 'roz', 'galben', 'gri', 'maro', 'bej', 'mov', 'portocaliu', 'turcoaz', 'bordo', 'kaki', 'navy', 'black', 'white', 'red', 'blue', 'green', 'pink', 'yellow', 'grey', 'gray', 'brown', 'beige', 'purple', 'orange', 'turquoise', 'burgundy', 'khaki'];
// Prima culoare care APARE în nume („White Black" → white), nu prima din listă.
const colorFrom = (s) => { const n = (s || '').toLowerCase(); let best = '', pos = Infinity; for (const c of COLORS) { const m = n.match(new RegExp('(^|[^a-zăâîșț])' + c + '([^a-zăâîșț]|$)')); if (m && m.index < pos) { pos = m.index; best = c; } } return best; };

// Mod verificare (DRYRUN=1): nu scrie nimic în site; rezultatele merg în DRY_OUT.
const DRYRUN = !!process.env.DRYRUN;
const dryResults = [];
async function api(path, body) {
  if (DRYRUN && body) { dryResults.push({ path, ...body }); return { ok: true, image: body.image || '' }; }
  const url = `${SITE}/wp-json/hainute/v1/${path}${path.includes('?') ? '&' : '?'}secret=${encodeURIComponent(SECRET)}`;
  const r = await fetch(url, body ? { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) } : {});
  if (!r.ok) throw new Error(`${path} HTTP ${r.status}`);
  return r.json();
}

/** Rulează ÎN PAGINĂ. Întoarce tot ce se poate citi despre produs. */
function pageExtract() {
  const host = location.hostname.replace(/^www\./, '');
  const out = { name: '', price: 0, currency: '', in_stock: null, sizes: [], unavailable: [], color: '', method: '', isProduct: false };
  const txt = (e) => (e && e.textContent || '').replace(/\s+/g, ' ').trim();
  const avail = (a) => /InStock|LimitedAvailability|PreOrder|BackOrder/i.test(String(a || ''));
  const sizeName = (s) => (s && typeof s === 'object' ? (s.name || s.value || '') : String(s || '')).trim();

  // ---- 1. JSON-LD ----
  const products = [], groups = [];
  document.querySelectorAll('script[type="application/ld+json"]').forEach((sc) => {
    let j; try { j = JSON.parse(sc.textContent); } catch (e) { return; }
    (function walk(o) {
      if (!o || typeof o !== 'object') return;
      if (Array.isArray(o)) { o.forEach(walk); return; }
      const t = [].concat(o['@type'] || '').join(' ');
      if (/ProductGroup/i.test(t)) groups.push(o);
      else if (/\bProduct\b/i.test(t)) products.push(o);
      for (const k in o) if (o[k] && typeof o[k] === 'object') walk(o[k]);
    })(j);
  });
  const offersOf = (p) => { const r = []; [].concat(p.offers || []).forEach((x) => { if (x && x.offers) r.push(...[].concat(x.offers)); else if (x) r.push(x); }); return r; };
  const main = groups[0] || products[0];
  if (main) {
    out.isProduct = true;
    out.name = String(main.name || '');
    out.color = sizeName(main.color);
  }
  // Variante pe mărime: Product-uri cu `size` (în ProductGroup.hasVariant sau separate).
  let variants = products.filter((p) => sizeName(p.size) && offersOf(p).length);
  if (variants.length >= 2 || (groups.length && variants.length)) {
    // Mai multe culori în același grup? Păstrăm culoarea paginii (din titlu).
    const cols = [...new Set(variants.map((p) => sizeName(p.color).toLowerCase()).filter(Boolean))];
    if (cols.length > 1) {
      const title = (document.title + ' ' + out.name).toLowerCase();
      const pick = cols.find((c) => title.includes(c)) || sizeName(variants[0].color).toLowerCase();
      variants = variants.filter((p) => sizeName(p.color).toLowerCase() === pick);
      out.color = pick;
    }
    let minIn = 0, minAll = 0;
    variants.forEach((p) => {
      const of = offersOf(p)[0] || {};
      const price = parseFloat(String(of.price || of.lowPrice || '').replace(',', '.')) || 0;
      const s = sizeName(p.size);
      if (avail(of.availability)) { out.sizes.push(s); if (price && (!minIn || price < minIn)) minIn = price; }
      else out.unavailable.push(s);
      if (price && (!minAll || price < minAll)) minAll = price;
      if (of.priceCurrency) out.currency = String(of.priceCurrency).toUpperCase();
      if (!out.color && p.color) out.color = sizeName(p.color);
    });
    out.price = minIn || minAll;
    out.in_stock = out.sizes.length > 0;
    out.method = 'ld-variante';
  } else if (main) {
    const ofs = offersOf(main);
    const inOf = ofs.filter((x) => avail(x.availability));
    const pick = inOf[0] || ofs[0] || {};
    out.price = parseFloat(String(pick.price || pick.lowPrice || '').replace(',', '.')) || 0;
    if (pick.priceCurrency) out.currency = String(pick.priceCurrency).toUpperCase();
    if (ofs.length) out.in_stock = inOf.length > 0;
    // Answear: `size` = lista mărimilor DISPONIBILE („140,152,164").
    const sz = sizeName(main.size);
    if (sz) { out.sizes = sz.split(/\s*,\s*/).filter(Boolean); out.method = 'ld-size'; }
    else out.method = 'ld';
  }

  // ---- meta (preț / monedă / stoc) ----
  const meta = (p) => { const m = document.querySelector(`meta[property="${p}"],meta[name="${p}"]`); return m ? m.content : ''; };
  if (!out.price) { const a = parseFloat(String(meta('product:price:amount') || meta('og:price:amount')).replace(',', '.')); if (a) { out.price = a; out.isProduct = true; } }
  if (!out.currency) out.currency = (meta('product:price:currency') || meta('og:price:currency') || '').toUpperCase();
  if (!out.name) out.name = meta('og:title') || document.title;
  // Poza variantei de pe pagina magazinului: JSON-LD image, altfel og:image.
  const pickImg = (v) => { if (!v) return ''; if (Array.isArray(v)) return pickImg(v[0]); if (typeof v === 'object') return String(v.url || v.contentUrl || ''); return String(v); };
  out.image = pickImg((variants && variants[0] && variants[0].image) || (main && main.image)) || meta('og:image') || '';
  if (out.image && out.image.startsWith('//')) out.image = 'https:' + out.image;

  // ---- 2. DOM pe site-uri cunoscute (doar dacă JSON-LD n-a dat mărimi) ----
  const add = (s, ok) => { s = String(s || '').trim(); if (!s) return; if (ok) { if (!out.sizes.includes(s)) out.sizes.push(s); } else if (!out.unavailable.includes(s)) out.unavailable.push(s); };
  const isOff = (e) => e.disabled || e.getAttribute('aria-disabled') === 'true' || e.hasAttribute('disabled')
    || /disabled|unavail|sold|indispon|epuiz|out-of-stock|is-out|--out|inactive|crossed/i.test(String(e.className || ''))
    || (getComputedStyle(e).textDecorationLine || '').includes('line-through');
  const domSizes = !out.sizes.length && !out.unavailable.length;

  if (domSizes && /fashiondays\.ro$/.test(host)) {
    document.querySelectorAll('[data-gtm-size]').forEach((e) => add(e.getAttribute('data-gtm-size'), e.getAttribute('data-gtm-avail') === 'available'));
    if (out.sizes.length || out.unavailable.length) out.method = 'dom-fd';
  } else if (domSizes && /sportisimo\.ro$/.test(host)) {
    // .p-select__option: <button> = disponibil, <div class="...--disabled"> = epuizat.
    // Text: „28 EU", „122-128", „XS". Doar primul bloc (desktop), fără duplicatul mobil.
    const box = document.querySelector('.p-select') || document.querySelector('[class*="p-select"]');
    const rx = /^(\d{2,3}([.,\/-]\d{1,3})?|\d{1,2}Y|XXS|XS|S|M|L|XL|XXL|XXXL)$/i;
    if (box) box.querySelectorAll('.p-select__option').forEach((o) => {
      const sp = o.querySelector('span') || o;
      const t = txt(sp).replace(/\s*EU$/i, '');
      if (!rx.test(t)) return;
      add(t, !/--disabled/.test(String(o.className)) && !o.disabled);
    });
    if (out.sizes.length || out.unavailable.length) out.method = 'dom-sportisimo';
  } else if (domSizes && /giraffe-shoes\.ro$/.test(host)) {
    document.querySelectorAll('select[name^="option"] option').forEach((o) => { if (!o.value) return; const m = txt(o).match(/^(\d{1,3}([.,]5)?)/); if (m) add(m[1], !o.disabled); });
    if (out.sizes.length || out.unavailable.length) out.method = 'dom-giraffe';
  } else if (domSizes && /sportvision\.ro$/.test(host)) {
    // <li data-productsize-name="S" data-productsize-price="319,99"> (doar mărimile listate)
    document.querySelectorAll('li[data-productsize-name]').forEach((li) => add(li.getAttribute('data-productsize-name'), !isOff(li)));
    if (out.sizes.length || out.unavailable.length) out.method = 'dom-sportvision';
  }
  // Magento (Sportano și alții): <select class="super-attribute-select"> cu
  // opțiuni „98 cm" / „104 cm (out of stock)".
  if (!out.sizes.length && !out.unavailable.length) {
    document.querySelectorAll('select.super-attribute-select option').forEach((o) => {
      if (!o.value) return;
      const t = txt(o);
      const off = o.disabled || /out of stock|stoc epuizat|indisponibil|niedost/i.test(t);
      add(t.replace(/\s*\(.*\)\s*$/, ''), !off);
    });
    if (out.sizes.length || out.unavailable.length) out.method += '+dom-magento';
  }
  // giraffe-shoes (OpenCart) n-are preț în date structurate: „339,90 RON Fără TVA: ...".
  if (!out.price && /giraffe-shoes\.ro$/.test(host)) {
    const m = document.body.innerText.match(/(\d{2,4}[.,]\d{2})\s*RON\s*Fără TVA/i);
    if (m) { out.price = parseFloat(m[1].replace(',', '.')); out.currency = 'RON'; out.isProduct = true; }
  }

  // Answear: dropdown-ul de mărimi (deschis de crawler) are și mărimile EPUIZATE
  // („Raportează disponibilitatea"), deci e mai complet decât JSON-LD.
  // Sursa principală: starea React a paginii (__REACT_QUERY_STATE__) are TOATE
  // mărimile produsului cu availability IN_STOCK / LAST / OUT_OF_STOCK.
  if (/answear\.ro$/.test(host) && window.__REACT_QUERY_STATE__) {
    const pid = (location.pathname.match(/-(\d+)$/) || [])[1];
    const cands = [];
    const seen = new Set();
    const walk = (o, depth) => {
      if (!o || typeof o !== 'object' || depth > 14 || seen.has(o)) return;
      seen.add(o);
      if (!Array.isArray(o)) {
        for (const k of Object.keys(o)) {
          const v = o[k];
          if (Array.isArray(v) && v.length && v[0] && typeof v[0] === 'object' && 'name' in v[0] && v[0].variation && 'availability' in v[0].variation) cands.push({ parent: o, arr: v });
        }
      }
      for (const k of Object.keys(o)) walk(o[k], depth + 1);
    };
    try { walk(window.__REACT_QUERY_STATE__, 0); } catch (e) {}
    const best = cands.find((c) => pid && String(c.parent.id) === pid) || cands[0];
    if (best) {
      out.sizes = []; out.unavailable = [];
      best.arr.forEach((x) => add(String(x.name), x.variation.availability !== 'OUT_OF_STOCK'));
      out.method = 'state-answear';
      out.complete = true;
      if (!out.sizes.length) out.soldOut = true;
    }
  }
  if (/answear\.ro$/.test(host) && out.method !== 'state-answear') {
    const items = document.querySelectorAll('li[class*="BaseSelectItem__listItem"]');
    if (items.length) {
      out.sizes = []; out.unavailable = [];
      items.forEach((li) => {
        const lab = li.querySelector('[class*="BaseSelectItem__selectItem__"]') || li;
        const t = txt(lab).split(' ')[0];
        const un = !!li.querySelector('[class*="LabelUnavailable"]') || /Raportează disponibilitatea/i.test(li.innerText || '');
        if (t) add(t, !un);
      });
      out.method = 'dom-answear';
      out.complete = true; // lista completă: ce lipsește din „disponibile" chiar e epuizat
    }
  }

  // ---- 3. Generic: butoane/pastile de mărime ----
  if (!out.sizes.length && !out.unavailable.length) {
    const re = /^(\d{1,3}([.,]\d)?|\d{2,3}\s?-\s?\d{2,3}|\d{1,2}\s?-\s?\d{1,2}\s?(ani|y|luni)|\d{1,2}\s?(ani|y)|xxs|xs|s|m|l|xl|xxl|xxxl|\d?xl)$/i;
    document.querySelectorAll('[class*="size" i] button,[class*="size" i] li,[class*="size" i] a,button[class*="size" i],[class*="pill" i],select[name*="size" i] option,select[id*="size" i] option,[data-testid*="size" i],[role="radio"],[role="option"]').forEach((e) => {
      if (e.closest('table,header,footer,nav')) return;
      const t = txt(e).replace(/\s*(EU|RO)$/i, '');
      if (re.test(t)) add(t, !isOff(e));
    });
    if (out.sizes.length || out.unavailable.length) out.method += '+dom-generic';
  }
  // Format comun între magazine: „134-140 CM" → „134-140", „7_8Y" → „7-8Y", „36 EU" → „36".
  const norm = (s) => String(s).replace(/_/g, '-').replace(/\s*(cm|eu)\.?$/i, '').replace(/\s+/g, ' ').trim();
  out.sizes = [...new Set(out.sizes.map(norm))].filter(Boolean);
  out.unavailable = [...new Set(out.unavailable.map(norm))].filter(Boolean);
  out.unavailable = out.unavailable.filter((s) => !out.sizes.includes(s));
  if (out.in_stock === null) out.in_stock = out.sizes.length ? true : !/stoc epuizat|indisponibil|sold out|out of stock|nu mai este disponibil/i.test(document.body.innerText.slice(0, 20000));
  if (!out.currency) out.currency = 'RON';
  if (!out.color) out.color = '';
  // Pentru verificarea „același produs?": EAN-urile din datele structurate și
  // textul paginii (unde caut codul producătorului).
  out.gtins = [];
  document.querySelectorAll('script[type="application/ld+json"]').forEach((sc) => { for (const m of sc.textContent.matchAll(/"gtin(?:8|12|13|14)?"\s*:\s*"?(\d{8,14})/g)) out.gtins.push(m[1]); });
  out.head = (document.title + ' ' + out.name + ' ' + location.pathname + ' ' + [...document.querySelectorAll('h1')].map((h) => h.textContent).join(' ')).toUpperCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  out.text = (document.title + ' ' + location.href + ' ' + document.body.innerText + ' ' + [...document.querySelectorAll('script[type="application/ld+json"]')].map((x) => x.textContent).join(' ')).toUpperCase().slice(0, 600000);
  // Pagină de produs fără preț, cu mesaj explicit de stoc epuizat (AboutYou își
  // scoate atunci și datele structurate).
  out.soldOut = out.soldOut || !out.price && /stocul este epuizat|stoc epuizat|produsul nu mai este disponibil|sold out|ausverkauft/i.test(document.body.innerText.slice(0, 30000));
  return out;
}

/**
 * Extracția, tolerantă la navigări târzii (unele site-uri, ex. Zalando, își
 * reîncarcă pagina prin JS după load — verificare anti-bot): așteaptă și reia.
 */
async function extractSafe(page) {
  for (let i = 0; i < 4; i++) {
    try {
      const hasBody = await page.evaluate(() => !!document.body);
      if (hasBody) return await page.evaluate(pageExtract);
    } catch (e) {
      if (!/context was destroyed|navigation|detached/i.test(e.message)) throw e;
    }
    await page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 15000 }).catch(() => {});
    await sleep(1500);
  }
  return { isProduct: false, price: 0, sizes: [], unavailable: [], method: 'fără conținut' };
}

/**
 * E ACELAȘI produs? EAN-ul nostru pe pagină → același produs și culoare ('ean');
 * codul producătorului (+ codul de culoare) → același model ('cod' / 'codculoare');
 * pagina are EAN-uri, dar nu pe al nostru și nici codul → alt produs ('diferit');
 * altfel nu se poate spune ('nesigur').
 */
function matchOf(ids, d) {
  if (!ids) return '';
  const T = d.text || '', gt = new Set(d.gtins || []);
  const ean = ids.ean || [];
  if (ean.some((e) => gt.has(e) || gt.has(e.padStart(13, '0')) || T.includes(e))) return 'ean';
  if ((ids.codes || []).some((c) => T.includes(String(c).toUpperCase()))) return ids.color_code && T.includes(ids.color_code) ? 'codculoare' : 'cod';
  if (gt.size && ean.length) return 'diferit';
  // Fără EAN-uri/cod pe pagină: măcar brandul trebuie să apară în titlul sau
  // numele produsului (prinde ex. o geacă Nike pusă la un produs Calvin Klein).
  if (ids.brand && !String(d.head || '').includes(ids.brand)) return 'diferit';
  return 'nesigur';
}

/** Așteaptă datele produsului și deschide selectoarele de mărimi care apar doar la click. */
async function preparePage(page, host) {
  // Așteptăm să apară datele produsului (JSON-LD sau widget-ul de mărimi), nu
  // toată rețeaua; max 10s, apoi extragem ce există.
  await page.waitForFunction(() => {
    if (document.querySelector('[data-gtm-size],.p-select,li[data-productsize-name],select.super-attribute-select,select[name^="option"]')) return true;
    return [...document.querySelectorAll('script[type="application/ld+json"]')].some((s) => /"Product(Group)?"/.test(s.textContent));
  }, { timeout: 10000 }).catch(() => {});
  // Answear: deschide dropdown-ul de mărimi (lista apare doar după click).
  if (/answear\.ro$/.test(host)) {
    await page.waitForSelector('button[class*="BaseSelectDropdown__selectTrigger"]', { timeout: 8000 }).catch(() => {});
    await page.click('button[class*="BaseSelectDropdown__selectTrigger"]').catch(() => page.evaluate(() => { const b = document.querySelector('button[class*="BaseSelectDropdown__selectTrigger"]'); if (b) b.click(); }).catch(() => {}));
    await page.waitForSelector('li[class*="BaseSelectItem__listItem"]', { timeout: 6000 }).catch(() => {});
  }
  // Magento (Sportano): opțiunile de mărime se completează prin JS după load;
  // la unele produse (pantofi) abia după ce deschizi lista → un click pe ea.
  await page.waitForFunction(() => { const sel = document.querySelector('select.super-attribute-select'); return !sel || sel.options.length > 1; }, { timeout: 10000 }).catch(() => {});
  const emptyMagento = await page.evaluate(() => { const sel = document.querySelector('select.super-attribute-select'); return !!sel && sel.options.length <= 1; }).catch(() => false);
  if (emptyMagento) {
    await page.evaluate(() => { const o = document.querySelector('.visual-ko-select .select-overlay') || document.querySelector('.visual-ko-select'); if (o) o.click(); }).catch(() => {});
    await page.waitForFunction(() => document.querySelector('select.super-attribute-select').options.length > 1, { timeout: 6000 }).catch(() => {});
  }
}

/** Blocaj anti-bot (nu „produs dispărut"). */
async function isBlocked(page, status) {
  if (status === 403 || status === 429 || status === 503) return true;
  const t = (await page.title().catch(() => '')).toLowerCase();
  return /access denied|attention required|just a moment|captcha|are you a robot|request unsuccessful|blocked/.test(t);
}

async function newContext(browser) {
  const ctx = await browser.createBrowserContext();
  const page = await ctx.newPage();
  // Versiunea REALĂ de Chrome (o versiune falsă în UA, diferită de cea din
  // Client Hints, e un semnal clasic de bot) + fără navigator.webdriver.
  await page.setUserAgent((await browser.userAgent()).replace('HeadlessChrome', 'Chrome'));
  await page.evaluateOnNewDocument(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  await page.setExtraHTTPHeaders({ 'Accept-Language': 'ro-RO,ro;q=0.9,en;q=0.8' });
  await page.setViewport({ width: 1366, height: 900 });
  // Fără poze/video/fonturi: datele sunt în HTML/JSON-LD; pagina se încarcă de
  // câteva ori mai repede și consumăm mult mai puțin din banda magazinului.
  // (CSS rămâne: e nevoie de el ca să vedem mărimile tăiate = epuizate.)
  await page.setRequestInterception(true);
  page.on('request', (req) => { const t = req.resourceType(); if (t === 'image' || t === 'media' || t === 'font') req.abort().catch(() => {}); else req.continue().catch(() => {}); });
  return { ctx, page };
}

async function crawlHost(browser, host, items, report) {
  const r = (report[host] = { total: items.length, ok: 0, cu_marimi: 0, fara_pret: 0, disparute: 0, blocate: 0, erori: 0, nefacute: 0 });
  let { ctx, page } = await newContext(browser);
  let blockedStreak = 0, n = 0;
  for (const it of items) {
    if (blockedStreak >= BLOCK_LIMIT) { r.nefacute++; continue; }
    if (n && n % RESTART_EVERY === 0) { await ctx.close().catch(() => {}); ({ ctx, page } = await newContext(browser)); }
    n++;
    try {
      const resp = await page.goto(it.url, { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(async (e) => {
        if (/timeout/i.test(e.message)) return null; // pagini grele: citim ce s-a încărcat
        throw e;
      });
      const status = resp ? resp.status() : 0;
      if (await isBlocked(page, status)) {
        r.blocate++; blockedStreak++;
        console.log(`  ⛔ ${host} #${it.product_id} blocat (${status})`);
        if (!IMAGES) await api('manual-result', { product_id: it.product_id, url: it.url, blocked: true }).catch(() => {});
        await sleep(jitter(DELAY * 4));
        continue;
      }
      blockedStreak = 0;
      if (OWN) {
        await preparePage(page, host);
        await sleep(1000);
        const d = await extractSafe(page);
        if (!d.price && !d.isProduct && !d.soldOut) { r.fara_pret++; console.log(`  ? ${host} #${it.product_id}: fără date (nu schimb nimic)`); }
        else {
          const known = d.sizes.length || d.unavailable.length;
          const body = { product_id: it.product_id, sizes: d.sizes, unavailable: d.unavailable, complete: !!d.complete, price: d.price,
            availability: d.soldOut ? 'OutOfStock' : (known ? (d.sizes.length ? 'InStock' : 'OutOfStock') : (d.in_stock ? 'InStock' : 'OutOfStock')) };
          await api('crawl-result', body);
          r.ok++; if (known) r.cu_marimi++;
          console.log(`  ✓ ${host} #${it.product_id} ${d.price} ${body.availability} [${d.sizes.join(',')}]${d.unavailable.length ? ' epuizate:[' + d.unavailable.join(',') + ']' : ''} (${d.method})`);
        }
      } else if (VARIANTS) {
        await preparePage(page, host);
        await sleep(1000);
        const d = await extractSafe(page);
        const known = d.sizes.length || d.unavailable.length;
        if (!d.price && !d.isProduct && !d.soldOut) { r.fara_pret++; console.log(`  ? ${host} #${it.product_id} varianta ${it.key}: fără date`); }
        else {
          const body = { product_id: it.product_id, key: it.key, in_stock: d.soldOut ? false : (known ? d.sizes.length > 0 : !!d.in_stock), checked: true };
          if (known || d.soldOut) { body.sizes = d.sizes; body.unavailable = d.unavailable; }
          await api('crawl-variant-result', body);
          r.ok++; if (known) r.cu_marimi++;
          console.log(`  ✓ ${host} #${it.product_id} varianta ${it.key}: ${body.in_stock ? 'stoc' : 'EPUIZAT'} [${d.sizes.join(',')}]${d.unavailable.length ? ' epuizate:[' + d.unavailable.join(',') + ']' : ''} (${d.method})`);
        }
      } else if (IMAGES) {
        const d = await extractSafe(page);
        const res = await api('ext-image', { product_id: it.product_id, store_id: it.store_id, image: d.image, color: d.color || colorFrom(d.name) });
        if (res.image) { r.ok++; console.log(`  ✓ ${host} #${it.product_id} poză ${String(d.image).slice(0, 70)} (${d.color || colorFrom(d.name) || '?'})`); }
        else { r.fara_pret++; console.log(`  ? ${host} #${it.product_id} fără poză`); }
      } else if (status === 404 || status === 410) {
        await api('manual-result', { product_id: it.product_id, url: it.url, gone: true });
        r.disparute++;
        console.log(`  ✗ ${host} #${it.product_id} produs dispărut (${status})`);
      } else {
        await preparePage(page, host);
        await sleep(1200); // hidratare (mărimile se randează uneori după load)
        let d = await extractSafe(page);
        if (!d.price && !d.isProduct) {
          // Încărcare incompletă (rețea/anti-bot lent): încă o încercare, mai răbdătoare.
          await sleep(jitter(DELAY));
          await page.reload({ waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
          await sleep(5000);
          d = await extractSafe(page);
        }
        // Redirect către altă pagină (listă/categorie) și fără produs = dispărut.
        const redirected = resp && resp.request().redirectChain().length > 0;
        // Multe magazine răspund 200 cu o pagină „produs negăsit" (ex. giraffe).
        const notFound = !d.isProduct && !d.price && /nu a fost găsit|nu mai există|nu există|pagina nu|not found|404/i.test((await page.title().catch(() => '')) + ' ' + (await page.$eval('h1', (h) => h.textContent).catch(() => '')));
        if (!d.isProduct && !d.price && (redirected || notFound)) { r.disparute++; await api('manual-result', { product_id: it.product_id, url: it.url, gone: true }); console.log(`  ✗ ${host} #${it.product_id} nu mai e pagină de produs`); }
        else if (!d.price && d.soldOut) {
          await api('manual-result', { product_id: it.product_id, url: it.url, gone: true });
          r.disparute++;
          console.log(`  ✗ ${host} #${it.product_id} stoc epuizat complet (fără preț pe pagină)`);
        } else if (d.price > 0) {
          const body = { product_id: it.product_id, url: it.url, name: d.name, price: d.price, currency: d.currency, in_stock: d.in_stock, color: d.color || colorFrom(d.name), image: d.image, match: matchOf(it.ids, d) };
          if (d.sizes.length || d.unavailable.length) { body.sizes = d.sizes; body.sizes_unavailable = d.unavailable; r.cu_marimi++; }
          const res = await api('manual-result', body);
          r.ok++;
          console.log(`  ✓ ${host} #${it.product_id} [${body.match}] ${d.price} ${d.currency} ${d.in_stock ? 'stoc' : 'EPUIZAT'} [${d.sizes.join(',')}]${d.unavailable.length ? ' epuizate:[' + d.unavailable.join(',') + ']' : ''} (${d.method})${res.ok ? '' : ' ! ' + res.error}`);
        } else {
          r.fara_pret++;
          console.log(`  ? ${host} #${it.product_id} fără preț citibil (${d.method || 'nimic'}) ${it.url.slice(0, 80)}`);
          // Pagină fără niciun semn de produs = de obicei o verificare anti-bot.
          if (!d.isProduct) { blockedStreak++; await api('manual-result', { product_id: it.product_id, url: it.url, blocked: true }).catch(() => {}); }
        }
      }
    } catch (e) {
      r.erori++;
      console.log(`  ! ${host} #${it.product_id} ${e.message.slice(0, 120)}`);
    }
    await sleep(jitter(DELAY));
  }
  await ctx.close().catch(() => {});
}

(async () => {
  const q = new URLSearchParams();
  for (const [k, v] of [['host', process.env.HOST], ['ids', process.env.IDS], ['limit', process.env.LIMIT], ['older', process.env.OLDER]]) if (v) q.set(k, v);
  if (IMAGES && process.env.ALL) q.set('all', '1');
  // QUEUE_FILE: coadă din fișier (ex. eșantion pentru verificare), nu din site.
  const { queue } = process.env.QUEUE_FILE
    ? { queue: JSON.parse(fs.readFileSync(process.env.QUEUE_FILE, 'utf8')) }
    : OWN
      ? await api('recrawl-queue?source=cj&limit=' + (process.env.LIMIT || 500) + (process.env.IDS ? '&ids=' + process.env.IDS : '')).then((j) => ({ queue: (j.queue || []).map((x) => { const real = new URL(x.url).searchParams.get('url') || x.url; return { ...x, url: real, host: new URL(real).hostname.replace(/^www\./, '') }; }) }))
    : VARIANTS
      ? await api('crawl-queue-variants?limit=5000' + (process.env.IDS ? '&ids=' + process.env.IDS : '')).then((j) => ({ queue: (j.queue || []).map((x) => { const real = new URL(x.url).searchParams.get('url') || x.url; return { ...x, url: real, host: new URL(real).hostname.replace(/^www\./, '') }; }) }))
      : await api((IMAGES ? 'ext-image-queue?' : 'manual-queue?') + q.toString());
  console.log(`[cross] ${queue.length} URL-uri de verificat`);
  if (!queue.length) return;

  const byHost = {};
  queue.forEach((it) => (byHost[it.host] = byHost[it.host] || []).push(it));
  const hosts = Object.keys(byHost).sort((a, b) => byHost[b].length - byHost[a].length);

  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: process.env.HEADFUL ? false : 'new',
    ignoreDefaultArgs: ['--enable-automation'],
    args: ['--no-sandbox', '--disable-blink-features=AutomationControlled', '--lang=ro-RO', '--disable-dev-shm-usage'],
  });
  const report = {};
  let next = 0;
  const worker = async () => { while (next < hosts.length) { const h = hosts[next++]; await crawlHost(browser, h, byHost[h], report); } };
  await Promise.all(Array.from({ length: Math.min(CONCURRENCY, hosts.length) }, worker));
  await browser.close();

  console.log('\n[cross] REZUMAT pe magazin:');
  console.table(report);
  if (process.env.REPORT) fs.writeFileSync(process.env.REPORT, JSON.stringify(report, null, 2));
  if (DRYRUN && process.env.DRY_OUT) fs.writeFileSync(process.env.DRY_OUT, JSON.stringify(dryResults, null, 1));
})();
