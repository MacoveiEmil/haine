/**
 * Citește paginile de produs găsite de brand-search.js (mărimi, culoare, preț, poză, coduri)
 * și scrie un JSON cu toate datele, ca să se poată potrivi produsele între magazine.
 * NU scrie nimic în site.
 *
 * Rulare: BRAND="en fant" STORES=zalando.ro,aboutyou.ro,4kidspoint.ro node brand-scan.js
 *   env: BRAND, STORES, IN (json de la brand-search.js), OUT, DELAY (ms), LIMIT (per magazin), CHROME
 * Extracția de pe pagină (`pageExtract`) e luată din manual.js, ca să citească la fel ca verificările de stoc.
 */
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const CHROME = process.env.CHROME || (process.platform === 'win32' ? 'C:/Program Files/Google/Chrome/Application/chrome.exe' : '/usr/bin/google-chrome');
const BRAND = (process.env.BRAND || 'en fant').trim();
const SLUG = BRAND.toLowerCase().replace(/\s+/g, '-');
const IN = process.env.IN || path.join(__dirname, `brand-${SLUG}.json`);
const OUT = process.env.OUT || path.join(__dirname, `brand-${SLUG}-produse.json`);
const ONLY = (process.env.STORES || '').split(',').map((s) => s.trim()).filter(Boolean);
const DELAY = parseInt(process.env.DELAY || '2500', 10);
const LIMIT = parseInt(process.env.LIMIT || '0', 10);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// pageExtract din manual.js (rulează în pagină); îl luăm ca text ca să nu-l copiem.
const src = fs.readFileSync(path.join(__dirname, 'manual.js'), 'utf8');
const m = src.match(/\nfunction pageExtract\(\) \{[\s\S]*?\n\}\n/);
if (!m) throw new Error('nu găsesc pageExtract în manual.js');
const PAGE_EXTRACT = m[0];

/** Rulează ÎN PAGINĂ: coduri de model/EAN și text-cheie pentru potrivire. */
function pageIds() {
  const t = document.body ? document.body.innerText : '';
  const html = document.documentElement.innerHTML;
  const uniq = (a) => [...new Set(a)];
  return {
    title: document.title,
    h1: (document.querySelector('h1') || {}).innerText || '',
    codes: uniq((t + ' ' + html).match(/\b[A-Z]{2,3}\d{2}[A-Z]\d{2,3}(?:-[A-Z]\d{2})?\b/g) || []).slice(0, 8),
    gtins: uniq((html.match(/"(?:gtin\d*|ean|barcode)"\s*:\s*"?(\d{8,14})/gi) || []).map((x) => x.replace(/\D+/g, ''))).slice(0, 40),
    images: uniq([...document.querySelectorAll('meta[property="og:image"]')].map((x) => x.content)).slice(0, 3),
  };
}

async function readPage(page, url) {
  await page.goto(url, { waitUntil: 'load', timeout: 60000 }).catch(() => {});
  await page.waitForFunction(() => [...document.querySelectorAll('script[type="application/ld+json"]')].some((s) => /"Product(Group)?"/.test(s.textContent)) || document.querySelector('h1'), { timeout: 12000 }).catch(() => {});
  await sleep(1500);
  for (let i = 0; i < 4; i++) {
    try {
      if (await page.evaluate(() => !!document.body)) {
        const d = await page.evaluate(`(${PAGE_EXTRACT.trim().replace(/^function pageExtract/, 'function')})()`);
        const ids = await page.evaluate(pageIds);
        return { ...d, ...ids, final: page.url() };
      }
    } catch (e) {
      if (!/context was destroyed|navigation|detached/i.test(e.message)) throw e;
    }
    await page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 15000 }).catch(() => {});
    await sleep(1500);
  }
  return { error: 'fără conținut', final: page.url() };
}

/** 4kidspoint e Shopify: .js dă variantele cu SKU, cod de bare și stoc, curat. */
async function shopify(url) {
  const u = url.split('?')[0].replace(/\/$/, '') + '.js';
  const r = await fetch(u, { headers: { 'User-Agent': 'Mozilla/5.0 Chrome/130' } });
  if (!r.ok) return null;
  const j = await r.json();
  const vs = j.variants || [];
  return {
    name: j.title, color: '', price: (j.price || 0) / 100, currency: 'RON', method: 'shopify',
    sizes: vs.filter((v) => v.available).map((v) => v.option1), unavailable: vs.filter((v) => !v.available).map((v) => v.option1),
    in_stock: vs.some((v) => v.available), gtins: vs.map((v) => v.barcode).filter(Boolean), skus: vs.map((v) => v.sku).filter(Boolean),
    options: (j.options || []).map((o) => o.name), tags: j.tags, type: j.type, vendor: j.vendor,
    image: (j.featured_image || '').replace(/^\/\//, 'https://'), images: (j.images || []).slice(0, 4).map((x) => x.replace(/^\/\//, 'https://')),
    description: String(j.description || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 600),
    isProduct: true,
  };
}

(async () => {
  const found = JSON.parse(fs.readFileSync(IN, 'utf8')).magazine;
  const hosts = Object.keys(found).filter((h) => found[h].produse.length && (!ONLY.length || ONLY.includes(h)));
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: 'new', ignoreDefaultArgs: ['--enable-automation'],
    args: ['--no-sandbox', '--disable-blink-features=AutomationControlled', '--lang=ro-RO', '--disable-dev-shm-usage'],
  });
  const out = {};
  const work = async (host) => {
    out[host] = [];
    const urls = found[host].produse.map((p) => p.url).slice(0, LIMIT || undefined);
    const page = await browser.newPage();
    await page.setViewport({ width: 1366, height: 900 });
    await page.setUserAgent((await browser.userAgent()).replace('HeadlessChrome', 'Chrome'));
    let n = 0;
    for (const url of urls) {
      n++;
      let d;
      try { d = host === '4kidspoint.ro' ? await shopify(url) : null; if (!d) d = await readPage(page, url); }
      catch (e) { d = { error: e.message.slice(0, 120) }; }
      out[host].push({ url, ...d });
      console.log(`${host} ${n}/${urls.length} ${d.error ? '✗ ' + d.error : '✓ ' + String(d.name || '').slice(0, 50) + ' | ' + (d.color || '-') + ' | ' + (d.sizes || []).length + ' mărimi'}`);
      fs.writeFileSync(OUT, JSON.stringify({ brand: BRAND, la: new Date().toISOString(), magazine: out }, null, 1));
      await sleep(DELAY);
    }
    await page.close();
  };
  await Promise.all(hosts.map(work));
  await browser.close();
  console.log('Scris în', OUT);
})().catch((e) => { console.error(e); process.exit(1); });
