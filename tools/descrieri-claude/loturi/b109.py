import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GUESS = A('/brand/guess/', 'GUESS')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
COLMAR = A('/brand/colmar/', 'Colmar')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
GU = '/categorie/unisex-imbracaminte-geci-jachete/'

w(8681,
  f'<p>Bluza {TH} KB0KB10362 albă este un hanorac cu glugă și fermoar, din categoria {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluze pentru băieți")}, din țesătură subțire, ușor elastică, cu mult bumbac. Bumbacul e regenerat din deșeuri textile, iar poliesterul e parțial reciclat.</p>'
  '<p>Croiala e simplă, fermoarul o face ușor de pus și de scos, iar gluga încorporată adaugă căldură când e nevoie. Mânecile și marginea de jos se termină cu elastic, iar pe laterale are două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '82% bumbac reciclat, 18% poliester reciclat.'), ('Glugă', 'integrată.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 sunt pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'KB0KB10362'), ('culoare', 'culoarea alb'), ('subțire', 'confecționat din țesătură subțire, usor elastica'),
   ('bumbac', 'Model realizat din material extrem de confortabil cu un conținut ridicat de bumbac'), ('regenerat', 'Modelul conține fibre de bumbac regenerate'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'), ('glugă', 'Gluga încorporată oferă un plus de căldură'),
   ('mâneci', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('buzunare', 'Două buzunare laterale'),
   ('material', '82% Bumbac reciclat, 18% Poliester reciclat'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB10362', 'Material': '82% bumbac reciclat, 18% poliester reciclat', 'Caracteristici': 'glugă, fermoar, buzunare laterale', 'Cod produs': 'KB0KB10362'})

w(8682,
  f'<p>Geaca {A("/brand/marc-jacobs/", "Marc Jacobs")} W60801 bej este o {A(GB, "geacă de tranziție pentru băieți")} din țesătură cu aplicații și material aerisit, cu mult bumbac. Are guler, fără glugă, și căptușeală completă.</p>'
  '<p>Tăietura e lejeră, se închide cu cleme și are două buzunare laterale. Mânecile și marginea de jos sunt finisate cu bătături, care o apără de vremea urâtă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '66% bumbac, 34% poliamidă.'), ('Material 2', '100% poliester.'), ('Închidere', 'cleme.'))
  + '<p>Mărimile 126-150 se potrivesc orientativ copiilor de 8-12 ani.</p>',
  [('cod', 'W60801'), ('culoare', 'culoarea bej'), ('aplicații', 'Model confecționat din țesătură cu aplicații'), ('aerisit', 'Model din material aerisit cu un conținut ridicat de bumbac'),
   ('guler', 'Model cu guler'), ('glugă', 'fără glugă'), ('căptușeală', 'cu căptușeală completă'), ('lejeră', 'Tăiere lejeră, fără blocare'), ('cleme', 'Incheiere cu cleme'),
   ('buzunare', 'Două buzunare laterale'), ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('material1', '66% Bumbac, 34% Poliamida'), ('material2', '100% Poliester')],
  {'Model': 'Marc Jacobs W60801', 'Material': '66% bumbac, 34% poliamidă', 'Caracteristici': 'aplicații, guler, cleme', 'Cod produs': 'W60801'})

w(8688,
  f'<p>Geaca {TH} KS0KS00620 bleumarin este o {A(GF, "geacă subțire pentru fete")}, matlasată, din nailon, cu umplutură sintetică ușoară și căptușeală completă. Logoul mărcii e brodat pe față.</p>'
  '<p>Croiala e simplă, fără glugă, cu buzunare oblice și mâneci finisate cu manșetă. Fermoarul o face ușor de pus și de scos, iar geaca e potrivită pentru zilele de tranziție, primăvara sau toamna.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% nailon.'), ('Umplutură', 'sintetică, ușoară.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 sunt pentru copii de cam 8-16 ani.</p>',
  [('cod', 'KS0KS00620'), ('culoare', 'culoarea albastru marin'), ('subțire', 'Model subtire confectionat din material matlasat'), ('material', '100% Nailon'),
   ('umplutură', 'sintetică'), ('ușoară', 'ușoară'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('logo', 'Logo-ul mărcii brodat pe față'),
   ('croială', 'croială simplă, fără blocare'), ('glugă', 'fără glugă'), ('buzunare', 'Buzunare oblice'), ('manșetă', 'Finisaj din manseta'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('tranziție', 'Izolare: tranzitional')],
  {'Model': 'Tommy Hilfiger KS0KS00620', 'Material': '100% nailon', 'Caracteristici': 'matlasată, logo brodat, fermoar', 'Cod produs': 'KS0KS00620'})

w(8696,
  f'<p>Geaca {A("/brand/adidas/", "adidas")} JW2396 neagră este o {A(GU, "geacă unisex")} izolată, matlasată, din țesătură netedă, cu izolație sintetică groasă. Tehnologia CLIMAWARM reține căldura și absoarbe umezeala, iar poliesterul e reciclat în întregime.</p>'
  '<p>Gulerul ridicat și gluga încorporată apără de frig. Fermoarul pe toată lungimea are clapă interioară împotriva furtunii, iar cele două buzunare laterale au fermoar. Tăietura e simplă, fără blocare, iar căptușeala acoperă tot interiorul.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Glugă', 'integrată.'), ('Căptușeală', 'completă.'))
  + '<p>Mărimile 140-176 se potrivesc orientativ copiilor de 10-16 ani.</p>',
  [('cod', 'JW2396'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat confecționat din țesătură neteda'), ('matlasat', 'Model matlasat cu izolație sintetică'),
   ('groasă', 'groasă'), ('CLIMAWARM', 'Tehnologia CLIMAWARM retine caldura'), ('umiditate', 'Proprietățile de absorbție a umidității'),
   ('reciclat', 'Poliesterul folosit la realizarea acestui model este reciclat în întregime'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('glugă', 'Gluga încorporată'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară împotriva furtunii'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material', '100% Poliester reciclat'), ('căptușeală', 'cu căptușeală completă')],
  {'Model': 'adidas JW2396', 'Material': '100% poliester reciclat', 'Caracteristici': 'CLIMAWARM, izolație groasă, glugă', 'Cod produs': 'JW2396'})

w(8700,
  f'<p>Geaca {COLMAR} CAPTION roz este o {A(GU, "geacă unisex")} pentru cei mici, ușor izolată, din material matlasat, cu umplutură de puf și căptușeală completă, sintetică. Gulerul ridicat ține gâtul la adăpost, iar gluga lipsește.</p>'
  '<p>Se închide cu fermoar și capsă, iar buzunarele exterioare se închid. Compoziția combină mai multe materiale, inclusiv unul cu puțin elastan.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliester.'), ('Material 3', '90% poliamidă, 10% puf.'), ('Material 4', '99% poliester, 1% elastan.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 86-98 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'CAPTION'), ('culoare', 'culoarea roz'), ('izolat', 'Model ușor izolat confecționat din material matlasat'), ('puf', 'puf'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('guler', 'Guler ridicat'), ('glugă', 'fără glugă'), ('fermoar', 'Fixare cu fermoar si snap'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('material1', '100% Poliester'), ('material3', '90% Poliamida, 10% Puf'), ('material4', '99% Poliester , 1% Elastan'),
   ('croială', 'Croială: regular fit')],
  {'Model': 'Colmar CAPTION', 'Material': 'poliester, poliamidă cu puf', 'Caracteristici': 'matlasată, umplutură de puf, guler ridicat', 'Cod produs': '3484.2XX'})

w(8714,
  f'<p>Adidașii {A("/brand/biomecanics/", "Biomecanics")} 262158 bej sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")}, ușori și confortabili, din textil, imitație de piele întoarsă și piele ecologică. Au fost creați împreună cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia.</p>'
  '<p>Vârful lat nu ciupește degetele, deschiderea largă ajută la încălțat, iar tăietura în formă de U lasă glezna să se miște liber. Se închid cu șireturi elastice și cârlig, iar bucla de la spate ajută la pus și la scos.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Branț', 'detașabil, antibacterian, profilat.'), ('Lungime branț', '15 cm la numărul 23.'), ('Talpă', 'material sintetic, profilată.'))
  + '<p>Numerele 19-23 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('cod', '262158'), ('culoare', 'culoarea bej'), ('materiale', 'combinatie de material textil, imitatie de piele întoarsă și piele ecologică'), ('ușor', 'Model ușor și confortabil'),
   ('pediatri', 'create in cooperare cu medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'), ('vârf', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('deschidere', 'Deschidere larga pentru incaltarea usoara'), ('U', 'taieturi in forma de U'), ('glezna', 'permit gleznei sa se miste liber'),
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('branț', 'Brant detasabil si antibacterian, profilat la mijlocul piciorului'), ('lungime', 'Lungimea brantului pentru marimea este de: 15 cm'), ('mărime', 'Dimensiunile date pentru marimea: 23'),
   ('talpă', 'Talpa: Material sintetic'), ('profilată', 'profilată')],
  {'Model': 'Biomecanics 262158', 'Material': 'textil, imitație de piele întoarsă, piele ecologică', 'Caracteristici': 'vârf lat, branț antibacterian, șireturi elastice', 'Cod produs': '262158'},
  notes=['Descrierea spune „fabricat numai din materiale naturale”, dar compoziția indică materiale sintetice; nu am preluat afirmația.'])

w(8737,
  f'<p>Geaca {A("/brand/converse/", "Converse")} 4CC926 roz este o {A(GF, "geacă matlasată pentru fete")}, din material neted rezistent la apă, cu impregnare hidrofobă și izolație sintetică ușoară spre medie, pentru temperaturile mai reci. Gluga nu se detașează.</p>'
  '<p>Tăietura e simplă, fermoarul o face ușor de pus și de scos, iar cele două buzunare laterale se închid prin apăsare. Căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 122-128 până la 155-159 se potrivesc orientativ copiilor de 7-13 ani.</p>',
  [('cod', '4CC926'), ('culoare', 'culoarea roz'), ('izolat', 'Model izolat confecționat din material neted cu izolatie sintetică'), ('reci', 'temperaturi mai reci'),
   ('apă', 'Rezistent la apa'), ('hidrofob', 'impregnare hidrofobă'), ('medie', 'ușoară, medie'), ('matlasat', 'Matlasare'), ('glugă', 'Gluga nedetasabila'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'),
   ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('material', '100% Poliester'),
   ('croială', 'Croială: regular fit')],
  {'Model': 'Converse 4CC926', 'Material': '100% poliester, umplutură sintetică', 'Caracteristici': 'rezistentă la apă, glugă fixă, matlasată', 'Cod produs': '4CC926'})

w(8753,
  f'<p>Geaca {GUESS} K6RL04 bej este o {A(GF, "geacă de tranziție pentru fete")} neizolată, din țesătură netedă, cu glugă și căptușeală completă. Poliesterul o face mai rezistentă la îndoire.</p>'
  '<p>Fasonul e drept, se închide cu fermoar și are protecție pentru bărbie. Mânecile sunt finisate cu manșetă, iar pe laterale sunt două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '35 cm la mărimea 96/104.'), ('Lățime la umeri', '25 cm.'))
  + '<p>Mărimile 88-96 până la 122-125 sunt pentru copii de cam 1-7 ani.</p>',
  [('cod', 'K6RL04'), ('culoare', 'culoarea bej'), ('neizolat', 'Model neizolat confecționat din țesătură netedă'), ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'),
   ('glugă', 'Model cu gluga'), ('căptușeală', 'cu căptușeală completă'), ('fason', 'Fason drept'), ('fermoar', 'Incheiere cu fermoar'),
   ('bărbie', 'Model echipat cu protecție pentru bărbie'), ('manșetă', 'Manecile finisate cu manseta'), ('buzunare', 'Două buzunare laterale'),
   ('material', '100% Poliester'), ('lungime', 'Lungimea: 35 cm'), ('mărime', '96/104 cm'), ('umeri', 'Latimea in umeri: 25 cm')],
  {'Model': 'GUESS K6RL04', 'Material': '100% poliester', 'Caracteristici': 'neizolată, glugă, protecție la bărbie', 'Cod produs': 'K6RL04.WFYD0'},
  notes=['Magazinul o marchează și „produs pentru bebe”; pe site e la geci pentru fete.'])

w(8776,
  f'<p>Geaca {COLMAR} LEGACIES neagră este o {A(GU, "geacă unisex")} ușor izolată, matlasată, care combină țesătură și tricot. Umplutura sintetică ține de cald la temperaturi mai scăzute, iar căptușeala e completă.</p>'
  '<p>Croiala e simplă, fără glugă, se închide cu fermoar și are buzunare exterioare care se închid. Partea din tricot conține mult bumbac.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliamidă.'), ('Material 2', '70% bumbac, 30% poliester.'), ('Umplutură', '100% poliester.'), ('Căptușeală', '100% poliester.'))
  + '<p>Mărimile 130-142 se potrivesc orientativ copiilor de 8-10 ani.</p>',
  [('model', 'LEGACIES'), ('culoare', 'culoarea negru'), ('izolat', 'Model usor izolat'), ('combinație', 'o combinatie de tesaturi si tricot'), ('matlasat', 'Matlasat'),
   ('izolație', 'Un model cu izolație sintetică care va oferi un confort suplimentar la temperaturi mai scăzute'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('glugă', 'fără glugă'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'),
   ('material1', '100% Poliamida'), ('material2', '70% Bumbac, 30% Poliester'), ('poliester', '100% Poliester')],
  {'Model': 'Colmar LEGACIES', 'Material': 'poliamidă, bumbac și poliester', 'Caracteristici': 'matlasată, țesătură și tricot, fermoar', 'Cod produs': '3170.8ZX'})

w(8817,
  f'<p>Geaca {GUESS} L5YL04 verde este o {A(GB, "geacă matlasată pentru băieți")}, ușor izolată, din material neted, cu izolație sintetică pentru temperaturile mai reci. Gulerul ridicat apără gâtul de frig, iar gluga lipsește.</p>'
  '<p>Tăietura e simplă, se închide cu cleme, iar buzunarele exterioare sunt oblice. Căptușeala e completă, sintetică, iar izolația ușoară o face bună pentru toamnă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Izolație', 'ușoară.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile de la 122-125 la 175 sunt pentru copii de aproximativ 7-16 ani.</p>',
  [('cod', 'L5YL04'), ('culoare', 'culoarea verde'), ('izolat', 'Model usor izolat confecționat din din material neted'), ('matlasat', 'Model matlasat cu izolație sintetica'),
   ('reci', 'temperaturi mai reci'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('glugă', 'fără glugă'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('cleme', 'Incheiere cu cleme'), ('buzunare', 'Buzunare oblice exterioare'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('material', '100% Poliamida'), ('ușoară', 'ușoară'), ('croială', 'Croială: regular fit')],
  {'Model': 'GUESS L5YL04', 'Material': '100% poliamidă', 'Caracteristici': 'matlasată, guler ridicat, cleme', 'Cod produs': 'L5YL04.WHFE0'})
