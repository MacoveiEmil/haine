import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

KS = A('/brand/konges-slojd/', 'Konges Sløjd')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
REIMA = A('/brand/reima/', 'Reima')
GF = '/categorie/geci-jachete/'
GU = '/categorie/unisex-imbracaminte-geci-jachete/'
VANDUT = 'Pagina magazinului arată produsul ca VÂNDUT și nu dă culoarea; culoarea e cea din titlul site-ului.'
NOAPA = 'Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'

w(13559,
  f'<p>Geaca {KS} JODY TEDDY JACKET roz este o {A(GF, "geacă din fleece pentru fete")}, subțire, moale și plăcută la atingere, din poliester reciclat certificat GRS. Nu are căptușeală, umplutură sau glugă.</p>'
  '<p>Se închide cu fermoar, iar mânecile și marginea de jos sunt finisate cu bătături, care țin vântul la distanță. Tăietura e simplă. Nu e impermeabilă, deci e bună pentru zilele uscate de tranziție.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Căptușeală', 'nu are.'), ('Croială', 'simplă.'))
  + '<p>Mărimile 74 până la 134-140 acoperă orientativ 9 luni - 10 ani.</p>',
  [('model', 'JODY TEDDY JACKET'), ('culoare', 'culoarea roz'), ('fleece', 'Model subțire confecționat din material fleece'), ('moale', 'material moale și plăcut la atingere'),
   ('GRS', 'GRS (Global Recycle Standard)'), ('căptușeală', 'fără căptușeală'), ('umplutură', 'fără umplutură'), ('glugă', 'fără glugă'), ('fermoar', 'Incheiere cu fermoar'),
   ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('tăiere', 'Tăiere simplă, fără blocare'), ('impermeabil', 'fără impermeabilitate'),
   ('tranziție', 'Izolare: tranzitional'), ('material', '100% Poliester reciclat'), ('croială', 'Croială: simplu')],
  {'Model': 'Konges Sløjd JODY TEDDY JACKET', 'Material': '100% poliester reciclat (fleece)', 'Caracteristici': 'fleece, fermoar, bătături', 'Cod produs': 'KS104868'})

w(13569,
  f'<p>Cizmele de iarnă {TH} T3A5-34052 bej, în numerele mari, sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} izolate, din textil și piele ecologică, cu finisaj hidrofob pe față, care ține umezeala afară. Interiorul moale, căptușit, păstrează căldura.</p>'
  '<p>Talpa groasă din cauciuc are bandă de rulare antiderapantă. Vârful rotund e întărit, contrafortul rigid ține călcâiul pe loc, iar închiderea combină șiretul cu fermoarul lateral.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele artificială.'), ('Interior', 'material textil.'), ('Lungime branț', '22 cm la numărul 35.'))
  + '<p>Numerele 35-40 se poartă cam de la 10 ani în sus.</p>',
  [('cod', 'T3A5-34052'), ('culoare', 'culoarea bej'), ('izolat', 'Model Izolat confecționat din combinația materialului textil cu pielea ecologică'),
   ('hidrofob', 'Finisajul hidrofob al feței superioare nu permite umezelii să pătrundă în interior'), ('interior', 'Interiorul moale căptușit asigură un confort ridicat la purtare și un confort termic optim'),
   ('groasă', 'groasă, profilată'), ('antiderapantă', 'cu bandă de rulare, antiderapantă'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece'),
   ('fermoar', 'Model cu siret cu fermoar lateral'), ('gambă', 'Material textil, Piele artificiala'), ('lungime', 'Lungimea brantului pentru marimea este de: 22 cm'),
   ('mărime', 'Dimensiunile date pentru marimea: 35')],
  {'Model': 'Tommy Hilfiger T3A5-34052', 'Talpă': 'cauciuc, antiderapantă', 'Caracteristici': 'izolate, hidrofobe, șiret și fermoar', 'Cod produs': 'T3A5.34052'},
  notes=[NOAPA])

