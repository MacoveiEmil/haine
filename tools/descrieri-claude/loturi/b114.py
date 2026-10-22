import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
LIEW = A('/brand/liewood/', 'Liewood')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'

w(9505,
  f'<p>Geaca {A("/brand/karl-lagerfeld/", "Karl Lagerfeld")} Z30234 aurie este o {A(GF, "geacă de iarnă pentru fete")} izolată, matlasată, din material neted cu strat de poliuretan, cu umplutură sintetică medie spre groasă. Gluga nu se detașează.</p>'
  '<p>Se închide cu fermoar, iar gulerul ridicat acoperă și bărbia. Căptușeala e din poliester și viscoză. Mărimile sunt italienești, raportate la cele europene, deci merită verificat tabelul magazinului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester cu strat de poliuretan.'), ('Căptușeală', '53% poliester, 47% viscoză.'), ('Umplutură', '100% poliester.'))
  + '<p>Mărimile 156-162 sunt pentru copii de aproximativ 13-14 ani.</p>',
  [('cod', 'Z30234'), ('culoare', 'culoarea auriu'), ('izolat', 'Model izolat confectionat din material neted'), ('matlasat', 'Matlasare'), ('groasă', 'medie, groasă'),
   ('glugă', 'Gluga nedetasabila'), ('fermoar', 'Are inchidere cu fermoar si guler ridicat cu barbie'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'),
   ('tabel', 'va rugam sa consultati tabelul cu marimi'), ('material', '100% Poliester cu strat de poliuretan'), ('căptușeală', '53% Poliester , 47% Viscoza'),
   ('umplutură', '100% Poliester')],
  {'Model': 'Karl Lagerfeld Z30234', 'Material': 'poliester cu strat de poliuretan', 'Caracteristici': 'izolată, matlasată, glugă fixă', 'Cod produs': 'Z30234'})

w(9524,
  f'<p>Geaca {A("/brand/bobo-choses/", "Bobo Choses")} 225AC129 multicoloră este o {A(GB, "geacă de tranziție pentru băieți")} neizolată și fără căptușeală, dintr-un material rezistent. Gulerul ridicat și gluga fixă apără de frig și vânt.</p>'
  '<p>Tăietura e simplă, se închide cu fermoar și capsă, iar buzunarele exterioare sunt oblice și se închid. E o geacă subțire, pentru zilele de primăvară sau toamnă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 99/110 până la 149/155 se potrivesc orientativ copiilor de 3-12 ani.</p>',
  [('cod', '225AC129'), ('culoare', 'Culoare multicolor'), ('neizolat', 'Model neizolat confecționat material rezistent'), ('căptușeală', 'fără căptușeală'),
   ('guler', 'Gulerul ridicat și gluga fixă'), ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Fixare cu fermoar si snap'),
   ('buzunare', 'Buzunare exterioare oblice, incheiate'), ('material', '100% Poliester'), ('umplutură', 'fără umplutură'), ('croială', 'Croială: regular fit')],
  {'Model': 'Bobo Choses 225AC129', 'Material': '100% poliester', 'Caracteristici': 'neizolată, glugă fixă, fermoar și capsă', 'Cod produs': '225AC129'},
  notes=['Titlul site-ului nu are culoare; culoarea e cea de la magazin (multicolor).', '„Primăvară sau toamnă” derivă din „neizolat, fără căptușeală”.'])

