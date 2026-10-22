import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
LEVIS = A('/brand/levis/', "Levi's")
LEVN = "Levi's"
REIMA = A('/brand/reima/', 'Reima')

w(13713,
  f'<p>Blugii {TH} WIDE LEG KG0KG09421 sunt {A("/categorie/pantaloni-treninguri/", "blugi pentru fete")} albaștri, cu crac larg, talie înaltă și efect prespălat, ușor vintage, pentru ieșiri informale. Amestecul de bumbac și lyocell e plăcut la atingere.</p>'
  '<p>Denimul e neelastic, deci își ține forma, ca la blugii clasici. Se închid cu fermoar și nasture, iar talia înaltă stă stabil pe șolduri.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '61% bumbac, 39% lyocell.'), ('Croială', 'wide leg, lejeră.'), ('Închidere', 'fermoar și nasture.'))
  + '<p>Mărimile 116-176 sunt pentru fete de aproximativ 6-16 ani.</p>',
  [('model', 'Tommy Hilfiger Blugi wide leg pentru copii WIDE LEG albaștri KG0KG09421'), ('croială', 'Croială wide leg'), ('talie', 'Talie înaltă – ajută la o așezare stabilă pe șolduri'),
   ('prespălat', 'Finisaj cu efect prespălat – conferă blugilor un caracter modern și ușor vintage'), ('informal', 'diverse ieșiri informale'),
   ('lyocell', 'Amestec de bumbac și lyocell – oferă o senzație plăcută la atingere'), ('neelastic', 'Denim neelastic – își menține forma și structura'),
   ('închidere', 'Închidere cu fermoar și nasture'), ('material', '61% Bumbac, 39% Lyocell')],
  {'Model': 'Tommy Hilfiger WIDE LEG KG0KG09421', 'Material': '61% bumbac, 39% lyocell', 'Caracteristici': 'crac larg, talie înaltă, efect prespălat', 'Cod produs': 'KG0KG09421'})

w(13725,
  f'<p>Jacheta scurtă {A("/brand/liewood/", "Liewood")} Nolan Pile Jacket roz este o {A("/categorie/geci-jachete/", "geacă pentru fete")} din material tip sherpa, moale la atingere, pentru sezonul de tranziție. E ușoară, uni, fără glugă, deci se poartă ușor și sub alte haine.</p>'
  '<p>Gulerul ridicat apără gâtul de aerul rece, iar fermoarul o face rapid de îmbrăcat. Lungimea scurtă lasă copilul să se miște liber.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'laterale.'), ('Material', '100% poliester.'), ('Croială', 'regulară, mâneci clasice.'))
  + '<p>Mărimile 80-140 se potrivesc fetelor de cam 1-10 ani.</p>',
  [('model', 'Liewood Jachetă scurtă pentru copii Nolan Pile Jacket roz LW19877'), ('sherpa', 'Material tip sherpa favorizează moliciunea și o senzație plăcută la atingere'),
   ('tranziție', 'Sezon de tranziție'), ('uni', 'Model uni și stilul casual'), ('glugă', 'Fără glugă favorizează lejeritatea modelului și facilitează purtarea sub alte articole vestimentare'),
   ('guler', 'Gulerul ridicat susține protecția gâtului împotriva aerului mai rece'), ('fermoar', 'Închidere cu fermoar'), ('scurt', 'Lungimea scurtă a modelului favorizează mobilitatea'),
   ('buzunare', 'Buzunare laterale practice'), ('material', '100% Poliester'), ('croială', 'Croiala regulară'), ('mânecă', 'Tip de mânecă clasic')],
  {'Model': 'Liewood Nolan Pile Jacket', 'Material': '100% poliester (sherpa)', 'Caracteristici': 'guler ridicat, fermoar, scurtă', 'Cod produs': 'LW19877'})

