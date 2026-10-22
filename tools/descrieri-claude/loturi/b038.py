import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')

w(10217,
  f'<p>{A("/brand/primigi/", "Primigi")} PIM 24565 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete de trekking unisex")}, bleumarin, înalte, pentru hiking și trekking pe teren variat. Tehnologia STORM TECHNOLOGY reduce absorbția apei, iar talpa de cauciuc are bandă de rulare.</p>'
  '<p>Aricii se ajustează repede pe piciorul copilului, iar carâmbul înalt din material sintetic, cu călcâi și guler întărite, ține glezna pe traseu.</p>'
  '<p>Înăuntru și în talpă:</p>'
  + L(('Branțuri', 'detașabile, din piele naturală.'), ('Anti-Shock', 'sistem în talpă care reduce microșocurile.'), ('Interior', 'piele naturală și material textil.'))
  + '<p>Numerele 26-37 sunt pentru copii de pe la 3 ani în sus.</p>',
  [('model', 'Primigi Încălțăminte de trekking pentru copii bleumarin PIM 24565'), ('înalt', 'încălțăminte înaltă'), ('hiking', 'potrivit pentru hiking și trekking'),
   ('teren', 'terenurilor variate'), ('STORM', 'Tehnologia STORM TECHNOLOGY ajută la reducerea absorbției apei'), ('talpă', 'Talpă de cauciuc cu bandă de rulare'),
   ('arici', 'Închidere cu arici'), ('carâmb', 'Profil înalt al carâmbului , din material sintetic'), ('întărit', 'Călcâi întărit și guler ușor întărit'),
   ('branțuri', 'Branțuri detașabile din piele naturală'), ('Anti-Shock', 'Sistemul Anti-Shock în talpă'), ('microșocuri', 'reducând microșocurile în timpul mersului'),
   ('interior', 'Piele naturală, Material textil')],
  {'Model': 'Primigi PIM 24565', 'Material': 'sintetic, interior din piele naturală și textil', 'Caracteristici': 'STORM TECHNOLOGY, arici, Anti-Shock, branțuri din piele', 'Cod produs': 'PIM 24565'})

w(10219,
  f'<p>Geaca din denim {A("/brand/levis/", "Levi&#39;s")} este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de blugi pentru băieți")}, albastră, din bumbac 100%, neizolată și necăptușită. E pentru zilele blânde de primăvară și toamnă, ca strat subțire peste un tricou sau un hanorac.</p>'.replace(' de primăvară și toamnă', '')
  + '<p>Tiparul e drept, deci geaca cade simplu pe corp și lasă loc unei bluze dedesubt. Nu are glugă.</p>'
  '<p>Ca orice geacă de blugi clasică, are:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'oblice, plus unul pe piept.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 140-176 sunt pentru copii de în jur de 10-16 ani.</p>',
  [('model', "Levi's Geacă din denim pentru copii"), ('denim', 'Model neizolat confectionat din denim'), ('material', '100% Bumbac'), ('necăptușit', 'Captuseala: necaptusit'),
   ('tipar', 'Tipar drept'), ('fără glugă', 'Gluga: fara gluga'), ('nasturi', 'Incheiere cu nasturi'), ('buzunare', 'Buzunare oblice'), ('buzunar piept', 'Buzunar pe piept'),
   ('culoare', 'albastru')],
  {'Model': "Levi's (geacă din denim)", 'Material': '100% bumbac', 'Caracteristici': 'neizolată, necăptușită, nasturi, tipar drept', 'Cod produs': ''},
  notes=['„Ca strat peste un tricou sau un hanorac” e dedus din faptul că e neizolată și necăptușită.'])

w(10223,
  f'<p>{BIO} 261164 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, din piele naturală, în stil casual, făcuți în parteneriatul Biomecanics Podology. Căptușeala textilă e moale, pentru zilele active ale celor mici.</p>'
  '<p>Vârful are spațiu sporit, deci degetele stau liber. Aricii se închid repede și îl lasă pe copil să se încalțe singur, iar gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Pantoful mai are:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Branț', 'textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-23 sunt pentru copii de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele roz 261164'), ('piele', 'Partea superioară din piele naturală'), ('casual', 'stilul casual'),
   ('parteneriat', 'Biomecanics Podology Partnership'), ('căptușeală', 'Căptușeală textilă moale'), ('vârf', 'Spațiu sporit în vârful pantofului permite poziționarea liberă a degetelor'),
   ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă de către copil'), ('guler', 'Gulerul ușor întărit'), ('călcâi', 'Călcâi ușor întărit'),
   ('branț', 'Branț respirabil'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Biomecanics 261164', 'Material': 'piele naturală și sintetic, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'arici, spațiu sporit la vârf', 'Cod produs': '261164'})

