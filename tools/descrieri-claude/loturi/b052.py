import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(11112,
  f'<p>Cizmele de iarnă {A("/brand/reima/", "Reima")} Talviuni 5400165A sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "cizme de iarnă pentru bebeluși")}, bleumarin, ușor izolate, din material textil și sintetic, impermeabile. Țin de cald chiar și la -20 de grade, deci sunt pentru zăpadă și ger.</p>'
  '<p>Velcro-ul le face ușor de încălțat și de scos, iar gamba ridicată ține zăpada departe de picior. Elementele reflectorizante îl fac pe copil vizibil după lăsarea serii.</p>'
  '<p>Pe scurt, din ce sunt făcute:</p>'
  + L(('Partea de sus', 'material sintetic și textil.'), ('Interior', 'material textil.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 20-28 sunt pentru copii de cam 1-5 ani.</p>',
  [('model', 'Reima Cizme de iarnă pentru copii Talviuni culoarea bleumarin, 5400165A'), ('izolare', 'Izolare usoara'), ('material', 'combinația materialului textil cu cel sintetic'),
   ('impermeabil', 'Model impermeabil'), ('-20', 'Asigura confortul termic chiar si la -20 grade'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('gambă', 'Gamba ridicata'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('interior', 'Interiorul: Material textil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Reima Talviuni', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'ușor izolate, impermeabile, până la -20°C, velcro, reflectorizante', 'Cod produs': '5400165A'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(11141,
  f'<p>{A("/brand/colmar/", "Colmar")} POLISHED 3430.2ZO este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de puf pentru băieți")}, bleumarin, matlasată, din nailon neted, umplută cu puf de rață și pene (90/10), pentru frigul de iarnă. Gulerul ridicat apără gâtul.</p>'
  '<p>Croiala e simplă, dreaptă, deci încape un pulover gros dedesubt. Nu are glugă, așa că merge purtată cu o căciulă și un fular în zilele cu vânt.</p>'
  '<p>Pe scurt, despre geacă:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', '100% nailon, căptușeală poliester.'))
  + '<p>Mărimile 154-172 sunt pentru adolescenți de 12-15 ani, aproximativ.</p>',
  [('model', 'Colmar Geacă de puf pentru copii POLISHED culoarea bleumarin, 3430.2ZO'), ('matlasat', 'Matlasare'), ('nailon', '100% Nailon'), ('puf', '90% Puf de rata, 10% Pene de rață'),
   ('frig', 'izolare impotriva frigului'), ('guler', 'Guler ridicat'), ('croială', 'Tăiere simplă, fără blocare'), ('fără glugă', 'Gluga: fara gluga'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'), ('căptușeală', 'Captuseala: 100% Poliester')],
  {'Model': 'Colmar POLISHED', 'Material': '100% nailon; umplutură 90% puf, 10% pene', 'Caracteristici': 'puf, matlasată, guler ridicat, fără glugă', 'Cod produs': '3430.2ZO'})

w(11143,
  f'<p>{A("/brand/mini-rodini/", "Mini Rodini")} E.T. 25810100 este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă bomber pentru bebeluși")}, neagră, subțire, din nailon reciclat ornamentat, ușor izolată pe căptușeală, pentru sezonul de tranziție. Nu are glugă.</p>'
  '<p>Croiala e simplă, dreaptă, deci încape un hanorac dedesubt, iar mânecile se termină cu manșetă, care strânge la încheieturi, ca la orice bomber.</p>'
  '<p>Pentru purtat zilnic, are:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale, cu capse.'), ('Material', '100% nailon reciclat.'))
  + '<p>Mărimile 80-86 până la 140-146 sunt pentru copii de 1-11 ani, de obicei.</p>',
  [('model', 'Mini Rodini Geacă bomber pentru copii E.T. culoarea negru, 25810100'), ('subțire', 'Model subțire'), ('material', '100% Nailon reciclat'), ('ornamentat', 'Material ornamentat'),
   ('izolat', 'Model usor izolat pe captuseala'), ('tranziție', 'Izolare: tranzitional'), ('fără glugă', 'Gluga: fara gluga'), ('croială', 'Tăiere simplă, fără blocare'),
   ('manșetă', 'Finisaj din manseta'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'), ('bomber', 'Fit: bomber')],
  {'Model': 'Mini Rodini E.T.', 'Material': '100% nailon reciclat', 'Caracteristici': 'bomber, ușor izolat, fermoar', 'Cod produs': '25810100'})

w(11144,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} KR6530 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de blugi unisex")}, albastră, din denim rezistent de bumbac 100%, cu efect prespălat și logo discret. Fără căptușeală, e ușoară, pentru sezoanele de tranziție.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar banda elastică de la bază și manșete strânge geaca pe corp și ține mânecile la locul lor.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, de obicei.</p>',
  [('model', 'adidas Originals Geacă de blugi pentru copii albastră KR6530'), ('denim', 'Denim rezistent'), ('prespălat', 'Efect prespălat'), ('logo', 'Logo subtil adidas Originals'),
   ('necăptușit', 'Fără căptușeală , favorizează lejeritatea și respirabilitatea, fiind potrivită pentru sezoanele de tranziție'), ('croială', 'Croială regulară'),
   ('lungime', 'Lungime până la șolduri'), ('bază', 'Bandă elastică la bază'), ('manșete', 'Manșete cu bandă elastică , ajută la menținerea mânecilor la locul lor'),
   ('fermoar', 'Închidere cu fermoar'), ('buzunare', 'Buzunare laterale tip slip-on'), ('material', '100% Bumbac')],
  {'Model': 'adidas Originals KR6530', 'Material': '100% bumbac (denim)', 'Caracteristici': 'prespălată, necăptușită, fermoar, bandă elastică', 'Cod produs': 'KR6530'})

w(11147,
  f'<p>{GEOX} BIGLIA B044DD sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} bleumarin, ușori, din piele naturală și piele întoarsă, cu interior din piele, pentru purtat zilnic. Branțul din piele previne frecarea și mirosul neplăcut.</p>'
  '<p>Velcro-ul se închide repede și se strânge după picior. Branțul Light Flexy lasă piciorul să se miște, iar talpa e moale și preia șocurile.</p>'
  '<p>Pe scurt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Interior', 'piele naturală.'), ('Talpă', 'material sintetic.'))
  + '<p>Numerele 18-26 sunt pentru cei mici de 1-4 ani, în general.</p>',
  [('model', 'Geox Încălțăminte din piele pentru copii BIGLIA culoarea bleumarin, B044DD.08522'), ('material', 'combinația pielii naturale cu pielea întoarsă'), ('ușor', 'Model ușor'),
   ('zilnic', 'purtarea zilnică'), ('interior', 'Interiorul: Piele naturala'), ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('Light Flexy', 'Light Flexy Sistem de brant pentru libertatea de miscare'),
   ('șocuri', 'Tehnologie moale pentru amortizare perfecta a socurilor'), RESPIRA, ('talpă', 'Talpa: Material sintetic'.split(': ')[1])],
  {'Model': 'Geox BIGLIA', 'Material': 'piele naturală și piele întoarsă, interior din piele', 'Caracteristici': 'velcro, Light Flexy, Geox Respira', 'Cod produs': 'B044DD.08522'})

w(11148,
  f'<p>{TH} KB0KB10501 este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")} alb, cu imprimeu în dungi, din tricot subțire de bumbac 100%, fără glugă și fără închidere. Decolteul e în V, cu guler și nervuri, pentru un aspect mai îngrijit.</p>'
  '<p>Croiala e lejeră, cu umerii coborâți pe mânecă, iar materialul elastic nu încurcă la joacă. Manșetele cu nervuri strâng la încheieturi.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', '100% bumbac, subțire.'), ('Decolteu', 'în V, cu guler.'), ('Model', 'dungi.'))
  + '<p>Mărimile 98-122 sunt pentru copii de 3-7 ani, cu aproximație.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii, din bumbac alb KB0KB10501'), ('dungi', 'Imprimeul în dungi'), ('bumbac', 'Tricotul moale din bumbac (100% bumbac)'),
   ('subțire', 'Materialul subțire'), ('fără glugă', 'Modelul fără glugă și fără închidere'), ('decolteu', 'Decolteul în V cu guler și cu nervuri'), ('croială', 'Croiala lejeră'),
   ('umeri', 'Mânecile cu linia umerilor coborâtă'), ('elastic', 'Materialul elastic'), ('manșete', 'Manșetele cu nervuri')],
  {'Model': 'Tommy Hilfiger KB0KB10501', 'Material': '100% bumbac', 'Caracteristici': 'decolteu în V cu guler, dungi, croială lejeră', 'Cod produs': 'KB0KB10501'})

