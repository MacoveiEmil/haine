import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(10537,
  f'<p>Ghetele {A("/brand/primigi/", "Primigi")} PTIGT 23549 sunt {A("/categorie/unisex-incaltaminte-pantofi/", "încălțăminte de iarnă unisex")}, galbene, din piele naturală, cu membrana GORE-TEX® din ePTFE, care oprește apa și vântul. Sunt pentru aventurile de iarnă și joaca afară, pe frig și umezeală.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, iar vârful rotund lasă degetele să se așeze liber. Pielea se adaptează la forma piciorului.</p>'
  '<p>Pentru mers sigur:</p>'
  + L(('Călcâi', 'întărit.'), ('Shock Absorber', 'limitează transferul șocurilor din talpă.'), ('Primigi × SIPeP', 'linie dezvoltată cu podologi.'))
  + '<p>Numerele 20-24 se potrivesc copiilor mici, de cam 1-3 ani.</p>',
  [('model', 'Primigi Încălțăminte pentru copii din piele galbenă PTIGT 23549'), ('iarnă', 'încălțăminte de iarnă pentru copii'), ('piele', 'Fața din piele naturală'),
   ('GORE-TEX', 'Tehnologia GORE-TEX® cu membrană ePTFE protejează împotriva apei și a vântului'), ('aer liber', 'aventurilor de iarnă și a diverselor activități în aer liber'),
   ('arici', 'Sistemul de închidere cu arici facilitează încălțarea și descălțarea rapidă'), ('vârf', 'Vârful rotund permite așezarea liberă a degetelor'),
   ('adaptare', 'adaptându-se la forma piciorului'), ('călcâi', 'Călcâiul întărit'), ('Shock Absorber', 'Sistemul Shock Absorber din talpă limitează transferul șocurilor'),
   ('SIPeP', 'Linia de încălțăminte Primigi × SIPeP , dezvoltată în colaborare cu podologi')],
  {'Model': 'Primigi PTIGT 23549', 'Material': 'piele naturală, interior textil, talpă sintetică', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber', 'Cod produs': 'PTIGT 23549'},
  notes=['Sunt ghete de iarnă, listate la Pantofi.'])

w(10542,
  f'<p>Geaca {A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 312B29175001 este o {A("/categorie/geci-jachete/", "geacă de puf pentru fete")}, bleumarin, cu finisaj lucios, umplută cu puf natural (75% puf, 25% pene de rață) cu elasticitate de 650 cuin. E pentru zilele geroase de iarnă.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, deci trunchiul rămâne acoperit la joacă. Gluga integrată și gulerul ridicat apără capul și gâtul de vânt și frig.</p>'
  '<p>Geaca mai are:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'tip slip-on.'), ('Căptușeală', 'completă, din nailon.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 94-100 până la 124-128 sunt pentru copii de 2-8 ani, cu aproximație.</p>',
  [('model', 'Polo Ralph Lauren Jachetă pentru copii bleumarin 312B29175001'), ('lucios', 'Țesătură rezistentă cu finisaj lucios'), ('puf', '75% Puf de rață, 25% Pene de rață'),
   ('650', 'Puf natural cu elasticitate de 650 cuin'), ('geroase', 'zilele geroase'), ('croială', 'Croiala regulară'), ('lungime', 'Lungimea până la șolduri'),
   ('glugă', 'Glugă integrată'), ('guler', 'Guler ridicat'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'), ('buzunare', 'Buzunare practice tip slip-on'),
   ('căptușeală', 'Căptușeală completă'), ('nailon', '100% Nailon'), ('material', '100% Poliester')],
  {'Model': 'Polo Ralph Lauren 312B29175001', 'Material': '100% poliester; umplutură 75% puf, 25% pene de rață; căptușeală nailon', 'Caracteristici': 'puf 650 cuin, glugă integrată, guler ridicat', 'Cod produs': '312B29175001'})

w(10543,
  f'<p>{A("/brand/donsje/", "Donsje")} 3048502 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă bomber unisex")}, bleumarin, ușoară, din bumbac și poliester, fără izolație termică, cu aplicații și broderii decorative. E pentru vremea schimbătoare din sezonul de tranziție.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar bordurile elastice de la bază și manșete strâng bomberul pe corp. Fără izolație, se poartă ușor peste alte straturi.</p>'
  '<p>Pentru zi de zi, are:</p>'
  + L(('Închidere', 'capse.'), ('Buzunare', 'laterale.'), ('Căptușeală', 'parțială, din bumbac.'), ('Material', '57% bumbac, 43% poliester.'))
  + '<p>Mărimile 98-140 sunt pentru copii de în jur de 3-10 ani.</p>',
  [('model', 'Donsje Geacă bomber pentru copii cu bumbac bleumarin 3048502'), ('ușor', 'Construcția ușoară'), ('neizolat', 'Fără izolație termică permite stratificarea liberă a hainelor'),
   ('decor', 'Detaliile decorative sub formă de aplicații și broderii'), ('tranziție', 'sezonului de tranziție'), ('croială', 'Croiala regulară'), ('lungime', 'Lungimea până la șolduri'),
   ('borduri', 'Bordurile elastice la bază și manșete'), ('capse', 'Închiderea comodă cu capse'), ('buzunare', 'Buzunarele laterale practice'),
   ('căptușeală', 'Căptușeala parțială din bumbac'), ('material', '57% Bumbac, 43% Poliester')],
  {'Model': 'Donsje 3048502', 'Material': '57% bumbac, 43% poliester; mâneci 100% poliester', 'Caracteristici': 'bomber, neizolat, capse, borduri elastice', 'Cod produs': '3048502'})

w(10547,
  f'<p>{GEOX} GISLI Hello Kitty B661MC sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, cu profil înalt și imprimeu Hello Kitty, din imitație de piele și material textil, ușor de întreținut. Membrana Geox Respira™ scoate umezeala spre exterior.</p>'
  '<p>Aricii îl lasă pe copil să se încalțe singur, iar gulerul ușor întărit cuprinde glezna. Branțurile se scot, pentru curățat sau pentru verificat mărimea.</p>'
  '<p>Detaliile de material și talpă:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'piele naturală și material textil.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 20-27 se poartă cam între 1 și 4 ani.</p>',
  [('model', 'Geox GISLI Hello Kitty sneakers pentru copii roz B661MC.05402'), ('profil', 'sneakerși cu profil înalt'), ('Hello Kitty', 'Imprimeul adorabil Hello Kitty'),
   ('material', 'Fața superioară din imitație de piele și material textil'), ('întreținere', 'ușurința de întreținere'), ('Respira', 'Tehnologia GEOX Respira™'),
   ('umezeală', 'eliminând umezeala spre exterior'), ('arici', 'Închiderea cu arici'), ('autonom', 'facilitează încălțarea și descălțarea autonomă de către copil'),
   ('guler', 'Gulerul superior ușor întărit'), ('branțuri', 'Branțurile detașabile'), ('călcâi', 'Călcâiul întărit'), ('interior', 'Interiorul din piele naturală și material textil'),
   ('talpă', 'Talpa din cauciuc')],
  {'Model': 'Geox GISLI Hello Kitty', 'Material': 'imitație de piele și textil, interior din piele și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici, branțuri detașabile, Geox Respira™', 'Cod produs': 'B661MC.05402'})

w(10551,
  f'<p>{TH} KG0KG09538 este o {A("/categorie/bluze-tricouri-hanorace/", "bluză cu mânecă lungă pentru fete")}, turcoaz, din bumbac 100%, cu dungi, imprimeu și inscripție. Decolteul are guler cu închidere, un detaliu care o face puțin mai elegantă.</p>'
  '<p>Croiala e lejeră, iar materialul elastic se îmbracă ușor și nu încurcă la joacă. Stilul e casual, pentru zilele obișnuite.</p>'
  '<p>Pe scurt, despre bluză:</p>'
  + L(('Material', '100% bumbac.'), ('Model', 'dungi, imprimeu și inscripție.'), ('Decolteu', 'cu guler și închidere.'))
  + '<p>Mărimile 128-176 sunt pentru copii de, în mare, 8-16 ani.</p>'.replace('de, în mare, 8-16 ani', 'de 8-16 ani, în mare'),
  [('model', 'Tommy Hilfiger Longsleeve pentru copii din bumbac turcoaz KG0KG09538'), ('material', '100% bumbac'), ('dungi', 'Modelul cu dungi, cu imprimeu și inscripție'),
   ('decolteu', 'Decolteu cu guler și închidere'), ('croială', 'Croială lejeră'), ('elastic', 'Material elastic facilitează îmbrăcarea'), ('casual', 'Stilul casual')],
  {'Model': 'Tommy Hilfiger KG0KG09538', 'Material': '100% bumbac', 'Caracteristici': 'mânecă lungă, croială lejeră, dungi, guler', 'Cod produs': 'KG0KG09538'})

w(10563,
  f'<p>{GEOX} CIBERDRON Spiderman J66LBJ sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} în culoarea albastru, cu motiv Spiderman din universul Marvel și lumini încorporate în talpă, care îl fac pe copil vizibil. Membrana microporoasă din talpă ține apa afară și scoate umezeala, deci picioarele rămân uscate.</p>'
  '<p>Profilul e înalt, cu guler ușor întărit în jurul gleznei. Șireturile elastice și scaiul se strâng repede, deci pantoful se pune fără nod.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'imitație de piele și material textil.'), ('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc, rezistentă la abraziune.'))
  + '<p>Numerele 24-35 sunt pentru copii de 2-11 ani, de obicei.</p>',
  [('model', 'Geox CIBERDRON Spiderman sneakers pentru copii albastri J66LBJ.01454'), ('Marvel', 'inspirat de universul Marvel'),
   ('lumini', 'Luminile încorporate în talpă adaugă dinamism și vizibilitate'), ('membrană', 'O membrană microporoasă specială în talpă protejează interiorul pantofului de apă'),
   ('Respira', 'Tehnologia GEOX Respira™'), ('profil', 'Profilul înalt al părții superioare cu guler ușor întărit'),
   ('închidere', 'Șireturi elastice și închidere cu scai facilitează încălțarea rapidă'), ('material', 'Partea superioară confecționată din imitație de piele și material textil'),
   ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpă plată din cauciuc asigură o aderență bună la sol și este rezistentă la abraziune')],
  {'Model': 'Geox CIBERDRON Spiderman', 'Material': 'imitație de piele și textil, interior textil și sintetic, talpă din cauciuc', 'Caracteristici': 'lumini în talpă, membrană în talpă, șireturi elastice și scai', 'Cod produs': 'J66LBJ.01454'})

w(10572,
  f'<p>{TH} KG0KG09265 este o {A("/categorie/bluze-tricouri-hanorace/", "cămașă din denim pentru fete")}, albastră, cu mânecă lungă, din denim cu 1% elastan, în stil casual. Se închide cu capse, iar la piept are un buzunar cu fermoar.</p>'
  '<p>Fasonul e oversize, cu linia umerilor lăsată, deci cămașa stă larg și se poate purta și deschisă, peste un tricou. Manșetele se încheie cu nasturi.</p>'
  '<p>Mai sunt câteva detalii:</p>'
  + L(('Închidere', 'capse.'), ('Buzunar', 'la piept, cu fermoar.'), ('Material', '99% bumbac, 1% elastan.'))
  + '<p>Mărimile 128-176 sunt pentru copii de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Cămașă din denim pentru copii KG0KG09265'), ('denim', 'confecționat din denim'), ('mânecă', 'Maneca: lung'), ('casual', 'Ocazie: casual'),
   ('elastan', '99% Bumbac, 1% Elastan'), ('capse', 'Incheiere cu cleme'), ('buzunar', 'Buzunar la piept cu fermoar'), ('fason', 'Fason oversize'),
   ('umeri', 'Linia umerilor lasata'), ('manșete', 'Manșete cu nasturi'), ('culoare', 'albastru')],
  {'Model': 'Tommy Hilfiger KG0KG09265', 'Material': '99% bumbac, 1% elastan (denim)', 'Caracteristici': 'oversize, capse, buzunar cu fermoar', 'Cod produs': 'KG0KG09265'},
  notes=['„Se poate purta și deschisă, peste un tricou” e dedus din croiala oversize și închiderea cu capse.'])

w(10576,
  f'<p>Cardiganul {TH} KG0KG09503 este o {A("/categorie/bluze-tricouri-hanorace/", "bluză cardigan pentru fete")}, albă, uni, din bumbac 100% tricotat elastic, subțire, cu nasturi și decolteu rotund. E ușor, pentru sezoanele de tranziție și zilele mai reci.</p>'
  '<p>Croiala e relaxată, cu mâneca lungă și umerii coborâți, deci stă lejer și se poartă peste o rochie sau un tricou fără să strângă.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Închidere', 'nasturi.'), ('Material', '100% bumbac, tricot subțire.'), ('Decolteu', 'rotund.'))
  + '<p>Mărimile 116-176 sunt pentru copii de aproximativ 6-16 ani.</p>',
  [('model', 'Tommy Hilfiger Cardigan pentru copii din bumbac alb KG0KG09503'), ('uni', 'Modelul uni'), ('bumbac', 'Confecționat 100% din bumbac'),
   ('elastic', 'Materialul tricotat elastic'), ('subțire', 'Materialul subțire face ca puloverul să fie ușor și ideal pentru sezoanele de tranziție'),
   ('nasturi', 'Închiderea practică cu nasturi'), ('decolteu', 'Decolteul rotund clasic'), ('reci', 'zilele mai reci'), ('croială', 'Croiala relaxată'),
   ('mânecă', 'Mâneca lungă cu linia umerilor coborâtă')],
  {'Model': 'Tommy Hilfiger KG0KG09503', 'Material': '100% bumbac', 'Caracteristici': 'cardigan subțire, nasturi, croială relaxată', 'Cod produs': 'KG0KG09503'})

