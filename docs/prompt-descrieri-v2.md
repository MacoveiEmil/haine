# Prompt descrieri de produs (v2) — hainute.ro

PASUL 1: DESCHIDE SI EXTRAGE DE PE PAGINA MERCHANT

Deschide URL-ul primit ca input (link_afiliat). Aceasta este pagina sursa de adevar pentru acest produs. Extrage tot ce gasesti explicit pe pagina:

brand

model / cod produs (MPN sau echivalent afisat de magazin)

tip produs (sneakers, geaca, salopeta, cizme etc)

categorie asa cum o numeste magazinul

gen (baieti / fete / unisex), daca e specificat

interval de varsta recomandat, daca e afisat

culoare

material / compozitie, daca e afisat

talpa, inchidere, croi, daca sunt afisate (pentru incaltaminte)

detalii de constructie: gluga detasabila, mansete, buzunare, cusaturi lipite, umplutura, captuseala, benzi reflectorizante

certificari sau tehnologii numite explicit (bluesign, Therma-FIT, GORE-TEX, REPREVE etc)

marimile disponibile, asa cum apar (lista exacta, nu rotunji)

pretul curent

disponibilitatea per marime, daca e afisata

imagine principala

Marcheaza explicit fiecare camp ca EXTRAS (gasit pe pagina) sau LIPSA.

PRAG MINIM DE FAPTE Numara cate fapte concrete despre acest model ai extras (material, umplutura, talpa, inchidere, gluga, mansete, buzunare, cusaturi, tehnologie, certificare, captuseala, benzi reflectorizante, interval de varsta).

5 sau mai multe fapte -> scrii 4 paragrafe

3 sau 4 fapte -> scrii 3 paragrafe

sub 3 fapte -> scrii 2 paragrafe si marchezi produsul in output cu "date_insuficiente": true

Nu compensezi lipsa de fapte cu propozitii mai lungi. Un text scurt si concret e preferabil unui text lung si gol.

Nu trece la pasul 2 pentru campuri deja EXTRASE. Cautarea web e doar pentru campurile LIPSA.

PASUL 2: COMPLETEAZA DOAR CAMPURILE LIPSA, PRIN CAUTARE WEB

Pentru fiecare camp marcat LIPSA la pasul 1 (de regula: material/compozitie, talpa, interval de varsta, particularitati de fit ale brandului), cauta:

"{brand} {model}" + termenul lipsa exemplu: "Geox J36LAA material" sau "Reima Alaniva compozitie"

REGULI DE VALIDARE A SURSELOR, IN ORDINE DE PRIORITATE:

Site-ul oficial al brandului -> incredere maxima

Alt magazin mare care vinde acelasi model exact (Answear, Zalando, ABOUT YOU, ePantofi, Modivo) -> incredere mare, DOAR daca modelul/codul coincide exact cu cel extras la pasul 1

Agregator de moda (GLAMI) -> incredere medie, foloseste doar daca confirma ce ai deja, nu ca sursa unica

Bloguri, forumuri, recenzii individuale -> NU folosi ca sursa de fapt. Poti folosi ca semnal de context, niciodata ca afirmatie in text.

REGULA DE COROBORARE: Daca gasesti informatia pe o singura sursa din categoria 2 sau mai slaba, NU o prezinti ca fapt cert. Fie o omiti, fie o marchezi in output la confidence_notes ca "sursa unica, neconfirmata".

Daca doua surse independente se contrazic (exemplu: un site zice "piele naturala", altul zice "piele ecologica"), NU alegi arbitrar. Marchezi campul ca CONTRADICTORY in confidence_notes si il omiti din textul narativ.

Daca nu gasesti nimic dupa cautare, campul ramane LIPSA. Nu inventezi.

LIMITA DE CAUTARE: maxim 3 interogari de cautare per produs. Daca dupa 3 cautari campul tot lipseste, il declari lipsa si mergi mai departe.

PASUL 3: STABILESTE GENUL, CATEGORIA SI INTERLINKURILE

--- 3.1 GENUL, SE FIXEAZA O SINGURA DATA ---

Stabileste genul din datele extrase la pasul 1. Aceasta decizie se ia acum si NU se mai schimba nicaieri in text.

gen = baieti -> in tot textul folosesti forme masculine: baiatul, cel mic, copilul. NU folosesti "fetita", "ea". gen = fete -> in tot textul folosesti forme feminine: fetita, cea mica, copila. NU folosesti "cel mic", "baiatul", "el". gen = unisex -> in tot textul folosesti forme neutre: copilul, cel mic, piciorul copilului. NU alunecati spre "fetita" sau "baiatul".

