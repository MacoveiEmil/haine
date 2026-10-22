import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
REIMA = A('/brand/reima/', 'Reima')

w(10644,
  f'<p>Ghetele de iarnă {PRIMIGI} PHHGT 23950 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} maro, înalte, din piele întoarsă și material textil, cu membrana GORE-TEX®, care protejează de apă și vânt. Sunt pentru aventurile de iarnă și drumurile de zi cu zi în lunile reci.</p>'
  '<p>Aricii permit încălțatul fără ajutor, iar partea de sus se adaptează la forma piciorului. Călcâiul întărit ține piciorul în poziție.</p>'
  '<p>Talpa și tehnologiile:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Anti-Shock', 'sistem în talpă care preia microșocurile.'), ('Primigi × SIPeP', 'dezvoltată cu podologi.'))
  + '<p>Numerele 31-35 sunt pentru copii de, de regulă, 6-11 ani.</p>'.replace('de, de regulă, 6-11 ani', 'de 6-11 ani, de regulă'),
  [('model', 'Primigi Încălțăminte de iarnă pentru copii maro PHHGT 23950'), ('înalt', 'încălțăminte înaltă pentru copii'),
   ('material', 'Partea superioară din piele întoarsă și material textil'), ('GORE-TEX', 'Membrana GORE-TEX® contribuie la protecția împotriva apei și vântului'),
   ('iarnă', 'aventurilor de iarnă și al activităților cotidiene'), ('arici', 'Închidere cu arici facilitează încălțarea și descălțarea ușoară'),
   ('adaptare', 'adaptarea la forma piciorului'), ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpă plată din cauciuc'),
   ('Anti-Shock', 'Sistemul Anti-Shock în talpă ajută la absorbția microșocurilor'), ('SIPeP', 'Tehnologia Primigi × SIPeP , dezvoltată în colaborare cu podologi')],
  {'Model': 'Primigi PHHGT 23950', 'Material': 'piele întoarsă și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, arici, Anti-Shock', 'Cod produs': 'PHHGT 23950'})

w(10663,
  f'<p>{GEOX} ACTIVART ILLUMINUS Batman J66LYA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, cu motiv Batman și lumini încorporate, care îl fac pe copil vizibil la joacă. Tehnologia Geox Respira™ scoate umiditatea și ține picioarele uscate.</p>'
  '<p>Șireturile elastice și velcro-ul se strâng repede pe picior, deci pantoful se pune fără nod. Gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Ce mai are, de la vârf la călcâi:</p>'
  + L(('Talpă', 'din spumă, ușoară și flexibilă.'), ('Călcâi', 'întărit.'), ('Partea de sus', 'imitație de piele și material textil.'))
  + '<p>Numerele 24-31 se poartă cam între 2 și 7 ani.</p>',
  [('model', 'Geox ACTIVART ILLUMINUS Batman sneakers pentru copii negri J66LYA.014CE'), ('Batman', 'dedicat micilor fani Batman'),
   ('lumini', 'Luminile încorporate adaugă dinamism și vizibilitate în timpul jocului'), ('Respira', 'Tehnologia GEOX Respira™ contribuie la eliminarea umidității, menținând picioarele uscate'),
   ('închidere', 'Șireturile elastice și închiderea cu velcro facilitează încălțarea rapidă și ajustarea'), ('guler', 'Gulerul superior ușor întărit'),
   ('talpă', 'Talpa din spumă conferă lejeritate și flexibilitate'), ('călcâi', 'Călcâiul întărit'), ('material', 'Partea superioară din imitație de piele și material textil')],
  {'Model': 'Geox ACTIVART ILLUMINUS Batman', 'Material': 'imitație de piele și textil, talpă din spumă', 'Caracteristici': 'lumini încorporate, șireturi elastice și velcro, Geox Respira™', 'Cod produs': 'J66LYA.014CE'})

