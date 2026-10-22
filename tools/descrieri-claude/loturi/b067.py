import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
GUESS = A('/brand/guess/', 'GUESS')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(12552,
  f'<p>{GEOX} WEEMBLE sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} în culoarea albastru, din material sintetic și textil, cu șireturi elastice și cârlig, deci se încalță și se descalță fără legat. Bucla de la spate ajută la tras pantoful pe picior.</p>'
  '<p>Talpa din spumă, ușor flexibilă, e moale la pas, iar cutia rotundă, ușor întărită, apără degetele.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textil moale, nu irită.'), ('Inserție', 'din piele naturală, tăbăcită fără crom.'), ('Partea de sus', 'sintetic și textil.'))
  + '<p>Mărimile 28-35 sunt pentru băieți de cam 4-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii WEEMBLE J56HAA.0MEFU'), ('culoare', 'Culoare albastru'), ('material', 'combinația materialului sintetic cu cel textil'),
   ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('talpă', 'O talpă din spumă ușor flexibilă oferă o senzație mai moale'), ('vârf', 'Cutie rotunda, usor intarita'),
   ('căptușeală', 'Căptușeala moale din material textil previne iritația'), ('crom', 'Inserția din piele a fost realizată fără utilizarea cromului')],
  {'Model': 'Geox WEEMBLE', 'Material': 'sintetic și textil, interior textil și piele, talpă din spumă', 'Caracteristici': 'șireturi elastice cu cârlig, buclă la spate', 'Cod produs': 'J56HAA.0MEFU'},
  notes=['Magazinul dă „Înălțime: jos”, dar și o parte superioară ridicată care rigidizează glezna; n-am precizat profilul.'])

