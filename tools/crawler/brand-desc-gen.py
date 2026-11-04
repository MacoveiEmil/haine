#!/usr/bin/env python3
"""
Scrie descrierile (promptul v7) pentru drafturile de brand din FAPTELE extrase de pe paginile magazinelor
(brand-surse/*.json, de la brand-desc-extract.js). Fiecare propoziție cu un fapt își are fragmentul copiat
exact din pagină (verificat apoi de brand-desc-check.py, aceeași verificare ca pe server).
Textul variază de la un produs la altul (formulările se aleg după cheia produsului), iar faptele care
lipsesc nu se inventează: sub 3 fapte, descrierea e scurtă („date insuficiente").

Rulare: python tools/crawler/brand-desc-gen.py   → brand-desc-src/auto.json
        python tools/crawler/brand-desc-check.py → verifică și scrie brand-drafts-desc.json
"""
import hashlib, json, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
drafts = json.load(open(os.path.join(HERE, 'brand-drafts-build.json'), encoding='utf-8'))


def rnd(key, slot, n):
    return int(hashlib.md5((key + slot).encode()).hexdigest(), 16) % n


def pick(key, slot, options):
    return options[rnd(key, slot, len(options))]


# ------------------------------------------------------------------ gramatică
LEX = {  # primul cuvânt al tipului → (articol, plural?)
    'bluză': ('o', 0), 'jachetă': ('o', 0), 'geacă': ('o', 0), 'salopetă': ('o', 0), 'căciulă': ('o', 0), 'rochie': ('o', 0), 'fustă': ('o', 0),
    'cravată': ('o', 0), 'vestă': ('o', 0), 'pălărie': ('o', 0), 'cagulă': ('o', 0), 'pijama': ('o', 0), 'mănușă': ('o', 0),
    'body': ('un', 0), 'trening': ('un', 0), 'halat': ('un', 0), 'tricou': ('un', 0), 'hanorac': ('un', 0), 'pulover': ('un', 0),
    'cardigan': ('un', 0), 'costum': ('un', 0), 'fular': ('un', 0), 'top': ('un', 0), 'set': ('un', 0), 'maiou': ('un', 0), 'palton': ('un', 0),
    'pijamale': ('niște', 1), 'șosete': ('niște', 1), 'papuci': ('niște', 1), 'cizme': ('niște', 1), 'adidași': ('niște', 1), 'pantofi': ('niște', 1),
    'pantaloni': ('niște', 1), 'sandale': ('niște', 1), 'mănuși': ('niște', 1), 'botoșei': ('niște', 1), 'botoși': ('niște', 1), 'saboți': ('niște', 1),
    'saboţi': ('niște', 1), 'chiloți': ('niște', 1), 'chiloţi': ('niște', 1), 'bocanci': ('niște', 1), 'leggings': ('niște', 1), 'jeans': ('niște', 1),
}
AGE_CLOTH = [(62, 'câteva luni'), (68, '6 luni'), (74, '9 luni'), (80, '12 luni'), (86, '18 luni'), (92, '2 ani'), (98, '3 ani'), (104, '4 ani'), (110, '5 ani'), (116, '6 ani'),
             (122, '7 ani'), (128, '8 ani'), (134, '9 ani'), (140, '10 ani'), (146, '11 ani'), (152, '12 ani'), (158, '13 ani'), (164, '14 ani'), (170, '15 ani'), (176, '16 ani')]
AGE_SHOE = [(19, '1 an'), (23, '2 ani'), (26, '3 ani'), (28, '4 ani'), (30, '6 ani'), (32, '8 ani'), (34, '10 ani'), (36, '12 ani')]


