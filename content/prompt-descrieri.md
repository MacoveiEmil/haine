# Prompt descrieri de produs (v7): beestyle.ro

Scrii descrierea unui singur produs (haine sau încălțăminte pentru copii) pentru beestyle.ro.
Site-ul arată părinților în ce magazine e pe stoc mărimea copilului. Nu e comparator de prețuri.

Textul se scrie în română, cu diacritice corecte (ș, ț cu virgulă dedesubt).

## Ce aduce v7

- **Vârsta nu mai are formulă fixă.** „Orientativ” apărea pe fiecare pagină, în aceeași frază. Vârsta rămâne
  aproximativă (așa e corect), dar o spui de fiecare dată altfel. Vezi punctul 5.
- **Cum vine pe copil.** O frază sau două despre croială și potrivire (cât de larg, până unde e lung,
  manșete, talie, calapod) și ce înseamnă asta pentru copil, doar din fapte. Vezi secțiunea dedicată.

## Ideea v6: strict pe conținut, liber pe formă

v4 și v5 fixau structura (ce stă în fiecare paragraf, câte puncte, ce frază la final). Rezultatul:
toate descrierile semănau între ele, lista nu era legată de text, iar fraza cu mărimile era identică
pe fiecare pagină. v6 fixează **ce trebuie să conțină** descrierea și lasă **forma** la alegerea ta:
scrii ca un om care cunoaște produsul, cu fraze legate între ele, diferite de la un produs la altul.

## Intrări (le iei din repo)

- `content/surse/{id}.json`: pagina magazinului, extrasă acum. **Singura sursă de fapte.**
- `content/produse.json`, produsul cu acest `id`: `titlu`, `brand`, `brand_slug`, `gen`, `tip`,
  `categorie_frunza` (sau `categorie_principala`), `marimi` (mărimile de pe site, din toate magazinele).
- `content/categorii.json`: categoriile existente (pentru linkul complementar, dacă îl pui).

## Regula zero: fapte doar din sursă

- Fiecare fapt din text apare în `content/surse/{id}.json`. Îl treci în `surse` cu fragmentul
  copiat **exact** de acolo (verificarea caută fragmentul literal în fișier).
- Fapt fără fragment = fapt care nu există. Nimic din memoria ta despre brand sau model.
- Ignori textul comercial al magazinului: prețuri, reduceri, coduri, livrare, retur, recenzii.
- Sub 3 fapte concrete despre model: `"date_insuficiente": true`, scrii doar un paragraf scurt
  cu ce e produsul și mărimile.

Magazinele amestecă fapte cu promisiuni. Preiei faptul, nu promisiunea:

| Pe pagină scrie | Scrii |
|---|---|
| „talpa din spumă oferă o senzație mai moale și amortizare” | talpă din spumă |
| „interior textil care favorizează circulația aerului” | interior textil |
| „profil înalt care stabilizează glezna” | profil înalt (gleznă înaltă) |
| „talpă din cauciuc care asigură aderență” | talpă din cauciuc |

Funcțiile tehnice declarate concret se păstrează, spuse simplu: „membrană impermeabilă”,
„coloană de apă de 5000 mm”, „cusături lipite”, „elemente reflectorizante”, „lumini în talpă”.

## Ce TREBUIE să conțină (verificat automat)

1. **Brandul și modelul** (numele modelului din titlu, ex. FADINLIGHT, LUSH; dacă nu are nume,
   codul), în prima frază.
2. **Linkul spre categoria produsului** (`categorie_frunza`), în primul paragraf, pe tipul de produs,
   cu genul în ancoră: „adidași pentru fete”, „geacă pentru băieți”, „salopetă pentru bebeluși”,
   „ghete unisex”. Ancora conține obligatoriu „pentru fete/băieți/bebeluși” sau „unisex”.
3. **Linkul de brand** (`brand_slug`), pe prima apariție firească a numelui brandului.
4. **Culoarea** din titlu.
5. **Mărimile din `produse.json`** (cea mai mică și cea mai mare, exact ca în listă) și **vârsta
   aproximativă** (Anexa). Vârsta e mereu aproximativă, dar o spui natural și de fiecare dată altfel:
   „cam 4-11 ani”, „copiii de pe la 4 până pe la 11 ani”, „în general între 4 și 11 ani”,
   „de obicei pentru 8-16 ani”, „aproximativ 1-4 ani”. „Orientativ” e doar una dintre variante: îl
   folosești rar și cel mult o dată. Verificarea cere vârsta și o formulare aproximativă
   (`varsta_formulari` din reguli). Folosești `marimi` din `produse.json`, nu mărimile de la un singur magazin.
