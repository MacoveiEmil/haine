import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
LEVIS = A('/brand/levis/', "Levi's")
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
BEBE = '/categorie/bebe-imbracaminte-geci-jachete/'

w(9715,
  f'<p>Geaca {LEVIS} CORE PUFFER verde este o {A(GB, "geacă puf pentru băieți")}, ușor izolată, din material matlasat cu izolație sintetică pentru temperaturile mai reci. Gulerul ridicat și gluga fixă apără de frig, iar căptușeala e completă.</p>'
  '<p>Se închide cu fermoar, are buzunare oblice, iar marginea de jos e finisată cu manșetă. Magazinul precizează că o parte din produsele mărcii au eticheta roșie fără logo („blank tab”), tot originale.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '50 cm la mărimea 128.'), ('Lățime la subraț', '45 cm.'))
  + '<p>Mărimile 92-128 sunt pentru copii de aproximativ 2-8 ani.</p>',
  [('model', 'CORE PUFFER'), ('culoare', 'culoarea verde'), ('izolat', 'Model ușor izolat confecționat din material matlasat cu izolatie sintetică'),
   ('reci', 'temperaturi mai reci'), ('guler', 'Gulerul ridicat și gluga fixă'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare oblice'), ('manșetă', 'Marginea de jos finisata cu manseta'), ('blank', 'blank tab'), ('originale', 'modelele sale sunt produse in totalitate originale'),
   ('material', '100% Poliester'), ('lungime', 'Lungimea: 50 cm'), ('mărime', 'Dimensiunile date pentru marimea: 128'), ('subraț', 'Latimea la subrat: 45 cm')],
  {'Model': "Levi's CORE PUFFER", 'Material': '100% poliester', 'Caracteristici': 'matlasată, glugă fixă, guler ridicat', 'Cod produs': '8EH924'})

w(9729,
  f'<p>Geaca {A("/brand/adidas-originals/", "adidas Originals")} JV8550 roșie este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, din material neted cu lână în compoziție, cu izolație sintetică groasă pentru temperaturile mai scăzute. Căptușeala e din viscoză și poliester.</p>'
  '<p>Gulerul ridicat și gluga fixă apără de frig, tăietura e simplă, fără blocare, iar închiderea se face cu fermoar. Căptușeala acoperă tot interiorul.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '53% poliester, 43% lână, 4% elastan.'), ('Căptușeală', '51% viscoză, 49% poliester.'), ('Izolație', 'groasă.'))
  + '<p>Mărimile 104-128 se potrivesc orientativ copiilor de 4-8 ani.</p>',
  [('cod', 'JV8550'), ('culoare', 'culoarea roșu'), ('izolat', 'Model izolat confecționat din material neted'),
   ('izolație', 'Un model cu izolație sintetică care va oferi un confort suplimentar la temperaturi mai scăzute'), ('groasă', 'groasă'),
   ('guler', 'Gulerul ridicat și gluga fixă'), ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'),
   ('material', '53% Poliester , 43% Lana, 4% Elastan'), ('căptușeală', '51% Viscoza, 49% Poliester')],
  {'Model': 'adidas Originals JV8550', 'Material': '53% poliester, 43% lână, 4% elastan', 'Caracteristici': 'izolație groasă, glugă fixă, guler ridicat', 'Cod produs': 'JV8550'},
  notes=['Sursa are puține detalii despre buzunare sau finisaje.'])

w(9755,
  f'<p>Geaca {A("/brand/donsje/", "Donsje")} Bettie Jacket Bunnies bej este o {A(BEBE, "geacă pentru bebeluși")} din imitație de blană, ușor izolată, cu căptușeală completă din bumbac. Are guler și se încheie cu nasturi.</p>'
  '<p>Tăietura e simplă, fără glugă, iar izolația ușoară e prinsă pe căptușeală. Magazinul precizează că nu este impermeabilă, deci e potrivită pentru zilele uscate și răcoroase.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', '100% bumbac.'), ('Umplutură', '100% poliester.'))
  + '<p>Mărimile 74-92 sunt pentru copii de cam 9 luni - 2 ani.</p>',
  [('model', 'Bettie Jacket Bunnies'), ('culoare', 'culoarea bej'), ('blană', 'Model ușor izolat confecționat din imitație de blană'), ('bumbac', 'din bumbac, cu căptușeală completă'),
   ('guler', 'Model cu guler'), ('nasturi', 'Incheiere cu nasturi'), ('tăiere', 'Tăiere simplă, fără blocare'), ('glugă', 'fără glugă'),
   ('căptușeală', 'Model usor izolat pe captuseala'), ('impermeabil', 'fără impermeabilitate'), ('material', '100% Poliester'), ('căptușeală2', '100% Bumbac')],
  {'Model': 'Donsje Bettie Jacket', 'Material': 'imitație de blană, căptușeală din bumbac', 'Caracteristici': 'ușor izolată, nasturi, guler', 'Cod produs': '3041001'},
  notes=['„Zile uscate și răcoroase” derivă din „fără impermeabilitate” și izolația ușoară.'])

