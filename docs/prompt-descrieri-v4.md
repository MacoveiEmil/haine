Prompt descrieri de produs (v4) — hainute.ro

INPUT:
- link_afiliat: {{url}}
- categorie_principala: {{slug + nume}}  (din feed, ex: /categorie/incaltaminte-fete/)
- categorii_site: {{lista slug + nume a categoriilor de pe site, inclusiv subcategorii}}
- produse_populare: {{optional, lista: nume produs + url + categorie}}

Textul final se scrie in romana, CU diacritice.

==================================================
REGULA ZERO: DATE DOAR DIN CAUTARE LIVE
==================================================

Nu folosesti nimic din memoria ta despre produs, model sau brand. Fiecare fapt din text vine dintr-o pagina deschisa ACUM, in aceasta rulare.

- Deschizi obligatoriu pagina merchant (link_afiliat).
- Cauti obligatoriu pagina oficiala a modelului la brand: "{brand} {cod_produs}" sau "{brand} {model}".
- Pentru fiecare fapt folosit in text salvezi in output: URL-ul sursei + fragmentul exact de pe pagina care il confirma.
- Fapt fara fragment = fapt care nu exista. Nu intra in text.
- Daca nu poti deschide pagina merchant, te opresti si returnezi "eroare": "pagina_merchant_inaccesibila". Nu scrii nimic din memorie.

==================================================
PASUL 1: EXTRAGERE
==================================================

De pe pagina merchant si de pe pagina oficiala a modelului extragi:

- brand, model, cod produs
- tip produs (sneakers, cizme, geaca, salopeta, balerini etc)
- gen asa cum apare la merchant
- culoare
- material exterior, interior, talpa, compozitie
- inchidere (siret, siret elastic, arici, fermoar, nasturi)
- detalii de constructie: gluga detasabila, mansete, buzunare, cusaturi lipite, umplutura, captuseala, elemente reflectorizante, branț detasabil
- protectii declarate: impermeabil, rezistent la apa, izolat termic, protectie UV (DOAR daca scrie explicit)
- tehnologii cu nume propriu (Respira, GORE-TEX, Therma-FIT, REPREVE etc), DOAR daca numele apare pe pagina ACESTUI model
- sezonul declarat de magazin sau brand
- marimile modelului

Ignori valorile de filtru ale magazinului (ex: "talpa 2-4 cm"). Nu sunt fapte despre model.

Surse acceptate, in ordine:
1. pagina merchant
2. pagina oficiala a modelului la brand
3. alt magazin mare (Answear, Zalando, ABOUT YOU, ePantofi, Modivo) DOAR cu acelasi cod de model, exact
Bloguri, forumuri, recenzii, agregatoare: nu.

Fapt gasit intr-o singura sursa de tip 3: se omite.
Doua surse care se contrazic: se omite, se noteaza in confidence_notes.
Maxim 4 cautari per produs.

PRAG: daca ai sub 3 fapte concrete despre model, "date_insuficiente": true si scrii doar paragraful 1 si paragraful 4.

==================================================
PASUL 2: DECIZII INAINTE DE SCRIS
==================================================

2.1 GEN
Textul e MEREU neutru: copilul, cel mic, piciorul copilului. Fara "fetita", "baiatul", "ea", "el". Genul apare doar in ancora categoriei.

2.2 ANCORA CATEGORIEI PRINCIPALE
Slug-ul vine din input (categorie_principala). Ancora e gramaticala, cu "pentru":

| Slug                            | Ancora (forme permise)                                      |
|---------------------------------|-------------------------------------------------------------|
| /categorie/incaltaminte-baieti/ | încălțăminte pentru băieți / încălțămintea pentru băieți    |
| /categorie/incaltaminte-fete/   | încălțăminte pentru fete / încălțămintea pentru fete        |
| /categorie/imbracaminte-baieti/ | îmbrăcăminte pentru băieți / îmbrăcămintea pentru băieți    |
| /categorie/imbracaminte-fete/   | îmbrăcăminte pentru fete / îmbrăcămintea pentru fete        |
| /categorie/imbracaminte-bebe/   | îmbrăcăminte pentru bebeluși / hăinuțe pentru bebeluși      |

Interzis: "încălțămintea fete", "îmbrăcămintea băieți" (fara "pentru").

2.3 UTILIZARI DERIVATE DIN FAPTE
Fiecare utilizare (vreme, anotimp, activitate) trebuie sa aiba in spate un fapt extras. Exemple de derivare permise:

