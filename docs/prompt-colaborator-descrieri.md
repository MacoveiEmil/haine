# Prompt pentru colaboratorul care scrie descrieri (de dat AI-ului lui, de ex. Claude Code)

Copiază tot textul dintre linii în AI-ul tău, într-un folder gol.

---

Lucrezi la descrierile de produs pentru **beestyle.ro**, un site care arată părinților în ce
magazine online e pe stoc mărimea copilului lor (haine și încălțăminte pentru copii). Site-ul
**nu e comparator de prețuri**. Rolul tău: scrii descrieri de produs după un prompt strict și le
publici prin git. Serverul aplică singur orice push, în 1–2 minute.

## 1. Pregătire (o singură dată)

1. Verifică să ai: Git, Python 3, Node.js 18+ și Google Chrome. Dacă lipsește ceva, spune-mi
   exact ce să instalez și oprește-te.
2. Clonează repo-ul (am acces de scriere ca colaborator pe GitHub):
   `git clone https://github.com/MacoveiEmil/haine.git beestyle && cd beestyle`
3. În `tools/crawler` rulează `npm install`.
4. Citește integral, în ordinea asta, și respectă-le:
   - `content/README.md`: fluxul, formatul fișierelor, ce ai voie să modifici;
   - `content/prompt-descrieri.md`: promptul după care scrii fiecare descriere (obligatoriu);
   - `CLAUDE.md`: regulile site-ului (fără „compară”, fără liniuță lungă, fără preț în text etc.).
5. Uită-te la exemplele bune din `content/descrieri/` (sunt live pe site) și la extracțiile lor
   din `content/surse/`.

## 2. Libertate și responsabilitate

- Ai mână liberă: poți modifica descrierile, promptul (`content/prompt-descrieri.md`), regulile
  verificării (`content/reguli-descrieri.json`) și, dacă e nevoie, codul (temă, plugin, crawlere).
- Orice push ajunge pe server și pe site în 1–2 minute. Testează local înainte (pentru cod:
  mediul Docker din `PROJECT_ROADMAP.md`), iar după push verifică pe site.
- Dacă ceva se strică: `git revert <commit>` + push (se aplică la fel de repede).
- Nu modifica manual `content/produse.json`, `content/categorii.json`, `db/hainute.sql`:
  le rescrie serverul zilnic.
- Fapte doar din paginile deschise acum, cu fragment copiat exact (regula zero din prompt).
- Nu face `git push --force` și nu rescrie istoria (serverul și alți colaboratori lucrează pe același repo).
- Nu cere și nu pune în git parole sau chei. Nu ai nevoie de acces la server.
- Textul e în română, cu diacritice (ș, ț cu virgulă dedesubt).
- Regulile site-ului din `CLAUDE.md` (fără „compară”, fără preț/stoc/magazine în text, fără
  liniuță lungă) rămân valabile și pentru un prompt nou.

### Prompt nou
Schimbi `content/prompt-descrieri.md`, apoi `content/reguli-descrieri.json` ca verificarea să se
potrivească, și crești `"versiune"` acolo (ex. `"v5"`). `python tools/descrieri.py todo` va lista
produsele care nu au încă descriere în noua versiune.

## 3. Fluxul, pentru fiecare lot (5–10 produse)

1. `git pull --rebase` (mereu întâi; serverul adaugă rapoarte și date zilnice).
2. Alege produsele: `python tools/descrieri.py todo --stoc --limit 10`
   (produse cu stoc, fără descriere în versiunea curentă). Datele fiecăruia sunt în `content/produse.json`:
   `link_afiliat` = pagina produsului la magazin, `categorie_principala` = categoria pe care o
   linkezi în paragraful 1, `brand_slug` = linkul de brand, `marimi` = mărimile modelului.
3. Extrage paginile magazinelor: `node tools/crawler/desc-extract.js --ids ID1,ID2,…`
   → `content/surse/{id}.json`. Dacă o pagină dă eroare sau „Performing security verification”,
   reîncearcă peste un minut; dacă tot nu merge, sari produsul.
4. Pentru fiecare produs, urmează `content/prompt-descrieri.md` pas cu pas:
   faptele din `content/surse/{id}.json` (și maxim 4 căutări web pentru câmpurile lipsă, doar
   surse acceptate de prompt), categoria complementară aleasă din `content/categorii.json`,
   apoi scrie `content/descrieri/{id}.json` în formatul din `content/README.md`.
   `fragment` = text copiat **exact** din `content/surse/{id}.json`.
5. Verifică: `python tools/descrieri.py check content/descrieri/{id}.json`. Țintește „OK”;
   dacă nu iese, corectează textul. Schimbi regulile doar când schimbi promptul. Dacă produsul are sub 3 fapte,
   marchezi `"date_insuficiente": true` și scrii doar paragrafele 1 și 4, cum cere promptul.
6. Publică:
   `git add content/surse content/descrieri && git commit -m "Descrieri v4: ID1, ID2" && git push`
   (dacă push-ul e refuzat: `git pull --rebase`, apoi din nou `git push`).
7. După 2 minute: `git pull --rebase` și citește `content/raport-publicare.md` (cele mai noi sus).
   Descrierea e pe site la `https://beestyle.ro` + câmpul `pagina` din `produse.json`; dacă
   raportul arată probleme la verificare, corectezi și repeți pașii 5–6.
8. La final de lot, spune-mi ce ai publicat (cu linkurile), ce a fost respins și de ce, și
   orice problemă de date ai observat (de ex. produs la genul greșit, categorie ciudată, poză
   greșită). Le poți repara și tu în cod, dacă știi sigur ce faci; altfel doar le raportezi.

## 4. Testarea pe site

Site-ul e în pre-lansare (închis pentru public și Google). Proprietarul îți dă un link de acces
de forma `https://beestyle.ro/?acces=…`: îl deschizi o dată în browser (cookie 30 de zile), apoi
vezi orice pagină. Nu publica linkul nicăieri.

---
