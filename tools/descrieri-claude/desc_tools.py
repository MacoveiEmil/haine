"""Unelte pentru scrierea descrierilor v7 în volum.

  python desc_tools.py dump 9165 9191 ...   # rezumat compact: date produs + sursa curățată
  (în scripturile de lot)  from desc_tools import w
"""
import io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AICI = os.path.dirname(os.path.abspath(__file__))
C = ROOT + '/content'
_P = None


def produse():
    global _P
    if _P is None:
        _P = {p['id']: p for p in json.load(io.open(C + '/produse.json', encoding='utf-8'))}
    return _P


CM = [(86, 1), (92, 2), (98, 3), (104, 4), (110, 5), (116, 6), (122, 7), (128, 8), (134, 9), (140, 10), (146, 11),
      (152, 12), (158, 13), (164, 14), (170, 15), (176, 16), (182, 17), (188, 18)]
CM_LUNI = [(44, 0), (50, 0), (56, 1), (62, 3), (68, 6), (74, 9), (80, 12)]
EU = [(15, (0, 1)), (19, (1, 2)), (23, (2, 3)), (26, (3, 4)), (28, (4, 5)), (30, (6, 7)), (32, (8, 9)), (34, (10, 11)), (36, (12, 99))]


def _nums(s):
    return [float(x.replace(',', '.')) for x in re.findall(r'\d+(?:[.,]\d+)?', str(s))]


def _cm_age(n):  # (valoare, unitate)
    if n < 83:
        v = 0
        for k, m in CM_LUNI:
            if n >= k:
                v = m
        return (1, 'ani') if v >= 12 else (v, 'luni')
    return min(CM, key=lambda x: abs(x[0] - n))[1], 'ani'


def _eu(n):
    r = EU[0][1]
    for k, rng in EU:
        if n >= k:
            r = rng
    return r


def varsta(marimi):
    """Vârsta aproximativă din prima și ultima mărime de pe site (Anexa promptului)."""
    nums = [x for m in marimi for x in _nums(m)]
    if not nums:
        return None
    lo, hi = _nums(marimi[0])[:1] or [min(nums)], _nums(marimi[-1])[-1:] or [max(nums)]
    lo, hi = lo[0], hi[0]
    if hi < lo:
        lo, hi = min(nums), max(nums)
    if hi <= 43:  # încălțăminte EU
        a, b = _eu(lo)[0], _eu(hi)[1]
        a = max(a, 1)
        return (f'de la {a} an în sus' if a == 1 else f'de la {a} ani în sus') if b == 99 else f'{a}-{b} ani'
    (a, ua), (b, ub) = _cm_age(lo), _cm_age(hi)
    if ua == ub == 'luni':
        return f'{a}-{b} luni'
    if ua == 'luni':
        return f'{a} {"lună" if a == 1 else "luni"} - {b} ani'
    return f'{a}-{b} ani'


GEN = {'fete': 'pentru fete', 'baieti': 'pentru băieți', 'bebe': 'pentru bebeluși', 'unisex': 'unisex'}
TITLU_GENERIC = {'FETE', 'BĂIEȚI', 'BAIETI', 'UNISEX', 'BEBE', 'JACKET', 'KIDS', 'JR', 'GORE', 'TEX'}


def strip(h):
    h = re.sub(r'<br\s*/?>', ' | ', str(h or ''))
    h = re.sub(r'</li>', ' | ', h)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()


def dump(pid):
    p = produse().get(pid)
    if not p:
        print(f'#{pid}: nu e în produse.json')
        return
    brand_w = {w.upper() for w in re.split(r'\W+', p.get('brand') or '') if w}
    model = [w for w in re.findall(r'[A-ZĂÂÎȘȚ0-9][A-ZĂÂÎȘȚ0-9-]{2,}', p['titlu']) if w not in brand_w and w not in TITLU_GENERIC and not w.isdigit()]
    m = p.get('marimi') or []
    print(f"=== #{pid} | {p['titlu']} | {p['magazin']}")
    print(f"  cat: {p.get('categorie_frunza') or p['categorie_principala']}  ancoră: „… {GEN.get(p['gen'], p['gen'])}”  brand: {p['brand_slug']}  "
          f"model-cerut: {' '.join(model) or '-'}  culoare-titlu: {p['titlu'].split()[-1]}")
    print(f"  mărimi: {m[0] if m else '-'} … {m[-1] if m else '-'} ({len(m)})  vârsta: {varsta(m) if m else '-'}  stoc: {p['cu_stoc']}")
    f = f'{C}/surse/{pid}.json'
    if not os.path.exists(f):
        print('  SURSĂ LIPSĂ')
        return
    s = json.load(io.open(f, encoding='utf-8'))
    if s.get('eroare'):
        print('  SURSĂ CU EROARE:', s['eroare'][:100])
    print('  h1:', strip(s.get('h1', '')).replace('\n', ' / ')[:160])
    a = s.get('answear')
    if a:
        print('  DESC:', strip(a.get('description'))[:700])
        print('  FULL:', strip(a.get('fullDescription'))[:1500])
        print('  MAT:', ' ; '.join(f"{x.get('componentName') or ''}: {strip(x.get('composition'))}" for x in (a.get('materials') or []))[:300])
        print('  ATTR:', ' ; '.join(a.get('attributes') or [])[:400], '| COLOR:', a.get('color'))
    else:
        ld = s.get('ld') or {}
        if ld:
            print('  LD:', strip(ld.get('description'))[:900], '| color:', ld.get('color'), '| material:', ld.get('material'), '| sku:', ld.get('sku'))
        t = re.split(r'Te-ar mai putea interesa|Altii le-au salvat in favorite|Produse similare|Recomandate pentru tine|Clienții au mai cumpărat|Ați putea fi interesat|Produse recomandate', s.get('text', ''))[0]
        t = re.sub(r'\d+[.,]\d{2} ?(LEI|lei|RON|Lei)', '', t)
        print('  TEXT:', re.sub(r'\s*\n\s*', ' | ', t)[:1400])