6. **Cum vine pe copil**, când sursa dă date de croială sau potrivire (vezi secțiunea dedicată).
7. **Cel puțin 3 fapte** din sursă (material, izolație, talpă, închidere, tehnologii, detalii).
8. **Pentru ce e bun produsul**: vreme, anotimp sau activitate, doar derivat din fapte (vezi „Utilizări”).
9. Opțional: un link spre o categorie complementară (alt tip de produs, același gen), doar când
   există o legătură reală (vezi „Complementar”).

## Forma: liberă, dar cu fir logic

- **Lungime: 80-240 de cuvinte.** Primul paragraf are 25-66 de cuvinte și e un paragraf adevărat,
  de 2-3 fraze, nu o etichetă. Scrii mai mult acolo unde ai fapte, nu umplutură.
- **Lista e opțională.** O folosești când ai 3 sau mai multe detalii de construcție care se citesc mai
  ușor ca listă. Dacă o folosești:
  - o **introduci cu o frază care o leagă de ce ai spus înainte** și se termină cu două puncte. Fraza
    spune de ce contează detaliile care urmează, pentru produsul ăsta. Bune: „Dimineața, când copilul
    se încalță singur, contează câteva detalii:”, „Pe pârtie, zăpada intră de obicei pe la încheieturi
    și pe la spate, iar acolo geaca are protecții separate:”. Proaste: „Caracteristici:”,
    „Iată detaliile:”, „Modelul are:”;
  - fiecare punct dezvoltă ideea din fraza de introducere (`<li><strong>Element</strong>: …</li>`),
    nu e o specificație aruncată. Efectul practic îl scrii când e concret și sigur (arici → se încalță
    fără ajutor; branț detașabil → se scoate la uscat);
  - nu repeți în listă ce ai spus deja în text.
- **Mărimile și vârsta nu au loc fix.** Pot sta în primul paragraf, în ultimul sau legate de alt
  detaliu (de exemplu închiderea cu arici la copiii mici). Formulezi de fiecare dată altfel, nu după
  un tipar. Verificarea compară descrierile între ele și respinge formulările care se repetă.
- **Fiecare frază are legătură cu cea dinainte.** Citește textul cu voce tare: dacă o frază ar
  putea fi mutată pe orice alt produs, o rescrii cu un detaliu al produsului ăstuia.

## Cum vine pe copil (croială și potrivire)

Părinții caută și după formă, nu doar după tip: „geacă lungă”, „blugi largi”, „pantofi pentru picior lat”.
Exemplu bun (geacă): „Croiala e relaxed fit, cu lungimea până la șolduri.” Spune pe scurt cum arată și
cum stă produsul. Nu e o frază fixă: o formulezi după produs, o legi de restul textului și o pui unde
are sens (în primul paragraf, lângă mărimi, după listă).

Ce iei din sursă, când există:
- **haine**: croiala (regulară, relaxed, lejeră, oversize, slim, mulată), lungimea (până la talie, la
  șolduri, la mijlocul coapsei, la genunchi; spate alungit), talia (elastică, cu șnur, reglabilă),
  manșetele și tivul (elastice, cu bordură, cu orificiu pentru deget), elastanul din compoziție, gluga reglabilă;
- **încălțăminte**: profilul (scurt, înalt, gleznă înaltă), vârful și cutia degetelor (rotund, lat),
  închiderea reglabilă (arici, șiret elastic), branțul detașabil, tureacul.

Ce poți spune pe baza lor (doar când faptul e în sursă):
- croială relaxed / lejeră / oversize → are loc de un strat mai gros dedesubt și vine comod și copiilor mai plinuți;
- slim / mulată / cu elastan → stă aproape de corp; la copiii slabi nu atârnă, peste haine groase e strâmtă;
- talie elastică, cu șnur sau reglabilă → se strânge la copiii mai slabi, fără curea;
- lungime până la șolduri sau coapse, spate alungit → acoperă spatele când copilul se apleacă sau stă jos;
- manșete și tiv elastice → strâng la încheieturi și jos, ca geaca să nu stea largă;
- vârf lat, cutie lată a degetelor → loc pentru degete, potrivit și la piciorul mai lat;
- arici sau șiret elastic → se reglează pe picior îngust sau lat;
- branț detașabil → piciorul copilului se poate măsura direct pe branț.

Fără date de croială în sursă, nu inventezi („vine mare”, „vine mic”, „croială generoasă”) și sari peste.
Nu recomanzi altă mărime decât cea obișnuită. O singură idee, una-două fraze: nu o listă de măsurători.

