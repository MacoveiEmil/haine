"""Unealta pentru descrierile de produs.

  python tools/descrieri.py check content/descrieri/8566.json [alt.json ...]
  python tools/descrieri.py check --all
  python tools/descrieri.py todo [--limit 20] [--stoc]     # produse fără descriere în versiunea curentă (câmpul "versiune")

Promptul curent: content/prompt-descrieri.md. Regulile verificării care se potrivesc
promptului: content/reguli-descrieri.json (se schimbă odată cu promptul, fără cod).
Regulile FIXE ale site-ului (mai jos, în cod) nu se pot ocoli: fără „compară”, preț,
stoc, nume de magazine sau liniuță lungă; fiecare fapt are fragment găsit pe pagina
magazinului (content/surse/{id}.json); linkuri doar spre categoria principală a
produsului, brandul lui și categorii care există.
Aceeași verificare rulează pe server înainte de publicare. Ieșire: 0 = toate OK.
"""
import html, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, 'content')

# --- Reguli FIXE (proprietar) ------------------------------------------------
MAIN_ANCHOR = {'fete': 'pentru fete', 'baieti': 'pentru băieți', 'bebe': 'pentru bebeluși', 'unisex': 'unisex'}
FIXED_BANNED = ['—', 'compar', 'reducere', 'ofert', 'promoți', 'cupon', 'ieftin', 'cel mai mic preț',
                ' preț', ' lei', 'stoc', 'magazinele care', 'answear', 'sportisimo', 'fashiondays',
                'fashion days', 'various-brands', 'zalando', 'about you', 'modivo', 'epantofi']
GENDERED = ['fetița', 'băiatul', 'cea mică']

# --- Reguli ajustabile (implicit v4; suprascrise de content/reguli-descrieri.json) ----
DEFAULT_RULES = {'versiune': 'v4', 'cuvinte_min': 170, 'cuvinte_max': 240, 'date_insuficiente_cuvinte_min': 60,
                 'paragraf1_min': 40, 'paragraf1_max': 60, 'lista_min': 4, 'lista_max': 7,
                 'lista_ultimul_punct': 'Potrivit pentru', 'paragraf_final_max_propozitii': 2,
                 'linkuri_total': 3, 'link_categorie_complementara': True, 'fapte_min': 3,
                 'cere_orientativ': True, 'gen_neutru': True, 'interzise_extra': [],
                 # v5: link_categorie_complementara poate fi "optional" (cel mult unul);
                 # linkuri_min/linkuri_max înlocuiesc linkuri_total când sunt date.
                 'linkuri_min': None, 'linkuri_max': None, 'link_categorie_in_paragraf1': False,
                 'orientativ_o_data': False,
                 # v6: conținut obligatoriu (brand, model, culoare, mărimi) + listă introdusă de o frază
                 # + formulări repetate între descrieri (n-grame de cuvinte din paragrafe).
                 'entitati': False, 'lista_cere_introducere': False,
                 'repetitie_ngram': 0, 'repetitie_min_descrieri': 4, 'repetitie_procent': 10,
                 # v7: vârsta e aproximativă, dar spusă în mai multe feluri (nu mereu „orientativ”);
                 # formulările repetate se caută și în descrierile versiunilor date aici.
                 'varsta_formulari': [], 'repetitie_versiuni': None}

# Culoarea din titlu → formele acceptate în text (rădăcini, fără diacritice obligatorii).
CULORI = {'bleumarin': ['bleumarin'], 'roz': ['roz'], 'negru': ['negr', 'neagr'], 'bej': ['bej'],
          'maro': ['maro'], 'alb': ['alb'], 'verde': ['verd', 'verzi'], 'violet': ['violet', 'mov'],
          'gri': ['gri'], 'rosu': ['roș', 'roşu', 'rosu', 'roși', 'roșii'], 'albastru': ['albastr'],
          'portocaliu': ['portocal'], 'multicolor': ['multicolor', 'colorat'], 'galben': ['galben'],
          'bordo': ['bordo'], 'argintiu': ['argint'], 'turcoaz': ['turcoaz'], 'mov': ['mov', 'violet'],
          'auriu': ['auri'], 'kaki': ['kaki'], 'crem': ['crem'], 'bleu': ['bleu']}
