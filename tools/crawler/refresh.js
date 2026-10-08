/**
 * Re-verificare disponibilitate (CRON) pentru hainute.ro.
 *
 * Spre deosebire de answear.js/fd.js (care crawluiesc produse NOI, o singură
 * dată), acesta reîmprospătează produse DEJA crawluite: cere din /recrawl-queue
 * cele mai vechi verificate (cu produsele „fierbinți" în față), le re-verifică
 * stocul/mărimile și marchează „verificat acum". Rulează de 2 ori pe zi din
 * planificatorul sistemului; varianta `hot` rulează des (orar) doar pe produsele
 * cu multe vizualizări recente, ca stocul lor să fie cât mai proaspăt.
 *
 * Rulare:
 *   node refresh.js cj          # reîmprospătează Answear (implicit)
 *   node refresh.js fd          # reîmprospătează Fashion Days
 *   node refresh.js cj hot      # doar produsele fierbinți Answear (lane rapid)
 * Env: SITE, SECRET, BATCH=40, DELAY=1600, MAX=1200 (plafon/rulare), BRAND.
 */
const puppeteer = require('puppeteer-core');

const SOURCE = (process.argv[2] || process.env.SOURCE || 'cj').toLowerCase();
const HOT    = process.argv.includes('hot') || process.env.HOT === '1';
const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const BATCH  = parseInt(process.env.BATCH || '40', 10);
const DELAY  = parseInt(process.env.DELAY || '1600', 10);
const MAX    = parseInt(process.env.MAX || (HOT ? '150' : '1200'), 10);
const BRAND  = process.env.BRAND || '';
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const jitter = (ms) => ms + Math.floor(Math.random() * ms * 0.5);

const RESULT = { cj: 'crawl-result', fd: 'crawl-fd-result' };
if (!RESULT[SOURCE]) { console.error(`sursă invalidă: ${SOURCE} (cj|fd)`); process.exit(1); }

/** Answear: mărimi/disponibilitate/sku din JSON-LD. */
function extractAnswear(html) {
  const out = { sizes: [], availability: '', sku: '', price: 0, old_price: 0 };
  const re = /<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;
  let m;
  while ((m = re.exec(html)) !== null) {
    let json; try { json = JSON.parse(m[1].trim()); } catch (e) { continue; }
    const stack = [json];
    while (stack.length) {
      const o = stack.pop();
      if (!o || typeof o !== 'object') continue;
      if (o['@type'] === 'Product' || o['@type'] === 'ProductGroup') {
        if (o.size) out.sizes = [].concat(o.size).map(String).map((s) => s.trim()).filter(Boolean);
        if (o.sku) out.sku = String(o.sku);
        for (const of of [].concat(o.offers || [])) {
          if (of && of.availability) { out.availability = String(of.availability).replace('https://schema.org/', ''); }
          // Prețul curent (reducerile Answear se schimbă des; feed-ul e rar).
          const pr = parseFloat(String((of && (of.price || of.lowPrice)) || '').replace(',', '.'));
          if (pr > 0 && !out.price) out.price = pr;
          if (out.availability) break;
        }
      }
      for (const k in o) if (o[k] && typeof o[k] === 'object') stack.push(o[k]);
    }
  }
  return out;
}

async function getQueue() {
  const u = `${SITE}/wp-json/hainute/v1/recrawl-queue?secret=${encodeURIComponent(SECRET)}&source=${SOURCE}&limit=${BATCH}` +
    (HOT ? '&hot=1' : '') + (BRAND ? `&brand=${encodeURIComponent(BRAND)}` : '') + (process.env.IDS ? `&ids=${process.env.IDS}` : '');
  const r = await fetch(u);
  if (!r.ok) throw new Error(`recrawl-queue HTTP ${r.status}`);
  return r.json();
}
async function postResult(payload) {
  await fetch(`${SITE}/wp-json/hainute/v1/${RESULT[SOURCE]}?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload),
  });
}

(async () => {
  console.log(`[refresh] sursă=${SOURCE}${HOT ? ' (HOT)' : ''}${BRAND ? ' brand=' + BRAND : ''} max=${MAX} site=${SITE}`);
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--disable-blink-features=AutomationControlled'] });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });
  await page.setRequestInterception(true);
  page.on('request', (req) => { const t = req.resourceType(); (t === 'image' || t === 'media' || t === 'font' || t === 'stylesheet') ? req.abort() : req.continue(); });

  let done = 0, live = 0, errors = 0, seen = new Set();
  try {
    while (done < MAX) {
      const { queue } = await getQueue();
      if (!queue || !queue.length) { console.log('[refresh] nimic scadent — gata.'); break; }
      // Protecție: dacă coada repetă aceleași id-uri (ceva nu se marchează), ieșim.
      const fresh = queue.filter((q) => !seen.has(q.product_id));
      if (!fresh.length) { console.log('[refresh] coada nu mai avansează — stop.'); break; }

      for (const item of fresh) {
        seen.add(item.product_id);
        try {
          await page.goto(item.url, { waitUntil: 'domcontentloaded', timeout: 30000 });
          if (SOURCE === 'cj') {
            const html = await page.content();
            const d = extractAnswear(html);
            await postResult({ product_id: item.product_id, sizes: d.sizes, availability: d.availability, sku: d.sku, price: d.price });
            if (d.sizes.length) live++;
          } else {
            const d = await page.evaluate(() => {
              var avail = {}, unavail = {};
              document.querySelectorAll('[data-gtm-size]').forEach(function (e) {
                var sz = (e.getAttribute('data-gtm-size') || '').trim();
                var av = e.getAttribute('data-gtm-avail') || '';
                if (!sz) return;
                if (av === 'available') { avail[sz] = 1; delete unavail[sz]; }
                else if (!avail[sz]) { unavail[sz] = 1; }
              });
              return { sizes: Object.keys(avail), unavailable: Object.keys(unavail) };
            });
            await postResult({ product_id: item.product_id, sizes: d.sizes, unavailable: d.unavailable, in_stock: d.sizes.length > 0 });
            if (d.sizes.length) live++;
          }
          done++;
          if (done % 10 === 0 || item.hot) console.log(`  #${item.product_id}${item.hot ? ' 🔥' : ''} ${item.brand || ''} — verificat (${done}/${MAX})`);
        } catch (e) {
          errors++;
          await postResult(SOURCE === 'cj'
            ? { product_id: item.product_id, sizes: [], availability: '', sku: '' }
            : { product_id: item.product_id, sizes: [], in_stock: false });
        }
        if (done >= MAX) break;
        await sleep(jitter(DELAY));
      }
    }
  } finally { await browser.close(); }
  console.log(`\n[refresh] TERMINAT: ${done} reîmprospătate, ${live} cu stoc, ${errors} erori.`);
})();
