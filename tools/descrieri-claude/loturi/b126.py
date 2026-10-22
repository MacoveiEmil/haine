import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
GEOX = A('/brand/geox/', 'Geox')
CKJ = A('/brand/calvin-klein-jeans/', 'Calvin Klein Jeans')
GF = '/categorie/geci-jachete/'
NOAPA = 'Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'

w(12939,
  f'<p>Cizmele {PRIMIGI} 8875333 negre, din material sintetic și piele întoarsă, sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")} cu izolație și branț de lână, deci păstrează căldura la frig. Membrana GORE-TEX e foarte subțire, respirabilă și oprește vântul.</p>'
  '<p>Pe gleznă, partea înaltă se strânge cu un șnur cu opritor, iar șiretul reglează potrivirea. Degetele au loc în vârful lat și moale, talpa groasă e antiderapantă și preia șocurile, iar branțul cu contur se scoate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, piele întoarsă.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 31-35 țin, cu aproximație, de 6-11 ani.</p>',
  [('cod', '8875333'), ('culoare', 'culoarea negru'), ('izolat', 'Izolare: izolat'), ('lână', 'Un model cu interior din lână'), ('GORE-TEX', 'Model cu membrana GORE-TEX®'),
   ('vânt', 'rezistenta la vant si respirabila'), ('șnur', 'Reglarea circumferinței superioare cu șnururi cu opritoare'), ('șiret', 'Fixare: cu snur'),
   ('vârf', 'Cutia lată a degetelor'), ('moale', 'moale'), ('antiderapantă', 'absorbție a șocurilor, cu bandă de rulare, antiderapantă'), ('groasă', 'groasă, profilată'),
   ('contur', 'Brant confortabil, cu contur'), ('detașabil', 'Branțuri detașabile'), ('gambă', 'Material sintetic, Piele intoarsa'), ('profil', 'înalt')],
  {'Model': 'Primigi 8875333', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, branț din lână, șiret și șnur', 'Cod produs': '8875333'},
  notes=['Magazinul descrie membrana ca 100% impermeabilă; nu am scris „impermeabile”.'])

w(12940,
  f'<p>Geaca matlasată {A("/brand/guess/", "GUESS")} J6YL01 bej este o {A(GF, "geacă de tranziție pentru fete")} cu izolație sintetică medie, din țesătură rezistentă, cu căptușeală completă. Gluga e integrată, iar gulerul ridicat apără de vânt și de frigul ușor.</p>'
  '<p>Se închide cu fermoar și capse, bordurile elastice de la bază și manșete ajută la potrivire, iar buzunarele laterale sunt de tip slip-on. Lungimea ajunge până la șold, iar logoul Guess decorează geaca. Nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Izolație', 'medie.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 122-125 până la 167 sunt gândite pentru 7-14 ani, orientativ.</p>',
  [('cod', 'J6YL01'), ('culoare', 'Culoare bej'), ('matlasat', 'Geaca matlasată Guess'), ('medie', 'Izolație sintetică medie'), ('rezistent', 'Țesătură rezistentă'),
   ('căptușeală', 'Căptușeală completă'), ('glugă', 'Glugă integrată'), ('guler', 'Guler și revere: ridicat'), ('fermoar', 'Sistem de închidere cu fermoar și capse'),
   ('borduri', 'Borduri elastice la bază și la manșete'), ('buzunare', 'Buzunare laterale tip slip-on'), ('șold', 'Lungime până la șolduri'), ('logo', 'Model decorat cu logo'),
   ('impermeabil', 'fără impermeabilitate'), ('material', 'Întregul produs:100% Poliester'), ('croială', 'Croială: regular fit')],
  {'Model': 'GUESS J6YL01', 'Material': '100% poliester', 'Caracteristici': 'matlasată, glugă, fermoar și capse', 'Cod produs': 'J6YL01.W2607'})

w(12953,
  f'<p>Adidașii {GEOX} FLEXYPER FAST albaștri sunt {A("/categorie/adidasi/", "adidași pentru fete")} din textil și material sintetic, cu interior textil care se păstrează ușor curat, și sistemul Geox Respira, cu talpă perforată în trei straturi pentru ventilare.</p>'
  '<p>Fața e rigidizată, vârful e rotund, iar talpa e din cauciuc. Se leagă cu șiret clasic, buclele ajută la încălțat și au detalii decorative.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'scurt.'))
  + '<p>Numerele 36-39 se poartă de pe la 12 ani în sus.</p>',
  [('model', 'FLEXYPER FAST'), ('culoare', 'Culoare albastru'), ('textil', 'combinația materialului textil cu cel sintetic'), ('interior', 'Interiorul textil este confortabil'),
   ('Respira', 'Sistemul Geox Respira'), ('straturi', 'talpei in trei straturi cu sistemul de perforari'), ('rigidizat', 'Partea superioară rigidizată'),
   ('vârf', 'Varf rotund'), ('talpă', 'Talpă din cauciuc'), ('șiret', 'Șiretul clasic permite ajustarea individuală'), ('bucle', 'Buclele facilitează alunecarea pantofului'),
   ('decorativ', 'Detalii decorative'), ('gambă', 'Material sintetic, Material textil'), ('profil', 'scurt')],
  {'Model': 'Geox FLEXYPER FAST', 'Material': 'textil, material sintetic', 'Caracteristici': 'Geox Respira, șiret, talpă din cauciuc', 'Cod produs': 'J55N5A.0149J'},
  notes=['Titlul site-ului are „FAST” în locul culorii; culoarea e cea de la magazin (albastru).'])

w(12967,
  f'<p>Geaca {CKJ} IG0IG02056 violet este o {A(GF, "geacă de iarnă pentru fete")} izolată, matlasată, cu umplutură sintetică medie spre groasă și fibră REPREVE din sticle de plastic reciclate. Căptușeala e din polar, iar interiorul gulerului e din fleece moale.</p>'
  '<p>Gluga se detașează, mânecile și marginea de jos au bătături, iar închiderea e cu fermoar. Buzunarele exterioare se închid, iar înăuntru e un buzunar cu velcro.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '50 cm la mărimea 128.'), ('Lățime la umeri', '43 cm.'))
  + '<p>Mărimile 104-176 se potrivesc pe la 4-16 ani.</p>',
  [('cod', 'IG0IG02056'), ('culoare', 'culoarea violet'), ('izolat', 'Model izolat confecționat din din material matlasat'), ('groasă', 'medie, groasă'),
   ('REPREVE', 'Fibra REPREVE este fabricata din sticle de plastic reciclate'), ('polar', 'cu căptușeală completă, din polar'),
   ('fleece', 'Partea interioara a gulerului este captusita cu un material moale, fleece'), ('glugă', 'detașabilă'), ('bătături', 'Mânecile și marginea inferioară finisate cu bătături'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'), ('velcro', 'Buzunar interior cu velcro'), ('material', '100% Poliester'),
   ('lungime', 'Lungimea: 50 cm'), ('mărime', '128 cm'), ('umeri', 'Latimea in umeri: 43 cm')],
  {'Model': 'Calvin Klein Jeans IG0IG02056', 'Material': '100% poliester, căptușeală din polar', 'Caracteristici': 'izolată, REPREVE, glugă detașabilă', 'Cod produs': 'IG0IG02056'})

w(13044,
  f'<p>Ghetele din piele {GEOX} SHAYLAX negre sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} ușor izolate, din piele naturală cu fața neporoasă, care se curăță ușor cu o cârpă umedă. Sistemul Geox Respira ajută ventilarea prin talpa perforată în trei straturi.</p>'
  '<p>Au șiret și fermoar lateral, vârful rotund e întărit, iar contrafortul rigid ține călcâiul pe loc. Talpa groasă, plată, din cauciuc, e durabilă, iar interiorul e textil.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'piele naturală.'), ('Interior', 'material textil.'), ('Talpă', 'groasă, plată.'))
  + '<p>Numerele 28-35 sunt potrivite cam pentru 4-11 ani.</p>',
  [('model', 'SHAYLAX'), ('culoare', 'culoarea negru'), ('izolat', 'Izolare: usor izolat'), ('piele', 'confecționat din piele naturala'),
   ('neporoasă', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'), ('Respira', 'Sistemul Geox Respira'), ('straturi', 'talpei in trei straturi cu sistemul de perforari'),
   ('fermoar', 'Model cu siret cu fermoar lateral'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('groasă', 'groasă, plată'), ('interior', 'Interiorul textil este confortabil'), ('gambă', 'Piele naturala')],
  {'Model': 'Geox SHAYLAX', 'Material': 'piele naturală', 'Caracteristici': 'Geox Respira, șiret și fermoar, ușor izolate', 'Cod produs': 'J46EXD.00043'})

w(13046,
  f'<p>Geaca matlasată {CKJ} LVCKTJM15B neagră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")} cu izolație termică medie, din material textil, cu căptușeală completă, sintetică. Are glugă integrată și guler ridicat.</p>'
  '<p>Se închide cu fermoar pe toată lungimea, manșetele au nervuri, iar pe laterale are buzunare. Magazinul o descrie ca lungă până la genunchi și precizează că nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Izolație', 'medie.'), ('Mânecă', 'clasică.'))
  + '<p>Mărimile 104-116 merg orientativ la 4-6 ani.</p>',
  [('cod', 'LVCKTJM15B'), ('culoare', 'Culoare negru'), ('matlasat', 'Geaca matlasată neagră Calvin Klein Jeans'), ('medie', 'Izolație termică medie'),
   ('textil', 'Confecționată din material textil'), ('căptușeală', 'Căptușeală completă, sintetică'), ('glugă', 'Glugă integrată'), ('guler', 'Guler și revere: ridicat'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea'), ('manșete', 'Manșete cu nervuri'), ('buzunare', 'Buzunare laterale practice'), ('genunchi', 'Lungime până la genunchi'),
   ('impermeabil', 'fără impermeabilitate'), ('material', 'Întregul produs:100% Poliester'), ('mânecă', 'Tip de mânecă: clasică')],
  {'Model': 'Calvin Klein Jeans LVCKTJM15B', 'Material': '100% poliester', 'Caracteristici': 'matlasată, glugă, fermoar', 'Cod produs': 'LVCKTJM15B'},
  notes=['Titlul site-ului are „petrecută” în locul culorii; culoarea e cea de la magazin (negru).'])

w(13064,
  f'<p>Geaca de schi {A("/brand/burton/", "Burton")} HILLSLOPE verde este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, cu izolație groasă Thermocore și certificare Bluesign. Sistemul Grow o ajută să țină mai multe sezoane, odată cu creșterea copilului.</p>'
  '<p>Înăuntru are o centură flexibilă, cauciucată, contra zăpezii, iar mânecile se reglează cu velcro. Pe lângă cele două buzunare laterale cu fermoar, are unul pe mânecă și unul interior. Gluga e integrată.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Umplutură', '95% poliester reciclat, 5% poliester.'), ('Impermeabilitate', 'impregnare hidrofobă.'))
  + '<p>Mărimile 116-122 până la 164-166 acoperă aproximativ 6-14 ani.</p>',
  [('model', 'HILLSLOPE'), ('culoare', 'culoarea verde'), ('izolat', 'Model izolat confecționat material extrem de durabil'), ('Thermocore', 'Thermocore este un strat de izolare sintetic'),
   ('groasă', 'groasă'), ('Bluesign', 'Model certificat Bluesign® Standard'), ('Grow', 'Sistemul Grow'), ('centură', 'In interior este o centura flexibila, cauciucata'),
   ('velcro', 'Marginile inferioare ale mânecilor sunt reglabile cu Velcro'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('mânecă', 'Un buzunar suplimentar pe mânecă'), ('interior', 'Un buzunar interior suplimentar'), ('glugă', 'integrată'), ('material', '100% Poliamida'),
   ('umplutură', '95% Poliester reciclat, 5% Poliester'), ('hidrofob', 'impregnare hidrofobă')],
  {'Model': 'Burton HILLSLOPE', 'Material': '100% poliamidă', 'Caracteristici': 'Thermocore, sistem Grow, centură de zăpadă', 'Cod produs': '243131'},
  notes=['Pagina magazinului dă în titlu „culoarea verde”, iar în datele produsului „galben”.'])

w(13114,
  f'<p>Ghetele de iarnă {PRIMIGI} 2352700 bleumarin sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "ghete pentru băieți")} înalte, din piele întoarsă și textil, cu membrană GORE-TEX care apără de apă și vânt și lasă piciorul să respire. Colaborarea Primigi × SIPeP ține cont de anatomia piciorului copilului.</p>'
  '<p>Căptușeala textilă păstrează căldura, talpa din cauciuc ține bine pe suprafețele de iarnă, iar călcâiul e întărit. Se închid cu arici, iar branțurile se scot.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'piele întoarsă, material textil.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 25-26 se potrivesc în jur de 2-4 ani.</p>',
  [('cod', '2352700'), ('culoare', 'Culoare bleumarin'), ('înalte', 'încălțăminte înaltă de iarnă'), ('GORE-TEX', 'Tehnologia GORE-TEX® asigură protecție împotriva apei și a vântului'),
   ('respire', 'permițând în același timp picioarelor să respire'), ('SIPeP', 'Colaborarea Primigi × SIPeP'), ('anatomie', 'ține cont de anatomia piciorului copilului'),
   ('căptușeală', 'Căptușeala interioară din material textil'), ('talpă', 'Talpa din cauciuc'), ('iarnă', 'pe suprafețele de iarnă'), ('călcâi', 'Călcâiul întărit'),
   ('arici', 'Sistemul practic de închidere cu arici'), ('detașabile', 'Branțuri detașabile'), ('față', 'Partea superioară:Piele întoarsă, Material textil')],
  {'Model': 'Primigi 2352700', 'Membrană': 'GORE-TEX', 'Caracteristici': 'arici, călcâi întărit, profil înalt', 'Cod produs': '2352700'})

w(13118,
  f'<p>Cizmele {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} T1A5-34049 roz sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} cu profil înalt, din textil și material sintetic, neizolate, cu rezistență sporită la apă. Talpa groasă din cauciuc are caneluri și bandă de rulare antiderapantă.</p>'
  '<p>Vârful e puternic rigidizat, contrafortul rigid ține călcâiul, iar partea înaltă sprijină glezna. Șireturile elastice cu cârlig și velcro-ul le fac ușor de pus, iar inserția detașabilă se curăță ușor.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Lungime branț', '21,5 cm la numărul 33.'))
  + '<p>Numerele 30-34 merg cam la 6-11 ani.</p>',
  [('cod', 'T1A5-34049'), ('culoare', 'culoarea roz'), ('profil', 'înalt'), ('neizolat', 'Model Neizolat confecționat din combinația materialului textil cu cel sintetic'),
   ('apă', 'Impermeabil înseamnă rezistență sporită la apă'), ('caneluri', 'Talpa exterioară din cauciuc cu caneluri'), ('antiderapantă', 'cu bandă de rulare, antiderapantă'),
   ('groasă', 'groasă, profilată'), ('vârf', 'Varful puternic rigidizat'), ('călcâi', 'Contorul de călcâi rigid'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig'), ('velcro', 'Fixare: cu scai'), ('inserție', 'Inserție detașabilă, ușor de curățat'),
   ('gambă', 'Material sintetic, Material textil'), ('lungime', 'Lungimea brantului pentru marimea este de: 21,5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 33')],
  {'Model': 'Tommy Hilfiger T1A5-34049', 'Material': 'textil, material sintetic', 'Caracteristici': 'profil înalt, șireturi elastice, velcro', 'Cod produs': 'T1A5.34049'},
  notes=[NOAPA, 'Magazinul le numește „pantofi de iarnă”, dar spune că modelul e neizolat.'])

w(13120,
  f'<p>Geaca {A("/brand/tinycottons/", "Tinycottons")} CHECK PADDED JACKET portocalie este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} subțire, matlasată, din bumbac, cu izolație sintetică de grosime medie pentru temperaturile mai reci. Căptușeala e completă, din poliester.</p>'
  '<p>Fermoarul pe toată lungimea are clapă de furtună prinsă cu capse, mânecile sunt raglan, gulerul e moale, iar pe laterale sunt două buzunare. Nu are glugă, iar tăietura e simplă, fără blocare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Căptușeală', '100% poliester.'), ('Umplutură', '100% poliester.'))
  + '<p>Mărimile 92-152 corespund orientativ vârstei de 2-12 ani.</p>',
  [('model', 'CHECK PADDED JACKET'), ('culoare', 'culoarea portocaliu'), ('subțire', 'Model subțire confecționat din material matlasat cu izolatie sintetică'),
   ('reci', 'temperaturi mai reci'), ('medie', 'medie'), ('bumbac', '100% Bumbac'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă de furtună prinsă cu capse'), ('raglan', 'Mânecile raglan'), ('guler', 'Model cu guler moale'),
   ('buzunare', 'Două buzunare laterale'), ('glugă', 'fără glugă'), ('poliester', '100% Poliester')],
  {'Model': 'Tinycottons CHECK PADDED JACKET', 'Material': '100% bumbac', 'Caracteristici': 'matlasată, mâneci raglan, clapă cu capse', 'Cod produs': 'AW25.145'})