w(10666,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KS0KS00709 este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")}, bleumarin, fără glugă și fără fermoar, din tricot moale de bumbac 100%, cu aplicație cu logo Tommy Hilfiger. Se poartă casual, zi de zi.</p>'
  '<p>Croiala e regulară, iar materialul elastic nu încurcă la mișcare. Decolteul rotund are bordură elastică, iar benzile de la manșete și bază țin hanoracul în formă.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'rotund, cu bordură elastică.'), ('Căptușeală', 'nu are.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, în general.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac bleumarin KS0KS00709'), ('fără fermoar', 'model fără fermoar'), ('fără glugă', 'Lipsa glugii și a închiderii'),
   ('tricot', 'Tricot moale din bumbac'), ('bumbac', '100% Bumbac'), ('logo', 'Aplicație cu logo Tommy Hilfiger'), ('casual', 'ținute casual'), ('croială', 'Croială regulară'),
   ('elastic', 'Material elastic'), ('decolteu', 'Decolteu rotund cu bordură elastică'), ('benzi', 'Benzi elastice la manșete și bază'), ('necăptușit', 'Lipsa căptușelii')],
  {'Model': 'Tommy Hilfiger KS0KS00709', 'Material': '100% bumbac', 'Caracteristici': 'fără glugă și fermoar, croială regulară, benzi elastice', 'Cod produs': 'KS0KS00709'})