w(10578,
  f'<p>{A("/brand/reima/", "Reima")} Rantaan 5400067C sunt {A("/categorie/unisex-incaltaminte-sandale/", "sandale sport unisex")}, roz, ușoare, cu partea de sus din material textil, pentru jocurile și activitățile de vară în aer liber. Construcția sandalei susține postura naturală a piciorului.</p>'
  '<p>Calapodul e pentru o lățime standard a piciorului, dar cu spațiu suplimentar la degete. Branțurile detașabile Happy Fit ajută la alegerea mărimii, iar velcro-ul se ajustează repede.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Interior', 'căptușit cu material textil.'), ('Închidere', 'velcro.'))
  + '<p>Numerele 22-40 acoperă copiii de la aproximativ 1 an în sus.</p>',
  [('model', 'Reima Sandale sport pentru copii Rantaan roz 5400067C'), ('sport', 'Sandale sport pentru copii'), ('ușor', 'încălțăminte ușoară'),
   ('textil', 'Partea superioară din material textil'), ('vară', 'jocurile și activitățile de vară'), ('postură', 'Construcția sandalei susține postura naturală'),
   ('lățime', 'Lățime standard a piciorului cu spațiu suplimentar în zona degetelor'), ('Happy Fit', 'Branțuri detașabile Happy Fit care facilitează ajustarea precisă a mărimii'),
   ('velcro', 'Închidere cu velcro care permite o ajustare rapidă'), ('talpă', 'Talpă flexibilă din cauciuc'), ('interior', 'Interior căptușit cu material textil')],
  {'Model': 'Reima Rantaan', 'Material': 'textil, interior textil, talpă din cauciuc', 'Caracteristici': 'sandale sport, velcro, Happy Fit, spațiu la degete', 'Cod produs': '5400067C'})

