import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
KS = A('/brand/konges-slojd/', 'Konges Sløjd')
CKJ = A('/brand/calvin-klein-jeans/', 'Calvin Klein Jeans')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
GU = '/categorie/unisex-imbracaminte-geci-jachete/'

w(11309,
  f'<p>Geaca de puf {A("/brand/emporio-armani/", "Emporio Armani")} 8N4BQ2 neagră este o {A(GB, "geacă puf pentru băieți")}, matlasată, umplută cu puf natural reciclat de rață, cu izolație medie. Conține și fibre reciclate.</p>'
  '<p>Se închide cu fermoar și are guler ridicat, fără glugă. Cele două buzunare laterale se închid prin apăsare. Tăietura e simplă. Mărimile sunt italienești, raportate la cele europene.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', '80% puf de rață, 20% pene de rață.'), ('Lungime', '45 cm la mărimea 128.'))
  + '<p>Mărimile 128-176 corespund orientativ vârstei de 8-16 ani.</p>',
  [('cod', '8N4BQ2'), ('culoare', 'culoarea negru'), ('puf', 'Geaca de puf pentru copii din colecția Emporio Armani'), ('matlasat', 'Model usor izolat confecționat din din material matlasat'),
   ('reciclat', 'Modelul este umplut cu puf natural, reciclat'), ('fibre', 'Produsul conține materiale din fibre reciclate'), ('medie', 'medie'),
   ('fermoar', 'Are inchidere cu fermoar si guler ridicat'), ('glugă', 'fără glugă'), ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '100% Poliester'),
   ('umplutură', '80% Duck Down, 20% Pene de rață'), ('lungime', 'Lungimea: 45 cm'), ('mărime', '128 cm')],
  {'Model': 'Emporio Armani 8N4BQ2', 'Material': '100% poliester, puf de rață', 'Caracteristici': 'puf reciclat, guler ridicat, fermoar', 'Cod produs': '8N4BQ2.1NLRZ'})

w(11323,
  f'<p>Geaca de schi {A("/brand/burton/", "Burton")} FROSTNER neagră este o {A(GU, "geacă unisex")} ușor izolată, din nailon rezistent, cu membrană impermeabilă și certificare Bluesign. Burton are și certificarea B Corporation, pentru standarde sociale și de mediu.</p>'
  '<p>Gulerul ridicat și gluga fixă apără de frig, mânecile raglan nu încurcă mișcarea, iar înăuntru are o centură flexibilă, cauciucată, contra zăpezii. Buzunarele exterioare se închid, iar unul e pentru skipass.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% nailon.'), ('Lungime', '63 cm la mărimea 116-122.'), ('Izolație', 'ușoară.'))
  + '<p>Mărimile 116-122 până la 164-166 merg cu aproximație la 6-14 ani.</p>',
  [('model', 'FROSTNER'), ('culoare', 'culoarea negru'), ('schi', 'Geacă de schi pentru copii din colecția Burton'), ('izolat', 'Model ușor izolat confecționat din material rezistent'),
   ('membrană', 'membrană impermeabilă'), ('Bluesign', 'Model certificat Bluesign® Standard'), ('B Corp', 'B Corporation'), ('guler', 'Gulerul ridicat și gluga fixă'),
   ('raglan', 'Maneca raglan'), ('centură', 'In interior este o centura flexibila, cauciucata'), ('buzunare', 'Buzunare exterioare incheiata'),
   ('skipass', 'Buzunar funcțional pentru permis de schi'), ('material', '100% Nailon'), ('lungime', 'Lungimea: 63 cm'), ('mărime', '116-122 cm'), ('ușoară', 'ușoară')],
  {'Model': 'Burton FROSTNER', 'Material': '100% nailon', 'Caracteristici': 'membrană, centură de zăpadă, buzunar skipass', 'Cod produs': '233641'},
  notes=['Pagina magazinului dă în titlu „culoarea negru”, iar în datele produsului „violet”.'])

