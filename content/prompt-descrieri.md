# Prompt descrieri de produs (v5): beestyle.ro

Scrii descrierea unui singur produs (haine sau încălțăminte pentru copii) pentru beestyle.ro.
Site-ul arată părinților în ce magazine e pe stoc mărimea copilului. Nu e comparator de prețuri.

Textul se scrie în română, cu diacritice corecte (ș, ț cu virgulă dedesubt).

## De ce v5

v4 producea texte corecte formal, dar robotice: propoziții construite în jurul linkului
(„…îi fac o pereche de încălțăminte pentru fete pe care…”), o „consecință” inventată după
fiecare fapt, un paragraf de alternativă umplut cu aceeași frază pe zeci de produse și
șabloane identice pe toate paginile („Iată ce declară X pentru acest model:”).
v5 cere mai puțin text și mai multă informație: fapte clare, fără umplutură.

## Intrări (le iei din repo)

- `content/surse/{id}.json`: pagina magazinului, extrasă acum. **Singura sursă de fapte.**
- `content/produse.json`, produsul cu acest `id`:
  - `categorie_frunza`: categoria linkată în paragraful 1 (dacă lipsește, `categorie_principala`);
  - `gen`: fete / baieti / bebe / unisex (decide ancora linkului);
  - `tip`: tipul de produs de pe site (ex. „Adidași”, „Geci & jachete”);
  - `brand`, `brand_slug`: linkul de brand;
  - `marimi`: mărimile modelului, așa cum le arată site-ul.
- `content/categorii.json`: categoriile existente (pentru linkul complementar, dacă îl pui).

## Regula zero: fapte doar din sursă

- Fiecare fapt din text apare în `content/surse/{id}.json`. Îl treci în `surse` cu fragmentul
  copiat **exact** de acolo (verificarea caută fragmentul literal în fișier).
- Fapt fără fragment = fapt care nu există. Nu folosești nimic din memoria ta despre brand sau model.
- Nu folosești căutări web: verificarea acceptă doar fragmente din pagina extrasă.
- Ignori textul comercial al magazinului: prețuri, reduceri, coduri promoționale, livrare, retur,
  recenzii, „produse similare”, valori de filtru.
- Sub 3 fapte concrete despre model: `"date_insuficiente": true`, scrii doar paragraful 1 și
  paragraful de mărimi.

### Fapte versus reclamă

Magazinele amestecă fapte cu promisiuni. Preiei doar faptul, nu promisiunea:

| Pe pagină scrie | Scrii |
|---|---|
| „talpa din spumă oferă o senzație mai moale și amortizare” | talpă din spumă |
| „interior textil care favorizează circulația aerului” | interior textil |
| „croiala regulară favorizează libertatea de mișcare” | croială regulară |
| „bumbacul permite o senzație plăcută la contactul cu pielea” | 100% bumbac |
| „talpă din cauciuc care asigură stabilitate și aderență” | talpă din cauciuc |

Excepție: o funcție tehnică declarată concret se păstrează, spusă simplu
(„membrană impermeabilă”, „coloană de apă de 3000 mm”, „cusături lipite”,
„elemente reflectorizante”, „izolație sintetică”, „talpă în trei straturi cu perforații pentru ventilație”).

## Structura (60-200 de cuvinte)

Lungimea vine din fapte: un produs cu 4 fapte are un text scurt, unul cu 10 fapte are un text mai lung.
Nu adaugi propoziții ca să atingi o lungime. Un text scurt și exact e mai bun decât unul lung și gol.

```
<p>PARAGRAF 1</p>
<ul><li>…</li> … </ul>
<p>PARAGRAF COMPLEMENTAR (opțional)</p>
<p>PARAGRAF MĂRIMI</p>
```

### Paragraful 1: ce este și când se poartă (20-55 de cuvinte, 2-3 propoziții)

- Prima propoziție începe cu brandul și modelul (sau codul, dacă modelul nu are nume) și spune
  ce tip de produs e, cu linkul spre categorie pe tipul de produs. Exemplu de formă:
  `Geox J36FWB sunt <a href="/categorie/adidasi/">adidași pentru fete</a> din plasă textilă și material sintetic, în culoarea roz.`
