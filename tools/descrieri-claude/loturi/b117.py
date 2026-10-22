import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
PP = A('/brand/patrizia-pepe/', 'Patrizia Pepe')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
GORE = 'Magazinul descrie membrana ca 100% impermeabilă, dar are și formula că nu garantează impermeabilitatea completă; nu am scris „impermeabile”.'

w(10138,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IG0IG03022 bej este o {A(GF, "geacă de tranziție pentru fete")} subțire, din poliamidă netedă, cu umplutură sintetică de grosime medie și căptușeală completă. Gulerul ridicat și gluga încorporată apără de frig.</p>'
  '<p>Tăietura e simplă, iar fermoarul o face ușor de pus și de scos. E potrivită pentru zilele de primăvară sau toamnă, când e prea frig pentru un hanorac.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Izolație', 'medie.'), ('Croială', 'regular fit.'))
  + '<p>Între 128 și 170, mărimile țin cam de la 8 până la 15 ani.</p>',
  [('cod', 'IG0IG03022'), ('culoare', 'culoarea bej'), ('subțire', 'Model subțire confecționat din material neted'), ('umplutură', 'sintetică'), ('medie', 'medie'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('glugă', 'Gluga încorporată'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'îl face ușor de pus și scos'), ('material', '100% Poliamida'), ('croială', 'Croială: regular fit'),
   ('tranziție', 'Izolare: tranzitional')],
  {'Model': 'Calvin Klein Jeans IG0IG03022', 'Material': '100% poliamidă', 'Caracteristici': 'subțire, glugă, guler ridicat', 'Cod produs': 'IG0IG03022'},
  notes=['„Primăvară sau toamnă” derivă din atributul „tranzițional”.'])