TITLU_GENERIC = {'FETE', 'BĂIEȚI', 'BAIETI', 'UNISEX', 'BEBE', 'JACKET', 'KIDS', 'JR', 'GORE', 'TEX'}


def entitati(p, text):
    """Ce trebuie să apară în text, scos din produse.json: brand, model, culoare, mărimi."""
    low, issues = text.lower(), []
    if p.get('brand') and p['brand'].lower() not in low:
        issues.append('lipsește brandul: ' + p['brand'])
    brand_w = {w.upper() for w in re.split(r'\W+', p.get('brand') or '') if w}
    model = [w for w in re.findall(r'[A-ZĂÂÎȘȚ0-9][A-ZĂÂÎȘȚ0-9-]{2,}', p.get('titlu', ''))
             if w not in brand_w and w not in TITLU_GENERIC and not w.isdigit()]
    if model and not any(w.lower() in low for w in model):
        issues.append('lipsește modelul din titlu: ' + ' '.join(model))
    last = (p.get('titlu') or '').split()[-1:] or ['']
    forms = CULORI.get(last[0].lower().replace('ș', 's').replace('ş', 's'))
    if forms and not any(f in low for f in forms):
        issues.append('lipsește culoarea din titlu: ' + last[0])
    m = [str(x) for x in p.get('marimi') or []]
    if m:
        for x in {m[0], m[-1]}:
            if not re.search(r'(?<!\d)' + re.escape(x) + r'(?!\d)', text):
                issues.append(f'lipsesc mărimile de pe site (cea mai mică și cea mai mare): {m[0]} și {m[-1]}')
                break
    return issues


def ngrame(h, n):
    words = re.findall(r'[a-zăâîșțşţ]+', text_of(' '.join(re.findall(r'<p>(.*?)</p>', h, re.S))).lower())
    return {' '.join(words[i:i + n]) for i in range(len(words) - n + 1)}


_CORPUS = None


def corpus(R):
    """n-gramele fiecărei descrieri din versiunea curentă (pentru formulările repetate)."""
    global _CORPUS
    if _CORPUS is None:
        _CORPUS = {}
        d = os.path.join(C, 'descrieri')
        for f in os.listdir(d) if os.path.isdir(d) else []:
            if f.endswith('.json'):
                try:
                    x = load(os.path.join(d, f))
                except ValueError:
                    continue
                if x.get('versiune', 'v4') in (R['repetitie_versiuni'] or [R['versiune']]):
                    _CORPUS[int(f[:-5])] = ngrame(x.get('descriere_html', ''), R['repetitie_ngram'])
    return _CORPUS


def load(p):
    with io.open(p, encoding='utf-8') as f:
        return json.load(f)


def rules():
    r = dict(DEFAULT_RULES)
    f = os.path.join(C, 'reguli-descrieri.json')
    if os.path.exists(f):
        r.update({k: v for k, v in load(f).items() if not k.startswith('_')})
    return r


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('\\n', ' ').replace('<br />', ' ')).lower()


def text_of(h):
    return html.unescape(re.sub(r'<[^>]+>', ' ', h))


