import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
NB = A('/brand/new-balance/', 'New Balance')
GU = '/categorie/unisex-imbracaminte-geci-jachete/'
FARA = 'Titlul site-ului nu are culoare („{0}”); culoarea e cea de la magazin ({1}).'
GORE = 'Magazinul descrie membrana ca 100% impermeabilă; nu am scris „impermeabile”.'

w(13125,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8895022 albastre sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme de iarnă pentru băieți")} izolate, din piele întoarsă și textil, cu căptușeală textilă și membrană GORE-TEX subțire, rezistentă la vânt și respirabilă. Talpa groasă din cauciuc are bandă de rulare antiderapantă și preia șocurile.</p>'
  '<p>Fața e rigidizată, vârful lat nu strânge degetele, iar bucla de la spate și velcro-ul ajută la încălțat. Interiorul e confortabil.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'piele întoarsă, material textil.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 31-35 se poartă cam la 6-11 ani.</p>',
  [('cod', '8895022'), ('culoare', 'Culoare albastru'), ('izolat', 'Model izolat'), ('căptușeală', 'Model cu captuseala textila'), ('GORE-TEX', 'Model cu membrana GORE-TEX®'),
   ('vânt', 'rezistenta la vant si respirabila'), ('antiderapantă', 'absorbție a șocurilor, cu bandă de rulare, antiderapantă'), ('groasă', 'groasă, profilată'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Cutia lată a degetelor'), ('buclă', 'Bucla de la spate'),
   ('velcro', 'Închiderea cu velcro'), ('interior', 'Interior confortabil'), ('gambă', 'Piele intoarsa, Material textil'), ('profil', 'înalt')],
  {'Model': 'Primigi 8895022', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, velcro, talpă antiderapantă', 'Cod produs': '8895022'},
  notes=[FARA.format('Băieți', 'albastru'), GORE])

w(13126,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8934233 albastre, în numerele mari, sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} izolate, din textil și piele ecologică, cu interior din lână care ține de cald la frig. Membrana GORE-TEX e subțire, respirabilă și oprește vântul.</p>'
  '<p>Fața e rigidizată, vârful lat lasă loc degetelor, iar talpa groasă din cauciuc e antiderapantă și durabilă. Se închid cu velcro, iar bucla de la spate ajută la încălțat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Branț', 'lână.'), ('Profil', 'înalt.'))
  + '<p>Numerele 36-39 se poartă orientativ de la 12 ani în sus.</p>',
  [('cod', '8934233'), ('culoare', 'Culoare albastru'), ('izolat', 'Izolare: izolat'), ('piele', 'combinatia materialului textil cu pielea ecologica'), ('lână', 'Un model cu interior din lână'),
   ('GORE-TEX', 'Model cu membrana GORE-TEX®'), ('vânt', 'rezistenta la vant si respirabila'), ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Cutia lată a degetelor'),
   ('antiderapantă', 'absorbție a șocurilor, cu bandă de rulare, antiderapantă'), ('groasă', 'groasă, profilată'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'),
   ('velcro', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'), ('gambă', 'Material sintetic, Material textil'), ('profil', 'înalt')],
  {'Model': 'Primigi 8934233', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, interior din lână, velcro', 'Cod produs': '8934233'},
  notes=[FARA.format('Unisex', 'albastru'), GORE])

w(13226,
  f'<p>Geaca de puf {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KB0KB10091 roșie este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")} matlasată, cu umplutură din puf natural de rață și pene, care izolează bine împotriva frigului. Exteriorul e din poliamidă, iar căptușeala completă din poliester.</p>'
  '<p>Gulerul ridicat și gluga fixă apără capul și gâtul, mânecile se termină cu elastic, iar fermoarul o face ușor de pus și de scos. Pe laterale are două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Umplutură', '70% puf de rață, 30% pene.'), ('Izolație', 'groasă.'))
  + '<p>Mărimile 98-122 se potrivesc pe la 3-7 ani.</p>',
  [('cod', 'KB0KB10091'), ('culoare', 'culoarea roșu'), ('puf', 'Geacă de puf pentru copii din colecția Tommy Hilfiger'), ('matlasat', 'Model izolat confecționat din material matlasat'),
   ('natural', 'Modelul cu umplutură din puf natural și pene garantează un nivel ridicat de izolare împotriva frigului'), ('material', '100% Poliamida'), ('căptușeală', '100% Poliester'),
   ('guler', 'Gulerul ridicat și gluga fixă'), ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('fermoar', 'Închiderea convenabilă cu fermoar'),
   ('buzunare', 'Două buzunare laterale'), ('umplutură', '70% Puf de rata, 30% Pene'), ('groasă', 'groasă')],
  {'Model': 'Tommy Hilfiger KB0KB10091', 'Material': '100% poliamidă, puf de rață', 'Caracteristici': 'puf natural, glugă fixă, guler ridicat', 'Cod produs': 'KB0KB10091'})

w(13238,
  f'<p>Pantofii din piele {PRIMIGI} 2411311 burgundia sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} pentru cei mici, din piele naturală la exterior și la interior. Sky Effect System pune materiale flexibile în talpă, iar colaborarea Primigi × SIPeP ține cont de anatomia piciorului copilului.</p>'
  '<p>Talpa din cauciuc are 1 cm, e flexibilă și are drop zero, vârful e lat, de tip barefoot, și cauciucat. Branțul din piele se scoate, bareta cu velcro se reglează, iar pe călcâi e o aplicație în formă de iepuraș.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'piele naturală.'), ('Interior', 'piele naturală.'), ('Lungime branț', '13,5 cm.'))
  + '<p>Numerele 20-24 țin cam de 1-3 ani.</p>',
  [('cod', '2411311'), ('culoare', 'Culoare burgundia'), ('piele', 'Partea superioară din piele naturală'), ('interior', 'Interior din piele naturală'),
   ('Sky Effect', 'Tehnologia Sky Effect System'), ('SIPeP', 'Colaborarea Primigi × SIPeP'), ('anatomie', 'ia în considerare dezvoltarea și anatomia piciorului copilului'),
   ('talpă', 'Talpă flexibilă din cauciuc'), ('1 cm', 'Înălțimea platformei: 1 cm'), ('drop', 'Construcție zero drop'), ('barefoot', 'Vârf lat de tip barefoot'),
   ('cauciucat', 'Vârf cauciucat'), ('branț', 'Branț detașabil din piele naturală'), ('velcro', 'Închidere cu velcro cu baretă reglabilă'), ('iepure', 'Aplicație drăguță în formă de iepure'),
   ('lungime', 'Lungimea branțului este: 13,5 cm')],
  {'Model': 'Primigi 2411311', 'Material': 'piele naturală', 'Caracteristici': 'Sky Effect System, barefoot, drop zero, velcro', 'Cod produs': '2411311'},
  notes=[FARA.format('piele', 'burgundia')])

w(13239,
  f'<p>Bocancii din piele {PRIMIGI} 2377211 negri sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} de tranziție, netezi, cu vârf rotund, care urcă peste gleznă. Nu au izolație, deci sunt pentru zilele mai calde de primăvară și toamnă.</p>'
  '<p>Talpa e o platformă din cauciuc de 4 cm. Se închid cu fermoar, iar șireturile ajustează potrivirea. Vârful e rigidizat, călcâiul întărit, gulerul ușor întărit, iar căptușeala și branțul sunt textile.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'piele acoperită.'), ('Interior', 'material textil.'), ('Platformă', '4 cm.'))
  + '<p>Numerele 27-30 corespund aproximativ vârstei de 3-7 ani.</p>',
  [('cod', '2377211'), ('culoare', 'Culoare negru'), ('piele', 'Bocancii Primigi sunt încălțăminte din piele pentru copii'), ('neted', 'negru, neted, cu vârf rotund'),
   ('gleznă', 'deasupra gleznei'), ('izolație', 'Fără izolație termică'), ('sezon', 'zilele mai calde de primăvară și toamnă'), ('platformă', 'Înălțimea platformei: 4 cm'),
   ('cauciuc', 'cauciuc'), ('fermoar', 'Închiderea cu fermoar facilitează încălțarea rapidă, iar șireturile permit ajustarea'), ('vârf', 'Vârful rigidizat'),
   ('călcâi', 'călcâiul întărit'), ('guler', 'Gulerul ușor întărit'), ('textil', 'Căptușeala și branțul textil'), ('față', 'Partea superioară:Piele acoperită')],
  {'Model': 'Primigi 2377211', 'Material': 'piele acoperită', 'Caracteristici': 'platformă 4 cm, fermoar și șireturi, neizolați', 'Cod produs': '2377211'},
  notes=[FARA.format('piele', 'negru')])

w(13240,
  f'<p>Geaca matlasată {NB} YJ62H2WF neagră este o {A("/categorie/geci-jachete/", "geacă de tranziție pentru fete")} cu umplutură din puf sintetic și izolație medie, bună și pentru iernile blânde. Materialul combină bumbac și nailon, iar căptușeala sintetică e completă.</p>'
  '<p>Croiala e lejeră, cu loc pentru un strat în plus dedesubt. Gluga e fixă, gulerul ridicat, manșetele au nervuri, iar buzunarele laterale sunt de tip slip-on. Se închide cu fermoar.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '44% bumbac, 56% nailon.'), ('Umplutură', '100% puf sintetic.'), ('Croială', 'lejeră.'))
  + '<p>Mărimile 122-128 până la 166-168 se potrivesc pe la 7-15 ani.</p>',
  [('cod', 'YJ62H2WF'), ('culoare', 'Culoare negru'), ('matlasat', 'Geaca matlasată neagră New Balance'), ('puf', 'Umplutură din puf sintetic'), ('medie', 'Izolație termică medie'),
   ('iarnă', 'sezonul de tranziție și iernile blânde'), ('material', '44% Bumbac, 56% Nailon'), ('căptușeală', 'Căptușeală sintetică integrală'), ('lejeră', 'Croială lejeră'),
   ('straturi', 'permițând purtarea de straturi suplimentare de îmbrăcăminte dedesubt'), ('glugă', 'Glugă fixă'), ('guler', 'Guler ridicat'), ('manșete', 'Manșete cu nervuri'),
   ('buzunare', 'Buzunare laterale tip slip-on'), ('fermoar', 'Închidere cu fermoar'), ('umplutură', 'Umplutură:100% Puf sintetic')],
  {'Model': 'New Balance YJ62H2WF', 'Material': '44% bumbac, 56% nailon', 'Caracteristici': 'puf sintetic, glugă fixă, croială lejeră', 'Cod produs': 'YJ62H2WF'},
  notes=[FARA.format('petrecută', 'negru')])

w(13252,
  f'<p>Geaca varsity {A("/brand/diesel/", "Diesel")} JBIRKYE JACKET neagră este o {A(GU, "geacă unisex")} de tranziție, fără izolație și fără glugă, din bumbac și alte țesături, cu croială lejeră și umeri coborâți. Imprimeul cu logoul Diesel îi dă stilul mărcii.</p>'
  '<p>Se închide cu capse, gulerul e înalt, iar tivul și manșetele au bandă elastică. Buzunarele laterale sunt deschise. Nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% bumbac.'), ('Material 2', '90% poliester, 10% bumbac.'), ('Tiv elastic', '98% poliester, 2% elastan.'))
  + '<p>Mărimile 156-175 merg aproximativ la 13-16 ani.</p>',
  [('model', 'JBIRKYE JACKET'), ('culoare', 'Culoare negru'), ('varsity', 'Geaca varsity neagră de la Diesel'), ('izolație', 'Lipsa izolației termice'), ('glugă', 'fără glugă'),
   ('lejeră', 'Croiala lejeră'), ('umeri', 'Mâneci cu linia umărului coborâtă'), ('logo', 'Imprimeul cu logo-ul mărcii Diesel'), ('capse', 'Închiderea cu capse'),
   ('guler', 'Gulerul înalt'), ('elastic', 'Tivul cu bandă elastică'), ('buzunare', 'Buzunarele laterale deschise'), ('impermeabil', 'fără impermeabilitate'),
   ('material1', 'Material 1:100% Bumbac'), ('material2', 'Material 2:90% Poliester, 10% Bumbac'), ('tiv', 'Tiv elastic:98% Poliester, 2% Elastan')],
  {'Model': 'Diesel JBIRKYE JACKET', 'Material': 'bumbac, poliester', 'Caracteristici': 'varsity, capse, guler înalt', 'Cod produs': 'J02643.KXBR4'},
  notes=[FARA.format('JBIRKYE', 'negru')])

