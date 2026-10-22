import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GF = '/categorie/geci-jachete/'
GU = '/categorie/unisex-imbracaminte-geci-jachete/'

w(9228,
  f'<p>Geaca {A("/brand/gosoaky/", "Gosoaky")} DESERT FOX verde este o {A(GU, "geacă unisex")} izolată, din poliester reciclat, cu impregnare DWR fără PFC, tehnologia Bionic-Finish Eco: apa nu intră în material, ci se adună la suprafață și se scurge. Rezistența la apă declarată e de 8000 mm.</p>'
  '<p>Gluga din trei bucăți ține mai cald capul, iar fermoarul pe toată lungimea are clapă interioară și exterioară. Izolația e medie spre groasă, cu căptușeală completă și două buzunare laterale.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', 'poliester reciclat.'), ('Glugă', 'integrată, din trei piese.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 98-104 până la 158-164 sunt pentru copii de aproximativ 3-14 ani.</p>',
  [('model', 'DESERT FOX'), ('culoare', 'culoarea verde'), ('izolat', 'Model izolat confectionat fabricate din țesătură cu un strat hidrofob'),
   ('reciclat', 'Poliester reciclat'), ('DWR', 'DWR fără PFC'), ('Bionic', 'Bionic-Finish® Eco'), ('scurge', 'făcând ca apa să se condenseze la suprafață și să se scurgă de ea'),
   ('8000', 'Impermeabilitate: 8000 mm/m2/24h'), ('glugă', 'Gluga din trei piese oferă un plus de căldură'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea, cu clapă interioară și exterioară'), ('groasă', 'medie, groasă'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('buzunare', 'Două buzunare laterale'), ('croială', 'Croială: regular fit')],
  {'Model': 'Gosoaky DESERT FOX', 'Material': 'poliester reciclat', 'Caracteristici': 'DWR fără PFC, glugă din trei piese, clapă dublă', 'Cod produs': '252.9.1.514'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă. Produsul e marcat și „pentru bebe”.'])

w(9236,
  f'<p>Geaca de schi {A("/brand/rossignol/", "Rossignol")} WISPILE turcoaz pe site (bleumarin la magazin) este o {A(GU, "geacă unisex")} ușor izolată, din material modelat, cu umplutură sintetică și glugă integrată. Înăuntru are centură de zăpadă, care oprește zăpada să intre sub geacă chiar și la o căzătură.</p>'
  '<p>Mânecile raglan nu încurcă mișcarea și au manșon cu gaură pentru degetul mare. Pe lângă cele două buzunare laterale cu fermoar, are unul pe piept și unul pe mânecă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', 'completă, sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-170 se potrivesc orientativ copiilor de 8-15 ani.</p>',
  [('model', 'WISPILE'), ('culoare', 'bleumarin'), ('izolat', 'Model ușor izolat confecționat din material modelat'), ('umplutură', 'sintetică'), ('glugă', 'integrată'),
   ('centură', 'La interior, o centură de zăpadă încorporată'), ('cădere', 'împiedică pătrunderea zăpezii sub jachetă, chiar și în caz de cădere'),
   ('raglan', 'Maneca raglan'), ('degetul', 'Manson cu gaura pentru degetul mare'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('piept', 'Buzunar pe piept'), ('mânecă', 'Un buzunar suplimentar pe mânecă'), ('material', '100% Poliester'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('croială', 'Croială: regular fit')],
  {'Model': 'Rossignol WISPILE', 'Material': '100% poliester', 'Caracteristici': 'centură de zăpadă, mâneci raglan, 4 buzunare', 'Cod produs': 'RLNYJ02'},
  notes=['Culoarea din titlul site-ului (turcoaz) nu se potrivește cu cea a magazinului (bleumarin).'])

w(9255,
  f'<p>Geaca {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KG0KG08927 violet este o {A(GF, "geacă de tranziție pentru fete")} ușor izolată, din material neted, realizată parțial din poliester reciclat. Nu are glugă, iar izolația ușoară e prinsă pe căptușeală.</p>'
  '<p>Tăietura e simplă, fără blocare, iar închiderea se face cu fermoar. E o geacă potrivită pentru zilele răcoroase, când o haină groasă ar fi prea mult.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', 'completă.'), ('Izolație', 'ușoară.'))
  + '<p>Mărimile 116-122 sunt pentru copii de cam 6-7 ani.</p>',
  [('cod', 'KG0KG08927'), ('culoare', 'culoarea violet'), ('izolat', 'Model usor izolat confecționat din material neted'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('glugă', 'fără glugă'), ('căptușeală', 'Model usor izolat pe captuseala'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'), ('material', '100% Poliester'), ('ușoară', 'ușoară'), ('completă', 'cu căptușeală completă')],
  {'Model': 'Tommy Hilfiger KG0KG08927', 'Material': '100% poliester', 'Caracteristici': 'ușor izolată, fermoar', 'Cod produs': 'KG0KG08927'},
  notes=['Sursa are puține detalii; „zilele răcoroase” derivă din izolația ușoară.'])

w(9258,
  f'<p>Bocancii {A("/brand/geox/", "Geox")} JUNETTE negri sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} cu talpă groasă, plată, canelată, din spumă EVA ușoară și elastică, și sistemul Geox Respira, cu talpă în trei straturi perforată pentru ventilare.</p>'
  '<p>Se leagă cu șiret clasic și au fermoar lateral, deci se pun și se scot ușor. Vârful e rotund, ușor întărit, contrafortul rigid ține călcâiul pe loc, iar bucla de la spate ajută la încălțat. Interiorul e textil.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic.'), ('Interior', 'material textil.'), ('Izolație', 'nu au.'))
  + '<p>Numerele 36-39 se poartă de pe la 12 ani în sus.</p>',
  [('model', 'JUNETTE'), ('culoare', 'culoarea negru'), ('canelată', 'Modelul cu talpa exterioară canelată'), ('EVA', 'Talpa exterioară este realizată din spumă EVA ușoară, elastică'),
   ('groasă', 'groasă, plată'), ('Respira', 'Sistemul Geox Respira'), ('straturi', 'talpei in trei straturi cu sistemul de perforari'), ('șiret', 'Șiretul clasic permite ajustarea individuală'),
   ('fermoar', 'Închiderea laterală convenabilă cu fermoar'), ('vârf', 'Cutie rotunda, usor intarita'), ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece'),
   ('buclă', 'Bucla de la spate'), ('interior', 'Interiorul textil este confortabil'), ('gambă', 'Material sintetic'), ('textil', 'Material textil'), ('neizolat', 'Izolare: neizolat')],
  {'Model': 'Geox JUNETTE', 'Talpă': 'EVA, Geox Respira', 'Caracteristici': 'șiret, fermoar lateral, talpă groasă', 'Cod produs': 'J56HVB.000BC'},
  notes=['Descrierea spune „piele întoarsă”, iar compoziția indică material sintetic, imitație de piele; am scris doar compoziția.'])

w(9266,
  f'<p>Geaca {A("/brand/liewood/", "Liewood")} Brantley Jacket portocalie este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă pentru bebeluși")} ușor izolată, din material textil cu model, din poliester reciclat certificat GRS. Croiala e lejeră, supradimensionată, cu umerii coborâți și spatele mai lung, care acoperă la mișcare.</p>'
  '<p>Gulerul ridicat apără de frig, fermoarul pe toată lungimea are clapă interioară și protecție pentru bărbie, iar mânecile se termină cu manșetă elastică. În față are două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Glugă', 'nu are.'), ('Umplutură', 'sintetică, ușoară.'))
  + '<p>Mărimile 86-140 se potrivesc orientativ copiilor de 1-10 ani.</p>',
  [('model', 'Brantley Jacket'), ('culoare', 'culoarea portocaliu'), ('izolat', 'Model ușor izolat confecționat din material textil cu model'),
   ('GRS', 'GLOBAL RECYCLED STANDARD (GRS)'), ('lejeră', 'Tăiere lejeră, fără blocare'), ('supradimensionat', 'Croială: supradimensionat'),
   ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'), ('spate', 'Spatele mai lung oferă acoperire atunci când vă mișcați'),
   ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară împotriva furtunii'),
   ('bărbie', 'Model echipat cu protecție pentru bărbie'), ('manșetă', 'Mâneci lungi finisate cu o manșetă confortabilă, elastică'),
   ('buzunare', 'Două buzunare în față'), ('material', '100% Poliester reciclat'), ('glugă', 'fără glugă'), ('umplutură', 'sintetică')],
  {'Model': 'Liewood Brantley Jacket', 'Material': '100% poliester reciclat (GRS)', 'Caracteristici': 'oversize, protecție la bărbie, spate prelungit', 'Cod produs': 'LW20056'})

w(9306,
  f'<p>Adidașii {A("/brand/biomecanics/", "Biomecanics")} 262159 albi sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} creați împreună cu podologi, pentru dezvoltarea sănătoasă a picioarelor mici și o mișcare naturală. Fața din textil și material sintetic e ușoară, iar talpa plată din cauciuc ține bine pe diverse suprafețe.</p>'
  '<p>Călcâiul e moale, gulerul de sus e ușor întărit și sprijină glezna. Branțul detașabil absoarbe șocurile, e respirabil și are imprimeu pentru verificarea mărimii. Se închid cu arici.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Interior', 'material textil.'), ('Lungime branț', '14,5 cm la numărul 24.'), ('Profil', 'scurt.'))
  + '<p>Numerele 24-26 sunt pentru copii de aproximativ 2-4 ani.</p>',
  [('cod', '262159'), ('culoare', 'alb'), ('podologi', 'creat în colaborare cu podologi'), ('dezvoltare', 'dezvoltarea sănătoasă a picioarelor mici'),
   ('față', 'Partea superioară din material textil și sintetic'), ('talpă', 'Talpă din cauciuc'), ('plată', 'plată'), ('călcâi', 'Călcâi moale'),
   ('guler', 'Guler superior ușor întărit'), ('branț', 'Branț cu absorbție a șocurilor și respirabil'), ('imprimeu', 'Branț detașabil cu imprimeu'),
   ('arici', 'Închidere practică cu arici'), ('interior', 'Interior din material textil'), ('lungime', 'Lungimea branțului este: 14,5 cm'), ('mărime', 'Dimensiuni indicate pentru mărimea: 24'),
   ('profil', 'scurt')],
  {'Model': 'Biomecanics 262159', 'Material': 'textil și material sintetic', 'Caracteristici': 'arici, branț detașabil, călcâi moale', 'Cod produs': '262159'},
  notes=['Titlul site-ului nu are culoare; culoarea e cea de la magazin (alb).'])

w(9314,
  f'<p>Geaca reversibilă {A("/brand/guess/", "GUESS")} J5BL25 neagră este o {A(GF, "geacă de tranziție pentru fete")} neizolată, care combină imitația de blană cu o țesătură netedă, deci se poate purta pe ambele fețe. Are glugă integrată și căptușeală completă, sintetică.</p>'
  '<p>Se închide cu fermoar, are două buzunare laterale și buzunare interioare. Magazinul precizează că nu este impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliester.'), ('Material 2', '100% poliamidă.'), ('Lungime', '50 cm la mărimea 122-125.'), ('Lățime la umeri', '33 cm.'))
  + '<p>Mărimile încep la 122-125 și ajung la 167, potrivite orientativ copiilor de 7-14 ani.</p>',
  [('cod', 'J5BL25'), ('culoare', 'culoarea negru'), ('reversibil', 'Geacă reversibilă pentru copii din colecția Guess'),
   ('blană', 'combinație de imitație de blană și țesătură netedă'), ('neizolat', 'Model neizolat cu captuseala'), ('glugă', 'Model cu gluga'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare laterale'), ('interioare', 'Buzunare interioare'),
   ('impermeabil', 'fără impermeabilitate'), ('material1', '100% Poliester'), ('material2', '100% Poliamida'), ('lungime', 'Lungimea: 50 cm'), ('mărime', '122-125 cm'),
   ('umeri', 'Latimea in umeri: 33 cm')],
  {'Model': 'GUESS J5BL25', 'Material': 'poliester, poliamidă, imitație de blană', 'Caracteristici': 'reversibilă, glugă, buzunare interioare', 'Cod produs': 'J5BL25.WHGO0'})