w(13589,
  f'<p>Cizmele de iarnă {TH} T1A5-34048 roz sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} izolate, din textil și piele ecologică, cu membrană și rezistență sporită la apă. Partea înaltă sprijină glezna pe suprafețe neuniforme.</p>'
  '<p>Talpa groasă din cauciuc are bandă de rulare antiderapantă și e durabilă. Vârful e întărit, contrafortul rigid ține călcâiul, iar velcro-ul și bucla de la spate le fac ușor de pus. Interiorul textil se păstrează curat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Lungime branț', '20,5 cm la numărul 31.'))
  + '<p>Numerele 30-34 merg pe la 6-11 ani.</p>',
  [('cod', 'T1A5-34048'), ('culoare', 'culoarea roz'), ('izolat', 'Model Izolat confecționat din combinația materialului textil cu pielea ecologică'), ('membrană', 'membrană impermeabilă'),
   ('apă', 'Impermeabil înseamnă rezistență sporită la apă'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('groasă', 'groasă, profilată'),
   ('antiderapantă', 'cu bandă de rulare, antiderapantă'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid'),
   ('velcro', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'), ('interior', 'Interiorul textil este confortabil'), ('gambă', 'Material sintetic, Material textil'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 20,5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 31')],
  {'Model': 'Tommy Hilfiger T1A5-34048', 'Talpă': 'cauciuc, antiderapantă', 'Caracteristici': 'izolate, velcro, profil înalt', 'Cod produs': 'T1A5.34048'},
  notes=[NOAPA])

w(13604,
  f'<p>Geaca de puf {A("/brand/united-colors-of-benetton/", "United Colors of Benetton")} 2WU0CN04Z bleumarin este o {A(GF, "geacă de iarnă pentru fete")} matlasată, din material neted, cu umplutură din puf de rață și pene, deci izolație groasă. Are rezistență sporită la apă și certificare RCS pentru materiale reciclate.</p>'
  '<p>Se închide cu fermoar și capsă, gulerul e ridicat, mânecile se termină cu elastic, iar buzunarele exterioare sunt oblice. Programul Dress Safely garantează că nu are elemente periculoase sau substanțe chimice nocive.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', '50% pene, 50% puf de rață.'), ('Lungime', '78 cm la mărimea 170.'))
  + '<p>Mărimile 120-170 corespund cam vârstei de 7-15 ani.</p>',
  [('cod', '2WU0CN04Z'), ('culoare', 'culoarea bleumarin'), ('puf', 'geacă de puf pentru copii'), ('matlasat', 'Modelul matlasat cu umplutură naturală din puf'),
   ('neted', 'Model izolat confecționat din material neted'), ('groasă', 'groasă'), ('apă', 'Model cu rezistenta sporita la apa'), ('RCS', 'Standardul de revendicare reciclat (RCS)'),
   ('fermoar', 'Fixare cu fermoar si snap'), ('guler', 'Gulerul ridicat'), ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('buzunare', 'Buzunare oblice exterioare'),
   ('Dress Safely', 'Dress Safely! Produsul nu contine elemente periculoase'), ('chimice', 'Produsul nu contine substante chimice periculoase'), ('material', '100% Poliester'),
   ('umplutură', '50% Pene, 50% Puf de rata'), ('lungime', 'Lungimea: 78 cm'), ('mărime', '170 cm')],
  {'Model': 'United Colors of Benetton 2WU0CN04Z', 'Material': '100% poliester, puf de rață', 'Caracteristici': 'puf natural, rezistentă la apă, Dress Safely', 'Cod produs': '2WU0CN04Z'},
  notes=['Informațiile despre glugă se contrazic („fără glugă, integrată”, „gluga fixă”, „detașabil”); nu am scris despre glugă.', NOAPA])