REGULA DURA: intr-o descriere nu pot coexista referinte de gen diferite. Daca ai scris "pentru fete" in interlink, nu poti scrie "cel mic" in aceeasi descriere. Aceasta este cea mai frecventa eroare din versiunea 1 si invalideaza output-ul.

Consecventa se verifica la pasul 5.

--- 3.2 CATEGORIA NIVEL 2, ANCORA SI SLUG ---

Nivelul 2 NU este genul singur ("baieti", "fete") si NU este tipul de produs singur ("pantofi sport"). Este combinatia tip-mare + gen.

Determina sectiunea principala din tipul de produs extras la pasul 1: pantofi, sneakers, cizme, sandale, ghete, papuci, adidasi -> Incaltaminte geaca, salopeta, pulover, rochie, pantaloni, bluza, set, combinezon, hanorac, tricou, fusta, colanti -> Imbracaminte

Tabel de mapare, obligatoriu de respectat exact:

Sectiune

Gen

Ancora

Slug

Incaltaminte

Baieti

incaltaminte baieti

/categorie/incaltaminte-baieti/

Incaltaminte

Fete

incaltaminte fete

/categorie/incaltaminte-fete/

Incaltaminte

Unisex/lipsa

incaltaminte copii

/categorie/incaltaminte-copii/

Imbracaminte

Baieti

imbracaminte baieti

/categorie/imbracaminte-baieti/

Imbracaminte

Fete

imbracaminte fete

/categorie/imbracaminte-fete/

Imbracaminte

Unisex/lipsa

imbracaminte copii

/categorie/imbracaminte-copii/

VERIFICARE OBLIGATORIE: slug-ul trebuie sa contina genul (baieti / fete / copii). Daca output-ul contine un slug de tip /categorie/imbracaminte/ fara sufix de gen, output-ul este invalid si se rescrie.

VERIFICARE OBLIGATORIE 2: ancora trebuie sa corespunda slug-ului. Nu poti avea ancora "imbracaminte pentru fete" pe slug /categorie/imbracaminte/. Ancora poate fi flexata gramatical in propozitie (imbracamintea pentru fete, gama de imbracaminte pentru fete), dar perechea ancora-slug trebuie sa se refere la aceeasi pagina.

--- 3.3 BRAND, PAGINA DE BRAND ---

Ancora = numele brandului asa cum apare oficial (respecta capitalizarea de brand: Geox, adidas cu litera mica, DD Step, 4F, ALPINE PRO). Slug tinta: /brand/{brand-slug}/

PASUL 4: STABILESTE VARIATIA, APOI SCRIE TEXTUL

--- 4.1 SEED DE VARIATIE ---

Ca sa nu iasa 1000 de descrieri cu aceeasi structura, calculezi un seed determinist inainte de a scrie.

seed = ultima cifra din cod_produs Daca cod_produs nu contine cifre, foloseste numarul de litere din numele modelului, modulo 10.

Din seed rezulta doua decizii, luate mecanic, fara sa alegi tu:

DECIZIA A, tipul de deschidere al paragrafului 1 (seed determina randul):

0 -> Deschizi cu situatia concreta de folosire (drum spre gradinita, ore in parc, teren ud, sala de sport), apoi introduci produsul. 1 -> Deschizi cu numele complet al produsului si tipul lui, apoi spui ce rezolva. 2 -> Deschizi cu o caracteristica fizica extrasa (materialul, umplutura, talpa), apoi spui despre ce produs e vorba. 3 -> Deschizi cu profilul copilului (varsta, temperament, cat de activ e), apoi produsul. 4 -> Deschizi cu vremea sau anotimpul concret pentru care e facut produsul, apoi produsul. 5 -> Deschizi cu contrastul dintre doua utilizari (zi de scoala si weekend, curte si drumetie), apoi produsul. 6 -> Deschizi cu brandul si modelul, apoi destinatia lui. 7 -> Deschizi cu problema pe care o rezolva (picioare ude, frig la incheieturi, incaltat greu dimineata), apoi produsul. 8 -> Deschizi cu un detaliu de constructie extras (gluga detasabila, inchidere cu arici, cusaturi lipite), apoi contextul de folosire. 9 -> Deschizi cu intervalul de varsta sau cu marimile disponibile, apoi produsul.

Deschiderea inseamna PRIMA PROPOZITIE. Nu copia formularile de mai sus, sunt descrieri de structura, nu texte gata facute.

DECIZIA B, pozitia interlinkurilor (seed determina randul):

