import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(11280,
  f'<p>{GEOX} LIGHTYLOO x Lilo &amp; Stitch B6561C sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} argintii, cu profil scurt, din material textil și piele ecologică, cu personaje din Lilo și Stitch. Talpa are sistemul Geox Respira, în trei straturi cu perforări.</p>'
  '<p>Velcro-ul îi face ușor de încălțat și de scos, iar contrafortul rigidizat ține călcâiul în pantof la primii pași prin parc.</p>'
  '<p>Pe scurt:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 20-27 sunt pentru cei mici de 1-4 ani, în general.</p>',
  [('model', 'Geox Sneakers pentru copii LIGHTYLOO x Lilo & Stitch culoarea argintiu, B6561C.0AJAS'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea ecologică'), RESPIRA, ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('călcâi', 'Contorul de călcâi rigidizat'), ('vârf', 'Cutie rotunda, intarita'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'talpă din cauciuc care este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox LIGHTYLOO x Lilo & Stitch', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira', 'Cod produs': 'B6561C.0AJAS'})

w(11281,
  f'<p>{GEOX} ASSISTER x Lilo &amp; Stitch J65E9B sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, ușori, cu profil scurt, din material textil și piele ecologică, cu personaje de basm, pentru purtat zilnic. Talpa are sistemul Geox Respira, perforat în trei straturi.</p>'
  '<p>Șireturile elastice cu cârlig și bucla de la spate permit încălțatul fără nod, deci copilul se descurcă singur dimineața.</p>'
  '<p>Pe scurt:</p>'
  + L(('Branț', 'textil, se ține ușor curat.'), ('Interior', 'material textil.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 24-31 sunt pentru copii de în jur de 2-7 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ASSISTER x Lilo & Stitch culoarea alb, J65E9B.0AN02'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('personaje', 'Personaje de basm'), ('zilnic', 'purtarea zilnică'), RESPIRA,
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'), ('interior', 'Interiorul: Material textil'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox ASSISTER x Lilo & Stitch', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, buclă, Geox Respira', 'Cod produs': 'J65E9B.0AN02'})

w(11284,
  f'<p>{A("/brand/puma/", "Puma")} Reversible Puffer Jacket 688407 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă reversibilă unisex")}, verde, izolată, cu tehnologia warmCell, care ține corpul la o temperatură potrivită pe frig. Face parte din linia Puma Forever Better, cu materiale reciclate.</p>'.replace('Face parte din linia', 'E din linia')
  + '<p>Croiala e simplă, dreaptă, iar mânecile și tivul au margine elastică, deci geaca stă bine pe corp și se îmbracă ușor. Are glugă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale, unele cu fermoar.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 116-176 sunt pentru copii de 6-16 ani, aproximativ.</p>',
  [('model', 'Puma Geacă reversibilă pentru copii Reversible Puffer Jacket culoarea verde, 688407'), ('reversibil', 'Geacă reversibilă pentru copii'), ('izolat', 'Model izolat cu captuseala'),
   ('warmCell', 'Tehnologia warmCell previne frigul si ajuta la mentinerea unei temperaturi corespunzatoare a corpului'), ('Forever Better', 'Puma Forever Better care contine materiale reciclate'),
   ('croială', 'Tăiere simplă, fără blocare'), ('tiv', 'Mânecile și marginea inferioară sunt finisate cu un tiv elastic'), ('glugă', 'Model cu gluga'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'Puma Reversible Puffer Jacket', 'Material': '100% poliester', 'Caracteristici': 'reversibilă, warmCell, glugă, tiv elastic', 'Cod produs': '688407'})

w(11288,
  f'<p>{A("/brand/columbia/", "Columbia")} Bugaboo 2089842 sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni de schi unisex")} (negru pe site, albaștri la magazin), cu Omni-tech® și cusături sudate pentru vreme rea și Omni-Heat pentru căldură. Sistemul OUTGROWN îi face să țină mai multe sezoane.</p>'
  '<p>Talia se reglează în lățime cu scai, deci se strânge pe un copil slab. Cracii sunt drepți, cu manșetă cauciucată jos, care ține zăpada afară.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'cu închidere.'), ('Umplutură', '85% poliester reciclat, 15% poliester.'))
  + '<p>Mărimile 104-164 sunt pentru copii de 4-14 ani, de obicei.</p>',
  [('model', 'Columbia Pantaloni de schi pentru copii Bugaboo 2089842'), ('Omni-tech', 'Tehnologia Omni-tech®'), ('cusături', 'cusaturilor sudate acoperite cu un strat impermeabil'),
   ('Omni-Heat', 'Tehnologia Omni-Heat'), ('OUTGROWN', 'Sistemul OUTGROWN Grow de la Columbia'), ('talie', 'Talia regleaza latimea cu scai'), ('craci', 'Picior drept'),
   ('manșetă', 'Partea de jos a piciorului cu manseta cauciucata'), ('fermoar', 'Inchidere si fixare cu fermoar'), ('buzunare', 'Buzunare incheiate'),
   ('umplutură', '85% Poliester reciclat, 15% Poliester'), ('culoare', 'albastru')],
  {'Model': 'Columbia Bugaboo', 'Material': '100% poliester; umplutură 85% poliester reciclat', 'Caracteristici': 'Omni-tech®, Omni-Heat, OUTGROWN, talie reglabilă', 'Cod produs': '2089842'},
  notes=['Titlul de pe site spune negru; magazinul dă culoarea albastru.', 'Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(11292,
  f'<p>Papucii {A("/brand/wheat/", "Wheat")} WF601-01 sunt {A("/categorie/papuci/", "papuci pentru fete")}, roz, din piele întoarsă, cu căptușeală din piele fără crom. Inserția din piele previne frecarea și mirosul neplăcut, deci sunt buni de purtat prin casă toată ziua.</p>'.replace(', deci sunt buni de purtat prin casă toată ziua', '')
  + '<p>Velcro-ul se închide repede și se strânge după picior, mai îngust sau mai plin, deci papucul nu iese la mers. Vârful e rotund, cu loc pentru degete.</p>'
  '<p>Pe scurt:</p>'
  + L(('Partea de sus', 'piele întoarsă.'), ('Interior', 'piele naturală.'), ('Talpă', 'material sintetic.'))
  + '<p>Numerele 19-26 sunt pentru copii de în jur de 1-4 ani.</p>',
  [('model', 'Wheat Papuci din piele întoarsă pentru copii culoarea roz, WF601-01'), ('piele întoarsă', 'confecționat din piele intoarsa'),
   ('căptușeală', 'Căptușeala din piele a fost realizată fără utilizarea cromului'), ('inserție', 'Un model cu inserție din piele'), ('frecare', 'previne frecarea, abraziunile și apariția unui miros neplăcut'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('vârf', 'Varf rotund'), ('interior', 'Interiorul: Piele naturala'), ('talpă', 'Talpa: Material sintetic'.split(': ')[1])],
  {'Model': 'Wheat WF601-01', 'Material': 'piele întoarsă, căptușeală din piele fără crom', 'Caracteristici': 'velcro, vârf rotund', 'Cod produs': 'WF601-01'})

w(11300,
  f'<p>Geaca de blugi {A("/brand/bobo-choses/", "Bobo Choses")} B126AC122 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de blugi unisex")}, albastră, ușoară, din denim de bumbac organic 100%, neizolată și necăptușită. E pentru zilele de tranziție.</p>'
  '<p>Croiala e lejeră, deci încape un hanorac dedesubt și vine comod și unui copil mai plinuț. Nu are glugă.</p>'
  '<p>Ca o geacă de blugi clasică, are:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'două, la piept, cu nasturi.'), ('Material', '100% bumbac organic.'))
  + '<p>Mărimile 99/110 până la 149/155 sunt pentru copii de 3-12 ani, cu aproximație.</p>',
  [('model', 'Bobo Choses Geaca de blugi pentru copii B126AC122'), ('ușor', 'Model usor confecționat din denim'), ('organic', '100% Bumbac organic'), ('necăptușit', 'Captuseala: necaptusit'),
   ('neizolat', 'Izolare: neizolat'), ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere lejeră, fără blocare'), ('fără glugă', 'Gluga: fara gluga'),
   ('nasturi', 'Incheiere cu nasturi'), ('buzunare', 'Două buzunare la piept cu nasturi'), ('culoare', 'albastru')],
  {'Model': 'Bobo Choses B126AC122', 'Material': '100% bumbac organic (denim)', 'Caracteristici': 'neizolată, necăptușită, nasturi, croială lejeră', 'Cod produs': 'B126AC122'})

w(11301,
  f'<p>{A("/brand/reima/", "Reima")} Viekkala 5100395A sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni sport de iarnă unisex")}, violet, uni, cu tehnologia ReimaTec împotriva ploii și vântului și impermeabilitate de 10 000 mm. Sunt pentru sporturi de iarnă și joacă pe zăpadă.</p>'
  '<p>Croiala e clasică, simplă, iar talia se reglează în lățime cu arici, deci pantalonii nu alunecă pe un copil slab.</p>'
  '<p>Pe scurt:</p>'
  + L(('Respirabilitate', '7 000 g/m2/24h.'), ('Finisaj', 'BIONIC-FINISH ECO, hidrofob.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-164 sunt pentru copii de în jur de 4-14 ani.</p>',
  [('model', 'Reima Viekkala violet 5100395A'), ('iarnă', 'Pantaloni sport de iarnă copii'), ('uni', 'Model: uni'), ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'),
   ('impermeabil', 'Impermeabilitate: 10 000 mm'), ('sport', 'Tip de activitate: Sporturi de iarnă'), ('croială', 'Croiala clasică, simplă'),
   ('talie', 'Ajustarea lățimii cu arici în talie facilitează reglarea și previne alunecarea'), ('respirabilitate', 'Respirabilitate: 7 000 g/m2/24h'),
   ('BIONIC', 'BIONIC-FINISH ECO este o finisare hidrofoba ecologica'), ('material', '100% Poliester')],
  {'Model': 'Reima Viekkala', 'Material': '100% poliester', 'Caracteristici': 'ReimaTec, 10 000 mm, talie reglabilă cu arici', 'Cod produs': '5100395A'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(11310,
  f'<p>{A("/brand/jack-wolfskin/", "Jack Wolfskin")} MALIMA este o {A("/categorie/geci-jachete/", "geacă de ploaie pentru fete")}, verde, ușor izolată, cu strat exterior TEXAPORE CORE, care apără de ploaie și vânt. E pentru sezonul de tranziție și zilele ude.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile se termină cu manșetă. Gluga încorporată și gulerul ridicat, cu protecție pentru bărbie, țin ploaia departe de gât.</p>'
  '<p>Pentru drumurile pe ploaie:</p>'
  + L(('Elemente reflectorizante', 'pentru vizibilitate.'), ('Căptușeală', 'din plasă.'), ('Buzunare', 'cu închidere.'), ('Închidere', 'fermoar.'))
  + '<p>Mărimile 92-152 sunt pentru copii de 2-12 ani, în mare.</p>',
  [('model', 'Jack Wolfskin Geaca de ploaie copii MALIMA culoarea verde'), ('izolat', 'Model usor izolat'), ('TEXAPORE', 'Stratul exterior este realizat din material TEXAPORE CORE, care oferă protecție împotriva ploii și vântului'),
   ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Manecile finisate cu manseta'), ('glugă', 'Gluga încorporată'),
   ('guler', 'guler ridicat cu barbie'), ('reflectorizant', 'Reflectorizante'), ('plasă', 'Model captusit cu plasa'), ('buzunare', 'Buzunare incheiate'),
   ('fermoar', 'Are inchidere cu fermoar')],
  {'Model': 'Jack Wolfskin MALIMA', 'Material': '100% poliester', 'Caracteristici': 'TEXAPORE CORE, ușor izolată, glugă, reflectorizante', 'Cod produs': ''},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(11311,
  f'<p>Pantofii {A("/brand/biomecanics/", "Biomecanics")} 261105 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} bej, din piele întoarsă, cu motiv animal simpatic, în stil casual, pentru purtat zi de zi, făcuți în parteneriatul Biomecanics Podology, cu podologi.</p>'
  '<p>Vârful rotund, rigidizat, lasă loc degetelor și le apără la joacă, deci pantoful merge și la un picior mai plin. Aricii permit încălțatul de către copil, fără ajutor.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Interior', 'material textil.'), ('Branț', 'plantilla textilă, strat moale în plus.'))
  + '<p>Numerele 19-25 sunt pentru copii de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele întoarsă bej 261105'), ('piele întoarsă', 'Partea superioară din piele întoarsă'), ('motiv', 'Modelul cu motiv animal'),
   ('casual', 'Stilul casual face ca încălțămintea să se potrivească multor ținute zilnice'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership , creată cu podologi'),
   ('vârf', 'Vârful rotund, rigidizat oferă spațiu degetelor și le protejează'), ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea independentă de către copil'),
   ('talpă', 'Talpa flexibilă din cauciuc'), ('interior', 'Interiorul din material textil'), ('branț', 'Branțul plantilla din material textil oferă un strat suplimentar')],
  {'Model': 'Biomecanics 261105', 'Material': 'piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, vârf rigidizat, motiv animal', 'Cod produs': '261105'})

w(11312,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} JX0550 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de puf unisex")}, neagră, matlasată, din poliamidă netedă, umplută cu puf de rață și pene (80/20), pentru frigul de iarnă. Gulerul ridicat și gluga detașabilă apără gâtul și capul.</p>'
  '<p>Croiala e simplă, dreaptă, deci încape un pulover dedesubt. Mânecile și tivul sunt simplu tăiate, fără elastic.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar și capse.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', '100% poliamidă, căptușeală poliester.'))
  + '<p>Mărimile 104-128 sunt pentru copii de 4-8 ani, de regulă.</p>',
  [('model', 'adidas Originals Geacă de puf pentru copii culoarea negru, JX0550'), ('matlasat', 'Modelul matlasat'), ('neted', 'material neted'), ('puf', '80% Puf de rata, 20% Pene'),
   ('frig', 'izolare împotriva frigului'), ('guler, glugă', 'Gulerul ridicat și gluga detașabilă'), ('croială', 'Tăiere simplă, fără blocare'),
   ('mâneci', 'Mâneci și marginea inferioară finisate cu tăiere'), ('închidere', 'Fixare cu fermoar si snap'), ('buzunare', 'Buzunare exterioare incheiata'),
   ('material', 'Materialul de baza: 100% Poliamida')],
  {'Model': 'adidas Originals JX0550', 'Material': '100% poliamidă; umplutură 80% puf, 20% pene', 'Caracteristici': 'puf, matlasată, glugă detașabilă', 'Cod produs': 'JX0550'})
