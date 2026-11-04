#!/usr/bin/env python3
"""
Construiește fișierul de drafturi (wp-content/plugins/hainute-core/data/drafts-brand-v1.json) din:
  - CSV-urile bifate de proprietar (Next / En Fant): coloana `bifa` = potrivirea e reală;
  - scanările brand-*-produse.json (magazinul sursă) și brand-matches-produse.json (magazinele bifate).
NU scrie nimic în site; fișierul îl importă hainute_import_drafts_file (draft-import.php).

Rulare:  python tools/crawler/brand-drafts-build.py [director_csv]
"""
import csv, json, os, re, sys, collections, unicodedata
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
CSV_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Downloads')
OUT = os.path.join(HERE, '..', '..', 'wp-content', 'plugins', 'hainute-core', 'data', 'drafts-brand-v1.json')


def load(p):
    with open(os.path.join(HERE, p), encoding='utf-8') as f:
        return json.load(f)


def host_of(u):
    return urlparse(u).netloc.replace('www.', '')


def recs(data):
    """url -> înregistrare, din formatul brand-scan.js (cu sau fără cheia `magazine`)."""
    M = data.get('magazine', data)
    out = {}
    for h, v in M.items():
        if isinstance(v, list):
            for r in v:
                out[r['url']] = r
    return out


SRC = {}
for f in ('brand-next-produse.json', 'brand-next-produse-toate.json', 'brand-en-fant-produse.json', 'brand-matches-produse.json'):
    if os.path.exists(os.path.join(HERE, f)):
        SRC.update(recs(load(f)))


def read_ticked(name):
    rows = list(csv.reader(open(os.path.join(CSV_DIR, name), encoding='utf-8-sig')))
    h = rows[0]
    return [dict(zip(h, r)) for r in rows[1:]]


def produse_csv(p):
    rows = list(csv.reader(open(os.path.join(HERE, p), encoding='utf-8-sig')))
    h = rows[0]
    return {r[0]: dict(zip(h, r)) for r in rows[1:]}


# ---------------------------------------------------------------- culori
COLOR_EN = [
    ('white', 'Alb'), ('black', 'Negru'), ('navy', 'Bleumarin'), ('blue', 'Albastru'), ('pink', 'Roz'),
    ('red', 'Roșu'), ('burgundy', 'Bordo'), ('green', 'Verde'), ('sage', 'Verde'), ('khaki', 'Kaki'),
    ('brown', 'Maro'), ('tan', 'Maro'), ('chocolate', 'Maro'), ('caramel', 'Maro'), ('mink', 'Bej'),
    ('grey', 'Gri'), ('gray', 'Gri'), ('charcoal', 'Gri'), ('beige', 'Bej'), ('neutral', 'Crem'),
    ('cream', 'Crem'), ('ecru', 'Crem'), ('yellow', 'Galben'), ('orange', 'Portocaliu'), ('purple', 'Mov'),
    ('lilac', 'Mov'), ('multi', 'Multicolor'), ('rainbow', 'Multicolor'), ('silver', 'Argintiu'), ('gold', 'Auriu'),
    ('stone', 'Bej'), ('oatmeal', 'Bej'), ('oat', 'Bej'),
]
COLOR_EF = {  # nume de culoare En Fant → română
    'ivy green': 'Verde', 'coffee bean': 'Maro', 'portabella': 'Maro', 'dark slate': 'Gri închis', 'mayflower': 'Roz',
    'bark': 'Maro', 'port royale': 'Bordo', 'burlwood': 'Maro deschis', 'old rose': 'Roz', 'rose taupe': 'Roz',
    'flint stone': 'Gri', 'flint': 'Gri', 'sand melange': 'Bej', 'marron': 'Maro', 'grey melange': 'Gri',
    'dark grey melange': 'Gri închis', 'parisian night': 'Bleumarin', 'blue night': 'Bleumarin', 'navy': 'Bleumarin',
    'fungi': 'Bej', 'withered rose': 'Roz', 'chocolate brown': 'Maro', 'leather brown': 'Maro',
    'wild rose': 'Roz', 'walnut melange': 'Maro', 'blue surf': 'Albastru',
}