w(11351,
  f'<p>Cămașa {TH} KG0KG09306 albastră e printre {A("/categorie/bluze-tricouri-hanorace/", "bluzele pentru fete")}, din poplin de bumbac pur, moale și respirabil. Are dungi verticale și steaguri brodate în formă de steluțe pe toată suprafața.</p>'
  '<p>Gulerul e clasic, semi-italian, iar pe piept are un buzunar aplicat. Pe interiorul decolteului e o bandă cu marca. Croiala e regular fit, lejeră la mișcare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Guler', 'clasic.'), ('Model', 'dungi verticale, steluțe brodate.'))
  + '<p>Între 128 și 176, vârsta potrivită e cam 8-16 ani.</p>',
  [('cod', 'KG0KG09306'), ('culoare', 'Culoare albastru'), ('poplin', 'poplin din bumbac pur'), ('respirabil', 'favorizează respirabilitatea și moliciunea la atingere'),
   ('dungi', 'model în dungi verticale'), ('steluțe', 'steaguri brodate în formă de steluțe pe toată suprafața'), ('guler', 'guler clasic semi-italian'),
   ('buzunar', 'buzunar aplicat pe piept'), ('bandă', 'bandă distinctivă pe partea interioară a decolteului'), ('croială', 'Croială: regular fit'),
   ('material', 'Întregul produs:100% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG09306', 'Material': '100% bumbac (poplin)', 'Caracteristici': 'dungi, steluțe brodate, buzunar pe piept', 'Cod produs': 'KG0KG09306'},
  notes=['Titlul site-ului are „bumbac” în locul culorii; culoarea e cea de la magazin (albastru).'])

w(11359,
  f'<p>Ghetele de iarnă {TH} T3X4-34141 negre sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "ghete pentru băieți")} ușor izolate, din textil și material sintetic, cu profil înalt care sprijină glezna pe teren neuniform. Talpa exterioară din cauciuc e durabilă și rezistentă la deteriorare.</p>'
  '<p>Șireturile rapide cu opritor fac încălțatul ușor. Vârful e rotund și întărit, spatele călcâiului e rigidizat, iar inserția textilă detașabilă se curăță ușor. Interiorul e confortabil.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Lungime branț', '21 cm la numărul 34.'))
  + '<p>Numerele 30-34 merg, orientativ, la 6-11 ani.</p>',
  [('cod', 'T3X4-34141'), ('culoare', 'culoarea negru'), ('izolat', 'Model Izolare ușoară'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('neuniforme', 'suprafețe neuniforme'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'),
   ('șireturi', 'Sistemul rapid de șireturi cu opritoare'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Spatele calcaiului rigidizat'),
   ('inserție', 'Inserție textilă detașabilă, ușor de curățat'), ('interior', 'Interior confortabil'), ('gambă', 'Material sintetic, Material textil'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 21 cm'), ('mărime', 'Dimensiunile date pentru marimea: 34'), ('profil', 'înalt')],
  {'Model': 'Tommy Hilfiger T3X4-34141', 'Talpă': 'cauciuc', 'Caracteristici': 'ușor izolate, șireturi rapide, profil înalt', 'Cod produs': 'T3X4.34141'},
  notes=['Pe site sunt la Cizme; magazinul le descrie ca pantofi de iarnă cu profil înalt.'])

w(11386,
  f'<p>Jacheta scurtă {A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 313B18915001 roz este o {A(GF, "geacă matlasată pentru fete")}, în stil harrington, ușor izolată cu umplutură sintetică, pentru zilele mai reci de tranziție. Materialul e durabil, iar căptușeala completă face îmbrăcatul ușor.</p>'
  '<p>Se închide dublu, cu fermoar și nasturi, nu are glugă, iar lungimea ajunge până la șold. În față are buzunare care se închid.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', '100% poliester.'), ('Mânecă', 'clasică.'))
  + '<p>Mărimile 130-134 până la 155-159 țin cam de 8-13 ani.</p>',
  [('cod', '313B18915001'), ('culoare', 'Culoare roz'), ('harrington', 'stilul harrington cu un finisaj matlasat'), ('ușor', 'Izolația sintetică ușoară'),
   ('reci', 'confort în zilele mai reci'), ('durabil', 'Material durabil'), ('căptușeală', 'Căptușeală completă'), ('închidere', 'Sistemul dublu de închidere cu fermoar și nasturi'),
   ('glugă', 'Fără glugă'), ('șold', 'Lungimea până la șolduri'), ('buzunare', 'Buzunare practice în față, cu închidere'), ('material', 'Material principal:100% Poliester'),
   ('umplutură', 'Umplutură:100% Poliester'), ('mânecă', 'Tip de mânecă: clasică')],
  {'Model': 'Polo Ralph Lauren 313B18915001', 'Material': '100% poliester', 'Caracteristici': 'harrington, matlasată, fermoar și nasturi', 'Cod produs': '313B18915001'})

w(11449,
  f'<p>Paltonul {KS} FUZZIE COAT roșu este listat la {A(GF, "geci pentru fete")} și e făcut din imitație de blană cu model, din poliester reciclat certificat GRS. Are căptușeală completă din bumbac și izolație ușoară, potrivită pentru tranziție.</p>'
  '<p>Designul e simplu, nu încurcă mișcarea, iar gulerul e moale. Se închide cu capse pe un singur rând. Nu are glugă și nu e impermeabil.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Căptușeală', '100% bumbac.'), ('Închidere', 'capse.'))
  + '<p>Mărimile 86 până la 134-140 sunt gândite cu aproximație pentru 1-10 ani.</p>',
  [('model', 'FUZZIE COAT GRS'), ('culoare', 'Culoare rosu'), ('blană', 'Material: imitatie blana'), ('model', 'confecționat din material cu model'),
   ('reciclat', 'Material principal: 100% poliester reciclat'), ('bumbac', 'din bumbac, cu căptușeală completă'), ('ușoară', 'ușoară'), ('tranziție', 'Izolare: tranzitional'),
   ('simplu', 'Design simplu care nu restricționează mișcarea'), ('guler', 'Guler moale'), ('capse', 'Închidere cu capse la un singur rând de nasturi'),
   ('glugă', 'fără glugă'), ('impermeabil', 'fără impermeabilitate'), ('căptușeală', 'Căptușeală: 100% bumbac')],
  {'Model': 'Konges Sløjd FUZZIE COAT', 'Material': 'poliester reciclat, căptușeală din bumbac', 'Caracteristici': 'imitație de blană, capse, guler moale', 'Cod produs': 'KS104302'},
  notes=['Titlul site-ului are „FUZZIE” în locul culorii; culoarea e cea de la magazin (roșu).', 'Descrierea are formularea confuză „fără căptușeală, căptușită”; am urmat caracteristicile (căptușeală completă din bumbac).'])