w(10165,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8881633 aurii sunt {A("/categorie/ghete-cizme/", "cizme de iarnă pentru fete")} izolate, din material sintetic și piele întoarsă, cu membrană GORE-TEX subțire, rezistentă la vânt și respirabilă. Branțul detașabil e din lână, cu contur, și preia șocurile.</p>'
  '<p>Carâmbul înalt ține glezna pe suprafețe neuniforme, vârful e lat și rigidizat, iar talpa din cauciuc are bandă de rulare antiderapantă. Velcro-ul le face ușor de pus și de scos.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, piele întoarsă.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 31-35 merg, orientativ, la copiii de 6-11 ani.</p>',
  [('cod', '8881633'), ('culoare', 'culoarea auriu'), ('izolat', 'Izolare: izolat'), ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire'),
   ('vânt', 'rezistenta la vant si respirabila'), ('lână', 'lână, cu absorbție a șocurilor'), ('detașabil', 'Branțuri detașabile'), ('contur', 'Brant confortabil, cu contur'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('vârf', 'Cutia lată a degetelor previne ciupirea degetelor'), ('rigidizat', 'rigidizat'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('antiderapantă', 'cu bandă de rulare, antiderapantă'), ('velcro', 'Închiderea cu velcro'),
   ('gambă', 'Material sintetic, Piele intoarsa'), ('profil', 'înalt')],
  {'Model': 'Primigi 8881633', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, branț din lână, velcro', 'Cod produs': '8881633'},
  notes=[GORE])

w(10254,
  f'<p>Geaca {PP} 7O0041 albastră este o {A(GF, "geacă subțire pentru fete")}, din imitație de blană, cu decolteu rotund, fără glugă. Are căptușeală și se încheie cu cârlige, iar tăietura e simplă.</p>'
  '<p>Magazinul precizează că nu e impermeabilă, deci e o haină pentru zilele uscate de toamnă sau primăvară. Mărimile sunt italienești, raportate la cele europene, așa că e bine de verificat tabelul magazinului înainte.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Închidere', 'cârlige.'), ('Decolteu', 'rotund.'))
  + '<p>Pentru 130-168, vârsta e orientativ de 8-15 ani.</p>',
  [('cod', '7O0041'), ('culoare', 'Culoare albastru'), ('blană', 'Model subțire confecționat din imitatie de blana'), ('decolteu', 'Decolteu clasic, rotund'),
   ('glugă', 'Gluga: fara gluga'), ('căptușeală', 'Model cu captuseala'), ('cârlige', 'Incheiere cu carlige'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('impermeabil', 'fără impermeabilitate'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '100% Poliester')],
  {'Model': 'Patrizia Pepe 7O0041', 'Material': '100% poliester, imitație de blană', 'Caracteristici': 'subțire, decolteu rotund, cârlige', 'Cod produs': '7O0041'},
  notes=['Titlul site-ului nu are culoare; culoarea e cea de la magazin (albastru).', '„Toamnă sau primăvară” e dedus din atributul „tranzițional”.'])

w(10264,
  f'<p>Varianta bej a cizmelor de zăpadă {PRIMIGI} 8858966 face parte tot din {A("/categorie/ghete-cizme/", "cizmele de iarnă pentru fete")}: ușor izolate, din material sintetic și piele naturală, cu membrană GORE-TEX respirabilă și rezistentă la vânt.</p>'
  '<p>Contrafortul rigidizat sprijină glezna și călcâiul, vârful lat și rigidizat lasă loc degetelor, iar partea înaltă ține glezna pe teren denivelat. Talpa din cauciuc e antiderapantă și durabilă, iar închiderea e cu arici.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, piele naturală.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>La numerele 25-29, vârsta e în jur de 2-5 ani.</p>',
  [('cod', '8858966'), ('culoare', 'culoarea bej'), ('izolat', 'Izolare: usor izolat'), ('GORE-TEX', 'Model cu membrana GORE-TEX®'), ('vânt', 'rezistenta la vant si respirabila'),
   ('contrafort', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), ('vârf', 'Cutia lată a degetelor'), ('rigidizat', 'rigidizat'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('antiderapantă', 'cu bandă de rulare, antiderapantă'),
   ('arici', 'cu arici'), ('gambă', 'Material sintetic, Piele naturala'), ('interior', 'Material textil'), ('profil', 'înalt')],
  {'Model': 'Primigi 8858966', 'Membrană': 'GORE-TEX', 'Caracteristici': 'ușor izolate, arici, talpă antiderapantă', 'Cod produs': '8858966'},
  notes=[GORE])

w(10271,
  f'<p>Paltonul {A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 323970093001 bleumarin, listat la {A(GB, "geci pentru băieți")}, e făcut dintr-un material care apără de frig, cu izolație groasă și fibre reciclate. Are glugă încorporată și căptușeală completă, sintetică.</p>'
  '<p>Tăietura e simplă, fermoarul îl face ușor de pus și de scos, iar pe laterale are două buzunare. Gluga încorporată adaugă căldură și acoperire când e nevoie.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Izolație', 'groasă.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 136-138 până la 163-174 sunt gândite, cu aproximație, pentru 9-16 ani.</p>',
  [('cod', '323970093001'), ('culoare', 'culoarea bleumarin'), ('frig', 'Model izolat confecționat material care protejează împotriva frigului'), ('groasă', 'groasă'),
   ('reciclat', 'Produsul contine materiale realizate din fibre reciclate'), ('glugă', 'Gluga încorporată'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('buzunare', 'Două buzunare laterale'),
   ('material', '100% Poliester reciclat'), ('croială', 'Croială: regular fit')],
  {'Model': 'Polo Ralph Lauren 323970093001', 'Material': '100% poliester reciclat', 'Caracteristici': 'izolație groasă, glugă, fermoar', 'Cod produs': '323970093001'},
  notes=['Magazinul îl numește o dată „palton”, o dată „geacă”, și spune o dată „izolat”, o dată „neizolat”; am urmat caracteristicile (izolație groasă).'])

w(10286,
  f'<p>Din aceeași serie {PP}, codul 7O0045 negru este o {A(GF, "geacă izolată pentru fete")}, din material neted, cu umplutură sintetică de grosime medie spre mare, pentru temperaturile mai reci. Căptușeala e din poliamidă.</p>'
  '<p>Gluga e încorporată, gulerul e ridicat, iar mânecile se termină cu o bandă elastică. Fermoarul o face ușor de îmbrăcat. Mărimile urmează sistemul italian, raportat la cel european.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', '100% poliamidă.'), ('Umplutură', '100% poliester.'))
  + '<p>Pentru 130-168, vârsta potrivită e cam 8-15 ani.</p>',
  [('cod', '7O0045'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat confecționat din material neted cu izolație sintetică'), ('reci', 'temperaturi mai reci'),
   ('groasă', 'medie, groasă'), ('căptușeală', '100% Poliamida'), ('glugă', 'Gluga încorporată'), ('guler', 'Gulerul ridicat'), ('mâneci', 'Mâneci finisate cu o coadă elastică'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '100% Poliester')],
  {'Model': 'Patrizia Pepe 7O0045', 'Material': '100% poliester, căptușeală din poliamidă', 'Caracteristici': 'izolată, glugă, guler ridicat', 'Cod produs': '7O0045'})

w(10327,
  f'<p>Geaca {A("/brand/columbia/", "Columbia")} Puffect roz este o {A(GF, "geacă puf pentru fete")}, izolată, din țesătură netedă, cu umplutură din poliester 100% reciclat, de grosime medie spre mare. Căptușeala e din nailon.</p>'
  '<p>Gulerul ridicat și gluga fixă apără de frig, iar fermoarul pe toată lungimea are clapă interioară împotriva furtunii. Mânecile au manșetă, cele două buzunare laterale au fermoar, iar detaliile reflectorizante ajută la vizibilitate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', '100% nailon.'), ('Umplutură', '100% poliester reciclat.'))
  + '<p>Mărimile 104-164 se potrivesc, cu aproximație, la 4-14 ani.</p>',
  [('model', 'Puffect'), ('culoare', 'culoarea roz'), ('izolat', 'Model izolat confecționat din tesatura neteda'), ('reciclat', 'Model cu umplutura din poliester reciclat 100%'),
   ('groasă', 'medie, groasă'), ('căptușeală', '100% Nailon'), ('guler', 'Gulerul ridicat și gluga fixă'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară împotriva furtunii'),
   ('manșetă', 'Manecile finisate cu manseta'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('reflectorizant', 'Reflectorizante'),
   ('material', '100% Poliester'), ('umplutură', '100% Poliester reciclat')],
  {'Model': 'Columbia Puffect', 'Material': '100% poliester, umplutură reciclată', 'Caracteristici': 'puf sintetic, glugă fixă, reflectorizante', 'Cod produs': '2096272'})

w(10333,
  f'<p>Geaca {A("/brand/levis/", "Levi's")} SHINY HVWT PUFFER roz este o {A(GF, "geacă puf pentru fete")}, lucioasă, ușor izolată, din material matlasat cu izolație sintetică pentru zilele mai reci. Gulerul ridicat și gluga fixă apără capul și gâtul.</p>'
  '<p>Se închide cu fermoar, are buzunare oblice, iar mânecile se termină cu elastic. Căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '56 cm la mărimea 140.'), ('Lățime la subraț', '45 cm.'))
  + '<p>Mărimile 140-164 corespund aproximativ vârstei de 10-14 ani.</p>',
  [('model', 'SHINY HVWT PUFFER'), ('culoare', 'culoarea roz'), ('izolat', 'Model ușor izolat confecționat din material matlasat cu izolatie sintetică'),
   ('reci', 'temperaturi mai reci'), ('guler', 'Gulerul ridicat și gluga fixă'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare oblice'),
   ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 56 cm'),
   ('mărime', 'Dimensiunile date pentru marimea: 140'), ('subraț', 'Latimea la subrat: 45 cm')],
  {'Model': "Levi's SHINY HVWT PUFFER", 'Material': '100% poliester', 'Caracteristici': 'lucioasă, matlasată, glugă fixă', 'Cod produs': '4EN640'},
  notes=['„Lucioasă” e dedus din numele modelului (SHINY).'])

w(10343,
  f'<p>Geaca reversibilă {A("/brand/liewood/", "Liewood")} LW17576 portocalie este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă pentru bebeluși")} ușor izolată, cu două fețe în culori diferite, care se poate purta pe ambele părți. E din poliester reciclat, cu finisaj hidrofob BIONIC-FINISH ECO.</p>'
  '<p>Se închide cu fermoar, gulerul ridicat apără de frig, iar gluga e integrată. Buzunarele sunt oblice, iar căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Izolație', 'ușoară.'), ('Croială', 'regular fit.'))
  + '<p>De la 80 la 140, mărimile acoperă orientativ 1-10 ani.</p>',
  [('cod', 'LW17576'), ('culoare', 'culoarea portocaliu'), ('reversibil', 'Model cu două fețe, asigurând funcționalitate deplină în utilizare pe ambele părți'),
   ('culori', 'din stofa in diferite culori'), ('izolat', 'Model usor izolat'), ('reciclat', 'Acest produs este fabricat din poliester reciclat'), ('BIONIC', 'BIONIC-FINISH® ECO'),
   ('fermoar', 'Incheiere cu fermoar'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('glugă', 'integrată'), ('buzunare', 'Buzunare oblice'),
   ('material', '100% Poliester reciclat'), ('croială', 'Croială: regular fit')],
  {'Model': 'Liewood LW17576', 'Material': '100% poliester reciclat', 'Caracteristici': 'reversibilă, BIONIC-FINISH ECO, glugă', 'Cod produs': 'LW17576'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(10411,
  f'<p>Geaca de iarnă {A("/brand/didriksons/", "Didriksons")} FALKEN KIDS JKT maro este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, pentru sporturi de iarnă, din poliamidă cu membrană, rezistentă la vânt și apă: 6 000 mm coloană de apă și respirabilitate de 4 000 g/m2/24h.</p>'
  '<p>Gluga se detașează, fermoarul are apărătoare pentru bărbie, iar manșetele elastice au velcro și găuri pentru degetul mare. Are buzunar de skipass pe mânecă, buzunar pe piept, bucle pentru mănuși, talie cu șnur și elemente reflectorizante.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Umplutură', '100% poliester.'), ('Izolație', 'medie spre groasă.'))
  + '<p>Mărimile 100-140 se potrivesc cam la 3-10 ani.</p>',
  [('model', 'FALKEN KIDS JKT'), ('culoare', 'culoarea maro'), ('izolat', 'Model izolat'), ('iarnă', 'Sporturi de iarnă'), ('vânt', 'Materialul exterior este rezistent la vânt și apă'),
   ('coloană', 'Impermeabilitate: 6 000 mm'), ('respirabil', 'Respirabilitate: 4 000 g/m2/24h'), ('glugă', 'Gluga detasabila'), ('bărbie', 'apărătoare pentru bărbie'),
   ('degetul', 'Manșete elastice cu găuri pentru degetul mare'), ('velcro', 'Manșetele elastice cu ajustare cu velcro'), ('skipass', 'Buzunar funcțional pentru permis de schi'),
   ('piept', 'Un buzunar la piept cu fermoar'), ('mănuși', 'Buclele pentru agățarea mănușilor'), ('talie', 'Ajustare în talie cu șnur'),
   ('reflectorizant', 'Elementele reflectorizante'), ('material', '100% Poliamida'), ('umplutură', '100% Poliester'), ('groasă', 'medie, groasă')],
  {'Model': 'Didriksons FALKEN KIDS JKT', 'Material': '100% poliamidă', 'Caracteristici': '6 000 mm, glugă detașabilă, buzunar skipass', 'Cod produs': '505849'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă. Produsul e marcat și „pentru bebe”.'])
