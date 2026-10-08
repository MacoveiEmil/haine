/**
 * Test rapid: Chrome headless trece de WAF-ul Answear și scoate JSON-LD-ul
 * (mărimi + disponibilitate + sku)? Rulează: node test-answear.js
 */
const puppeteer = require('puppeteer-core');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

const URLS = [
  'https://answear.ro/p/calvin-klein-jeans-compleu-de-trening-pentru-copii-cu-bumbac-roz-lv1cktji13-1819064',
  'https://answear.ro/p/adidas-geaca-petrecuta-pentru-copii-neagra-kh0197-1843627',
];

// Extrage din JSON-LD: sizes[], availability, sku, brand.
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
        if (o.size) out.sizes = [].concat(o.size).map(String);
        if (o.sku) out.sku = String(o.sku);
        if (o.brand) out.brand = o.brand.name || o.brand;
        const offers = [].concat(o.offers || []);
        for (const of of offers) {
          if (of && of.availability) { out.availability = String(of.availability).replace('https://schema.org/', ''); break; }
        }
      }
      for (const k in o) if (o[k] && typeof o[k] === 'object') stack.push(o[k]);
    }
  }
  return out;
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--no-sandbox', '--disable-blink-features=AutomationControlled', '--window-size=1280,900'],
  });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });

  for (const url of URLS) {
    try {
      const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
      const status = resp ? resp.status() : 0;
      const html = await page.content();
      const data = extractFromHtml(html);
      const blocked = /just a moment|attention required|captcha|access denied/i.test(html);
      console.log('\nURL:', url);
      console.log('  HTTP:', status, '| blocked:', blocked, '| html bytes:', html.length);
      console.log('  →', JSON.stringify(data));
    } catch (e) {
      console.log('\nURL:', url, '\n  EROARE:', e.message);
    }
  }

  await browser.close();
})();