def ro_color_zalando(color):
    left = (color or '').split('/')[0].lower()
    for en, ro in COLOR_EN:
        if re.search(r'\b' + en + r'\b', left):
            return ro
    fam = (color or '').split('/')[-1].strip()
    return fam[:1].upper() + fam[1:] if fam else ''


def ro_color_ef(text):
    t = (text or '').lower()
    for k in sorted(COLOR_EF, key=len, reverse=True):
        if re.search(r'\b' + re.escape(k) + r'\b', t):
            return COLOR_EF[k]
    return ''


# ---------------------------------------------------------------- tip → categorie
def deacc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')


# (regex pe tip fără diacritice, grup, frunză)
TYPES = [
    (r'rochie|fusta', 'imbracaminte', 'rochii-fuste'),
    (r'costum de schi|costum de iarna|geaca|jacheta|parka|vesta|palton|pufoaica|costum matlasat|haina', 'imbracaminte', 'geci-jachete'),
    (r'pantaloni|trening|jogger|leggings|colanti|jeans|salopeta de ploaie', 'imbracaminte', 'pantaloni-treninguri'),
    (r'salopeta|pijama|compleu|set lenjerie|halat|combinezon|body set|set ', 'imbracaminte', 'salopete-compleuri'),
    (r'bluza|tricou|polo|hanorac|pulover|cardigan|body|top|camasa|molton|maiou', 'imbracaminte', 'bluze-tricouri-hanorace'),
    (r'sneakers|adidasi|pantofi sport|trainers|incaltaminte pentru bebe|incaltaminte bebelusi', 'incaltaminte', 'adidasi'),
    (r'cizme|ghete|bocanci|wellingtons|wellies|kalosze|boots', 'incaltaminte', 'ghete-cizme'),
    (r'papuci|sabot|botosei|botosi|slipper|saboti', 'incaltaminte', 'papuci'),
    (r'sandale|sapatica', 'incaltaminte', 'sandale'),
    (r'pantofi|mocasini|balerini|pantofi cu', 'incaltaminte', 'pantofi'),
    (r'caciula|sosete|cravata|manusi|palarie|sapca|fular|esarfa|geanta|cagula|guler|bandana|turban|chiloti|slip', 'accesorii', 'caciuli-manusi-accesorii'),
]
# frunze disponibile pe site (slug de term); lipsa → înlocuire
LEAF_SLUG = {
    'fete': {'imbracaminte': {'bluze-tricouri-hanorace': 'bluze-tricouri-hanorace', 'geci-jachete': 'geci-jachete', 'pantaloni-treninguri': 'pantaloni-treninguri', 'rochii-fuste': 'rochii-fuste', 'salopete-compleuri': 'salopete-compleuri'},
             'incaltaminte': {'adidasi': 'adidasi', 'ghete-cizme': 'ghete-cizme', 'pantofi': 'incaltaminte-pantofi', 'papuci': 'papuci', 'sandale': 'incaltaminte-sandale'},
             'accesorii': {'caciuli-manusi-accesorii': 'caciuli-manusi-accesorii'}},
    'baieti': {'imbracaminte': {k: 'baieti-imbracaminte-' + k for k in ('bluze-tricouri-hanorace', 'geci-jachete', 'pantaloni-treninguri', 'salopete-compleuri')},
               'incaltaminte': {k: 'baieti-incaltaminte-' + k for k in ('adidasi', 'ghete-cizme', 'pantofi', 'papuci', 'sandale')},
               'accesorii': {'caciuli-manusi-accesorii': 'baieti-accesorii-caciuli-manusi-accesorii'}},
    'unisex': {'imbracaminte': {k: 'unisex-imbracaminte-' + k for k in ('bluze-tricouri-hanorace', 'geci-jachete', 'pantaloni-treninguri', 'salopete-compleuri')},
               'incaltaminte': {k: 'unisex-incaltaminte-' + k for k in ('adidasi', 'ghete-cizme', 'pantofi', 'papuci', 'sandale')},
               'accesorii': {'caciuli-manusi-accesorii': 'unisex-accesorii-caciuli-manusi-accesorii'}},
    'bebe': {'imbracaminte': {k: 'bebe-imbracaminte-' + k for k in ('bluze-tricouri-hanorace', 'geci-jachete', 'pantaloni-treninguri', 'salopete-compleuri')},
             'incaltaminte': {k: 'bebe-incaltaminte-' + k for k in ('adidasi', 'ghete-cizme', 'pantofi')}},
}
FEMALE = r'rochie|fusta|balerin|unicorn|girl|sequin|printesa|ballerina'
MALE = r'\bboy|baiat|baieti|dinozaur|dino\b'


