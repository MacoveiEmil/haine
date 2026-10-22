import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
CURAT = ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')

w(12611,
  f'<p>{REIMA} Vaellus violet sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} de drumeție, cu construcție Barefoot, ușori, care lasă piciorul să se miște liber și întăresc mușchii, cu profil până la gleznă. Talpa flexibilă din cauciuc ține bine pe mai multe tipuri de teren, iar zona cauciucată din jurul degetelor apără de zgârieturi.</p>'
  '<p>Înșiretarea rapidă îl lasă pe copil să se încalțe singur și să strângă pantoful pe picior.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Branț', 'EVA, profilat, detașabil, cu imprimeu pentru verificarea mărimii.'), ('Partea de sus', 'textil și material sintetic.'), ('Interior', 'material textil.'))
  + '<p>Numerele 28-38 se poartă, orientativ, de la 4 ani în sus.</p>',
  [('model', 'Reima Pantofi pentru copii Vaellus violet 5400173A'), ('drumeție', 'Ghetele de drumeție Reima Barefoot'), ('ușor', 'o încălțăminte ușoară pentru copii'),
   ('Barefoot', 'Construcția Barefoot favorizează dezvoltarea naturală a piciorului, permițând mișcarea liberă și întărirea mușchilor'),
   ('gleznă', 'cu profil până la gleznă'), ('talpă', 'Talpa flexibilă din cauciuc'), ('suprafețe', 'pe mai multe suprafețe'),
   ('degete', 'Zona cauciucată din jurul degetelor ajută la protejarea împotriva abraziunilor'), ('înșiretare', 'Sistemul de înșiretare rapidă permite o încălțare ușoară și rapidă'),
   ('branț', 'Branțurile EVA profilate, detașabile , cu imprimeu pentru verificarea mărimii'), ('material', 'Partea superioară din material textil și sintetic'), ('interior', 'Material textil')],
  {'Model': 'Reima Vaellus', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Barefoot, înșiretare rapidă, branț EVA detașabil', 'Cod produs': '5400173A'},
  notes=['Magazinul îi numește „ghete de drumeție”, pe site sunt la Pantofi; profil până la gleznă.'])

w(12614,
  f'<p>Geaca {A("/brand/donsje/", "Donsje")} Suzan Jacket portocalie este o {A("/categorie/geci-jachete/", "geacă pentru fete")} izolată, matlasată, din material neted și rezistent, cu căptușeală. Nu are glugă, dar gulerul ridicat are o bandă de protecție pe fermoar, ca să nu intre vântul.</p>'
  '<p>Mânecile se termină cu manșetă, iar croiala e simplă, dreaptă. Pe lângă poliester, unele detalii au și lână, nailon și acril.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Exterior', '100% poliester.'), ('Căptușeală și umplutură', 'poliester.'), ('Alte materiale', '45% nailon, 35% lână, 20% acril.'))
  + '<p>Mărimile 104-128 sunt pentru fete de în jur de 4-8 ani.</p>',
  [('model', 'Donsje Geacă copii Suzan Jacket culoarea portocaliu, 4106200'), ('izolat', 'Model izolat cu captuseala'), ('matlasat', 'Matlasat'), ('neted', 'Material neted'),
   ('rezistent', 'material rezistent'), ('glugă', 'Gluga: fara gluga'), ('guler', 'Guler ridicat cu membrana pe fermoar'), ('manșete', 'Manecile finisate cu manseta'),
   ('croială', 'Tăiere simplă, fără blocare'), ('exterior', 'Material de bază: 100% Poliester'), ('alte', '45% Nailon, 35% Lana, 20% Acril')],
  {'Model': 'Donsje Suzan Jacket', 'Material': 'poliester, umplutură din poliester', 'Caracteristici': 'izolată, matlasată, guler ridicat', 'Cod produs': '4106200'})

w(12615,
  f'<p>{GEOX} ASSISTER sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, sport, cu luminițe în talpă și imprimeu decorativ, din material textil și sintetic. Tehnologia GEOX Respira, cu membrană microporoasă, scoate umezeala și ține piciorul uscat.</p>'
  '<p>Combină șireturile cu aricii, deci copilul se încalță singur, iar talpa din spumă e ușoară și flexibilă. Călcâiul ușor întărit ține piciorul așezat corect.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Branț', 'textil, detașabil.'), ('Imprimeu', 'decorativ, pe partea de sus.'))
  + '<p>Numerele 24-27 se potrivesc băieților de cam 2-4 ani.</p>',
  [('model', 'Geox ASSISTER sneakers pentru copii negri J66DZB.02A9J'), ('sport', 'stilului sportiv'), ('lumini', 'Luminițe încorporate în talpă'), ('imprimeu', 'Imprimeul decorativ de pe partea superioară'),
   ('material', 'Partea superioară din material textil și sintetic'), ('Respira', 'Tehnologia GEOX Respira™ cu o membrană microporoasă favorizează eliminarea umezelii'),
   ('închidere', 'Combinația de șireturi și închidere cu arici permite o ajustare ușoară și o încălțare independentă'), ('talpă', 'Talpă din spumă contribuie la lejeritate și flexibilitate'),
   ('căptușeală', 'Interior căptușit cu material textil'), ('branț', 'Branțuri detașabile din material textil'), ('călcâi', 'Călcâi ușor întărit')],
  {'Model': 'Geox ASSISTER', 'Material': 'textil și sintetic, interior textil, talpă din spumă', 'Caracteristici': 'luminițe în talpă, Geox Respira, șireturi și arici', 'Cod produs': 'J66DZB.02A9J'})

