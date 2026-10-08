/**
 * Crawler Fashion Days pentru hainute.ro.
 *
 * Feed-ul FD n-are stoc, iar mărimile sunt incomplete. Dar PAGINA FD are
 * selectorul de mărimi cu `data-gtm-size` + `data-gtm-avail` → de aici luăm
 * mărimile DISPONIBILE și stocul real. Fără mărimi disponibile = fără stoc.
 *
 * Rulare: node fd.js   (env: SITE, SECRET, BATCH=30, DELAY=1800, MAX)
 */
const puppeteer = require('puppeteer-core');

const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const BATCH  = parseInt(process.env.BATCH || '30', 10);
const DELAY  = parseInt(process.env.DELAY || '1800', 10);
const MAX    = parseInt(process.env.MAX || '0', 10);
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const jitter = (ms) => ms + Math.floor(Math.random() * ms * 0.5);

async function getQueue() {
  const r = await fetch(`${SITE}/wp-json/hainute/v1/crawl-queue-fd?secret=${encodeURIComponent(SECRET)}&limit=${BATCH}`);
  if (!r.ok) throw new Error(`crawl-queue-fd HTTP ${r.status}`);
  return r.json();
}
async function postResult(payload) {
  await fetch(`${SITE}/wp-json/hainute/v1/crawl-fd-result?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload),
  });
}

(async () => {
  console.log(`[fd] site=${SITE} batch=${BATCH} delay=${DELAY}ms`);
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--disable-blink-features=AutomationControlled'] });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });
  await page.setRequestInterception(true);
  page.on('request', (req) => { const t = req.resourceType(); (t === 'image' || t === 'media' || t === 'font') ? req.abort() : req.continue(); });

  let done = 0, inStock = 0, errors = 0;
  try {
    while (true) {
      const { queue, remaining } = await getQueue();
      if (!queue || !queue.length) { console.log('[fd] coadă goală — gata.'); break; }
      console.log(`[fd] lot ${queue.length} (rămase ~${remaining})`);

      for (const item of queue) {
        try {
          await page.goto(item.url, { waitUntil: 'domcontentloaded', timeout: 30000 });
          const data = await page.evaluate(() => {
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
          const in_stock = data.sizes.length > 0;
          await postResult({ product_id: item.product_id, sizes: data.sizes, unavailable: data.unavailable, in_stock: in_stock });
          done++;
          if (in_stock) inStock++;
          if (done % 10 === 0 || data.sizes.length) console.log(`  #${item.product_id} mărimi: ${data.sizes.join(',') || '— (fără stoc)'}`);
        } catch (e) {
          errors++;
          await postResult({ product_id: item.product_id, sizes: [], in_stock: false });
          console.log(`  #${item.product_id} EROARE: ${e.message}`);
        }
        if (MAX && done >= MAX) { console.log(`[fd] MAX=${MAX}.`); await browser.close(); return report(); }
        await sleep(jitter(DELAY));
      }
    }
  } finally { await browser.close(); }
  report();
  function report() { console.log(`\n[fd] TERMINAT: ${done} produse, ${inStock} cu stoc, ${errors} erori.`); }
})();