w(10581,
  f'<p>Blugii {TH} BAGGY KB0KB10417 sunt {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "blugi largi pentru băieți")}, albaștri, cu fason baggy în stilul anilor 90, din denim cu bumbac și lyocell, decorați cu broderie cu steagul Tommy Hilfiger și abraziuni.</p>'
  '<p>Fasonul larg lasă loc de mișcare, iar talia e normală și stă stabil pe șolduri. Se închid cu fermoar și nasture.</p>'
  '<p>Pe scurt, despre blugi:</p>'
  + L(('Buzunare', 'cinci.'), ('Material', '61% bumbac, 39% lyocell.'), ('Detalii', 'broderie cu steag și abraziuni.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, de regulă.</p>',
  [('model', 'Tommy Hilfiger Blugi pentru copii BAGGY albaștri KB0KB10417'), ('baggy', 'Fason baggy'), ('anii 90', "stilul anilor '90"), ('material', '61% Bumbac, 39% Lyocell'),
   ('broderie', 'Broderie cu steagul Tommy Hilfiger și abraziuni'), ('talie', 'Talie normală – permite o așezare confortabilă pe șolduri'),
   ('închidere', 'Sistem de închidere cu fermoar și nasture'), ('buzunare', 'Cinci buzunare practice')],
  {'Model': 'Tommy Hilfiger BAGGY', 'Material': '61% bumbac, 39% lyocell', 'Caracteristici': 'baggy, talie normală, cinci buzunare, broderie', 'Cod produs': 'KB0KB10417'})
