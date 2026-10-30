/**
 * Alege din rezultatele Lens (brand-<slug>-lens.csv) potrivirile bune și le bifează.
 * Reguli: doar magazine .ro; un singur rând per magazin pentru un produs; maxim 3 rânduri / produs;
 * ordinea = potrivirea de poză (poziția în Google Lens) + potrivirea de titlu (brandul în titlu/URL,
 * cuvinte comune cu produsul nostru). Aceeași pagină de magazin nu merge la 2 produse diferite
 * (afară de produsele din același grup cross, care sunt de fapt același produs).
 * NU scrie nimic în site.
 *
 * Rulare: BRAND="en fant" node brand-pick.js   (env: MAX=3, OUT)
 */
const fs = require('fs');
const path = require('path');

const BRAND = (process.env.BRAND || 'en fant').trim();
const SLUG = BRAND.toLowerCase().replace(/\s+/g, '-');
const MAX = parseInt(process.env.MAX || '3', 10);
const LENS = path.join(__dirname, `brand-${SLUG}-lens.csv`);
const PROD = path.join(__dirname, `brand-${SLUG}-produse.csv`);
const OUT = process.env.OUT || path.join(__dirname, `brand-${SLUG}-lens-bifat.csv`);

function readCsv(file) {
  const t = fs.readFileSync(file, 'utf8').replace(/^﻿/, '');
  const rows = []; let row = [], cell = '', q = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (q) { if (c === '"') { if (t[i + 1] === '"') { cell += '"'; i++; } else q = false; } else cell += c; }
    else if (c === '"') q = true;
    else if (c === ',') { row.push(cell); cell = ''; }
    else if (c === '\n' || c === '\r') { if (c === '\r' && t[i + 1] === '\n') i++; row.push(cell); cell = ''; if (row.some((x) => x !== '')) rows.push(row); row = []; }
    else cell += c;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  const head = rows.shift();
  return rows.map((r) => Object.fromEntries(head.map((h, i) => [h, r[i] || ''])));
}
const q = (s) => `"${String(s ?? '').replace(/"/g, '""')}"`;

const norm = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();
const STOP = new Set(['cu', 'de', 'pentru', 'copii', 'copil', 'din', 'si', 'la', 'in', 'pe', 'the', 'for', 'kids', 'baby', 'en', 'fant', 'enfant', 'ro', 'by', 'a', 'o', 'un', 'sau']);
const tokens = (s) => [...new Set(norm(s).split(' ').filter((w) => w.length >= 3 && !STOP.has(w) && !/^\d+$/.test(w)))];
// stem simplu: „manusi"/„manusa", „cizme"/„cizma" etc. se potrivesc pe primele 5 litere
const stem = (w) => w.slice(0, 5);

// grupuri de culori RO/EN: „green" ≈ „verde", „sand" ≈ „bej" etc.
const COLOR_GROUPS = [
  ['verde', 'green', 'ivy', 'oliv', 'olive', 'kaki', 'khaki', 'mint', 'sage', 'kambaba', 'ivy'],
  ['albastru', 'blue', 'bleumarin', 'navy', 'indigo', 'slate', 'denim', 'ocean', 'midnight', 'night', 'turcoaz', 'teal'],
  ['roz', 'rose', 'pink', 'blush', 'corai', 'coral', 'old', 'mauve', 'pastel'],
  ['gri', 'grey', 'gray', 'shadow', 'ash', 'melange', 'antracit', 'charcoal'],
  ['negru', 'black', 'ebony'],
  ['alb', 'white', 'egret', 'cream', 'crem', 'ivory', 'ecru', 'snow'],
  ['maro', 'brown', 'coffee', 'bean', 'chocolate', 'cognac', 'coniac', 'portabella', 'bark', 'leather', 'taupe', 'chestnut', 'acorn', 'tan'],
  ['bej', 'beige', 'sand', 'sandshell', 'nisipiu', 'camel', 'oat', 'natural'],
  ['rosu', 'red', 'henna', 'burgundy', 'bordo', 'wine', 'cherry', 'poppy'],
  ['galben', 'yellow', 'mustard', 'mustar', 'lemon', 'sun'],
  ['mov', 'purple', 'lilac', 'liliachiu', 'lavender', 'violet', 'plum', 'mesa'],
  ['portocaliu', 'orange', 'rust', 'terracotta', 'caramel'],
];
const colorGroup = (w) => { const i = COLOR_GROUPS.findIndex((g) => g.includes(w)); return i < 0 ? null : 'c' + i; };
const colorKeys = (arr) => new Set(arr.flatMap((w) => [w, colorGroup(w)]).filter(Boolean));

const prods = readCsv(PROD);
const byId = Object.fromEntries(prods.map((p) => [p.id, p]));
const lens = readCsv(LENS);

const isRo = (host) => /\.ro$/i.test(host);
// paginile de catalog / brand / căutare nu sunt produse; URL-ul se curăță de parametri (cupoane etc.)
const notProduct = (u) => /\/(catalog|brand|marca|marci|collections?|search|cauta|cautare|c|categorie)\//i.test(u.replace(/^https?:\/\/[^/]+/, '')) || /[?&](q|search|s)=/i.test(u);
const clean = (u) => u.split('?')[0].split('#')[0];
const hasBrand = (m) => /\ben[ -]?fant\b/.test(norm(m.titlu) + ' ' + norm(decodeURIComponent(m.url_produs).replace(/[-_/]/g, ' ')));

