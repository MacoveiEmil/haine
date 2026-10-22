import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GUESS = A('/brand/guess/', 'GUESS')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'

w(8832,
  f'<p>Geaca {A("/brand/adidas/", "adidas")} JL7433 roz este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, matlasată, din material rezistent, cu izolație sintetică medie spre groasă și glugă integrată. Tehnologia CLIMAWARM păstrează căldura și ajută corpul să rămână uscat.</p>'
  '<p>Are impregnare hidrofobă și e rezistentă la vânt. Gulerul ridicat apără de frig, fermoarul o face ușor de pus și de scos, buzunarele exterioare se închid, iar elementele reflectorizante se văd după lăsarea întunericului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '55 cm la mărimea 140.'), ('Lățime la umeri', '35 cm.'))
  + '<p>Mărimile 140-176 sunt pentru copii de aproximativ 10-16 ani.</p>',
  [('cod', 'JL7433'), ('culoare', 'culoarea roz'), ('izolat', 'Model izolat confecționat din material rezistent'), ('matlasat', 'Model matlasat cu izolație sintetica'),
   ('groasă', 'medie, groasă'), ('glugă', 'integrată'), ('CLIMAWARM', 'Tehnologia CLIMAWARM retine caldura'), ('uscat', 'vă ajută să vă simțiți uscat'),
   ('hidrofob', 'impregnare hidrofobă'), ('vânt', 'Model rezistent la vânt'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'), ('buzunare', 'Buzunare exterioare incheiata'),
   ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 55 cm'),
   ('mărime', 'Dimensiunile date pentru marimea: 140 cm'), ('umeri', 'Latimea in umeri: 35 cm')],
  {'Model': 'adidas JL7433', 'Material': '100% poliester', 'Caracteristici': 'CLIMAWARM, hidrofobă, reflectorizante', 'Cod produs': 'JL7433'},
  notes=['Magazinul o numește „impermeabilă”, dar spune și că nu garantează impermeabilitatea completă; am scris doar impregnare hidrofobă.'])

w(8835,
  f'<p>Geaca {GUESS} K6GL00 roz este o {A(GF, "geacă subțire pentru fete")}, neizolată, din material ornamentat foarte plăcut, care conține plastic reciclat. Căptușeala e dintr-o plasă respirabilă, iar gulerul ridicat și gluga fixă apără de frig.</p>'
  '<p>Mânecile și marginea de jos sunt finisate cu bătături, contra vremii urâte. Fermoarul o face ușor de pus și de scos, iar pe laterale are două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '35 cm la mărimea 88-99.'), ('Lungimea mânecii', '31 cm.'))
  + '<p>Mărimile 88-96 până la 122-125 se potrivesc orientativ copiilor de 1-7 ani.</p>',
  [('cod', 'K6GL00'), ('culoare', 'culoarea roz'), ('subțire', 'Model subțire confecționat din material ornamentat'), ('confortabil', 'Material foarte confortabil'),
   ('reciclat', 'Conține plastic reciclat'), ('plasă', 'Căptușeala este realizată dintr-un material plasă respirabil'), ('guler', 'Gulerul ridicat și gluga fixă'),
   ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'),
   ('buzunare', 'Două buzunare laterale'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 35 cm'), ('mărime', '88-99 cm'), ('mânecă', '31 cm')],
  {'Model': 'GUESS K6GL00', 'Material': '100% poliester', 'Caracteristici': 'subțire, căptușeală din plasă, glugă fixă', 'Cod produs': 'K6GL00.WCFM2'},
  notes=['Magazinul o marchează și „produs pentru bebe”; pe site e la geci pentru fete.'])

w(8837,
  f'<p>Geaca {GUESS} K5YL05 bej este o {A(GF, "geacă din imitație de blană pentru fete")}, subțire, neizolată și fără căptușeală, dintr-un material modelat, foarte plăcut la atingere. Nu are glugă.</p>'
  '<p>Tăietura e simplă, fără blocare, se închide cu fermoar, iar buzunarele sunt oblice. E o geacă de tranziție, pentru zilele mai blânde, iar materialul cu aspect de blăniță e moale la atingere.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 88-96 până la 122-125 sunt pentru copii de cam 1-7 ani.</p>',
  [('cod', 'K5YL05'), ('culoare', 'culoarea bej'), ('blană', 'Material: imitatie blana'), ('subțire', 'Model subtire confecționat din din material modelat'),
   ('plăcut', 'Model realizat din material extrem de placut la atingere'), ('neizolat', 'Izolare: neizolat'), ('căptușeală', 'Captuseala: necaptusit'), ('glugă', 'fără glugă'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare oblice'), ('tranziție', 'Izolare: tranzitional'),
   ('material', '100% Poliester'), ('croială', 'Croială: regular fit')],
  {'Model': 'GUESS K5YL05', 'Material': '100% poliester, imitație de blană', 'Caracteristici': 'subțire, fără căptușeală, fermoar', 'Cod produs': 'K5YL05.WGSO0'},
  notes=['Magazinul o marchează și „produs pentru bebe”; pe site e la geci pentru fete. Caracteristicile dau „umplutură sintetică”, dar și „neizolat”; nu am scris despre umplutură.'])

w(8840,
  f'<p>Geaca {A("/brand/wheat/", "Wheat")} 7402 maro este o {A(GF, "geacă de tranziție pentru fete")} ușor izolată, din material neted, cu căptușeală completă. Poliesterul o face rezistentă la șifonare, iar gulerul ridicat apără de frig.</p>'
  '<p>Tăietura e simplă, iar fermoarul o face ușor de pus și de scos. Mânecile se termină cu elastic și au manșon cu gaură pentru degetul mare, ca să nu urce. Pe laterale are două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Glugă', 'nu are.'), ('Izolație', 'ușoară.'))
  + '<p>Mărimile 98-152 se potrivesc orientativ copiilor de 3-12 ani.</p>',
  [('cod', '7402'), ('culoare', 'culoarea maro'), ('izolat', 'Model ușor izolat confecționat din material neted'), ('căptușeală', 'cu căptușeală completă'),
   ('șifonare', 'Poliesterul garantează o rezistență ridicată împotriva șifonării'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'),
   ('elastic', 'Mâneci finisate cu o coadă elastică'), ('degetul', 'Manson cu gaura pentru degetul mare'), ('buzunare', 'Două buzunare laterale'),
   ('material', '100% Poliester'), ('glugă', 'fără glugă'), ('ușoară', 'ușoară')],
  {'Model': 'Wheat 7402', 'Material': '100% poliester', 'Caracteristici': 'ușor izolată, manșon pentru deget, guler ridicat', 'Cod produs': '7402.993R'},
  notes=['Magazinul o marchează și „produs pentru bebe”; pe site e la geci pentru fete.'])

w(8842,
  f'<p>Geaca {GUESS} L6RL03 gri este o {A(GB, "geacă matlasată pentru băieți")}, ușor izolată, din material ornamentat, cu izolație sintetică pentru temperaturi mai scăzute. Gulerul ridicat și gluga fixă țin frigul departe.</p>'
  '<p>Croiala e simplă, se închide cu fermoar, iar buzunarele exterioare se închid. Căptușeala acoperă tot interiorul.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '62 cm la mărimea 166-175.'), ('Lățime la umeri', '42 cm.'), ('Lungimea mânecii', '59 cm.'))
  + '<p>Mărimile de la 122-125 la 175 sunt pentru copii de aproximativ 7-16 ani.</p>',
  [('cod', 'L6RL03'), ('culoare', 'culoarea gri'), ('izolat', 'Model ușor izolat confecționat din material ornamentat'),
   ('izolație', 'Un model cu izolație sintetică care va oferi un confort suplimentar la temperaturi mai scăzute'), ('matlasat', 'Matlasare'),
   ('guler', 'Gulerul ridicat și gluga fixă'), ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'),
   ('căptușeală', 'cu căptușeală completă'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 62 cm'), ('mărime', '166-175 cm'), ('umeri', 'Latimea in umeri: 42 cm'),
   ('mânecă', '59 cm')],
  {'Model': 'GUESS L6RL03', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, glugă fixă, guler ridicat', 'Cod produs': 'L6RL03.WCFM2'})

w(8850,
  f'<p>Geaca {A("/brand/emporio-armani/", "Emporio Armani")} EB000922 bleumarin este o {A(GB, "geacă subțire pentru băieți")}, neizolată și fără căptușeală, din material rezistent, gândită pentru anotimpurile mai calde. Nu are glugă.</p>'
  '<p>Fermoarul pe toată lungimea are clapă interioară împotriva furtunii, iar pe lateral se închide și cu butoane presate. Mânecile lungi se termină cu manșetă elastică, iar pe laterale sunt două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '55% poliamidă, 45% poliester.'), ('Bandă elastică', '80% bumbac, 18% poliester, 2% elastan.'), ('Mărimi', 'italienești, raportate la cele europene.'))
  + '<p>Mărimile 128-176 se potrivesc orientativ copiilor de 8-16 ani.</p>',
  [('cod', 'EB000922'), ('culoare', 'culoarea bleumarin'), ('neizolat', 'Model neizolat fara captuseala'), ('rezistent', 'Model neizolat confecționat din material rezistent'),
   ('cald', 'perfect pentru anotimpurile mai calde'), ('glugă', 'fără glugă'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară împotriva furtunii'),
   ('butoane', 'Inchidere laterala cu butoane presate'), ('manșetă', 'Mâneci lungi finisate cu o manșetă confortabilă, elastică'), ('buzunare', 'Două buzunare laterale'),
   ('material', '55% Poliamida, 45% Poliester'), ('bandă', '80% Bumbac, 18% Poliester , 2% Elastan'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian, raportate la dimensiunile europene standard')],
  {'Model': 'Emporio Armani EB000922', 'Material': '55% poliamidă, 45% poliester', 'Caracteristici': 'subțire, clapă împotriva furtunii, manșete elastice', 'Cod produs': 'EB000922.AF20711'},
  notes=['Compoziția include „Umplutura: 100% Poliester”, deși modelul e descris ca neizolat; nu am scris despre umplutură.'])

w(8869,
  f'<p>Paltonul {GUESS} L5BL00 maro este listat la {A(GB, "geci pentru băieți")} și e făcut din imitație de piele întoarsă, un material gros, ușor izolat, fără căptușeală. Fasonul e drept și nu are glugă.</p>'
  '<p>Se încheie cu nasturi, iar buzunarele sunt oblice. E o haină mai lungă decât o geacă obișnuită, pentru zilele răcoroase de toamnă și primăvară.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '64 cm la mărimea 122-125.'), ('Lungimea mânecii', '46 cm.'))
  + '<p>Mărimile încep la 122-125 și ajung la 175, pentru copii de cam 7-16 ani.</p>',
  [('cod', 'L5BL00'), ('culoare', 'culoarea maro'), ('palton', 'Palton copii din colecția Guess'), ('piele', 'Model ușor izolat confecționat din imitatie de piele intoarsa'),
   ('gros', 'Material gros'), ('căptușeală', 'Captuseala: necaptusit'), ('fason', 'Fason drept'), ('glugă', 'fără glugă'), ('nasturi', 'Incheiere cu nasturi'),
   ('buzunare', 'Buzunare oblice'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 64 cm'), ('mărime', '122-125 cm'), ('mânecă', '46 cm')],
  {'Model': 'GUESS L5BL00', 'Material': '100% poliester, imitație de piele întoarsă', 'Caracteristici': 'palton, fason drept, nasturi', 'Cod produs': 'L5BL00.WHGN0'},
  notes=['„Toamnă și primăvară” derivă din izolația ușoară; magazinul nu numește sezonul.'])

w(8877,
  f'<p>Geaca {GUESS} J6RQ03 bej este o {A(GF, "geacă de tranziție pentru fete")} neizolată, din material modelat, cu glugă și căptușeală completă. Poliesterul o face mai rezistentă la îndoire, iar magazinul precizează că nu e impermeabilă.</p>'
  '<p>Umerii sunt coborâți, deci mânecile nu încurcă mișcarea. Se închide cu fermoar, are două buzunare aplicate pe piept, iar mânecile și marginea de jos sunt finisate cu bătături.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '93% poliester, 7% poliamidă.'), ('Lungime', '43 cm la mărimea 158-166.'), ('Lățime la subraț', '47 cm.'))
  + '<p>Mărimile de la 122-125 la 167 se potrivesc orientativ copiilor de 7-14 ani.</p>',
  [('cod', 'J6RQ03'), ('culoare', 'culoarea bej'), ('neizolat', 'Model neizolat confecționat din material modelat'), ('glugă', 'Model cu gluga'),
   ('căptușeală', 'Model neizolat cu captuseala'), ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'), ('impermeabil', 'fără impermeabilitate'),
   ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor nu limitează mobilitatea'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare aplicate pe piept'),
   ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('material', '93% Poliester , 7% Poliamida'), ('lungime', 'Lungimea: 43 cm'),
   ('mărime', '158-166 cm'), ('subraț', 'Latimea la subrat: 47 cm')],
  {'Model': 'GUESS J6RQ03', 'Material': '93% poliester, 7% poliamidă', 'Caracteristici': 'neizolată, glugă, buzunare pe piept', 'Cod produs': 'J6RQ03.WH2K0'})

w(8884,
  f'<p>Geaca {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KB0KB09889 portocalie este o {A(GB, "geacă de iarnă pentru băieți")} izolată, din țesătură netedă, cu umplutură sintetică medie spre groasă și materiale din fibre reciclate. Gulerul ridicat și gluga fixă apără de frig.</p>'
  '<p>Se închide cu fermoar și capse, buzunarele exterioare se închid, iar mânecile se termină cu elastic. Căptușeala e completă, sintetică, iar tăietura e simplă, fără blocare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 sunt pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'KB0KB09889'), ('culoare', 'culoarea portocaliu'), ('izolat', 'Model izolat confecționat din țesătură netedă'), ('groasă', 'medie, groasă'),
   ('reciclat', 'Produsul contine materiale realizate din fibre reciclate'), ('guler', 'Gulerul ridicat și gluga fixă'), ('fermoar', 'Fixare cu fermoar si snap'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('material', '100% Poliester'), ('umplutură', 'sintetică'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB09889', 'Material': '100% poliester', 'Caracteristici': 'izolată, glugă fixă, fermoar și capse', 'Cod produs': 'KB0KB09889'})

w(8892,
  f'<p>Pantofii {A("/brand/biomecanics/", "Biomecanics")} 262101 bej sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} din piele naturală netedă, creați împreună cu podologi pentru dezvoltarea corectă a piciorului. Talpa din cauciuc e flexibilă și plată, iar vârful rotund e cauciucat, ca să protejeze degetele.</p>'
  '<p>Se închid cu velcro, deci se pun și se reglează repede. Interiorul e din textil, iar branțurile detașabile sunt antibacteriene și inodore. Modelul merge primăvara, vara și toamna.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'piele naturală.'), ('Interior', 'material textil.'), ('Talpă', 'material sintetic, cauciuc.'))
  + '<p>Numerele 19-25 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('cod', '262101'), ('culoare', 'bej'), ('piele', 'Fața din piele naturală netedă'), ('podologi', 'creați în colaborare cu podologi pentru a sprijini dezvoltarea corectă a piciorului copilului'),
   ('talpă', 'Talpa flexibilă din cauciuc'), ('plată', 'plată'), ('vârf', 'Vârful rotund, cauciucat sprijină protecția degetelor'),
   ('velcro', 'Închiderea practică cu velcro facilitează încălțarea rapidă și ajustarea încălțămintei'), ('interior', 'Interiorul din material textil'),
   ('branț', 'Branțurile inodore și antibacteriene'), ('detașabile', 'Branțurile detașabile'), ('sezon', 'primăvară, vară și toamnă'), ('naturală', 'Piele naturală'),
   ('textil', 'Material textil'), ('sintetic', 'Material sintetic')],
  {'Model': 'Biomecanics 262101', 'Material': 'piele naturală', 'Caracteristici': 'velcro, branțuri antibacteriene, vârf cauciucat', 'Cod produs': '262101'})