## Utilizări permise (doar cu faptul în sursă)

- impermeabil, membrană, cusături lipite, coloană de apă → ploaie, zăpadă, bălți
- izolat, umplutură, puf → frig, iarnă
- plasă, sandale, bumbac subțire → zile calde, vară
- elemente reflectorizante, lumini în talpă → drumuri pe întuneric
- arici, șiret elastic → se încalță fără ajutor
- geacă de schi declarată → pârtie, zăpadă
- magazinul scrie explicit „zi de zi”, „casual” → purtat zilnic, la grădiniță sau la școală

Fără fapt, fără utilizare. „Bun pentru ploaie” fără impermeabilitate declarată = interzis.
Dacă protecția acoperă doar o parte (ex. doar talpa are membrană), spui exact atât.

## Complementar (opțional)

Doar când e o legătură reală: o limită declarată a produsului (plasă, neizolat, sandale, fără glugă)
sau piese care se poartă evident împreună (geacă de schi și mănuși). Linkul duce spre o categorie
din `content/categorii.json`, alta decât a produsului, de același gen. Fără legătură reală, fără link.

## Limbaj

Ton: cineva care cunoaște produsul și îi explică unui părinte, la obiect. Fraze legate, acord corect,
fără reclamă. Text neutru ca gen: „copilul”, „copiii”; genul apare doar în ancora categoriei.

Interzis:
- liniuța lungă (em dash), exclamațiile, întrebările, persoana I plural
- „compară”, „comparator”, preț, reducere, ofertă, stoc, nume de magazine
- laudă și superlative: cel mai bun, perfect, ideal, premium, must-have, alegerea potrivită, la îndemână,
  un plus, un avantaj, pentru părinții atenți
- promisiunile magazinului: respiră, aerul circulă, aderență, amortizare, stabilitate, ortopedic,
  susține piciorul, plăcut la contactul cu pielea, libertate de mișcare
- formule-șablon: „iată”, „caracteristici:”, „mărimile merg de la”, „îi fac o pereche”, „o fac o piesă”,
  „face parte din”, „se încadrează”, „confort și stil”, „face diferența”, „se simte”
- etape de școală (grupa mică, clasele I-IV, gimnaziu), țara de fabricație, dimensiuni în cm ale produsului

## Exemple

Exemplele din `content/descrieri/` marcate `"versiune": "v6"` arată calitatea cerută. **Nu le copia
frazele:** fiecare produs are alt fir logic. Verificarea respinge formulările repetate între descrieri.

## Output: `content/descrieri/{id}.json`

```json
{
 "id": 8566,
 "versiune": "v7",
 "descriere_html": "<p>…</p><p>…:</p><ul><li><strong>…</strong>: …</li></ul><p>…</p>",
 "surse": [ { "fapt": "plasă ușoară", "url": "answear.ro/p/…", "fragment": "text copiat EXACT din surse/{id}.json" } ],
 "specificatii_tehnice": { "Model": "", "Material": "", "Caracteristici": "", "Cod produs": "" },
 "categorie_complementara": { "slug": "/categorie/ghete-cizme/", "motiv": "…" },
 "varsta_orientativa": "4-11 ani",
 "date_insuficiente": false,
 "confidence_notes": []
}
```

`categorie_complementara` e `null` dacă nu ai link complementar. În `confidence_notes` notezi
problemele de date (gen diferit la magazin, mărimi diferite între magazin și site, reclamă omisă).

## Anexă: mărime → vârstă (vârsta e mereu aproximativă, formulată variat)

Îmbrăcăminte (cm): 86 = 1 an | 92 = 2 | 98 = 3 | 104 = 4 | 110 = 5 | 116 = 6 | 122 = 7 | 128 = 8 |
134 = 9 | 140 = 10 | 146 = 11 | 152 = 12 | 158 = 13 | 164 = 14 | 170 = 15 | 176 = 16.
Mărimi din 10 în 10 (90, 100, 120…): se aproximează la cea mai apropiată (90 = 2 ani).

Încălțăminte (EU): 19-22 = 1-2 ani | 23-25 = 2-3 | 26-27 = 3-4 | 28-29 = 4-5 | 30-31 = 6-7 |
32-33 = 8-9 | 34-35 = 10-11 | 36 și peste = 12 ani și peste.

Intervalul de vârstă = vârsta celei mai mici mărimi până la vârsta celei mai mari. Dacă cea mai mare
mărime e 36+ la încălțăminte, scrii „de la X ani în sus”.
