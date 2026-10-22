import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
REIMA = A('/brand/reima/', 'Reima')
BIO = A('/brand/biomecanics/', 'Biomecanics')
PRIMA = ('PrimaLoft', 'PrimaLoft® - un material patentat din microfibre sintetice, acționând ca izolație termică')
NOTA_M = 'Mărimile sunt date în ani (2-4 ani … 12-14 ani); vârsta e luată direct din ele.'

w(13155,
  f'<p>Vesta de puf {TH} KS0KS00755 roz este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "vestă pentru băieți")} matlasată, ușoară, umplută cu puf natural de rață și pene, pentru sezoanele de tranziție. Gulerul ridicat apără gâtul de vânt, iar fermoarul merge pe toată lungimea.</p>'
  '<p>Nu are glugă, deci se poartă ușor și sub alte haine. Croiala regulară lasă loc de mișcare.</p>'
  '<p>Ce mai are vesta:</p>'
  + L(('Căptușeală', 'completă.'), ('Buzunare', 'laterale, slip-on.'), ('Exterior', '100% nailon.'), ('Umplutură', '90% puf de rață, 10% pene.'))
  + '<p>Mărimile 104-122 sunt pentru băieți de aproximativ 4-7 ani.</p>',
  [('model', 'Tommy Hilfiger Vestă de puf pentru copii roz KS0KS00755'), ('matlasat', 'structură matlasată'), ('puf', 'Umplutură ușoară din puf natural'),
   ('tranziție', 'sezoanele de tranziție'), ('guler', 'Guler ridicat asigură protecția gâtului împotriva frigului'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'),
   ('glugă', 'Fără glugă favorizează un aspect minimalist și facilitează purtarea sub alte articole vestimentare'), ('croială', 'Croială regulară'),
   ('căptușeală', 'Căptușeală completă'), ('buzunare', 'Buzunare laterale tip slip-on'), ('exterior', '100% Nailon'), ('umplutură', '90% Puf de rață, 10% Pene de rață')],
  {'Model': 'Tommy Hilfiger KS0KS00755', 'Material': '100% nailon, umplutură 90% puf de rață', 'Caracteristici': 'vestă de puf, guler ridicat, fermoar', 'Cod produs': 'KS0KS00755'})

w(13159,
  f'<p>Mănușile de schi {REIMA} Hanskas negre sunt {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "mănuși unisex")} cu izolație PrimaLoft, din microfibre sintetice ușoare, care nu absorb umezeala și țin bine căldura. Finisajul hidrofob BIONIC-FINISH ECO le face rezistente la apă, fără garanția impermeabilității complete.</p>'
  '<p>Palma are întărituri din PU, iar cureaua reglabilă strânge mănușa pe încheietură.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Exterior', 'poliamidă, parțial reciclată.'), ('Căptușeală', 'moale, din poliester reciclat.'), ('Certificare', 'Bluesign.'))
  + '<p>Pe site sunt mărimi între 2-4ani și 12-14 ani, pentru copii de cam 2-14 ani.</p>',
  [('model', 'Reima Hanskas negre 5300255B'), ('PrimaLoft', 'PrimaLoft® - un material patentat din microfibre sintetice'), ('umezeală', 'nu absoarbe umezeala'),
   ('căldură', 'retine perfect caldura'), ('BIONIC', 'BIONIC-FINISH ECO este o finisare hidrofoba ecologica'), ('apă', 'nu garantează impermeabilitatea completă'),
   ('PU', 'Întăriri suplimentare pe interiorul mâinii din PU'), ('curea', 'Cureaua reglabilă facilitează ajustarea circumferinței la încheietura mâinii'),
   ('exterior', '59% Poliamida reciclata, 41% Poliamida'), ('căptușeală', 'Interiorul este căptușit cu un material moale'), ('reciclat', 'Captuseala: 100% Poliester reciclat'),
   ('Bluesign', 'Model certificat Bluesign® Standard')],
  {'Model': 'Reima Hanskas', 'Material': 'poliamidă parțial reciclată, căptușeală din poliester reciclat, PrimaLoft', 'Caracteristici': 'PrimaLoft, BIONIC-FINISH ECO, curea reglabilă', 'Cod produs': '5300255B'},
  varsta_txt='2-14 ani', notes=[NOTA_M])

