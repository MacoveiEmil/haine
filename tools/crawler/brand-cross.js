/**
 * Potrivește produsele unui brand între magazine, după codul de bare (EAN) comun.
 * Citește brand-<slug>-produse.json (de la brand-scan.js), scrie brand-<slug>-cross.csv.
 * NU scrie nimic în site.
 *
 * Rulare: BRAND="en fant" node brand-cross.js
 */
const fs = require('fs');
const path = require('path');
const BRAND = (process.env.BRAND || 'en fant').trim();
const SLUG = BRAND.toLowerCase().replace(/\s+/g, '-');
const IN = path.join(__dirname, `brand-${SLUG}-produse.json`);
const OUT = path.join(__dirname, `brand-${SLUG}-cross.csv`);

const data = JSON.parse(fs.readFileSync(IN, 'utf8')).magazine;
const items = [];
for (const [host, list] of Object.entries(data)) {
  for (const p of list) {
    if (p.error || /^error page$/i.test(p.name || '')) continue;
    const ean = new Set((p.gtins || []).map((g) => String(g).replace(/^0+/, '')).filter((g) => g.length >= 8));
    items.push({ host, ...p, ean });
  }
}

// graf: două produse din magazine diferite sunt legate dacă au cel puțin un EAN comun
const parent = items.map((_, i) => i);
const find = (i) => (parent[i] === i ? i : (parent[i] = find(parent[i])));
const byEan = new Map();
items.forEach((it, i) => it.ean.forEach((e) => { if (!byEan.has(e)) byEan.set(e, []); byEan.get(e).push(i); }));
const overlap = {};
for (const idx of byEan.values()) {
  for (let a = 0; a < idx.length; a++) for (let b = a + 1; b < idx.length; b++) {
    const i = idx[a], j = idx[b];
    if (items[i].host === items[j].host) continue;
    const k = i < j ? `${i}-${j}` : `${j}-${i}`;
    overlap[k] = (overlap[k] || 0) + 1;
  }
}
// legăm doar perechile cu ≥2 EAN-uri comune (un EAN rătăcit dintr-un carusel nu e destul)
for (const [k, n] of Object.entries(overlap)) if (n >= 2) { const [i, j] = k.split('-').map(Number); parent[find(i)] = find(j); }

const groups = {};
items.forEach((it, i) => (groups[find(i)] = groups[find(i)] || []).push(it));
const cross = Object.values(groups).filter((g) => new Set(g.map((x) => x.host)).size >= 2);
const hostsOf = (g) => [...new Set(g.map((x) => x.host))].sort();

const q = (s) => `"${String(s ?? '').replace(/"/g, '""')}"`;
const rows = [['grup', 'magazine', 'magazin', 'nume', 'culoare', 'mărimi pe stoc', 'epuizate', 'preț', 'link']];
cross.sort((a, b) => hostsOf(b).length - hostsOf(a).length).forEach((g, n) => {
  g.sort((a, b) => a.host.localeCompare(b.host)).forEach((it) => rows.push([n + 1, hostsOf(g).join(' + '), it.host, it.name, it.color || '', (it.sizes || []).join(' '), (it.unavailable || []).join(' '), it.price ? `${it.price} ${it.currency || ''}`.trim() : '', it.url]));
});
fs.writeFileSync(OUT, '\ufeff' + rows.map((r) => r.map(q).join(',')).join('\n'));

const per = {};
items.forEach((it) => (per[it.host] = (per[it.host] || 0) + 1));
console.log('Produse citite:', per);
console.log(`Grupuri cross: ${cross.length}`);
const combos = {};
cross.forEach((g) => { const k = hostsOf(g).join(' + '); combos[k] = (combos[k] || 0) + 1; });
console.log(combos);
console.log('Scris în', OUT);