w(9788,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8893955 negre sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme de iarnă pentru băieți")} izolate, din material sintetic și textil, cu membrană GORE-TEX foarte subțire, impermeabilă, rezistentă la vânt și respirabilă, plus impregnare hidrofobă.</p>'
  '<p>Partea de sus e rigidizată, talpa din cauciuc e durabilă și rezistentă la deteriorare, iar căptușeala textilă e confortabilă și se păstrează ușor curată. Se închid cu velcro, iar ochiurile sunt fără nichel.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 25-30 sunt pentru copii de aproximativ 2-7 ani.</p>',
  [('cod', '8893955'), ('culoare', 'culoarea negru'), ('zăpadă', 'Cizme de zăpadă pentru copii'), ('izolat', 'Model izolat'),
   ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant si respirabila'), ('hidrofob', 'impregnare hidrofobă'),
   ('rigidizat', 'Partea superioară rigidizată'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('căptușeală', 'Model cu captuseala textila'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('velcro', 'Închiderea cu velcro'), ('nichel', 'Ochiurile din dantelă sunt fără nichel'),
   ('gambă', 'Material sintetic, Material textil'), ('profil', 'înalt')],
  {'Model': 'Primigi 8893955', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, velcro, talpă din cauciuc', 'Cod produs': '8893955'})

w(9809,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8883800 roz sunt {A("/categorie/ghete-cizme/", "cizme de iarnă pentru fete")} ușor izolate, din textil, piele întoarsă și piele naturală, cu membrană GORE-TEX subțire și respirabilă. Talpa Primitor Shock Absorber preia șocurile și protejează articulațiile, iar banda de rulare e antiderapantă.</p>'
  '<p>Partea de sus ridicată sprijină glezna pe teren neuniform, vârful rotund e ușor întărit, iar contrafortul rigid ține călcâiul pe loc. Se închid cu arici, iar interiorul textil se păstrează ușor curat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele naturală, piele întoarsă.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 25-30 se potrivesc orientativ copiilor de 2-7 ani.</p>',
  [('cod', '8883800'), ('culoare', 'culoarea roz'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Izolare: usor izolat'),
   ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant si respirabila'),
   ('Shock', 'Primitor Shock Absorber'), ('articulații', 'Amelioreaza si protejeaza articulatiile'), ('antiderapantă', 'cu bandă de rulare, antiderapantă'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('vârf', 'Cutie rotunda, usor intarita'), ('călcâi', 'Contorul de călcâi rigid'),
   ('arici', 'cu arici'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('gambă', 'Material textil, Piele naturala, Piele intoarsa'), ('profil', 'înalt')],
  {'Model': 'Primigi 8883800', 'Membrană': 'GORE-TEX', 'Caracteristici': 'Primitor Shock Absorber, arici, talpă antiderapantă', 'Cod produs': '8883800'},
  notes=['Magazinul descrie membrana ca 100% impermeabilă, dar are și formula că nu garantează impermeabilitatea completă; nu am scris „impermeabile”.'])

w(9810,
  f'<p>Geaca {A("/brand/lego/", "LEGO")} LWJAZ 802 roz, varianta cu codul 11010971, este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, cu umplutură sintetică medie spre groasă. Materialul exterior, cu BIONIC-FINISH ECO, rezistă la vânt și apă, iar respirabilitatea e de 4000 g/m2/24h.</p>'
  '<p>Gluga se detașează, gulerul e ridicat, iar manșetele elastice au găuri pentru degetul mare, ca mânecile să nu se ridice. Are buzunar de skipass pe mânecă, două buzunare laterale cu fermoar, fermoare YKK și reflectorizante 3M Scotchlite.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Coloană de apă', '10000.'), ('Căptușeală', 'completă, sintetică.'))
  + '<p>Mărimile 98-164 se potrivesc orientativ copiilor de 3-14 ani.</p>',
  [('cod', 'LWJAZ 802'), ('culoare', 'culoarea roz'), ('cod2', '11010971'), ('izolat', 'Model izolat'), ('groasă', 'medie, groasă'), ('BIONIC', 'BIONIC-FINISH® ECO'),
   ('vânt', 'Materialul exterior este rezistent la vânt și apă'), ('respirabil', 'Respirabilitate: 4000 g/m2/24h'), ('glugă', 'Gulerul ridicat și gluga detașabilă'),
   ('manșete', 'Manșete elastice cu găuri pentru degetul mare'), ('skipass', 'Buzunar funcțional pentru permis de schi, cu fermoar, pe mânecă'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('YKK', 'Fermoarele YKK®'), ('3M', '3M ™ Scotchlite'), ('material', '100% Poliester'),
   ('coloană', 'Impermeabilitate: 10000'), ('căptușeală', 'cu căptușeală completă, sintetică')],
  {'Model': 'LEGO LWJAZ 802', 'Material': '100% poliester', 'Caracteristici': 'BIONIC-FINISH ECO, glugă detașabilă, buzunar skipass', 'Cod produs': '11010971'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(9852,
  f'<p>Pantofii din piele {A("/brand/geox/", "Geox")} B163MB violet sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} cu profil înalt, din piele naturală, cu membrană impermeabilă și sistemul Geox Respira: talpa în trei straturi are perforații care ajută ventilarea.</p>'
  '<p>Se închid cu scai, deci se pun ușor. Vârful e rotund, spatele călcâiului e rigidizat, iar interiorul e textil. Talpa e din material sintetic.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'piele naturală.'), ('Interior', 'material textil.'), ('Talpă', 'material sintetic.'))
  + '<p>Numerele 24-27 sunt pentru copii de aproximativ 2-4 ani.</p>',
  [('cod', 'B163MB'), ('culoare', 'culoarea violet'), ('piele', 'Model confectionat din piele naturala'), ('profil', 'înalt'), ('membrană', 'membrană impermeabilă'),
   ('Respira', 'Sistemul Geox Respira'), ('straturi', 'talpei in trei straturi cu sistemul de perforari'), ('scai', 'Incheiere cu scai'), ('vârf', 'Varf rotund'),
   ('călcâi', 'Spatele calcaiului rigidizat'), ('interior', 'Interior textil'), ('gambă', 'Piele naturala'), ('textil', 'Material textil'), ('talpă', 'Material sintetic')],
  {'Model': 'Geox B163MB', 'Material': 'piele naturală', 'Caracteristici': 'Geox Respira, membrană, scai', 'Cod produs': 'B163MB.00032'})

w(9867,
  f'<p>Geaca bomber {A("/brand/dkny/", "DKNY")} D60237 neagră este o {A(GF, "geacă subțire pentru fete")}, de tranziție, dintr-o combinație de țesături, cu un detaliu decorativ. Croiala e lejeră, iar căptușeala e completă, sintetică.</p>'
  '<p>Se închide cu fermoar, iar mânecile sunt finisate cu manșetă, ca la orice bomber. Nu are glugă, iar magazinul precizează că nu e impermeabilă. Mărimile sunt pentru adolescenți.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Alte materiale', '100% poliester cu strat de poliuretan.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 156-162 se potrivesc orientativ copiilor de 13-14 ani.</p>',
  [('cod', 'D60237'), ('culoare', 'culoarea negru'), ('bomber', 'Geaca bomber pentru copii din colectia Dkny'), ('subțire', 'Model subtire confecționat dintr-o combinatie de tesaturi diferite'),
   ('decorativ', 'Detaliu decorativ'), ('lejeră', 'Croială lejeră'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('fermoar', 'Incheiere cu fermoar'),
   ('manșetă', 'Finisaj din manseta'), ('glugă', 'fără glugă'), ('impermeabil', 'fără impermeabilitate'), ('material', '100% Poliester'),
   ('alte', '100% Poliester cu strat de poliuretan'), ('croială', 'Croială: regular fit')],
  {'Model': 'DKNY D60237', 'Material': '100% poliester', 'Caracteristici': 'bomber, subțire, detaliu decorativ', 'Cod produs': 'D60237'})

w(9882,
  f'<p>Geaca {A("/brand/mini-rodini/", "Mini Rodini")} Ritzratz roșie este o {A(BEBE, "geacă pentru bebeluși")} izolată, din poliester reciclat ornamentat, cu izolație sintetică medie spre groasă. Are BIONIC-FINISH ECO și acoperire PFC Repellent, fără compuși perfluorurați, care o fac rezistentă la apă, plus rezistență la vânt.</p>'
  '<p>Croiala e lejeră, cu umeri coborâți, iar talia se reglează cu șnur. Fermoarul pe toată lungimea are clapă cu capse, gulerul e ridicat, gluga se detașează, iar în față are buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Căptușeală', 'completă, sintetică.'), ('Glugă', 'detașabilă.'))
  + '<p>Mărimile 80-86 până la 140-146 sunt pentru copii de cam 1-11 ani.</p>',
  [('model', 'Ritzratz'), ('culoare', 'culoarea roșu'), ('izolat', 'Model izolat confecționat din material ornamentat'), ('groasă', 'medie, groasă'),
   ('reciclat', 'Acest produs este fabricat din poliester reciclat'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('PFC', 'Modelul cu acoperire ecologica PFC Repellent cu apa libera'),
   ('vânt', 'Model respirabil, rezistent la vant'), ('lejeră', 'Croială lejeră'), ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'),
   ('talie', 'Talia este reglabila cu snur'), ('fermoar', 'Închidere cu fermoar pe toată lungimea, cu clapă rezistentă la vânt, cu capse'),
   ('guler', 'Gulerul ridicat și gluga detașabilă'), ('buzunare', 'In fata buzunare'), ('material', '100% Poliester reciclat'), ('căptușeală', 'cu căptușeală completă, sintetică')],
  {'Model': 'Mini Rodini Ritzratz', 'Material': '100% poliester reciclat', 'Caracteristici': 'BIONIC-FINISH ECO, talie cu șnur, glugă detașabilă', 'Cod produs': '25710110'},
  notes=['Magazinul o numește „impermeabilă”, dar spune și că nu garantează impermeabilitatea completă.'])

w(9962,
  f'<p>Geaca {A("/brand/karl-lagerfeld/", "Karl Lagerfeld")} Z31107 neagră este o {A(GB, "geacă de tranziție pentru băieți")} neizolată, din țesătură netedă, cu glugă încorporată și căptușeală completă. Poliesterul o face rezistentă la îndoire.</p>'
  '<p>Tăietura e simplă, iar fermoarul o face ușor de pus și de scos. Magazinul precizează că nu e impermeabilă. Mărimile sunt italienești, raportate la cele europene, deci merită verificat tabelul magazinului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'nu are.'), ('Glugă', 'integrată.'))
  + '<p>Mărimile 114-150 se potrivesc orientativ copiilor de 6-12 ani.</p>',
  [('cod', 'Z31107'), ('culoare', 'culoarea negru'), ('neizolat', 'Model neizolat confecționat din țesătură netedă'), ('glugă', 'Gluga încorporată'),
   ('căptușeală', 'cu căptușeală completă'), ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'), ('impermeabil', 'fără impermeabilitate'),
   ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '100% Poliester'), ('umplutură', 'fără umplutură')],
  {'Model': 'Karl Lagerfeld Z31107', 'Material': '100% poliester', 'Caracteristici': 'neizolată, glugă integrată, fermoar', 'Cod produs': 'Z31107'})