w(12554,
  f'<p>Geaca {GUESS} H4BJ10 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} în culoarea albastru, matlasată, ușor izolată, din material neted, cu glugă, pentru zile mai reci. Croiala e simplă, dreaptă, iar închiderea se face cu fermoar.</p>'
  '<p>Mânecile și tivul au margine elastică, care ține vântul afară.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Izolație', 'sintetică, ușoară, pe căptușeală.'), ('Material', '100% poliester.'))
  + '<p>Mărimile încep la 122-125 și ajung la 166-175, adică băieți de cam 7-16 ani. La 147-157 cm geaca are 55 cm lungime.</p>',
  [('model', 'Guess Geaca copii H4BJ10 WCFM0'), ('culoare', 'Culoare albastru'), ('matlasat', 'Model matlasat cu izolație sintetica'), ('neted', 'Model usor izolat confecționat din material neted'),
   ('glugă', 'Model cu gluga'), ('frig', 'temperaturi mai reci'), ('croială', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'),
   ('margini', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('izolație', 'Model usor izolat pe captuseala'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 55 cm')],
  {'Model': 'GUESS H4BJ10', 'Material': '100% poliester, izolație sintetică ușoară', 'Caracteristici': 'matlasată, glugă, fermoar, buzunare cu fermoar', 'Cod produs': 'H4BJ10 WCFM0'})

w(12556,
  f'<p>Adidașii {TH} T3A9-34269 argintii sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din material textil și piele ecologică, ușori, pentru purtarea zilnică. Șireturile plate nu apasă pe arcada piciorului, deci pantoful se strânge bine fără puncte de presiune.</p>'
  '<p>Cutia rotundă e moale, iar călcâiul puternic rigid ține piciorul în pantof la mers.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Partea de sus', 'imitație de piele și textil.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 35-40 se potrivesc fetelor de la 10 ani în sus, orientativ; la 40 branțul are 25,5 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea argintiu, T3A9-34269'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('șireturi', 'Sireturile plate elimina punctele de presiune de pe arcada piciorului'), ('vârf', 'Cutie rotunda si moale'),
   ('călcâi', 'Călcâiul puternic rigid stabilizează călcâiul'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('lungime', 'Lungimea brantului pentru marimea este de: 25,5 cm')],
  {'Model': 'Tommy Hilfiger T3A9-34269', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi plate, călcâi rigid', 'Cod produs': 'T3A9-34269'})

w(12566,
  f'<p>{GEOX} WASHIBA sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil înalt, din imitație de piele și material textil, cu talpă GEOX Respira cu membrană microporoasă. Membrana scoate umezeala și, în același timp, oprește apa din exterior.</p>'
  '<p>Profilul înalt sprijină glezna, iar aricii fac încălțatul și descălțatul rapid. Partea de sus, din imitație de piele și textil, e gândită să fie durabilă, iar talpa plată lasă piciorul să se miște liber.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Talpă', 'plată, din cauciuc.'), ('Închidere', 'arici.'))
  + '<p>Mărimile disponibile, 24-27, sunt pentru fetițe de aproximativ 2-4 ani.</p>',
  [('model', 'Geox WASHIBA sneakers pentru copii roz J36HXA.05415'), ('profil', 'Profil înalt al părții superioare stabilizează glezna'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia GEOX Respira™ cu o membrană microporoasă favorizează eliminarea umezelii'),
   ('apă', 'Talpă respirabilă cu membrană protejează interiorul încălțămintei de pătrunderea apei din exterior'), ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă'),
   ('căptușeală', 'Căptușeală moale din material textil'), ('talpă', 'Talpă din cauciuc'), ('plată', 'Talpă plată')],
  {'Model': 'Geox WASHIBA', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici, profil înalt', 'Cod produs': 'J36HXA.05415'})

w(12567,
  f'<p>{REIMA} Ohitus sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, sport, cu croială până la gleznă și fața din material textil, buni pentru primăvară, vară și toamnă. Branțul detașabil are imprimeu cu care verificați ușor mărimea pe piciorul copilului.</p>'
  '<p>Înșiretarea rapidă și găicile de pe limbă și din spate îl lasă pe copil să se încalțe singur.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Călcâi', 'contrafort ușor rigidizat.'), ('Interior', 'căptușit cu textil.'), ('Talpă', 'tip platformă, din cauciuc și spumă.'), ('Branț', 'moale, reduce șocurile la alergat.'))
  + '<p>Numerele 28-40 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'Reima Ohitus sneakers pentru copii albi 5400174A'), ('gleznă', 'Croiala până la gleznă'), ('textil', 'Partea superioară din material textil'),
   ('sezon', 'zilele de primăvară, vară și toamnă'), ('branț', 'Branțul detașabil cu imprimeu facilitează ajustarea precisă a mărimii'),
   ('înșiretare', 'Sistemul de înșiretare rapidă permite copiilor să se încalțe și să se descalțe singuri'), ('găici', 'Găicile din spate și de pe limbă'),
   ('călcâi', 'Contragreutatea călcâiului ușor rigidizată'), ('interior', 'Interiorul căptușit cu material textil'), ('talpă', 'Talpa tip platformă din cauciuc și spumă'),
   ('șocuri', 'ajută la reducerea șocurilor')],
  {'Model': 'Reima Ohitus', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc și spumă', 'Caracteristici': 'înșiretare rapidă, branț cu verificare de mărime', 'Cod produs': '5400174A'})

w(12569,
  f'<p>{REIMA} Oikotie în negru sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")} de ploaie și noroi, din pânză cu tratament Teflon EcoElite, de origine vegetală, care respinge apa mult timp. Membrana dă 10000 g/m2 la impermeabilitate și 3000 g/m2/24h la respirabilitate.</p>'
  '<p>Talia înaltă, cu elastic, se trage repede peste haine, iar tivul elastic și îngust stă bine peste cizme.</p>'
  '<p>Materialul, pe scurt:</p>'
  + L(('Compoziție', '92% poliamidă și 8% elastan.'), ('Model', 'uni, croială clasică.'), ('Apă', 'rezistenți, fără garanția impermeabilității complete.'))
  + '<p>Mărimile 92-140 merg, orientativ, la 2-10 ani.</p>',
  [('model', 'Reima Pantaloni copii Oikotie culoarea negru, 5100010B'), ('pânză', 'Material: panza'),
   ('Teflon', 'Teflon EcoElite este prima tesatura de origine vegetala care asigura o rezistenta durabila la apa'), ('impermeabilitate', 'Impermeabilitate: 10000 g/m2'),
   ('respirabilitate', 'Respirabilitate: 3000 g/m2/24h'), ('talie', 'Talie inalta cu banda elastica in talie'), ('tiv', 'Picioarele sunt finisate cu un tiv elastic, îngust'),
   ('material', '92% Poliamida, 8% Elastan'), ('uni', 'Model: uni'), ('croială', 'Croiala clasică, simplă'), ('apă', 'nu garantează impermeabilitatea completă')],
  {'Model': 'Reima Oikotie', 'Material': '92% poliamidă, 8% elastan', 'Caracteristici': 'Teflon EcoElite, 10000 mm impermeabilitate, talie elastică', 'Cod produs': '5100010B'})

w(12570,
  f'<p>Varianta verde a gecii {GUESS} N6YL01 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, căptușită complet, umplută cu fibră sintetică, care ține de cald când vremea se schimbă des. Gluga e prinsă de geacă, iar gulerul ridicat acoperă gâtul.</p>'
  '<p>Merge până la șolduri și lasă brațele libere, fiind croită regulat. Fermoarul o face rapid de îmbrăcat.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Borduri', 'elastice jos și la manșete.'), ('Buzunare', 'două, slip-on, pe laterale.'), ('Compoziție', 'integral poliester.'))
  + '<p>Între 88-96 și 122-125 sunt mărimile pentru 1-7 ani, aproximativ.</p>',
  [('model', 'Guess Geacă petrecută pentru copii verde N6YL01 W2656'), ('matlasat', 'Construcția matlasată'), ('căptușeală', 'Căptușeala completă'),
   ('umplutură', 'Umplutura sintetică ajută la menținerea căldurii'), ('vreme', 'vremea schimbătoare a sezonului de tranziție'), ('glugă', 'Gluga integrată'),
   ('guler', 'Gulerul ridicat oferă o protecție suplimentară a gâtului împotriva frigului'), ('lungime', 'Lungimea până la șolduri'), ('croială', 'Croiala regulară permite libertatea de mișcare'),
   ('fermoar', 'Închiderea cu fermoar'), ('borduri', 'Bordurile elastice la bază și manșete'), ('buzunare', 'Buzunarele laterale tip slip-on'), ('material', '100% Poliester')],
  {'Model': 'GUESS N6YL01', 'Material': '100% poliester, umplutură sintetică', 'Caracteristici': 'matlasată, glugă integrată, guler ridicat', 'Cod produs': 'N6YL01 W2656'})

w(12572,
  f'<p>Geaca {A("/brand/mayoral/", "Mayoral")} 7440 bej este o {A("/categorie/geci-jachete/", "geacă pentru fete")} de iarnă, matlasată, cu umplutură sintetică groasă și guler din blană artificială, care apără gâtul de frig. Matlasajul împarte uniform umplutura, iar modelul uni se poartă ușor cu restul hainelor.</p>'
  '<p>Lungimea până la șolduri acoperă trunchiul fără să încurce la joacă. Se închide cu fermoar.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'completă, încă un strat de izolație.'), ('Tiv și manșete', 'cu bordură elastică, contra vântului.'), ('Buzunare', 'laterale, slip-on.'), ('Material', '99% poliester, 1% elastan.'))
  + '<p>Mărimile 128-167 se potrivesc fetelor de cam 8-14 ani.</p>',
  [('model', 'Mayoral Geacă petrecută pentru copii bej 7440'), ('iarnă', 'potrivită pentru zilele de iarnă'), ('umplutură', 'Umplutură sintetică groasă'),
   ('blană', 'Guler din blană artificială adaugă un aspect elegant și ajută la protejarea gâtului de frig'), ('matlasat', 'Finisajul matlasat al materialului ajută la distribuirea uniformă a umpluturii'),
   ('uni', 'Modelul uni al materialului conferă versatilitate'), ('lungime', 'Lungime până la șolduri'), ('fermoar', 'Închidere cu fermoar'),
   ('căptușeală', 'Căptușeală completă în interiorul gecii'), ('tiv', 'Tivul și manșetele cu bordură elastică'), ('buzunare', 'Buzunare laterale tip slip-on'),
   ('material', '99% Poliester, 1% Elastan')],
  {'Model': 'Mayoral 7440', 'Material': '99% poliester, 1% elastan, umplutură sintetică', 'Caracteristici': 'guler din blană artificială, matlasată, fermoar', 'Cod produs': '7440'})

w(12576,
  f'<p>{GEOX} RISHON sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, cu profil jos, din material textil și piele ecologică, pentru cei mai mici. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos, iar talpa din cauciuc e durabilă.</p>'
  '<p>Sistemul Light Flexy din branț lasă piciorul să se miște liber, iar o tehnologie moale din talpă preia șocurile.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Interior', 'textil, ușor de ținut curat.'), ('Partea de sus', 'imitație de piele și textil.'))
  + '<p>Numerele 18-26 sunt pentru fetițe de în jur de 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii RISHON culoarea alb, B560LA.0BCEW'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('talpă', 'talpă din cauciuc care este durabilă'),
   ('Light Flexy', 'Light Flexy Sistem de brant pentru libertatea de miscare'), ('moale', 'Tehnologie moale pentru amortizare'), RESPIRA,
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Geox RISHON', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, Light Flexy, șireturi elastice cu cârlig', 'Cod produs': 'B560LA.0BCEW'})