w(13668,
  f'<p>Geaca {A("/brand/diesel/", "Diesel")} JOMOX-FUR JACKET albastră este o {A(GU, "geacă de blugi unisex")}, din denim de bumbac spălat, ușor izolată, cu decor de denim decolorat. Nu are glugă.</p>'
  '<p>Se închide cu fermoar, buzunarele sunt oblice, iar manșetele se încheie. Tăietura e simplă, fără blocare. Magazinul precizează că nu e impermeabilă, deci e potrivită pentru zilele uscate de primăvară sau toamnă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Izolație', 'ușoară.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 132-175 se potrivesc pe la 9-16 ani.</p>',
  [('model', 'JOMOX-FUR JACKET'), ('culoare', 'Culoare albastru'), ('denim', 'Model ușor izolat confecționat din denim spălat'), ('decolorat', 'Denim spalacit decorativ'),
   ('glugă', 'fără glugă'), ('fermoar', 'Încheiere cu fermoar'), ('buzunare', 'Buzunare oblice'), ('manșete', 'Maneci cu mansete incheiate'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('impermeabil', 'fără impermeabilitate'), ('material', '100% Bumbac'), ('ușoară', 'ușoară'), ('croială', 'Croială: regular fit')],
  {'Model': 'Diesel JOMOX-FUR JACKET', 'Material': '100% bumbac (denim)', 'Caracteristici': 'denim spălat, ușor izolată, fermoar', 'Cod produs': 'J02506'},
  notes=['Titlul site-ului are „JACKET” în locul culorii; culoarea e cea de la magazin (albastru).', 'Informațiile despre căptușeală se contrazic; nu am scris despre ea.'])

w(13679,
  f'<p>Geaca {KS} MAGNUM DOWN JACKET SOLID bleumarin este o {A(GU, "geacă unisex")} matlasată, subțire, cu izolație sintetică medie, din poliester reciclat certificat GRS. Finisajul BIONIC-FINISH ECO respinge apa, iar materialul e respirabil și rezistent la vânt.</p>'
  '<p>Gulerul ridicat și gluga fixă apără de frig, fermoarul pe toată lungimea are clapă de furtună cu capse, iar buzunarele exterioare sunt oblice. Căptușeala e din bumbac și poliester.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Căptușeală 1', '100% bumbac.'), ('Căptușeală 2', '100% poliester.'))
  + '<p>Mărimile 86 până la 134-140 țin cam de 1-10 ani.</p>',
  [('model', 'MAGNUM DOWN JACKET SOLID'), ('culoare', 'culoarea bleumarin'), ('matlasat', 'Model subțire confecționat din material matlasat cu izolatie sintetică'), ('medie', 'medie'),
   ('GRS', 'GRS (Global Recycle Standard)'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('vânt', 'Model respirabil, rezistent la vant'), ('guler', 'Gulerul ridicat și gluga fixă'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă de furtună prinsă cu capse'), ('buzunare', 'Buzunare oblice exterioare'), ('material', '100% Poliester reciclat'),
   ('bumbac', '100% Bumbac'), ('poliester', '100% Poliester')],
  {'Model': 'Konges Sløjd MAGNUM DOWN JACKET SOLID', 'Material': '100% poliester reciclat', 'Caracteristici': 'matlasată, BIONIC-FINISH ECO, glugă fixă', 'Cod produs': 'KS103510'},
  notes=['Magazinul o numește „impermeabilă”, dar caracteristicile dau doar impregnare hidrofobă. Numele spune „DOWN”, dar umplutura e sintetică.'])

w(13682,
  f'<p>Hanoracul cu glugă {TH} KB0KB10319 bej e printre {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluzele pentru băieți")}, din tricot moale tip buclă, cu bumbac și poliester. Are imprimeuri cu text și logo, iar pe mânecă e brodat steagul Tommy Hilfiger.</p>'
  '<p>Nu are fermoar, umerii sunt coborâți, iar croiala e lejeră. Gluga e integrată, iar benzile elastice de la manșete și de la bază îl țin în formă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '68% bumbac, 32% poliester.'), ('Închidere', 'nu are.'), ('Glugă', 'integrată.'))
  + '<p>Mărimile 128-176 merg aproximativ la 8-16 ani.</p>',
  [('cod', 'KB0KB10319'), ('culoare', 'Culoare bej'), ('buclă', 'tricotul moale tip buclă din amestec de bumbac'), ('imprimeu', 'Imprimeurile expresive cu text și logo Tommy Hilfiger'),
   ('steag', 'Steagul brodat Tommy Hilfiger pe mânecă'), ('fermoar', 'Hanoracul fără fermoar cu glugă'), ('umeri', 'Linia umerilor coborâtă'), ('lejeră', 'croiala lejeră'),
   ('glugă', 'Gluga integrată'), ('elastic', 'Benzile elastice de la manșete și de la bază'), ('material', 'Întregul produs:68% Bumbac, 32% Poliester')],
  {'Model': 'Tommy Hilfiger KB0KB10319', 'Material': '68% bumbac, 32% poliester', 'Caracteristici': 'tricot buclé, glugă, imprimeu', 'Cod produs': 'KB0KB10319'})

w(13933,
  f'<p>Pantalonii izolați {REIMA} PROXIMA mov sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")} pentru zăpadă, cu membrană Reimatec, cusături sigilate ermetic și finisaj BIONIC ECO fără fluorocarburi. Izolația Fellex e certificată bluesign, iar materialul conține fibre reciclate certificate.</p>'
  '<p>Cracul are manșetă interioară contra zăpezii și întărituri din material rezistent la muchiile schiurilor. Talia e elastică, iar bretelele elastice se reglează și se detașează.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Coloană de apă', '10.000 mm.'), ('Respirabilitate', '7.000 g/m²/24 h.'), ('Buzunare', 'două laterale, cu fermoar.'), ('Greutate', '400 g.'))
  + '<p>Mărimile 116-164 se potrivesc în jur de 6-14 ani.</p>',
  [('model', 'REIMA PROXIMA'), ('izolat', 'Pantalonii izolați pentru copii Reima PROXIMA'), ('Reimatec', 'Reimatec'), ('sigilate', 'sigilate ermetic'),
   ('BIONIC', 'FINISAJ BIONIC®ECO fără fluorocarburi'), ('Fellex', 'material termoizolant Fellex® certificat de bluesign®'), ('reciclat', 'fibre reciclate certificate'),
   ('manșetă', 'crac cu manșetă interioară împotriva pătrunderii zăpezii'), ('schiuri', 'întărituri la nivelul cracului din material rezistent la tăiere prin muchiile schiurilor'),
   ('talie', 'Au talie elastică și bretele ajustabile'), ('bretele', 'bretele elastice reglabile și detașabile'), ('coloană', '10.000 mm'), ('respirabilitate', '7.000 g/m²/24 h'),
   ('buzunare', '2x laterale cu fermoar'), ('greutate', '400 g')],
  {'Model': 'Reima PROXIMA', 'Material': '100% poliester reciclat, laminare TPU', 'Caracteristici': 'Reimatec, Fellex, bretele detașabile', 'Cod produs': '259969'},
  notes=[VANDUT])