def w(pid, html, surse, specs=None, comp=None, notes=(), insuf=False, varsta_txt=None):
    p = produse()[pid]
    src = json.load(io.open(f'{C}/surse/{pid}.json', encoding='utf-8'))
    url = src.get('url', '').replace('https://', '').split('?')[0]
    d = {'id': pid, 'versiune': 'v7', 'descriere_html': html,
         'surse': [{'fapt': a, 'url': url, 'fragment': b} for a, b in surse],
         'specificatii_tehnice': specs or {}, 'categorie_complementara': comp,
         'varsta_orientativa': varsta_txt or varsta(p.get('marimi') or []) or '', 'date_insuficiente': insuf, 'confidence_notes': list(notes)}
    with io.open(f'{C}/descrieri/{pid}.json', 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write('\n')


def L(*items):
    """Lista: L(('Material', '…'), ('Închidere', '…'))."""
    return '<ul>' + ''.join(f'<li><strong>{k}</strong>: {v}</li>' for k, v in items) + '</ul>'


def A(slug_or_url, text):
    return f'<a href="{slug_or_url}">{text}</a>'


if __name__ == '__main__' and len(sys.argv) > 2 and sys.argv[1] == 'dump':
    for x in sys.argv[2:]:
        dump(int(x))


def up(pid, pairs, surse=(), notes=()):
    """Actualizează o descriere existentă la v7 (înlocuiri punctuale + surse noi)."""
    f = f'{C}/descrieri/{pid}.json'
    d = json.load(io.open(f, encoding='utf-8'))
    if d.get('versiune') == 'v7':  # deja actualizată (lotul se poate rula din nou)
        return
    h = d['descriere_html']
    for a, b in pairs:
        assert h.count(a) == 1, (pid, a[:60])
        h = h.replace(a, b)
    d['descriere_html'], d['versiune'] = h, 'v7'
    url = d['surse'][0]['url'] if d.get('surse') else ''
    d['surse'] = (d.get('surse') or []) + [{'fapt': a, 'url': url, 'fragment': b} for a, b in surse]
    d['confidence_notes'] = (d.get('confidence_notes') or []) + list(notes)
    with io.open(f, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
        fh.write('\n')


def sursa_ok(pid):
    f = f'{C}/surse/{pid}.json'
    if not os.path.exists(f):
        return False
    s = json.load(io.open(f, encoding='utf-8'))
    if s.get('eroare') or 'SE INCARCA' in s.get('text', '')[:400]:
        return False
    a = s.get('answear') or {}
    return bool(a.get('description') or a.get('fullDescription') or (s.get('ld') or {}).get('description') or len(s.get('text', '')) > 1500)


def urmatoarele(n=10, skip=()):
    ids = [int(l) for l in open(os.path.join(AICI, 'todo.txt')) if l.strip()]
    out = []
    for i in ids:
        if i in skip:
            continue
        f = f'{C}/descrieri/{i}.json'
        if os.path.exists(f) and json.load(io.open(f, encoding='utf-8')).get('versiune') == 'v7':
            continue
        if sursa_ok(i):
            out.append(i)
        if len(out) >= n:
            break
    return out


if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'next':
    sk = {int(l) for l in open(os.path.join(AICI, 'sari.txt')) if l.strip()}
    ids = urmatoarele(int(sys.argv[2]) if len(sys.argv) > 2 else 10, skip=sk)
    print('IDS:', ' '.join(map(str, ids)))
    for x in ids:
        dump(x)
