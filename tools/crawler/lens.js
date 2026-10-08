/**
 * Reverse image search prin Google Lens pentru hainute.ro.
 *
 * Ia produsele PUBLICATE (id + imagine) din /image-list, caută fiecare imagine pe
 * Google Lens (uploadbyurl), extrage potrivirile vizuale (site + URL produs de pe
 * acel site), prioritizează magazinele "safe" pentru manual cross (Modivo, Answear,
 * epantofi, Sportisimo, Farfetch, Fashion Days, Zalando...) și scrie un CSV pentru
 * revizuire manuală. NU adaugă nimic direct în comparator.
 *
 * Rulare: node lens.js
 *   env: SITE, SECRET, MAX (0=tot), DELAY (ms între produse), MATCHES (rânduri/produs),
 *        OUT (fișier csv), START (offset în listă), HEADLESS (0=headful pentru debug)
 *
 * CSV: id, brand, poza_mea, poza_gasita, site, url_produs, titlu, in_stoc, safe
 */
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const SITE    = process.env.SITE   || 'http://hainutero.local';
const SECRET  = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const CHROME  = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const MAX     = parseInt(process.env.MAX || '0', 10);
const DELAY   = parseInt(process.env.DELAY || '1200', 10);
const MATCHES = parseInt(process.env.MATCHES || '3', 10);
const START   = parseInt(process.env.START || '0', 10);
const HEADLESS = process.env.HEADLESS === '0' ? false : 'new';
const OUT     = process.env.OUT || path.join(__dirname, 'lens-matches.csv');
const PROFILE = path.join(__dirname, '.lens-profile');
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Magazine unde extractorul manual cross merge bine (anti-bot gestionat / JSON-LD curat).
const SAFE = [
  'modivo.ro', 'modivo.pl', 'modivo.hu', 'answear.ro', 'answear.com', 'answear.hu',
  'epantofi.ro', 'sportisimo.ro', 'farfetch.com', 'fashiondays.ro', 'zalando',
  'sportvision.ro', 'deichmann', 'aboutyou', 'notino', 'sizeer.ro', 'footlocker',
  'giraffe', 'eobuwie', 'ccc.eu', 'sportano', 'about-you',
];
const isSafe = (host) => SAFE.some((s) => host.includes(s));

async function getList() {
  const r = await fetch(`${SITE}/wp-json/hainute/v1/image-list?secret=${encodeURIComponent(SECRET)}&status=publish`);
  if (!r.ok) throw new Error(`image-list HTTP ${r.status}`);
  const j = await r.json();
  return j.items || [];
}

async function acceptConsent(page) {
  // Google poate afișa un ecran de consimțământ (consent.google.com) la prima accesare.
  try {
    if (/consent\.google/.test(page.url())) {
      await page.evaluate(() => {
        const b = [...document.querySelectorAll('button')].find((x) =>
          /accept all|acceptă tot|tot de acord|accept the use|agree/i.test((x.textContent || '')));
        if (b) b.click();
      });
      await page.waitForNavigation({ timeout: 10000 }).catch(() => {});
    }
  } catch (e) { /* noop */ }
}

function countExternal() {
  let n = 0;
  for (const a of document.querySelectorAll('a[href^="http"]')) {
    if (!/google\.|gstatic|googleusercontent|youtube\./.test(a.href)) n++;
  }
  return n;
}

