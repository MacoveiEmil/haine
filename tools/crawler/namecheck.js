/**
 * Cross-check pe NUME MODEL pentru produsele Sportisimo cu branduri mainstream.
 *
 * Lens (imagine) nu prinde produsele Sportisimo (fotografii proprii). Aici căutăm
 * „{brand} {model}" pe Google și extragem rezultatele de pe magazinele safe
 * (Answear, Modivo, Zalando, About You, epantofi, Fashion Days...). Sar brandurile
 * exclusive Sportisimo (ALPINE PRO, LOAP, Kilpi...) și produsele deja în lens-matches.
 *
 * Rulare: node namecheck.js   (env: SITE, SECRET, MAX, DELAY, MATCHES, OUT)
 * CSV: id, brand, model, query, site, url_produs, titlu
 */
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const MAX    = parseInt(process.env.MAX || '0', 10);
const DELAY  = parseInt(process.env.DELAY || '3000', 10);
const MATCHES = parseInt(process.env.MATCHES || '4', 10);
const RESTART_EVERY = parseInt(process.env.RESTART_EVERY || '15', 10);
const OUT    = process.env.OUT || path.join(__dirname, 'namecheck-matches.csv');
const LENS   = path.join(__dirname, 'lens-matches.csv');
const PROFILE = path.join(__dirname, '.namecheck-profile');
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const sleep  = (ms) => new Promise((r) => setTimeout(r, ms));
const jitter = (ms) => ms + Math.floor(Math.random() * ms * 0.5);

// Branduri sold și în altă parte (merită cross-check). Restul (ALPINE PRO, LOAP,
// Kilpi, Klimatex, Umbro, Willard) sunt exclusive Sportisimo → le sărim.
const MAINSTREAM = ['reima', 'geox', 'tommy', 'columbia', 'gap', '4f', 'primigi', 'didriksons', 'head', 'nike', 'adidas', 'puma', 'new-balance', 'name-it', 'guess', 'boss', 'calvin-klein'];
const SAFE = ['answear.ro', 'answear.com', 'modivo.ro', 'epantofi.ro', 'zalando', 'aboutyou', 'fashiondays.ro', 'sportvision.ro', 'sizeer', 'eobuwie', 'giraffe', 'notino'];

async function getQueue() {
  const r = await fetch(`${SITE}/wp-json/hainute/v1/sportisimo-queue?secret=${encodeURIComponent(SECRET)}&limit=2000`);
  if (!r.ok) throw new Error(`sportisimo-queue HTTP ${r.status}`);
  return (await r.json()).queue || [];
}
function lensIds() {
  try { return new Set(fs.readFileSync(LENS, 'utf8').split('\n').slice(1).map((l) => l.split(',')[0]).filter(Boolean)); }
  catch (e) { return new Set(); }
}
function rawStoreUrl(url) {
  // URL-ul poate fi împachetat CJ: click-...?url={sportisimo encoded}. Scoate destinația.
  try { const u = new URL(url); const inner = u.searchParams.get('url'); if (inner) return inner; } catch (e) {}
  return url;
}
function parseBrandModel(url) {
  url = rawStoreUrl(url);
  try {
    const segs = new URL(url).pathname.split('/').filter(Boolean); // [brand, model, spid]
    while (segs.length && /^\d+$/.test(segs[segs.length - 1])) segs.pop();
    return { brand: (segs[0] || '').toLowerCase(), model: (segs[1] || '').replace(/-/g, ' ') };
  } catch (e) { return { brand: '', model: '' }; }
}