w(11150,
  f'<p>Geaca {TH} KS0KS00751 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, bleumarin, de tip windbreaker, care oprește rafalele de vânt, fără izolație termică. E un strat exterior ușor pentru zilele mai blânde.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar manșetele cu bordură elastică strâng mânecile. Nu are glugă, iar căptușeala e doar parțială.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'capse.'), ('Buzunare', 'oblice, în față.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă de tranziție pentru copii bleumarin KS0KS00751'), ('windbreaker', 'Construcție windbreaker – asigură protecție împotriva rafalelor de vânt'),
   ('neizolat', 'Fără izolație termică – model ideal pentru zilele mai blânde'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'),
   ('manșete', 'Manșete cu bordură elastică'), ('fără glugă', 'Fără glugă'), ('căptușeală', 'Căptușeală parțială'), ('capse', 'Închidere cu capse'),
   ('buzunare', 'Buzunare oblice frontale'), ('material', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KS0KS00751', 'Material': '100% poliester', 'Caracteristici': 'windbreaker, neizolată, capse, fără glugă', 'Cod produs': 'KS0KS00751'})

w(11153,
  f'<p>{A("/brand/primigi/", "Primigi")} PBZGT 23529 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "încălțăminte de iarnă pentru bebeluși")}, maro, înaltă, din piele întoarsă, cu interior izolat termic și membrana GORE-TEX®, care blochează apa și vântul. Sunt pentru aventurile de iarnă și zilele reci.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, iar vârful rotund, întărit, apără degetele. Călcâiul întărit ține piciorul în poziție.</p>'
  '<p>Pe scurt:</p>'
  + L(('Shock Absorber', 'limitează transferul șocurilor la mers.'), ('Interior', 'material textil, izolat.'), ('Partea de sus', 'piele întoarsă.'))
  + '<p>Numerele 19-24 sunt pentru cei mici de 1-3 ani, de regulă.</p>',
  [('model', 'Primigi Încălțăminte pentru copii din piele întoarsă maro PBZGT 23529'), ('înalt', 'încălțăminte înaltă din piele întoarsă'),
   ('GORE-TEX', 'Membrana GORE-TEX® contribuie la menținerea uscăciunii picioarelor, blocând apa și vântul'), ('izolat', 'Interior izolat termic din material textil'),
   ('iarnă', 'aventurile de iarnă'), ('arici', 'Închidere cu arici permite încălțarea și descălțarea rapidă'), ('vârf', 'Vârf rotund întărit sprijină protecția degetelor'),
   ('călcâi', 'Călcâi întărit'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă'), ('șocuri', 'limitând transferul șocurilor la mers'),
   ('piele întoarsă', 'Partea superioară din piele întoarsă')],
  {'Model': 'Primigi PBZGT 23529', 'Material': 'piele întoarsă, interior textil izolat', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber', 'Cod produs': 'PBZGT 23529'},
  notes=['Sunt ghete de iarnă, listate la Pantofi.'])

w(11155,
  f'<p>{TH} KB0KB10594 este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")} gri, tip crewneck, fără închidere, din tricot subțire și elastic de bumbac 100%, cu logo discret. Stilul e casual și streetwear, iar materialul subțire îl face bun pentru zilele mai calde.</p>'
  '<p>Croiala e lejeră, relaxed fit, cu umerii coborâți pe mânecă, deci stă larg. Manșetele și tivul cu nervuri strâng ușor și țin hanoracul în formă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'rotund.'), ('Închidere', 'nu are, se îmbracă peste cap.'))
  + '<p>Mărimile 128-176 se potrivesc copiilor de 8-16 ani, în mare.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac gri KB0KB10594'), ('crewneck', 'Hanoracul fără închidere tip crewneck'), ('subțire', 'Tricotajul subțire asigură confort în zilele mai calde'),
   ('elastic', 'Tricotajul elastic'), ('bumbac', 'Confecționat în 100% din bumbac'), ('logo', 'un logo subtil'), ('casual', 'Stilul casual și streetwear'),
   ('croială', 'Croiala lejeră tip relaxed fit'), ('umeri', 'Mâneci cu linia umerilor coborâtă'), ('nervuri', 'Manșete și tiv cu nervuri'), ('decolteu', 'Decolteu rotund')],
  {'Model': 'Tommy Hilfiger KB0KB10594', 'Material': '100% bumbac', 'Caracteristici': 'crewneck, relaxed fit, tricot subțire', 'Cod produs': 'KB0KB10594'})

w(11162,
  f'<p>Pantofii {A("/brand/biomecanics/", "Biomecanics")} 261103 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} gri, ușori, din piele întoarsă moale, cu ornamente cu sclipici și ecusoane. Stilul e casual, pentru plimbări și joacă afară, în zilele obișnuite.</p>'
  '<p>Aricii permit încălțatul rapid și ajustarea pe picior. Talpa e subțire, deci piciorul stă natural, iar vârful întărit apără degetele la joacă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Branț', 'textil, detașabil.'), ('Călcâi', 'ușor întărit.'), ('Talpă', 'din cauciuc, flexibilă.'), ('Interior', 'material textil.'))
  + '<p>Numerele 18-25 sunt pentru copii de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele întoarsă gri 261103'), ('ușor', 'încălțăminte ușoară pentru copii'), ('piele întoarsă', 'Partea superioară din piele întoarsă'),
   ('sclipici', 'Ornamentele sub formă de sclipici și ecusoane'), ('casual', 'Stilul casual'), ('activități', 'de la plimbări la joacă în aer liber'),
   ('arici', 'Închiderea cu arici permite încălțarea rapidă și ajustarea'), ('subțire', 'Grosimea redusă a tălpii'), ('vârf', 'Vârful întărit susține protecția degetelor'),
   ('branț', 'Branțul textil detașabil'), ('călcâi', 'Călcâiul ușor întărit'), ('talpă', 'Talpă din cauciuc favorizează flexibilitatea'), ('interior', 'Interiorul din material textil')],
  {'Model': 'Biomecanics 261103', 'Material': 'piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, branț detașabil, sclipici', 'Cod produs': '261103'})