w(12577,
  f'<p>{GEOX} ARIL sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil jos și detalii decorative, din material textil și sintetic, cu partea de sus flexibilă care se adaptează la picior. Au șiret cu închidere Velcro, deci se reglează repede.</p>'
  '<p>Bucla de la spate ajută la încălțat, iar spatele călcâiului e ușor rigidizat. Talpa din cauciuc absoarbe șocurile.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Vârf', 'cutie rotundă, ușor întărită.'), ('Geox Respira', 'talpă în trei straturi, perforată.'), ('Inserție', 'detașabilă, ușor de curățat.'))
  + '<p>Numerele 24-27 merg la fetițe de cam 2-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ARIL culoarea roz, J55DLB.07QBC'), ('profil', 'Înălțime: mic de statură'), ('decor', 'Detalii decorative'),
   ('material', 'combinatia materialului textil cu cel sintetic'), ('flexibil', 'Partea superioară flexibilă se adaptează cu ușurință la picior'),
   ('închidere', 'Model cu siret cu inchidere Velcro'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('călcâi', 'Spatele calcaiului usor rigidizat'), ('talpă', 'Talpă din cauciuc'), ('șoc', 'Absorbtia socului'), ('vârf', 'Cutie rotunda, usor intarita'), RESPIRA,
   ('inserție', 'Inserție detașabilă, ușor de curățat')],
  {'Model': 'Geox ARIL', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șiret cu Velcro, inserție detașabilă', 'Cod produs': 'J55DLB.07QBC'})
