/**
 * Verificare disponibilitate VARIANTE de culoare (Answear) pentru hainute.ro.
 * Culorile dispărute/fără stoc rămân altfel marcate „disponibile". Aici deschidem
 * URL-ul fiecărei variante: dacă pagina nu mai are produs cu mărimi disponibile,
 * o marcăm in_stock=false → e exclusă din afișaj.
 *
 * Rulare: node variants.js   (env: SITE, SECRET, DELAY=1500, MAX)
 */
const puppeteer = require('puppeteer-core');

const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const DELAY  = parseInt(process.env.DELAY || '1500', 10);
const MAX    = parseInt(process.env.MAX || '0', 10);
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function getQueue() {
  const r = await fetch(`${SITE}/wp-json/hainute/v1/crawl-queue-variants?secret=${encodeURIComponent(SECRET)}&limit=4000`);
  if (!r.ok) throw new Error(`queue HTTP ${r.status}`);
  return r.json();
}
async function post(payload) {
  await fetch(`${SITE}/wp-json/hainute/v1/crawl-variant-result?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload),
  });
}

(async () => {
  const { queue } = await getQueue();
  console.log(`[variants] ${queue.length} variante de verificat`);
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--disable-blink-features=AutomationControlled'] });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });

  let done = 0, gone = 0, errors = 0;
  for (const item of queue) {
    try {
      const resp = await page.goto(item.url, { waitUntil: 'domcontentloaded', timeout: 30000 });
      const status = resp ? resp.status() : 0;
      // În stoc = pagina are un Product cu cel puțin o mărime disponibilă.
      const inStock = await page.evaluate(() => {
        var ok = false;
        [].slice.call(document.querySelectorAll('script[type="application/ld+json"]')).forEach(function (s) {
          try { var j = JSON.parse(s.textContent);
            (function sc(o){ if(!o||typeof o!=='object')return;
              if(o['@type']==='Product' && o.size && [].concat(o.size).length) ok = true;
              for(var k in o) if(typeof o[k]==='object') sc(o[k]); })(j);
          } catch (e) {}
        });
        return ok;
      });
      const alive = status === 200 && inStock;
      await post({ product_id: item.product_id, key: item.key, in_stock: alive });
      done++;
      if (!alive) { gone++; console.log(`  #${item.product_id}/${item.key} DISPĂRUT (HTTP ${status})`); }
    } catch (e) {
      errors++;
      await post({ product_id: item.product_id, key: item.key, in_stock: false });
    }
    if (MAX && done >= MAX) break;
    await sleep(DELAY + Math.floor(Math.random() * DELAY * 0.4));
  }
  await browser.close();
  console.log(`\n[variants] TERMINAT: ${done} verificate, ${gone} dispărute/fără stoc, ${errors} erori.`);
})();
