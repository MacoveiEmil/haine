/**
 * Caută un brand în magazinele partenere (pagina de căutare a fiecărui magazin) și
 * scrie ce găsește. NU scrie nimic în site: doar un JSON + un rezumat în consolă.
 *
 * Rulare: BRAND="en fant" node brand-search.js
 *   env: BRAND (implicit „en fant"), STORES (listă separată prin virgulă, ex. zalando.ro,modivo.ro),
 *        OUT (fișier json), HEADLESS=0 (fereastră vizibilă, pentru debug), CHROME
 */
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const CHROME = process.env.CHROME || (process.platform === 'win32' ? 'C:/Program Files/Google/Chrome/Application/chrome.exe' : '/usr/bin/google-chrome');
const BRAND = (process.env.BRAND || 'en fant').trim();
const SLUG = BRAND.toLowerCase().replace(/\s+/g, '-');
const Q = encodeURIComponent(BRAND).replace(/%20/g, '+');
const OUT = process.env.OUT || path.join(__dirname, `brand-${SLUG}.json`);
const ONLY = (process.env.STORES || '').split(',').map((s) => s.trim()).filter(Boolean);
const HEADLESS = process.env.HEADLESS === '0' ? false : 'new';
const HOMES = new Proxy({}, { get: (_, h) => `https://www.${h}/` });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Pagini de căutare (sau de brand) per magazin; prima care dă rezultate câștigă.
const STORES = {
  'zalando.ro': [`https://www.zalando.ro/${SLUG}/`, `https://www.zalando.ro/catalog/?q=${Q}`],
  'aboutyou.ro': [`https://www.aboutyou.ro/b/${SLUG}`, `https://www.aboutyou.ro/search?term=${Q}`],
  'modivo.ro': [`https://modivo.ro/search?q=${Q}`, `https://modivo.ro/c/copii?q=${Q}`],
  'answear.ro': [`https://answear.ro/search?q=${Q}`, `https://answear.ro/c/copii?q=${Q}`],
  'epantofi.ro': [`https://www.epantofi.ro/catalogsearch/result/?q=${Q}`, `https://www.epantofi.ro/cautare?q=${Q}`],
  'sportisimo.ro': [`https://www.sportisimo.ro/cautare/?q=${Q}`, `https://www.sportisimo.ro/search/?q=${Q}`],
  'fashiondays.ro': [`https://www.fashiondays.ro/search?q=${Q}`, `https://www.fashiondays.ro/b/${SLUG}/`],
  'various-brands.ro': [`https://www.various-brands.ro/catalogsearch/result/?q=${Q}`],
  'sportano.ro': [`https://sportano.ro/catalogsearch/result/?q=${Q}`, `https://sportano.ro/search?q=${Q}`],
  'magicstep.ro': [`https://www.magicstep.ro/search?q=${Q}`, `https://www.magicstep.ro/catalogsearch/result/?q=${Q}`],
  'giraffe-shoes.ro': [`https://www.giraffe-shoes.ro/search?q=${Q}`, `https://www.giraffe-shoes.ro/catalogsearch/result/?q=${Q}`],
  '4kidspoint.ro': [`https://www.4kidspoint.ro/search?q=${Q}`, `https://www.4kidspoint.ro/?s=${Q}`],
  'sizeer.ro': [`https://sizeer.ro/search?q=${Q}`, `https://sizeer.ro/cauta?q=${Q}`],
  'sportvision.ro': [`https://www.sportvision.ro/search?q=${Q}`, `https://www.sportvision.ro/cautare?q=${Q}`],
};