w(13727,
  f'<p>Geaca de tranziție {TH} KG0KG09501 bej este o {A("/categorie/geci-jachete/", "geacă pentru fete")} ușoară, fără izolație, din țesătură cu bumbac, cu croială relaxed fit și umeri coborâți. Se închide cu două rânduri de nasturi și are guler clasic, ceea ce îi dă un aer elegant.</p>'
  '<p>Nu are glugă, ajunge până la șolduri, iar manșetele cu nervuri se așază bine la încheieturi.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'laterale, slip-on.'), ('Material', '65% bumbac, 35% poliamidă.'), ('Închidere', 'nasturi pe două rânduri.'))
  + '<p>Mărimile 128-176 sunt pentru fete de aproximativ 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă de tranziție pentru copii cu bumbac bej KG0KG09501'), ('izolație', 'Construcție ușoară, fără izolație termică'), ('bumbac', 'Confecționată din țesătură cu bumbac'),
   ('croială', 'Croială relaxed fit'), ('umeri', 'Mâneci cu linia umerilor coborâtă'), ('nasturi', 'Sistem de închidere cu două rânduri de nasturi , care conferă gecii un aspect clasic și elegant'),
   ('guler', 'Guler clasic'), ('glugă', 'Model fără glugă'), ('lungime', 'Lungime până la șolduri'), ('manșete', 'Manșete cu nervuri'),
   ('buzunare', 'Buzunare laterale tip slip-on'), ('material', '65% Bumbac, 35% Poliamidă')],
  {'Model': 'Tommy Hilfiger KG0KG09501', 'Material': '65% bumbac, 35% poliamidă', 'Caracteristici': 'nasturi pe două rânduri, guler clasic, fără izolație', 'Cod produs': 'KG0KG09501'})

w(13729,
  f'<p>Blugii {A("/brand/konges-slojd/", "Konges Sløjd")} MAGOT PANTS GOTS sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "blugi unisex")} albaștri, straight, cu croială regulară și imprimeu decorativ, din bumbac natural, moale. Banda elastică din talie îl ajută pe copil să-i îmbrace și să-i dea jos singur.</p>'
  '<p>Talia normală stă stabil pe șolduri la joacă, iar buzunarele slip-on sunt în față și la spate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Talie', 'normală, elastică.'), ('Model', 'cu imprimeu.'))
  + '<p>Mărimile 80 până la 134-140 se potrivesc copiilor de aproximativ 1-10 ani.</p>',
  [('model', 'Konges Sløjd Blugi straight pentru copii MAGOT PANTS GOTS albaștri KS106133'), ('croială', 'Model cu croială regulară'), ('imprimeu', 'Imprimeu decorativ'),
   ('bumbac', 'Confecționat din bumbac natural'), ('elastic', 'Bandă elastică în talie facilitează îmbrăcarea și dezbrăcarea pantalonilor de către copil'),
   ('talie', 'Talie normală asigură o așezare stabilă pe șolduri'), ('buzunare', 'Buzunare practice tip slip-on în față și la spate'), ('material', '100% Bumbac')],
  {'Model': 'Konges Sløjd MAGOT PANTS GOTS', 'Material': '100% bumbac', 'Caracteristici': 'talie elastică, croială straight, imprimeu', 'Cod produs': 'KS106133'})