w(11478,
  f'<p>Jacheta {A("/brand/jack-wolfskin/", "Jack Wolfskin")} ADVENTURETRIBE 2L JKT K bleumarin este o {A(GU, "geacă unisex")} ușoară, de exterior, cu tehnologia TEXAPORE CORE: membrana oprește apa și vântul și lasă pielea să respire. Coloana de apă e de 10 000 mm, iar respirabilitatea de 6 000 g/m²/24h.</p>'
  '<p>Fermoarele sunt rezistente la apă, gulerul e înalt, iar detaliile reflectorizante se văd după lăsarea întunericului. Croiala e regulară, până la șold, cu loc pentru un strat în plus dedesubt.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Material', '100% poliester.'), ('Tehnologie', 'TEXAPORE CORE.'))
  + '<p>Mărimile 104-152 se potrivesc pe la 4-12 ani.</p>',
  [('model', 'ADVENTURETRIBE 2L JKT K'), ('culoare', 'Culoare bleumarin'), ('ușoară', 'jachetă ușoară de exterior'), ('TEXAPORE', 'Tehnologia TEXAPORE CORE'),
   ('membrană', 'Construcția cu membrană blochează eficient apa și vântul, permițând în același timp pielii să respire'), ('coloană', 'Nivel impermeabilitate: 10 000 mm H2O'),
   ('respirabil', 'Respirabilitate: 6 000 g/m²/24h'), ('fermoare', 'Fermoare rezistente la apă'), ('guler', 'guler înalt'),
   ('reflectorizant', 'Detalii reflectorizante sporesc vizibilitatea copilului după lăsarea întunericului'), ('straturi', 'permițând purtarea de straturi suplimentare'),
   ('șold', 'Lungime până la șolduri'), ('buzunare', 'Două buzunare laterale cu fermoar'), ('material', 'Întregul produs:100% Poliester')],
  {'Model': 'Jack Wolfskin ADVENTURETRIBE 2L JKT K', 'Material': '100% poliester', 'Caracteristici': 'TEXAPORE CORE, 10 000 mm, fermoare rezistente la apă', 'Cod produs': 'A65947'},
  notes=['Descrierea spune „glugă integrată”, caracteristicile „detașabilă”; nu am precizat tipul glugii.'])

