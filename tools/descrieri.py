"""Unealta pentru descrierile de produs (prompt v4: docs/prompt-descrieri-v4.md).

  python tools/descrieri.py check content/descrieri/8566.json [alt.json ...]
  python tools/descrieri.py check --all
  python tools/descrieri.py todo [--limit 20] [--stoc]     # produse fără descriere v4

Fiecare descriere (content/descrieri/{id}.json) trebuie să aibă alături extracția
paginii magazinului pe care se bazează (content/surse/{id}.json, făcută cu
tools/crawler/desc-extract.js). Verificarea: fiecare fragment din „surse” există
pe pagina magazinului, lungimi, listă 4-7 puncte, cuvinte interzise, gen neutru,
exact 3 linkuri (categoria principală cu „pentru”, brandul, o categorie existentă).
Aceeași verificare rulează pe server înainte de publicare: ce nu trece nu se publică.
Ieșire: cod 0 dacă toate sunt OK, 1 altfel.
"""
import html, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, 'content')
MAIN = {'/categorie/incaltaminte-baieti/': 'pentru băieți', '/categorie/incaltaminte-fete/': 'pentru fete',
        '/categorie/imbracaminte-baieti/': 'pentru băieți', '/categorie/imbracaminte-fete/': 'pentru fete',
        '/categorie/imbracaminte-bebe/': 'pentru bebeluși', '/categorie/incaltaminte-bebe/': 'pentru bebeluși',
        '/categorie/incaltaminte-unisex/': 'unisex', '/categorie/imbracaminte-unisex/': 'unisex',
        '/categorie/accesorii-baieti/': 'pentru băieți', '/categorie/accesorii-fete/': 'pentru fete',
        '/categorie/accesorii-unisex/': 'unisex'}
BANNED = ['—', '!', '?', 'cel mai bun', 'perfect', 'ideal', 'extraordinar', 'premium', 'must-have', 'revoluționar',
          'în concluzie', 'așadar', 'în plus,', 'de asemenea', 'compar', 'reducere', 'ofert', 'intră în gama',
          'face parte din', 'se încadrează', 'aparține', 'secțiunea', 'confort și stil', 'nu va dezamăgi', 'ore în șir',
          'fără să limiteze', 'se asortează', 'nu stau locului', 'respiră', 'aerul circulă', 'aderență', 'amortiz',
          'moale la fiecare pas', 'fără presiune', 'stabilitate', 'ortopedic', 'susține piciorul', 'verificabil pe eticheta',
          'recunosc imediat', 'face diferența', 'se simte', 'fetița', 'băiatul', 'cea mică', ' preț', ' lei', 'stoc',
          'magazinele care', 'answear', 'sportisimo', 'fashiondays', 'fashion days', 'various-brands']


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return json.load(f)


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('\\n', ' ').replace('<br />', ' ')).lower()


def text_of(h):
    return html.unescape(re.sub(r'<[^>]+>', ' ', h))