def num(s):
    m = re.match(r'^(\d+(?:[.,]\d+)?)', str(s))
    return float(m.group(1).replace(',', '.')) if m else None


def classify(ptype, all_sizes, title_raw):
    """-> (top, grup, leaf_key, slug_term) ; top în fete/baieti/unisex/bebe."""
    t = deacc(ptype)
    grp = leaf = None
    cands = [t]
    if re.search(r'incaltaminte', t):  # tip generic: decide numele („school shoes" → pantofi, „trainers" → adidași)
        cands = [deacc(title_raw)]
    for cand in cands:
        for rx, g, l in TYPES:
            if re.search(rx, cand):
                grp, leaf = g, l
                break
        if grp:
            break
    if not grp and re.search(r'shoes', deacc(title_raw)):
        grp, leaf = 'incaltaminte', 'pantofi'
    if not grp:
        return None
    sizes = [n for n in (num(s) for s in all_sizes) if n is not None]
    cm = [n for n in sizes if n >= 44]
    top = 'unisex'
    low = deacc(title_raw)
    if re.search(FEMALE, low) and not re.search(MALE, low):
        top = 'fete'
    elif re.search(MALE, low) and not re.search(FEMALE, low):
        top = 'baieti'
    is_baby = (grp == 'imbracaminte' and (bool(re.search(r'bebelus|baby', low)) or (cm and max(cm) <= 104))) or (grp == 'incaltaminte' and bool(sizes) and max(sizes) <= 24 and not cm) or bool(re.search(r'botosei|botosi|footies', low))
    if is_baby:
        top = 'bebe'
    slug = LEAF_SLUG[top][grp].get(leaf) if grp in LEAF_SLUG[top] else None
    if not slug:  # bebe fără frunza respectivă → arborele unisex
        top = 'unisex' if top == 'bebe' else top
        slug = LEAF_SLUG[top][grp].get(leaf)
    return top, grp, leaf, slug


# ---------------------------------------------------------------- titluri
JUNK = re.compile(r'^(regular fit|standard|plain|\.|family|set|slim fit|wide fit)$', re.I)


def title_case(s):
    small = {'and', 'of', 'the', 'in', 'on', 'with', 'for', 'to'}
    out = []
    for i, w in enumerate(re.split(r'\s+', s.strip())):
        if not w:
            continue
        if re.match(r'^\d', w) or w.upper() == w and len(w) <= 3 and not w.isalpha():
            out.append(w)
        elif w.lower() in small and i:
            out.append(w.lower())
        else:
            out.append(w[:1].upper() + w[1:].lower())
    return ' '.join(out)


def parse_zalando(name):
    """„REGULAR FIT - TWO WAY ZIP 3 PACK - Salopetă bebeluși - beige" → (tip, model)."""
    parts = [p.strip(' .') for p in re.split(r'\s+-\s+', name) if p.strip(' .')]
    if len(parts) >= 2:
        parts = parts[:-1]  # fără culoare
    ptype = parts[-1]
    desc = [p for p in parts[:-1] if not JUNK.match(p)]
    desc = [re.sub(r'\b(REGULAR FIT|STANDARD|PLAIN|SLIM FIT)\b', ' ', d, flags=re.I) for d in desc]
    model = title_case(re.sub(r'\s+', ' ', ' '.join(desc)).strip(' .-'))
    return ptype, model


