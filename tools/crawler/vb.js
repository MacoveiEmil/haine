/**
 * Verificare + mărimi various-brands (2Performant) pentru hainute.ro.
 *
 * IMPORTANT: various-brands are un consent-wall Cookiebot — fără cookie de
 * consimțământ, ORICE URL de produs redirectează la home („Home Page"). De aceea
 * acceptăm cookie-urile O DATĂ la pornire (rămân în context pt toate paginile),
 * apoi produsele se încarcă normal și le putem citi mărimile reale.
 *
 * Pe pagina de produs mărimile DISPONIBILE sunt <option> în selectorul „Selectati
 * marimea" (clasă tile-root...). Doar cele disponibile apar → autoritativ pt
 * mărimile magazinului. Fără mărimi + „Home Page" = produs dispărut → fără stoc.
 *
 * Rulare: node vb.js        (env: SITE, SECRET, DELAY=1200, MAX, LIMIT=300)
 */
const puppeteer = require('puppeteer-core');

const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const DELAY  = parseInt(process.env.DELAY || '1200', 10);
const MAX    = parseInt(process.env.MAX || '0', 10);
const LIMIT  = parseInt(process.env.LIMIT || '300', 10);
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function getQueue() {
  const r = await fetch(`${SITE}/wp-json/hainute/v1/crawl-queue-vb?secret=${encodeURIComponent(SECRET)}&limit=${LIMIT}${process.env.IDS ? '&ids=' + process.env.IDS : ''}`);
  if (!r.ok) throw new Error(`queue HTTP ${r.status}`);
  return r.json();
}
async function post(payload) {
  await fetch(`${SITE}/wp-json/hainute/v1/crawl-vb-result?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload),
  });
}

/** Acceptă consimțământul Cookiebot o dată — altfel produsele redirectează la home. */
async function acceptCookies(page) {
  await page.goto('https://www.various-brands.ro/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await sleep(1500);
  const clicked = await page.evaluate(() => {
    const ids = ['CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll', 'CybotCookiebotDialogBodyButtonAccept', 'CybotCookiebotDialogBodyLevelButtonAccept'];
    for (const id of ids) { const b = document.getElementById(id); if (b) { b.click(); return id; } }
    const b = [...document.querySelectorAll('button,a')].find((x) => /permite toate|accept all|accept/i.test(x.textContent || ''));
    if (b) { b.click(); return 'text'; }
    return '';
  });
  await sleep(1800);
  const ok = await page.evaluate(() => /CookieConsent/.test(document.cookie));
  return { clicked, ok };
}

(async () => {
  const { queue } = await getQueue();
  console.log(`[vb] ${queue.length} oferte various-brands de verificat`);
  if (!queue.length) return;
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--disable-blink-features=AutomationControlled'] });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });
  await page.setRequestInterception(true);
  page.on('request', (req) => { const t = req.resourceType(); (t === 'image' || t === 'media' || t === 'font') ? req.abort() : req.continue(); });

  const consent = await acceptCookies(page);
  console.log(`[vb] consimțământ cookie: ${consent.clicked || 'NEGĂSIT'} (cookie set: ${consent.ok})`);

  let done = 0, dead = 0, withSizes = 0, errors = 0;
  for (const item of queue) {
    try {
      const extract = () => page.evaluate(() => {
        const out = { title: document.title || '', sizes: [], unavail: [], hasCart: false };
        out.hasCart = /adauga in cos|adaugă în coș/i.test(document.body.innerText || '');
        // Mărimi: pantofi (32, 32-33, 38.5), haine (116, 128, 164, „128 CM"),
        // litere (XS-XXL), vârstă („13-14 ani"). NU 4+ cifre (an/cod).
        const sizeRe = /^(\d{1,3}([.,\/-]\d{1,3})?(\s?(cm|ani|luni|m))?|xxs|xs|s|m|l|xl|xxl|xxxl)$/i;
        const push = (arr, t) => { t = t.trim(); if (sizeRe.test(t) && !arr.includes(t)) arr.push(t); };
        document.querySelectorAll('option, [class*="tile-root"], [class*="clickable-root"]').forEach((el) => {
          if (el.closest('table')) return;
          const t = (el.textContent || '').trim();
          if (!sizeRe.test(t)) return;
          const off = el.disabled || /disabled|unavail|inactive|sold|epuizat|indispon/i.test(el.className);
          off ? push(out.unavail, t) : push(out.sizes, t);
        });
        return out;
      });

      const resp = await page.goto(item.url, { waitUntil: 'networkidle2', timeout: 35000 });
      const status = resp ? resp.status() : 200; // SPA: goto poate întoarce null deși pagina e OK
      // React randează selectorul de mărimi + coșul DUPĂ load — așteptăm conținutul.
      await page.waitForFunction(
        () => /adauga in cos|adaug[ăa] [îi]n co[șs]/i.test(document.body.innerText || '') ||
              /home\s*page/i.test(document.title) ||
              document.querySelector('option'),
        { timeout: 9000 }
      ).catch(() => {});
      await sleep(300);
      let data = await extract();
      const isHome = /home\s*page/i.test(data.title);
      // Hidratare ratată (nici home, nici mărimi, nici coș) → un reload.
      if ( ! isHome && ! data.hasCart && ! data.sizes.length ) {
        await page.reload({ waitUntil: 'networkidle2', timeout: 35000 }).catch(() => {});
        await sleep(800);
        data = await extract();
      }

      // Mort DOAR la redirect clar spre home (feed-ul e adevărul pt existență;
      // crawler-ul ia mai ales mărimile). O pagină de produs fără listă de mărimi
      // rămâne „vie" (stoc din feed), nu o marcăm greșit dispărută.
      const alive = ! /home\s*page/i.test( data.title );
      const sizes = alive ? data.sizes : [];

      await post({ product_id: item.product_id, store_id: item.store_id, sizes, alive });
      done++;
      if (!alive) { dead++; if (dead <= 20) console.log(`  #${item.product_id} MORT (HTTP ${status}${isHome ? ', home' : ', fără mărimi/coș'})`); }
      else { withSizes += sizes.length ? 1 : 0; if (done % 20 === 0 || sizes.length) console.log(`  #${item.product_id} ✓ mărimi: ${sizes.join(',') || '(fără listă, dar în stoc)'}`); }
    } catch (e) {
      errors++;
      await post({ product_id: item.product_id, store_id: item.store_id, sizes: [], alive: false });
    }
    if (MAX && done >= MAX) break;
    await sleep(DELAY + Math.floor(Math.random() * DELAY * 0.4));
  }
  await browser.close();
  console.log(`\n[vb] TERMINAT: ${done} verificate, ${withSizes} cu mărimi reale, ${dead} moarte, ${errors} erori.`);
})();
