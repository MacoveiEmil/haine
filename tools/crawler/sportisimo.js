/**
 * Recheck Sportisimo pentru hainute.ro.
 *
 * Reîmprospătează preț/stoc + mărimile DISPONIBILE (și cele indisponibile, tăiate)
 * pentru produsele publicate cu ofertă sportisimo.ro. Sportisimo nu ne dă mărimile
 * din feed → le citim din pagina reală (JSON-LD Product pt preț/availability +
 * widget-ul de mărimi `.p-select`). Chrome real, trece de anti-bot.
 *
 * Rulare: node sportisimo.js   (env: SITE, SECRET, MAX, DELAY, LIMIT)
 */
const puppeteer = require('puppeteer-core');

const SITE   = process.env.SITE   || 'http://hainutero.local';
const SECRET = process.env.SECRET || 'pune-aici-un-sir-lung-aleatoriu-abc123xyz';
const CHROME = process.env.CHROME || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const MAX    = parseInt(process.env.MAX || '0', 10);
const DELAY  = parseInt(process.env.DELAY || '3500', 10);
const LIMIT  = parseInt(process.env.LIMIT || '150', 10);
const RESTART_EVERY = parseInt(process.env.RESTART_EVERY || '15', 10); // sesiune nouă la N produse
const jitter = (ms) => ms + Math.floor(Math.random() * ms * 0.6);
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function getQueue() {
  const r = await fetch(`${SITE}/wp-json/hainute/v1/sportisimo-queue?secret=${encodeURIComponent(SECRET)}&limit=${LIMIT}${process.env.IDS ? '&ids=' + process.env.IDS : ''}`);
  if (!r.ok) throw new Error(`sportisimo-queue HTTP ${r.status}`);
  return (await r.json()).queue || [];
}
async function postResult(p) {
  const r = await fetch(`${SITE}/wp-json/hainute/v1/sportisimo-result?secret=${encodeURIComponent(SECRET)}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(p),
  });
  return r.json().catch(() => ({}));
}

async function acceptCookies(page) {
  await page.evaluate(() => {
    const b = [...document.querySelectorAll('button,a')].find((x) =>
      /accept|sunt de acord|de acord|permite/i.test((x.textContent || '').trim()) && (x.textContent || '').length < 40);
    if (b) b.click();
  }).catch(() => {});
}

function extract(page) {
  return page.evaluate(() => {
    const out = { name: '', price: 0, in_stock: true, sizes: [], sizes_unavailable: [] };
    // JSON-LD Product: name, price, availability.
    for (const s of document.querySelectorAll('script[type="application/ld+json"]')) {
      let j; try { j = JSON.parse(s.textContent); } catch (e) { continue; }
      (function f(o) {
        if (!o || typeof o !== 'object') return;
        if (o['@type'] === 'Product') {
          if (o.name) out.name = String(o.name);
          const of = [].concat(o.offers || [])[0] || {};
          if (of.price) out.price = parseFloat(String(of.price).replace(',', '.'));
          if (of.availability) out.in_stock = /InStock/i.test(String(of.availability));
        }
        for (const k in o) if (typeof o[k] === 'object') f(o[k]);
      })(j);
    }
    // Fallback preț din body.
    if (!out.price) {
      const pm = document.body.innerText.match(/(\d{2,4}[.,]\d{2})\s*lei/i);
      if (pm) out.price = parseFloat(pm[1].replace(',', '.'));
    }
    // „Produs indisponibil" la nivel de produs.
    if (/produs(ul)?\s+(este\s+)?indisponibil|stoc epuizat/i.test(document.body.innerText)) out.in_stock = false;

    // Mărimi din widget-ul `.p-select`: <button class="p-select__option"> = disponibil,
    // <div class="p-select__option--disabled"> = epuizat. Text: „28 EU", „122-128", „XS".
    // (Varianta veche citea textul frunzelor și nu vedea starea de pe părinte →
    // raporta mărimi epuizate ca disponibile.)
    const rx = /^(\d{2,3}([.,\/-]\d{1,3})?|\d{1,2}Y|XXS|XS|S|M|L|XL|XXL|XXXL)$/i;
    const box = document.querySelector('.p-select') || document.querySelector('[class*="p-select"]');
    const seenA = new Set(), seenU = new Set();
    if (box) box.querySelectorAll('.p-select__option').forEach((o) => {
      const sp = o.querySelector('span') || o;
      const t = (sp.textContent || '').trim().replace(/\s*EU$/i, '');
      if (!rx.test(t)) return;
      const dis = /--disabled/.test(String(o.className)) || o.disabled;
      if (dis) { if (!seenU.has(t)) { seenU.add(t); out.sizes_unavailable.push(t); } }
      else { if (!seenA.has(t)) { seenA.add(t); out.sizes.push(t); } }
    });
    // O mărime nu poate fi și disponibilă și indisponibilă.
    out.sizes_unavailable = out.sizes_unavailable.filter((s) => !seenA.has(s));
    return out;
  });
}

async function main() {
  let queue = await getQueue();
  if (MAX > 0) queue = queue.slice(0, MAX);
  console.log(`Recheck Sportisimo: ${queue.length} produse`);

  const launch = () => puppeteer.launch({
    executablePath: CHROME, headless: 'new',
    args: ['--no-sandbox', '--disable-blink-features=AutomationControlled', '--lang=ro-RO'],
  });
  let browser = await launch();
  let page = await browser.newPage();
  await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
  await page.setViewport({ width: 1280, height: 900 });

  let done = 0, ok = 0, oos = 0, empties = 0, streak = 0;
  for (const it of queue) {
    done++;
    // Sesiune nouă periodic (evită rate-limit-ul Sportisimo pe sesiune/cookie).
    if (done > 1 && (done % RESTART_EVERY) === 1) {
      try { await browser.close(); } catch (e) {}
      browser = await launch();
      page = await browser.newPage();
      await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */
      await page.setViewport({ width: 1280, height: 900 });
    }
    let data = null;
    try {
      await page.goto(it.url, { waitUntil: 'networkidle2', timeout: 40000 });
      await acceptCookies(page);
      await sleep(800);
      data = await extract(page);
    } catch (e) {
      console.log(`[${done}/${queue.length}] #${it.product_id} — eroare: ${e.message}`);
      continue;
    }
    // Extragere goală = probabil blocaj/redirect → NU marca „verificat", reia altă dată.
    if (!data.price && data.sizes.length === 0) {
      empties++; streak++;
      console.log(`[${done}/${queue.length}] #${it.product_id} — gol (skip, retry later)`);
      if (streak >= 3) {
        console.log('   …3 goale la rand -> pauza 60s + sesiune noua');
        try { await browser.close(); } catch (e) {}
        await sleep(60000);
        browser = await launch(); page = await browser.newPage();
        await page.setUserAgent((await page.browser().userAgent()).replace('HeadlessChrome', 'Chrome')); /* UA real: o versiune falsă ≠ Client Hints e semnal de bot */ await page.setViewport({ width: 1280, height: 900 });
        streak = 0;
      }
      await sleep(jitter(DELAY));
      continue;
    }
    streak = 0;
    const res = await postResult({
      product_id: it.product_id, store_id: it.store_id,
      price: data.price, in_stock: data.in_stock,
      sizes: data.sizes, sizes_unavailable: data.sizes_unavailable,
    });
    if (res && res.ok) ok++;
    if (!data.in_stock) oos++;
    console.log(`[${done}/${queue.length}] #${it.product_id} ${data.name || ''} — ${data.price} lei, ${data.in_stock ? 'stoc' : 'FĂRĂ stoc'}, mărimi: ${data.sizes.join('/') || '—'}${data.sizes_unavailable.length ? ' (indispon: ' + data.sizes_unavailable.join('/') + ')' : ''}`);
    await sleep(jitter(DELAY));
  }
  await browser.close();
  console.log(`\nGata. Actualizate: ${ok}/${queue.length}. Fără stoc: ${oos}. Goale (de reluat): ${empties}.`);
}

main().catch((e) => { console.error(e); process.exit(1); });
