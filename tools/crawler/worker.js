/**
 * Worker permanent pentru hainute.ro (Node + Chrome, rulează pe același server cu site-ul).
 *
 * 1. Reverificări LA CERERE: butonul „Reverifică disponibilitatea acum" de pe pagina
 *    produsului pune produsul în /recheck-queue; worker-ul îl ia în câteva secunde,
 *    rulează crawlerele pentru toate magazinele lui (proprii + cross) și raportează
 *    la /recheck-done → pagina se reîncarcă singură cu datele noi.
 * 2. Opțional, reîmprospătare PERIODICĂ (CYCLE_HOURS > 0): cross-urile neverificate
 *    de CYCLE_HOURS ore + produsele Answear scadente, apoi recalculul stocului.
 *
 * Rulare: node worker.js        (env: SITE, SECRET, POLL=10, CYCLE_HOURS=6)
 * Pe Linux, ca serviciu: vezi CRON.md (systemd).
 */
const { spawn } = require('child_process');
const path = require('path');

const SITE = process.env.SITE || 'http://hainutero.local';
const SECRET = process.env.SECRET || '';
const POLL = parseInt(process.env.POLL || '10', 10) * 1000;
const CYCLE_HOURS = parseFloat(process.env.CYCLE_HOURS || '0');
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const log = (...a) => console.log(new Date().toISOString().slice(0, 19).replace('T', ' '), ...a);

async function api(p, body) {
  const url = `${SITE}/wp-json/hainute/v1/${p}${p.includes('?') ? '&' : '?'}secret=${encodeURIComponent(SECRET)}`;
  const r = await fetch(url, body ? { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) } : {});
  if (!r.ok) throw new Error(`${p} HTTP ${r.status}`);
  return r.json();
}

/** Rulează un crawler ca proces separat; întoarce la ieșirea lui. */
function run(script, args, env, timeoutMs = 10 * 60 * 1000) {
  return new Promise((resolve) => {
    const p = spawn(process.execPath, [path.join(__dirname, script), ...args], { env: { ...process.env, SITE, SECRET, ...env }, stdio: ['ignore', 'pipe', 'pipe'] });
    let out = '';
    p.stdout.on('data', (d) => { out += d; });
    p.stderr.on('data', (d) => { out += d; });
    const t = setTimeout(() => p.kill(), timeoutMs);
    p.on('close', (code) => { clearTimeout(t); resolve({ code, out }); });
  });
}

// Lanul fiecărei surse: scriptul + parametrii pentru UN produs.
const LANES = {
  // Answear: mărimile + epuizatele din starea paginii, apoi variantele de culoare.
  answear: (id) => run('manual.js', [], { OWN: '1', IDS: String(id) }).then(() => run('manual.js', [], { VARIANTS: '1', IDS: String(id) })),
  sportisimo: (id) => run('sportisimo.js', [], { IDS: String(id), MAX: '5' }),
  fd: (id) => run('refresh.js', ['fd'], { IDS: String(id) }),
  vb: (id) => run('vb.js', [], { IDS: String(id) }),
  cross: (id) => run('manual.js', [], { IDS: String(id), DELAY: '1500', CONCURRENCY: '6' }),
};

async function recheck(item) {
  const t0 = Date.now();
  log(`reverific #${item.id} (${item.lanes.join(', ')})`);
  // Lanurile în paralel: sunt magazine diferite, deci nu „lovim" același site de două ori.
  await Promise.all(item.lanes.filter((l) => LANES[l]).map((l) => LANES[l](item.id).then((r) => {
    const last = r.out.trim().split('\n').filter((x) => /✓|✗|TERMINAT|\[\d+\/\d+\]/.test(x)).slice(-4).join(' | ');
    log(`  ${l}: ${last.slice(0, 220)}`);
  })));
  await api('recheck-done', { id: item.id });
  log(`  gata #${item.id} în ${Math.round((Date.now() - t0) / 1000)}s`);
}

let lastCycle = 0;
async function cycle() {
  log(`ciclu periodic (toate magazinele, la ${CYCLE_HOURS}h)`);
  // Magazinele proprii în paralel cu cross-urile (site-uri diferite).
  await Promise.all([
  run('manual.js', [], { OLDER: String(CYCLE_HOURS), DELAY: '3000', CONCURRENCY: '6' }, 4 * 3600 * 1000),
  run('manual.js', [], { OWN: '1', LIMIT: '5000', DELAY: '1500', CONCURRENCY: '3' }, 4 * 3600 * 1000)
  	.then(() => run('manual.js', [], { VARIANTS: '1', DELAY: '1500', CONCURRENCY: '3' }, 2 * 3600 * 1000)),
  run('sportisimo.js', [], {}, 3 * 3600 * 1000),
  run('refresh.js', ['fd'], {}, 3600 * 1000).then(() => run('vb.js', [], {}, 3600 * 1000)),
  ]);
  await api('recompute-buyable').catch(() => {});
  log('ciclu periodic gata');
}

(async () => {
  if (!SECRET) { console.error('Lipsește SECRET (HAINUTE_SYNC_SECRET).'); process.exit(1); }
  log(`worker pornit: ${SITE}, verific cererile la ${POLL / 1000}s${CYCLE_HOURS ? `, ciclu periodic la ${CYCLE_HOURS}h` : ''}`);
  for (;;) {
    try {
      const { queue } = await api('recheck-queue');
      for (const item of queue || []) await recheck(item);
      if (CYCLE_HOURS > 0 && Date.now() - lastCycle > CYCLE_HOURS * 3600 * 1000 && !(queue || []).length) {
        lastCycle = Date.now();
        cycle().catch((e) => log('ciclu: ' + e.message)); // în fundal: cererile la buton au prioritate
      }
    } catch (e) {
      log('eroare: ' + e.message);
    }
    await sleep(POLL);
  }
})();
