import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
GEOX = A('/brand/geox/', 'Geox')
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
GU = '/categorie/unisex-imbracaminte-geci-jachete/'

w(13283,
  f'<p>Geaca {A("/brand/tinycottons/", "Tinycottons")} COLOR BLOCK PADDED JACKET maro este o {A(GU, "geacă unisex")} izolată, matlasată, din bumbac, cu izolație sintetică groasă pentru temperaturile mai reci. Căptușeala e completă, din poliester.</p>'
  '<p>Gulerul ridicat și gluga adaugă căldură, mânecile se termină cu elastic, iar buzunarele exterioare sunt oblice. Se închide cu fermoar și cleme, iar tăietura e simplă, fără blocare. Izolația groasă o face potrivită pentru iarnă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Umplutură', '100% poliester.'), ('Izolație', 'groasă.'))
  + '<p>Mărimile 92-152 se potrivesc cam între 2 și 12 ani.</p>',
  [('model', 'COLOR BLOCK PADDED JACKET'), ('culoare', 'culoarea maro'), ('izolat', 'Model izolat confecționat din material matlasat cu izolatie sintetică'),
   ('reci', 'temperaturi mai reci'), ('bumbac', '100% Bumbac'), ('groasă', 'groasă'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('glugă', 'Gluga încorporată oferă un plus de căldură'),
   ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('buzunare', 'Buzunare oblice exterioare'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('cleme', 'Incheiere cu cleme'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('umplutură', '100% Poliester')],
  {'Model': 'Tinycottons COLOR BLOCK PADDED JACKET', 'Material': '100% bumbac', 'Caracteristici': 'izolație groasă, glugă, guler ridicat', 'Cod produs': 'AW25.141'},
  notes=['Descrierea spune glugă „încorporată”, caracteristicile „detașabilă”; nu am precizat tipul glugii.'])

w(13286,
  f'<p>Hanoracul {TH} KB0KB10177 alb e printre {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluzele pentru băieți")}, din bumbac 100%, cu glugă și imprimeu. Tăietura e simplă, regular fit, ușor de purtat zi de zi.</p>'
  '<p>În față are un buzunar cangur, iar mânecile se termină cu manșetă. Gluga e integrată în decolteu, iar țesătura are imprimeu. Bumbacul 100% e plăcut pe piele, iar hanoracul se poartă zi de zi, peste un tricou.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Glugă', 'integrată.'), ('Buzunar', 'cangur, în față.'))
  + '<p>Mărimile 128-176 sunt potrivite orientativ între 8 și 16 ani.</p>',
  [('cod', 'KB0KB10177'), ('culoare', 'culoarea alb'), ('bumbac', '100% Bumbac'), ('glugă', 'Model cu gluga'), ('imprimeu', 'Model cu imprimeu'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('croială', 'Croială: regular fit'), ('cangur', 'Un buzunar cangur practic'), ('manșetă', 'Finisaj din manseta'), ('decolteu', 'Decolteu: integrat cu glugă')],
  {'Model': 'Tommy Hilfiger KB0KB10177', 'Material': '100% bumbac', 'Caracteristici': 'glugă, buzunar cangur, imprimeu', 'Cod produs': 'KB0KB10177'},
  notes=['Sursa are puține detalii despre hanorac.'])

w(13304,
  f'<p>Geaca {A("/brand/bobo-choses/", "Bobo Choses")} Tic Tac Toe albastră este o {A(GB, "geacă de iarnă pentru băieți")} izolată, cu umplutură sintetică groasă, din material modelat. Exteriorul e din poliamidă parțial reciclată, iar căptușeala completă din poliester parțial reciclat.</p>'
  '<p>Gulerul ridicat apără de frig, buzunarele exterioare sunt oblice, iar tăietura e simplă, fără blocare. Nu are glugă, deci în zilele cu vânt merge purtată cu o căciulă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă reciclată.'), ('Căptușeală', '100% poliester reciclat.'), ('Izolație', 'groasă.'))
  + '<p>Mărimile 89/98 până la 149/155 țin cam de 1-12 ani.</p>',
  [('model', 'Tic Tac Toe'), ('culoare', 'Culoare albastru'), ('izolat', 'Model izolat confecționat din material modelat'), ('umplutură', 'Model cu umplutură sintetică'),
   ('groasă', 'groasă'), ('poliamidă', 'realizat partial din poliamida reciclata'), ('poliester', 'realizat partial din poliester reciclat'),
   ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('buzunare', 'Buzunare oblice exterioare'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('glugă', 'fără glugă'), ('material', '100% Poliamida reciclata'), ('căptușeală', '100% Poliester reciclat')],
  {'Model': 'Bobo Choses Tic Tac Toe', 'Material': 'poliamidă reciclată', 'Caracteristici': 'izolație groasă, guler ridicat', 'Cod produs': '225AC124'},
  notes=['Titlul site-ului nu are culoare („Băieți”); culoarea e cea de la magazin (albastru). Produsul e marcat și „pentru bebe”.'])