w(13261,
  f'<p>Adidașii {A("/brand/biomecanics/", "Biomecanics")} 261212 bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} izolați, pentru iarnă, cu interior din lână care ține piciorul la o temperatură plăcută. Fața combină piele naturală cu materiale sintetice.</p>'
  '<p>Talpa din cauciuc are bandă de rulare, vârful și călcâiul sunt întărite, iar gulerul întărit ține glezna. Se închid cu șireturi elastice și scai, iar branțurile din lână se scot. Nu sunt impermeabili.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'piele naturală, material sintetic.'), ('Interior', 'lână.'), ('Profil', 'scurt.'))
  + '<p>Numerele 28-34 corespund cam vârstei de 4-11 ani.</p>',
  [('cod', '261212'), ('culoare', 'Culoare bleumarin'), ('izolat', 'încălțăminte izolată termic'), ('lână', 'Izolația interioară din lână'),
   ('față', 'Partea superioară din combinație de piele naturală și materiale sintetice'), ('talpă', 'Talpa de cauciuc cu bandă de rulare'), ('întărit', 'Vârful și călcâiul întărite'),
   ('guler', 'Gulerul întărit'), ('scai', 'Șireturile elastice și închiderea cu scai'), ('branț', 'Branțurile detașabile din lână'), ('impermeabil', 'fără impermeabilitate'),
   ('interior', 'Interior:Lână'), ('profil', 'scurt')],
  {'Model': 'Biomecanics 261212', 'Material': 'piele naturală, interior din lână', 'Caracteristici': 'izolați, branț din lână, scai', 'Cod produs': '261212'})