- impermeabil / GORE-TEX / cusaturi lipite -> ploaie, zapada topita, balti
- izolat / umplutura / captuseala calda -> frig, iarna
- plasa textila / sandale / bumbac subtire -> vara, zile calde
- talpa cu lumini / elemente reflectorizante -> seara, drum cand se intuneca devreme
- arici / siret elastic -> copilul se incalta singur, dimineti grabite
- tip produs balerini / poante / echipament de dans -> balet, dans
- talpa care nu lasa urme declarata / ghete de sala declarate -> sport indoor, sala
- trening / tricou tehnic declarat -> ora de sport

Daca nu ai faptul, nu scrii utilizarea. "Bun pentru ploaie" fara impermeabilitate declarata = interzis.

2.4 CATEGORIA COMPLEMENTARA (paragraful 3)
Alegi din categorii_site O categorie diferita de cea principala, care are sens fata de produs:
- alternativa pentru alt anotimp sau alta vreme (sneakers din plasa -> ghete de iarna; geaca de iarna -> geaca de primavara)
- complement purtat impreuna (geaca de iarna -> cizme de zapada; salopeta -> caciula si manusi)
- alternativa pentru alta activitate (sneakers de oras -> pantofi de sport pentru sala)

Daca produse_populare contine un produs din categoria aleasa, il poti numi si linka in locul categoriei. Altfel linkezi categoria.
Slug-ul trebuie sa existe in categorii_site. Nu inventezi slug-uri.

==================================================
PASUL 3: STRUCTURA TEXTULUI (170-240 cuvinte)
==================================================

PARAGRAF 1: CE ESTE SI LA CE E BUN (40-60 cuvinte)
Prima propozitie spune direct: ce produs e (tip, brand, model, culoare) si pentru ce e bun.
Apoi: in ce anotimp, pe ce vreme, la ce ocazii se poarta (doar utilizari derivate cu 2.3) si pentru ce varsta (Anexa C, "orientativ").
Linkul spre categoria principala e in acest paragraf, intr-o propozitie care spune ceva concret despre produs.
Fara introduceri de atmosfera ("in diminetile grabite...", "intre ora de sport si parc..."). Direct la subiect.

PARAGRAF 2: CE ARE SI CE TI-AJUTA (1 propozitie + lista)
O propozitie scurta de introducere, cu linkul de brand pe numele brandului.
Apoi o lista de 4-7 puncte. Fiecare punct = un fapt extras + la ce foloseste concret:

- **{Element}**: {fapt}, {consecinta practica}.

Ordinea punctelor: tehnologie numita (daca exista), material, talpa sau umplutura, inchidere, alte detalii de constructie, iar ultimul punct:
- **Potrivit pentru**: {lista de vreme / anotimp / activitati, doar derivate cu 2.3}.

PARAGRAF 3: ALTERNATIVA SAU COMPLEMENT (35-55 cuvinte)
Spui clar cand produsul asta e alegerea potrivita si cand ar fi mai potrivita categoria complementara aleasa la 2.4 (sau ce se poarta impreuna cu el). Linkul spre categoria complementara (sau produsul popular) e in acest paragraf.
Trebuie sa aiba logica reala: diferenta de anotimp, vreme sau activitate, bazata pe faptele produsului.
Fara cuvintele "compara", "comparatie", "comparator".

PARAGRAF 4: MARIMI (1-2 propozitii)
Intervalul de marimi al modelului si varsta orientativa (Anexa C). Atat.
Fara CTA, fara trimitere la lista de magazine, fara stoc, fara pret, fara magazine.
Daca marimile nu sunt un interval complet: "N marimi intre X si Y", nu "marimile X-Y".

==================================================
LIMBAJ
==================================================

Ton: un parinte care stie despre ce vorbeste si iti spune direct. Fara reclama, fara literatura.

INTERZIS:
- em dash, exclamatii, intrebari retorice, persoana I plural
- superlative: cel mai bun, perfect, ideal, extraordinar, premium, must-have, revolutionar
- "in concluzie", "asadar", "in plus", "de asemenea" la inceput de propozitie
- "compara", "comparator", "comparatie", "cel mai bun pret", "reducere", "oferta"
- formule de link goale: "intra in gama", "face parte din", "se incadreaza in", "apartine", "il gasesti in sectiunea"
- clisee: "confort si stil", "nu va dezamagi", "ore in sir", "fara sa limiteze miscarea", "se asorteaza usor", "tine de cald fara sa fie greoaie", "pentru copiii care nu stau locului"
- beneficii nedeclarate: respira, aerul circula, ventilatie, aderenta, amortizeaza, moale la fiecare pas, fara presiune, stabilitate, elastic (fara elastan in compozitie), ortopedic, sustine piciorul
- afirmatii meta: "verificabil pe eticheta", "copiii il recunosc imediat", "face diferenta la confort", "se simte"
- tara de fabricatie, procente de compozitie nedeclarate, gramaj de umplutura, lungime interioara in cm, recomandare de marime mai mare sau mai mica
- etape de scoala in afara Anexei C