w(13961,
  f'<p>Tenișii {REIMA} EKANA roz sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} pentru copii mici, din textil și material sintetic, cu talpă ușoară și moale din EVA, flexibilă. Căptușeala e textilă, iar detaliile reflectorizante se văd seara.</p>'
  '<p>Șireturile elastice și banda velcro îi fac ușor de pus. Branțul modelat din EVA se scoate, are căptușeală din jerseu și imprimeu Happy Fit pentru alegerea mărimii, iar perechea se spală în mașină la 30 °C.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'material sintetic și textil.'), ('Talpă', 'EVA.'), ('Cod produs', '198074.'))
  + '<p>Magazinul nu mai afișează numere; modelul e gândit pentru copii mici, orientativ în jur de 1-4 ani.</p>',
  [('model', 'REIMA EKANA'), ('mici', 'Tenișii Reima EKANA sunt concepuți special pentru copiii mici'), ('față', 'material sintetic și textil'), ('EVA', 'talpă ușoară și moale EVA'),
   ('flexibilă', 'Talpa este flexibilă'), ('căptușeală', 'Căptușeală de textil'), ('reflectorizant', 'detalii reflectorizante'), ('velcro', 'Șireturile elastice și banda velcro facilitează încălțarea'),
   ('branț', 'branț modelat din EVA detașabil, cu căptușeală din jerseu și imprimeu Happy Fit'), ('spălare', 'Se pot spăla în mașina de spălat la 30 °C'), ('talpă', 'EVA')],
  {'Model': 'Reima EKANA', 'Talpă': 'EVA', 'Caracteristici': 'velcro, Happy Fit, lavabili la 30 °C', 'Cod produs': '198074'},
  notes=[VANDUT, 'Produsul nu are mărimi în catalog; vârsta 1-4 ani e estimată din „copiii mici”.'], varsta_txt='1-4 ani')
