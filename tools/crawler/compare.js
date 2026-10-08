/**
 * Comparator magazine externe pentru hainute.ro.
 *
 * Pentru fiecare produs (cu cod de model) din /compare-queue, caută codul pe
 * fiecare magazin extern, extrage preț + disponibilitate + link, și le trimite
 * la /external-offer (apar în panoul „Disponibilitate în magazine"). Non-afiliat.
 *
 * Rulare: node compare.js   (env: SITE, SECRET, BATCH=20, DELAY=2500, MAX)
 */
const puppeteer = require('puppeteer-core');

const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const BATCH  = parseInt(process.env.BATCH || '20', 10);
const DELAY  = parseInt(process.env.DELAY || '2500', 10);
const MAX    = parseInt(process.env.MAX || '0', 10);
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const norm = (s) => (s || '').toLowerCase().replace(/[^a-z0-9]/g, '');
const COLORS = ['bleumarin', 'negru', 'alb', 'rosu', 'albastru', 'verde', 'roz', 'galben', 'gri', 'maro', 'bej', 'mov', 'portocaliu', 'turcoaz', 'bordo', 'kaki', 'navy', 'black', 'white', 'red', 'blue', 'green', 'pink', 'yellow', 'grey', 'gray', 'brown', 'beige', 'purple', 'orange', 'turquoise', 'burgundy', 'khaki'];
// Prima culoare care APARE în nume („White Black" → white), nu prima din listă.
const colorFrom = (name) => { const n = (name || '').toLowerCase(); let best = '', pos = Infinity; for (const c of COLORS) { const m = n.match(new RegExp('\\b' + c + '\\b')); if (m && m.index < pos) { pos = m.index; best = c; } } return best; };
const EUR_RON = parseFloat(process.env.EUR_RON || '4.97');

// Branduri de lux — Farfetch e interogat DOAR pentru ele (crawl mic, țintit,
// evită anti-bot + acoperă exact segmentul pe care celelalte magazine nu-l au).
const LUXURY = new Set(['kenzo', 'kenzokids', 'boss', 'hugo', 'hugoboss', 'moncler', 'dolcegabbana', 'dsquared2', 'dsquared', 'fendi', 'burberry', 'versace', 'youngversace', 'karllagerfeld', 'emporioarmani', 'ea7', 'armani', 'calvinklein', 'calvinkleinjeans', 'poloralphlauren', 'ralphlauren', 'michaelkors', 'stoneisland', 'offwhite', 'palmangels', 'guess', 'marcelo', 'givenchy', 'balmain', 'gucci', 'kentgo', 'tommyhilfiger', 'diesel']);
const isLuxury = (brand) => LUXURY.has(norm(brand));