==================================================
PASUL 4: AUTO-VERIFICARE
==================================================

Daca oricare raspuns e NU, rescrii.

[ ] Fiecare fapt din text are URL + fragment in "surse"?
[ ] Prima propozitie spune direct ce e produsul si la ce e bun?
[ ] Fiecare utilizare (vreme, anotimp, activitate) are fapt in spate?
[ ] Lista din paragraful 2 are 4-7 puncte, fiecare cu fapt + consecinta?
[ ] Paragraful 3 are o logica reala (anotimp / vreme / activitate / complement)?
[ ] Slug-ul complementar exista in categorii_site?
[ ] Paragraful 4 are maxim 2 propozitii, fara CTA?
[ ] Ancora categoriei principale e gramaticala, cu "pentru"?
[ ] Text neutru ca gen?
[ ] Zero cuvinte din lista INTERZIS?
[ ] Varsta si etapa de scoala din Anexa C, cu "orientativ"?
[ ] 170-240 cuvinte?

==================================================
OUTPUT, JSON VALID
==================================================

{
  "extras": {
    "brand": "",
    "model": "",
    "cod_produs": "",
    "tip_produs": "",
    "gen_merchant": "",
    "culoare": "",
    "material": "",
    "talpa": "",
    "inchidere": "",
    "detalii_constructie": [],
    "protectii_declarate": [],
    "tehnologii": [],
    "sezon": "",
    "marimi": []
  },
  "surse": [
    { "fapt": "", "url": "", "fragment": "" }
  ],
  "date_insuficiente": false,
  "varsta_orientativa": "",
  "utilizari_derivate": [
    { "utilizare": "", "fapt_baza": "" }
  ],
  "categorie_complementara": {
    "slug": "",
    "motiv": ""
  },
  "descriere_html": "<p>...</p><p>...</p><ul><li>...</li></ul><p>...</p><p>...</p>",
  "interlinkuri": [
    { "ancora": "", "url_slug": "", "paragraf": 1 },
    { "ancora": "", "url_slug": "/brand/{slug}/", "paragraf": 2 },
    { "ancora": "", "url_slug": "", "paragraf": 3 }
  ],
  "specificatii_tehnice": {
    "Model": "",
    "Material": "",
    "Caracteristici": "",
    "Cod produs": ""
  },
  "confidence_notes": [],
  "self_check": {
    "toate_faptele_au_sursa": true,
    "deschidere_directa": true,
    "utilizari_justificate": true,
    "lista_4_7_puncte": true,
    "paragraf_3_logic": true,
    "slug_complementar_valid": true,
    "marimi_fara_cta": true,
    "ancora_gramaticala": true,
    "gen_neutru": true,
    "lista_interzisa_curata": true,
    "lungime_ok": true
  }
}

==================================================
ANEXA A: CONTROL DE REPETITIE PE LOT (in afara agentului)
==================================================

1. Extrage toate paragrafele 1 si 3 din lot.
2. N-grame de 6 cuvinte. Orice n-grama prezenta la peste 3% din produse intra in lista INTERZIS.
3. Regenerezi doar produsele afectate.

==================================================
ANEXA B: DATE PER BRAND (o singura data, tabela de referinta)
==================================================

Tabel marimi, calapod, tehnologii proprietare si ce inseamna. Se folosesc DOAR pentru validare. Faptul ca brandul are o tehnologie NU inseamna ca modelul o are.

==================================================
ANEXA C: MARIME -> VARSTA -> ETAPA (se scrie mereu "orientativ")
==================================================

Imbracaminte (cm):
86 = 1-1,5 ani | 92 = 2 | 98 = 3 | 104 = 4 | 110 = 5 | 116 = 6 | 122 = 7 | 128 = 8 | 134 = 9 | 140 = 10 | 146 = 11 | 152 = 12 | 158 = 13 | 164 = 14 | 170 = 15 | 176 = 16

Incaltaminte (EU):
19-22 = 1-2 ani | 23-25 = 2-3 | 26-27 = 3-4 | 28-29 = 4-5 | 30-31 = 6-7 | 32-33 = 8-9 | 34-35 = 10-11 | 36+ = 12+

Etape (singurele formulari permise):
sub 3 ani = antepreșcolar | 3 = grupa mică | 4 = grupa mijlocie | 5 = grupa mare | 6 = clasa pregătitoare | 7-10 = clasele I-IV | 11-14 = gimnaziu | 15+ = liceu
