# Predare: descrierile v7 (scrise de Claude)

Ultima actualizare: după lotul 131 (commit „Descrieri v7: lotul 131”).

## Stare

- **Gata.** Toată lista din `tools/descrieri-claude/todo.txt` e parcursă; `desc_tools.py next` nu mai întoarce nimic.
- **1300 de descrieri v7** în `content/descrieri/*.json`, toate trecute de `tools/descrieri.py check`, împinse pe `main`
  (serverul le aplică singur în 1–2 minute).
- Scripturile fiecărui lot: `tools/descrieri-claude/loturi/b001.py` … `b131.py`.
- Instrumentele și regulile învățate: `tools/descrieri-claude/README.md`.

## Ce a rămas nescris

**Produse sărite (19, sunt în `tools/descrieri-claude/sari.txt`):**
- pentru adulți: 5390, 8668, 9443, 9662, 10584, 10816, 11358, 12393, 12716;
- fără sursă: 5063, 5075, 5123;
- Sportisimo VÂNDUT, fără nicio mărime și fără indiciu de vârstă (verificarea cere vârsta): 14008, 14133, 14326, 14733, 14753, 14803, 14899.
  Dacă revin pe stoc cu mărimi, se pot scrie.

**55 de duplicate canonice fără descriere v7 (nu sunt în todo.txt):**
12362, 12384, 12398, 12408, 12441, 12448, 12467, 12497, 12515, 12525, 12558, 12560, 12562, 12620, 12628, 12660,
12663, 12666, 12702, 12707, 12710, 12713, 12719, 12726, 12728, 12742, 12758, 12761, 12762, 12779, 12782, 12794,
12798, 12833, 12847, 12861, 12885, 12919, 12927, 12929, 12933, 12942, 12944, 13014, 13035, 13038, 13048, 13050,
13073, 13076, 13129, 13148, 13200, 13277, 13474.

## Probleme de catalog

Lista completă: `tools/descrieri-claude/probleme-catalog.txt` (127 de rânduri). Pe scurt:
- culoarea din titlul site-ului diferă de cea a magazinului, sau titlul are alt cuvânt în loc de culoare
  („JACKET”, „blugi”, „Băieți”, „Unisex”, „piele” etc.); în descriere s-a folosit culoarea magazinului, cu notă;
- categorie greșită: multe ghete de iarnă/trekking listate la Pantofi, seturi și overale la Geci,
  cămăși/tricouri/hanorace la Geci, romper la Bluze, căciulă la Fular;
- material contradictoriu la magazin („piele întoarsă” în text, compoziție sintetică);
- Sportisimo: produse VÂNDUT fără culoare; Fashion Days: 16 produse doar cu titlu (descrieri scurte, `date_insuficiente`).

## În așteptare

- Paragraful despre cookie-uri (GA Consent Mode v2): **scris pe 22.10.2026, cu acordul proprietarului**
  (politica de cookie-uri + cea de confidențialitate, din `includes/analytics.php`).

## Cum continui într-o conversație nouă

Lipește asta ca prim mesaj:

> Citește `CLAUDE.md`, `docs/handover-descrieri-v7.md` și `tools/descrieri-claude/README.md`.
> Descrierile v7 sunt gata (1300). Vreau să [ce urmează: ex. corectăm problemele din probleme-catalog.txt /
> scriem cele 55 de duplicate canonice / reverificăm produsele sărite].

Reguli de reținut: repo public (fără secrete), fără force-push, fără SSH pe server, nu se schimbă textele legale,
poarta de pre-lansare sau codul fără acord; fără em-dash, diacritice corecte, fără „compară”, preț sau promoții în texte.