seed 0, 3, 6, 9 -> link categorie in propozitia 2 din paragraful 1 link brand in ultima propozitie a paragrafului de brand seed 1, 4, 7 -> link categorie in ultima propozitie din paragraful 1 link brand in prima propozitie a paragrafului de brand seed 2, 5, 8 -> link categorie in prima propozitie din paragraful 1 link brand la mijlocul paragrafului de brand

--- 4.2 CINE CITESTE ---

O mama sau un tata care compara rapid doua sau trei variante si vrea sa stie daca produsul asta e alegerea buna pentru copilul lui. Nu citeste ca sa se informeze enciclopedic, citeste ca sa decida. Vorbeste-i direct, cald, ca un sfat de la cineva care intelege ce conteaza: raportul calitate-pret, confortul copilului, daca merita banii fata de brandul mai ieftin de alaturi, daca arata bine fara sa coste enorm.

Evita tonul de fisa tehnica in text narativ (fisa tehnica vine separat, la bullets). Evita tonul de reclama. Tonul corect e undeva la mijloc: cineva care stie despre ce vorbeste si iti spune sincer daca merita.

--- 4.3 STRUCTURA, 180-260 CUVINTE TOTAL ---

PARAGRAF 1, prezentare si potrivire (45-70 cuvinte) Ce este produsul, pentru cine, ce rezolva concret pentru copil. Deschiderea respecta DECIZIA A. Interlinkul de categorie se pune conform DECIZIEI B. OBLIGATORIU: paragraful contine cel putin un fapt extras la pasul 1 care e specific acestui model. Nu e suficient "tine de cald" sau "e usoara". Un fapt specific inseamna: materialul numit, umplutura, tipul de inchidere, gluga detasabila, tehnologia numita, intervalul de varsta.

PARAGRAF 2, constructie si folosire zilnica (55-80 cuvinte) Aici e miezul deciziei. Ce ofera concret produsul raportat la cat de comod e de folosit zi de zi: usor de incaltat singur, se spala usor, rezista la joaca, se usuca repede, nu se sifoneaza. Legi fiecare caracteristica extrasa de o consecinta practica pentru parinte sau copil. Foloseste DOAR fapte extrase sau validate la pasii 1 si 2.

PARAGRAF 3, brand si incredere (35-55 cuvinte) Se scrie DOAR daca ai fapte confirmate despre brand legate de acest model (tehnologie proprie, certificare, materiale). Nu se scrie cu generalitati de tip "brand de renume international". Interlinkul de brand se pune conform DECIZIEI B. Daca nu ai fapte de brand, sari peste acest paragraf si treci la 4.

PARAGRAF 4, potrivire pe marimi si disponibilitate (30-50 cuvinte) Se scrie doar daca ai date reale despre marimi in feed sau pe pagina. Spui cate marimi sunt si intre ce valori, daca produsul acopera un interval de varsta anume, daca sunt marimi epuizate. Nu recomanzi sa se ia o marime mai mare sau mai mica decat daca informatia e confirmata explicit de brand la pasul 2.

--- 4.4 BULLET POINTS (dupa paragrafele narative, 4-8 puncte) ---

Aici, si doar aici, ton tehnic-factual, fara adjective:

Brand: ... Model: ... Material: ... (doar daca EXTRAS sau VALIDAT) Umplutura: ... (doar daca disponibil) Talpa: ... (doar la incaltaminte, daca disponibil) Inchidere: ... (doar daca disponibil) Categorie: ... Interval de varsta: ... (doar daca EXTRAS sau VALIDAT) Marimi disponibile: ... Cod produs: ...

Nu completa o linie cu "N/A" sau "nespecificat". Daca nu ai date, linia nu exista in output.

LISTA NEAGRA, FORMULE INTERZISE

Aceste constructii au aparut repetitiv in versiunea 1 si sunt interzise complet. Daca una apare in output, output-ul se rescrie.

FORMULE DE INTRODUCERE A LINKULUI DE CATEGORIE, INTERZISE: "Intra in gama de ..." "Face parte din ..." "Fac parte din ..." "Se incadreaza in ..." "Apartine gamei ..." "Este inclus in categoria ..." "Il gasesti in sectiunea ..." orice propozitie al carei singur rol este sa gazduiasca linkul

Linkul de categorie trebuie sa fie in interiorul unei propozitii care spune ceva concret despre produs. Daca stergi linkul si propozitia ramasa nu mai transmite nicio informatie, propozitia e gresita.

FORMULE DE INCHEIERE, INTERZISE: "E o alegere solida din gama ..." "E o alegere buna pentru ..." "pentru un copil care nu sta locului" "pentru copiii care nu stau o clipa locului" "E o {produs} practica pentru ..." "Sunt genul de {produs} pe care ..."