w(13330,
  f'<p>Geaca de puf {TH} KB0KB09815 bleumarin este o {A(GB, "geacă puf pentru băieți")}, matlasată, din material neted, cu umplutură din puf de rață și pene, deci izolație groasă. Tăietura e lejeră, iar sigla mărcii decorează geaca.</p>'
  '<p>Are glugă, se închide cu fermoar, mânecile se termină cu elastic, iar buzunarele sunt oblice. Căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', '70% puf de rață, 30% pene.'), ('Izolație', 'groasă.'))
  + '<p>Mărimile 128-176 corespund cu aproximație vârstei de 8-16 ani.</p>',
  [('cod', 'KB0KB09815'), ('culoare', 'culoarea bleumarin'), ('puf', 'Umplutura din puf si pene'), ('matlasat', 'Model izolat confecționat din material matlasat'),
   ('neted', 'Material neted'), ('groasă', 'groasă'), ('lejeră', 'Tăiere lejeră, fără blocare'), ('siglă', 'Model cu sigla brandului'), ('glugă', 'Model cu gluga'),
   ('fermoar', 'Incheiere cu fermoar'), ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('buzunare', 'Buzunare oblice'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('material', '100% Poliester'), ('umplutură', '70% Duck Down, 30% Pene')],
  {'Model': 'Tommy Hilfiger KB0KB09815', 'Material': '100% poliester, puf de rață', 'Caracteristici': 'puf natural, glugă, croială lejeră', 'Cod produs': 'KB0KB09815'})

w(13339,
  f'<p>Cizmele {TH} T3X5-34125 maro sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} cu profil înalt, din material sintetic, neizolate. Talpa groasă din cauciuc are bandă de rulare antiderapantă, e durabilă și rezistentă la deteriorare.</p>'
  '<p>Se închid cu șiret, fermoar lateral și velcro, iar bucla de la spate ajută la încălțat. Vârful e rigidizat, iar branțul textil e confortabil și ține încălțămintea curată mai ușor.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic.'), ('Interior', 'material sintetic, material textil.'), ('Lungime branț', '22,5 cm la numărul 35.'))
  + '<p>Numerele 35-41 se poartă de pe la 10 ani în sus.</p>',
  [('cod', 'T3X5-34125'), ('culoare', 'culoarea maro'), ('profil', 'înalt'), ('neizolat', 'Model Neizolat confecționat din material sintetic'), ('groasă', 'groasă, profilată'),
   ('antiderapantă', 'cu bandă de rulare, antiderapantă'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'),
   ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('buclă', 'Bucla de la spate'), ('vârf', 'rigidizat'), ('branț', 'Brantul textil este confortabil'),
   ('gambă', 'Material sintetic'), ('lungime', 'Lungimea brantului pentru marimea este de: 22,5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 35')],
  {'Model': 'Tommy Hilfiger T3X5-34125', 'Talpă': 'cauciuc, antiderapantă', 'Caracteristici': 'profil înalt, șiret, fermoar, velcro', 'Cod produs': 'T3X5.34125'},
  notes=['Magazinul le numește „pantofi de iarnă”, dar spune că modelul e neizolat.'])