def check(path, produse, categorii, R):
    x = load(path)
    pid = int(x.get('id', 0))
    issues = []
    if str(pid) != os.path.splitext(os.path.basename(path))[0]:
        issues.append('id-ul din fișier nu corespunde numelui fișierului')
    p = produse.get(pid)
    if not p:
        return pid, 0, ['produsul nu există (sau nu e publicat) în content/produse.json']
    h = x.get('descriere_html', '')
    low = text_of(h).lower()
    words = len(text_of(h).split())
    paras = re.findall(r'<p>(.*?)</p>', h, re.S)
    items = re.findall(r'<li>.*?</li>', h, re.S)
    insuf = bool(x.get('date_insuficiente'))

    # Reguli fixe
    for b in FIXED_BANNED:
        if b in low: issues.append('interzis pe site: ' + b.strip())
    if re.search(r'[!?]', text_of(h)): issues.append('fără exclamații sau întrebări')
    links = re.findall(r'<a href="([^"]+)">([^<]+)</a>', h)
    if re.search(r'<a\s(?![^>]*href="/(categorie|brand)/)', h): issues.append('doar linkuri interne spre /categorie/ sau /brand/')
    # Linkul de categorie al produsului: categoria lui frunză (ex. /categorie/adidasi/) sau cea principală.
    own = {u for u in (p.get('categorie_frunza'), p['categorie_principala']) if u}
    want = p.get('categorie_frunza') or p['categorie_principala']
    mains = [l for l in links if l[0] in own]
    if len(mains) != 1:
        issues.append(f'linkul spre categoria produsului {want} lipsește sau apare de mai multe ori')
    elif MAIN_ANCHOR.get(p.get('gen')) and MAIN_ANCHOR[p['gen']] not in html.unescape(mains[0][1]):
        issues.append(f'ancora categoriei principale trebuie să conțină „{MAIN_ANCHOR[p["gen"]]}”')
    if p['brand_slug'] and not any(l[0] == p['brand_slug'] for l in links): issues.append('lipsește linkul de brand ' + p['brand_slug'])
    for u, _ in links:
        if u.startswith('/categorie/') and u not in categorii: issues.append('link spre categorie inexistentă: ' + u)
        if u.startswith('/brand/') and u != p['brand_slug']: issues.append('link spre alt brand: ' + u)
    src = os.path.join(C, 'surse', f'{pid}.json')
    surse = x.get('surse') or []
    if not os.path.exists(src):
        issues.append('lipsește extracția paginii: content/surse/%d.json (tools/crawler/desc-extract.js)' % pid)
    else:
        page = norm(json.dumps(load(src), ensure_ascii=False))
        miss = [s.get('fragment', '') for s in surse if not s.get('fragment') or norm(s['fragment']) not in page]
        if miss: issues.append('fragmente care NU apar pe pagina magazinului: ' + ' | '.join(m or '(gol)' for m in miss[:5]))
    if not surse: issues.append('lipsesc sursele faptelor („surse”)')

    # Reguli ajustabile (content/reguli-descrieri.json)
    for b in R['interzise_extra']:
        if b.lower() in low: issues.append('formulă interzisă: ' + b.strip())
    if R['gen_neutru']:
        for g in GENDERED:
            if g in low: issues.append('textul trebuie să fie neutru ca gen: ' + g)
    lo = R['date_insuficiente_cuvinte_min'] if insuf else R['cuvinte_min']
    if not lo <= words <= R['cuvinte_max']: issues.append(f'lungime {words} cuvinte (trebuie {lo}-{R["cuvinte_max"]})')
    if not insuf and R['lista_max']:
        if not R['lista_min'] <= len(items) <= R['lista_max']: issues.append(f'lista are {len(items)} puncte (trebuie {R["lista_min"]}-{R["lista_max"]})')
        elif R['lista_ultimul_punct'] and R['lista_ultimul_punct'] not in items[-1]: issues.append(f'ultimul punct al listei nu e „{R["lista_ultimul_punct"]}”')
    if paras:
        p1 = len(text_of(paras[0]).split())
        if not R['paragraf1_min'] <= p1 <= R['paragraf1_max']: issues.append(f'paragraful 1 are {p1} cuvinte ({R["paragraf1_min"]}-{R["paragraf1_max"]})')
        if R['paragraf_final_max_propozitii'] and len(re.findall(r'[.]\s', text_of(paras[-1]) + ' ')) > R['paragraf_final_max_propozitii']:
            issues.append(f'ultimul paragraf are peste {R["paragraf_final_max_propozitii"]} propoziții')
    if R['cere_orientativ'] and 'orientativ' not in low: issues.append('lipsește „orientativ” la vârstă')
    if R['varsta_formulari']:
        if not re.search(r'\b(ani|an|luni)\b', low):
            issues.append('lipsește vârsta (din mărimi, vezi Anexa)')
        elif not re.search(r'\b(' + '|'.join(re.escape(f) for f in R['varsta_formulari']) + r')\b', low):
            issues.append('vârsta trebuie spusă aproximativ, de ex.: ' + ', '.join(R['varsta_formulari'][:5]))
    if R['linkuri_min'] is not None or R['linkuri_max'] is not None:
        lo_l, hi_l = R['linkuri_min'] or 0, R['linkuri_max'] or 99
        if not lo_l <= len(links) <= hi_l: issues.append(f'{len(links)} linkuri (trebuie {lo_l}-{hi_l})')
    elif R['linkuri_total'] and len(links) != R['linkuri_total']: issues.append(f'{len(links)} linkuri (trebuie {R["linkuri_total"]})')
    comp = [l for l in links if l[0].startswith('/categorie/') and l[0] not in own]
    if R['link_categorie_complementara'] == 'optional':
        if len(comp) > 1: issues.append('cel mult un link spre o categorie complementară')
    elif R['link_categorie_complementara'] and len(comp) != 1:
        issues.append('trebuie exact un link spre o categorie complementară')
    if R['link_categorie_in_paragraf1'] and paras and not any(f'href="{u}"' in paras[0] for u in own):
        issues.append('linkul spre categoria produsului trebuie să fie în paragraful 1')
    if R['orientativ_o_data'] and low.count('orientativ') > 1: issues.append('vârsta („orientativ”) apare de mai multe ori')
    if R['entitati']:
        issues += entitati(p, text_of(h))
    if R['lista_cere_introducere'] and '<ul>' in h:
        before = text_of(h.split('<ul>')[0]).strip()
        if not before.endswith(':'):
            issues.append('lista trebuie introdusă de o frază care o leagă de text și se termină cu „:”')
    if R['repetitie_ngram']:
        corp = corpus(R)
        others = {k: v for k, v in corp.items() if k != pid}
        prag = max(R['repetitie_min_descrieri'], len(others) * R['repetitie_procent'] / 100)
        rep_ = []
        for g in sorted(ngrame(h, R['repetitie_ngram'])):
            k = sum(g in v for v in others.values())
            if k + 1 >= prag:
                rep_.append(f'„{g}” ({k + 1} descrieri)')
        if rep_:
            issues.append('formulări repetate în alte descrieri (cifrele sunt scoase), scrie altfel: ' + '; '.join(rep_[:4]))
    if x.get('versiune', 'v4') != R['versiune']: issues.append(f'descriere {x.get("versiune", "v4")}, promptul curent e {R["versiune"]} („versiune” în fișier)')
    if len(surse) < R['fapte_min'] and not insuf: issues.append(f'sub {R["fapte_min"]} fapte cu sursă: marchează "date_insuficiente": true')
    return pid, words, issues