def parse_aboutyou(name, brand):
    n = re.sub(r'^(next|en fant)\s+', '', name, flags=re.I).strip()
    m = re.search(r"['‘’\"]([^'\"]+)['‘’\"]", n)
    model = title_case(m.group(1)) if m else ''
    ptype = re.sub(r"\s*['‘’\"][^'\"]+['‘’\"]", '', n).strip()
    return ptype, model


EF_TYPE_FIX = [
    (r'wellingtons', 'Cizme de cauciuc'),
]


def parse_4kp(name, color):
    n = re.sub(r'^En Fant\s*-?\s*', '', name, flags=re.I).strip()
    for a, b in (('Salopeta de iarna', 'Salopetă de iarnă'), ('Salopeta', 'Salopetă'), ('iarna', 'iarnă')):
        n = n.replace(a, b)
    n = re.sub(r'\s+pentru copii', '', n, flags=re.I)
    return n


def clean_title_words(s):
    return re.sub(r'\s+', ' ', s).strip()


GENERIC = set("""regular fit standard plain unisex baby set price starter long short sleeve cuffed crew neck pull on up through zip
two way footless matching family and top trousers joggers jogger hoodie hooded jumper jacket fleece sweat sweatshirt
sweatpants pants leggings dress skirt robe coat parka slippers slipper mule clogs shoes trainers socks sock hat hats beanie
beanies turban turbans tie wellies boots sleepsuit sleepsuits bodysuit bodysuits snowsuit pyjamas polo shirt shirts tee
tshirt t-shirt tops piece pc low lace smart school leather touch fastening fasten elastic strap loafer flip flops sneakers
handle warm lined borg faux fur padded printed graphic bear faced trapper cord cosy novelty character textured barrel younger
yrs soft essential wide the of with for""".split())


def short_model(model):
    """Din descriptorul englezesc al Zalando pastram doar ce deosebeste produsul: 5 Pack, Christmas, Toy Story."""
    toks = re.split(r'\s+', re.sub(r'[()\u00ae]', ' ', model).strip())
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        tl = t.lower().strip('-')
        if re.match(r'^\d+$', t) and i + 1 < len(toks) and toks[i + 1].lower() in ('pack', 'piece', 'pc'):
            out.append(t + ' Pack')
            i += 2
            continue
        if re.match(r'^\d+$', t) or re.match(r'^\d+pc$', tl) or re.match(r'^\d+-\d+yrs$', tl) or tl in GENERIC:
            i += 1
            continue
        if tl == 'five':
            out.append('5 Pack')
        elif tl != 'pack':
            out.append(t)
        i += 1
    seen, res = set(), []
    for w in out:
        if w.lower() not in seen:
            seen.add(w.lower())
            res.append(w)
    return ' '.join(res[:4])


def make_title(ptype, brand, gender_word, model, color):
    ptype = ptype[:1].upper() + ptype[1:]
    parts = [ptype, brand, gender_word, model, color]
    return clean_title_words(' '.join(p for p in parts if p))


GENDER_WORD = {'fete': 'Fete', 'baieti': 'Băieți', 'unisex': 'Unisex', 'bebe': 'Bebe'}


# ---------------------------------------------------------------- produs din înregistrări
def norm_size(x):
    x = str(x).strip()
    if x.lower() in ('default title', 'one size', 'onesize', 'os', ''):
        return ''
    x = re.sub(r'\s*\(.*?\)', '', x)            # "62-68cm (3-6 Months)" -> "62-68cm"
    x = re.sub(r'\s*cm$', '', x, flags=re.I)
    x = x.replace('\\', '-').replace('/', '-')   # "19\20" -> "19-20"
    x = re.sub(r'(\d),5', r'\1.5', x)             # 23,5 -> 23.5
    return x.strip()


