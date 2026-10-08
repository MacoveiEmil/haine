/**
 * Extragere specificații reale pentru hainute.ro (partea A din prompt-ul de descriere).
 *
 * Deschide pagina fiecărui produs pe magazinul sursă (Answear/Sportisimo/Fashion Days/
 * various-brands), extrage MATERIAL + specs + caracteristici și le salvează în meta
 * (`_hainute_specs`, `_hainute_features`, `_hainute_extract`) pentru descrieri + folosire
 * ulterioară. Chrome real, trece de anti-bot. Reia automat (coada = cele mai vechi extrase).
 *
 * Rulare: node specscrawl.js   (env: SITE, SECRET, MAX, DELAY, LIMIT, STORE, RESTART_EVERY)
 */
const puppeteer = require('puppeteer-core');
const path = require('path');

const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const MAX    = parseInt(process.env.MAX || '0', 10);
const DELAY  = parseInt(process.env.DELAY || '2600', 10);
const LIMIT  = parseInt(process.env.LIMIT || '800', 10);
const STORE  = (process.env.STORE || '').toLowerCase();
const RESTART_EVERY = parseInt(process.env.RESTART_EVERY || '20', 10);
const PROFILE = path.join(__dirname, '.specs-profile');
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const sleep  = (ms) => new Promise((r) => setTimeout(r, ms));
const jitter = (ms) => ms + Math.floor(Math.random() * ms * 0.5);

