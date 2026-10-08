/** Re-crawl țintit al unui singur produs Answear. Env: PID, URL, SITE, SECRET. */
const puppeteer = require('puppeteer-core');
const PID = process.env.PID, URL = process.env.URL;
const SITE = process.env.SITE || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

function extract(html) {
  const out = { sizes: [], availability: '', sku: '' };
  const re = /<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;
  let m;
  while ((m = re.exec(html))) {
    let j; try { j = JSON.parse(m[1].trim()); } catch (e) { continue; }
    const st = [j];
    while (st.length) {
      const o = st.pop();
      if (!o || typeof o !== 'object') continue;
      if (o['@type'] === 'Product' || o['@type'] === 'ProductGroup') {
        if (o.size) out.sizes = [].concat(o.size).map(String).map((s) => s.trim()).filter(Boolean);
        if (o.sku) out.sku = String(o.sku);
        for (const of of [].concat(o.offers || [])) if (of && of.availability) { out.availability = String(of.availability).replace('https://schema.org/', ''); break; }
      }
      for (const k in o) if (o[k] && typeof o[k] === 'object') st.push(o[k]);
    }
  }
  return out;
}

(async () => {
  const b = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.goto(URL, { waitUntil: 'networkidle2', timeout: 35000 });
  await p.waitForFunction(() => {
    return [...document.querySelectorAll('script[type="application/ld+json"]')].some((s) => /"size"/.test(s.textContent || ''));
  }, { timeout: 8000 }).catch(() => {});
  const d = extract(await p.content());
  await b.close();
  await fetch(`${SITE}/wp-json/hainute/v1/crawl-result?secret=${SECRET}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ product_id: +PID, sizes: d.sizes, availability: d.availability, sku: d.sku }),
  });
  console.log('crawl:', JSON.stringify(d));
})();
