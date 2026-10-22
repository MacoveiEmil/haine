import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9926,
  f'<p>{GEOX} FADINLIGHT Hello Kitty J66M4D sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil scurt și motiv Hello Kitty, pentru ținutele de zi cu zi. Partea de sus e din material textil și sintetic, iar tehnologia Geox Respira™ ține piciorul uscat.</p>'
  '<p>Aricii îi lasă pe copii să se încalțe singuri, iar branțurile textile se scot, deci se curăță ușor și pot fi folosite la măsurat piciorul.</p>'
  '<p>Sub picior și în jurul lui:</p>'
  + L(('Talpă', 'groasă, din cauciuc.'), ('Călcâi', 'întărit.'), ('Interior', 'moale, din material sintetic și textil.'))
  + '<p>Numerele 24-35 sunt, în general, pentru copii de 2-11 ani.</p>',
  [('model', 'Geox FADINLIGHT Hello Kitty sneakers pentru copii roz J66M4D.000BC'), ('profil', 'încălțăminte pentru copii cu profil scurt'), ('Hello Kitty', 'Motivul adorabil Hello Kitty'),
   ('zilnic', 'ținutele zilnice'), ('material', 'Partea superioară din material textil și sintetic'), ('Respira', 'Tehnologia GEOX Respira™ favorizează termoreglarea naturală a piciorului, menținându-l uscat'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea independentă'), ('branțuri', 'Branțuri detașabile din material textil'),
   ('talpă', 'Talpă groasă din cauciuc'), ('călcâi', 'Călcâiul întărit'), ('interior', 'Interiorul moale , din material sintetic și textil')],
  {'Model': 'Geox FADINLIGHT Hello Kitty', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'arici, branțuri detașabile, Geox Respira™', 'Cod produs': 'J66M4D.000BC'})