w(13264,
  f'<p>Geaca matlasată {NB} LAKB0036 verde este o {A(GU, "geacă unisex")} de iarnă, cu umplutură groasă din puf sintetic, din nailon rezistent, cu căptușeală completă tot din nailon. Gluga integrată apără de vânt și frig.</p>'
  '<p>Lungimea ajunge până la șold, partea de jos se strânge cu șnur, iar manșetele cu nervuri țin frigul afară. Buzunarele laterale sunt de tip slip-on, iar fermoarul o face ușor de pus și de scos.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% nailon.'), ('Umplutură', '100% puf sintetic.'), ('Izolație', 'groasă.'))
  + '<p>Mărimile 122-128 până la 170-176 acoperă orientativ 7-16 ani.</p>',
  [('cod', 'LAKB0036'), ('culoare', 'Culoare verde'), ('matlasat', 'Geaca matlasată verde New Balance'), ('groasă', 'Umplutura groasă din puf sintetic'),
   ('rezistent', 'Țesătura rezistentă cu finisaj matlasat'), ('căptușeală', 'Căptușeala sintetică completă'), ('glugă', 'Gluga integrată'), ('șold', 'Lungimea până la șolduri'),
   ('șnur', 'Partea inferioară cu șnur'), ('manșete', 'Manșetele cu nervuri'), ('buzunare', 'Buzunarele laterale practice de tip slip-on'), ('fermoar', 'Închiderea cu fermoar'),
   ('material', 'Material principal:100% Nailon'), ('umplutură', 'Umplutură:100% Puf sintetic'), ('nailon', 'Căptușeală:100% Nailon')],
  {'Model': 'New Balance LAKB0036', 'Material': '100% nailon, puf sintetic', 'Caracteristici': 'izolație groasă, glugă, tiv cu șnur', 'Cod produs': 'LAKB0036'})