w(10229,
  f'<p>{GEOX} GISLI B461NE sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} maro, cu profil înalt și guler ușor întărit, din imitație de piele și material textil, ușor de întreținut. Interiorul are căptușeală textilă cu imitație de lână, care ține de cald.</p>'
  '<p>Șireturile elastice și aricii se strâng repede pe picior, deci copilul se încalță singur. Tehnologia Geox Respira™ scoate umezeala spre exterior.</p>'
  '<p>Sub și în jurul piciorului:</p>'
  + L(('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc, rezistentă la abraziune.'), ('Partea de sus', 'imitație de piele și textil.'))
  + '<p>Numerele 24-27 sunt pentru copii de, de obicei, 2-4 ani.</p>'.replace('de, de obicei, 2-4 ani', 'de 2-4 ani, de obicei'),
  [('model', 'Geox GISLI sneakers pentru copii maro B461NE.0AFME'), ('profil', 'Profil înalt al încălțămintei cu gulerul ușor întărit'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('întreținere', 'ușor de întreținut'),
   ('lână', 'Interior căptușit cu material textil cu imitație de lână, ce contribuie la menținerea căldurii'),
   ('închidere', 'Șireturi elastice și închidere cu arici'), ('Respira', 'Tehnologia GEOX Respira™'), ('umezeală', 'eliminând umezeala către exterior'),
   ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpă plată din cauciuc asigură o bună aderență la sol și este rezistentă la abraziune')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, căptușeală cu imitație de lână, talpă din cauciuc', 'Caracteristici': 'profil înalt, șireturi elastice și arici, Geox Respira™', 'Cod produs': 'B461NE.0AFME'})

w(10230,
  f'<p>{A("/brand/mini-rodini/", "Mini Rodini")} Ritzratz 26220110 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de tranziție unisex")}, neagră, neizolată, din țesătură netedă de poliester, căptușită. E pentru zilele blânde, nu pentru frig.</p>'
  '<p>Croiala e lejeră, oversize, cu umerii coborâți pe mânecă, deci lasă loc unui hanorac dedesubt. Mânecile și tivul au bordură, care strânge la încheieturi și jos.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Închidere', 'fermoar.'), ('Glugă', 'nu are.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 80-86 până la 140-146 sunt pentru copii de pe la 1 până pe la 11 ani.</p>',
  [('model', 'Mini Rodini Geacă copii Ritzratz culoarea negru, 26220110'), ('neizolat', 'Model neizolat confecționat din tesatura neteda'), ('tranziție', 'Izolare: tranzitional'),
   ('căptușeală', 'Captuseala: cu captuseala'), ('croială', 'Tăiere lejeră, fără blocare'), ('oversize', 'Fit: oversize'), ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'),
   ('bordură', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('fără glugă', 'Gluga: fara gluga'),
   ('material', '100% Poliester')],
  {'Model': 'Mini Rodini Ritzratz', 'Material': '100% poliester', 'Caracteristici': 'neizolată, căptușită, oversize, fermoar', 'Cod produs': '26220110'})

w(10236,
  f'<p>{A("/brand/guess/", "Guess")} J6YL04 W2610 este o {A("/categorie/geci-jachete/", "geacă bomber reversibilă pentru fete")}, neagră, cu inscripție decorativă, fără izolație, deci un strat ușor pentru sezonul de tranziție. Se poartă pe oricare față, iar căptușeala e completă.</p>'
  '<p>Croiala e lejeră, cu mâneci raglan și lungimea până la șolduri. Baza și manșetele cu bandă elastică strâng jacheta pe corp, ca să nu se ridice la mișcare.</p>'
  '<p>Câteva detalii practice:</p>'
  + L(('Închidere', 'fermoar.'), ('Glugă', 'nu are.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 122-125 până la 167 sunt, în general, pentru 7-14 ani.</p>',
  [('model', 'Guess Jachetă reversibilă pentru copii neagră J6YL04 W2610'), ('bomber', 'Jacheta bomber neagră Guess'), ('inscripție', 'Inscripția decorativă'),
   ('neizolat', 'Model fără izolație, potrivit pentru sezonul de tranziție'), ('reversibil', 'Construcție reversibilă'), ('căptușeală', 'Căptușeală completă'),
   ('croială', 'Croială lejeră'), ('raglan', 'Croiala raglan a mânecilor'), ('lungime', 'Lungimea până la șolduri'), ('bază', 'Bază cu bandă elastică'),
   ('manșete', 'Manșete cu bandă elastică'), ('fermoar', 'Închidere practică cu fermoar'), ('fără glugă', 'Lipsa glugii'), ('material', '100% Poliester')],
  {'Model': 'Guess J6YL04 W2610', 'Material': '100% poliester', 'Caracteristici': 'bomber reversibil, neizolat, mâneci raglan, bază și manșete elastice', 'Cod produs': 'J6YL04 W2610'})

w(10248,
  f'<p>{A("/brand/didriksons/", "Didriksons")} ROXEN KIDS JACKET 505811 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, maro, matlasată, izolată cu umplutură din poliester reciclat, pentru temperaturile mai reci. Gulerul ridicat, gluga detașabilă și protecția pentru bărbie țin frigul departe.</p>'
  '<p>Croiala e simplă, dreaptă. Mânecile au găuri pentru degetul mare, care nu lasă mânecile să se ridice și apără mâinile, iar bordura de la mâneci și tiv strânge pe corp.</p>'
  '<p>Pentru zilele scurte de iarnă:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede pe întuneric.'), ('Fermoar', 'pe toată lungimea, cu clapă împotriva furtunii.'), ('Buzunare', 'două, laterale.'))
  + '<p>Mărimile 90-140 sunt pentru copii de în jur de 2-10 ani.</p>',
  [('model', 'Didriksons Geacă copii ROXEN KIDS JACKET culoarea maro, 505811'), ('matlasat', 'Model matlasat cu izolație sintetică'), ('reciclat', 'Umplutura: 100% Poliester reciclat'),
   ('reci', 'temperaturi mai reci'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('glugă', 'Gluga detasabila'),
   ('bărbie', 'Model echipat cu protecție pentru bărbie'), ('croială', 'Tăiere simplă, fără blocare'),
   ('deget', 'Găurile pentru degetul mare din partea de jos a mânecilor protejează mâinile și împiedică mânecile să se sufle'),
   ('bordură', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară împotriva furtunii'), ('buzunare', 'Două buzunare laterale')],
  {'Model': 'Didriksons ROXEN KIDS JACKET', 'Material': '100% poliester, căptușeală și umplutură din poliester reciclat', 'Caracteristici': 'matlasată, izolată, glugă detașabilă, găuri pentru deget, reflectorizante', 'Cod produs': '505811'})

w(10273,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IG0IG03020 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, neagră, izolată și căptușită, din nailon 100% cu material ornamentat. E pentru zilele reci, iar gluga apără capul de vânt.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri pe corp, deci încape un pulover dedesubt. Mânecile se termină cu manșetă, care strânge la încheieturi și ține căldura înăuntru.</p>'
  '<p>Se îmbracă repede și are loc pentru mâini:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'oblice.'), ('Material', '100% nailon.'))
  + '<p>Mărimile 128-170 sunt, de regulă, pentru 8-15 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă copii culoarea negru, IG0IG03020'), ('matlasat', 'Matlasat'), ('izolat', 'Model izolat cu captuseala'), ('material', '100% Nailon'),
   ('ornamentat', 'Material ornamentat'), ('glugă', 'Model cu gluga'), ('croială', 'Tăiere simplă, fără blocare'), ('manșetă', 'Finisaj din manseta'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare oblice')],
  {'Model': 'Calvin Klein Jeans IG0IG03020', 'Material': '100% nailon', 'Caracteristici': 'matlasată, izolată, glugă, manșete', 'Cod produs': 'IG0IG03020'})

w(10275,
  f'<p>{A("/brand/reima/", "Reima")} Tahti 5200048A este un {A("/categorie/bebe-imbracaminte-bluze-tricouri-hanorace/", "romper pentru bebeluși")}, bleumarin, din tricot neted de poliester reciclat, cu mânecă lungă. Se închide cu fermoar, deci se îmbracă și se dă jos ușor, fără să fie tras peste cap.</p>'
  '<p>Fasonul e drept, simplu, fără strângeri, deci cel mic se mișcă liber în el.</p>'
  '<p>Pe scurt, despre romper:</p>'
  + L(('Închidere', 'fermoar.'), ('Mâneci', 'lungi.'), ('Material', '100% poliester, reciclat.'))
  + '<p>Mărimile 74-98 sunt pentru cei mici de pe la 9 luni până pe la 3 ani.</p>',
  [('model', 'Reima bleumarin 5200048A'), ('romper', 'Rampers bebe din colectia Reima'), ('tricot', 'Model confectionat din tricot neted'), ('reciclat', 'fabricat din poliester reciclat'),
   ('mânecă', 'Maneca lunga'), ('fermoar', 'Incheiere cu fermoar'), ('fason', 'Fason drept'), ('material', '100% Poliester')],
  {'Model': 'Reima Tahti', 'Material': '100% poliester reciclat', 'Caracteristici': 'romper, fermoar, mânecă lungă', 'Cod produs': '5200048A'},
  notes=['E un romper (salopetă), listat la Bluze.'])

w(10277,
  f'<p>{GEOX} ECLYPER B665MB sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} albi, cu profil înalt, din imitație de piele și material textil. Membrana Geox Respira™ scoate umiditatea și protejează împotriva apei, iar culoarea albă merge la multe ținute.</p>'
  '<p>Șireturile elastice se strâng repede pe picior, iar profilul înalt cuprinde glezna, deci pantoful stă bine pe picior și nu iese când copilul aleargă.</p>'
  + '<p>Înăuntru și dedesubt:</p>'
  + L(('Branț', 'textil.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-23 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi B665MB.0BCQ6'), ('profil', 'Profil înalt al părții superioare'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('Respira', 'Tehnologia GEOX Respira™ cu membrană, care susține eliminarea umidității și protejează împotriva apei'), ('alb', 'Culoare albă universală'),
   ('șireturi', 'Șireturi elastice , care facilitează încălțarea rapidă'), ('branț', 'Branț respirabil din material textil'), ('interior', 'Interior căptușit cu material textil'),
   ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, șireturi elastice, Geox Respira™', 'Cod produs': 'B665MB.0BCQ6'})