w(13342,
  f'<p>Cizmele de iarnă {GEOX} J169XC negre sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme pentru băieți")} izolate, din textil și piele ecologică, cu membrană impermeabilă și sistemul Geox Respira, cu talpă perforată în trei straturi pentru ventilare. Interiorul textil se păstrează ușor curat.</p>'
  '<p>Vârful rotund e întărit, contrafortul rigid ține călcâiul, iar talpa din cauciuc e durabilă. Velcro-ul și bucla de la spate le fac ușor de pus și de scos.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Lungime branț', '22 cm la numărul 34.'), ('Profil', 'înalt.'))
  + '<p>Numerele 28-35 merg cam la 4-11 ani.</p>',
  [('cod', 'J169XC'), ('culoare', 'culoarea negru'), ('izolat', 'Model Izolat confectionat din combinatia materialului textil cu pielea ecologica'), ('membrană', 'membrană impermeabilă'),
   ('Respira', 'Sistemul Geox Respira'), ('straturi', 'talpei in trei straturi cu sistemul de perforari'), ('interior', 'Model cu interior textil'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Contorul de călcâi rigid'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('velcro', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'),
   ('gambă', 'Material sintetic, Material textil'), ('lungime', 'Lungimea brantului pentru marimea este de: 22 cm'), ('mărime', 'Dimensiunile date pentru marimea: 34'), ('profil', 'înalt')],
  {'Model': 'Geox J169XC', 'Membrană': 'impermeabilă', 'Caracteristici': 'izolate, Geox Respira, velcro', 'Cod produs': 'J169XC.0FU50'})

w(13371,
  f'<p>Geaca de schi {A("/brand/rossignol/", "Rossignol")} SIZ QUILTED neagră este o {A(GB, "geacă de schi pentru băieți")} izolată, matlasată, din poliester reciclat, cu izolație groasă și membrană: 20000 mm coloană de apă și 15000 g/m2/24h respirabilitate. Înăuntru are centură flexibilă, cauciucată.</p>'
  '<p>Gulerul ridicat și gluga fixă apără de frig, fermoarul are clapă interioară și exterioară, iar manșetele se încheie. Jos are șnururi, pe mânecă buzunar de skipass, plus două buzunare laterale și unul interior.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Coloană de apă', '20000 mm.'), ('Respirabilitate', '15000 g/m2/24h.'))
  + '<p>Mărimile 140-170 corespund aproximativ vârstei de 10-15 ani.</p>',
  [('model', 'SIZ QUILTED'), ('culoare', 'culoarea negru'), ('schi', 'Geacă de schi pentru copii din colecția Rossignol'), ('izolat', 'Model izolat cu captuseala'),
   ('matlasat', 'Matlasat'), ('reciclat', '100% Poliester reciclat'), ('groasă', 'groasă'), ('coloană', 'Impermeabilitate: 20000 mm/m2/24h'), ('respirabil', 'Respirabilitate: 15000 g/m2/24h'),
   ('centură', 'In interior este o centura flexibila, cauciucata'), ('guler', 'Gulerul ridicat și gluga fixă'), ('fermoar', 'Închidere cu fermoar pe toată lungimea, cu clapă interioară și exterioară'),
   ('manșete', 'Maneci cu mansete incheiate'), ('șnur', 'Jos snururi'), ('skipass', 'Buzunar ski-pass pe maneca'), ('buzunare', 'Două buzunare laterale'),
   ('interior', 'Un buzunar interior suplimentar'), ('membrană', 'membrană impermeabilă')],
  {'Model': 'Rossignol SIZ QUILTED', 'Material': '100% poliester reciclat', 'Caracteristici': '20000 mm, centură de zăpadă, buzunar skipass', 'Cod produs': 'RLOYJ02'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(13436,
  f'<p>Același {A("/brand/karl-lagerfeld/", "Karl Lagerfeld")} Z31072 bej, de data asta în mărimile pentru adolescenți, rămâne o {A(GB, "geacă subțire pentru băieți")}: bumbac curat, cu imprimeu, moale la atingere, fără căptușeală și fără umplutură.</p>'
  '<p>Gulerul e moale, glugă nu are, iar fermoarul o închide pe față. Clapele decorează buzunarele, iar manșetele se încheie. Nu e impermeabilă. Mărimile urmează sistemul italian, așa că merită verificat tabelul.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Căptușeală', 'nu are.'), ('Izolație', 'nu are.'))
  + '<p>Mărimile 162-174 merg orientativ la 14-16 ani.</p>',
  [('cod', 'Z31072'), ('culoare', 'culoarea bej'), ('imprimeu', 'Model confecționat din material textil cu imprimeu'), ('moale', 'material moale și plăcut la atingere'),
   ('căptușeală', 'fără căptușeală'), ('umplutură', 'fără umplutură'), ('guler', 'Model cu guler moale'), ('glugă', 'fără glugă'), ('fermoar', 'Incheiere cu fermoar'),
   ('clape', 'Model cu buzunare, decorat cu clape'), ('manșete', 'Maneci cu mansete incheiate'), ('impermeabil', 'fără impermeabilitate'),
   ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '100% Bumbac'), ('izolație', 'fără izolație')],
  {'Model': 'Karl Lagerfeld Z31072', 'Material': '100% bumbac', 'Caracteristici': 'imprimeu, fermoar, buzunare cu clape', 'Cod produs': 'Z31072'})