w(13160,
  f'<p>Mănușile de schi {REIMA} Kajastus gri sunt {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "mănuși unisex")} din poliester reciclat, cu izolație PrimaLoft ușoară, care absoarbe de trei ori mai puțină apă decât alte materiale. Sunt tratate cu BIONIC-FINISH ECO, deci rezistă la apă, deși nu complet impermeabil.</p>'
  '<p>Elementele reflectorizante le fac vizibile seara, iar cureaua reglabilă se strânge pe încheietură.</p>'
  '<p>Ce mai au mănușile:</p>'
  + L(('Palmă', 'întărită cu PU.'), ('Interior', 'căptușit moale, mai cald.'), ('Certificare', 'Bluesign.'))
  + '<p>Mărimile de pe site, de la 2-4ani la 12-14 ani, acoperă cam 2-14 ani.</p>',
  [('model', 'Reima Kajastus gri 5300330A'), ('reciclat', 'Materialul de baza: 100% Poliester reciclat'), ('PrimaLoft', 'PrimaLoft® - un material patentat din microfibre sintetice'),
   ('apă', 'Absoarbe de 3 ori mai puțină apă decât alte materiale'), ('BIONIC', 'BIONIC-FINISH ECO este o finisare hidrofoba ecologica'), ('impermeabil', 'nu garantează impermeabilitatea completă'),
   ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'), ('curea', 'Cureaua reglabilă facilitează ajustarea circumferinței la încheietura mâinii'),
   ('PU', 'Întăriri suplimentare pe interiorul mâinii din PU'), ('căptușeală', 'mărește protecția împotriva frigului'), ('Bluesign', 'Model certificat Bluesign® Standard')],
  {'Model': 'Reima Kajastus', 'Material': 'poliester reciclat, PrimaLoft', 'Caracteristici': 'PrimaLoft, reflectorizante, curea reglabilă', 'Cod produs': '5300330A'},
  varsta_txt='2-14 ani', notes=[NOTA_M])

w(13162,
  f'<p>În bej, ghetele de iarnă {A("/brand/primigi/", "Primigi")} 23500 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} înalte, cu carâmbul din piele întoarsă și material textil, care apără de frig și de umezeală. Membrana GORE-TEX oprește apa și vântul, iar piciorul rămâne aerisit.</p>'
  '<p>Închiderea cu arici e rapidă și se reglează după picior. Vârful rotund lasă degetele libere.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Căptușeală', 'textilă, ține de cald.'), ('Talpă', 'din cauciuc, pentru drumurile de iarnă.'), ('Vârf și călcâi', 'întărite.'))
  + '<p>Numerele 25-29 se potrivesc fetițelor de aproximativ 2-5 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii bej PSNGT 23500'), ('carâmb', 'Carâmbul înalt , din combinație de piele întoarsă și material textil, ajută la protecția împotriva frigului și a umezelii'),
   ('GORE-TEX', 'Membrana GORE-TEX® asigură protecție împotriva apei și vântului'), ('arici', 'Sistemul de închidere cu arici facilitează încălțarea și descălțarea rapidă a încălțămintei, precum și ajustarea sa'),
   ('vârf', 'Vârful rotund oferă libertate de mișcare pentru degete'), ('căptușeală', 'Interiorul căptușit cu material textil ajută la menținerea căldurii'),
   ('talpă', 'Talpa din cauciuc contribuie la o bună aderență la sol în condiții de iarnă'), ('întărit', 'Călcâiul întărit și vârful rigidizat')],
  {'Model': 'Primigi 23500', 'Material': 'piele întoarsă și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX, arici', 'Cod produs': 'PSNGT 23500'})

w(13164,
  f'<p>Pantofii {BIO} 221002 roz sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} din piele naturală și piele întoarsă, ușori, pentru purtarea zilnică, creați cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia. Velcro-ul îi face ușor de pus și îi strânge bine pe picior.</p>'
  '<p>Vârful rotund, ușor rigid, lasă loc degetelor, iar călcâiul întărit are umplutură moale care previne frecarea.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, durabilă.'), ('Închidere', 'velcro.'))
  + '<p>Numerele 18-25 sunt pentru copii de în jur de 1-3 ani; la 23 branțul are 14,5 cm.</p>',
  [('model', 'Biomecanics roz 221002'), ('material', 'combinatia pielii naturale cu pielea intoarsa'), ('ușor', 'Model ușor și confortabil'),
   ('Valencia', 'Acestea au fost create in cooperare cu medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'),
   ('velcro', 'Usor de imbracat si se potriveste bine datorita fixarii cu velcro'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('lungime', 'Lungimea brantului pentru marimea este de: 14,5 cm')],
  {'Model': 'Biomecanics 221002', 'Material': 'piele naturală și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, călcâi căptușit', 'Cod produs': '221002'})

