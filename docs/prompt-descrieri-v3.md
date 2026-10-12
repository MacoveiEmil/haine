# Prompt descrieri de produs (v3), hainute.ro

Primit de la proprietar pe 2026-10-12. Test pe 10 produse: `docs/descrieri-v3-test.json`
(extracție: `tools/crawler/desc-extract.js`, verificare automată: `tools/check-descrieri-v3.py`).

```text
INPUT: link_afiliat: {{url}}

==================================================
PASUL 1: DESCHIDE SI EXTRAGE DE PE PAGINA MERCHANT
==================================================

Deschide URL-ul primit ca input (link_afiliat). Pagina merchant (Answear / Fashion Days / Sportisimo / various-brands) este sursa de adevar pentru acest produs. Extrage tot ce gasesti explicit pe pagina:

- brand
- model / cod produs (MPN sau echivalent afisat de magazin)
- tip produs (sneakers, geaca, salopeta, cizme etc)
- categorie asa cum o numeste magazinul
- gen (baieti / fete / unisex), daca e specificat
- interval de varsta recomandat, daca e afisat
- culoare
- material / compozitie, daca e afisat
- talpa, inchidere, croi, daca sunt afisate (pentru incaltaminte)
- detalii de constructie: gluga detasabila, mansete, buzunare, cusaturi lipite, umplutura, captuseala, benzi reflectorizante
- certificari sau tehnologii numite explicit (bluesign, Therma-FIT, GORE-TEX, REPREVE etc)
- marimile disponibile, asa cum apar (lista exacta, nu rotunji)
- imagine principala

Marcheaza explicit fiecare camp ca EXTRAS (gasit pe pagina) sau LIPSA.

ATENTIE LA FILTRE: valorile afisate ca interval de filtru al magazinului (ex: "talpa 2-4 cm", "inaltime toc 0-3 cm") NU sunt fapte despre model. Le ignori.

PRAG MINIM DE FAPTE
Numara cate fapte concrete despre acest model ai extras (material, umplutura, talpa, inchidere, gluga, mansete, buzunare, cusaturi, tehnologie, certificare, captuseala, benzi reflectorizante, interval de varsta).

- 5 sau mai multe fapte -> scrii 4 paragrafe
- 3 sau 4 fapte -> scrii 3 paragrafe
- sub 3 fapte -> scrii 2 paragrafe si marchezi produsul in output cu "date_insuficiente": true

Nu compensezi lipsa de fapte cu propozitii mai lungi. Un text scurt si concret e preferabil unui text lung si gol.

Nu trece la pasul 2 pentru campuri deja EXTRASE. Cautarea web e doar pentru campurile LIPSA.

==================================================
PASUL 2: COMPLETEAZA DOAR CAMPURILE LIPSA, PRIN CAUTARE WEB
==================================================

Pentru fiecare camp marcat LIPSA la pasul 1 (de regula: material/compozitie, talpa, interval de varsta), cauta:

"{brand} {model}" + termenul lipsa
exemplu: "Geox J36LAA material" sau "Reima Alaniva compozitie"

SURSE ACCEPTATE, IN ORDINE DE PRIORITATE:

1. Site-ul oficial al brandului, pagina ACESTUI model -> incredere maxima
2. Alt magazin mare care vinde acelasi model (Answear, Zalando, ABOUT YOU, ePantofi, Modivo) -> DOAR daca codul de model coincide EXACT cu cel extras la pasul 1
3. Agregator de moda (GLAMI) -> doar ca confirmare a ce ai deja, niciodata sursa unica
4. Bloguri, forumuri, recenzii -> NU se folosesc ca sursa de fapt

REGULA DE COROBORARE: informatia gasita intr-o singura sursa secundara (categoria 2 sau mai slaba) se OMITE din text si se noteaza in confidence_notes ca "sursa unica, neconfirmata".

Daca doua surse se contrazic (ex: "piele naturala" vs "piele ecologica"), campul se marcheaza CONTRADICTORY in confidence_notes si se omite din text.

Daca nu gasesti nimic, campul ramane LIPSA. Nu inventezi.

LIMITA: maxim 3 interogari de cautare per produs.

==================================================
PASUL 3: GENUL, CATEGORIA, BRANDUL, ENTITATILE DE CAUTARE
==================================================

--- 3.1 GENUL TEXTULUI, SE FIXEAZA O SINGURA DATA ---

Genul textului vine de pe pagina merchant. Decizia se ia acum si NU se mai schimba nicaieri in text.

- gen = baieti -> forme masculine: baiatul, cel mic, copilul. NU "fetita", "ea".
- gen = fete -> forme feminine: fetita, cea mica, copila. NU "cel mic", "baiatul", "el".
- gen = unisex sau nespecificat -> forme neutre: copilul, cel mic, piciorul copilului. NU "fetita", NU "baiatul". Textul ramane neutru chiar daca slug-ul de categorie e de baieti sau fete.
- categoria bebe -> forme neutre.

REGULA DURA: intr-o descriere nu pot coexista referinte de gen diferite.

--- 3.2 CATEGORIA NIVEL 2, ANCORA SI SLUG ---

Slug-ul de categorie NU se deduce. Se ia din categoria produsului pe site (camp din feed).

Slug-uri valide (singurele care exista pe site):

| Slug                            | Ancora               |
|---------------------------------|----------------------|
| /categorie/incaltaminte-baieti/ | incaltaminte baieti  |
| /categorie/incaltaminte-fete/   | incaltaminte fete    |
| /categorie/imbracaminte-baieti/ | imbracaminte baieti  |
| /categorie/imbracaminte-fete/   | imbracaminte fete    |
| /categorie/imbracaminte-bebe/   | imbracaminte bebe    |

VERIFICARE: slug-ul trebuie sa fie unul din tabel. Orice alt slug invalideaza output-ul.
VERIFICARE 2: ancora corespunde slug-ului. Ancora poate fi flexata gramatical (incaltamintea pentru fete, imbracamintea pentru bebe), dar se refera la aceeasi pagina.

--- 3.3 BRAND, PAGINA DE BRAND ---

Ancora = numele brandului asa cum apare oficial (Geox, adidas cu litera mica, DD Step, 4F, ALPINE PRO).
Slug tinta: /brand/{brand-slug}/

--- 3.4 ENTITATI DE CAUTARE ---

Textul trebuie sa contina, natural, entitatile pe care un parinte le cauta:

1. varsta in ani, derivata din marimi cu Anexa C, formulata mereu ca "orientativ" (ex: "acopera orientativ copiii de 4-10 ani")
2. sezonul, doar daca rezulta clar din tipul produsului sau de pe pagina
3. culoarea ca adjectiv langa tipul produsului ("ghetele maro", "geaca bleumarin")
4. atributele de cautare EXTRASE: fara siret, cu arici, impermeabil, captusit, gluga detasabila
5. o ocazie concreta: gradinita, scoala, sport, zapada, oras

Minim 3 din 5 in descriere. Fiecare apare maxim o data. Fara insiruiri de keyword-uri.

==================================================
PASUL 4: VARIATIA, APOI TEXTUL
==================================================

--- 4.1 SEED DE VARIATIE ---

seed = ultima cifra din cod_produs.
Daca cod_produs nu contine cifre: seed = numarul de litere din numele modelului, modulo 10.
Daca in lot terminatiile codurilor sunt ne-uniforme (multe se termina in 0): seed = (suma cifrelor din cod_produs + numarul de litere din model) modulo 10.

DECIZIA A, tipul de deschidere al paragrafului 1 (prima propozitie):

0 -> situatia concreta de folosire (drum spre gradinita, ore in parc, teren ud, sala de sport), apoi produsul
1 -> numele complet al produsului si tipul lui, apoi ce rezolva
2 -> o caracteristica fizica extrasa (material, umplutura, talpa), apoi produsul
3 -> profilul copilului (varsta, cat de activ e), apoi produsul
4 -> vremea sau anotimpul pentru care e facut, apoi produsul
5 -> contrastul dintre doua utilizari (zi de scoala si weekend, curte si drumetie), apoi produsul
6 -> brandul si modelul, apoi destinatia lui
7 -> problema pe care o rezolva (picioare ude, frig la incheieturi, incaltat greu dimineata), apoi produsul
8 -> un detaliu de constructie extras (gluga detasabila, arici, cusaturi lipite), apoi contextul
9 -> intervalul de varsta sau marimile, apoi produsul

Sunt descrieri de structura, nu texte de copiat.

DECIZIA B, pozitia interlinkurilor:

- seed 0, 3, 6, 9 -> link categorie in propozitia 2 din paragraful 1; link brand in ultima propozitie a paragrafului de brand
- seed 1, 4, 7 -> link categorie in ultima propozitie din paragraful 1; link brand in prima propozitie a paragrafului de brand
- seed 2, 5, 8 -> link categorie in prima propozitie din paragraful 1; link brand la mijlocul paragrafului de brand

Daca paragraful de brand nu se scrie, linkul de brand se pune natural in paragraful 1 sau 2.

DECIZIA C, structura propozitiei cu linkul de categorie:

index_pool = (suma cifrelor din cod_produs + numarul de litere din model) modulo 50.
Folosesti structura cu acest index din Anexa D. Adaptezi flexiunea, completezi cu fapte reale ale produsului. Nu copiezi literal.

--- 4.2 CINE CITESTE ---

O mama sau un tata care decide rapid daca produsul e alegerea buna pentru copilul lui. Vorbeste-i direct, cald, ca un sfat de la cineva care intelege ce conteaza: confortul copilului, cat de usor e de folosit zi de zi, daca merita.

Fara ton de fisa tehnica in text narativ. Fara ton de reclama.

--- 4.3 STRUCTURA, 180-260 CUVINTE TOTAL ---

PARAGRAF 1, prezentare si potrivire (45-70 cuvinte)
Ce este produsul, pentru cine, ce rezolva concret. Deschiderea respecta DECIZIA A. Linkul de categorie respecta DECIZIA B si DECIZIA C.
OBLIGATORIU: cel putin un fapt extras specific acestui model (materialul numit, umplutura, inchiderea, gluga detasabila, tehnologia numita, intervalul de varsta).

PARAGRAF 2, constructie si folosire zilnica (55-80 cuvinte)
Ce ofera concret produsul in folosirea de zi cu zi: usor de incaltat singur, se spala usor, se usuca repede. Fiecare caracteristica extrasa e legata de o consecinta practica. DOAR fapte extrase sau validate.

PARAGRAF 3, brand si incredere (35-55 cuvinte)
Se scrie DOAR daca ai fapte de brand confirmate PE ACEST MODEL (tehnologie proprie al carei nume apare pe pagina modelului, certificare, material). Fara generalitati de tip "brand de renume". Altfel se sare.

PARAGRAF 4, marimi si varsta (30-50 cuvinte)
Se scrie doar daca ai date reale despre marimi. Spui intervalul modelului (ex: "de la 28 la 35") si varsta orientativa din Anexa C.
Fara nume de magazin, fara numar de magazine, fara stoc, fara "acum", fara marimi epuizate, fara pret.
Nu recomanzi marime mai mare sau mai mica decat daca e confirmat explicit de brand.
Inchiderea cu trimitere la lista de magazine e OPTIONALA:
- seed par -> o singura propozitie din Anexa E, varianta = seed, reformulata
- seed impar -> fara trimitere la lista

--- 4.4 SPECIFICATII TEHNICE (NU intra in descriere) ---

Merg separat, in tabelul "Specificatii tehnice" al paginii. Ton factual, fara adjective. O linie exista doar daca ai date EXTRASE sau VALIDATE. Fara "N/A" sau "nespecificat".

- Model
- Material
- Caracteristici (inchidere, talpa, umplutura, gluga etc)
- Cod produs

==================================================
LISTA NEAGRA, FORMULE INTERZISE
==================================================

Daca una apare in output, output-ul se rescrie.

INTRODUCEREA LINKULUI DE CATEGORIE:
"Intra in gama de ...", "Face parte din ...", "Fac parte din ...", "Se incadreaza in ...", "Apartine gamei ...", "Este inclus in categoria ...", "Il gasesti in sectiunea ...", orice propozitie al carei singur rol este sa gazduiasca linkul.

Test: daca stergi linkul si propozitia ramasa nu mai spune nimic despre produs, propozitia e gresita.

INCHEIERI:
"E o alegere solida din gama ...", "E o alegere buna pentru ...", "pentru un copil care nu sta locului", "pentru copiii care nu stau o clipa locului", "E o {produs} practica pentru ...", "Sunt genul de {produs} pe care ..."

DESCHIDERI:
"{Produs} e gandita pentru ...", "{Produs} sunt facuti pentru ...", "{Produs} e o alegere calda ...", "{Produs} este perfect pentru ..."

CLISEE:
"tine de cald fara sa fie greoaie", "pe cat de usoara, pe atat de calduroasa", "incalzeste fara sa adauge volum", "fara sa limiteze miscarea", "se asorteaza usor cu restul hainelor", "confort si stil", "un must-have in garderoba", "nu va dezamagi", "ore in sir"

COMPARATOR (nu suntem comparator):
"compara", "comparator", "comparatie", "cel mai bun pret". Formularea corecta: "vezi marimile disponibile", "disponibil in aceste magazine".

REGULI GENERALE DE LIMBAJ:
- fara em dash, niciodata
- fara superlative nesustinute: cel mai bun, perfect, ideal, extraordinar, premium (daca nu e categorie de pret reala), must-have, revolutionar
- fara exclamatii
- fara persoana intai plural ("va oferim", "recomandam")
- fara intrebari retorice
- fara "in concluzie", "asadar", "in plus", "de asemenea" ca deschideri de propozitie

==================================================
REGULI ANTI-HALUCINATIE, OBLIGATORII
==================================================

- Folosesti DOAR fapte din pasul 1 sau din pasul 2 (validate, fara contradictie).
- Niciodata nu inventezi: tehnologii, beneficii medicale sau ortopedice, impermeabilitate, respirabilitate, lungime interioara in cm, recomandare de marime, tara de fabricatie, compozitie in procente neconfirmata, gramaj de umplutura.
- Nu atribui beneficii de performanta neafisate: aderenta, amortizare, rezistenta la uzura, izolare termica.
- Nu transformi filtre de magazin in fapte (ex: "talpa 2-4 cm"). Daca valoarea e un interval de filtru, o omiti.
- Tehnologiile cu nume propriu (Respira, Therma-FIT, BIONIC-FINISH ECO, REPREVE, bluesign, GORE-TEX) se mentioneaza DOAR daca numele lor apare explicit pe pagina merchant sau pe pagina oficiala a ACESTUI model. Nu extrapolezi de la brand la model.
- Marimile: daca lista NU e un interval complet, nu scrii "marimile X-Y". Scrii lista reala sau "N marimi intre X si Y".
- Varsta din marimi se scrie mereu cu "orientativ".
- Fara date care se schimba zilnic in text: pret, nume de magazine, numar de magazine, stoc curent.
- Nu copia propozitii de pe pagina merchant sau din surse. Reformuleaza integral.
- Fiecare paragraf contine cel putin un fapt specific acestui model. Daca un paragraf e doar generalitati, il stergi.
- Interlinkurile sunt EXACT doua: categoria nivel 2 si brandul.

==================================================
PASUL 5: AUTO-VERIFICARE INAINTE DE OUTPUT, OBLIGATORIE
==================================================

Daca oricare raspuns e NU, rescrii textul.

[ ] Slug-ul de categorie e unul din cele 5 valide?
[ ] Ancora de categorie corespunde slug-ului?
[ ] Genul e consecvent in TOATA descrierea (neutru daca merchant e unisex)?
[ ] Paragraful 1 contine cel putin un fapt specific acestui model?
[ ] Prima propozitie respecta tipul de deschidere dat de seed?
[ ] Interlinkurile sunt in pozitiile date de seed?
[ ] Propozitia cu linkul de categorie foloseste structura index_pool, reformulata?
[ ] Daca sterg linkul de categorie, propozitia gazda mai spune ceva despre produs?
[ ] Nicio formula din lista neagra?
[ ] Zero em dash-uri?
[ ] Numarul de paragrafe corespunde pragului de fapte?
[ ] Lungimea totala e intre 180 si 260 cuvinte?
[ ] Toate afirmatiile au sursa in pasul 1 sau pasul 2?
[ ] Zero filtre de magazin transformate in fapte?
[ ] Zero tehnologii de brand neconfirmate pe model?
[ ] Zero nume de magazine, pret sau stoc curent in text?
[ ] Marimile sunt exprimate corect (lista reala, nu interval fals)?
[ ] Varsta derivata din Anexa C si marcata "orientativ"?
[ ] Minim 3 entitati de cautare din 3.4?

==================================================
OUTPUT, JSON VALID
==================================================

{
  "extras_de_pe_pagina": {
    "brand": "", "model": "", "tip_produs": "", "categorie_magazin": "", "gen": "",
    "varsta_recomandata": "", "culoare": "", "material": "", "umplutura": "", "talpa": "",
    "inchidere": "", "detalii_constructie": [], "tehnologii_certificari": [],
    "marimi_disponibile": [], "cod_produs": ""
  },
  "completat_prin_cautare": { "camp": "sursa_folosita_si_nivel_de_incredere" },
  "numar_fapte_extrase": 0,
  "date_insuficiente": false,
  "seed_variatie": 0,
  "tip_deschidere_folosit": "",
  "pozitie_interlinkuri": "",
  "index_pool_link": 0,
  "varsta_orientativa": "",
  "entitati_cautare_folosite": [],
  "paragrafe": [
    "paragraf 1",
    "paragraf 2",
    "paragraf 3, doar daca exista fapte de brand pe model",
    "paragraf 4, doar daca exista date de marimi"
  ],
  "specificatii_tehnice": { "Model": "", "Material": "", "Caracteristici": "", "Cod produs": "" },
  "interlink_categorie": { "ancora": "incaltaminte baieti", "url_slug": "/categorie/incaltaminte-baieti/" },
  "interlink_brand": { "ancora": "Geox", "url_slug": "/brand/geox/" },
  "missing_data": [],
  "confidence_notes": [],
  "self_check": {
    "slug_valid": true, "ancora_corespunde_slug": true, "gen_consecvent": true,
    "fapt_specific_in_paragraf_1": true, "deschidere_conform_seed": true,
    "structura_pool_folosita": true, "lista_neagra_curata": true, "fara_em_dash": true,
    "lungime_in_interval": true, "fara_filtre_ca_fapte": true,
    "fara_tehnologii_neconfirmate": true, "fara_magazine_pret_stoc": true,
    "varsta_orientativa_corecta": true, "minim_3_entitati_cautare": true
  }
}

==================================================
ANEXA A: CONTROL DE REPETITIE LA NIVEL DE LOT
==================================================

Se ruleaza dupa generarea lotului, in afara agentului:

1. Extrage toate paragrafele 1 si toate paragrafele 4 din lot.
2. Calculeaza n-gramele de 6 cuvinte si numara aparitiile.
3. Orice n-grama de 6 cuvinte care apare la peste 3% din produse se adauga in LISTA NEAGRA.
4. Regenerezi doar produsele afectate.

Verifica si distributia seed-urilor si a index_pool. Daca sunt ne-uniforme, treci pe formula alternativa de la 4.1.

==================================================
ANEXA B: DATE CARE SE CAUTA O SINGURA DATA PER BRAND
==================================================

Se cauta o singura data, se salveaza intr-o tabela de referinta si se refolosesc:

- tabel de conversie marimi EU si lungime interioara in cm
- particularitati de calapod (ingust, lat)
- tehnologii proprietare ale brandului si ce inseamna fiecare
- certificari la nivel de companie

Faptul ca un brand detine o tehnologie NU inseamna ca modelul curent o are. Tabela se foloseste pentru validare, nu ca sursa de afirmatii despre model.

==================================================
ANEXA C: MARIME -> VARSTA (se scrie mereu "orientativ")
==================================================

Imbracaminte (inaltime in cm):
86 = 1-1,5 ani | 92 = 2 ani | 98 = 3 ani | 104 = 4 ani | 110 = 5 ani | 116 = 6 ani | 122 = 7 ani | 128 = 8 ani | 134 = 9 ani | 140 = 10 ani | 146 = 11 ani | 152 = 12 ani | 158 = 13 ani | 164 = 14 ani | 170 = 15 ani | 176 = 16 ani

Incaltaminte (EU):
19-22 = 1-2 ani | 23-25 = 2-3 ani | 26-27 = 3-4 ani | 28-29 = 4-5 ani | 30-31 = 6-7 ani | 32-33 = 8-9 ani | 34-35 = 10-11 ani | 36+ = 12 ani si peste

==================================================
ANEXA D: POOL STRUCTURI LINK CATEGORIE (index 0-49)
==================================================

[L] = ancora cu link. Placeholderele se completeaza DOAR cu fapte reale ale produsului. Se adapteaza flexiunea, nu se copiaza literal.

0. Cand alegi [L] pentru {ocazie}, merita verificat {criteriu}, iar aici {fapt}.
1. La [L] purtata zi de zi, {fapt} se simte la {consecinta}.
2. Pentru [L] de {sezon}, {fapt} conteaza mai mult decat aspectul.
3. Multi parinti cauta la [L] {criteriu}, iar modelul asta are {fapt}.
4. O problema frecventa la [L] e {problema}, iar {fapt} o rezolva.
5. Daca la [L] te intereseaza {criteriu}, {fapt} e raspunsul.
6. Ce il diferentiaza intre modelele de [L] pentru {ocazie} e {fapt}.
7. Un criteriu bun la [L] e {criteriu}, iar {produs} are {fapt}.
8. {fapt}, detaliu util la orice pereche de [L] pentru {sezon}.
9. La [L] pentru copiii de {varsta}, {fapt} ajuta la {consecinta}.
10. Cine alege [L] pentru {ocazie} se uita la {criteriu}, iar aici {fapt}.
11. {fapt}, asa ca {produs} trece usor de la {ocazie1} la {ocazie2} printre piesele de [L].
12. Intre [L] cu {atribut}, {produs} vine si cu {fapt}.
13. Pentru parintii care cauta [L] {atribut}, {fapt} e un plus concret.
14. La [L], {criteriu} face diferenta dimineata, iar {fapt}.
15. {produs} adauga la [L] obisnuita {fapt}.
16. Daca ai mai cumparat [L] care {problema}, aici {fapt}.
17. In zona de [L] pentru {sezon}, {fapt} e ce cauti.
18. Pentru {ocazie}, [L] are nevoie de {criteriu}, iar {fapt}.
19. {fapt} e motivul pentru care modelul merita pus pe lista de [L] pentru {ocazie}.
20. La [L] {culoare}, {criteriu} conteaza, iar {fapt}.
21. Cand cauti [L] usor de {actiune}, {fapt} rezolva asta.
22. Pentru [L] care rezista la {ocazie}, {fapt}.
23. Spre deosebire de [L] {atribut_opus}, {produs} are {fapt}.
24. La [L], detaliul de {zona} e des neglijat, iar aici {fapt}.
25. {fapt}, ceea ce il face practic printre [L] pentru {varsta}.
26. Pentru un copil de {varsta}, [L] trebuie sa fie {criteriu}, iar {fapt}.
27. Daca prioritatea la [L] e {criteriu}, {produs} bifeaza asta prin {fapt}.
28. La [L] purtata la {ocazie}, {fapt} inseamna {consecinta}.
29. {produs} e o varianta de [L] cu {fapt}, potrivita pentru {ocazie}.
30. Intre doua perechi de [L], {fapt} poate fi criteriul care decide.
31. Pentru [L] pe care copilul o poarta singur, {fapt}.
32. La [L] de {sezon}, {problema} e grija principala, iar {fapt}.
33. {fapt}, un avantaj concret la [L] folosita {frecventa}.
34. Cand alegi intre mai multe modele de [L], {fapt} e usor de observat.
35. Daca la [L] pui pret pe {criteriu}, {fapt}.
36. Pentru {ocazie}, {produs} aduce in [L] {fapt}.
37. La [L] {atribut}, {fapt} completeaza bine {alt_fapt}.
38. {fapt}, deci perechea se descurca la {ocazie} mai bine decat [L] {atribut_opus}.
39. Parintii care aleg [L] pentru {varsta} vor aprecia {fapt}.
40. La [L], {zona} se uzeaza primul, iar {fapt}.
41. Pentru [L] pe vreme de {vreme}, {fapt}.
42. {produs} rezolva la [L] partea de {criteriu}: {fapt}.
43. Daca ai nevoie de [L] {atribut} pentru {ocazie}, {fapt}.
44. La [L] din {material}, {fapt} ajuta la {consecinta}.
45. {fapt}, iar asta conteaza la [L] care se schimba des din cauza cresterii.
46. Pentru [L] de purtat de dimineata pana seara, {fapt}.
47. La alegerea de [L] pentru {ocazie}, {fapt} e primul lucru vizibil.
48. {produs} adauga {fapt} intr-o piesa de [L] altfel {atribut}.
49. Daca vrei [L] care sa {beneficiu_extras}, {fapt}.

==================================================
ANEXA E: INCHIDERI PARAGRAF MARIMI (doar seed par)
==================================================

0. Marimea potrivita o alegi din lista de mai jos, unde raman doar magazinele care o au.
2. Selectezi marimea si vezi imediat unde e disponibila.
4. Lista de magazine se filtreaza dupa marimea aleasa.
6. Alegi marimea copilului, iar lista arata doar ofertele care o au.
8. Disponibilitatea pe fiecare marime o vezi in lista, dupa ce selectezi marimea.
```