async function searchGoogle(page, query) {
  await page.goto('https://www.google.com/search?q=' + encodeURIComponent(query), { waitUntil: 'networkidle2', timeout: 35000 });
  await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((x) => /respinge tot|reject all|accept all|acceptă tot/i.test(x.textContent || ''));
    if (b) b.click();
  }).catch(() => {});
  await sleep(700);
  return page.evaluate((SAFE) => {
    if (/detectat.*neobișnuit|unusual traffic|nu ești robot|our systems have detected|recaptcha/i.test(document.body.innerText)) {
      return { captcha: true, results: [] };
    }
    const seen = new Set(), out = [];
    for (const a of document.querySelectorAll('a[href^="http"]')) {
      let host = '';
      try { host = new URL(a.href).hostname.replace(/^www\./, ''); } catch (e) { continue; }
      if (!SAFE.some((s) => host.includes(s))) continue;
      if (seen.has(host)) continue; // un rezultat per magazin
      seen.add(host);
      const h3 = a.querySelector('h3') || (a.closest('div') ? a.closest('div').querySelector('h3') : null);
      out.push({ host, url: a.href.split('#')[0], title: (h3 ? h3.textContent : '').trim().slice(0, 130) });
    }
    return { captcha: false, results: out };
  }, SAFE);
}

function csvCell(s) { s = String(s == null ? '' : s); return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; }

async function main() {
  let queue = await getQueue();
  const skip = lensIds();
  // Doar Sportisimo (queue e deja sportisimo) + brand mainstream + nu-i deja în lens.
  let targets = [];
  for (const it of queue) {
    const bm = parseBrandModel(it.url);
    if (!bm.brand || !bm.model) continue;
    if (!MAINSTREAM.some((b) => bm.brand.includes(b))) continue;
    if (skip.has(String(it.product_id))) continue;
    targets.push({ id: it.product_id, brand: bm.brand, model: bm.model });
  }
  // dedup pe id
  const seenId = new Set();
  targets = targets.filter((t) => (seenId.has(t.id) ? false : seenId.add(t.id)));
  if (MAX > 0) targets = targets.slice(0, MAX);
  console.log(`Target: ${targets.length} produse Sportisimo mainstream (nu-s în lens)`);

  const header = ['id', 'brand', 'model', 'query', 'site', 'url_produs', 'titlu'];
  if (!fs.existsSync(OUT) || fs.statSync(OUT).size === 0) fs.writeFileSync(OUT, header.join(',') + '\n');

  const launch = () => puppeteer.launch({ executablePath: CHROME, headless: 'new', userDataDir: PROFILE, args: ['--no-sandbox', '--disable-blink-features=AutomationControlled', '--lang=ro-RO'] });
  let browser = await launch();
  let page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });

  let done = 0, withM = 0, rows = 0, streak = 0;
  for (const t of targets) {
    done++;
    if (done > 1 && (done % RESTART_EVERY) === 1) {
      try { await browser.close(); } catch (e) {}
      browser = await launch(); page = await browser.newPage();
      await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */ await page.setViewport({ width: 1280, height: 900 });
    }
    const query = `${t.brand} ${t.model} copii`.replace(/\s+/g, ' ').trim();
    let res = { captcha: false, results: [] };
    try { res = await searchGoogle(page, query); } catch (e) { console.log(`[${done}/${targets.length}] #${t.id} eroare: ${e.message}`); }
    if (res.captcha) {
      streak++;
      console.log(`[${done}/${targets.length}] #${t.id} — CAPTCHA (skip), pauză`);
      try { await browser.close(); } catch (e) {}
      await sleep(streak >= 2 ? 90000 : 30000);
      browser = await launch(); page = await browser.newPage();
      await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */ await page.setViewport({ width: 1280, height: 900 });
      continue;
    }
    streak = 0;
    const top = res.results.slice(0, MATCHES);
    if (top.length) withM++;
    for (const m of top) {
      fs.appendFileSync(OUT, [t.id, t.brand, t.model, query, m.host, m.url, m.title].map(csvCell).join(',') + '\n');
      rows++;
    }
    console.log(`[${done}/${targets.length}] #${t.id} ${t.brand} ${t.model} — ${top.length} potriviri`);
    await sleep(jitter(DELAY));
  }
  await browser.close();
  console.log(`\nGata. Produse cu potriviri: ${withM}/${targets.length}. Rânduri CSV: ${rows}.`);
  console.log(`CSV: ${OUT}`);
}
main().catch((e) => { console.error(e); process.exit(1); });