const cands = [];
for (const m of lens) {
  const p = byId[m.id];
  if (!p || !isRo(m.site) || m.site.endsWith(p.magazin) || notProduct(m.url_produs)) continue;
  const srcTok = tokens(`${p.titlu} ${p.culoare}`.replace(new RegExp(BRAND.replace(/\s+/g, '\\s*'), 'ig'), ' '));
  const mTok = tokens(`${m.titlu} ${decodeURIComponent(m.url_produs).replace(/[-_/.]/g, ' ')}`);
  const mStems = new Set(mTok.map(stem));
  const common = srcTok.filter((w) => mStems.has(stem(w)));
  const brand = hasBrand(m);
  // culoarea produsului nostru: coloana culoare + ultimele cuvinte din titlu (4kidspoint / Zalando pun culoarea la coada titlului)
  const titleTok = tokens(p.titlu.replace(new RegExp(BRAND.replace(/s+/g, '\s*'), 'ig'), ' '));
  const srcColors = colorKeys([...tokens(p.culoare), ...titleTok.slice(-2)]);
  const hasSrcColor = [...srcColors].some((k) => /^cd+$/.test(k)) || tokens(p.culoare).length > 0 || titleTok.slice(-2).length > 0;
  const mColors = colorKeys(mTok);
  const colorOk = [...srcColors].some((k) => mColors.has(k));
  const poz = parseInt(m.pozitie, 10) || 99;
  const score = Math.max(0, 25 - poz) + (brand ? 30 : 0) + Math.min(common.length, 4) * 6 + (colorOk ? 15 : 0);
  // acceptăm doar dacă titlul/URL-ul confirmă brandul (altfel sunt produse doar asemănătoare vizual)
  if (!brand) continue;
  // variantă de altă culoare: o păstrăm doar dacă poza e chiar printre primele 2 rezultate Google
  if (hasSrcColor && !colorOk && poz > 2) continue;
  cands.push({ ...m, p, score, brand, common, poz, colorOk });
}

// perechile cross confirmate prin EAN (din brand-cross.js) intră direct, înaintea potrivirilor de poză
for (const p of prods) {
  if (!p.grup_cross || !/^sigur/.test(p.potrivire)) continue;
  for (const o of prods) {
    if (o === p || o.grup_cross !== p.grup_cross || o.magazin === p.magazin) continue;
    cands.push({ id: p.id, site: o.magazin, url_produs: o.url, titlu: o.titlu, pozitie: '', in_stoc: o['mărimi pe stoc'] ? '1' : '', poza_gasita: o.poza, p, score: 100, brand: true, common: [], poz: 0, colorOk: true, ean: true });
  }
}
cands.sort((a, b) => b.score - a.score || a.poz - b.poz);
const chosen = {}; // id -> [cand]
const urlOwner = new Map(); // url -> cheie (grup cross sau id)
for (const c of cands) {
  const list = (chosen[c.id] = chosen[c.id] || []);
  const key = c.p.grup_cross ? 'g' + c.p.grup_cross : c.id;
  const url = clean(c.url_produs);
  if (list.length >= MAX || list.some((x) => x.site === c.site)) continue;
  if (urlOwner.has(url) && urlOwner.get(url) !== key) continue;
  urlOwner.set(url, key);
  list.push(c);
}

const head = ['id', 'magazin_sursa', 'titlu_sursa', 'grup_cross', 'site', 'url_produs', 'titlu_gasit', 'pozitie_poza', 'scor', 'motiv', 'in_stoc', 'poza_mea', 'poza_gasita', 'bifa'];
const lines = [];
let withMatch = 0, rows = 0;
for (const p of prods) {
  const list = chosen[p.id] || [];
  if (!list.length) { lines.push([p.id, p.magazin, p.titlu, p.grup_cross, '', '', '(nicio potrivire .ro)', '', '', '', '', p.poza, '', '']); continue; }
  withMatch++;
  list.forEach((c) => {
    rows++;
    const motiv = c.ean ? 'cross: același cod de bare (EAN)' : [`poza #${c.poz}`, c.brand ? 'brand în titlu/URL' : '', c.colorOk ? 'culoare potrivită' : '', c.common.length ? 'cuvinte comune: ' + c.common.slice(0, 4).join(' ') : ''].filter(Boolean).join('; ');
    lines.push([p.id, p.magazin, p.titlu, p.grup_cross, c.site, clean(c.url_produs), c.titlu, c.ean ? '' : c.poz, c.score, motiv, c.in_stoc, p.poza, c.poza_gasita, 'da']);
  });
}
fs.writeFileSync(OUT, '﻿' + [head, ...lines].map((r) => r.map(q).join(',')).join('\n'));

const per = {};
Object.values(chosen).forEach((l) => l.forEach((c) => (per[c.site] = (per[c.site] || 0) + 1)));
console.log(`Produse: ${prods.length}; cu cel puțin o potrivire .ro: ${withMatch}; rânduri bifate: ${rows}`);
console.log('Pe magazin:', Object.entries(per).sort((a, b) => b[1] - a[1]).map(([h, n]) => `${h} ${n}`).join(' | '));
console.log('Scris în', OUT);