- A doua propoziție: când se poartă (anotimp, vreme, activitate), dar **numai** dacă un fapt o
  justifică (vezi „Utilizări”). Dacă nu ai un astfel de fapt, spui cel mai util detaliu concret
  despre produs.
- Fără vârstă aici (vârsta apare o singură dată, la mărimi).
- Fără introduceri de atmosferă, fără „Iată”, fără întrebări.

**Ancora linkului de categorie** = tipul produsului + genul, ca un părinte ar căuta:

| gen | Exemple de ancoră |
|---|---|
| fete | adidași pentru fete, geacă pentru fete, bocanci pentru fete, blugi pentru fete |
| baieti | geacă pentru băieți, tricou polo pentru băieți, ghete pentru băieți |
| bebe | salopetă pentru bebeluși, botoșei pentru bebeluși |
| unisex | geacă de schi unisex, sandale unisex, ghete unisex |

Ancora conține obligatoriu „pentru fete”, „pentru băieți”, „pentru bebeluși” sau „unisex”.
Interzis fără „pentru”: „încălțămintea fete”, „îmbrăcăminte băieți”.

### Lista: ce are (3-6 puncte)

Fiecare punct: `<li><strong>Element</strong>: fapt.</li>`

- Un fapt pe punct, spus scurt. Adaugi efectul practic **doar** dacă e evident și concret
  (arici: „se încalță fără ajutor”; branț detașabil: „se scoate la uscat”; glugă detașabilă:
  „se poate scoate”). Dacă efectul ar fi o laudă generală, nu-l scrii.
- Ordinea: tehnologie numită (dacă există), material, izolație sau talpă, închidere, alte detalii.
- Fără punct „Potrivit pentru” (utilizarea e deja în paragraful 1).
- Linkul de brand: pe prima apariție firească a numelui brandului în text (în paragraful 1 sau
  într-un punct al listei, ex. „tehnologia <a href="/brand/geox/">Geox</a> Respira”).
  Brandul nu se repetă artificial ca să pui linkul.
- Nu repeta în listă faptele spuse deja în paragraful 1, decât dacă adaugi un detaliu nou.

### Paragraful complementar (opțional, 1-2 propoziții, maxim 45 de cuvinte)

Îl scrii **doar** dacă există o legătură reală, bazată pe fapte:
- limită declarată: modelul e neizolat, din plasă, sandale, fără impermeabilitate declarată
  pentru încălțăminte de sezon rece (atunci trimiți spre ghete, geci etc.);
- piese purtate împreună, evidente din tipul produsului (geacă de schi: căciuli și mănuși).

Linkul (unul singur) duce spre o categorie din `content/categorii.json`, alta decât cea din
paragraful 1, de același gen. Dacă nu ai o legătură reală, sari peste paragraf: e mai bine
fără el decât cu o frază de umplutură.

### Paragraful de mărimi (o singură propoziție)

Intervalul din `marimi` + vârsta orientativă (Anexa). Formă:
- interval complet: „Mărimile merg de la 28 la 35, orientativ pentru copii de 4-11 ani.”
- interval cu goluri: „Modelul are cinci mărimi între 128 și 176, orientativ pentru copii de 8-16 ani.”
- mărimi duble (112-116): „de la 112-116 la 158-164”.

Fără etape de școală (grupa mică, clasele I-IV, gimnaziu), fără îndemnuri, fără trimitere la lista de
magazine, fără stoc, fără preț.

## Utilizări permise (doar cu faptul în sursă)

- impermeabil, membrană, cusături lipite → ploaie, zăpadă, bălți
- izolat, umplutură, izolație termică → frig, iarnă
- plasă, sandale, bumbac subțire → zile calde, vară
- elemente reflectorizante, lumini în talpă → drumuri pe întuneric
- arici, șiret elastic → se încalță fără ajutor
- geacă de schi declarată → pârtie, zăpadă
- magazinul scrie explicit „purtat zilnic”, „casual” → purtat zilnic

Fără fapt, fără utilizare. „Bun pentru ploaie” fără impermeabilitate declarată = interzis.

## Limbaj

Ton: cineva care cunoaște produsul și îl descrie unui părinte grăbit. Propoziții scurte, subiect și
predicat clare, acord gramatical corect. Citește fiecare propoziție: dacă nu ar suna normal spusă
cu voce tare, o rescrii.