async function getQueue() {
  const u = `${SITE}/wp-json/hainute/v1/specs-queue?secret=${encodeURIComponent(SECRET)}&limit=${LIMIT}` + (STORE ? `&store=${STORE}` : '');
  const r = await fetch(u);
  if (!r.ok) throw new Error(`specs-queue HTTP ${r.status}`);
  return (await r.json()).queue || [];
}
async function postResult(p) {
  const r = await fetch(`${SITE}/wp-json/hainute/v1/specs-result?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(p),
  });
  return r.json().catch(() => ({}));
}
async function acceptCookies(page) {
  await page.evaluate(() => {
    const ids = ['CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll', 'onetrust-accept-btn-handler', 'CybotCookiebotDialogBodyButtonAccept'];
    for (const id of ids) { const b = document.getElementById(id); if (b) { b.click(); return; } }
    const b = [...document.querySelectorAll('button,a')].find((x) => /accept|sunt de acord|de acord|permite toate|acceptă/i.test((x.textContent || '').trim()) && (x.textContent || '').length < 40);
    if (b) b.click();
  }).catch(() => {});
}

function extract(page) {
  return page.evaluate(() => {
    const out = { material: '', features: [], specs: {}, raw: {} };
    const text = document.body.innerText;

    // 1. Material — etichetat, VALIDAT (conține % sau un cuvânt de material real).
    const MATWORDS = /poliester|poliamid|piele|bumbac|nailon|elasta|lân[ăa]|vâscoz|acril|softshell|membran|poliuretan|textil|cauciuc|sintetic|nubuc|in\b|modal|cânep/i;
    for (const re of [
      /Materialul de baz[ăa]\s*[:\-]?\s*([^\n]{3,90})/i,
      /Compozi[țt]ie\s*[:\-]?\s*([^\n]{3,90})/i,
      /\bMaterial(?:ul)?\b\s*[:\-]?\s*([^\n]{3,90})/i,
    ]) {
      const m = text.match(re);
      if (m && (MATWORDS.test(m[1]) || /\d\s*%/.test(m[1]))) { out.material = m[1].trim().replace(/\s+/g, ' '); break; }
    }
    // linie de compoziție standalone (ex. „52% Poliester reciclat, 48% Poliester").
    if (!out.material) {
      const m = text.match(/(\d{1,3}\s*%\s*[A-Za-zăâîșțĂÂÎȘȚ][^\n]{2,80})/);
      if (m && MATWORDS.test(m[1])) out.material = m[1].trim().replace(/\s+/g, ' ');
    }
    // curăță etichete de parte (Gamba/Interior/Talpă) + „Material" redundant.
    if (out.material) {
      out.material = out.material
        .replace(/^(Gamba|Interior|Talp[ăa]|Bran[țt]|C[ăa]ptu[șs]eal[ăa]|Exterior|Parte superioar[ăa])\s*[:\-]?\s*/i, '')
        .replace(/^Material(?:ul)?\s*[:\-]?\s*/i, '')
        .replace(/\s*[,;]\s*$/, '')
        .trim();
    }

    // 2. Specs din tabele (th/td) și liste de definiții (dt/dd).
    document.querySelectorAll('table tr').forEach((tr) => {
      const c = tr.querySelectorAll('th,td');
      if (c.length >= 2) {
        const k = (c[0].innerText || '').trim(), v = (c[1].innerText || '').trim();
        if (k && v && k.length <= 40 && v.length <= 90 && !/^\s*$/.test(k)) out.specs[k] = v;
      }
    });
    document.querySelectorAll('dl').forEach((dl) => {
      const dt = dl.querySelectorAll('dt'), dd = dl.querySelectorAll('dd');
      for (let i = 0; i < Math.min(dt.length, dd.length); i++) {
        const k = (dt[i].innerText || '').trim(), v = (dd[i].innerText || '').trim();
        if (k && v && k.length <= 40 && v.length <= 90) out.specs[k] = v;
      }
    });

    // 3. Caracteristici — bullet-uri din zona de descriere/detalii (filtrăm UI-ul).
    const junk = /coș|coş|meniu|cont|coupon|newsletter|cookie|livrare|retur|reclamați|coleta|preț|coins|feedback|conectează|accesibilit|confidenț|termeni|garanți|adaug|selectează|mărime|marime|recenzi/i;
    const seen = new Set();
    document.querySelectorAll('li').forEach((li) => {
      if (li.children.length) return;
      const t = (li.innerText || '').trim().replace(/\s+/g, ' ');
      if (t.length >= 6 && t.length <= 90 && !junk.test(t) && /[a-zăâîșț]/i.test(t) && !seen.has(t.toLowerCase())) {
        seen.add(t.toLowerCase()); out.features.push(t);
      }
    });
    out.features = out.features.slice(0, 12);

    // JSON-LD (material/culoare uneori acolo).
    for (const s of document.querySelectorAll('script[type="application/ld+json"]')) {
      let j; try { j = JSON.parse(s.textContent); } catch (e) { continue; }
      (function f(o) {
        if (!o || typeof o !== 'object') return;
        if (o['@type'] === 'Product') {
          if (o.material && !out.material) out.material = String(o.material);
          if (o.sku) out.specs['Cod'] = String(o.sku);
        }
        for (const k in o) if (typeof o[k] === 'object') f(o[k]);
      })(j);
    }
    out.raw = { specs: out.specs, features: out.features, material: out.material };
    return out;
  });
}

async function main() {
  let queue = await getQueue();
  if (MAX > 0) queue = queue.slice(0, MAX);
  console.log(`Extragere specs: ${queue.length} produse` + (STORE ? ` (${STORE})` : ''));

  const launch = () => puppeteer.launch({ executablePath: CHROME, headless: 'new', userDataDir: PROFILE, args: ['--no-sandbox', '--disable-blink-features=AutomationControlled', '--lang=ro-RO'] });
  let browser = await launch();
  let page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });

  let done = 0, withMat = 0, empties = 0, streak = 0;
  for (const it of queue) {
    done++;
    if (done > 1 && (done % RESTART_EVERY) === 1) {
      try { await browser.close(); } catch (e) {}
      browser = await launch(); page = await browser.newPage();
      await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */ await page.setViewport({ width: 1280, height: 900 });
    }
    let data = null;
    try {
      await page.goto(it.url, { waitUntil: 'networkidle2', timeout: 40000 });
      await acceptCookies(page);
      // various-brands: cookie-wall → reload o dată după accept.
      if (it.store === 'vb') { await sleep(600); await page.goto(it.url, { waitUntil: 'networkidle2', timeout: 40000 }).catch(() => {}); }
      await sleep(800);
      data = await extract(page);
    } catch (e) {
      console.log(`[${done}/${queue.length}] #${it.product_id} — eroare: ${e.message}`);
      continue;
    }
    const gotSomething = data.material || Object.keys(data.specs).length || data.features.length;
    if (!gotSomething) {
      empties++; streak++;
      console.log(`[${done}/${queue.length}] #${it.product_id} (${it.store}) — gol`);
      if (streak >= 4) { try { await browser.close(); } catch (e) {} await sleep(45000); browser = await launch(); page = await browser.newPage(); await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */ await page.setViewport({ width: 1280, height: 900 }); streak = 0; }
      await sleep(jitter(DELAY));
      continue;
    }
    streak = 0;
    if (data.material) withMat++;
    await postResult({ product_id: it.product_id, material: data.material, features: data.features, specs: data.specs, raw: data.raw });
    console.log(`[${done}/${queue.length}] #${it.product_id} (${it.store}) — material: ${data.material ? data.material.slice(0, 40) : '—'} | ${data.features.length} caract.`);
    await sleep(jitter(DELAY));
  }
  await browser.close();
  console.log(`\nGata. Cu material: ${withMat}/${queue.length}. Goale: ${empties}.`);
}
main().catch((e) => { console.error(e); process.exit(1); });