w(13730,
  f'<p>Pantalonii de trening {TH} KB0KB10593 bleumarin sunt {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "pantaloni pentru băieți")} din tricot moale de bumbac 100%, cu logo brodat, în stil casual și streetwear. Talia are bandă elastică cu șnururi, deci se reglează ușor.</p>'
  '<p>Croiala regulară și materialul elastic lasă copilul să se miște liber, iar buzunarele sunt pe laterale și la spate. Bumbacul e plăcut la atingere.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Decor', 'logo brodat.'), ('Talie', 'elastică, cu șnur.'))
  + '<p>Mărimile 104-122 sunt pentru băieți de cam 4-7 ani.</p>',
  [('model', 'Tommy Hilfiger Pantaloni de trening pentru copii, din bumbac bleumarin regular waist KB0KB10593'), ('tricot', 'Confecționați din tricot moale de bumbac (100%), plăcut la atingere'),
   ('logo', 'Decorate cu logo brodat'), ('stil', 'stilizările casual și streetwear'), ('talie', 'Bandă elastică în talie cu șnururi permite o ajustare ușoară'),
   ('croială', 'Croiala regulară'), ('elastic', 'Materialul elastic sprijină libertatea'), ('buzunare', 'Buzunarele laterale și din spate practice'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB10593', 'Material': '100% bumbac', 'Caracteristici': 'talie elastică cu șnur, logo brodat', 'Cod produs': 'KB0KB10593'})

w(13731,
  f'<p>Pantalonii de trening {TH} KB0KB10498 bleumarin sunt {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "pantaloni pentru băieți")} din tricot moale de bumbac 100%, uni, cu imprimeu și logo, în stil casual și streetwear. Talia are bandă elastică cu șnururi.</p>'
  '<p>Cracii se termină cu manșete elastice, care țin de cald și țin pantalonii pe loc, iar buzunarele sunt pe laterale și la spate. Tricotul e respirabil și plăcut.</p>'
  '<p>Detaliile principale:</p>'
  + L(('Material', '100% bumbac.'), ('Croială', 'regulară.'), ('Manșete', 'elastice, la glezne.'))
  + '<p>Mărimile 128-176 sunt pentru băieți de aproximativ 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Pantaloni de trening pentru copii din bumbac bleumarin regular waist KB0KB10498'), ('tricot', 'Tricot moale din bumbac 100% , favorizează respirabilitatea și o senzație plăcută la atingere'),
   ('uni', 'Material uni cu imprimeu și logo-ul brandului'), ('stil', 'Stil universal casual și streetwear'), ('talie', 'Bandă elastică în talie cu șnururi'),
   ('manșete', 'Craci terminați cu manșete elastice , ajută la menținerea căldurii și la o așezare stabilă a pantalonilor'), ('buzunare', 'Buzunare laterale și la spate practice'),
   ('croială', 'Pantaloni de trening cu croială regulară'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB10498', 'Material': '100% bumbac', 'Caracteristici': 'talie elastică cu șnur, manșete elastice, logo', 'Cod produs': 'KB0KB10498'})

w(13744,
  f'<p>Același trening {TH} KB0KB10498 bleumarin, în mărimile 104-122: {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "pantaloni pentru băieți")} din bumbac 100%, moale și elastic, cu imprimeu decorativ cu logo. Talia cu elastic și șnur se potrivește ușor pe corp.</p>'
  '<p>La glezne, manșetele elastice țin cracii pe poziție și dau un aer sportiv. Pe laterale și la spate sunt buzunare.</p>'
  '<p>Ce trebuie știut:</p>'
  + L(('Compoziție', 'bumbac 100%.'), ('Croială', 'de trening, regulară.'), ('Decor', 'imprimeu cu logo.'))
  + '<p>Se potrivesc băieților de pe la 4 până pe la 7 ani.</p>',
  [('model', 'Tommy Hilfiger Pantaloni de trening pentru copii din bumbac bleumarin regular waist KB0KB10498'), ('bumbac', 'Confecționați 100% din bumbac'),
   ('elastic', 'Material elastic susține libertatea de mișcare'), ('imprimeu', 'Imprimeu decorativ cu logo al mărcii'), ('talie', 'Talie cu bandă elastică și șnururi'),
   ('manșete', 'Manșete elastice la glezne mențin pantalonii pe poziție, adăugând un caracter sportiv'), ('buzunare', 'Buzunare laterale și la spate practice'),
   ('croială', 'Croiala de trening cu croială regulară'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB10498', 'Material': '100% bumbac', 'Caracteristici': 'talie elastică cu șnur, manșete elastice', 'Cod produs': 'KB0KB10498'})

w(13758,
  f'<p>Pantalonii de iarnă {REIMA} Matias sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")} de schi, bordo (burgundia la magazin), impermeabili și respirabili, cu bretele și cusături complet lipite. Rezistă la apă și la pete, cu finisaj BIONIC-FINISH ECO, iar fibra REPREVE e din sticle reciclate.</p>'
  '<p>Talia înaltă are bandă elastică, iar fermoarul scurt face îmbrăcatul ușor. Fasonul e drept, uni.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Exterior', 'poliester reciclat și poliester cu poliuretan.'), ('Căptușeală', 'poliester, parțial reciclat.'), ('Umplutură', '100% poliester reciclat.'))
  + '<p>Mărimile 80-110 sunt pentru copii de aproximativ 1-5 ani.</p>',
  [('model', 'Reima Matias burgundia 5100130A'), ('culoare', 'burgundia'), ('iarnă', 'Pantaloni sport de iarnă copii'), ('impermeabil', 'material impermeabil cu respirabilitate ridicată'),
   ('bretele', 'Model cu bretele'), ('lipite', 'Cusaturi complet lipite'), ('pete', 'Rezistent la apa si la pete'), ('BIONIC', 'BIONIC-FINISH ECO este o finisare hidrofoba ecologica'),
   ('REPREVE', 'Fibra REPREVE este fabricata din sticle de plastic reciclate'), ('talie', 'Talie inalta cu banda elastica in talie'), ('fermoar', 'Incheiere scurta cu fermoar'),
   ('fason', 'Fason drept'), ('uni', 'Model: uni'), ('exterior', '52% Poliester reciclat, 48% Poliester cu strat de poliuretan'), ('umplutură', 'Umplutura: 100% Poliester reciclat')],
  {'Model': 'Reima Matias', 'Material': 'poliester reciclat cu poliuretan, umplutură din poliester reciclat', 'Caracteristici': 'impermeabili, bretele, cusături lipite', 'Cod produs': '5100130A'},
  notes=['Titlul spune bordo, magazinul scrie burgundia; e aceeași nuanță.'])

w(13761,
  f'<p>Jacheta scurtă {LEVIS} LIGHT WEIGHT WINDBREAKER neagră este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} ușoară, care oprește rafalele reci de vânt și ploaia ușoară, pentru anotimpurile de tranziție. Are logo {LEVN}, glugă integrată și croială simplă.</p>'
  '<p>Fermoarul merge pe toată lungimea, iar manșetele cu nervuri se strâng pe încheieturi. Țesătura rezistă la frecare, deci face față jocului de zi cu zi. Lungimea până la șolduri nu încurcă mișcarea.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'laterale, slip-on.'), ('Lungime', 'până la șolduri.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 140-176 sunt pentru copii de aproximativ 10-16 ani.</p>',
  [('model', "Levi's Jachetă scurtă pentru copii LIGHT WEIGHT WINDBREAKER neagră 9EP678"), ('windbreaker', 'Construcția ușoară a gecii windbreaker favorizează protecția împotriva rafalelor reci de vânt'),
   ('ploaie', 'protejează eficient împotriva vântului și a ploii ușoare'), ('tranziție', 'anotimpurile de tranziție'), ('logo', "Modelul cu logo Levi's"),
   ('glugă', 'Glugă integrată'), ('croială', 'Croiala simplă'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'), ('manșete', 'Manșete cu nervuri'),
   ('abraziune', 'Țesătură rezistentă sprijină rezistența la abraziune, susținând utilizarea pe termen lung în timpul jocului'), ('buzunare', 'Buzunare practice tip slip-on pe laterale'), ('lungime', 'Lungimea până la șolduri'), ('material', '100% Poliester')],
  {'Model': "Levi's LIGHT WEIGHT WINDBREAKER", 'Material': '100% poliester', 'Caracteristici': 'windbreaker, glugă integrată, fermoar', 'Cod produs': '9EP678'})

w(13816,
  f'<p>Pantofii barefoot {REIMA} ASTELU mov sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} pentru un mers natural, vegani, cu drop zero și partea de sus flexibilă, elastică și respirabilă. Vârful e mai lat, ca degetele să aibă loc să se miște.</p>'
  '<p>Șiretul elastic face încălțatul rapid, iar talpa flexibilă din cauciuc ține bine pe sol. Branțul detașabil Happy Fit ajută la alegerea mărimii.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Față', '80% poliester reciclat, 12% poliuretan, 6% poliester, 2% bumbac.'), ('Talpă', '100% cauciuc.'), ('Greutate', '300 g.'))
  + '<p>Gama e lungă, 22-40, deci merge de la aproximativ 1 an în sus.</p>',
  [('model', 'REIMA ASTELU'), ('culoare', 'Mov (mov / alb)'), ('barefoot', 'Pantofii barefoot pentru copii Reima ASTELU asigură un mers sănătos și natural'),
   ('vegan', 'vegani'), ('drop', 'drop zero pentru o poziție naturală'), ('superior', 'parte superioară respirabilă și elastică'), ('vârf', 'un vârf lat pentru mișcarea liberă a degetelor'),
   ('șiret', 'șiret elastic pentru încălțare rapidă și ușoară'), ('talpă', 'talpă din cauciuc pentru o aderență mai bună'), ('flexibil', 'talpă flexibilă pentru libertate de mișcare'),
   ('Happy Fit', 'Branțul detașabil Happy Fit permite alegerea mărimii potrivite'), ('față', '80% poliester (reciclat), 12% poliuretan, 6% poliester, 2% bumbac'),
   ('cauciuc', '100 % cauciuc'), ('greutate', '300 g')],
  {'Model': 'Reima ASTELU', 'Material': 'poliester reciclat, poliuretan, talpă din cauciuc', 'Caracteristici': 'barefoot, drop zero, șiret elastic, Happy Fit', 'Cod produs': '240075'})