w(13166,
  f'<p>În roz, {BIO} 261162 sunt {A("/categorie/adidasi/", "adidași pentru fete")} din piele naturală rezistentă, cu un motiv animalier drăguț, pentru joaca de zi cu zi. Talpa din cauciuc, flexibilă și de tip barefoot, lasă piciorul să lucreze natural.</p>'
  '<p>Cureaua reglabilă cu arici o ajută pe fetiță să se încalțe singură. Gulerul moale nu irită, iar vârful are spațiu sporit pentru degete.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textilă, cu branț aerisit.'), ('Călcâi', 'întărit, pentru postură corectă.'), ('Podology Partnership', 'sprijin pentru piciorul în creștere.'))
  + '<p>Numerele 20-23 merg la fetițe de pe la 1 până pe la 3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele roz 261162'), ('piele', 'Față rezistentă din piele naturală'), ('animal', 'Motiv animalier drăguț'),
   ('barefoot', 'Talpă flexibilă de tip barefoot din cauciuc'), ('arici', 'Închidere practică cu arici cu o curea reglabilă, care facilitează încălțarea independentă'),
   ('guler', 'Guler moale al feței'), ('degete', 'Spațiu sporit în zona degetelor'), ('căptușeală', 'Căptușeală moale din material textil combinată cu un branț respirabil'),
   ('călcâi', 'Călcâi întărit , care stabilizează călcâiul și susține menținerea unei posturi corecte'), ('Podology', 'Sprijin Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261162', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'talpă barefoot, arici cu curea reglabilă', 'Cod produs': '261162'})

w(13170,
  f'<p>Hanoracul {TH} KB0KB10766 roșu este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")} tip pulover clasic, fără glugă și fără închidere, din bumbac 100%, moale la atingere. Modelul uni are un logo discret și se potrivește la multe combinații casual și streetwear.</p>'
  '<p>Decolteul rotund, baza și manșetele au benzi elastice. Nu are căptușeală, deci e ușor, iar croiala simplă stă lejer pe corp. Materialul moale e plăcut pe piele.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Croială', 'simplă, lejeră.'), ('Decor', 'logo discret.'))
  + '<p>Mărimile 104-122 sunt pentru băieți de cam 4-7 ani.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac roșu KB0KB10766'), ('pulover', 'Modelul fără glugă și închidere este un pulover clasic'),
   ('bumbac', 'Confecționat din 100% bumbac , asigură o senzație moale la atingere'), ('logo', 'Modelul uni cu un logo subtil al mărcii'),
   ('stil', 'Stilul casual și streetwear se potrivește la multe combinații'), ('decolteu', 'Decolteul rotund cu bordură elastică'),
   ('benzi', 'Benzile elastice de la bază și de la manșete'), ('căptușeală', 'Lipsa căptușelii permite o construcție ușoară'), ('croială', 'Croiala simplă permite o așezare lejeră'), ('moale', 'Materialul moale asigură o senzație plăcută pe piele')],
  {'Model': 'Tommy Hilfiger KB0KB10766', 'Material': '100% bumbac', 'Caracteristici': 'fără glugă și fermoar, logo discret', 'Cod produs': 'KB0KB10766'})