w(9929,
  f'<p>{A("/brand/primigi/", "Primigi")} PNEGT 88798 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de zăpadă unisex")}, negre, izolate, din material textil și piele întoarsă, cu interior din lână. Membrana GORE-TEX® e foarte subțire, impermeabilă și rezistentă la vânt, deci picioarele stau uscate și la cald pe zăpadă.</p>'
  '<p>Gura cizmei se strânge cu șnur cu opritor, ca zăpada să nu intre pe sus, iar cutia lată a degetelor lasă loc și unui picior mai lat.</p>'
  '<p>Talpa și branțul:</p>'
  + L(('Talpă', 'exterioară, din cauciuc, cu absorbția șocului.'), ('Branț', 'detașabil, cu contur.'), ('Partea de sus', 'rigidizată.'))
  + '<p>Numerele 31-35 sunt pentru copii de cam 6-11 ani.</p>',
  [('model', 'Primigi Cizme de iarna copii culoarea negru, PNEGT 88798'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinatia materialului textil cu pielea intoarsa'), ('lână', 'Un model cu interior din lână'),
   ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant'),
   ('șnur', 'Reglarea circumferinței superioare cu șnururi cu opritoare'), ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('șoc', 'Absorbtia socului'), ('branț', 'Brant detasabil, cu contur'),
   ('rigidizat', 'Partea superioară rigidizată')],
  {'Model': 'Primigi PNEGT 88798', 'Material': 'textil și piele întoarsă, interior textil și lână, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, izolate, șnur cu opritor, branț detașabil', 'Cod produs': 'PNEGT 88798'})

w(9931,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IG0IG02987 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, gri, izolată cu umplutură sintetică și căptușită, din material neted, pentru temperaturile mai reci. Conține fibre reciclate.</p>'
  '<p>Mânecile se termină cu bandă elastică și au în plus o ajustare cu velcro, deci se strâng pe încheietură, ca frigul și umezeala să nu intre.</p>'
  '<p>Geaca mai are:</p>'
  + L(('Glugă', 'da.'), ('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale, cu capse.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-170 sunt, de obicei, pentru copii de 8-15 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă copii culoarea gri, IG0IG02987'), ('matlasat', 'Model matlasat cu izolație sintetică'), ('căptușeală', 'Model izolat cu căptușeala'),
   ('neted', 'Model izolat confecționat din material neted'), ('reci', 'temperaturi mai reci'), ('reciclat', 'materiale realizate din fibre reciclate'),
   ('velcro', 'o ajustare suplimentară cu velcro'), ('glugă', 'Gluga: cu gluga'), ('fermoar', 'Încheiere cu fermoar'),
   ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'), ('material', 'Materialul de baza: 100% Poliester')],
  {'Model': 'Calvin Klein Jeans IG0IG02987', 'Material': '100% poliester', 'Caracteristici': 'matlasată, izolată, glugă, manșete elastice cu velcro', 'Cod produs': 'IG0IG02987'})

w(9935,
  f'<p>{GEOX} ECLYPER B555LA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} albi, cu profil scurt, cu exterior din imitație de piele, care se îngrijește ușor. Branțul detașabil are un imprimeu după care se verifică mărimea, deci se vede ușor când piciorul a crescut.</p>'
  '<p>Aricii îl lasă pe copil să se încalțe și să se descalțe repede, iar gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Înăuntru și dedesubt:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 20-27 sunt pentru cei mici de pe la 1 până pe la 4 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi B555LA.000BC'), ('profil', 'Profilul scurt al încălțămintei'), ('exterior', 'Exterior din imitație de piele'),
   ('îngrijire', 'facilitează îngrijirea acestora'), ('branț', 'Branț detașabil cu imprimeu pentru verificarea mărimii'),
   ('arici', 'Închidere practică cu arici , permite încălțarea și descălțarea rapidă'), ('guler', 'Gulerul superior ușor întărit'), ('călcâi', 'Călcâi întărit'),
   ('interior', 'Interior din material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, branț cu imprimeu de mărime', 'Cod produs': 'B555LA.000BC'})

w(9937,
  f'<p>{GEOX} ECLYPER J65LRF sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, ușori, cu profil scurt, din material textil și piele ecologică, pentru purtat în fiecare zi. Talpa are sistemul Geox Respira, cu trei straturi și perforări.</p>'
  '<p>Șireturile elastice cu cârlig se strâng o dată pe picior, iar apoi pantoful se pune și se scoate fără legat, ușor pentru un copil mic.</p>'
  '<p>Restul e simplu:</p>'
  + L(('Branț', 'textil, se ține ușor curat.'), ('Interior', 'material textil.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 24-27 sunt, cu aproximație, pentru 2-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ECLYPER culoarea alb, J65LRF.000BC'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'purtarea zilnică'), RESPIRA,
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'), ('interior', 'Interiorul: Material textil'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox ECLYPER', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J65LRF.000BC'})

w(9948,
  f'<p>Blugii {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KB0KB10467 sunt {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "blugi straight pentru băieți")}, albaștri, cu efect prespălat, din denim neelastic de bumbac și lyocell. Denimul își păstrează forma, deci blugii rezistă la purtat des.</p>'
  '<p>Croiala straight stă lejer pe picior, iar talia e normală. Materialul nu are elastan, deci blugii nu se mulează pe corp.</p>'
  '<p>Pe scurt, despre blugi:</p>'
  + L(('Închidere', 'fermoar și nasture.'), ('Material', '61% bumbac, 39% lyocell.'), ('Aspect', 'prespălat, ușor uzat.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Blugi straight pentru copii albaștri KB0KB10467'), ('prespălat', 'Efectul prespălat oferă blugilor un aspect la modă, ușor uzat'),
   ('neelastic', 'Denim neelastic își menține forma'), ('material', '61% Bumbac, 39% Lyocell'), ('croială', 'Croială straight favorizează o așezare lejeră pe silueta copilului'),
   ('talie', 'Talie normală'), ('închidere', 'Închidere cu fermoar și nasture')],
  {'Model': 'Tommy Hilfiger KB0KB10467', 'Material': '61% bumbac, 39% lyocell', 'Caracteristici': 'straight, neelastic, talie normală, prespălat', 'Cod produs': 'KB0KB10467'})

w(9949,
  f'<p>{BIO} 261154 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} albaștri, din piele naturală, cu profil scurt și motiv animal, făcuți în parteneriatul Biomecanics Podology. Sunt pentru activitățile și joaca de zi cu zi.</p>'
  '<p>Spațiul extins din zona degetelor le lasă să stea liber, iar scaiul se închide repede. Branțurile se scot, deci se curăță ușor și arată cât a crescut piciorul.</p>'
  '<p>Pentru mers, pantoful are:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Interior', 'material textil.'), ('Talpă', 'flexibilă, din cauciuc.'))
  + '<p>Mărimile 20-26 se potrivesc, de regulă, copiilor de 1-4 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele albastri 261154'), ('piele', 'Partea superioară din piele naturală'), ('profil', 'Profilul scurt al părții superioare'),
   ('motiv', 'Motivul animal atractiv'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership'), ('zilnic', 'activitățile și jocurile zilnice'),
   ('degete', 'Spațiul extins în zona degetelor permite o poziționare liberă a degetelor'), ('scai', 'Închiderea practică cu scai facilitează încălțarea și descălțarea rapidă'),
   ('branțuri', 'Branțurile detașabile'), ('călcâi', 'Călcâiul ușor întărit'), ('interior', 'Interiorul din material textil'), ('talpă', 'Talpa flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261154', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'scai, spațiu extins la degete, branțuri detașabile', 'Cod produs': '261154'})

w(9958,
  f'<p>Bocancii {GEOX} cu toc plat sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} negre, din piele naturală și piele ecologică, fără izolație, deci pentru zilele de tranziție, nu pentru ger. Talpa are sistemul Geox Respira, în trei straturi perforate.</p>'
  '<p>Se închid cu fermoar, deci se încalță repede, fără șireturi de legat. Vârful e o cutie rotundă, întărită.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'piele naturală și material sintetic.'), ('Interior', 'sintetic și textil.'), ('Talpă', 'din gumă, plată.'))
  + '<p>Numerele 36-41 sunt pentru adolescenți, cam de la 12 ani în sus.</p>',
  [('model', 'Geox Bocanci copii femei, culoarea negru, cu toc plat'), ('material', 'combinatia pielii naturale cu pielea ecologica'), ('neizolat', 'Izolare: neizolat'),
   RESPIRA, ('fermoar', 'Incheiere cu fermoar'), ('vârf', 'Cutie rotunda, intarita'), ('parte de sus', 'Material sintetic, Piele naturala'),
   ('interior', 'Material sintetic, Material textil'), ('talpă', 'Talpa din guma'), ('plat', 'Toc: plat')],
  {'Model': 'Geox (bocanci cu toc plat)', 'Material': 'piele naturală și piele ecologică, interior sintetic și textil, talpă din gumă', 'Caracteristici': 'neizolați, fermoar, Geox Respira', 'Cod produs': ''},
  notes=['Magazinul scrie „Bocanci copii femei”, mărimi 36-41; posibil model de adolescente/adulte.'])

w(9959,
  f'<p>Pantofii {BIO} 262120 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} albaștri, ușori, din piele naturală și material sintetic, cu finisaj mat și motiv animal, pentru primăvară, vară și toamnă. Talpa e plată, subțire și flexibilă, din cauciuc.</p>'
  '<p>Velcro-ul se închide repede și se strânge după picior. Branțul detașabil are un imprimeu după care se verifică mărimea, deci se vede când e nevoie de o pereche nouă.</p>'
  '<p>Pantoful mai are:</p>'
  + L(('Vârf', 'rotund, cauciucat, apără degetele.'), ('Interior', 'căptușit cu material textil moale.'), ('Stil', 'casual, pentru purtat zi de zi.'))
  + '<p>Numerele 19-25 sunt pentru copii de, aproximativ, 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii albaștri 262120'), ('ușor', 'încălțăminte ușoară'), ('material', 'Partea superioară dintr-o combinație de piele naturală și material sintetic'),
   ('mat', 'Finisajul mat cu un motiv animal'), ('sezon', 'aventurile de primăvară, vară și toamnă'), ('talpă', 'Talpa flexibilă din cauciuc'), ('plată', 'Încălțămintea are talpă plată'),
   ('subțire', 'Grosimea redusă a tălpii'), ('velcro', 'Închiderea practică cu velcro permite o încălțare rapidă'),
   ('branț', 'Branțul detașabil cu imprimeu permite verificarea ușoară a mărimii'), ('vârf', 'Vârful rotund, cauciucat protejează degetele copilului'),
   ('interior', 'Interiorul căptușit cu material textil moale'), ('casual', 'Stilul casual cu motiv animal se potrivește perfect cu ținutele de zi cu zi')],
  {'Model': 'Biomecanics 262120', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, branț cu imprimeu de mărime, vârf cauciucat', 'Cod produs': '262120'})

w(9960,
  f'<p>{A("/brand/mayoral/", "Mayoral")} 4469 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")}, verde, matlasată, cu umplutură sintetică groasă și căptușeală moale din polar, pentru activitățile de iarnă afară. Țesătura exterioară e rezistentă și ușor de întreținut.</p>'
  '<p>Croiala e regulară, cu loc pentru straturi în plus pe dedesubt, iar mânecile raglan lasă brațele să se miște liber. Manșetele cu nervuri strâng la încheieturi și opresc aerul rece.</p>'
  '<p>La închidere și la cap, geaca are:</p>'
  + L(('Glugă', 'integrată, contra vântului.'), ('Fermoar', 'pe toată lungimea.'), ('Buzunare', 'laterale, cu fermoar.'), ('Material', '89% poliamidă, 10% poliester, 1% elastan.'))
  + '<p>Mărimile 92-140 sunt pentru copii de în jur de 2-10 ani.</p>',
  [('model', 'Mayoral Jachetă pentru copii verde 4469'), ('matlasat', 'Geaca matlasată verde Mayoral'), ('umplutură', 'Umplutura sintetică groasă'),
   ('polar', 'Căptușeala moale din polar'), ('iarnă', 'activităților de iarnă în aer liber'), ('țesătură', 'Țesătura exterioară rezistentă'), ('întreținere', 'este ușor de întreținut'),
   ('croială', 'Croiala regulară permite libertatea de mișcare și posibilitatea de a purta straturi suplimentare de îmbrăcăminte pe dedesubt'),
   ('raglan', 'Croiala raglan a mânecilor'), ('manșete', 'Manșetele cu nervuri'), ('aer rece', 'limitează pătrunderea aerului rece'),
   ('glugă', 'Gluga integrată oferă protecție suplimentară capului împotriva vântului'), ('fermoar', 'fermoar pe toată lungimea'),
   ('buzunare', 'Buzunarele laterale cu fermoar'), ('material', '89% Poliamidă, 10% Poliester, 1% Elastan')],
  {'Model': 'Mayoral 4469', 'Material': '89% poliamidă, 10% poliester, 1% elastan; căptușeală polar', 'Caracteristici': 'matlasată, umplutură groasă, glugă integrată, mâneci raglan', 'Cod produs': '4469'})