def norm_sizes(lst):
    out = []
    for x in lst or []:
        n = norm_size(x)
        if n and n not in out:
            out.append(n)
    return out


def offer_from(r, source=False, lens_url=None):
    sizes = norm_sizes(r.get('sizes'))
    un = norm_sizes(r.get('unavailable'))
    price = r.get('price') or 0
    in_stock = bool(sizes) if (sizes or un) else bool(r.get('in_stock'))
    img = r.get('images') or []
    image = (img[0] if img else r.get('image') or '')
    return {
        'url': r['url'], 'host': host_of(r['url']), 'price': price, 'currency': r.get('currency') or 'RON',
        'in_stock': in_stock, 'sizes': sizes, 'unavail': un, 'color': '', 'image': image,
        'gtins': r.get('gtins') or [], 'name': r.get('name') or '', 'source': source,
    }


def build(brand, ticked, produse):
    by_id = collections.OrderedDict()
    for r in ticked:
        by_id.setdefault(r['id'], []).append(r)
    # grupuri cross (EAN): același produs în magazine diferite
    groups = collections.OrderedDict()
    for i, rows in by_id.items():
        g = rows[0]['grup_cross']
        groups.setdefault('g' + g if g else i, []).append(i)
    out, skipped = [], []
    for gk, ids in groups.items():
        offers, imgs, names, colors_raw = [], [], [], []
        ok_ids = []
        for i in ids:
            src = produse.get(i)
            rec = SRC.get(src['url']) if src else None
            if not rec or not rec.get('name') or rec.get('name', '').lower() == 'error page' or not (rec.get('price') or 0) > 0 or not (rec.get('sizes') or rec.get('unavailable')):
                skipped.append((i, 'fără date de pe pagina sursă'))
                continue
            ok_ids.append(i)
            o = offer_from(rec, source=True)
            o['color_raw'] = rec.get('color') or ''
            offers.append(o)
            names.append((host_of(rec['url']), rec))
            for r in by_id[i]:
                if r['bifa'].upper() == 'TRUE' and r['url_produs']:
                    mrec = SRC.get(r['url_produs'])
                    if mrec:
                        offers.append(dict(offer_from(mrec), match_lens=True))
                    else:
                        offers.append({'url': r['url_produs'], 'host': host_of(r['url_produs']), 'price': 0, 'currency': 'RON', 'in_stock': False, 'sizes': [], 'unavail': [], 'color': '', 'image': r['poza_gasita'], 'gtins': [], 'name': r['titlu_gasit'], 'source': False, 'match_lens': True})
        if not ok_ids:
            continue
        # o ofertă per magazin (prima câștigă: sursele înaintea potrivirilor)
        seen, uniq = set(), []
        for o in offers:
            if o['host'] in seen:
                continue
            seen.add(o['host'])
            uniq.append(o)
        offers = uniq
        prim = next(o for o in offers if o['source'])
        host0, rec0 = names[0]
        allz = set()
        for o in offers:
            allz.update(o['sizes'])
        un_all = set()
        for o in offers:
            un_all.update(o['unavail'])
        # titlu
        if host0 == 'zalando.ro':
            ptype, model = parse_zalando(rec0['name'])
            color = ro_color_zalando(prim.get('color_raw'))
            if brand == 'En Fant':
                color = ro_color_ef(rec0.get('name') or '') or color
        elif host0 == 'aboutyou.ro':
            ptype, model = parse_aboutyou(rec0['name'], brand)
            color = (rec0.get('color') or '').strip().capitalize()
        else:  # 4kidspoint
            full = parse_4kp(rec0['name'], rec0.get('color'))
            color = ro_color_ef(full)
            model = ''
            ptype = full
        cl = classify(ptype, list(allz | un_all), rec0['name'])
        if not cl:
            skipped.append((ids[0], 'tip necunoscut: ' + ptype))
            continue
        top, grp, leaf, slug = cl
        img = prim['image']
        gal = []
        for i in ids:
            src = produse.get(i)
            rec = SRC.get(src['url']) if src else None
            if rec:
                for u in (rec.get('images') or [])[:6]:
                    if u not in gal and u != img:
                        gal.append(u)
        out.append({'_ptype': ptype, '_model': model, '_color': color, '_top': top, 'key': f"{brand.lower().replace(' ', '-')}:{gk if gk.startswith('g') else ids[0]}",
                    'brand': brand, 'cat': slug, 'gender': 'unisex' if top in ('bebe', 'unisex') else top, 'image': img, 'gallery': gal[:6],
                    'colors': color, 'sizes': sorted(allz, key=lambda s: (num(s) or 0, s)), 'sizes_unavail': sorted(un_all - allz, key=lambda s: (num(s) or 0, s)),
                    'offers': offers, 'ids': ids})
    return out, skipped