w(12617,
  f'<p>Varianta B461NC a modelului {GEOX} GISLI: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} maro, înalți, cu logo Geox, din imitație de piele și material textil, în stil casual. Se strâng cu șiret, iar velcro-ul suplimentar fixează pantoful pe picior.</p>'
  '<p>Gulerul ușor întărit sprijină glezna, iar membrana microporoasă GEOX Respira ajută la păstrarea piciorului uscat. Călcâiul întărit ține piciorul în poziție corectă la joacă.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Interior', 'căptușit cu material textil.'), ('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 20-27 sunt pentru băieți mici, de aproximativ 1-4 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii maro B461NC.0MEFU'), ('înalt', 'Profil înalt al părții superioare cu guler ușor întărit sprijină glezna'),
   ('logo', 'Model cu logo Geox'), ('material', 'Partea superioară din imitație de piele și material textil'), ('casual', 'stilurile casual'),
   ('închidere', 'Sistem de închidere cu șireturi și velcro suplimentar'), ('Respira', 'Tehnologia GEOX Respira™ ajută la menținerea picioarelor uscate, datorită membranei microporoase'),
   ('interior', 'Interior căptușit cu material textil'), ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șiret și velcro, profil înalt', 'Cod produs': 'B461NC.0MEFU'})

w(12618,
  f'<p>Adidașii {TH} T1X9-35216 albi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} uni, cu profil scurt, din imitație de piele, care se curăță ușor, pentru picioarele active ale celor mici. Aricii permit încălțatul și descălțatul rapid, chiar de către copil.</p>'
  '<p>Gulerul întărit se așază în jurul gleznei, iar talpa plată lasă piciorul să se rostogolească natural la pas. Culoarea albă, uni, merge cu multe ținute.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'căptușit cu textil.'), ('Branț', 'textil.'))
  + '<p>Numerele 20-29 se potrivesc copiilor de 1-5 ani, aproximativ.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii albi T1X9-35216'), ('uni', 'Modelul uni'), ('profil', 'Profilul scurt al părții superioare'),
   ('imitație', 'Partea superioară din imitație de piele oferă încălțămintei un aspect estetic și facilitează menținerea curățeniei'),
   ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă de către copii'), ('guler', 'Gulerul întărit al părții superioare ajută la ajustarea în jurul gleznei'),
   ('talpă', 'Talpa plată favorizează rularea naturală a piciorului'), ('călcâi', 'Călcâi întărit'), ('interior', 'Interiorul căptușit cu material textil'), ('branț', 'Branț textil')],
  {'Model': 'Tommy Hilfiger T1X9-35216', 'Material': 'imitație de piele, interior textil', 'Caracteristici': 'arici, guler întărit, profil scurt', 'Cod produs': 'T1X9-35216'})

w(12621,
  f'<p>Jacheta {A("/brand/mayoral/", "Mayoral")} 4469 gri este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, de iarnă, cu izolație sintetică groasă și căptușeală moale din polar, totuși ușoară. Gluga integrată apără capul de vânt și frig, iar croiala regulară lasă loc pentru straturi pe dedesubt.</p>'
  '<p>Mânecile raglan dau brațelor libertate, iar manșetele cu elastic țin aerul rece afară.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, cu fermoar.'), ('Material', '89% poliamidă, 10% poliester, 1% elastan.'))
  + '<p>Mărimile 92-140 merg cam la 2-10 ani.</p>',
  [('model', 'Mayoral Jachetă pentru copii gri 4469'), ('matlasat', 'Jacheta matlasată gri Mayoral'), ('iarnă', 'activități de iarnă'),
   ('izolație', 'Izolația sintetică groasă ajută la menținerea căldurii'), ('polar', 'Căptușeala moale din polar'), ('ușor', 'face ca jacheta să fie ușoară'),
   ('glugă', 'Gluga integrată oferă protecție suplimentară capului împotriva vântului și frigului'), ('straturi', 'permite purtarea de straturi suplimentare de îmbrăcăminte pe dedesubt'),
   ('raglan', 'Croiala raglan a mânecilor'), ('manșete', 'Manșetele cu elastic ajută la ajustarea mânecilor și limitează accesul aerului rece'),
   ('fermoar', 'Închiderea practică cu fermoar pe toată lungimea'), ('buzunare', 'Buzunarele laterale cu fermoar'), ('material', '89% Poliamidă, 10% Poliester, 1% Elastan')],
  {'Model': 'Mayoral 4469', 'Material': '89% poliamidă, 10% poliester, 1% elastan, căptușeală din polar', 'Caracteristici': 'glugă integrată, mâneci raglan, fermoar', 'Cod produs': '4469'})

