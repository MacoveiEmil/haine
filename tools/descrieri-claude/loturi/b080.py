import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
CURAT = ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')

w(12912,
  f'<p>Ghetele de iarnă {A("/brand/biomecanics/", "Biomecanics")} 261253 bleumarin sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "ghete pentru băieți")} înalte, din piele naturală, piele întoarsă și material textil, cu căptușeală de lână care ține de cald. Magazinul precizează că nu sunt impermeabile, ca să lase aerul să treacă.</p>'
  '<p>Aricii fac încălțatul rapid, iar călcâiul întărit și gulerul ajută la un pas sigur. Vârful rotund lasă degetele să se miște.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Branțuri', 'detașabile.'), ('Podology Partnership', 'dezvoltată cu podologi.'))
  + '<p>Numerele 28-34 sunt pentru băieți de aproximativ 4-11 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii bleumarin 261253'), ('înalt', 'Partea superioară înaltă , realizată din piele naturală, piele întoarsă și material textil'),
   ('lână', 'Căptușeală interioară din lână'), ('impermeabil', 'Fără impermeabilitate, ceea ce permite o circulație liberă a aerului'),
   ('arici', 'Închidere practică cu arici'), ('călcâi', 'Călcâi întărit și gulerul superior al feței susțin stabilizarea piciorului, sprijinind un pas sigur'),
   ('vârf', 'Vârful rotund favorizează libertatea de mișcare a degetelor'), ('talpă', 'Talpă plată din cauciuc'), ('branț', 'branțuri detașabile'),
   ('Podology', 'Tehnologia Biomecanics Podology Partnership , dezvoltată împreună cu podologi')],
  {'Model': 'Biomecanics 261253', 'Material': 'piele naturală, piele întoarsă și textil, căptușeală din lână', 'Caracteristici': 'ghete de iarnă, arici, neimpermeabile', 'Cod produs': '261253'})

w(12915,
  f'<p>Blugii {TH} BARREL KG0KG09182 sunt {A("/categorie/pantaloni-treninguri/", "blugi pentru fete")} albaștri, cu croială lejeră barrel leg și efect de uzură, din denim rigid de bumbac, care își ține forma. Talia e normală și stă confortabil pe șolduri.</p>'
  '<p>Se închid cu fermoar și nasture, iar pe buzunarul din spate e steagul Tommy Hilfiger în formă de stea.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '100% bumbac.'), ('Croială', 'barrel leg, lejeră.'), ('Talie', 'normală.'))
  + '<p>Mărimile 128-176 sunt pentru fete de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Blugi pentru copii BARREL albaștri KG0KG09182'), ('barrel', 'Croiala barrel leg conferă un aspect modern și lejer'), ('uzură', 'un efect de uzură'),
   ('denim', 'Confecționarea din denim rigid permite menținerea formei'), ('talie', 'Talie normală asigură o așezare confortabilă pe șolduri'),
   ('închidere', 'Sistemul practic de închidere cu fermoar și nasture'), ('steag', 'Steagul Tommy Hilfiger în formă de stea pe buzunarul din spate'),
   ('material', '100% Bumbac'), ('lejer', 'Croială lejeră favorizează libertatea deplină de mișcare')],
  {'Model': 'Tommy Hilfiger BARREL', 'Material': '100% bumbac (denim rigid)', 'Caracteristici': 'croială barrel leg, efect de uzură, talie normală', 'Cod produs': 'KG0KG09182'})

