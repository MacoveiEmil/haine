/**
 * Extrage de pe pagina magazinului sursă faptele pentru descrieri (material, detalii, croială):
 * deschide secțiunile pliate („Material și îngrijire", „Detalii", „Mărime și croială" la Zalando,
 * „Detalii produs" la About You) și salvează textul în sursele de descriere, pe cheia produsului.
 * NU scrie nimic în site.
 *
 * Rulare: node brand-desc-extract.js [brand-drafts-build.json] [LIMIT=n] [ONLY=cheie1,cheie2]
 * Scrie brand-surse/{cheie}.json (cheie cu „:" → „_"); format ca content/surse/{id}.json.
 */
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');
const CHROME = process.env.CHROME || (process.platform === 'win32' ? 'C:/Program Files/Google/Chrome/Application/chrome.exe' : '/usr/bin/google-chrome');
const IN = process.argv[2] || path.join(__dirname, 'brand-drafts-build.json');
const OUTDIR = path.join(__dirname, 'brand-surse');
const LIMIT = parseInt(process.env.LIMIT || '0', 10);
const ONLY = (process.env.ONLY || '').split(',').filter(Boolean);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
  fs.mkdirSync(OUTDIR, { recursive: true });
  let items = JSON.parse(fs.readFileSync(IN, 'utf8'));
  if (ONLY.length) items = items.filter((d) => ONLY.includes(d.key));
  if (process.env.HOSTS) { const H = process.env.HOSTS.split(','); items = items.filter((d) => H.includes((d.offers.find((o) => o.source) || d.offers[0]).host)); }
  if (process.env.REVERSE) items.reverse();
  if (LIMIT) items = items.slice(0, LIMIT);
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--window-size=1366,900', '--lang=ro-RO'] });
  const ua = (await browser.userAgent()).replace('HeadlessChrome', 'Chrome');
  let n = 0;
  for (let ix = 0; ix < items.length; ix++) {
    const d = items[ix];
    n++;
    const file = path.join(OUTDIR, d.key.replace(/[^a-z0-9-]+/gi, '_') + '.json');
    if (fs.existsSync(file) && !process.env.FORCE) continue;
    const prim = d.offers.find((o) => o.source) || d.offers[0];
    const url = prim.url;
    const page = await browser.newPage();
    await page.setUserAgent(ua);
    await page.setViewport({ width: 1366, height: 900 });
    await page.setRequestInterception(true);
    page.on('request', (r) => (['image', 'font', 'media'].includes(r.resourceType()) ? r.abort() : r.continue()));
    let rec;
    const tries = (d._t = (d._t || 0) + 1);
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await page.waitForSelector('h1', { timeout: 20000 }).catch(() => {});
      await sleep(3500);
      // deschide secțiunile pliate
      await page.evaluate(async () => {
        const want = /^(material și îngrijire|material si ingrijire|detalii|mărime și croială|descriere|detalii produs|materiale|compoziție|descrierea produsului)/i;
        const els = [...document.querySelectorAll('button,[role="button"],summary,h2,h3,a,div[tabindex]')].filter((e) => want.test((e.innerText || '').trim().slice(0, 40)));
        for (const e of els.slice(0, 8)) { try { e.click(); } catch (x) {} await new Promise((r) => setTimeout(r, 400)); }
      }).catch(() => {});
      await sleep(1200);
      const data = await page.evaluate(() => {
        const r = { h1: (document.querySelector('h1') || {}).innerText || document.title };
        for (const s of document.querySelectorAll('script[type="application/ld+json"]')) {
          try { const j = JSON.parse(s.textContent); const arr = Array.isArray(j) ? j : (j['@graph'] || [j]); const p = arr.find((x) => /Product/.test(x['@type'])); if (p) { r.ld = { name: p.name, description: p.description, color: p.color, material: p.material, sku: p.sku, mpn: p.mpn, brand: p.brand && (p.brand.name || p.brand) }; } } catch (e) {}
        }
        // Galeria produsului: toate pozele (Zalando / About You / Shopify), la rezoluție mare, fără duplicate
        const seen = new Set(); r.imgs = [];
        // doar pozele de ÎNAINTEA butonului „Adaugă în coș" (galeria produsului); mai jos sunt caruselurile altor produse
        const cart = [...document.querySelectorAll('button,a,[role="button"]')].find((e) => /^(adaug[aă] [iî]n co[sș]|adaug[aă] [iî]n co[sș]ul)/i.test((e.innerText || '').trim()));
        document.querySelectorAll('img[src],img[srcset],source[srcset]').forEach((im) => {
          if (cart && !(cart.compareDocumentPosition(im) & Node.DOCUMENT_POSITION_PRECEDING)) return;
          const raw = im.getAttribute('src') || (im.getAttribute('srcset') || '').split(' ')[0];
          let u = (raw || '').trim();
          let key = '';
          if (/img\d*\.ztat\.net\/article\/spp-media/.test(u)) { key = u.split('?')[0]; u = key + '?imwidth=800&filter=packshot'; }
          else if (/cdn\.aboutstatic\.com\/file\/images\//.test(u)) { key = u.split('?')[0]; u = key + '?quality=75&trim=1&width=900'; }
          else if (/cdn\.shopify\.com\/s\/files/.test(u)) { key = u.split('?')[0]; u = key; }
          else return;
          if (key && !seen.has(key)) { seen.add(key); r.imgs.push(u); }
        });
        r.imgs = r.imgs.slice(0, 8);
        const main = document.querySelector('main') || document.body;
        r.text = (main.innerText || '').replace(/\n{2,}/g, '\n').slice(0, 9000);
        return r;
      });
      if (/a ap[aă]rut o problem[aă] [iî]n garderob[aă]|access denied/i.test(data.text) || data.text.length < Number(process.env.MINLEN || 1500)) throw new Error('pagină de eroare / blocată (încercare ' + tries + ')');
      rec = { extras_la: new Date().toISOString(), key: d.key, sursa: prim.host, titlu_site: d.title, url, ...data };
      console.log(`✓ ${n}/${items.length} ${d.key} ${prim.host} text ${data.text.length}`);
    } catch (e) {
      console.log(`✗ ${n}/${items.length} ${d.key} ${e.message}`);
      await page.close();
      if (d._t < 4) { items.push(d); await sleep(20000 * d._t); } // mai încolo, mai lent
      else fs.writeFileSync(file, JSON.stringify({ key: d.key, url, eroare: e.message }, null, 1));
      continue;
    }
    await page.close();
    fs.writeFileSync(file, JSON.stringify(rec, null, 1));
    await sleep(Number(process.env.GAP || 2500));
  }
  await browser.close();
})();