w(12627,
  f'<p>{GEOX} IUPIDOO roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din material textil, piele întoarsă și piele ecologică, ușori, pentru purtarea zilnică. Velcro-ul face încălțatul și descălțatul ușor.</p>'
  '<p>Branțul Geox e din piele perforată, antibacterian, conturat pentru așezarea corectă a piciorului, iar sistemul anti-shock preia șocurile la pas.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Vârf', 'cutie rotundă, ușor întărită.'), ('Călcâi', 'contrafort rigid.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 18-26 sunt pentru fetițe de în jur de 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii IUPIDOO culoarea roz, B3558C.02214'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatie de material textil, piele întoarsă și piele ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('branț', 'brant din piele cu perforari'),
   ('antibacterian', 'Are proprietati antibacteriene'), ('contur', 'Este conturat corespunzator pentru o asezare corecta a piciorului'), ('anti-shock', 'sistemului anti-shockl'),
   RESPIRA, ('vârf', 'Cutie rotunda, usor intarita'), ('călcâi', 'Contorul de călcâi rigid'), TALPA],
  {'Model': 'Geox IUPIDOO', 'Material': 'textil, piele întoarsă și piele ecologică, interior textil și piele', 'Caracteristici': 'velcro, branț Geox antibacterian, Geox Respira', 'Cod produs': 'B3558C.02214'})

w(12631,
  f'<p>Geaca {A("/brand/colmar/", "Colmar")} GLOWER neagră este o {A("/categorie/geci-jachete/", "geacă pentru fete")} izolată cu umplutură naturală din puf și pene, pentru frig serios. Are glugă, guler ridicat și se închide cu fermoar.</p>'
  '<p>Materialul exterior e neted, din poliamidă, iar croiala e simplă, dreaptă. Căptușeala e tot din poliamidă, iar puful dă, după magazin, un nivel ridicat de izolare.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Umplutură', '90% puf de rață, 10% pene.'), ('Buzunare', 'două laterale, cu fermoar.'), ('Exterior', '100% poliamidă.'))
  + '<p>Mărimile 154-172 sunt pentru fete de aproximativ 12-15 ani.</p>',
  [('model', 'Colmar Geacă copii GLOWER culoarea negru, 3475.8XV'), ('puf', 'Umplutura din puf si pene'), ('izolat', 'Model izolat cu captuseala'),
   ('frig', 'garantează un nivel ridicat de izolare împotriva frigului'), ('glugă', 'Model cu gluga'), ('închidere', 'Are inchidere cu fermoar si guler ridicat'), ('neted', 'material neted'),
   ('croială', 'Tăiere simplă, fără blocare'), ('exterior', 'Material de bază: 100% Poliamida'), ('umplutură', '90% Duck Down, 10% Pene'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar')],
  {'Model': 'Colmar GLOWER', 'Material': '100% poliamidă, umplutură 90% puf de rață și 10% pene', 'Caracteristici': 'glugă, guler ridicat, fermoar', 'Cod produs': '3475.8XV'})

w(12633,
  f'<p>{GEOX} ECLYPER albi sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, ușor de curățat și de întreținut, care se închid cu velcro. Sistemul Check Your Feet ajută la verificarea mărimii, deci vedeți când a crescut piciorul.</p>'
  '<p>Vârful rotund, ușor rigid, lasă degetele să stea liber, iar contrafortul rigid ține călcâiul în pantof.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, perforată.'), ('Interior', 'material textil.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 20-27 merg, orientativ, la fetițe de 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ECLYPER culoarea alb, B555MA.000BC'), ('profil', 'Înălțime: mic de statură'), ('întreținere', 'Modelul este ușor de curățat și întreținut'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('Check', 'Check Your Feet ajuta la ajustarea pantofilor'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('degete', 'degetele se pot aranja liber în pantof'), ('călcâi', 'Contorul de călcâi rigid'), RESPIRA, CURAT, TALPA],
  {'Model': 'Geox ECLYPER', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Check Your Feet, Geox Respira', 'Cod produs': 'B555MA.000BC'},
  notes=['Descrierea spune piele întoarsă, compoziția dă material sintetic (imitație de piele); n-am pomenit materialul de sus.'])

w(12634,
  f'<p>{GEOX} SPRINTYE roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos și detalii decorative, din material textil și piele ecologică. Partea de sus e rigidizată, deci ține forma, iar velcro-ul face încălțatul ușor.</p>'
  '<p>Vârful e rotund, iar interiorul textil e confortabil și se păstrează curat ușor. Partea de sus, rigidizată, ține piciorul bine pe loc la joacă.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Talpă', 'din cauciuc.'), ('Închidere', 'velcro.'))
  + '<p>Numerele 24-27 se potrivesc fetițelor de aproximativ 2-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii SPRINTYE culoarea roz, B654TA.0GNHH'), ('profil', 'Înălțime: mic de statură'), ('decor', 'Detalii decorative'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('rigid', 'Partea superioară rigidizată'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('vârf', 'Varf rotund'), CURAT, RESPIRA, ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira, parte superioară rigidizată', 'Cod produs': 'B654TA.0GNHH'})
