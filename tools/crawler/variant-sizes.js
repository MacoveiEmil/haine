/**
 * Mărimi PER CULOARE pentru hainute.ro.
 *
 * Un produs grupat (mai multe culori din același model) stochează o singură serie
 * de mărimi → o culoare poate arăta o mărime pe care de fapt n-o are. Aici crawluim
 * URL-ul FIECĂREI culori (variant offer) și stocăm mărimile ei reale, ca matricea
 * să dea disponibilitate corectă per culoare.
 *
 * Extragere după magazin: Answear = JSON-LD size[]; Fashion Days = data-gtm-size +
 * data-gtm-avail; various-brands = <option> din selector (după consimțământ cookie).
 *
 * Rulare: node variant-sizes.js [answear|fd|vb]   (env: SITE, SECRET, DELAY, MAX)
 */
const puppeteer = require('puppeteer-core');

const ONLY   = (process.argv[2] || process.env.SOURCE || '').toLowerCase();
const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const DELAY  = parseInt(process.env.DELAY || '1200', 10);
const MAX    = parseInt(process.env.MAX || '0', 10);
const LIMIT  = parseInt(process.env.LIMIT || '4000', 10);
const IDS    = process.env.IDS || ''; // țintește produse anume (ex. "10471,10500")
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function getQueue() {
  const u = `${SITE}/wp-json/hainute/v1/crawl-queue-variants?secret=${encodeURIComponent(SECRET)}&limit=${LIMIT}` + (ONLY ? `&source=${ONLY}` : '') + (IDS ? `&ids=${encodeURIComponent(IDS)}` : '');
  const r = await fetch(u);
  if (!r.ok) throw new Error(`queue HTTP ${r.status}`);
  return r.json();
}
async function post(p) {
  await fetch(`${SITE}/wp-json/hainute/v1/crawl-variant-result?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(p),
  });
}

async function acceptVbCookies(page) {
  await page.goto('https://www.various-brands.ro/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await sleep(1500);
  await page.evaluate(() => { const b = document.getElementById('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'); if (b) b.click(); });
  await sleep(1500);
}

const extractors = {
  answear: (page) => page.evaluate(() => {
    const sizes = [];
    document.querySelectorAll('script[type="application/ld+json"]').forEach((s) => {
      try { const j = JSON.parse(s.textContent);
        (function sc(o){ if(!o||typeof o!=='object')return;
          if((o['@type']==='Product'||o['@type']==='ProductGroup')&&o.size)[].concat(o.size).forEach((z)=>sizes.push(String(z).trim()));
          for(const k in o) if(o[k]&&typeof o[k]==='object') sc(o[k]); })(j);
      } catch(e){}
    });
    return { sizes: [...new Set(sizes.filter(Boolean))] };
  }),
  fd: (page) => page.evaluate(() => {
    const avail = {};
    document.querySelectorAll('[data-gtm-size]').forEach((e) => {
      const sz = (e.getAttribute('data-gtm-size') || '').trim();
      if (sz && e.getAttribute('data-gtm-avail') === 'available') avail[sz] = 1;
    });
    return { sizes: Object.keys(avail) };
  }),
  vb: (page) => page.evaluate(() => {
    const sizes = [], re = /^(\d{1,3}([.,\/-]\d{1,3})?(\s?(cm|ani|luni|m))?|xxs|xs|s|m|l|xl|xxl|xxxl)$/i;
    document.querySelectorAll('option, [class*="tile-root"]').forEach((el) => {
      if (el.closest('table')) return;
      const t = (el.textContent || '').trim();
      if (re.test(t) && !el.disabled && !sizes.includes(t)) sizes.push(t);
    });
    return { sizes };
  }),
};

(async () => {
  const { queue } = await getQueue();
  console.log(`[variant-sizes] ${queue.length} variante${ONLY ? ' (' + ONLY + ')' : ''}`);
  if (!queue.length) return;
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--disable-blink-features=AutomationControlled'] });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });
  await page.setRequestInterception(true);
  page.on('request', (req) => { const t = req.resourceType(); (t === 'image' || t === 'media' || t === 'font') ? req.abort() : req.continue(); });

  if (queue.some((q) => q.host === 'vb')) { await acceptVbCookies(page); console.log('[variant-sizes] cookie vb acceptat'); }

  let done = 0, withSizes = 0, errors = 0;
  for (const item of queue) {
    try {
      await page.goto(item.url, { waitUntil: 'networkidle2', timeout: 35000 });
      if (item.host === 'vb') {
        await page.waitForFunction(() => document.querySelector('option') || /adauga in cos/i.test(document.body.innerText) || /home\s*page/i.test(document.title), { timeout: 9000 }).catch(() => {});
      }
      const d = await (extractors[item.host] || extractors.answear)(page);
      await post({ product_id: item.product_id, key: item.key, sizes: d.sizes, in_stock: d.sizes.length > 0 });
      done++;
      if (d.sizes.length) { withSizes++; if (done % 15 === 0 || d.sizes.length) console.log(`  #${item.product_id}/${item.key} ✓ ${d.sizes.join(',')}`); }
    } catch (e) {
      errors++;
      await post({ product_id: item.product_id, key: item.key, sizes: [], in_stock: false });
    }
    if (MAX && done >= MAX) break;
    await sleep(DELAY + Math.floor(Math.random() * DELAY * 0.4));
  }
  await browser.close();
  console.log(`\n[variant-sizes] TERMINAT: ${done} variante, ${withSizes} cu mărimi, ${errors} erori.`);
})();
