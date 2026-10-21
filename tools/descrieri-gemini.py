"""Scrie descrierile de produs cu Gemini (Google AI Studio), după content/prompt-descrieri.md.

  python tools/descrieri-gemini.py 9165 9191 ...        # scrie content/descrieri/{id}.json
  python tools/descrieri-gemini.py --model gemini-pro-latest 9165

Cheia API: variabila GEMINI_API_KEY sau fișierul ~/.gemini-api-key (NU în repo, repo-ul e public).
Înainte: content/surse/{id}.json (node tools/crawler/desc-extract.js --ids ...).
Pentru fiecare produs: Gemini scrie JSON-ul, `tools/descrieri.py check` îl verifică, iar dacă
are probleme, Gemini primește lista și corectează (max. 3 încercări). Rămâne ultima variantă,
chiar dacă nu e „OK”: se vede în ieșire și în content/raport-publicare.md după push.
"""
import io, json, os, re, subprocess, sys, time, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, 'content')
URL = 'https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent'


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return json.load(f)


def key():
    k = os.environ.get('GEMINI_API_KEY', '').strip()
    f = os.path.expanduser('~/.gemini-api-key')
    if not k and os.path.exists(f):
        k = io.open(f, encoding='utf-8').read().strip()
    if not k:
        sys.exit('Lipsește cheia: GEMINI_API_KEY sau ~/.gemini-api-key')
    return k


def gemini(model, contents):
    body = json.dumps({'contents': contents, 'generationConfig': {'temperature': 0.8, 'responseMimeType': 'application/json'}}).encode()
    for attempt in range(5):
        req = urllib.request.Request(URL.format(model), data=body, headers={'Content-Type': 'application/json', 'x-goog-api-key': key()})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                j = json.load(r)
            parts = j['candidates'][0]['content']['parts']
            return ''.join(p.get('text', '') for p in parts if not p.get('thought'))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and attempt < 4:  # limită de rată pe free tier: așteaptă
                time.sleep(30 * (attempt + 1))
                continue
            sys.exit(f'Gemini HTTP {e.code}: {e.read()[:400]!r}')
        except (TimeoutError, urllib.error.URLError) as e:  # răspuns lent / rețea: încă o dată
            if attempt == 4:
                sys.exit(f'Gemini nu răspunde: {e}')
            time.sleep(10)


def check(path):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'descrieri.py'), 'check', path],
                       capture_output=True, text=True, encoding='utf-8', env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def main():
    args = sys.argv[1:]
    model = 'gemini-flash-latest'
    if '--model' in args:
        i = args.index('--model')
        model = args[i + 1]
        del args[i:i + 2]
    ids = [int(a) for a in args if a.isdigit()]
    prompt = io.open(os.path.join(C, 'prompt-descrieri.md'), encoding='utf-8').read()
    reguli = io.open(os.path.join(C, 'reguli-descrieri.json'), encoding='utf-8').read()
    produse = {p['id']: p for p in load(os.path.join(C, 'produse.json'))}
    categorii = load(os.path.join(C, 'categorii.json'))
    versiune = load(os.path.join(C, 'reguli-descrieri.json')).get('versiune')
    # Exemplele: descrierile scrise de mână în versiunea curentă (doar textul, ca să nu copieze structura JSON-ului
    # altui produs). Mai multe exemple, de tipuri diferite, ca Gemini să nu imite unul singur.
    ex_ids = [8566, 14784, 10723]
    exemple = []
    for e in ex_ids:
        pe = os.path.join(C, 'descrieri', f'{e}.json')
        if os.path.exists(pe) and load(pe).get('versiune') == versiune:
            exemple.append((e, load(pe)['descriere_html']))
    cats = '\n'.join(f"{c.get('slug')} | {c.get('cale', c.get('nume', ''))}" for c in (categorii if isinstance(categorii, list) else categorii.values()))

    for pid in ids:
        sursa_p = os.path.join(C, 'surse', f'{pid}.json')
        if pid not in produse or not os.path.exists(sursa_p):
            print(f'#{pid}: lipsește din produse.json sau content/surse/{pid}.json, sar peste')
            continue
        sursa = io.open(sursa_p, encoding='utf-8').read()
        task = (
            f'{prompt}\n\n## Regulile verificării automate (content/reguli-descrieri.json)\n{reguli}\n\n'
            '## Exemple de text bun (alte produse). Arată nivelul cerut: fraze legate, listă introdusă logic, '
            'mărimi formulate natural. NU le copia frazele și nici ordinea: fiecare produs are alt fir logic, iar '
            'verificarea respinge formulările repetate între descrieri.\n'
            + ''.join(f'\n### {e}\n{h}\n' for e, h in exemple if e != pid) + '\n'
            f'## Categoriile existente (slug | cale)\n{cats}\n\n'
            f'## Produsul (din content/produse.json)\n{json.dumps(produse[pid], ensure_ascii=False, indent=1)}\n\n'
            f'## content/surse/{pid}.json (singura sursă de fapte; fragmentele se copiază EXACT de aici, caracter cu caracter)\n{sursa}\n\n'
            f'Scrie acum content/descrieri/{pid}.json. Răspunde DOAR cu obiectul JSON.'
        )
        contents = [{'role': 'user', 'parts': [{'text': task}]}]
        out = os.path.join(C, 'descrieri', f'{pid}.json')
        for attempt in range(1, 4):
            raw = gemini(model, contents)
            try:
                data = json.loads(re.sub(r'^```(?:json)?\s*|\s*```$', '', raw.strip()))
            except ValueError:
                contents += [{'role': 'model', 'parts': [{'text': raw}]}, {'role': 'user', 'parts': [{'text': 'Răspunsul nu e JSON valid. Trimite doar obiectul JSON.'}]}]
                continue
            data['id'], data['versiune'] = pid, load(os.path.join(C, 'reguli-descrieri.json')).get('versiune', data.get('versiune'))
            with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
                f.write('\n')
            ok, msg = check(out)
            print(f'#{pid} încercarea {attempt}: {"OK" if ok else "probleme"}')
            if ok:
                break
            print('   ' + msg.replace('\n', '\n   '))
            contents += [{'role': 'model', 'parts': [{'text': raw}]},
                         {'role': 'user', 'parts': [{'text': f'Verificarea automată (tools/descrieri.py check) a găsit:\n{msg}\n\nCorectează și trimite din nou tot JSON-ul. Nu inventa fapte; fragmentele se copiază exact din sursă.'}]}]


if __name__ == '__main__':
    main()
