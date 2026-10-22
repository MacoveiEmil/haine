import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(10368,
  f'<p>Ghetele de iarnă {PRIMIGI} PRO 23749 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} maro, înalte, cu fața din imitație de piele întoarsă și guler moale. Interiorul căptușit cu material textil ține căldura în zilele reci de iarnă.</p>'
  '<p>Fermoarul permite încălțatul și descălțatul rapid, practic pentru copii mici. Vârful rigidizat și călcâiul întărit țin piciorul stabil la mers.</p>'
  '<p>Talpa și tehnologiile:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare.'), ('Shock Absorber', 'tehnologie în talpă care limitează șocurile.'), ('Primigi × SIPeP', 'creată cu podologi.'))
  + '<p>Numerele 25-30 merg, în general, la copii între 2 și 7 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii maro PRO 23749'), ('înalt', 'încălțăminte înaltă pentru copii'),
   ('față', 'Fața din imitație de piele întoarsă cu guler moale'), ('interior', 'Interiorul căptușit din material textil ajută la menținerea căldurii în zilele reci'),
   ('fermoar', 'Închiderea cu fermoar facilitează încălțarea și descălțarea rapidă'), ('întărit', 'Vârful rigidizat și călcâiul întărit'),
   ('talpă', 'Talpa de cauciuc cu bandă de rulare'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă'), ('șocuri', 'limitând șocurile în timpul mișcării'),
   ('SIPeP', 'Tehnologia Primigi × SIPeP'), ('podologi', 'creată în colaborare cu podologi')],
  {'Model': 'Primigi PRO 23749', 'Material': 'imitație de piele întoarsă, interior textil și piele, talpă din cauciuc', 'Caracteristici': 'fermoar, Shock Absorber, Primigi × SIPeP', 'Cod produs': 'PRO 23749'})