DESCHIDERI INTERZISE (prea folosite in v1): "{Produs} e gandita pentru ..." "{Produs} sunt facuti pentru ..." "{Produs} e o alegere calda ..." "{Produs} este perfect pentru ..."

CLISEE DE UMPLUTURA, INTERZISE: "tine de cald fara sa fie greoaie" "pe cat de usoara, pe atat de calduroasa" "incalzeste fara sa adauge volum" "fara sa limiteze miscarea" "se asorteaza usor cu restul hainelor" "confort si stil" "un must-have in garderoba" "nu va dezamagi"

REGULI GENERALE DE LIMBAJ:

fara em dash, niciodata, sub nicio forma

fara superlative nesustinute: cel mai bun, perfect, ideal, extraordinar, premium (daca nu e categorie de pret reala), must-have, revolutionar

fara exclamatii

fara adresare la persoana intai plural ("va oferim", "recomandam")

fara intrebari retorice

fara fraze de tip "in concluzie", "asadar", "in plus", "de asemenea" ca deschideri de propozitie

REGULI ANTI-HALUCINATIE, OBLIGATORII

Foloseste DOAR fapte din pasul 1 (extras de pe pagina) sau din pasul 2 (validat prin cautare, cu sursa de incredere si fara contradictie).

Niciodata nu inventezi: tehnologii, beneficii medicale sau ortopedice, impermeabilitate, respirabilitate, lungime interioara in cm, recomandare de a lua o marime mai mare sau mai mica, tara de fabricatie, compozitie exacta in procente daca nu e confirmata, gramaj de umplutura.

Marimile disponibile: daca lista NU e un interval complet, nu scrii "marimile X-Y". Scrii lista reala sau "N marimi intre X si Y". exemplu: date 28, 29, 30, 31, 32, 34 -> scrii "sase marimi intre 28 si 34" sau enumeri direct, NU "marimile 28-34".

Pretul nu se scrie ca numar fix in text narativ. Se lasa ca variabila de template legata de feed.

Nu copia propozitii de pe pagina merchant sau de pe sursele gasite prin cautare. Reformuleaza integral. Verificare interna: daca o propozitie din output ar putea aparea identica pe pagina magazinului, rescrie-o.

Fiecare paragraf contine cel putin un fapt specific acestui model. Daca un paragraf e doar generalitati, il stergi.

Interlinkurile sunt EXACT doua: categoria nivel 2 si brandul. Nu adauga linkuri suplimentare in text narativ.

Tehnologiile cu nume propriu (Therma-FIT, BIONIC-FINISH ECO, REPREVE, bluesign, GORE-TEX) se mentioneaza doar daca apar explicit pe pagina merchant sau pe site-ul oficial al brandului PENTRU ACEST MODEL. Nu extrapolezi de la brand la model.

PASUL 5: AUTO-VERIFICARE INAINTE DE OUTPUT, OBLIGATORIE

Parcurgi lista si raspunzi mental la fiecare punct. Daca oricare raspuns e NU, rescrii textul inainte de a returna output-ul.

[ ] Slug-ul de categorie contine genul (baieti / fete / copii)? [ ] Ancora de categorie corespunde slug-ului? [ ] Genul e consecvent in TOATA descrierea, inclusiv in paragraful 2, 3, 4? [ ] Paragraful 1 contine cel putin un fapt specific acestui model? [ ] Prima propozitie respecta tipul de deschidere dat de seed? [ ] Interlinkurile sunt in pozitiile date de seed? [ ] Daca sterg linkul de categorie, propozitia gazda transmite in continuare o informatie despre produs? [ ] Nicio formula din lista neagra nu apare in text? [ ] Zero em dash-uri? [ ] Numarul de paragrafe corespunde pragului de fapte de la pasul 1? [ ] Lungimea totala e intre 180 si 260 cuvinte? [ ] Toate afirmatiile din text au sursa in pasul 1 sau pasul 2? [ ] Marimile sunt exprimate corect (lista reala, nu interval fals)?

Adauga in output rezultatul verificarii, la campul "self_check".

INPUT ASTEPTAT DE PROMPT

link_afiliat: {{url}}

OUTPUT, JSON VALID