def check(path, produse, categorii):
    x = load(path)
    pid = int(x.get('id', 0))
    issues = []
    if str(pid) != os.path.splitext(os.path.basename(path))[0]:
        issues.append('id-ul din fișier nu corespunde numelui fișierului')
    p = produse.get(pid)
    if not p:
        return pid, 0, ['produsul nu există (sau nu e publicat) în content/produse.json']
    h = x.get('descriere_html', '')
    words = len(text_of(h).split())
    low = text_of(h).lower()
    paras = re.findall(r'<p>(.*?)</p>', h, re.S)
    items = re.findall(r'<li>.*?</li>', h, re.S)
    if x.get('date_insuficiente'):
        if not 60 <= words <= 240: issues.append(f'lungime {words} cuvinte (date insuficiente: 60-240)')
    else:
        if not 170 <= words <= 240: issues.append(f'lungime {words} cuvinte (trebuie 170-240)')
        if not 4 <= len(items) <= 7: issues.append(f'lista are {len(items)} puncte (trebuie 4-7)')
        elif 'Potrivit pentru' not in items[-1]: issues.append('ultimul punct al listei nu e „Potrivit pentru”')
    if paras:
        p1 = len(text_of(paras[0]).split())
        if not 40 <= p1 <= 60: issues.append(f'paragraful 1 are {p1} cuvinte (40-60)')
        if len(re.findall(r'[.]\s', text_of(paras[-1]) + ' ')) > 2: issues.append('paragraful de mărimi are peste 2 propoziții')
    for b in BANNED:
        if b in low: issues.append('cuvânt/formulă interzisă: ' + b.strip())
    if 'orientativ' not in low: issues.append('lipsește „orientativ” la vârstă')
    links = re.findall(r'<a href="([^"]+)">([^<]+)</a>', h)
    want = p['categorie_principala']
    mains = [l for l in links if l[0] == want]
    if len(mains) != 1: issues.append(f'linkul spre categoria principală {want} lipsește sau e de mai multe ori')
    elif MAIN.get(want) and MAIN[want] not in html.unescape(mains[0][1]): issues.append(f'ancora categoriei principale trebuie să conțină „{MAIN[want]}”')
    if p['brand_slug'] and not any(l[0] == p['brand_slug'] for l in links): issues.append('lipsește linkul de brand ' + p['brand_slug'])
    comp = [l for l in links if l[0].startswith('/categorie/') and l[0] != want]
    if len(comp) != 1: issues.append('trebuie exact un link spre o categorie complementară')
    elif comp[0][0] not in categorii: issues.append('categoria complementară nu există: ' + comp[0][0])
    if len(links) != 3: issues.append(f'{len(links)} linkuri (trebuie exact 3)')
    src = os.path.join(C, 'surse', f'{pid}.json')
    if not os.path.exists(src):
        issues.append('lipsește extracția paginii: content/surse/%d.json (tools/crawler/desc-extract.js)' % pid)
    else:
        page = norm(json.dumps(load(src), ensure_ascii=False))
        surse = x.get('surse') or []
        if len(surse) < 3 and not x.get('date_insuficiente'): issues.append('sub 3 fapte cu sursă: marchează "date_insuficiente": true')
        miss = [s.get('fragment', '') for s in surse if norm(s.get('fragment', '')) not in page]
        if miss: issues.append('fragmente care NU apar pe pagina magazinului: ' + ' | '.join(miss[:5]))
    return pid, words, issues


def main(a):
    produse = {int(p['id']): p for p in load(os.path.join(C, 'produse.json'))}
    categorii = {c['slug'] for c in load(os.path.join(C, 'categorii.json'))}
    if a and a[0] == 'todo':
        lim = int(a[a.index('--limit') + 1]) if '--limit' in a else 20
        done = {int(f[:-5]) for f in os.listdir(os.path.join(C, 'descrieri')) if f.endswith('.json')} if os.path.isdir(os.path.join(C, 'descrieri')) else set()
        todo = [p for p in produse.values() if p['descriere_versiune'] != 'v4' and p['id'] not in done and (p['cu_stoc'] or '--stoc' not in a)]
        for p in todo[:lim]:
            print(p['id'], p['link_afiliat'], '|', p['titlu'])
        print(f'# {len(todo)} produse fără descriere v4', file=sys.stderr)
        return 0
    if a and a[0] == 'check':
        files = a[1:]
        if files == ['--all']:
            d = os.path.join(C, 'descrieri')
            files = [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith('.json')]
        bad = 0
        for f in files:
            try:
                pid, words, issues = check(f, produse, categorii)
            except Exception as e:  # JSON invalid etc.
                pid, words, issues = os.path.basename(f), 0, ['fișier invalid: %s' % e]
            print(pid, f'{words} cuv |', 'OK' if not issues else '; '.join(issues))
            bad += bool(issues)
        return 1 if bad else 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main(sys.argv[1:]))