w(10375,
  f'<p>Ghetele de iarnă {PRIMIGI} PTIGT 23549 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} bleumarin, înalte, din piele naturală și imitație de piele, cu membrana GORE-TEX®, un laminat ePTFE care oprește apa și vântul. Interiorul căptușit textil ține de cald la temperaturi scăzute.</p>'
  '<p>Înșiretarea rapidă și aricii strâng gheata repede după picior, iar vârful rotund și moale lasă degetele să se miște.</p>'
  '<p>Pentru mersul pe zăpadă:</p>'
  + L(('Călcâi și guler', 'întărite.'), ('Talpă', 'plată, din cauciuc.'), ('Partea de sus', 'piele naturală și material sintetic.'))
  + '<p>Numerele 25-29 sunt, cu aproximație, pentru 2-5 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii bleumarin PTIGT 23549'), ('înalt', 'încălțăminte înaltă'),
   ('material', 'Partea superioară din combinație de piele naturală și imitație de piele'), ('GORE-TEX', 'Membrana GORE-TEX® este un laminat ePTFE care ajută la protecția împotriva apei și a vântului'),
   ('interior', 'Interior căptușit cu material textil ajută la menținerea căldurii'), ('închidere', 'Sistem de înșiretare rapidă și închidere cu arici'),
   ('vârf', 'Vârf rotund și moale permite libertatea de mișcare a degetelor'), ('călcâi', 'Călcâiul întărit și gulerul superior'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Primigi PTIGT 23549', 'Material': 'piele naturală și imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, înșiretare rapidă și arici', 'Cod produs': 'PTIGT 23549'})

w(10383,
  f'<p>Geaca bomber {TH} KG0KG09410 este o {A("/categorie/geci-jachete/", "geacă bomber pentru fete")}, albastră, cu izolație sintetică ușoară și căptușeală completă, pentru zilele mai răcoroase din anotimpurile de tranziție. Materialul textil e rezistent și se întreține ușor.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri. Tivul și manșetele cu nervuri strâng geaca la încheieturi și jos, ca bomberul să stea aproape de corp.</p>'
  '<p>Material și închidere, pe rând:</p>'
  + L(('Închidere', 'capse.'), ('Buzunare', 'laterale.'), ('Glugă', 'nu are.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă bomber pentru copii albastră KG0KG09410'), ('izolație', 'Izolație sintetică ușoară'), ('căptușeală', 'Căptușeala completă'),
   ('tranziție', 'anotimpurile de tranziție'), ('material', 'Confecționată din material textil rezistent'), ('întreținere', 'ușurința în întreținere'), ('croială', 'Croiala regulară'),
   ('lungime', 'Lungimea până la șolduri'), ('nervuri', 'Tivul și manșetele cu nervuri'), ('capse', 'Închiderea cu capse'), ('buzunare', 'Buzunarele laterale practice'),
   ('fără glugă', 'Lipsa glugii'), ('poliester', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KG0KG09410', 'Material': '100% poliester', 'Caracteristici': 'bomber, izolație ușoară, capse, tiv și manșete cu nervuri', 'Cod produs': 'KG0KG09410'})

w(10384,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} LVCKTJM16B este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")}, neagră, cu izolație termică medie, căptușeală completă și logo-ul mărcii, pentru zilele reci. Gluga integrată apără capul de frig și vânt.</p>'
  '<p>Croiala e regulară, cu loc pentru un pulover dedesubt, cu umerii coborâți și lungimea până la șolduri. Tivul cu bordură elastică și manșetele cu nervuri țin aerul rece afară.</p>'
  '<p>Pentru închidere și mâini:</p>'
  + L(('Închidere', 'fermoar și capse.'), ('Buzunare', 'laterale.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-176 sunt, de regulă, pentru 8-16 ani.</p>',
  [('model', 'Calvin Klein Jeans Jachetă pentru copii neagră LVCKTJM16B'), ('izolație', 'Izolație termică medie'), ('căptușeală', 'Căptușeală completă'), ('logo', 'logo-ul caracteristic al mărcii'),
   ('reci', 'zilele reci'), ('glugă', 'Glugă integrată oferă protecție suplimentară a capului împotriva frigului și vântului'),
   ('croială', 'Croiala regulară permite libertatea de mișcare, potrivită pentru a fi purtată cu straturi suplimentare'), ('umeri', 'Mânecile cu linia umerilor coborâtă'),
   ('lungime', 'Lungime până la șolduri'), ('tiv', 'Tiv cu bordură elastică'), ('manșete', 'Manșete cu nervuri'), ('închidere', 'Închidere cu fermoar și capse'),
   ('buzunare', 'Buzunare laterale practice'), ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans LVCKTJM16B', 'Material': '100% poliester', 'Caracteristici': 'izolație medie, glugă integrată, tiv elastic, fermoar și capse', 'Cod produs': 'LVCKTJM16B'})

w(10396,
  f'<p>Ghetele {A("/brand/biomecanics/", "Biomecanics")} 261104 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "încălțăminte pentru bebeluși")}, roz, din piele naturală, căptușite cu lână care ține căldura, pentru zilele reci și uscate. Nu sunt impermeabile, deci nu sunt pentru zăpadă udă sau ploaie.</p>'
  '<p>Aricii cu curea reglabilă se strâng după picior și permit încălțatul rapid. Stabilizatorii laterali și contrafortul rigidizat țin piciorul în poziție la mers.</p>'
  '<p>Talpa și vârful:</p>'
  + L(('Vârf', 'rotund, cauciucat, apără degetele.'), ('Talpă', 'plată, din cauciuc, cu bandă de rulare.'), ('Parteneriat', 'Biomecanics Podology, dezvoltat cu podologi.'))
  + '<p>Numerele 18-25 sunt pentru copii de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte pentru copii din piele roz 261104'), ('piele', 'Partea superioară din piele naturală'), ('lână', 'căptușeala din lână menține căldura'),
   ('uscat', 'Fără impermeabilitate , ceea ce înseamnă că încălțămintea este destinată condițiilor meteorologice uscate'), ('reci', 'zilele reci'),
   ('arici', 'Sistem practic de închidere cu arici cu curea reglabilă'), ('stabilizatori', 'Stabilizatori laterali și contrafortul rigidizat'),
   ('vârf', 'Vârf rotund, cauciucat asigură protecția degetelor'), ('talpă', 'Talpă plată din cauciuc cu bandă de rulare'),
   ('parteneriat', 'Tehnologia Biomecanics Podology Partnership , dezvoltată împreună cu podologi')],
  {'Model': 'Biomecanics 261104', 'Material': 'piele naturală, căptușeală din lână, talpă din cauciuc', 'Caracteristici': 'neimpermeabile, arici cu curea, vârf cauciucat', 'Cod produs': '261104'},
  notes=['Magazinul le numește ghete; sunt listate la Pantofi.'])

w(10403,
  f'<p>{GEOX} MIKIROSHI J45DVA sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, ușori, cu profil scurt, cu aspect de piele întoarsă, pentru purtat zi de zi. Talpa are sistemul Geox Respira, cu trei straturi perforate.</p>'
  '<p>Șireturile plate nu apasă pe arcada piciorului și se strâng după forma lui. Contrafortul rigid ține călcâiul în pantof, ca piciorul să nu alunece la alergat.</p>'
  '<p>Restul e simplu:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 28-35 sunt pentru copii de, în mare, 4-11 ani.</p>'.replace('de, în mare, 4-11 ani', 'de 4-11 ani, în mare'),
  [('model', 'Geox Sneakers pentru copii MIKIROSHI culoarea alb, J45DVA.054EW'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('piele întoarsă', 'confecționat din piele întoarsă'), ('zilnic', 'purtarea zilnică'), RESPIRA,
   ('șireturi', 'Sireturile plate elimina punctele de presiune de pe arcada piciorului'), ('călcâi', 'Contorul de călcâi rigid'),
   ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('vârf', 'Cutie rotunda, intarita'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox MIKIROSHI', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi plate, Geox Respira', 'Cod produs': 'J45DVA.054EW'})

w(10413,
  f'<p>Geaca {A("/brand/wheat/", "Wheat")} 0699-261 este o {A("/categorie/geci-jachete/", "geacă de bumbac pentru fete")}, multicoloră, din material ornamentat, bumbac 100%, neizolată și fără căptușeală. E o geacă ușoară, pentru zilele calde de primăvară sau de la începutul toamnei.</p>'.replace(' de primăvară sau de la începutul toamnei', '')
  + '<p>Croiala e simplă, dreaptă, iar geaca se închide cu nasturi, deci se pune repede peste un tricou sau o rochiță. Nu are glugă și nici căptușeală.</p>'
  '<p>Fiind din bumbac, e simplă și ușor de purtat:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'oblice, pentru mâini.'), ('Material', '100% bumbac.'))
  + '<p>Pe site, mărimile 92-140 acoperă cam vârsta de 2-10 ani.</p>',
  [('model', 'Wheat Geacă de bumbac pentru copii 0699-261'), ('ornamentat', 'Model neizolat confecționat din material ornamentat'), ('material', '100% Bumbac'),
   ('necăptușit', 'Model neizolat fara captuseala'), ('croială', 'Tăiere simplă, fără blocare'), ('nasturi', 'Închiderea convenabilă cu buton'),
   ('fără glugă', 'Gluga: fara gluga'), ('buzunare', 'Buzunare oblice'), ('culoare', 'multicolor')],
  {'Model': 'Wheat 0699-261', 'Material': '100% bumbac', 'Caracteristici': 'neizolată, fără căptușeală, nasturi, buzunare oblice', 'Cod produs': '0699-261'},
  notes=['„Peste un tricou sau o rochiță” e dedus din faptul că e neizolată și necăptușită.'])

w(10417,
  f'<p>Cardiganul {TH} KB0KB10491 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză cardigan pentru băieți")}, bleumarin, uni, din tricot de bumbac 100% cu model torsadat și o broderie discretă cu logo. Stilul e casual, cu nasturi în față.</p>'
  '<p>Croiala e relaxed fit, deci vine comod și peste o cămașă, iar materialul elastic nu încurcă la joacă. Bordurile elastice de la bază și manșete țin forma și strâng ușor.</p>'
  '<p>Ce merită știut în plus:</p>'
  + L(('Închidere', 'nasturi.'), ('Material', '100% bumbac.'), ('Model', 'torsadat, uni.'))
  + '<p>Mărimile 104-176 sunt pentru copii de, cu aproximație, 4-16 ani.</p>'.replace('de, cu aproximație, 4-16 ani', 'de 4-16 ani, cu aproximație'),
  [('model', 'Tommy Hilfiger Cardigan pentru copii din bumbac bleumarin KB0KB10491'), ('uni', 'Modelul uni cu model torsadat'), ('bumbac', '100% Bumbac'),
   ('tricot', 'Tricotul din bumbac'), ('broderie', 'Broderia subtilă cu logo-ul brandului'), ('casual', 'Stilul casual'), ('nasturi', 'Cardigan cu nasturi'),
   ('croială', 'Croiala relaxed fit'), ('elastic', 'Materialul elastic'), ('borduri', 'Bordurile elastice la bază și la manșete')],
  {'Model': 'Tommy Hilfiger KB0KB10491', 'Material': '100% bumbac', 'Caracteristici': 'cardigan, relaxed fit, model torsadat, nasturi', 'Cod produs': 'KB0KB10491'})

w(10421,
  f'<p>Geaca scurtă {A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 323B15066001 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, bleumarin, cu izolație sintetică ușoară, din nailon cu finisaj neted. E gândită pentru anotimpurile de tranziție și vremea schimbătoare.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar căptușeala completă o face ușor de îmbrăcat peste alte straturi. Gulerul ridicat apără gâtul de vânt.</p>'
  '<p>Pentru purtat zilnic, are:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'în față, pentru mâini reci.'), ('Material', '100% nailon, umplutură 100% poliester.'))
  + '<p>Mărimile 136-138 până la 163-174 se potrivesc, de obicei, la 9-16 ani.</p>',
  [('model', 'Polo Ralph Lauren Jachetă scurtă pentru copii bleumarin 323B15066001'), ('matlasat', 'Geaca matlasată bleumarin Polo Ralph Lauren'), ('izolație', 'Izolație sintetică ușoară'),
   ('neted', 'Material rezistent cu finisaj neted'), ('tranziție', 'anotimpurile de tranziție'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'),
   ('căptușeală', 'Căptușeală completă asigură confortul la purtare și facilitează îmbrăcarea peste alte straturi de haine'),
   ('guler', 'Guler ridicat oferă protecție suplimentară gâtului împotriva frigului și a vântului'), ('fermoar', 'Închidere cu fermoar'),
   ('buzunare', 'Buzunare practice în față sunt utile pentru depozitarea obiectelor mici sau pentru încălzirea mâinilor'), ('material', '100% Nailon'),
   ('umplutură', '100% Poliester'), ('zilnic', 'diverse ținute zilnice')],
  {'Model': 'Polo Ralph Lauren 323B15066001', 'Material': '100% nailon, umplutură 100% poliester', 'Caracteristici': 'matlasată, izolație ușoară, guler ridicat', 'Cod produs': '323B15066001'})

w(10427,
  f'<p>{GEOX} CIBERDRON Looney Tunes J66LPA sunt {A("/categorie/adidasi/", "adidași pentru fete")} negri, cu design inspirat de Looney Tunes și lumini în talpă, care îl fac pe copil mai ușor de văzut. Talpa cu membrană Geox Respira™ scoate umezeala și ține picioarele uscate.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, iar călcâiul întărit ține piciorul stabil când copilul aleargă.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'componente textile și sintetice.'), ('Interior', 'căptușeală sintetică și textilă.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 24-31 sunt pentru copii de în jur de 2-7 ani.</p>',
  [('model', 'Geox CIBERDRON Looney Tunes sneakers pentru copii negri J66LPA.05411'), ('Looney', 'Designul inspirat de Looney Tunes'),
   ('lumini', 'Luminile spectaculoase din talpă adaugă veselie și susțin vizibilitatea'), ('Respira', 'Talpa cu membrană elimină umezeala, ceea ce contribuie la menținerea picioarelor uscate'),
   ('arici', 'O închidere practică cu arici facilitează încălțarea și descălțarea rapidă'), ('călcâi', 'Călcâi întărit'),
   ('material', 'Combinația de componente textile și sintetice'), ('interior', 'Căptușeala din material sintetic și textil'), ('talpă', 'O talpă durabilă din cauciuc')],
  {'Model': 'Geox CIBERDRON Looney Tunes', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'lumini în talpă, arici, Geox Respira™', 'Cod produs': 'J66LPA.05411'})