w(13269,
  f'<p>Geaca reversibilă {A("/brand/bobo-choses/", "Bobo Choses")} Clover verde este o {A("/categorie/geci-jachete/", "geacă de tranziție pentru fete")} ușoară, cu izolație sintetică subțire, dintr-o combinație de țesături. Are guler și detalii decorative, fără glugă.</p>'
  '<p>Se închide cu cleme, iar mânecile se termină cu o bandă elastică confortabilă. Tăietura e simplă, iar faptul că e reversibilă îți dă două variante de purtare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliester.'), ('Material 2', '100% poliamidă.'), ('Izolație', 'ușoară.'))
  + '<p>Mărimile 89/98 până la 149/155 țin cam de 1-12 ani.</p>',
  [('model', 'Clover'), ('culoare', 'culoarea verde'), ('reversibil', 'geacă reversibilă pentru copii Clover'), ('ușor', 'Model ușor confecționat dintr-o combinație de țesături diferite'),
   ('sintetică', 'sintetică'), ('ușoară', 'ușoară'), ('guler', 'Model cu guler'), ('decorativ', 'Detalii decorative'), ('glugă', 'fără glugă'), ('cleme', 'Incheiere cu cleme'),
   ('elastic', 'Mâneci finisate cu o coadă elastică'), ('tăiere', 'Tăiere simplă, fără blocare'), ('material1', '100% Poliester'), ('material2', '100% Poliamida')],
  {'Model': 'Bobo Choses Clover', 'Material': 'poliester, poliamidă', 'Caracteristici': 'reversibilă, cleme, guler', 'Cod produs': '225AC121'})