// ---- Config magazine externe ------------------------------------------------
// searchUrl(code) → pagina de căutare; extract(page) rulează în browser și
// întoarce {name, price, inStock, url} sau null.
const STORES = [
  {
    slug: 'giraffe-shoes',
    name: 'giraffe-shoes.ro',
    searchUrl: (code) => 'https://giraffe-shoes.ro/index.php?route=product/search&search=' + encodeURIComponent(code),
    async extract(page, code) {
      // Căutarea sare direct pe produs când e un singur rezultat; altfel listă.
      const first = await page.$('.product-thumb a, .product-layout a[href*="/"]');
      if (first && !(await page.$('h1'))) { await first.click().catch(() => {}); await page.waitForNavigation({ timeout: 15000 }).catch(() => {}); }
      return page.evaluate(() => {
        const h1 = document.querySelector('h1');
        if (!h1) return null;
        const body = document.body.innerText;
        const pm = body.match(/(\d{2,4}[.,]\d{2})\s*(RON|lei)/i) || body.match(/(RON|lei)\s*(\d{2,4}[.,]\d{2})/i);
        const price = pm ? (pm[1] && /\d/.test(pm[1]) ? pm[1] : pm[2]) : '';
        // „În Stoc" = badge-ul principal; „anunță-mă/revine" apare per mărime
        // indisponibilă, deci NU-l folosim ca semnal de out la nivel de produs.
        const inStock = /în stoc/i.test(body) && !/produs(ul)?\s+(este\s+)?indisponibil|stoc epuizat/i.test(body);
        // Mărimi DISPONIBILE: opțiunile din <select> FĂRĂ atribut disabled.
        const sizes = [].slice.call(document.querySelectorAll('select[name^="option"] option'))
          .filter((o) => !o.disabled && o.value)
          .map((o) => { const m = (o.textContent || '').trim().match(/^(\d{1,3}([.,]5)?)/); return m ? m[1] : ''; })
          .filter(Boolean);
        return { name: h1.textContent.trim(), price: price.replace(',', '.'), inStock: inStock, url: location.href.split('?')[0], sizes: sizes };
      });
    },
  },
  {
    slug: 'sportisimo',
    name: 'Sportisimo.ro',
    searchUrl: (code) => 'https://www.sportisimo.ro/?search=' + encodeURIComponent(code),
    async extract(page, code) {
      // Dacă nu suntem pe produs (fără JSON-LD Product), intră pe primul rezultat.
      let hasProduct = await page.evaluate(() => [].slice.call(document.querySelectorAll('script[type="application/ld+json"]')).some((s) => { try { return JSON.stringify(JSON.parse(s.textContent)).indexOf('"Product"') >= 0; } catch (e) { return false; } }));
      if (!hasProduct) {
        const link = await page.$('a[href*="/"][class*="product" i], .product a, [data-product] a');
        if (link) { await link.click().catch(() => {}); await page.waitForNavigation({ timeout: 15000 }).catch(() => {}); }
      }
      return page.evaluate(() => {
        let res = null;
        [].slice.call(document.querySelectorAll('script[type="application/ld+json"]')).forEach((s) => {
          try { const j = JSON.parse(s.textContent); (function sc(o){ if(!o||typeof o!=='object')return; if(o['@type']==='Product'){ const of=[].concat(o.offers||[])[0]||{}; res={name:o.name||'',sku:String(o.sku||o.mpn||o.gtin13||''),price:String(of.price||'').replace(',','.'),inStock:/InStock/i.test(of.availability||''),url:location.href.split('?')[0]}; } for(const k in o) if(typeof o[k]==='object') sc(o[k]); })(j); } catch (e) {}
        });
        return (res && res.price) ? res : null;
      });
    },
  },
  {
    slug: 'farfetch',
    name: 'Farfetch.com',
    luxuryOnly: true,   // interogat doar pt branduri de lux
    trustSearch: true,  // căutarea pe cod redirectează la produsul EXACT → e verificarea
    searchUrl: (code) => 'https://www.farfetch.com/ro/search?q=' + encodeURIComponent(code),
    async extract(page) {
      // Căutarea pe cod redirectează la pagina de produs când e match unic
      // (URL conține „item-"); altfel e listă/404 → fără match.
      await page.waitForFunction(
        () => location.href.indexOf('item-') >= 0 || /not found|nu (mai )?exist/i.test(document.title),
        { timeout: 9000 }
      ).catch(() => {});
      return page.evaluate((eurRon) => {
        if (location.href.indexOf('item-') < 0) return null; // nu a aterizat pe produs
        const g = (p) => { const m = document.querySelector('meta[property="' + p + '"]'); return m ? m.content : ''; };
        const amt = parseFloat(g('product:price:amount') || g('og:price:amount') || '0');
        if (!amt) return null;
        const cur = (g('product:price:currency') || g('og:price:currency') || 'EUR').toUpperCase();
        const price = cur === 'EUR' ? (amt * eurRon).toFixed(2) : String(amt);
        const avail = /in ?stock/i.test(g('product:availability') || g('og:availability') || '');
        return { name: g('og:title') || document.title, sku: '', price: price, inStock: avail, url: location.href.split('?')[0], sizes: [] };
      }, EUR_RON);
    },
  },
];

