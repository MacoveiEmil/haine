/**
 * Crawler îmbogățire Answear pentru hainute.ro.
 *
 * Ia loturi de produse din endpoint-ul WP /crawl-queue, deschide fiecare pagină
 * Answear cu Chrome headless, scoate din JSON-LD mărimile disponibile +
 * disponibilitate + codul de model (sku), și le trimite înapoi la /crawl-result.
 * Reia automat de unde a rămas (coada întoarce doar produse ne-crawluite).
 *
 * Rulare:  node answear.js
 * Config prin variabile de mediu (opțional):
 *   SITE   (default http://hainutero.local)
 *   SECRET (default din constanta de mai jos)
 *   BATCH  (câte produse/lot, default 40)
 *   DELAY  (ms între cereri, default 1800)
 *   MAX    (plafon produse pe rulare, default 0 = tot)
 */
const puppeteer = require('puppeteer-core');

const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const BATCH  = parseInt(process.env.BATCH || '40', 10);
const DELAY  = parseInt(process.env.DELAY || '1800', 10);
const MAX    = parseInt(process.env.MAX || '0', 10);

const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const jitter = (ms) => ms + Math.floor(Math.random() * ms * 0.5);

/** Scoate mărimi/disponibilitate/sku/brand din JSON-LD-ul unei pagini. */
function extractFromHtml(html) {
  const out = { sizes: [], availability: '', sku: '', brand: '', found: false };
  const re = /<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;
  let m;
  while ((m = re.exec(html)) !== null) {
    let json;
    try { json = JSON.parse(m[1].trim()); } catch (e) { continue; }
    const stack = [json];
    while (stack.length) {
      const o = stack.pop();
      if (!o || typeof o !== 'object') continue;
      if (o['@type'] === 'Product' || o['@type'] === 'ProductGroup') {
        out.found = true;
        if (o.size) out.sizes = [].concat(o.size).map(String).map((s) => s.trim()).filter(Boolean);
        if (o.sku) out.sku = String(o.sku);
        if (o.brand) out.brand = o.brand.name || o.brand;
        for (const of of [].concat(o.offers || [])) {
          if (of && of.availability) { out.availability = String(of.availability).replace('https://schema.org/', ''); break; }
        }
      }
      for (const k in o) if (o[k] && typeof o[k] === 'object') stack.push(o[k]);
    }
  }
  return out;
}

async function getQueue() {
  const res = await fetch(`${SITE}/wp-json/hainute/v1/crawl-queue?secret=${encodeURIComponent(SECRET)}&limit=${BATCH}`);
  if (!res.ok) throw new Error(`crawl-queue HTTP ${res.status}`);
  return res.json();
}

async function postResult(payload) {
  const res = await fetch(`${SITE}/wp-json/hainute/v1/crawl-result?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  return res.ok;
}

(async () => {
  console.log(`[crawler] site=${SITE} batch=${BATCH} delay=${DELAY}ms max=${MAX || '∞'}`);
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--no-sandbox', '--disable-blink-features=AutomationControlled', '--window-size=1280,900'],
  });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });
  // Nu descărca imagini/fonturi — mai rapid, mai puțină bandă.
  await page.setRequestInterception(true);
  page.on('request', (req) => {
    const t = req.resourceType();
    if (t === 'image' || t === 'media' || t === 'font' || t === 'stylesheet') req.abort();
    else req.continue();
  });

  let done = 0, withSizes = 0, errors = 0;

  try {
    while (true) {
      const { queue, remaining } = await getQueue();
      if (!queue || queue.length === 0) { console.log('[crawler] coadă goală — gata.'); break; }
      console.log(`[crawler] lot ${queue.length} (rămase ~${remaining})`);

      for (const item of queue) {
        try {
          const resp = await page.goto(item.url, { waitUntil: 'domcontentloaded', timeout: 30000 });
          const status = resp ? resp.status() : 0;
          const html = await page.content();
          const data = extractFromHtml(html);

          await postResult({
            product_id: item.product_id,
            sizes: data.sizes,
            availability: data.availability,
            sku: data.sku,
          });

          done++;
          if (data.sizes.length) withSizes++;
          if (done % 10 === 0 || data.sizes.length) {
            console.log(`  #${item.product_id} [${status}] mărimi: ${data.sizes.join(',') || '—'} (${data.availability || '?'})`);
          }
        } catch (e) {
          errors++;
          // marcăm ca încercat trimițând un rezultat gol, ca să nu blocheze coada
          await postResult({ product_id: item.product_id, sizes: [], availability: '', sku: '' });
          console.log(`  #${item.product_id} EROARE: ${e.message}`);
        }

        if (MAX && done >= MAX) { console.log(`[crawler] atins MAX=${MAX}.`); await browser.close(); return report(); }
        await sleep(jitter(DELAY));
      }
    }
  } finally {
    await browser.close();
  }

  report();
  function report() {
    console.log(`\n[crawler] TERMINAT: ${done} produse, ${withSizes} cu mărimi, ${errors} erori.`);
  }
})();