w(10673,
  f'<p>{REIMA} Wingon 5100052B sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni de schi unisex")}, bleumarin, uni, izolați și căptușiți, cu tehnologia ReimaTec, care apără de ploaie și vânt. Impermeabilitatea de 12000 mm îi face buni pentru zăpadă și pârtie.</p>'
  '<p>Croiala e simplă, dreaptă, iar talia reglabilă se strânge pe un copil mai slab, fără curea.</p>'
  '<p>Pentru zilele pe zăpadă:</p>'
  + L(('Buzunare', 'două, laterale, cu fermoar.'), ('Respirabilitate', '7000 g/m2/24h.'), ('Material', '100% poliester reciclat, certificat Bluesign®.'), ('Finisaj', 'BIONIC-FINISH® ECO, hidrofob.'))
  + '<p>Mărimile 92-164 sunt pentru copii de în jur de 2-14 ani.</p>',
  [('model', 'Reima Pantaloni de schi pentru copii Wingon culoarea bleumarin, 5100052B'), ('schi', 'Pantaloni de schi copii'), ('uni', 'Model: uni'), ('izolat', 'Model izolat cu captuseala'),
   ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'), ('impermeabil', 'Impermeabilitate: 12000 mm/m2/24h'), ('croială', 'Tăiere simplă, fără blocare'),
   ('talie', 'Talie reglabilă'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('respirabilitate', 'Respirabilitate: 7000 g/m2/24h'),
   ('reciclat', '100% Poliester reciclat'), ('Bluesign', 'Model certificat Bluesign® Standard'), ('BIONIC', 'BIONIC-FINISH® ECO - o alternativa ecologica la acoperirea traditionala, hidrofoba DWR')],
  {'Model': 'Reima Wingon', 'Material': '100% poliester reciclat; căptușeală poliester', 'Caracteristici': 'ReimaTec, 12000 mm, izolați, talie reglabilă, Bluesign®', 'Cod produs': '5100052B'})

w(10684,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} KD5801 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de blugi unisex")}, albastră, din denim rigid de bumbac 100%, care își păstrează forma. E neizolată și fără căptușeală, pentru zilele blânde de tranziție.</p>'
  '<p>Croiala e lejeră, oversize, deci încape un hanorac dedesubt. Mânecile și tivul au bordură, care strânge la încheieturi și jos, iar gulerul ridicat apără gâtul.</p>'
  '<p>Spre deosebire de o geacă de blugi clasică, aceasta are:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 104-128 sunt pentru copii de aproximativ 4-8 ani.</p>',
  [('model', 'adidas Originals Geacă de blugi pentru copii KD5801'), ('denim', 'Model neizolat confecționat dindenim'), ('rigid', 'Modelul este realizat dintr-un material rigid, care păstrează forma'),
   ('material', '100% Bumbac'), ('necăptușit', 'Model neizolat fara captuseala'), ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere lejeră, fără blocare'), ('oversize', 'Fit: oversize'),
   ('bordură', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('buzunare', 'Două buzunare laterale'), ('fără glugă', 'Gluga: fara gluga'), ('culoare', 'albastru')],
  {'Model': 'adidas Originals KD5801', 'Material': '100% bumbac (denim)', 'Caracteristici': 'oversize, neizolată, fermoar, guler ridicat', 'Cod produs': 'KD5801'})

w(10693,
  f'<p>Balerinii {GEOX} din piele sunt {A("/categorie/incaltaminte-pantofi/", "balerini pentru fete")} negri, din piele naturală, cu interior tot din piele, potriviți la ținute mai elegante sau la școală. Se închid cu o cataramă cu ac, deci se strâng după piciorul copilului.</p>'.replace(', potriviți la ținute mai elegante sau la școală', '')
  + '<p>Spatele călcâiului e rigidizat și ține piciorul în pantof, ca să nu iasă la mers, iar vârful e o cutie rotundă, întărită, care își păstrează forma.</p>'
  '<p>Pe scurt, din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'piele naturală.'), ('Interior', 'piele naturală.'), ('Talpă', 'din gumă.'))
  + '<p>Numerele 28-35 sunt pentru copii de 4-11 ani, cu aproximație.</p>',
  [('model', 'Geox Balerini din piele pentru copii culoarea negru'), ('piele', 'Model confectionat din piele naturala'), ('interior', 'Interiorul: Piele naturala'),
   ('cataramă', 'Incheiere cu catarama cu ac'), ('călcâi', 'Spatele calcaiului rigidizat'), ('vârf', 'Cutie rotunda, intarita'), ('talpă', 'Talpa din guma'),
   ('parte de sus', 'Gamba: Piele naturala')],
  {'Model': 'Geox (balerini din piele)', 'Material': 'piele naturală, interior din piele, talpă din gumă', 'Caracteristici': 'cataramă cu ac, călcâi rigidizat', 'Cod produs': ''})

w(10694,
  f'<p>Ghetele de iarnă {PRIMIGI} PIK 23701 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} maro, înalte, din imitație de piele și material sintetic, care țin frigul departe. Nu sunt impermeabile, deci sunt pentru zilele de iarnă uscate, nu pentru zăpadă udă.</p>'
  '<p>Fermoarul permite încălțatul și descălțatul rapid, practic pentru copii. Vârful rotund, rigidizat, și călcâiul întărit țin piciorul stabil.</p>'
  '<p>Talpa e partea cea mai solidă:</p>'
  + L(('Talpă', 'plată, din cauciuc, groasă.'), ('Shock Absorber', 'tehnologie în talpă care reduce șocurile.'), ('Interior', 'material textil.'))
  + '<p>Numerele 31-35 sunt pentru copii de 6-11 ani, de obicei.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii maro PIK 23701'), ('înalt', 'Partea superioară înaltă din imitație de piele și material sintetic'),
   ('frig', 'sporește protecția împotriva frigului'), ('neimpermeabil', 'Modelul nu este impermeabil , ce indică destinația sa pentru condiții de iarnă uscate'),
   ('fermoar', 'Închiderea cu fermoar facilitează încălțarea și descălțarea rapidă'), ('întărit', 'Vârful rotund și rigidizat și călcâiul întărit'),
   ('talpă', 'Talpă plată din cauciuc cu o grosime de 3,5 cm'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă contribuie la reducerea șocurilor'), ('interior', 'Material textil')],
  {'Model': 'Primigi PIK 23701', 'Material': 'imitație de piele și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'neimpermeabile, fermoar, Shock Absorber', 'Cod produs': 'PIK 23701'})

w(10706,
  f'<p>{REIMA} Terrie 5100053B sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni de schi unisex")}, roz, uni, izolați și căptușiți, cu tehnologia ReimaTec împotriva ploii și vântului și impermeabilitate de 12000 mm. Sunt pentru zăpadă, pârtie și joacă afară iarna.</p>'
  '<p>Talia e reglabilă și se strânge pe un copil mai slab, iar bretelele incluse țin pantalonii sus când copilul se rostogolește prin zăpadă. Croiala e simplă, dreaptă.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'două, laterale.'), ('Respirabilitate', '7000 g/m2/24h.'), ('Material', '100% poliester reciclat, certificat Bluesign®.'))
  + '<p>Mărimile 104-164 merg, în mare, la 4-14 ani.</p>',
  [('model', 'Reima Pantaloni de schi pentru copii Terrie culoarea roz, 5100053B'), ('schi', 'Pantaloni de schi copii'), ('uni', 'Model: uni'), ('izolat', 'Model izolat cu captuseala'),
   ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'), ('impermeabil', 'Impermeabilitate: 12000 mm/m2/24h'), ('talie', 'Talie reglabilă'), ('bretele', 'Bretele incluse'),
   ('croială', 'Tăiere simplă, fără blocare'), ('buzunare', 'Două buzunare laterale'), ('respirabilitate', 'Respirabilitate: 7000 g/m2/24h'),
   ('reciclat', '100% Poliester reciclat'), ('Bluesign', 'Model certificat Bluesign® Standard')],
  {'Model': 'Reima Terrie', 'Material': '100% poliester reciclat; căptușeală poliester', 'Caracteristici': 'ReimaTec, 12000 mm, izolați, talie reglabilă, bretele', 'Cod produs': '5100053B'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(10707,
  f'<p>{A("/brand/donsje/", "Donsje")} 3048501 este o {A("/categorie/geci-jachete/", "geacă bomber pentru fete")}, bej, din bumbac și poliester, cu finisaj neted și matlasat și detalii brodate, pentru sezonul de tranziție. Căptușeala e completă, din bumbac.</p>'
  '<p>Croiala e relaxată, cu mâneci raglan și lungimea până la șolduri, iar tivul și manșetele cu nervuri strâng bomberul pe corp. Gulerul ridicat apără gâtul.</p>'
  '<p>Câteva detalii practice:</p>'
  + L(('Închidere', 'capse pe toată lungimea.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '57% bumbac, 43% poliester.'))
  + '<p>Mărimile 98-140 sunt pentru copii de 3-10 ani, aproximativ.</p>',
  [('model', 'Donsje Geacă bomber pentru copii, cu bumbac bej 3048501'), ('material', '57% Bumbac, 43% Poliester'), ('finisaj', 'Combinația de finisaj neted și matlasat'),
   ('brodat', 'detalii brodate'), ('tranziție', 'sezonul de tranziție'), ('căptușeală', 'Căptușeala completă din bumbac'), ('croială', 'Croiala relaxată'), ('raglan', 'Mâneci raglan'),
   ('lungime', 'Lungimea până la șolduri'), ('nervuri', 'Tivul și manșetele cu nervuri'), ('guler', 'Gulerul ridicat'), ('capse', 'Închiderea cu capse pe toată lungimea'),
   ('buzunare', 'Buzunarele laterale tip slip-on')],
  {'Model': 'Donsje 3048501', 'Material': '57% bumbac, 43% poliester; căptușeală 100% bumbac', 'Caracteristici': 'bomber, căptușit, capse, mâneci raglan', 'Cod produs': '3048501'})

w(10723,
  f'<p>{A("/brand/colmar/", "Colmar")} LUSH 3440.5YM este o {A("/categorie/geci-jachete/", "geacă de puf pentru fete")}, roz, matlasată, izolată cu puf de rață și pene (90/10), cu impermeabilitate de 5000 mm. E pentru iarnă, inclusiv pe ninsoare.</p>'
  '<p>Croiala e simplă, dreaptă, iar elastanul din material o face să se miște cu copilul. Gulerul ridicat are protecție pentru bărbie, iar gluga lipsește.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Închidere', 'fermoar.'), ('Respirabilitate', '5000 g/m2/24h.'), ('Material', '90% poliester, 10% elastan; căptușeală nailon.'))
  + '<p>Mărimile 106-172 se potrivesc, în general, copiilor de 4-15 ani.</p>',
  [('model', 'Colmar Geaca de puf pentru copii LUSH culoarea roz, 3440.5YM'), ('matlasat', 'Matlasare'), ('puf', '90% Puf de rata, 10% Pene'), ('izolat', 'Model izolat cu captuseala'),
   ('impermeabil', 'Impermeabilitate: 5000 mm'), ('croială', 'Tăiere simplă, fără blocare'), ('elastan', '90% Poliester , 10% Elastan'),
   ('guler', 'Are inchidere cu fermoar si guler ridicat cu barbie'), ('fără glugă', 'Gluga: fara gluga'), ('respirabilitate', 'Respirabilitate: 5000 g/m2/24h'), ('nailon', '100% Nailon')],
  {'Model': 'Colmar LUSH', 'Material': '90% poliester, 10% elastan; umplutură 90% puf, 10% pene', 'Caracteristici': 'puf, matlasată, 5000 mm, guler cu protecție pentru bărbie', 'Cod produs': '3440.5YM'})
