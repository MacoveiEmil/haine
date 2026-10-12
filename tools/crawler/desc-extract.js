/**
 * Pasul 1 din promptul de descrieri v3 (docs/prompt-descrieri-v3.md): deschide
 * pagina magazinului pentru fiecare produs și salvează tot ce e explicit acolo
 * (titlu, descriere, detalii, compoziție, culoare, cod, mărimi) într-un JSON
 * din care se scriu apoi descrierile. Nu scrie nimic pe site.
 *
 * Rulare: node desc-extract.js produse.tsv iesire.json
 *   produse.tsv: id<TAB>sursa<TAB>categorie<TAB>titlu<TAB>url
 */
const fs = require('fs');
const puppeteer = require('puppeteer-core');
const CHROME = process.env.CHROME || (process.platform === 'win32' ? 'C:/Program Files/Google/Chrome/Application/chrome.exe' : '/usr/bin/google-chrome');
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const rows = fs.readFileSync(process.argv[2], 'utf8').trim().split('\n').map((l) => l.split('\t'));
const realUrl = (u) => { try { const x = new URL(u); return x.searchParams.get('redirect_to') || x.searchParams.get('url') || u; } catch (e) { return u; } };

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new' });
  const ua = (await browser.userAgent()).replace('HeadlessChrome', 'Chrome');
  const out = [];
  for (const [id, src, cat, title, url0] of rows) {
    const url = realUrl(url0).split('?channable')[0];
    const page = await browser.newPage();
    await page.setUserAgent(ua);
    try {
      await page.goto(url, { waitUntil: 'networkidle2', timeout: 45000 });
      if (/various-brands/.test(url)) { // consent Cookiebot, apoi reîncarcă
        await page.evaluate(() => { const b = document.getElementById('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll') || [...document.querySelectorAll('button,a')].find((x) => /permite toate|accept all/i.test(x.textContent || '')); if (b) b.click(); }).catch(() => {});
        await sleep(1500);
        await page.goto(url, { waitUntil: 'networkidle2', timeout: 45000 });
      }
      await sleep(2500);
      const data = await page.evaluate(() => {
        const r = { h1: (document.querySelector('h1') || {}).innerText || document.title };
        // JSON-LD Product
        for (const s of document.querySelectorAll('script[type="application/ld+json"]')) {
          try { const j = JSON.parse(s.textContent); const arr = Array.isArray(j) ? j : (j['@graph'] || [j]); const p = arr.find((x) => /Product/.test(x['@type'])); if (p) { r.ld = { name: p.name, description: p.description, color: p.color, material: p.material, sku: p.sku, mpn: p.mpn, brand: p.brand && (p.brand.name || p.brand) }; } } catch (e) {}
        }
        // Answear: obiectul produsului din starea React (descriere completă, materiale, atribute, mărimi)
        if (window.__REACT_QUERY_STATE__) {
          const pid = (location.pathname.match(/-(\d+)$/) || [])[1];
          let best = null; const seen = new Set();
          const walk = (o, d) => { if (!o || typeof o !== 'object' || d > 14 || seen.has(o)) return; seen.add(o); if (!Array.isArray(o) && String(o.id) === pid && (o.description || o.fullDescription)) best = o; for (const k of Object.keys(o)) walk(o[k], d + 1); };
          try { walk(window.__REACT_QUERY_STATE__, 0); } catch (e) {}
          if (best) {
            r.answear = {
              name: best.name, code: best.code || best.productCode, description: best.description, fullDescription: best.fullDescription,
              materials: best.materials, careInstructions: best.careInstructions,
              attributes: (best.attributes || []).map((a) => `${a.name}: ${a.value}`),
              sizes: (best.productSizes || best.sizes || []).map((s) => `${s.name}${s.variation && s.variation.availability === 'OUT_OF_STOCK' ? ' (epuizat)' : ''}`),
              color: best.color && (best.color.name || best.color), sizeChartType: best.sizeChartType,
            };
            if (!r.answear.sizes.length) { for (const k of Object.keys(best)) if (Array.isArray(best[k]) && best[k][0] && best[k][0].variation) r.answear.sizes = best[k].map((s) => `${s.name}${s.variation.availability === 'OUT_OF_STOCK' ? ' (epuizat)' : ''}`); }
          }
        }
        // Text vizibil din zona de produs (descriere / detalii / compoziție), pentru celelalte magazine
        const main = document.querySelector('main') || document.body;
        r.text = (main.innerText || '').replace(/\n{2,}/g, '\n').slice(0, 7000);
        return r;
      });
      out.push({ id: +id, sursa: src, categorie: cat, titlu_site: title, url, ...data });
      console.log(`✓ #${id} ${src} ${data.h1.slice(0, 60)}`);
    } catch (e) {
      out.push({ id: +id, sursa: src, url, eroare: e.message });
      console.log(`✗ #${id} ${e.message}`);
    }
    await page.close();
    await sleep(1500);
  }
  await browser.close();
  fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1));
})();
