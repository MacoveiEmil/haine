#!/usr/bin/env python3
"""
Verifică descrierile scrise pentru drafturile de brand (Next / En Fant) cu aceeași verificare ca pe server
(tools/descrieri.py), înainte să ajungă în fișierul de import.

Intrare:  tools/crawler/brand-desc-src/*.json   (liste de {key, html, surse:[{fapt,fragment}], specs, varsta, complement})
          tools/crawler/brand-surse/{cheie}.json (pagina magazinului, de la brand-desc-extract.js)
          tools/crawler/brand-drafts-build.json  (produsele)
Ieșire:   tools/crawler/brand-drafts-desc.json   ({cheie: {html, specs, versiune}}), doar cele care trec
          raport în consolă (probleme pe produs).

Rulare: python tools/crawler/brand-desc-check.py [--all]
"""
import glob, json, os, re, shutil, sys, tempfile

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import descrieri as D  # noqa: E402

TMP = os.path.join(tempfile.gettempdir(), 'brand-desc-check')
shutil.rmtree(TMP, ignore_errors=True)
for sub in ('surse', 'descrieri'):
    os.makedirs(os.path.join(TMP, sub))
for f in ('reguli-descrieri.json', 'categorii.json'):
    shutil.copy(os.path.join(ROOT, 'content', f), TMP)
for f in glob.glob(os.path.join(ROOT, 'content', 'descrieri', '*.json')):
    shutil.copy(f, os.path.join(TMP, 'descrieri'))
D.C = TMP
D._CORPUS = None

drafts = {d['key']: d for d in json.load(open(os.path.join(HERE, 'brand-drafts-build.json'), encoding='utf-8'))}
GEN = {'unisex': 'unisex', 'bebe': 'bebe', 'fete': 'fete', 'baieti': 'baieti'}


def ro_age_sizes(d):
    return d['sizes'] + d['sizes_unavail']


def num_sizes(d):
    out = []
    for s in ro_age_sizes(d):
        m = re.match(r'^\d+(\.\d+)?', str(s))
        if m:
            out.append(float(m.group(0)) if '.' in m.group(0) else int(m.group(0)))
    return out


src = {}
for f in sorted(glob.glob(os.path.join(HERE, 'brand-desc-src', '*.json'))):
    for x in json.load(open(f, encoding='utf-8')):
        src[x['key']] = x

produse, files = {}, {}
for i, (key, x) in enumerate(src.items(), start=900001):
    d = drafts.get(key)
    if not d:
        print('cheie necunoscută:', key)
        continue
    cat = '/categorie/%s/' % d['cat']
    produse[i] = {'id': i, 'titlu': d['title'], 'brand': d['brand'], 'brand_slug': '/brand/%s/' % d['brand'].lower().replace(' ', '-'), 'magazin': '',
                  'link_afiliat': '', 'categorie_principala': cat, 'categorie_frunza': cat, 'tip': '', 'gen': 'bebe' if d['top'] == 'bebe' else d['gender'],
                  'marimi': (x.get('marimi') or d['sizes'] or d['sizes_unavail']), 'cu_stoc': True, 'descriere_versiune': '', 'pagina': ''}
    sp = os.path.join(HERE, 'brand-surse', key.replace(':', '_') + '.json')
    page = json.load(open(sp, encoding='utf-8')) if os.path.exists(sp) else {}
    json.dump(page, open(os.path.join(TMP, 'surse', '%d.json' % i), 'w', encoding='utf-8'), ensure_ascii=False)
    files[key] = i
    out = {'id': i, 'versiune': 'v7', 'descriere_html': x['html'], 'surse': [{'fapt': a, 'url': d['offers'][0]['url'], 'fragment': b} for a, b in x['surse']],
           'specificatii_tehnice': x.get('specs', {}), 'categorie_complementara': x.get('complement'), 'varsta_orientativa': x.get('varsta', ''),
           'date_insuficiente': bool(x.get('insuf')), 'confidence_notes': []}
    json.dump(out, open(os.path.join(TMP, 'descrieri', '%d.json' % i), 'w', encoding='utf-8'), ensure_ascii=False)

categorii = {c['slug'] for c in json.load(open(os.path.join(TMP, 'categorii.json'), encoding='utf-8'))}
R = D.rules()
ok, bad, final = 0, 0, {}
for key, i in files.items():
    pid, words, issues = D.check(os.path.join(TMP, 'descrieri', '%d.json' % i), produse, categorii, R)
    # fără mărimi pe pagină (mărime unică) nu avem de unde scoate vârsta: nu o inventăm
    if not drafts[key]['sizes'] and not drafts[key]['sizes_unavail']:
        issues = [i for i in issues if not i.startswith('lipsește vârsta')]
    if issues:
        bad += 1
        print(key, f'{words} cuv |', '; '.join(issues))
    else:
        ok += 1
        x = src[key]
        final[key] = {'html': x['html'], 'specs': x.get('specs', {}), 'versiune': 'v7'}
print(f'\nOK: {ok}  cu probleme: {bad}  (din {len(files)} scrise; {len(drafts)} produse în total)')
# păstrăm și ce a trecut data trecută (încrementat pe loturi)
outp = os.path.join(HERE, 'brand-drafts-desc.json')
old = json.load(open(outp, encoding='utf-8')) if os.path.exists(outp) else {}
old.update(final)
json.dump(old, open(outp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('în brand-drafts-desc.json:', len(old))