LEAF_LABEL = {'adidasi': 'Adidași', 'pantofi': 'Pantofi', 'ghete-cizme': 'Cizme', 'papuci': 'Papuci', 'sandale': 'Sandale'}


def title_for(d, brand, extra=0):
    ptype = d['_ptype']
    t = deacc(ptype)
    if re.search(r'^incaltaminte', t):
        for k, v in LEAF_LABEL.items():
            if d['cat'].endswith(k):
                ptype = v
    for rx, lab in ((r'^sneakers low$', 'Adidași'), (r'^wellingtons', 'Cizme de cauciuc'), (r'^pantofi sport$', 'Adidași')):
        if re.search(rx, t):
            ptype = lab
    model = d['_model']
    m = re.match(r'^(Tapered|Wide leg|Slim|Regular|Straight)\s+(.+)$', ptype, re.I)
    if m:
        ptype, model = m.group(2), (m.group(1) + ' ' + model).strip()
    color = d['_color'].split(' / ')[0].strip()
    if brand == 'En Fant':  # 4kidspoint: numele englezesc al culorii En Fant din titlu se scoate
        for k in sorted(COLOR_EF, key=len, reverse=True):
            ptype = re.sub(r'\b' + re.escape(k) + r'\b', '', ptype, flags=re.I)
        ptype = re.sub(r'\s+', ' ', ptype).strip(' -')
        if re.search(r'boots', ptype, re.I) and not re.search(r'cizme', ptype, re.I):
            ptype = 'Cizme ' + ptype
    if brand == 'Next' and model:
        if extra == 1:
            gen = [w for w in re.sub(r'[()]', '', model).split() if w.lower() in ('long', 'sleeve', 'short', 'school', 'polo', 'wide')]
            model = (' '.join(gen[:3]) + ' ' + short_model(model)).strip()
        elif extra == 2:
            model = re.sub(r'[()]', '', model)
        else:
            model = short_model(model)
    word = GENDER_WORD['bebe' if d['_top'] == 'bebe' else d['gender']]
    if re.search(r'bebelus', deacc(ptype)):
        word = ''
    model = re.sub(r'\b(\w+)\s+\1\b', r'\1', model, flags=re.I)
    return make_title(ptype, brand, word, model, color)


def model_code(key):
    """Codul modelului din pagina sursa (AY: Nr. articol ENF0034..., Zalando: Articol nr. NX324G2M1-A11)."""
    sp = os.path.join(HERE, 'brand-surse', key.replace(':', '_') + '.json')
    if not os.path.exists(sp):
        return ''
    try:
        t = json.load(open(sp, encoding='utf-8')).get('text', '')
    except ValueError:
        return ''
    m = re.search(r'Nr\. articol\s+([A-Z0-9]+)', t)
    if m:
        return m.group(1)[:7]
    m = re.search(r'Articol nr\.:\s*([A-Z0-9]+)', t)
    return m.group(1) if m else ''


