"""Verificare automată pentru descrierile v4 (docs/prompt_descrieri_hainute_v4).
Rulare: python tools/check-descrieri-v4.py docs/descrieri-v4-test.json extract1.json [extract2.json ...] [--cats cats.txt]"""
import io, json, re, sys, html
args = sys.argv[1:]
cats = set()
if '--cats' in args:
    i = args.index('--cats'); cats = {l.split(' | ')[0].strip() for l in io.open(args[i+1], encoding='utf-8') if l.strip()}; args = args[:i] + args[i+2:]
d = json.load(io.open(args[0], encoding='utf-8'))
pages = {}
for f in args[1:]:
    for p in json.load(io.open(f, encoding='utf-8')):
        pages.setdefault(p['id'], '')
        pages[p['id']] += ' ' + json.dumps(p, ensure_ascii=False)
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\n', ' ').replace('<br />', ' ')).lower()
main_ok = {'/categorie/incaltaminte-baieti/': 'pentru băieți', '/categorie/incaltaminte-fete/': 'pentru fete', '/categorie/imbracaminte-baieti/': 'pentru băieți', '/categorie/imbracaminte-fete/': 'pentru fete', '/categorie/imbracaminte-bebe/': 'pentru bebeluși'}
banned = ['—', '!', '?', 'cel mai bun', 'perfect', 'ideal', 'extraordinar', 'premium', 'must-have', 'revoluționar', 'în concluzie', 'așadar', 'în plus,', 'de asemenea', 'compar', 'reducere', 'ofert', 'intră în gama', 'face parte din', 'se încadrează', 'aparține', 'secțiunea', 'confort și stil', 'nu va dezamăgi', 'ore în șir', 'fără să limiteze', 'se asortează', 'nu stau locului', 'respiră', 'aerul circulă', 'aderență', 'amortiz', 'moale la fiecare pas', 'fără presiune', 'stabilitate', 'ortopedic', 'susține piciorul', 'verificabil pe eticheta', 'recunosc imediat', 'face diferența', 'se simte', 'fetița', 'băiatul', 'cea mică', ' preț', 'stoc', 'magazinele care']
for x in d:
    h = x['descriere_html']; txt = html.unescape(re.sub(r'<[^>]+>', ' ', h)); words = len(txt.split()); low = txt.lower(); issues = []
    paras = re.findall(r'<p>(.*?)</p>', h, re.S); items = re.findall(r'<li>', h)
    if not 170 <= words <= 240: issues.append(f'lungime {words}')
    p1 = len(html.unescape(re.sub(r'<[^>]+>', ' ', paras[0])).split())
    if not 40 <= p1 <= 60: issues.append(f'P1 {p1}')
    if not 4 <= len(items) <= 7: issues.append(f'listă {len(items)} puncte')
    if 'Potrivit pentru' not in re.findall(r'<li>.*?</li>', h)[-1]: issues.append('ultimul punct nu e Potrivit pentru')
    p4 = html.unescape(re.sub(r'<[^>]+>', ' ', paras[-1])); 
    if len(re.findall(r'[.]\s', p4 + ' ')) > 2: issues.append('P4 > 2 propoziții')
    for b in banned:
        if b in low: issues.append('interzis: ' + b.strip())
    if 'orientativ' not in low: issues.append('fără orientativ')
    links = re.findall(r'<a href="([^"]+)">([^<]+)</a>', h)
    mains = [l for l in links if l[0] in main_ok]
    if len(mains) != 1 or main_ok[mains[0][0]] not in html.unescape(mains[0][1]): issues.append('ancoră/slug principal: ' + str(mains))
    if not any(l[0].startswith('/brand/') for l in links): issues.append('fără link brand')
    comp = x['categorie_complementara']['slug']
    if comp == x['categorie_principala'] or (cats and comp not in cats): issues.append('slug complementar invalid: ' + comp)
    if len(links) != 3: issues.append(f'{len(links)} linkuri (trebuie 3)')
    page = norm(pages.get(x['id'], ''))
    miss = [s['fragment'] for s in x['surse'] if norm(s['fragment']) not in page]
    if miss: issues.append('fragmente negăsite pe pagină: ' + ' | '.join(miss))
    print(x['id'], words, 'cuv |', '; '.join(issues) if issues else 'OK')