{ "extras_de_pe_pagina": { "brand": "", "model": "", "tip_produs": "", "categorie_magazin": "", "gen": "", "varsta_recomandata": "", "culoare": "", "material": "", "umplutura": "", "talpa": "", "inchidere": "", "detalii_constructie": [], "tehnologii_certificari": [], "marimi_disponibile": [], "pret": "", "cod_produs": "" }, "completat_prin_cautare": { "camp": "sursa_folosita_si_nivel_de_incredere" }, "numar_fapte_extrase": 0, "date_insuficiente": false, "seed_variatie": 0, "tip_deschidere_folosit": "", "pozitie_interlinkuri": "", "paragrafe": [ "paragraf 1", "paragraf 2", "paragraf 3, doar daca exista fapte de brand", "paragraf 4, doar daca exista date de marimi" ], "bullets": [ "Brand: ...", "Model: ..." ], "interlink_categorie": { "ancora": "incaltaminte baieti", "url_slug": "/categorie/incaltaminte-baieti/" }, "interlink_brand": { "ancora": "Geox", "url_slug": "/brand/geox/" }, "missing_data": [], "confidence_notes": [], "self_check": { "slug_contine_gen": true, "ancora_corespunde_slug": true, "gen_consecvent": true, "fapt_specific_in_paragraf_1": true, "deschidere_conform_seed": true, "lista_neagra_curata": true, "fara_em_dash": true, "lungime_in_interval": true } }

ANEXA A: CONTROL DE REPETITIE LA NIVEL DE LOT

Agentul nu are memorie intre produse, deci nu poate sti singur ca a mai scris o fraza identica la produsul 340. Seed-ul rezolva structura, dar nu garanteaza unicitatea la nivel de fraza. De aceea, dupa generarea lotului, rulezi un pas de verificare separat, in afara agentului:

Extrage toate paragrafele 1 din lot.

Calculeaza n-gramele de 6 cuvinte si numara aparitiile.

Orice n-grama de 6 cuvinte care apare la peste 3% din produse se marcheaza si se adauga in LISTA NEAGRA din acest prompt.

Regenerezi doar produsele afectate.

Repeti ciclul dupa fiecare lot mare. Lista neagra creste in timp si asta e mecanismul care tine descrierile diferite la scara de mii de pagini.

Suplimentar, verifica distributia seed-urilor. Daca furnizorul de feed foloseste coduri de produs cu terminatii ne-uniforme (multe se termina in 0), variatia se strica. In cazul asta schimba formula de seed pe: seed = (suma cifrelor din cod_produs + numarul de litere din model) modulo 10

ANEXA B: DATE CARE SE CAUTA O SINGURA DATA PER BRAND

Nu rula cautari per produs pentru informatii stabile la nivel de brand. Acestea se cauta o singura data, se salveaza intr-o tabela de referinta si se refolosesc:

tabel de conversie marimi EU si lungime interioara in cm

particularitati de calapod (ingust, lat, alergator)

tehnologii proprietare ale brandului si ce inseamna fiecare

certificari pe care brandul le detine la nivel de companie

politica de garantie si retur, daca e relevanta

Atentie: faptul ca un brand detine o tehnologie nu inseamna ca modelul curent o are. Tabela de brand se foloseste pentru context si pentru validare, nu ca sursa de afirmatii despre un model anume.

---

ADENDUM (reguli adăugate după feedback, 2026-10)

1. NU suntem comparator. Interzis în text: „compară”, „comparator”, „comparație”, „cel mai bun preț”. Formularea corectă: „vezi mărimile disponibile”, „disponibil în aceste magazine”.
2. Fără date care se schimbă zilnic în text: fără preț, fără numele magazinelor, fără numărul de magazine, fără „mărimile epuizate acum”. Acestea sunt afișate live în lista de magazine de pe pagină. Paragraful de mărimi spune doar intervalul modelului (ex. „de la 28 la 35”) și trimite la lista de magazine.
3. Interlinkul de categorie trebuie să sune natural, ca o recomandare reală, nu ca o propoziție construită doar pentru link. Formulările variază (pool de 50-60 de variante), ca să nu se repete pe sute de pagini.
4. Slug-urile reale de categorie nivel 2 de pe site: /categorie/incaltaminte-baieti/, /categorie/incaltaminte-fete/, /categorie/imbracaminte-baieti/, /categorie/imbracaminte-fete/, /categorie/imbracaminte-bebe/ (bebe = gen neutru în text). Brand: /brand/{slug}/.
5. Faptele se iau doar de pe pagina magazinului nostru (Answear / Fashion Days / Sportisimo / various-brands) sau de pe pagini de la alte magazine care au EXACT același cod de model. Cele care apar într-o singură sursă secundară sau contradictoriu se omit.
6. Paragraful de brand se scrie doar dacă există fapte de brand legate de acest model; altfel se sare (al doilea link, cel de brand, se pune natural în alt paragraf).
7. Bullets-urile tehnice nu intră în descriere: merg în tabelul „Specificații tehnice” (Model, Material, Caracteristici, Cod produs).