def age_from_units(sizes):
    """Marimi de tip 6-12M, 1-2Y, 2-4 ani, 6-12 luni -> (a, b) in luni/ani, sau None."""
    mo = []
    for s_ in sizes:
        m = re.match(r'^(\d+)(?:\s*-\s*(\d+))?\s*(M|luni|Y|ani|an)$', str(s_).strip(), re.I)
        if not m:
            return None
        k = 1 if m.group(3).lower() in ('m', 'luni') else 12
        mo += [int(m.group(1)) * k] + ([int(m.group(2)) * k] if m.group(2) else [])
    if not mo:
        return None

    def lab(v):
        return ('%d luni' % v) if v < 24 else ('%d ani' % (v // 12))
    a, b = lab(min(mo)), lab(max(mo))
    return a if a == b else (a, b)


def age_from_page(page):
    m = re.search(r'\(mărimea (\d+)-(\d+)\)', page.get('text', ''))
    if not m:
        return None
    lo, hi = int(m.group(1)), int(m.group(2))
    d_ = {'cat': 'imbracaminte'}
    return age_phrase(d_, [str(lo), str(hi)])


def lower_first(s):
    return s[:1].lower() + s[1:] if s else s


def type_of(title, brand):
    t = title.split(' ' + brand + ' ')[0] if (' ' + brand + ' ') in title else title.split(' ' + brand)[0]
    return t.strip()


def art_phrase(t):
    w = t.split()[0].lower()
    art, pl = LEX.get(w, ('un', 0))
    return art, pl


def numfirst(s):
    m = re.match(r'^\d+(?:\.\d+)?', str(s))
    return float(m.group(0)) if m else None


def is_shoe(cat):
    return 'incaltaminte' in cat or cat == 'sosete'


def is_hat(cat, title):
    return re.search(r'căciul|pălări|cagul|șapc|fular', title, re.I) is not None


def age_from_units(sizes):
    """Marimi de tip 6-12M, 1-2Y, 2-4 ani, 6-12 luni -> (a, b) in luni/ani, sau None."""
    mo = []
    for s_ in sizes:
        m = re.match(r'^(\d+)(?:\s*-\s*(\d+))?\s*(M|luni|Y|ani|an)$', str(s_).strip(), re.I)
        if not m:
            return None
        k = 1 if m.group(3).lower() in ('m', 'luni') else 12
        mo += [int(m.group(1)) * k] + ([int(m.group(2)) * k] if m.group(2) else [])
    if not mo:
        return None

    def lab(v):
        return ('%d luni' % v) if v < 24 else ('%d ani' % (v // 12))
    a, b = lab(min(mo)), lab(max(mo))
    return a if a == b else (a, b)


def age_from_page(page):
    m = re.search(r'\(mărimea (\d+)-(\d+)\)', page.get('text', ''))
    if not m:
        return None
    lo, hi = int(m.group(1)), int(m.group(2))
    d_ = {'cat': 'imbracaminte'}
    return age_phrase(d_, [str(lo), str(hi)])


def lower_first(s):
    return s[:1].lower() + s[1:] if s else s


def type_of(title, brand):
    t = title.split(' ' + brand + ' ')[0] if (' ' + brand + ' ') in title else title.split(' ' + brand)[0]
    return t.strip()


def art_phrase(t):
    w = t.split()[0].lower()
    art, pl = LEX.get(w, ('un', 0))
    return art, pl


def numfirst(s):
    m = re.match(r'^\d+(?:\.\d+)?', str(s))
    return float(m.group(0)) if m else None


def is_shoe(cat):
    return 'incaltaminte' in cat or cat == 'sosete'


def is_hat(cat, title):
    return re.search(r'căciul|pălări|cagul|șapc|fular', title, re.I) is not None


def age_from_units(sizes):
    """Marimi de tip 6-12M, 1-2Y, 2-4 ani, 6-12 luni -> (a, b) in luni/ani, sau None."""
    mo = []
    for s_ in sizes:
        m = re.match(r'^(\d+)(?:\s*-\s*(\d+))?\s*(M|luni|Y|ani|an)$', str(s_).strip(), re.I)
        if not m:
            return None
        k = 1 if m.group(3).lower() in ('m', 'luni') else 12
        mo += [int(m.group(1)) * k] + ([int(m.group(2)) * k] if m.group(2) else [])
    if not mo:
        return None

    def lab(v):
        return ('%d luni' % v) if v < 24 else ('%d ani' % (v // 12))
    a, b = lab(min(mo)), lab(max(mo))
    return a if a == b else (a, b)


def age_from_page(page):
    m = re.search(r'\(mărimea (\d+)-(\d+)\)', page.get('text', ''))
    if not m:
        return None
    lo, hi = int(m.group(1)), int(m.group(2))
    d_ = {'cat': 'imbracaminte'}
    return age_phrase(d_, [str(lo), str(hi)])


def lower_first(s):
    return s[:1].lower() + s[1:] if s else s


def type_of(title, brand):
    t = title.split(' ' + brand + ' ')[0] if (' ' + brand + ' ') in title else title.split(' ' + brand)[0]
    return t.strip()


def art_phrase(t):
    w = t.split()[0].lower()
    art, pl = LEX.get(w, ('un', 0))
    return art, pl


def numfirst(s):
    m = re.match(r'^\d+(?:\.\d+)?', str(s))
    return float(m.group(0)) if m else None


def is_shoe(cat):
    return 'incaltaminte' in cat or cat == 'sosete'


def is_hat(cat, title):
    return re.search(r'căciul|pălări|cagul|șapc|fular', title, re.I) is not None


def age_from_units(sizes):
    """Marimi de tip 6-12M, 1-2Y, 2-4 ani, 6-12 luni -> (a, b) in luni/ani, sau None."""
    mo = []
    for s_ in sizes:
        m = re.match(r'^(\d+)(?:\s*-\s*(\d+))?\s*(M|luni|Y|ani|an)$', str(s_).strip(), re.I)
        if not m:
            return None
        k = 1 if m.group(3).lower() in ('m', 'luni') else 12
        mo += [int(m.group(1)) * k] + ([int(m.group(2)) * k] if m.group(2) else [])
    if not mo:
        return None

    def lab(v):
        return ('%d luni' % v) if v < 24 else ('%d ani' % (v // 12))
    a, b = lab(min(mo)), lab(max(mo))
    return a if a == b else (a, b)


def age_from_page(page):
    m = re.search(r'\(mărimea (\d+)-(\d+)\)', page.get('text', ''))
    if not m:
        return None
    lo, hi = int(m.group(1)), int(m.group(2))
    d_ = {'cat': 'imbracaminte'}
    return age_phrase(d_, [str(lo), str(hi)])


def lower_first(s):
    return s[:1].lower() + s[1:] if s else s


def type_of(title, brand):
    t = title.split(' ' + brand + ' ')[0] if (' ' + brand + ' ') in title else title.split(' ' + brand)[0]
    return t.strip()


def art_phrase(t):
    w = t.split()[0].lower()
    art, pl = LEX.get(w, ('un', 0))
    return art, pl


def numfirst(s):
    m = re.match(r'^\d+(?:\.\d+)?', str(s))
    return float(m.group(0)) if m else None


def is_shoe(cat):
    return 'incaltaminte' in cat or cat == 'sosete'


def is_hat(cat, title):
    return re.search(r'căciul|pălări|cagul|șapc|fular', title, re.I) is not None


def age_phrase(d, sizes):
    """Intervalul de vârstă (cu „ani/luni") din mărimi; sau None."""
    nums = [n for n in (numfirst(s) for s in sizes) if n is not None]
    if not nums:
        return None
    lo, hi = min(nums), max(nums)
    shoe = is_shoe(d['cat']) or (bool(re.search('șosete', d.get('title', ''), re.I)) and hi < 50)
    table = AGE_SHOE if shoe else AGE_CLOTH
    if shoe:
        if hi > 60:
            return None
    else:
        if lo < 44 or hi > 190:
            return None

    def at(v):
        best = table[0][1]
        for k, lab in table:
            if k <= v:
                best = lab
        return best
    if not shoe and lo < 62:
        a = 'nou-născuți'
    else:
        a = at(lo)
    b = at(hi)
    if shoe and hi >= 36:
        return 'de la ' + a + ' în sus' if lo < 36 else '12 ani și peste'
    if a == b:
        return a
    return a, b


# ------------------------------------------------------------------ extragerea faptelor
def kv_lines(lines):
    out = []
    for ln in lines:
        m = re.match(r'^([^:]{2,45}):\s*(.+)$', ln.strip())
        if m:
            out.append((m.group(1).strip(), m.group(2).strip(), ln.strip()))
    return out


def section(text, start, ends):
    i = text.find(start)
    if i < 0:
        return ''
    j = len(text)
    for e in ends:
        k = text.find(e, i + len(start))
        if k >= 0:
            j = min(j, k)
    return text[i + len(start):j]


SKIP_KEYS = re.compile(r'^(articol nr|nr\. articol|țara de origine|tara de origine|instrucțiuni de îngrijire|culoare|informații producător|brand|vândut)', re.I)


def facts_for(page):
    """-> dict: mat:[(label,value,frag)], cut:[...], det:[...], tags:[...], care:[...], code:str, prose:[...]"""
    f = {'mat': [], 'cut': [], 'det': [], 'tags': [], 'care': [], 'code': '', 'prose': []}
    host = page.get('sursa', '')
    t = page.get('text', '')
    if host == 'zalando.ro':
        blk = section(t, 'Material și îngrijire', ['Raportează', 'Next\nUrmărește', 'Urmărește'])
        sub = {'mat': section(blk, '', ['Detalii\n', 'Mărime și croială'])}
        det = section(blk, 'Detalii\n', ['Mărime și croială', 'Vezi detaliile', 'Deschide'])
        cut = section(blk, 'Mărime și croială', ['Deschide ghidul', 'Next'])
        for k, v, fr in kv_lines(sub['mat'].split('\n')):
            if re.search(r'instruc', k, re.I):
                f['care'].append((k, v, fr))
            elif not SKIP_KEYS.match(k):
                f['mat'].append((k, v, fr))
        for k, v, fr in kv_lines(det.split('\n')):
            if re.match(r'articol nr', k, re.I):
                f['code'] = v
            elif not SKIP_KEYS.match(k):
                f['det'].append((k, v, fr))
        for k, v, fr in kv_lines(cut.split('\n')):
            f['cut'].append((k, v, fr))
    elif host == 'aboutyou.ro':
        blk = section(t, 'Design și funcționalitate\n', ['Informații producător', 'Raportarea'])
        tags = section(blk, '', ['Nr. articol', 'Mărime și croi', 'Material și îngrijire'])
        f['tags'] = [ln.strip() for ln in tags.split('\n') if ln.strip()]
        m = re.search(r'Nr\. articol\s+(\S+)', blk)
        f['code'] = m.group(1) if m else ''
        cut = section(blk, 'Mărime și croi\n', ['Material și îngrijire'])
        for k, v, fr in kv_lines(cut.split('\n')):
            f['cut'].append((k, v, fr))
        mat = section(blk, 'Material și îngrijire\n', [])
        for ln in mat.split('\n'):
            ln = ln.strip()
            if not ln:
                continue
            m2 = re.match(r'^([^:]{2,45}):\s*(.+)$', ln)
            if m2:
                if SKIP_KEYS.match(m2.group(1)):
                    continue
                f['mat'].append((m2.group(1).strip(), m2.group(2).strip(), ln))
            elif re.search(r'spăl|usca|uscător|călca|clor|curăț', ln, re.I):
                f['care'].append(('Îngrijire', ln, ln))
    else:  # 4kidspoint: descrierea (ld) + liniile Material / Îngrijire
        d = (page.get('ld') or {}).get('description') or ''
        body = (page.get('text') or '') + '\n' + d
        for pat, label in (
            (r'Material:\s*([^\n]+)', 'Material'),
            (r'Îngrijire:\s*([^\n]+)', 'Îngrijire'),
        ):
            m = re.search(pat, body)
            if m:
                (f['care'] if label == 'Îngrijire' else f['mat']).append((label, m.group(1).strip().rstrip('.'), m.group(0).strip()))
        PAT = [
            (r'coloană de apă de ([\d  .]+ ?mm)', 'Impermeabilitate', 'coloană de apă de {1}'),
            (r'rezistent[ăa]? la vânt', 'Vânt', 'rezistent la vânt'),
            (r'(?<!coloană de apă )(?<!fără )impermeabil[ăa]?', 'Impermeabilitate', 'material impermeabil'),
            (r'respirabil[ăa]?', 'Respirabilitate', 'material respirabil'),
            (r'cusături (lipite|etanșe)', 'Cusături', '{0}'),
            (r'gluga detașabil[ăa]|glugă (?:detașabil[ăa]|reglabil[ăa])', 'Glugă', 'detașabilă'),
            (r'manșete elastice', 'Manșete', 'elastice'),
            (r'căptușeal[ăa] (moale|termic[ăa]|călduroas[ăa])', 'Căptușeală', '{1}'),
            (r'poliester reciclat', 'Material', 'poliester reciclat'),
            (r'lână (?:100% )?naturală', 'Material', 'lână naturală'),
            (r'amestec (?:moale )?de lână și acril', 'Material', 'amestec de lână și acril'),
            (r'Megol', 'Material', 'Megol (material ecologic)'),
            (r'membran[ăa] din aluminiu', 'Membrană', 'din aluminiu, la nivelul tălpii'),
            (r'piele întoarsă', 'Talpă', 'din piele întoarsă'),
            (r'talpă flexibilă', 'Talpă', 'flexibilă'),
            (r'structur[ăa] raiat[ăa]', 'Structură', 'de tip rib (nervurată)'),
            (r'izolați[ea] termic[ăa]|termoizolant[ăe]?', 'Izolație', 'termică'),
            (r'reflectorizant[ăe]', 'Siguranță', 'elemente reflectorizante'),
            (r'(?:cu arici|bandă (?:lată )?(?:cu )?velcro|închidere[^.\n,;]{0,20}velcro)', 'Închidere', 'cu arici'),
            (r'(?:lână|lana) merino', 'Material', 'lână merino'),
            (r'cauciuc natural', 'Material', 'cauciuc natural'),
            (r'fără PVC și ftalați', 'Material', 'fără PVC și ftalați'),
            (r'fără (?:compuși )?PFC', 'Impregnare', 'fără compuși PFC'),
            (r'OEKO-TEX[^.\n,;]{0,25}', 'Certificare', '{0}'),
            (r'talpă antiderapantă|suprafața antiderapantă', 'Talpă', 'antiderapantă'),
            (r'fermoar[^.\n,;]{0,45}', 'Închidere', '{0}'),
            (r'se spală la mașină la \d+ ?°C', 'Îngrijire', '{0}'),
        ]
        seen = set()
        for pat, label, fmt in PAT:
            m = re.search(pat, body, re.I)
            if m and m.group(0).lower() not in seen:
                seen.add(m.group(0).lower())
                if label == 'Impermeabilitate' and any(x[0] == 'Impermeabilitate' for x in f['prose']):
                    continue
                val = fmt.replace('{0}', m.group(0).strip()).replace('{1}', m.group(1) if m.groups() else '')
                f['prose'].append((label, val.strip(), m.group(0).strip()))
    return f


# ------------------------------------------------------------------ text
def join_ro(parts):
    parts = [p for p in parts if p]
    if len(parts) <= 1:
        return ''.join(parts)
    return ', '.join(parts[:-1]) + ' și ' + parts[-1]


def last_seg(v):
    parts = [x.strip() for x in v.split(':') if x.strip()]
    return parts[-1] if parts else v


def comp_phrase(v):
    v = last_seg(v)
    """„85% bumbac, 15% poliester" → „85% bumbac și 15% poliester"."""
    items = [x.strip() for x in re.split(r',\s*', v) if x.strip()]
    return join_ro(items)


def clean_val(v):
    v = last_seg(v.strip().rstrip('.'))
    if re.search(r'Megol', v):
        return v
    if re.search(r'\d|[A-ZĂÂÎȘȚ]{2,}', v):
        return v[:1].lower() + v[1:] if v[:1].isalpha() and not v[:2].isupper() else v
    return v.lower()


def usage_from(f):
    cand = [(v, fr) for _, v, fr in f['prose'] + f['mat'] + f['det']] + [(t, t) for t in f['tags']]
    for rx, label in ((r'coloană de apă|impermeabil', 'ploaie și umezeală'), (r'rezistent[ăa]? la vânt', 'vânt'), (r'izolați[ea] termic|termoizolant|umplutură|puf', 'frig')):
        for v, fr in cand:
            if re.search(rx, v.lower()):
                return [(label, fr)]
    return []


ADJ_PL = {'lungă': 'lungi', 'scurtă': 'scurte', 'lung': 'lungi', 'scurt': 'scurte', 'lungi': 'lungi', 'scurte': 'scurte'}
STRUCT = re.compile(r'^structura materialului$', re.I)


def fmt_age(age, form, rng):
    """Propozitia despre marimi si varsta; varsta e mereu aproximativa si spusa in feluri diferite."""
    one = not isinstance(age, tuple)
    if one:
        a1 = age
        a2 = ''
        between = pair_to = a1
    else:
        a1, a2 = age
        if a1.endswith(' ani') and a2.endswith(' ani'):
            a1 = a1[:-4]
        between = '%s și %s' % (a1, a2)
        pair_to = '%s până la %s' % (a1, a2)
    if not one and a1.startswith('nou-născuți'):
        between = pair_to = 'de la nou-născut până la %s' % a2
        kids = between
        if form in ('cam', 'aproximativ'):
            pair_to = 'de la nou-născut până la cam %s' % a2
            between = kids = pair_to
        if form in ('de obicei',):
            return 'Mărimile %s se potrivesc, de obicei, copiilor %s.' % (rng, kids)
        if form == 'în general':
            return 'În general, gama %s este potrivită copiilor %s.' % (rng, kids)
        if form == 'de regulă':
            return 'De regulă, mărimile %s acoperă copiii %s.' % (rng, kids)
        if form == 'cam':
            return 'Mărimile %s sunt făcute pentru copii %s.' % (rng, kids)
        if form == 'aproximativ':
            return 'Mărimile %s se adresează, aproximativ, copiilor %s.' % (rng, between.replace('cam ', ''))
        return 'Gama %s se adresează, în mare, copiilor %s.' % (rng, kids)
    kids = (a1 if a1.startswith('de la ') else 'de %s' % a1) if one else ('între ' + between)
    if form == 'de obicei':
        return 'Mărimile %s se potrivesc, de obicei, copiilor %s.' % (rng, kids)
    if form == 'în general':
        return 'În general, gama %s este potrivită copiilor %s.' % (rng, kids)
    if form == 'de regulă':
        return 'De regulă, mărimile %s acoperă copiii %s.' % (rng, kids)
    if form == 'cam':
        return 'Mărimile %s sunt făcute pentru copii de cam %s.' % (rng, a1 if one else pair_to)
    if form == 'aproximativ':
        return 'Pentru copii de aproximativ %s sunt gândite mărimile %s.' % (a1 if one else pair_to, rng)
    return 'Gama %s se adresează, în mare, copiilor %s.' % (rng, kids)


def cut_inference(cr):
    c = (cr or '').lower()
    if re.search(r'loose|relaxed|oversize|lejer|larg', c):
        return 'are loc de un strat mai gros dedesubt și vine comod și copiilor mai plinuți'
    if re.search(r'slim|mulat|skinny|strâns', c):
        return 'stă aproape de corp, deci peste haine groase poate fi strâmt'
    return ''


def build(d, page):
    key = d['key']
    brand = d['brand']
    f = facts_for(page)
    title = d['title']
    ptype = type_of(title, brand)
    art, pl = art_phrase(ptype)
    gen = 'bebe' if d['top'] == 'bebe' else d['gender']
    gen_anchor = {'bebe': 'pentru bebeluși', 'fete': 'pentru fete', 'baieti': 'pentru băieți', 'unisex': 'unisex'}[gen]
    base = lower_first(ptype)
    if gen == 'bebe' and 'bebelu' in base:
        anchor = base if 'pentru bebelu' in base else re.sub(r'bebelu', 'pentru bebelu', base, count=1)
    else:
        anchor = base + ' ' + gen_anchor
    cat_href = '/categorie/%s/' % d['cat']
    brand_a = '<a href="/brand/%s/">%s</a>' % (brand.lower().replace(' ', '-'), brand)
    cat_a = '<a href="%s">%s</a>' % (cat_href, anchor)
    color = (d['colors'] or '').lower()
    pack = re.search(r'(\d+) Pack', title)
    sizes = d['sizes'] or d['sizes_unavail']
    smin, smax = (sizes[0], sizes[-1]) if sizes else ('', '')
    page_blob = (page.get('text', '') + ' ' + page.get('h1', '') + ' ' + json.dumps(page.get('ld') or {}, ensure_ascii=False))
    surse = []

    def src(label, frag):
        if frag and frag in page_blob and not any(s_[1] == frag for s_ in surse):
            surse.append((label, frag))

    # ---- faptele (lista 3-6)
    mats = [m for m in f['mat'] if re.match(r'^material( textil)?( exterior)?$|^material suprafață$', m[0], re.I)] or f['mat'][:1]
    main_mat = mats[0] if mats else None
    items = []
    if main_mat:
        items.append(main_mat)
    for m in f['mat']:
        if m is not main_mat and not re.search(r'conține|origine animal', m[0], re.I) and len(items) < 3:
            items.append(m)
    struct = next((m for m in items if STRUCT.match(m[0])), None)
    items += list(f['cut'][:3])
    items += list(f['det'][:3])
    items += [x for x in f['prose'] if x[0] != 'Îngrijire']
    if f['tags']:
        items.append(('Detalii', ', '.join(lower_first(x) for x in f['tags'][:5]), f['tags'][0]))
    if f['care']:
        items.append(('Îngrijire', f['care'][-1][1], f['care'][-1][2]))
    seen, uniq = set(), []
    for lab, val, fr in items:
        if fr in seen:
            continue
        seen.add(fr)
        uniq.append((lab, val, fr))
    BAN = ('ortopedic', 'amortiz', 'aderen', 'stabil', 'respiră', 'se simte', 'perfect', 'ideal', 'premium', 'ofert', 'compar', 'stoc', ' preț', ' lei')
    items = [it for it in uniq if not any(b in (it[0] + ' ' + it[1]).lower() for b in BAN)][:6]
    for lab, val, fr in items:
        src(lab.lower(), fr)
    if not surse:
        nm = (page.get('ld') or {}).get('name') or ''
        if nm and nm in page_blob:
            surse.append(('nume produs', nm))
    for tg in f['tags'][1:5]:
        src('detaliu', tg)
    if pack and pack.group(0).upper() in page_blob.upper():
        surse.append(('set', pack.group(0).upper() if pack.group(0).upper() in page_blob else pack.group(0)))
    insuf = len(surse) < 3 or len(items) < 3

    # ---- propozitia 1
    verb = 'sunt' if pl else 'este'
    matp = ''
    if main_mat:
        v = main_mat[1]
        matp = ', din ' + (comp_phrase(v) if re.search(r'\d+\s*%', v) else clean_val(v))
    colp = (', de culoare ' + color) if color else ''
    packp = (', în set de %s bucăți' % pack.group(1)) if pack else ''
    t1 = pick(key, 'p1', ([] if pl else ['{B} {V} {art} {A}{col}{pack}{mat}.']) + [
        'Aici găsești {art} {A} {B}{col}{pack}{mat}.',
        '{B} are în gamă {art} {A}{col}{pack}{mat}.',
    ])
    s1 = (t1.replace('{B}', brand_a).replace('{V}', verb).replace('{art}', art).replace('{A}', cat_a).replace('{col}', colp)
          .replace('{pack}', packp).replace('{mat}', matp))
    s1 = re.sub(r'\s+', ' ', s1)
    # ---- propozitiile 2-3: fapte din sursa
    s2 = []
    mcode = re.search(r'\(([A-Z0-9]{6,9})\)', title)
    if mcode and f['code'] and f['code'].startswith(mcode.group(1)):
        s2.append(pick(key, 'code', ['Codul modelului este %s.', 'În fișa produsului apare codul %s.']) % f['code'])
        frag_code = ('Nr. articol ' + f['code']) if page.get('sursa') == 'aboutyou.ro' else ('Articol nr.:' + f['code'])
        src('cod model', frag_code)
    cut = {k.lower(): (v, fr) for k, v, fr in f['cut']}
    cr = cut.get('croială') or cut.get('croi')
    if cr:
        inf = cut_inference(cr[0])
        cv = clean_val(cr[0])
        if cv.startswith('croi'):
            txt = 'Fișa produsului indică %s' % cv
        else:
            txt = pick(key, 'cutS', ['Croiala declarată e %s' % cv, 'Fișa produsului indică croială %s' % cv])
        s2.append(txt + ((', deci ' + inf) if inf else '') + '.')
        src('croială', cr[1])
    if struct:
        s2.append(pick(key, 'struct', ['Țesătura este de tip %s.', 'Materialul are structură de %s.']) % clean_val(struct[1]))
    use = usage_from(f)
    if use:
        s2.append(pick(key, 'use', ['Materialul declarat potrivește zilele cu %s.', 'Datele din fișă duc spre zilele cu %s.']) % use[0][0])
        src('utilizare', use[0][1])
    prose = [p for p in f['prose'] if p[0] not in ('Îngrijire',)]
    if prose and not use:
        phr = [(('%s %s' % (p[0].lower(), clean_val(p[1]))) if len(p[1].split()) == 1 else clean_val(p[1])) for p in prose[:3]]
        s2.append('Descrierea modelului menționează: %s.' % join_ro(phr))
    det = [x for x in f['det'] if x[0].lower() in ('buzunare', 'detalii', 'talie', 'decolteu', 'guler', 'design', 'model')]
    if det and len(' '.join(s2).split()) < 14:
        s2.append(pick(key, 'detS', ['Printre detalii se numără %s.', 'Mai are %s.']) % join_ro([('%s %s' % (k.lower(), clean_val(v))) for k, v, _ in det[:3]]))
    tags = f['tags'][:3]
    if tags and len(' '.join(s2).split()) < 14:
        s2.append(pick(key, 'tagS', ['Fișa mai menționează: %s.', 'Ca detalii de design, apar: %s.']) % join_ro([lower_first(x) for x in tags]))
    used_care = set()
    if len((s1 + ' ' + ' '.join(s2[:3])).split()) < 27 and f['care']:
        c0 = f['care'][0]
        s2.append('Despre îngrijire, fișa spune: %s.' % clean_val(c0[1]))
        src('îngrijire', c0[2])
        used_care.add(c0[2])
    if len((s1 + ' ' + ' '.join(s2[:3])).split()) < 26 and color:
        s2.append('Culoarea declarată în fișa produsului este %s.' % color)
    if len((s1 + ' ' + ' '.join(s2[:3])).split()) < 26 and smin:
        s2.append('Se găsește în mărimile %s.' % (smin if smin == smax else '%s-%s' % (smin, smax)))
    p1 = '<p>' + (s1 + ' ' + ' '.join(s2[:3])).strip() + '</p>'

    # ---- lista
    li = []
    for lab, val, fr in items:
        v = comp_phrase(val) if re.search(r'\d+\s*%', val) else clean_val(val)
        li.append('<li><strong>%s</strong>: %s</li>' % (lab, v))
    ref = ('acești ' if pl else ('acest ' if art == 'un' else 'această ')) + base.split()[0]
    intro = pick(key, 'intro', [
        'Pe pagina produsului sunt trecute câteva detalii care contează la alegere:',
        'Înainte de a alege mărimea, merită citite detaliile declarate pentru %s:' % ref,
        'Detaliile modelului, așa cum apar în fișa produsului:',
        'Din descrierea modelului reținem aceste detalii:',
        'Ce se știe despre construcția și materialul acestui model:',
        'Pentru a ști la ce să te aștepți, fișa tehnică spune:',
    ])
    lead = '<p>' + intro + '</p>' if li else ''
    ul = '<ul>' + ''.join(li) + '</ul>' if li else ''

    # ---- marimi / varsta
    age = None if (is_hat(d['cat'], title) and sizes) else age_phrase(d, sizes)
    if age is None and not (is_hat(d['cat'], title) and sizes):
        age = age_from_units(sizes)
    if age is None and not (is_hat(d['cat'], title) and sizes):
        age = age_from_page(page)
    form = pick(key, 'form', ['de obicei', 'în general', 'de regulă', 'cam', 'aproximativ', 'în mare'])
    rng = smin if smin == smax else '%s-%s' % (smin, smax)
    if age is None and is_hat(d['cat'], title) and smin:
        p3 = '<p>Mărimile sunt între %s și %s și se măsoară în centimetri, după circumferința capului; acoperă, de regulă, vârste de la nou-născut până la câțiva ani.</p>' % (smin, smax)
    elif age is not None and smin:
        p3 = '<p>' + fmt_age(age, form, rng) + '</p>'
    elif smin:
        p3 = '<p>Pe pagină sunt trecute mărimile de la %s până la %s; vârsta potrivită depinde de înălțimea copilului, așa că merită măsurat înainte de comandă.</p>' % (smin, smax)
        insuf = True
    else:
        p3 = '<p>Produsul se vinde într-o singură mărime, fără variante de ales în funcție de vârstă.</p>'
        insuf = True
    extra = ''
    nwords = len(re.sub(r'<[^>]+>', ' ', p1 + lead + ul + p3).split())
    care = [c for c in f['care'] if c[2] not in [it[2] for it in items] and c[2] not in used_care]
    if nwords < 92 and care:
        extra += '<p>Despre îngrijire, fișa menționează: %s.</p>' % clean_val(care[0][1])
        src('îngrijire', care[0][2])
        nwords += 8 + len(care[0][1].split())
    allsz = sorted(set(sizes) | set(d['sizes_unavail']), key=lambda z: (numfirst(z) or 0, str(z)))
    shown = allsz if len(allsz) <= 9 else (list(sizes) if len(sizes) <= 9 else [])
    if nwords < 90 and len(shown) > 1:
        extra += '<p>Pe pagina produsului sunt trecute mărimile %s.</p>' % join_ro(shown)
    nwords = len(re.sub(r'<[^>]+>', ' ', p1 + lead + ul + p3 + extra).split())
    if nwords < 86:
        extra += '<p>' + pick(key, 'tip', [
            'Înainte de comandă, merită verificat tabelul de mărimi al magazinului, pentru că fiecare producător măsoară puțin diferit.',
            'Fiecare producător măsoară puțin diferit, așa că tabelul de mărimi al magazinului rămâne ghidul sigur la alegere.',
        ]) + '</p>'
    html = p1 + lead + ul + p3 + extra
    specs = {}
    if main_mat:
        specs['Material'] = comp_phrase(main_mat[1]) if re.search(r'\d+\s*%', main_mat[1]) else clean_val(main_mat[1])
    det_s = [lower_first(x) for x in f['tags'][:4]] or [clean_val(v) for _, v, _ in (f['det'] + f['cut'])[:3]]
    if det_s:
        specs['Caracteristici'] = ', '.join(det_s)
    if f['code']:
        specs['Cod produs'] = f['code']
    return {'key': key, 'html': html, 'surse': surse, 'specs': specs, 'insuf': insuf}


def main():
    out = []
    miss = 0
    for d in drafts:
        sp = os.path.join(HERE, 'brand-surse', d['key'].replace(':', '_') + '.json')
        if not os.path.exists(sp):
            miss += 1
            continue
        page = json.load(open(sp, encoding='utf-8'))
        if page.get('eroare'):
            miss += 1
            continue
        out.append(build(d, page))
    os.makedirs(os.path.join(HERE, 'brand-desc-src'), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, 'brand-desc-src', 'auto.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('generate:', len(out), '| fără sursă:', miss, '| insuficiente:', sum(1 for x in out if x['insuf']))


if __name__ == '__main__':
    main()
