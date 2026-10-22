import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GUESS = A('/brand/guess/', 'GUESS')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'

w(8537,
  f'<p>Geaca {GUESS} L6RL09 bleumarin este o {A(GB, "geacă de tranziție pentru băieți")} din material neted, cu glugă și căptușeală completă din bumbac. Poliesterul de la exterior o face rezistentă la șifonare.</p>'
  '<p>Se închide cu fermoar, are două buzunare laterale, iar mânecile și marginea de jos sunt finisate cu elastic, ca să nu intre vântul pe la margini.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', '100% bumbac.'), ('Lungime', '49 cm la mărimea 125/135.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile de la 122-125 la 175 sunt pentru copii de aproximativ 7-16 ani.</p>',
  [('cod', 'L6RL09'), ('culoare', 'culoarea bleumarin'), ('neted', 'Model confecționat din material neted'), ('șifonare', 'Poliester pentru rezistență ridicată la șifonare'),
   ('glugă', 'Model cu gluga'), ('căptușeală', 'cu căptușeală completă'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare laterale'),
   ('mâneci', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('material', '100% Poliester'), ('bumbac', '100% Bumbac'), ('lungime', 'Lungimea: 49 cm'),
   ('mărime', '125/ 135 cm'), ('croială', 'Croială: regular fit')],
  {'Model': 'GUESS L6RL09', 'Material': '100% poliester, căptușeală din bumbac', 'Caracteristici': 'glugă, fermoar, margini elastice', 'Cod produs': 'L6RL09.WCFM0'})

w(8565,
  f'<p>Geaca {GUESS} N6GL00 galbenă este o {A(GB, "geacă de tranziție pentru băieți")} neizolată, din material ornamentat, cu căptușeală completă. Gulerul ridicat și gluga fixă apără de frig, iar poliesterul rezistă bine la îndoire.</p>'
  '<p>Croiala e simplă, fermoarul o face ușor de pus și de scos, iar mânecile se termină cu elastic. Buzunarele exterioare se închid.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '42 cm la mărimea 113-118.'), ('Lățime la umeri', '30 cm.'))
  + '<p>Mărimile 88-96 până la 118-122 se potrivesc orientativ copiilor de 1-7 ani.</p>',
  [('cod', 'N6GL00'), ('culoare', 'culoarea galben'), ('neizolat', 'Model neizolat confecționat din din material ornamentat'), ('căptușeală', 'cu căptușeală completă'),
   ('guler', 'Gulerul ridicat și gluga fixă'), ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'), ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('buzunare', 'Buzunare exterioare incheiata'),
   ('material', '100% Poliester'), ('lungime', 'Lungimea: 42 cm'), ('mărime', '113-118 cm'), ('umeri', 'Latimea in umeri: 30 cm')],
  {'Model': 'GUESS N6GL00', 'Material': '100% poliester', 'Caracteristici': 'neizolată, glugă fixă, guler ridicat', 'Cod produs': 'N6GL00.WCFM2'})

w(8598,
  f'<p>Geaca {GUESS} J5YL11 neagră este o {A(GF, "geacă subțire pentru fete")}, de tranziție, din material neted, cu croială supradimensionată, lejeră. Compoziția combină poliamidă și bumbac, iar căptușeala e completă.</p>'
  '<p>Nu are glugă și se închide cu cleme. Mânecile și marginea de jos sunt finisate cu bătături, care o apără de vremea urâtă, iar pe laterale are două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '71% poliamidă, 29% bumbac.'), ('Închidere', 'cleme.'), ('Croială', 'supradimensionată.'))
  + '<p>Mărimile încep la 122-125 și ajung la 167, potrivite orientativ copiilor de 7-14 ani.</p>',
  [('cod', 'J5YL11 WHE80'), ('culoare', 'culoarea negru'), ('subțire', 'Model subtire confecționat din din material neted'), ('lejeră', 'Croială lejeră'),
   ('supradimensionat', 'Croială: supradimensionat'), ('material', '71% Poliamida, 29% Bumbac'), ('căptușeală', 'cu căptușeală completă'), ('glugă', 'fără glugă'),
   ('cleme', 'Incheiere cu cleme'), ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături pentru a proteja împotriva condițiilor meteorologice nefavorabile'),
   ('buzunare', 'Două buzunare laterale')],
  {'Model': 'GUESS J5YL11', 'Material': '71% poliamidă, 29% bumbac', 'Caracteristici': 'subțire, oversize, cleme', 'Cod produs': 'J5YL11.WHE80'})

w(8605,
  f'<p>Treningul {TH} KS0KS00708 bleumarin este un compleu din tricot, printre {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "treningurile pentru băieți")}, făcut dintr-un material foarte confortabil, cu mult bumbac. Bumbacul e regenerat, adică fibrele sunt refăcute din deșeuri textile, iar poliesterul este parțial reciclat.</p>'
  '<p>Bluza are fason drept, decolteu rotund, mânecă lungă și finisaj cu manșetă. Pantalonii au șnur de strângere, iar modelul e uni, ușor de purtat acasă sau la plimbare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '50% poliester reciclat, 50% bumbac reciclat.'), ('Decolteu', 'rotund.'), ('Model', 'uni, tricotaj.'))
  + '<p>Mărimile 128-176 sunt pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'KS0KS00708'), ('culoare', 'culoarea bleumarin'), ('tricot', 'Compleu din colecția Tommy Hilfiger confecționat din tricot'),
   ('confortabil', 'Model realizat din material extrem de confortabil cu un conținut ridicat de bumbac'), ('regenerat', 'Modelul conține fibre de bumbac regenerate'),
   ('deșeuri', 'Din deșeuri textile vechi sunt create fibre și fire noi'), ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('fason', 'Fason drept'),
   ('decolteu', 'Decolteu clasic, rotund'), ('mânecă', 'Maneca lunga'), ('manșetă', 'Finisaj din manseta'), ('șnur', 'cu șnur de strângere'), ('uni', 'Model: uni'),
   ('material', '50% Poliester reciclat, 50% Bumbac reciclat')],
  {'Model': 'Tommy Hilfiger KS0KS00708', 'Material': '50% poliester reciclat, 50% bumbac reciclat', 'Caracteristici': 'tricot, decolteu rotund, pantaloni cu șnur', 'Cod produs': 'KS0KS00708'})

w(8615,
  f'<p>Același cod {GUESS} H4BJ10, de data asta în negru: o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, matlasată, din material neted, cu umplutură groasă din poliester pentru zilele cu temperaturi mai reci. Căptușeala e completă.</p>'
  '<p>Gluga fixă și gulerul ridicat țin frigul departe de gât. Tăietura e simplă, închiderea cu fermoar, iar buzunarele de la exterior se închid.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester, inclusiv căptușeala și umplutura.'), ('Lungime', '47 cm la mărimea 125-135.'), ('Lățime la umeri', '33 cm.'))
  + '<p>Mărimile 122-125 până la 166-175 se potrivesc orientativ copiilor de 7-16 ani.</p>',
  [('cod', 'H4BJ10'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat confecționat din material neted'), ('matlasat', 'Model matlasat cu izolație sintetica'),
   ('reci', 'confort suplimentar la temperaturi mai reci'), ('groasă', 'groasă'), ('căptușeală', 'cu căptușeală completă'), ('guler', 'Gulerul ridicat și gluga fixă'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'), ('material', '100% Poliester'),
   ('lungime', 'Lungimea: 47 cm'), ('mărime', '125-135 cm'), ('umeri', 'Latimea in umeri: 33 cm')],
  {'Model': 'GUESS H4BJ10', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, izolație groasă, glugă fixă', 'Cod produs': 'H4BJ10.WCFM0'})

w(8635,
  f'<p>Geaca {GUESS} L5YL02 gri este o {A(GB, "geacă subțire pentru băieți")}, ușor izolată, din material textil cu model, foarte plăcut la purtare. Gulerul ridicat și gluga fixă apără de frig, iar căptușeala e completă, sintetică.</p>'
  '<p>Croiala e simplă, iar fermoarul o face ușor de pus și de scos. Mânecile și marginea de jos sunt finisate cu bătături, care țin vântul și umezeala la distanță.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Izolație', 'ușoară.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile de la 122-125 până la 175 sunt pentru copii de cam 7-16 ani.</p>',
  [('cod', 'L5YL02'), ('culoare', 'culoarea gri'), ('subțire', 'Model subțire confecționat din material textil cu model'),
   ('confortabil', 'material excepțional de confortabil'), ('guler', 'Gulerul ridicat și gluga fixă'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'),
   ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('material', '100% Poliamida'), ('ușoară', 'ușoară'), ('croială', 'Croială: regular fit')],
  {'Model': 'GUESS L5YL02', 'Material': '100% poliamidă', 'Caracteristici': 'subțire, glugă fixă, guler ridicat', 'Cod produs': 'L5YL02.WF090'})

w(8637,
  f'<p>Geaca {TH} KB0KB09852 maro este o {A(GB, "geacă de tranziție pentru băieți")} neizolată, din material neted, realizată parțial din poliamidă reciclată. Are guler ridicat, fără glugă, și căptușeală completă, sintetică.</p>'
  '<p>Tăietura e simplă, se închide cu fermoar, iar mânecile sunt finisate cu manșetă. E o geacă ușoară, pentru zilele de primăvară sau toamnă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă reciclată.'), ('Căptușeală', '100% poliamidă.'), ('Umplutură', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 se potrivesc orientativ copiilor de 8-16 ani.</p>',
  [('cod', 'KB0KB09852'), ('culoare', 'culoarea maro'), ('neizolat', 'Model neizolat confecționat din material neted'),
   ('reciclat', 'Acest produs a fost realizat partial din poliamida reciclata'), ('guler', 'Guler ridicat'), ('glugă', 'fără glugă'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'), ('manșetă', 'Finisaj din manseta'),
   ('material', '100% Poliamida reciclata'), ('poliamidă', '100% Poliamida'), ('umplutură', 'fără umplutură'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB09852', 'Material': '100% poliamidă reciclată', 'Caracteristici': 'neizolată, guler ridicat, fermoar', 'Cod produs': 'KB0KB09852'},
  notes=['„Primăvară sau toamnă” derivă din „neizolat” și „fără umplutură”.'])

w(8642,
  f'<p>Bocancii {A("/brand/geox/", "Geox")} CASEY negri sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} cu talpă groasă, plată, din cauciuc durabil și rezistent la deteriorare, și sistemul Geox Respira: talpa în trei straturi are perforații care ajută ventilarea.</p>'
  '<p>Se leagă cu șiret și au fermoar lateral, deci se încalță ușor. Vârful e rotund, tocul gros, iar branțul textil e confortabil și ține încălțămintea curată mai ușor.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic.'), ('Interior', 'material sintetic, material textil.'), ('Izolație', 'nu au.'))
  + '<p>Numerele 36-39 se poartă de pe la 12 ani în sus.</p>',
  [('model', 'CASEY'), ('culoare', 'culoarea negru'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('groasă', 'groasă, plată'),
   ('Respira', 'Sistemul Geox Respira'), ('straturi', 'talpei in trei straturi cu sistemul de perforari'), ('fermoar', 'Model cu siret cu fermoar lateral'),
   ('vârf', 'rotund'), ('toc', 'toc gros'), ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'),
   ('gambă', 'Material sintetic'), ('interior', 'Material sintetic, Material textil'), ('neizolat', 'Izolare: neizolat')],
  {'Model': 'Geox CASEY', 'Talpă': 'cauciuc, Geox Respira', 'Caracteristici': 'șiret, fermoar lateral, toc gros', 'Cod produs': 'J5620B.000BC'},
  notes=['Descrierea spune „piele întoarsă”, iar compoziția și atributele indică material sintetic, imitație de piele; am scris doar compoziția.',
         'Descrierea pomenește și închidere cu velcro; atributele dau șiret și fermoar, așa că am lăsat velcro deoparte.'])

w(8650,
  f'<p>Adidașii {A("/brand/primigi/", "Primigi")} 1420022 multicolori sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu membrană GORE-TEX, care ține picioarele uscate pe vreme schimbătoare, și talpă Vibram plată, din cauciuc, cu galanț de protecție. Fața din textil și material sintetic e ușoară și respirabilă.</p>'
  '<p>Urcă până la gleznă și au guler moale. Contrafortul e ușor rigidizat, vârful are spațiu mărit pentru degete, iar șireturile elastice și velcro-ul ajută la încălțat. Branțul detașabil e din piele naturală.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Sezon', 'primăvară, vară și toamnă.'))
  + '<p>Numerele 26-29 sunt pentru copii de aproximativ 3-5 ani.</p>',
  [('cod', '1420022'), ('culoare', 'multicolor'), ('GORE-TEX', 'Membrana GORE-TEX® asigură menținerea picioarelor uscate în condiții meteorologice schimbătoare'),
   ('Vibram', 'Talpa Vibram asigură stabilitate și aderență'), ('galanț', 'Talpa plată din cauciuc, cu galanț de protecție'),
   ('față', 'Partea superioară din materiale textile și sintetice asigură lejeritatea și respirabilitatea'), ('gleznă', 'Partea superioară care ajunge până la gleznă, împreună cu gulerul moale'),
   ('contrafort', 'Contrafortul ușor rigidizat'), ('degete', 'Spațiul mărit în zona degetelor'), ('velcro', 'Șireturile elastice și închiderea cu velcro'),
   ('branț', 'Branțul detașabil din piele naturală'), ('sezon', 'primăvară, vară și toamnă'), ('interior', '100% Material textil')],
  {'Model': 'Primigi 1420022', 'Membrană': 'GORE-TEX', 'Caracteristici': 'talpă Vibram, branț din piele, șireturi elastice și velcro', 'Cod produs': '1420022'})

w(8653,
  f'<p>Geaca {A("/brand/converse/", "Converse")} 3CC926 neagră este o {A(GF, "geacă de iarnă pentru fete")} izolată, matlasată, din material neted, cu umplutură sintetică medie spre groasă și căptușeală completă. Are glugă integrată.</p>'
  '<p>Croiala e simplă, fără detalii care să încurce, se închide cu fermoar, iar buzunarele se închid și ele, ca lucrurile mici să nu cadă. Izolația sintetică e gândită pentru zilele reci de iarnă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 92-98 până la 116-122 sunt pentru copii de cam 2-7 ani.</p>',
  [('cod', '3CC926'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat confecționat din material neted'), ('matlasat', 'Matlasare'), ('groasă', 'medie, groasă'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('glugă', 'integrată'), ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare incheiate'), ('material', '100% Poliester'), ('umplutură', 'sintetică'), ('croială', 'Croială: regular fit')],
  {'Model': 'Converse 3CC926', 'Material': '100% poliester, umplutură sintetică', 'Caracteristici': 'izolată, matlasată, glugă integrată', 'Cod produs': '3CC926'})
