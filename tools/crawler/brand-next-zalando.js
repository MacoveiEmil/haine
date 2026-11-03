/**
 * Adună paginile de produs Next pentru copii din listarea Zalando (/catalog-copii/next/),
 * primele PAGES pagini (implicit 2). Scrie în brand-next-f.json (formatul brand-search.js),
 * ca să urmeze brand-scan.js. NU scrie nimic în site.
 * Rulare: PAGES=2 node brand-next-zalando.js
 */
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');
const CHROME = process.env.CHROME || (process.platform === 'win32' ? 'C:/Program Files/Google/Chrome/Application/chrome.exe' : '/usr/bin/google-chrome');
const PAGES = parseInt(process.env.PAGES || '2', 10);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--window-size=1366,900', '--lang=ro-RO'] });
  const urls = new Set();
  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1366, height: 900 });
    await page.setUserAgent((await browser.userAgent()).replace('HeadlessChrome', 'Chrome'));
    for (let p = 1; p <= PAGES; p++) {
      await page.goto(`https://www.zalando.ro/catalog-copii/next/${p > 1 ? '?p=' + p : ''}`, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await sleep(2500);
      for (let i = 0; i < 14; i++) { await page.evaluate(() => window.scrollBy(0, 1400)); await sleep(500); }
      const found = await page.evaluate(() => [...document.querySelectorAll('a[href]')].map((a) => a.href.split('?')[0]).filter((h) => /^https:\/\/www\.zalando\.ro\/next-[^/]+\.html$/.test(h)));
      found.forEach((u) => urls.add(u));
      console.log(`pagina ${p}: ${found.length} linkuri, total ${urls.size}`);
    }
  } finally { await browser.close(); }
  const out = { brand: 'next', la: new Date().toISOString(), magazine: { 'zalando.ro': { gasite: urls.size, produse: [...urls].map((url) => ({ url, text: '' })), incercari: [] } } };
  fs.writeFileSync(path.join(__dirname, 'brand-next-f.json'), JSON.stringify(out));
})();