w(9351,
  f'<p>Geaca {A("/brand/patrizia-pepe/", "Patrizia Pepe")} 7O0044 neagră este o {A(GF, "geacă de iarnă pentru fete")} izolată, cu umplutură sintetică groasă care apără de frig și căptușeală completă din poliamidă. Gulerul ridicat și gluga încorporată adaugă căldură când e nevoie.</p>'
  '<p>Tăietura e simplă, fermoarul o face ușor de pus și de scos, iar mânecile se termină cu elastic. Mărimile sunt italienești, raportate la cele europene, așa că merită verificat tabelul magazinului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', '100% poliamidă.'), ('Umplutură', '100% poliester.'))
  + '<p>Mărimile 140-168 sunt pentru copii de aproximativ 10-15 ani.</p>',
  [('cod', '7O0044'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat confecționat material care protejează împotriva frigului'), ('groasă', 'groasă'),
   ('umplutură', 'sintetică'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('glugă', 'Gluga încorporată oferă un plus de căldură'), ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'),
   ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('tabel', 'va rugam sa consultati tabelul cu marimi'),
   ('material', '100% Poliester'), ('poliamidă', '100% Poliamida')],
  {'Model': 'Patrizia Pepe 7O0044', 'Material': '100% poliester, căptușeală din poliamidă', 'Caracteristici': 'izolație groasă, glugă, guler ridicat', 'Cod produs': '7O0044'})

w(9377,
  f'<p>Geaca {A("/brand/columbia/", "Columbia")} Hikebound bordo pe site (roz la magazin) este o {A(GF, "geacă de iarnă pentru fete")} izolată, din material neted, cu izolație sintetică medie spre groasă. Tehnologia Omni-Tech are membrană microporoasă, respirabilă, și cusături sudate, iar Omni-Heat ajută la reglarea temperaturii corpului.</p>'
  '<p>Are glugă integrată, se închide cu fermoar și velcro, iar mânecile se termină cu elastic. În talie are bandă elastică, iar cele două buzunare laterale au fermoar.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '57 cm la mărimea 116.'), ('Impermeabilitate', 'membrană impermeabilă.'))
  + '<p>Mărimile 104-164 se potrivesc orientativ copiilor de 4-14 ani.</p>',
  [('model', 'Hikebound'), ('culoare', 'roz'), ('izolat', 'Model izolat confecționat din material neted'), ('groasă', 'medie, groasă'),
   ('Omni-Tech', 'Tehnologia Omni-tech® ofera protectie completa impotriva schimbarilor bruste ale vremii datorita membranei microporoase, respirabile si a cusaturilor sudate'),
   ('Omni-Heat', 'Tehnologia Omni-Heat regleaza temperatura corpului'), ('glugă', 'integrată'), ('fermoar', 'Fixarea cu fermoar si velcro'),
   ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('talie', 'Banda elastica in talie'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('material', '100% Poliester'), ('lungime', 'Lungimea: 57 cm'), ('mărime', '116 cm'), ('membrană', 'membrană impermeabilă')],
  {'Model': 'Columbia Hikebound', 'Material': '100% poliester', 'Caracteristici': 'Omni-Tech, Omni-Heat, glugă integrată', 'Cod produs': '2089971'},
  notes=['Culoarea din titlul site-ului (bordo) nu se potrivește cu cea a magazinului (roz).'])

w(9387,
  f'<p>Adidașii {A("/brand/primigi/", "Primigi")} PIM GTX 24192 negri sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt și membrană GORE-TEX Invisible Fit integrată în față, care ține picioarele uscate și se potrivește mai bine. Fața din textil și material sintetic e durabilă și ușor de întreținut.</p>'
  '<p>Călcâiul e întărit, iar gulerul ușor întărit cuprinde glezna. Talpa din cauciuc e flexibilă, iar închiderea cu arici îi ajută pe copii să se încalțe singuri. Branțul textil absoarbe umezeala.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Interior', 'material textil.'), ('Lungime branț', '19 cm la numărul 30.'), ('Talpă', 'cauciuc, flexibilă, plată.'))
  + '<p>Numerele 30-35 se potrivesc orientativ copiilor de 6-11 ani.</p>',
  [('cod', '24192'), ('culoare', 'negru'), ('profil', 'încălțăminte cu profil scurt'), ('GORE-TEX', 'Tehnologia GORE-TEX® Invisible Fit'),
   ('uscate', 'contribuie la menținerea picioarelor uscate și la o potrivire mai bună'), ('față', 'Partea superioară din material textil și sintetic'),
   ('călcâi', 'Călcâi întărit'), ('guler', 'Gulerul superior ușor întărit'), ('talpă', 'Talpa flexibilă din cauciuc'), ('arici', 'Închiderea practică cu arici'),
   ('autonomie', 'autonomia copilului'), ('branț', 'Branțul din material textil'), ('umezeală', 'absorbind umezeala'), ('interior', 'Interior:Material textil'),
   ('lungime', 'Lungimea branțului este: 19 cm'), ('mărime', 'Dimensiuni indicate pentru mărimea: 30')],
  {'Model': 'Primigi PIM GTX 24192', 'Membrană': 'GORE-TEX Invisible Fit', 'Caracteristici': 'arici, talpă flexibilă, călcâi întărit', 'Cod produs': '2419255'},
  notes=['Titlul site-ului nu are culoare; culoarea e cea de la magazin (negru).'])