async function lensFor(page, imageUrl) {
  const url = 'https://lens.google.com/uploadbyurl?url=' + encodeURIComponent(imageUrl);
  for (let attempt = 1; attempt <= 2; attempt++) {
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 45000 });
    await acceptConsent(page);
    if (/consent\.google/.test(page.url())) {
      await page.goto(url, { waitUntil: 'networkidle2', timeout: 45000 });
      await acceptConsent(page);
    }
    // Așteaptă potrivirile vizuale (link-uri externe reale).
    const ok = await page.waitForFunction(
      countExternal + '; countExternal() > 5',
      { timeout: 20000 }
    ).then(() => true).catch(() => false);
    if (ok) { await sleep(900); break; }
    if (attempt === 1) await sleep(2500); // retry o dată dacă a venit gol
  }

  return page.evaluate(() => {
    const seen = new Set();
    const out = [];
    for (const a of document.querySelectorAll('a[href^="http"]')) {
      const href = a.href;
      if (/google\.|gstatic|googleusercontent|youtube\.|schema\.org|policies|support\./.test(href)) continue;
      const txt = (a.innerText || '').replace(/\s+/g, ' ').trim();
      if (!txt) continue;
      let host = '';
      try { host = new URL(href).hostname.replace(/^www\./, ''); } catch (e) { continue; }
      if (seen.has(host)) continue; // un rezultat / magazin
      seen.add(host);
      const inStock = /în stoc|in stock|disponibil|available/i.test(txt);
      const img = a.querySelector('img');
      let imgSrc = img ? (img.src || '') : '';
      // Lens dă thumbnail base64 / favicon gstatic — niciunul nu e URL de imagine real.
      if (imgSrc.startsWith('data:') || /gstatic|favicon|googleusercontent/.test(imgSrc)) imgSrc = '';
      out.push({ href, host, txt: txt.slice(0, 140), in_stock: inStock, img: imgSrc });
    }
    return out;
  });
}

function rank(matches) {
  return matches
    .map((m) => ({ ...m, safe: isSafe(m.host) }))
    .sort((a, b) => (b.safe - a.safe) || (b.in_stock - a.in_stock));
}

function csvCell(s) {
  s = String(s == null ? '' : s);
  return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
}

async function main() {
  let items = await getList();
  if (START > 0) items = items.slice(START);
  if (MAX > 0) items = items.slice(0, MAX);
  console.log(`Produse de procesat: ${items.length} (din publish)`);

  const header = ['id', 'brand', 'poza_mea', 'poza_gasita', 'site', 'url_produs', 'titlu', 'in_stoc', 'safe'];
  // Scriem header doar dacă fișierul nu există (permite reluare cu START).
  if (!fs.existsSync(OUT) || fs.statSync(OUT).size === 0) {
    fs.writeFileSync(OUT, header.join(',') + '\n');
  }

  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: HEADLESS,
    userDataDir: PROFILE,
    args: ['--no-sandbox', '--disable-blink-features=AutomationControlled', '--lang=ro-RO'],
  });
  const page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });

  // Warm-up: rezolvă ecranul de consimțământ Google o singură dată la început.
  try {
    await page.goto('https://lens.google.com/', { waitUntil: 'networkidle2', timeout: 30000 });
    await acceptConsent(page);
    await sleep(1500);
  } catch (e) { /* noop */ }

  let done = 0, withMatches = 0, rows = 0;
  for (const it of items) {
    done++;
    if (!it.image) { console.log(`[${done}/${items.length}] #${it.id} — fără imagine, skip`); continue; }
    let matches = [];
    try {
      matches = await lensFor(page, it.image);
    } catch (e) {
      console.log(`[${done}/${items.length}] #${it.id} — eroare: ${e.message}`);
    }
    const ranked = rank(matches).slice(0, MATCHES);
    if (ranked.length) withMatches++;
    for (const m of ranked) {
      const line = [it.id, it.brand, it.image, m.img, m.host, m.href, m.txt, m.in_stock ? '1' : '', m.safe ? '1' : '']
        .map(csvCell).join(',');
      fs.appendFileSync(OUT, line + '\n');
      rows++;
    }
    const tag = ranked.filter((r) => r.safe).length;
    console.log(`[${done}/${items.length}] #${it.id} ${it.brand} — ${ranked.length} match (${tag} safe)`);
    await sleep(DELAY);
  }

  await browser.close();
  console.log(`\nGata. Produse cu potriviri: ${withMatches}/${items.length}. Rânduri CSV: ${rows}.`);
  console.log(`CSV: ${OUT}`);
}

main().catch((e) => { console.error(e); process.exit(1); });