w(13173,
  f'<p>Geaca de puf {A("/brand/adidas-originals/", "adidas Originals")} JV8547 roz este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, matlasată, cu umplutură naturală din puf de rață și pene, care ține bine de cald pe frig. Gluga căptușită se detașează.</p>'
  '<p>Se închide cu fermoar și capse, iar mânecile și tivul au margine elastică.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'două laterale, cu capse.'), ('Exterior', '100% poliamidă.'), ('Umplutură', '80% puf de rață, 20% pene.'))
  + '<p>Mărimile 104-128 sunt pentru copii de aproximativ 4-8 ani; la 116 cm geaca are 46 cm lungime.</p>',
  [('model', 'adidas Originals Geacă de puf pentru copii culoarea roz, JV8547'), ('izolat', 'Model izolat confecționat din din material matlasat'),
   ('puf', 'Modelul cu umplutura din puf natural si pene garanteaza un nivel ridicat de izolare impotriva frigului'), ('glugă', 'Gluga detasabila'),
   ('glugă căptușită', 'Gluga captusita: 100% Polipropilena'), ('închidere', 'Fixare cu fermoar si snap'), ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică confortabilă'),
   ('buzunare', 'Două buzunare laterale'), ('exterior', 'Materialul de baza: 100% Poliamida'), ('umplutură', '80% Duck Down, 20% Pene'), ('lungime', 'Lungimea: 46 cm')],
  {'Model': 'adidas Originals JV8547', 'Material': '100% poliamidă, umplutură 80% puf de rață', 'Caracteristici': 'geacă de puf, glugă detașabilă, fermoar și capse', 'Cod produs': 'JV8547'})

w(13181,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} LVCKTJM15B violet este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, ușoară, cu umplutură sintetică, pentru sezonul de tranziție. Gluga integrată apără capul de vânt și de frig, iar fermoarul o face rapid de îmbrăcat.</p>'
  '<p>Croiala e regulară, iar lungimea până la șolduri lasă loc de mișcare la joacă.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Căptușeală', 'completă, încă un strat de izolație.'), ('Buzunare', 'laterale.'), ('Material', '100% poliester, țesătură rezistentă.'))
  + '<p>Mărimile 128-176 se potrivesc băieților de cam 8-16 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă petrecută pentru copii violet LVCKTJM15B'), ('matlasat', 'Geaca matlasată Calvin Klein Jeans'), ('umplutură', 'Umplutură sintetică ușoară'),
   ('tranziție', 'sezonul de tranziție'), ('glugă', 'Glugă integrată – element practic care contribuie la protejarea capului împotriva vântului și frigului'),
   ('fermoar', 'Închidere cu fermoar'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'), ('căptușeală', 'Căptușeală completă – stratul interior asigură confort la purtare și o izolație suplimentară'),
   ('buzunare', 'Buzunare laterale funcționale'), ('material', '100% Poliester'), ('țesătură', 'Țesătură rezistentă')],
  {'Model': 'Calvin Klein Jeans LVCKTJM15B', 'Material': '100% poliester, umplutură sintetică', 'Caracteristici': 'matlasată, glugă integrată, fermoar', 'Cod produs': 'LVCKTJM15B'})

w(13182,
  f'<p>Geaca {A("/brand/liewood/", "Liewood")} Nolan Pile Jacket este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} în culoarea maro pe site (bej la magazin), din fleece ușor și foarte rezistent, din poliester reciclat certificat GRS. E neizolată și fără căptușeală, pentru sezonul de tranziție.</p>'
  '<p>Mânecile au găuri pentru degetul mare, care țin mâinile la căldură și nu lasă mânecile să urce. Gulerul ridicat apără de frig.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Închidere', 'fermoar.'), ('Material', '100% poliester reciclat.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 80-140 acoperă copii de aproximativ 1-10 ani.</p>',
  [('model', 'Liewood Geacă copii Nolan Pile Jacket culoarea maro, LW19877'), ('culoare', 'Culoare bej'), ('fleece', 'Model neizolat confecționat din material fleece'),
   ('ușor', 'Material ușor, extrem de rezistent'), ('GRS', 'GRS (Global Recycle Standard)'), ('necăptușit', 'Captuseala: necaptusit'), ('tranziție', 'Izolare: tranzitional'),
   ('degete', 'Găurile pentru degetul mare din partea de jos a mânecilor protejează mâinile'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('material', '100% Poliester reciclat'), ('glugă', 'Gluga: fara gluga')],
  {'Model': 'Liewood Nolan Pile Jacket', 'Material': '100% poliester reciclat (fleece)', 'Caracteristici': 'găuri pentru degetul mare, guler ridicat, fermoar', 'Cod produs': 'LW19877'},
  notes=['Titlul spune maro, magazinul dă culoarea bej; am scris ambele.'])