w(11525,
  f'<p>Geaca bomber {CKJ} IB0IB02567 neagră este o {A(GB, "geacă de tranziție pentru băieți")} ușoară, dintr-o combinație de țesături, cu bumbac și puțin elastan. Fasonul e lejer, iar umerii coborâți nu limitează mișcarea.</p>'
  '<p>Se închide cu capse, are guler moale, buzunare oblice și mâneci lungi cu manșetă elastică. Căptușeala e completă. Nu are glugă și nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '98% bumbac, 2% elastan.'), ('Închidere', 'capse.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-170 corespund cam vârstei de 8-15 ani.</p>',
  [('cod', 'IB0IB02567'), ('culoare', 'culoarea negru'), ('bomber', 'Geaca bomber pentru copii din colecția Calvin Klein Jeans'), ('ușor', 'Model usor confecționat din dintr-o combinatie de tesaturi diferite'),
   ('lejer', 'Fason lejer'), ('umeri', 'linie coborâtă a umerilor'), ('capse', 'Închiderea convenabilă cu capsă'), ('guler', 'Model cu guler moale'),
   ('buzunare', 'Buzunare oblice'), ('manșetă', 'Mâneci lungi finisate cu o manșetă confortabilă, elastică'), ('căptușeală', 'cu căptușeală completă'),
   ('glugă', 'fără glugă'), ('impermeabil', 'fără impermeabilitate'), ('material', '98% Bumbac, 2% Elastan'), ('croială', 'Croială: regular fit')],
  {'Model': 'Calvin Klein Jeans IB0IB02567', 'Material': '98% bumbac, 2% elastan', 'Caracteristici': 'bomber, umeri coborâți, capse', 'Cod produs': 'IB0IB02567'})

w(11556,
  f'<p>Sacoul de catifea {KS} ROCKY BLAZER verde este listat la {A("/categorie/bebe-imbracaminte-geci-jachete/", "geci pentru bebeluși")} și e făcut din velur de bumbac cu puțin elastan, un material foarte confortabil. E căptușit cu poliester și viscoză.</p>'
  '<p>Designul e simplu, ușor de purtat, cu revere clasice și închidere cu nasturi pe un singur rând. Bumbacul domină compoziția, cu doar 2% elastan, așa că velurul e plăcut la atingere și cedează puțin la mișcare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '98% bumbac, 2% elastan.'), ('Căptușeală', '55% poliester, 45% viscoză.'), ('Închidere', 'nasturi, un rând.'))
  + '<p>Mărimile 86 până la 134-140 acoperă orientativ 1-10 ani.</p>',
  [('model', 'ROCKY BLAZER'), ('culoare', 'Culoare verde'), ('catifea', 'sacou de catifea'), ('velur', 'este confecționat din velur'),
   ('confortabil', 'material excepțional de confortabil, cu un conținut ridicat de bumbac'), ('căptușit', 'Căptușit'), ('simplu', 'Design simplu, ușor de purtat'),
   ('revere', 'Revere clasice'), ('nasturi', 'Închidere cu nasturi la un singur rând de nasturi'), ('material', '98% bumbac, 2% elastan'), ('căptușeală', '55% poliester, 45% viscoză')],
  {'Model': 'Konges Sløjd ROCKY BLAZER', 'Material': '98% bumbac, 2% elastan (velur)', 'Caracteristici': 'sacou, revere clasice, nasturi', 'Cod produs': 'KS104412'},
  notes=['Pe site e la geci; magazinul îl descrie ca sacou.'])

w(11605,
  f'<p>Geaca de blugi {CKJ} IU0IU00727 albastră este o {A(GF, "geacă de blugi pentru fete")}, din denim rigid care își păstrează forma, cu puțin elastan. E neizolată și fără căptușeală, potrivită pentru zilele de tranziție.</p>'
  '<p>Se închide cu nasturi, manșetele moi au și ele nasturi, iar pe piept are un buzunar. Tăietura e simplă. Nu are glugă și nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '93% bumbac, 7% elastan.'), ('Umplutură', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>De la 128 la 170, mărimile țin cam de 8-15 ani.</p>',
  [('cod', 'IU0IU00727'), ('culoare', 'Culoare albastru'), ('denim', 'Model neizolat confecționat din denim'), ('rigid', 'material rigid, care păstrează forma'),
   ('căptușeală', 'fără căptușeală'), ('tranziție', 'Izolare: tranzitional'), ('buton', 'Închiderea convenabilă cu buton'), ('manșete', 'Manșete moi cu închidere cu nasturi'),
   ('buzunar', 'Buzunar pe piept'), ('tăiere', 'Tăiere simplă, fără blocare'), ('glugă', 'fără glugă'), ('impermeabil', 'fără impermeabilitate'),
   ('material', '93% Bumbac, 7% Elastan'), ('umplutură', 'fără umplutură'), ('croială', 'Croială: regular fit')],
  {'Model': 'Calvin Klein Jeans IU0IU00727', 'Material': '93% bumbac, 7% elastan', 'Caracteristici': 'denim rigid, nasturi, buzunar pe piept', 'Cod produs': 'IU0IU00727'},
  notes=['Titlul site-ului are „blugi” în locul culorii; culoarea e cea de la magazin (albastru).'])
