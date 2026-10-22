import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
GUESS = A('/brand/guess/', 'GUESS')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(12535,
  f'<p>Adidașii {REIMA} Kiirus sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} în culoarea albastru, ușori, cu profil jos, din material textil și piele ecologică, pentru purtarea zilnică. Partea de sus rezistă mai bine la înmuiere, deci pantoful face față unei zile umede, fără să fie complet impermeabil.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, iar velcro-ul face încălțatul și descălțatul ușor.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Inserții Happy Fit', 'detașabile, ajută la alegerea mărimii.'), ('Interior', 'material textil.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 20-28 merg, cu aproximație, la copii de 1-5 ani.</p>',
  [('model', 'Reima Sneakers pentru copii Kiirus 5400006A'), ('culoare', 'Culoare albastru'), ('ușor', 'Model ușor și confortabil'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'),
   ('apă', 'nu garantează impermeabilitatea completă'), ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('Happy Fit', 'Inserțiile detașabile Happy Fit vă permit să alegeți dimensiunea potrivită'),
   ('interior', 'Material textil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă')],
  {'Model': 'Reima Kiirus', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, inserții Happy Fit, rezistență la înmuiere', 'Cod produs': '5400006A'})

w(12537,
  f'<p>Geaca {A("/brand/lego/", "LEGO")} LWJAZ 704 roșie este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, cu căptușeală, pentru frig, cu material exterior rezistent la vânt și apă, tratat cu BIONIC-FINISH ECO în locul stratului DWR clasic. Gulerul ridicat și gluga detașabilă apără de frig.</p>'
  '<p>Fermoarul YKK merge pe toată lungimea și are clapă externă, iar detaliile reflectorizante 3M Scotchlite fac copilul vizibil pe întuneric.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'în față.'), ('Mâneci', 'cu manșetă elastică.'), ('Material', '100% poliester.'))
  + '<p>Gama de mărimi, 104-164, acoperă cam 4-14 ani. Rezistă la ploaie, dar magazinul nu garantează impermeabilitatea completă.</p>',
  [('model', 'Lego Geacă copii LWJAZ 704 culoarea roșu, 11010981'), ('izolat', 'Model izolat cu captuseala'), ('frig', 'material care izolează împotriva frigului'),
   ('vânt', 'Materialul exterior este rezistent la vânt și apă'), ('BIONIC', 'BIONIC-FINISH® ECO - o alternativa ecologica la acoperirea traditionala, hidrofoba DWR'),
   ('glugă', 'Gulerul ridicat și gluga detașabilă oferă protecție suplimentară împotriva frigului'), ('YKK', 'Fermoarele YKK® de înaltă calitate'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă externă'), ('3M', 'Materialele reflectorizante 3M ™ Scotchlite'), ('buzunare', 'In fata buzunare'),
   ('mâneci', 'Mâneci finisate cu o coadă elastică confortabilă'), ('material', '100% Poliester'), ('apă', 'nu garantează impermeabilitatea completă')],
  {'Model': 'LEGO LWJAZ 704', 'Material': '100% poliester, izolată, cu căptușeală', 'Caracteristici': 'glugă detașabilă, fermoar YKK cu clapă, reflectorizante 3M', 'Cod produs': '11010981'})

w(12538,
  f'<p>{GEOX} GISLI sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} maro, uni, cu profil înalt și guler ușor întărit care susține glezna, pentru cei mai mici. Interiorul din material textil și imitație de lână ține de cald în zilele mai reci.</p>'
  '<p>Șireturile elastice și aricii fac încălțatul rapid și reglarea simplă, iar călcâiul întărit ține piciorul pe loc la joacă.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Partea de sus', 'imitație de piele și material textil.'), ('GEOX Respira', 'scoate umezeala și ține piciorul uscat.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-23 se potrivesc băieților de aproximativ 1-3 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii maro B461NE.0AFME'), ('uni', 'Modelul uni al părții superioare'), ('profil', 'Profilul înalt al părții superioare cu guler ușor întărit susține glezna'),
   ('interior', 'Interiorul din material textil și imitație de lână asigură confort în zilele mai reci'), ('închidere', 'Șireturi elastice și închidere cu arici'),
   ('călcâi', 'Călcâiul întărit susține stabilizarea piciorului'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('Respira', 'Tehnologia GEOX Respira™ favorizează eliminarea umidității, ceea ce menține picioarele uscate'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior cu imitație de lână, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice și arici, profil înalt', 'Cod produs': 'B461NE.0AFME'})

w(12540,
  f'<p>Geaca {GUESS} K6YL04 maro este o {A("/categorie/geci-jachete/", "geacă pentru fete")} matlasată, scurtă, cu izolație sintetică ușoară, pentru zilele de tranziție. Are glugă, un motiv animal și logoul Guess, iar croiala regulară lasă loc și pentru un strat pe dedesubt.</p>'
  '<p>Se închide cu fermoar și capse, iar tivul și manșetele cu nervuri țin aerul rece afară.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'sintetică, completă.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '100% poliester.'))
  + '<p>Mărimile încep la 88-96 și ajung la 122-125, pentru fete de cam 1-7 ani.</p>',
  [('model', 'Guess Geacă petrecută pentru copii maro K6YL04 W2597'), ('matlasat', 'Geaca matlasată maro Guess'), ('scurt', 'Lungimea scurtă a modelului'),
   ('izolație', 'Izolație sintetică ușoară'), ('tranziție', 'zilele de tranziție'), ('glugă', 'Glugă practică'), ('motiv', 'Motiv animal și logo Guess'),
   ('croială', 'Croială regulară – permite libertate de mișcare, potrivită pentru a fi purtată cu straturi suplimentare'), ('închidere', 'Închidere cu fermoar și capse'),
   ('nervuri', 'Tivul și manșetele cu nervuri – ajută la ajustare, limitând pătrunderea aerului rece'), ('căptușeală', 'Căptușeală sintetică completă'),
   ('buzunare', 'Buzunare laterale tip slip-on'), ('material', '100% Poliester')],
  {'Model': 'GUESS K6YL04', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, glugă, fermoar și capse', 'Cod produs': 'K6YL04 W2597'})

w(12541,
  f'<p>{GEOX} NASHIK sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil înalt și guler ușor întărit, din piele naturală, piele întoarsă și material textil. Membrana microporoasă din talpă ajută la păstrarea unui interior uscat, iar tehnologia GEOX Respira scoate umezeala spre exterior.</p>'
  '<p>Aricii permit încălțatul rapid, iar călcâiul întărit ține piciorul așezat corect în pantof.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'căptușit cu piele naturală și textil.'), ('Branț', 'din piele naturală, detașabil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-27 sunt pentru fete de în jur de 2-4 ani.</p>',
  [('model', 'Geox NASHIK sneakers pentru copii roz B663HB.0CL22'), ('profil', 'Profilul înalt al părții superioare cu gulerul ușor întărit'),
   ('material', 'Combinația de piele naturală și piele întoarsă cu material textil'), ('membrană', 'Membrana microporoasă din talpă ajută la menținerea unui interior uscat'),
   ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală a piciorului, eliminând umiditatea spre exterior'),
   ('arici', 'Închiderea practică cu arici'), ('călcâi', 'Călcâiul întărit stabilizează piciorul copilului'), ('interior', 'Interiorul căptușit cu piele naturală și material textil'),
   ('branț', 'Branțul detașabil din piele naturală'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox NASHIK', 'Material': 'piele naturală, piele întoarsă și textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, membrană în talpă, arici', 'Cod produs': 'B663HB.0CL22'})

w(12542,
  f'<p>Geaca bomber {GUESS} J6YL05 maro este o {A("/categorie/geci-jachete/", "geacă pentru fete")} scurtă, din imitație de piele, cu umplutură sintetică ușoară, pentru vremea schimbătoare de tranziție. Croiala e lejeră, cu linia umerilor coborâtă și guler clasic.</p>'
  '<p>Se închide cu fermoar, iar manșetele cu nervuri strâng mânecile la încheieturi. Imitația de piele se întreține ușor.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Căptușeală', 'completă.'), ('Material', '100% poliuretan.'), ('Lungime', 'scurtă.'))
  + '<p>Mărimile pornesc de la 122-125 și urcă până la 167, deci fete de aproximativ 7-14 ani.</p>',
  [('model', 'Guess Geacă bomber pentru copii maro J6YL05 W2612'), ('imitație', 'Confecționată din imitație de piele'), ('umplutură', 'Umplutură sintetică ușoară'),
   ('tranziție', 'Caracterul de tranziție face ca geaca să fie potrivită pentru vremea schimbătoare'), ('croială', 'Croială lejeră'), ('umeri', 'Mâneci cu linia umerilor coborâtă'),
   ('guler', 'Guler clasic'), ('fermoar', 'Sistem de închidere cu fermoar'), ('manșete', 'Manșete cu nervuri ajută la ajustarea mânecilor la încheieturi'),
   ('întreținere', 'este ușor de întreținut'), ('căptușeală', 'Căptușeală completă'), ('material', '100% Poliuretan'), ('scurt', 'Lungimea scurtă a modelului')],
  {'Model': 'GUESS J6YL05 (bomber)', 'Material': '100% poliuretan (imitație de piele), umplutură sintetică', 'Caracteristici': 'fermoar, manșete cu nervuri, căptușeală completă', 'Cod produs': 'J6YL05 W2612'})

w(12543,
  f'<p>{GEOX} GISLI bej sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din material textil și piele ecologică, ușori, pentru purtarea zilnică. Au șiret cu fermoar lateral și închidere cu Velcro, deci se reglează o dată și se încalță repede.</p>'
  '<p>Vârful rotund, ușor rigid, lasă degetele să se așeze liber, iar contrafortul rigid ține călcâiul în pantof.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, perforată.'), ('Branț', 'din piele, previne frecarea.'), ('Interior', 'textil, sintetic și piele naturală.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 36-39 se potrivesc fetelor de la vreo 12 ani în sus, orientativ.</p>',
  [('model', 'Geox Sneakers pentru copii GISLI culoarea bej, J654NB.0BCEW'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('degete', 'degetele se pot aranja liber în pantof'), ('călcâi', 'Contorul de călcâi rigid stabilizează călcâiul'), RESPIRA,
   ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'), ('interior', 'Material sintetic, Material textil, Piele naturala'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă')],
  {'Model': 'Geox GISLI', 'Material': 'textil și piele ecologică, interior cu piele, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șiret cu fermoar lateral și Velcro', 'Cod produs': 'J654NB.0BCEW'})

w(12544,
  f'<p>Cizmele {REIMA} Ankka negre sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} de ploaie, din masă plastică netedă, cu finisaj mat, care țin piciorul uscat la precipitații moderate. Partea de sus nu e poroasă, deci se curăță cu o cârpă umedă după bălți.</p>'
  '<p>Bucla de la spate ajută la tras și la scos cizma, iar contrafortul rigid ține călcâiul pe loc.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Vârf', 'cutie rotundă, ușor întărită.'), ('Interior', 'textil.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Gama e lungă, de la 22 la 38, deci merge de la aproximativ 1 an în sus.</p>',
  [('model', 'Reima Cizme copii Ankka culoarea negru, 5400158A'), ('plastic', 'Model confectionat din masă plastică netedă'), ('mat', 'Finisare: mat'),
   ('uscat', 'Modelul este realizat din materiale care asigură uscăciunea în timpul precipitațiilor moderate'), ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior și ajută la scoaterea acestuia'), ('călcâi', 'Contorul de călcâi rigid'),
   ('vârf', 'Cutie rotunda, usor intarita'), ('interior', 'Interiorul textil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă')],
  {'Model': 'Reima Ankka', 'Material': 'masă plastică, interior textil, talpă din cauciuc', 'Caracteristici': 'cizme de ploaie, buclă la spate, finisaj mat', 'Cod produs': '5400158A'})

w(12545,
  f'<p>Geaca {GUESS} N6YL01 neagră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, izolată, cu umplutură sintetică, pentru zilele reci din sezonul de tranziție. Matlasajul împarte uniform izolația, iar lungimea până la șolduri acoperă bine trunchiul.</p>'
  '<p>Are glugă integrată și guler ridicat, care apără capul și gâtul de vânt. Se închide cu fermoar.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Margini', 'elastice la bază și la manșete.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '100% poliester, căptușeală completă.'))
  + '<p>Mărimile 88-96 până la 122-125 sunt pentru băieți de în jur de 1-7 ani.</p>',
  [('model', 'Guess Geacă petrecută pentru copii neagră N6YL01 W2656'), ('matlasat', 'Geaca matlasată neagră Guess'), ('umplutură', 'Umplutura sintetică ajută la menținerea căldurii'),
   ('tranziție', 'sezonului de tranziție'), ('izolație', 'distribuie uniform izolația'), ('lungime', 'Lungimea până la șolduri'), ('glugă', 'Gluga integrată'),
   ('guler', 'Gulerul ridicat oferă o protecție suplimentară pentru gât'), ('fermoar', 'Închiderea cu fermoar'), ('margini', 'Bordurile elastice la bază și manșete'),
   ('buzunare', 'Buzunarele laterale tip slip-on'), ('material', '100% Poliester'), ('căptușeală', 'Căptușeala completă')],
  {'Model': 'GUESS N6YL01', 'Material': '100% poliester, umplutură sintetică', 'Caracteristici': 'matlasată, glugă integrată, guler ridicat', 'Cod produs': 'N6YL01 W2656'})

w(12551,
  f'<p>Adidașii {TH} T1A9-35063 albi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} uni, cu profil scurt, cu exteriorul din material sintetic rezistent, care se păstrează curat ușor. Aricii îl lasă pe copil să se încalțe și să se descalțe singur.</p>'
  '<p>Călcâiul întărit ține piciorul pe loc la joacă, iar interiorul din textil moale e plăcut pe picior.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Branț', 'textil, detașabil.'), ('Talpă', 'din cauciuc.'), ('Model', 'uni, ușor de purtat cu multe ținute.'))
  + '<p>Numerele 30-34 se poartă cam între 6 și 11 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii albi T1A9-35063'), ('uni', 'Design uni'), ('profil', 'Profil scurt'),
   ('sintetic', 'Material sintetic rezistent la exterior care facilitează menținerea încălțămintei curate'), ('arici', 'Închidere practică cu arici care facilitează încălțarea și descălțarea autonomă'),
   ('călcâi', 'Călcâi întărit'), ('interior', 'Material textil moale în interior'), ('branț', 'Branțuri detașabile din material textil'), ('talpă', 'Talpă de cauciuc'),
   ('ținute', 'facilitează asortarea cu multe ținute')],
  {'Model': 'Tommy Hilfiger T1A9-35063', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, branț detașabil, profil scurt', 'Cod produs': 'T1A9-35063'})