w(9531,
  f'<p>Geaca {TH} KG0KG09373 roz este o {A(GF, "geacă matlasată pentru fete")}, lejeră, pentru zilele mai răcoroase, din nailon ușor și rezistent la uzură. Matlasarea ondulată ține de cald, iar modelul floral discret îi dă un aer vesel.</p>'
  '<p>Se închide cu capse, la fel ca buzunarele laterale. Umerii sunt căzuți, lungimea ajunge până la șold, iar gulerul vătuit apără gâtul. Pe piept are steagul Tommy Hilfiger.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% nailon.'), ('Glugă', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 sunt pentru copii de cam 8-16 ani.</p>',
  [('cod', 'KG0KG09373'), ('culoare', 'Culoare roz'), ('lejeră', 'o propunere lejeră pentru zilele mai răcoroase'), ('nailon', 'Confecționată din nailon'),
   ('uzură', 'lejeritate și rezistență la uzura de zi cu zi'), ('ondulată', 'Matlasarea ondulată ajută la menținerea căldurii'), ('floral', 'model floral subtil'),
   ('capse', 'Închiderea cu capse'), ('buzunare', 'Buzunare laterale cu închidere cu capse'), ('umeri', 'umeri căzuți'), ('șold', 'Lungimea până la șolduri'),
   ('guler', 'Gulerul vătuit'), ('steag', 'steagul pe piept'), ('material', '100% Nailon'), ('glugă', 'fără glugă'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KG0KG09373', 'Material': '100% nailon', 'Caracteristici': 'matlasare ondulată, capse, guler vătuit', 'Cod produs': 'KG0KG09373'})

w(9534,
  f'<p>Geaca {A("/brand/columbia/", "Columbia")} Nordic Strider bordo este o {A(GB, "geacă de iarnă pentru băieți")} izolată, cu izolație groasă și membrană Omni-Tech microporoasă, respirabilă, cu cusături sudate. Omni-Heat ajută la reglarea temperaturii corpului, iar umplutura e în mare parte din poliester reciclat.</p>'
  '<p>Sistemul OUTGROWN o ajută să țină mai multe sezoane, pe măsură ce copilul crește. Gluga are blăniță artificială detașabilă, fermoarul are clapă antifurtună cu velcro, iar mânecile se termină cu elastic.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', '85% poliester reciclat, 15% poliester.'), ('Lungime', '50 cm la mărimea 116.'))
  + '<p>Mărimile 104-164 se potrivesc orientativ copiilor de 4-14 ani.</p>',
  [('model', 'Nordic Strider'), ('culoare', 'culoarea bordo'), ('izolat', 'Model izolat confecționat material impermeabil'), ('groasă', 'groasă'),
   ('Omni-Tech', 'membranei microporoase, respirabile si a cusaturilor sudate'), ('Omni-Heat', 'Tehnologia Omni-Heat regleaza temperatura corpului'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('OUTGROWN', 'Sistemul OUTGROWN Grow de la Columbia'), ('sezoane', 'astfel incat sa reziste mai multe sezoane'),
   ('blăniță', 'Gluga cu blanita artificiala, detasabila'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă antifurtună cu velcro'),
   ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('material', '100% Poliester'), ('umplutură', '85% Poliester reciclat, 15% Poliester'), ('lungime', 'Lungimea: 50 cm'),
   ('mărime', '116 cm')],
  {'Model': 'Columbia Nordic Strider', 'Material': '100% poliester', 'Caracteristici': 'Omni-Tech, Omni-Heat, OUTGROWN', 'Cod produs': '2090222'},
  notes=['Pagina magazinului dă în titlu „culoarea bordo”, iar în datele produsului „maro” (Camel).'])

w(9587,
  f'<p>Cizmele de iarnă {A("/brand/geox/", "Geox")} J26ETA negre sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} ușor izolate, cu interior textil confortabil, care se păstrează ușor curat. Talpa e din gumă, profilată.</p>'
  '<p>Au șiret, fermoar lateral și închidere cu velcro, deci se pun și se scot repede. Vârful e rotund și ușor întărit, contrafortul rigid ține călcâiul pe loc, iar branțul are contur. Bucla de la spate ajută la încălțat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic.'), ('Interior', 'material textil.'), ('Lungime branț', '23,5 cm la numărul 36.'))
  + '<p>Numerele 36-39 se poartă de pe la 12 ani în sus.</p>',
  [('cod', 'J26ETA'), ('culoare', 'Culoare negru'), ('izolat', 'Model Izolare usoara'), ('interior', 'Model cu interior textil care este confortabil pentru picior'),
   ('talpă', 'Talpa din guma'), ('profilată', 'profilată'), ('fermoar', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('vârf', 'Cutie rotunda, usor intarita'),
   ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece'), ('branț', 'Brant confortabil, cu contur'), ('buclă', 'Bucla de la spate'),
   ('gambă', 'Material sintetic'), ('textil', 'Material textil'), ('lungime', 'Lungimea brantului pentru marimea este de: 23,5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 36')],
  {'Model': 'Geox J26ETA', 'Talpă': 'gumă, profilată', 'Caracteristici': 'ușor izolate, șiret, fermoar lateral, velcro', 'Cod produs': 'J26ETA.000BC'},
  notes=['Descrierea spune „piele întoarsă”, iar compoziția și atributele indică material sintetic, imitație de piele; am scris doar compoziția.'])

w(9589,
  f'<p>Geaca {A("/brand/konges-slojd/", "Konges Sløjd")} MAGOT JACKET albastră este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă pentru bebeluși")} subțire, din denim de bumbac organic certificat, cultivat fără îngrășăminte și pesticide. Are căptușeală completă și detalii din imitație de blană.</p>'
  '<p>Tăietura e simplă, se încheie cu nasturi pe toată lungimea, iar manșetele se încheie și ele. Pe piept are un buzunar. Magazinul precizează că nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material de bază', '100% bumbac.'), ('Material suplimentar', '100% poliester.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 86 până la 110-116 sunt pentru copii de aproximativ 1-6 ani.</p>',
  [('model', 'MAGOT JACKET'), ('culoare', 'Culoare albastru'), ('denim', 'Model subțire confecționat din denim de bumbac'), ('organic', 'bumbac organic certificat'),
   ('pesticide', 'fara utilizarea ingrasamintelor sau pesticidelor'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('blană', 'Material: imitatie blana'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('nasturi', 'Incheiere lunga cu nasturi'), ('manșete', 'Mansete incheiate'), ('piept', 'Buzunar pe piept'),
   ('impermeabil', 'fără impermeabilitate'), ('material', '100% Bumbac'), ('suplimentar', '100% Poliester'), ('glugă', 'fără glugă')],
  {'Model': 'Konges Sløjd MAGOT JACKET', 'Material': 'bumbac organic (denim)', 'Caracteristici': 'denim, nasturi, căptușeală completă', 'Cod produs': 'KS105178'},
  notes=['Titlul site-ului are „JACKET” în locul culorii; culoarea e cea de la magazin (albastru, denim).'])

w(9591,
  f'<p>Salopeta de ploaie {LIEW} Maddy PU Rainsuit portocalie este o {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopetă unisex")} cu mânecă lungă, din material ornamentat cu membrană impermeabilă și izolație THERMOLITE EcoMade din sticle de plastic reciclate. Certificatul GRS confirmă materialele reciclate.</p>'
  '<p>Hamul ține pantalonii pe loc la joacă, iar manșetele elastice stau bine pe încheieturi și lasă loc pentru mănuși. Mânecile raglan nu încurcă, fermoarul are guler ridicat cu protecție la bărbie, iar inserțiile reflectorizante ajută la vizibilitate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Umplutură', '100% Thermolite.'), ('Izolație', 'ușoară spre medie.'))
  + '<p>Mărimile 86-122 se potrivesc orientativ copiilor de 1-7 ani.</p>',
  [('model', 'Maddy PU Rainsuit'), ('culoare', 'culoarea portocaliu'), ('mânecă', 'Model cu maneca lunga, confecționat din material ornamentat'),
   ('membrană', 'membrană impermeabilă'), ('THERMOLITE', 'Izolatia THERMOLITE® EcoMade este fabricata din sticle de plastic reciclate 100%'), ('GRS', 'GRS (Global Recycle Standard)'),
   ('ham', 'Hamul previne alunecarea pantalonilor în timpul activității'), ('manșete', 'Manșetele elastice se potrivesc perfect la încheieturile tale'),
   ('mănuși', 'să bagi cu ușurință manșetele mănușilor dedesubt'), ('raglan', 'Mânecile raglan'), ('fermoar', 'Are inchidere cu fermoar si guler ridicat cu barbie'),
   ('reflectorizant', 'Model cu insertii reflectorizante'), ('material', '100% Poliester reciclat'), ('umplutură', '100% Thermolite'), ('izolație', 'ușoară, medie')],
  {'Model': 'Liewood Maddy PU Rainsuit', 'Material': '100% poliester reciclat, Thermolite', 'Caracteristici': 'membrană impermeabilă, ham, reflectorizante', 'Cod produs': 'LW20049'},
  notes=['Magazinul spune o dată glugă „detașabilă” și o dată „încorporată”; nu am scris despre glugă.'])

w(9646,
  f'<p>Geaca scurtă {TH} KB0KB10396 bleumarin este o {A(GB, "geacă de tranziție pentru băieți")} din nailon, cu glugă care se ascunde în guler și iese la o schimbare bruscă a vremii. Gulerul înalt apără gâtul de frig și vânt.</p>'
  '<p>Manșetele și tivul sunt elastice, ca să țină căldura înăuntru. Fermoarul pe toată lungimea o face ușor de pus și de scos, lungimea ajunge până la șold, iar în față are două buzunare oblice.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', 'nailon.'), ('Guler', 'ridicat.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 sunt pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'KB0KB10396'), ('culoare', 'Culoare bleumarin'), ('scurtă', 'Geaca scurtă bleumarin Tommy Hilfiger'), ('glugă', 'Gluga care se poate ascunde discret în guler'),
   ('vreme', 'în cazul unei schimbări bruște a vremii'), ('guler', 'Gulerul înalt protejează gâtul de frig și vânt'), ('manșete', 'Manșetele elastice'),
   ('tiv', 'Tivul elastic'), ('fermoar', 'Închiderea cu fermoar pe toată lungimea'), ('șold', 'Lungimea până la șolduri'), ('buzunare', 'Două buzunare oblice în față'),
   ('material', 'Întregul produs:Nailon'), ('ridicat', 'Guler și revere: ridicat'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB10396', 'Material': 'nailon', 'Caracteristici': 'glugă ascunsă în guler, manșete și tiv elastice', 'Cod produs': 'KB0KB10396'})

w(9673,
  f'<p>Geaca bomber {A("/brand/guess/", "GUESS")} N6RL04 neagră este o {A(GB, "geacă de tranziție pentru băieți")} ușor izolată, din imitație de piele, cu căptușeală completă. Mânecile și marginea de jos sunt finisate cu benzi elastice confortabile, ca la orice bomber.</p>'
  '<p>Tăietura e simplă, se închide cu fermoar, iar pe laterale are două buzunare. Nu are glugă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Lungime', '45 cm la mărimea 113-118.'), ('Lungimea mânecii', '42 cm.'), ('Lățime la subraț', '35 cm.'))
  + '<p>Mărimile 88-96 până la 122-125 se potrivesc orientativ copiilor de 1-7 ani.</p>',
  [('cod', 'N6RL04'), ('culoare', 'Culoare negru'), ('bomber', 'Geacă bomber pentru copii din colecția Guess'), ('piele', 'Model ușor izolat confecționat din imitație de piele'),
   ('căptușeală', 'cu căptușeală completă'), ('elastic', 'Mâneci și marginea inferioară finisate cu colțuri elastice, confortabile'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare laterale'), ('glugă', 'fără glugă'), ('lungime', 'Lungimea: 45 cm'), ('mărime', '113 - 118 cm'),
   ('mânecă', 'Lungimea manecii. 42 cm'), ('subraț', 'Latimea la subrat: 35 cm')],
  {'Model': 'GUESS N6RL04', 'Material': 'imitație de piele', 'Caracteristici': 'bomber, ușor izolată, margini elastice', 'Cod produs': 'N6RL04.WH2J0'},
  notes=['Compoziția de la magazin e cea a unei încălțări (gambă, talpă), deci nu am folosit-o.'])

w(9677,
  f'<p>Geaca tehnică {LIEW} Kalle Jacket roz este o {A(GF, "geacă de iarnă pentru fete")} izolată, cu umplutură THERMOLITE EcoMade din sticle de plastic reciclate, medie spre groasă. Toate cusăturile sunt lipite, ca să oprească vântul și umezeala, iar materialul are impregnare hidrofobă.</p>'
  '<p>Gulerul ridicat și gluga fixă apără de frig, talia se ajustează cu șnur, iar mânecile raglan au manșete care se încheie. Buzunarele exterioare se închid, iar înăuntru are buzunare oblice.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Căptușeală', '100% poliester reciclat.'), ('Umplutură', '100% Thermolite.'))
  + '<p>Mărimile 98-140 sunt pentru copii de cam 3-10 ani.</p>',
  [('model', 'Kalle Jacket'), ('culoare', 'Culoare roz'), ('tehnică', 'Geacă tehnica pentru copii din colecția Liewood'), ('THERMOLITE', 'Izolatia THERMOLITE® EcoMade este fabricata din sticle de plastic reciclate 100%'),
   ('groasă', 'medie, groasă'), ('lipite', 'Toate cusăturile sunt lipite'), ('vânt', 'împiedică pătrunderea vântului și a umezelii'), ('hidrofob', 'impregnare hidrofobă'),
   ('guler', 'Gulerul ridicat și gluga fixă'), ('talie', 'Ajustare în talie cu șnur'), ('raglan', 'Maneca raglan'), ('manșete', 'Maneci cu mansete incheiate'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('interioare', 'Buzunare oblice interioare'), ('material', '100% Poliester reciclat'), ('umplutură', '100% Thermolite')],
  {'Model': 'Liewood Kalle Jacket', 'Material': '100% poliester reciclat, Thermolite', 'Caracteristici': 'cusături lipite, glugă fixă, talie cu șnur', 'Cod produs': 'LW20052'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])