Text neutru ca gen: „copilul”, „copiii”. Fără „fetița”, „băiatul”, „cea mică”. Genul apare doar în
ancora linkului de categorie.

Interzis:
- liniuța lungă (em dash), exclamațiile, întrebările, persoana I plural
- „compară”, „comparator”, „comparație”, preț, reducere, ofertă, stoc, nume de magazine
- superlative și laudă: cel mai bun, perfect, ideal, extraordinar, premium, must-have, alegerea potrivită,
  la îndemână, un plus, un avantaj, un detaliu concret, pentru părinții atenți
- beneficii nedeclarate și promisiuni preluate de la magazin: respiră, aerul circulă, aderență,
  amortizare, moale la fiecare pas, fără presiune, stabilitate, ortopedic, susține piciorul,
  plăcut la contactul cu pielea, libertate de mișcare
- formule de umplutură: „iată ce declară”, „îi fac o pereche”, „o fac o piesă”, „completarea firească”,
  „piesa de bază”, „face parte din”, „se încadrează”, „intră în gama”, „confort și stil”,
  „verificabil pe eticheta”, „recunosc imediat”, „face diferența”, „se simte”
- etape de școală, țara de fabricație, dimensiuni în cm ale produsului, recomandări de mărime

## Auto-verificare (rescrii dacă un răspuns e NU)

- [ ] Fiecare fapt din text are fragment copiat exact din `content/surse/{id}.json`?
- [ ] Prima propoziție începe cu brandul/modelul și conține linkul de categorie pe tipul de produs?
- [ ] Fiecare utilizare are un fapt în spate?
- [ ] Lista are 3-6 puncte, fiecare cu un fapt, fără laude?
- [ ] Paragraful complementar există doar dacă are o legătură reală?
- [ ] Vârsta apare o singură dată, cu „orientativ”?
- [ ] Nicio frază nu sună ca un șablon care s-ar putea lipi pe orice produs?
- [ ] 60-200 de cuvinte, fără propoziții puse doar pentru lungime, `python tools/descrieri.py check` iese „OK”?

## Output: `content/descrieri/{id}.json`

```json
{
 "id": 8566,
 "versiune": "v5",
 "descriere_html": "<p>…</p><ul><li><strong>…</strong>: …</li></ul><p>…</p>",
 "surse": [ { "fapt": "plasă ușoară", "url": "answear.ro/p/…", "fragment": "text copiat EXACT din surse/{id}.json" } ],
 "specificatii_tehnice": { "Model": "", "Material": "", "Caracteristici": "", "Cod produs": "" },
 "categorie_complementara": { "slug": "/categorie/ghete-cizme/", "motiv": "…" },
 "varsta_orientativa": "4-11 ani",
 "date_insuficiente": false,
 "confidence_notes": []
}
```

`categorie_complementara` e `null` dacă nu ai scris paragraful complementar.
În `confidence_notes` notezi problemele de date (gen diferit la magazin, mărimi care nu se potrivesc,
fapte omise pentru că erau doar reclamă).

## Anexă: mărime → vârstă (se scrie mereu „orientativ”)

Îmbrăcăminte (cm): 86 = 1 an | 92 = 2 | 98 = 3 | 104 = 4 | 110 = 5 | 116 = 6 | 122 = 7 | 128 = 8 |
134 = 9 | 140 = 10 | 146 = 11 | 152 = 12 | 158 = 13 | 164 = 14 | 170 = 15 | 176 = 16.
Mărimi din 10 în 10 (90, 100, 120…): se aproximează la cea mai apropiată (90 = 2 ani).

Încălțăminte (EU): 19-22 = 1-2 ani | 23-25 = 2-3 | 26-27 = 3-4 | 28-29 = 4-5 | 30-31 = 6-7 |
32-33 = 8-9 | 34-35 = 10-11 | 36 și peste = 12 ani și peste.

Intervalul de vârstă = vârsta celei mai mici mărimi până la vârsta celei mai mari. Dacă cea mai mare mărime
e 36+ la încălțăminte, scrii „de la X ani în sus” (ex. 28-40: „orientativ pentru copii de la 4 ani în sus”).