def main(a):
    produse = {int(p['id']): p for p in load(os.path.join(C, 'produse.json'))}
    categorii = {c['slug'] for c in load(os.path.join(C, 'categorii.json'))}
    R = rules()
    if a and a[0] == 'todo':
        lim = int(a[a.index('--limit') + 1]) if '--limit' in a else 20
        d = os.path.join(C, 'descrieri')
        # Gata = există fișier scris în versiunea curentă (câmpul "versiune"; fișierele fără el sunt v4).
        done = set()
        for f in (os.listdir(d) if os.path.isdir(d) else []):
            if f.endswith('.json'):
                try:
                    if load(os.path.join(d, f)).get('versiune', 'v4') == R['versiune']: done.add(int(f[:-5]))
                except (ValueError, OSError):
                    pass
        todo = [p for p in produse.values() if p['descriere_versiune'] != R['versiune'] and p['id'] not in done and (p['cu_stoc'] or '--stoc' not in a)]
        for p in todo[:lim]:
            print(p['id'], p['link_afiliat'], '|', p['titlu'])
        print(f'# {len(todo)} produse fără descriere {R["versiune"]}', file=sys.stderr)
        return 0
    if a and a[0] == 'check':
        files = a[1:]
        if files == ['--all']:
            d = os.path.join(C, 'descrieri')
            files = [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith('.json')]
        bad = 0
        for f in files:
            try:
                pid, words, issues = check(f, produse, categorii, R)
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