const PRODUCT_IDS = process.env.PRODUCT_IDS || '';
const ONLY_STORE = process.env.ONLY_STORE || ''; // rulează doar un magazin (ex. farfetch)
const FILTER = (process.env.FOOTWEAR === '1' ? '&footwear=1' : '') + (process.env.LUXURY === '1' ? '&luxury=1' : '');
async function getQueue() {
  const extra = PRODUCT_IDS ? `&ids=${encodeURIComponent(PRODUCT_IDS)}` : `&limit=${BATCH}${FILTER}`;
  const r = await fetch(`${SITE}/wp-json/hainute/v1/compare-queue?secret=${encodeURIComponent(SECRET)}${extra}`);
  if (!r.ok) throw new Error(`compare-queue HTTP ${r.status}`);
  const data = await r.json();
  if (PRODUCT_IDS) data.remaining = 0; // mod țintit: o singură trecere
  return data;
}
async function postOffer(payload) {
  await fetch(`${SITE}/wp-json/hainute/v1/external-offer?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload),
  });
}

(async () => {
  console.log(`[compare] site=${SITE} batch=${BATCH} delay=${DELAY}ms`);
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--disable-blink-features=AutomationControlled'] });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });

  let done = 0, offers = 0;
  try {
    while (true) {
      const { queue, remaining } = await getQueue();
      if (!queue || !queue.length) { console.log('[compare] coadă goală — gata.'); break; }
      console.log(`[compare] lot ${queue.length} (rămase ~${remaining})`);

      for (const item of queue) {
        const found = [];
        for (const store of STORES) {
          if (ONLY_STORE && store.slug !== ONLY_STORE) continue; // rulează doar magazinul cerut
          if (store.luxuryOnly && !isLuxury(item.brand)) continue; // Farfetch: doar branduri de lux
          try {
            await page.goto(store.searchUrl(item.code), { waitUntil: 'domcontentloaded', timeout: 30000 });
            const data = await store.extract(page, item.code);
            // Sanity: marca în NUME + codul oriunde (nume/sku/url). Magazinele cu
            // trustSearch (Farfetch) redirectează pe cod la produsul exact → căutarea
            // e verificarea, nu cerem codul în datele paginii.
            const hay = norm((data && data.name) + ' ' + (data && data.sku || '') + ' ' + (data && data.url || ''));
            const codeOk = store.trustSearch || hay.indexOf(norm(item.code)) >= 0;
            if (data && data.price && norm(data.name).indexOf(norm(item.brand)) >= 0 && codeOk) {
              // Poza variantei de la acest magazin (altă culoare = altă poză pe site).
              const image = await page.evaluate(() => { const m = document.querySelector('meta[property="og:image"]'); return m ? m.content : ''; }).catch(() => '');
              await postOffer({ product_id: item.product_id, store: store.name, slug: store.slug, price: parseFloat(data.price), currency: 'RON', url: data.url, in_stock: data.inStock, sizes: data.sizes || [], color: colorFrom(data.name), image });
              found.push(store.slug + (data.inStock ? '' : '(x)'));
              offers++;
            }
          } catch (e) { /* magazinul n-are produsul / eroare → ignorăm */ }
          await sleep(DELAY);
        }
        await postOffer({ product_id: item.product_id, done: true });
        done++;
        if (found.length) console.log(`  #${item.product_id} ${item.brand} ${item.code} → ${found.join(', ')}`);
        if (MAX && done >= MAX) { console.log(`[compare] MAX=${MAX} atins.`); await browser.close(); console.log(`\n[compare] ${done} produse, ${offers} oferte externe.`); return; }
      }
    }
  } finally { await browser.close(); }
  console.log(`\n[compare] TERMINAT: ${done} produse verificate, ${offers} oferte externe adăugate.`);
})();