// „en fant", „en-fant", „en_fant" ca cuvinte întregi (nu „enfant" singur: e și cuvânt francez).
const RX = new RegExp('(^|[^a-z0-9])' + BRAND.toLowerCase().split(/[\s-]+/).map((w) => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('[\\s_-]') + '([^a-z0-9]|$)', 'i');

async function typeInSearch(page) {
  const sel = 'input[type=search], input[name=q], input[name=term], input[name=search], input[name=query], input[name=s], input[placeholder*=aut], input[placeholder*=earch], input[aria-label*=aut], input[aria-label*=earch]';
  let h = await page.$(sel);
  if (!h) { // unele magazine ascund caseta în spatele unei iconițe
    const ic = await page.$('[class*=search i] button, button[class*=search i], a[class*=search i], [aria-label*=aut i][role=button], [data-testid*=search i]');
    if (ic) { await ic.click().catch(() => {}); await sleep(800); h = await page.$(sel); }
  }
  if (!h) return false;
  await h.click({ clickCount: 3 }).catch(() => {});
  // valoarea setată direct (tastarea pierdea litere când căsuța se reîncarcă la sugestii)
  await h.evaluate((el, v) => {
    const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
    set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
  }, BRAND);
  await sleep(600);
  await page.keyboard.press('Enter');
  await sleep(4500);
  return true;
}

async function scan(page, url) {
  const box = url === 'BOX';
  const home = box ? HOMES[page.__host] : url;
  const resp = await page.goto(home, { waitUntil: 'domcontentloaded', timeout: 45000 }).catch((e) => ({ err: e.message }));
  if (resp && resp.err) return { url, error: resp.err };
  await sleep(3500);
  // acceptă/respinge bannerul de cookie-uri ca să nu acopere lista
  await page.evaluate(() => {
    const b = [...document.querySelectorAll('button,a')].find((x) => /^(refuz|respinge|reject|doar necesare|continu[ăa] f[ăa]r[ăa])/i.test((x.innerText || '').trim()));
    if (b) b.click();
  }).catch(() => {});
  if (box && !(await typeInSearch(page))) return { url, final: page.url(), status: resp ? resp.status() : null, title: 'fără casetă de căutare', products: [] };
  for (let i = 0; i < 6; i++) { await page.evaluate(() => window.scrollBy(0, 1400)); await sleep(500); }
  const info = await page.evaluate((rxSrc) => {
    const rx = new RegExp(rxSrc, 'i');
    const out = [];
    const seen = new Set();
    for (const a of document.querySelectorAll('a[href]')) {
      const href = a.href.split('#')[0];
      const text = (a.innerText || a.getAttribute('title') || a.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim();
      const img = a.querySelector('img');
      const alt = img ? (img.alt || '') : '';
      const hay = `${decodeURIComponent(href)} ${text} ${alt}`;
      if (!rx.test(hay) || seen.has(href.split('?')[0])) continue;
      const u = new URL(href);
      if (/[?&](p|page|pagina)=\d/i.test(u.search) || /error|not_found|page-not-found|oops/i.test(href)) continue;
      // doar linkuri de produs: .html, /p/, /products/, /produs..., sau slug lung cu cratime
      const isProd = /\.html?$/i.test(u.pathname) || /\/(p|products?|produs[a-z]*|articol)\//i.test(u.pathname) || /-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+/i.test(u.pathname.split('/').pop());
      if (!isProd || /\/(collections?|search|catalogsearch|cauta|cautare|b|brand|marca|marci|catalog-copii)\/?$/i.test(u.pathname)) continue;
      seen.add(href.split('?')[0]);
      out.push({ url: href.split('?')[0], text: text.slice(0, 140) || alt.slice(0, 140) });
    }
    const body = (document.body.innerText || '').slice(0, 20000);
    return { title: document.title, products: out, nofound: /nu am g[ăa]sit|niciun rezultat|0 rezultate|no results|nu s-au g[ăa]sit/i.test(body), mentions: (body.match(rx) || []).length };
  }, RX.source);
  return { url, final: page.url(), status: resp ? resp.status() : null, ...info };
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: HEADLESS, args: ['--no-sandbox', '--window-size=1366,900', '--lang=ro-RO'] });
  const results = {};
  const hosts = Object.keys(STORES).filter((h) => !ONLY.length || ONLY.includes(h));
  console.log(`Caut „${BRAND}" în ${hosts.length} magazine…`);
  for (const host of hosts) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1366, height: 900 });
    await page.setUserAgent((await browser.userAgent()).replace('HeadlessChrome', 'Chrome'));
    await page.setExtraHTTPHeaders({ 'Accept-Language': 'ro-RO,ro;q=0.9,en;q=0.5' });
    let best = null;
    const tried = [];
    page.__host = host;
    for (const url of [...STORES[host], 'BOX']) {
      try {
        const r = await scan(page, url);
        tried.push({ url, status: r.status, final: r.final, title: r.title, produse: (r.products || []).length, error: r.error });
        if (!best || (r.products || []).length > (best.products || []).length) best = r;
        if (r.products && r.products.length) break;
      } catch (e) { tried.push({ url, error: e.message.slice(0, 120) }); }
    }
    results[host] = { gasite: best && best.products ? best.products.length : 0, produse: best && best.products || [], incercari: tried };
    const t = tried[tried.length - 1] || {};
    console.log(`${results[host].gasite ? '✓' : '·'} ${host}: ${results[host].gasite} produse${results[host].gasite ? '' : ` (${tried.map((x) => x.error ? 'eroare' : x.status).join('/')})`}`);
    await page.close();
  }
  await browser.close();
  fs.writeFileSync(OUT, JSON.stringify({ brand: BRAND, la: new Date().toISOString(), magazine: results }, null, 1));
  console.log('Scris în', OUT);
})().catch((e) => { console.error(e); process.exit(1); });