def dedup_titles(items):
    for lvl in (1,):
        c = collections.Counter(d['title'] for d in items)
        for d in items:
            if c[d['title']] > 1:
                d['title'] = title_for(d, d['brand'], extra=lvl)
    c = collections.Counter(d['title'] for d in items)
    for d in items:
        if c[d['title']] > 1:
            code = model_code(d['key'])
            if code:
                d['title'] += ' (%s)' % code
    c = collections.Counter(d['title'] for d in items)
    for d in items:
        if c[d['title']] > 1:
            lo, hi = (d['sizes'] or ['?'])[0], (d['sizes'] or ['?'])[-1]
            d['title'] += ' (%s-%s)' % (lo, hi) if lo != hi else ' (%s)' % lo


def main():
    all_out, all_skipped = [], []
    for brand, csvname, prod in (('Next', 'hainute.ro - Next.csv', 'brand-next-produse.csv'), ('En Fant', 'hainute.ro - En Fant.csv', 'brand-en-fant-produse.csv')):
        o, s = build(brand, read_ticked(csvname), produse_csv(prod))
        for d in o:
            d['top'] = d['_top']
            d['title'] = title_for(d, brand)
        all_out += o
        all_skipped += [(brand, *x) for x in s]
    # lanțul de titluri duplicate: adaugă un sufix cu mărimea minimă, ca titlurile să fie unice
    dedup_titles(all_out)
    cnt = collections.Counter(d['title'] for d in all_out)
    json.dump(all_out, open(os.path.join(HERE, 'brand-drafts-build.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    write_final(all_out)
    print(len(all_out), 'produse;', len(all_skipped), 'sărite')
    for s in all_skipped[:60]:
        print('  sărit', s)
    print('titluri duplicate:', sum(1 for v in cnt.values() if v > 1))


def write_final(items):
    desc = {}
    dp = os.path.join(HERE, 'brand-drafts-desc.json')
    if os.path.exists(dp):
        desc = json.load(open(dp, encoding='utf-8'))
    out = []
    for d in items:
        sp = os.path.join(HERE, 'brand-surse', d['key'].replace(':', '_') + '.json')
        if os.path.exists(sp):
            try:
                imgs = json.load(open(sp, encoding='utf-8')).get('imgs') or []
            except ValueError:
                imgs = []
            if imgs:
                base = lambda u: u.split('?')[0]
                if base(imgs[0]) == base(d['image']) or base(d['image']) in [base(x) for x in imgs]:
                    d['image'] = next(x for x in imgs if base(x) == base(d['image']))  # aceeași poză, la rezoluție mare
                d['gallery'] = [x for x in imgs if base(x) != base(d['image'])][:6]
        prim = d['offers'][0]
        pg = set(str(g).lstrip('0') for g in prim.get('gtins', []))
        offers = []
        for o in d['offers']:
            og = set(str(g).lstrip('0') for g in o.get('gtins', []))
            match = 'ean' if og and pg and (og & pg) else ''
            offers.append({'url': o['url'], 'price': o['price'], 'in_stock': o['in_stock'], 'sizes': o['sizes'], 'unavail': o['unavail'],
                           'image': o['image'], 'color': d['colors'], 'match': match})
        rec = {'key': d['key'], 'title': d['title'], 'brand': d['brand'], 'cat': d['cat'], 'gender': d['gender'], 'top': d['top'],
               'image': d['image'], 'gallery': d['gallery'], 'colors': d['colors'], 'sizes': d['sizes'], 'sizes_unavail': d['sizes_unavail'], 'offers': offers, 'partner_block': len(offers) <= 2}
        x = desc.get(d['key'])
        if x:
            rec['description_html'] = x['html']
            rec['specs'] = x.get('specs', {})
            rec['desc_version'] = x.get('versiune', 'v7')
        out.append(rec)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('scris', len(out), 'produse in', os.path.normpath(OUT), '(%d cu descriere)' % sum(1 for r in out if 'description_html' in r))


if __name__ == '__main__':
    main()