w(12920,
  f'<p>{GEOX} THELEVEN J56HTA gri vin și în numerele 28-35: {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, făcuți din piele naturală și ecologică, gândiți pentru fiecare zi. Nu trebuie legați, pentru că au șireturi elastice cu cârlig.</p>'
  '<p>În față, cutia rotundă e întărită, iar la spate contrafortul rigid împiedică alunecarea călcâiului. Sunt ușori și confortabili.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Exterior', 'piele naturală și sintetic.'), ('Căptușeală', 'textilă, se curăță ușor.'), ('Talpă', 'cauciuc rezistent la deteriorare.'))
  + '<p>Se potrivesc fetelor de vreo 4-11 ani, orientativ.</p>',
  [('model', 'Geox Sneakers pentru copii THELEVEN culoarea gri, J56HTA.077BC'), ('profil', 'Înălțime: jos'), ('material', 'combinația pielii naturale cu cea ecologică'),
   ('zilnic', 'ideal pentru purtarea zilnică'), ('ușor', 'Model ușor și confortabil'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid stabilizează călcâiul și ține piciorul în pantof, astfel încât să nu alunece'),
   ('gamba', 'Material sintetic, Piele naturala'), CURAT, TALPA],
  {'Model': 'Geox THELEVEN', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, vârf întărit', 'Cod produs': 'J56HTA.077BC'})

w(12921,
  f'<p>Adidașii {TH} T1X9-34369 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} multicolori, cu profil jos, din material sintetic și textil, ușori, cu panouri din plasă pentru aerisire. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos.</p>'
  '<p>Bucla de la spate ajută la încălțat, iar călcâiul întărit are umplutură moale care îl apără de frecare.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Vârf', 'cutie rotundă, ușor întărită.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 30-34 se potrivesc copiilor de cam 6-11 ani; la 30 branțul are 19,5 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii T1X9-34369'), ('culoare', 'Culoare multicolor'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatia materialului sintetic cu cel textil'),
   ('ușor', 'Model ușor și confortabil'), ('plasă', 'Panourile din plasă ajută la ventilație'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'),
   ('vârf', 'Cutie rotunda, usor intarita'), CURAT, TALPA, ('lungime', 'Lungimea brantului pentru marimea este de: 19.5 cm')],
  {'Model': 'Tommy Hilfiger T1X9-34369', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, panouri din plasă', 'Cod produs': 'T1X9-34369'})

w(12922,
  f'<p>{GEOX} WASHIBA bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu profil jos, din material textil și piele ecologică, ușori, pentru purtarea zilnică. Șireturile elastice și cârligul permit încălțatul fără legat, iar bucla de la spate ajută la tras pantoful.</p>'
  '<p>Cutia rotundă, întărită, apără degetele, iar călcâiul puternic rigid ține piciorul în pantof.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi cu perforări.'), ('Inserție', 'textilă, detașabilă, ușor de curățat.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 24-27 sunt pentru băieți de aproximativ 2-4 ani; la 24 branțul are 16 cm.</p>',
  [('model', 'Geox Sneakers pentru copii WASHIBA culoarea albastru marin'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatia materialului textil cu pielea ecologica'),
   ('ușor', 'Model ușor și confortabil'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Călcâiul puternic rigid stabilizează călcâiul'),
   RESPIRA, ('inserție', 'Inserție textilă detașabilă, ușor de curățat'), TALPA, ('lungime', 'Lungimea brantului pentru marimea este de: 16 cm')],
  {'Model': 'Geox WASHIBA', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira, inserție detașabilă', 'Cod produs': ''})

w(12924,
  f'<p>Adidașii {TH} T1X9-34366 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} în culoarea albastru, cu profil jos, din material textil și piele ecologică, care se închid cu velcro. Cutia rotundă e întărită și apără degetele la joacă.</p>'
  '<p>Contrafortul rigidizat sprijină călcâiul și glezna, iar interiorul textil se păstrează curat ușor.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Talpă', 'din cauciuc, durabilă.'), ('Închidere', 'velcro.'), ('Partea de sus', 'imitație de piele și textil.'))
  + '<p>Numerele 30-34 sunt pentru copii de în jur de 6-11 ani; la 31 branțul are 20,5 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii T1X9-34366'), ('culoare', 'Culoare albastru'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), CURAT, ('talpă', 'talpă din cauciuc care este durabilă'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 20,5 cm')],
  {'Model': 'Tommy Hilfiger T1X9-34366', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, vârf întărit', 'Cod produs': 'T1X9-34366'})

w(12925,
  f'<p>{GEOX} GISLI J465CC verzi sunt {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi pentru băieți")} descriși de magazin ca ghete de iarnă, din imitație de piele și material textil, care se închid cu arici. Tehnologia GEOX Respira scoate umezeala și ține picioarele uscate chiar și la joacă intensă.</p>'
  '<p>Gulerul ușor întărit sprijină glezna, iar călcâiul ușor întărit ține piciorul corect în gheată.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'material textil.'), ('Interior', 'textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 28-35 se potrivesc băieților de cam 4-11 ani.</p>',
  [('model', 'Geox Încălțăminte pentru copii GISLI verde J465CC.0MEFU'), ('iarnă', 'Ghetele de iarnă pentru copii Geox GISLI'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('arici', 'Închiderea practică cu arici'), ('Respira', 'Tehnologia GEOX Respira™ contribuie la eliminarea umidității, menținând picioarele uscate'),
   ('joacă', 'chiar și în timpul jocurilor intense'), ('guler', 'Gulerul ușor întărit al părții superioare susține stabilizarea gleznei'),
   ('călcâi', 'Călcâiul ușor întărit contribuie la poziționarea corectă a piciorului în gheată'), ('branț', 'Branțul din material textil'), ('interior', 'Material textil'),
   ('talpă', 'Talpa de cauciuc plată')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici', 'Cod produs': 'J465CC.0MEFU'},
  notes=['Magazinul îi descrie drept ghete de iarnă; pe site sunt la Pantofi.'])

w(12926,
  f'<p>Același {GEOX} LOFTUS J65M2B, dar în roz: {A("/categorie/adidasi/", "adidași pentru fete")} joși și ușori, cu fața din textil și material sintetic, buni pentru zi de zi. Șireturile sunt elastice și au cârlig, deci nu se desfac la joacă.</p>'
  '<p>Vârful are cutie rotundă ușor întărită, iar contrafortul rigid nu lasă călcâiul să alunece.</p>'
  '<p>Talpa și căptușeala:</p>'
  + L(('Geox Respira', 'talpă în trei straturi perforate.'), ('Căptușeală', 'textilă, ușor de curățat.'), ('Talpă exterioară', 'cauciuc rezistent.'))
  + '<p>Mărimile 28-35 sunt gândite pentru fete de pe la 4 până pe la 11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii LOFTUS culoarea roz, J65M2B.0BC14'), ('profil', 'Înălțime: mic de statură'), ('ușor', 'Model ușor și confortabil'),
   ('material', 'combinația materialului textil cu cel sintetic'), ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('vârf', 'Cutie rotunda, usor intarita'),
   ('călcâi', 'Contorul de călcâi rigid stabilizează călcâiul și ține piciorul în pantof'), RESPIRA, CURAT, TALPA],
  {'Model': 'Geox LOFTUS', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J65M2B.0BC14'})

w(12930,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IG0IG02987 neagră este o {A("/categorie/geci-jachete/", "geacă pentru fete")} izolată, matlasată, din material neted, cu glugă și căptușeală, care conține fibre reciclate. Izolația sintetică ține de cald la temperaturi mai scăzute.</p>'
  '<p>Mânecile au margine elastică și se strâng suplimentar cu velcro, contra frigului și umezelii. Se închide cu fermoar, iar căptușeala e tot din poliester.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două, laterale, cu capse.'), ('Material', '100% poliester.'), ('Bandă elastică', 'din poliester reciclat.'))
  + '<p>Mărimile 128-170 sunt pentru fete de aproximativ 8-15 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă copii culoarea negru, IG0IG02987'), ('izolat', 'Model izolat confecționat din material neted'), ('matlasat', 'Model matlasat cu izolație sintetică'),
   ('glugă', 'Gluga: cu gluga'), ('căptușeală', 'Captuseala: cu captuseala'), ('reciclat', 'materiale realizate din fibre reciclate'),
   ('velcro', 'o ajustare suplimentară cu velcro'), ('fermoar', 'Încheiere cu fermoar'), ('buzunare', 'Două buzunare laterale'),
   ('material', 'Materialul de baza: 100% Poliester'), ('căptușeală 2', 'Captuseala: 100% Poliester'), ('bandă', 'Banda elastica: 100% Poliester reciclat')],
  {'Model': 'Calvin Klein Jeans IG0IG02987', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, glugă, manșete cu velcro', 'Cod produs': 'IG0IG02987'})

w(12931,
  f'<p>În bleumarin și în numerele 36-41, {GEOX} PERTH J367RE sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} pentru adolescenți, cu fața din imitație de piele, rezistentă și ușor de întreținut. Talpa patentată GEOX Respira lasă umezeala să iasă și nu lasă apa să intre.</p>'
  '<p>Aricii merg împreună cu șireturile elastice, iar gulerul moale stă bine pe gleznă. Căptușeala textilă e plăcută la purtare.</p>'
  '<p>Construcția, în trei puncte:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Călcâi', 'întărit.'), ('Talpă', 'cauciuc plat, stabil.'))
  + '<p>Se potrivesc băieților de la aproximativ 12 ani în sus.</p>',
  [('model', 'Geox PERTH sneakers pentru copii bleumarin J367RE.0MEMS'), ('imitație', 'Partea superioară din imitație de piele oferă durabilitate și un aspect estetic, ușor de întreținut'),
   ('Respira', 'Tehnologia patentată GEOX Respira™'), ('membrană', 'Membrană microporoasă elimină eficient umezeala, protejând în același timp de apă din exterior'),
   ('închidere', 'Închiderea cu arici în combinație cu șireturile elastice'), ('guler', 'Gulerul moale al părții superioare îmbrățișează delicat glezna'),
   ('căptușeală', 'Interior din material textil asigură moliciune'), ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpa plată din cauciuc favorizează o bună aderență și stabilitate')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici și șireturi elastice', 'Cod produs': 'J367RE.0MEMS'})