w(13472,
  f'<p>Cizmele de zăpadă {GEOX} JUNSHEE PG A negre sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} izolate, din textil și piele ecologică, cu căptușeală moale din textil. Membrana Amphibiox e respirabilă și apără atât talpa, cât și fața, iar Geox Respira ventilează prin talpa perforată.</p>'
  '<p>Talpa ușoară din spumă EVA, cu exterior din cauciuc foarte durabil, preia șocurile. Vârful e întărit, contrafortul ține călcâiul, iar velcro-ul și bucla de la spate ajută la încălțat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 28-35 sunt gândite pentru aproximativ 4-11 ani.</p>',
  [('model', 'JUNSHEE PG A'), ('culoare', 'culoarea negru'), ('izolat', 'Model Izolat din combinația materialului textil cu pielea ecologică'), ('căptușeală', 'căptușeală moale din material textil'),
   ('Amphibiox', 'Tehnologia Amphibiox®'), ('membrană', 'Membrana special respirabila si nepermeabila protejeaza atat talpa exterioara, cat si cea superioara'),
   ('Respira', 'Sistemul Geox Respira'), ('EVA', 'Talpa usoara, de amortizare din spuma EVA'), ('cauciuc', 'Talpa din cauciuc este extrem de durabilă'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid'), ('velcro', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'),
   ('gambă', 'Material sintetic, Material textil'), ('profil', 'înalt')],
  {'Model': 'Geox JUNSHEE PG A', 'Membrană': 'Amphibiox', 'Caracteristici': 'izolate, talpă EVA, velcro', 'Cod produs': 'J46D8A.0MEFU'},
  notes=['Pagina magazinului dă în titlu „culoarea negru”, iar în datele produsului „verde”.'])

w(13532,
  f'<p>Cizmele de iarnă {TH} T3A5-34050 bej sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} izolate, din textil, material sintetic și piele ecologică, cu căptușeală textilă moale. Talpa groasă din cauciuc are bandă de rulare antiderapantă și e foarte durabilă.</p>'
  '<p>Partea înaltă sprijină glezna pe teren neuniform, vârful rotund e întărit, iar spatele călcâiului e puternic rigidizat. Au șiret și fermoar lateral.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material sintetic, material textil.'), ('Lungime branț', '22 cm la numărul 34.'))
  + '<p>Numerele 30-34 se potrivesc în jur de 6-11 ani.</p>',
  [('cod', 'T3A5-34050'), ('culoare', 'culoarea bej'), ('izolat', 'Model Izolat'), ('materiale', 'combinatie de material textil, material sintetic și piele ecologică'),
   ('căptușeală', 'căptușeală moale din material textil'), ('groasă', 'groasă, profilată'), ('antiderapantă', 'cu bandă de rulare, antiderapantă'),
   ('talpă', 'Talpa din cauciuc este extrem de durabilă'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Spatele calcaiului peternic rigidizat'), ('fermoar', 'Model cu siret cu fermoar lateral'), ('gambă', 'Material sintetic, Material textil'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 22 cm'), ('mărime', 'Dimensiunile date pentru marimea: 34')],
  {'Model': 'Tommy Hilfiger T3A5-34050', 'Talpă': 'cauciuc, antiderapantă', 'Caracteristici': 'izolate, șiret și fermoar lateral', 'Cod produs': 'T3A5.34050'})
