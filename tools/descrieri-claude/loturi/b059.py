import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(11739,
  f'<p>Geaca {A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 312970094003 este o {A("/categorie/geci-jachete/", "geacă cu puf pentru fete")}, bleumarin, uni, umplută cu puf de rață și pene (75/25), din țesătură netedă, ușor de întreținut. E pentru zilele mai reci, iar gluga integrată și gulerul înalt apără capul și gâtul de vânt.</p>'
  '<p>Croiala e regular fit, cu loc pentru straturi dedesubt, iar lungimea ajunge până la șolduri.</p>'
  '<p>Material și închidere, pe rând:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'tip slip-on, pentru mâini.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 88-93 până la 124-128 sunt pentru copii de 1-8 ani, cu aproximație.</p>',
  [('model', 'Polo Ralph Lauren Geacă cu puf pentru copii bleumarin 312970094003'), ('uni', 'Model uni'), ('puf', '75% Puf de rață, 25% Pene de rață'),
   ('neted', 'Țesătură exterioară netedă'), ('întreținere', 'ușor de întreținut'), ('reci', 'zilele mai reci'), ('glugă', 'Glugă integrată împreună cu gulerul înalt oferă protecție pentru cap și gât împotriva vântului'),
   ('croială', 'Croiala regular fit favorizează libertatea de mișcare, permițând purtarea de straturi suplimentare'), ('lungime', 'Lungimea până la șolduri'),
   ('fermoar', 'Închidere cu fermoar'), ('buzunare', 'Buzunare practice tip slip-on'), ('material', 'Material principal: 100% Poliester'.split(': ')[1])],
  {'Model': 'Polo Ralph Lauren 312970094003', 'Material': '100% poliester; umplutură 75% puf, 25% pene de rață', 'Caracteristici': 'puf, glugă integrată, guler înalt', 'Cod produs': '312970094003'})

w(11749,
  f'<p>{A("/brand/liewood/", "Liewood")} Manu Rainwear Set LW19910 este un {A("/categorie/bebe-imbracaminte-salopete-compleuri/", "set de ploaie pentru bebeluși")}, bleumarin, cu membrană impermeabilă de 20000 mm H2O, din țesătură rezistentă, pentru zilele ploioase și joaca afară. Detaliile reflectorizante îl fac pe copil vizibil seara.</p>'
  '<p>Croiala e regulară, cu mâneci raglan. Manșetele și bordurile de la picioare sunt elastice, iar bretelele reglabile țin pantalonii la locul lor.</p>'
  '<p>Ce merită știut în plus:</p>'
  + L(('Glugă', 'detașabilă, cu urechi de animal.'), ('Închidere', 'fermoar cu clapetă cu arici.'), ('Buzunare', 'laterale, inserate.'))
  + '<p>Mărimile 80-104 sunt pentru cei mici de 1-4 ani, în general.</p>',
  [('model', 'Liewood Pelerină de ploaie pentru copii Manu Rainwear Set bleumarin LW19910'), ('membrană', 'Membrană impermeabilă cu un parametru de 20000 mm H2O'),
   ('țesătură', 'Confecționat din țesătură rezistentă'), ('reflectorizant', 'Detalii reflectorizante pe set sporesc vizibilitatea copilului după lăsarea întunericului'),
   ('croială', 'Croiala regulară'), ('raglan', 'Mâneci raglan'), ('elastic', 'Manșete elastice și borduri elastice la picioare'), ('bretele', 'Bretele reglabile la pantaloni le mențin în poziție'),
   ('glugă', 'Glugă detașabilă cu urechi drăguțe de animale'), ('fermoar', 'Fermoarul cu clapetă cu arici'), ('buzunare', 'Buzunare laterale inserate')],
  {'Model': 'Liewood Manu Rainwear Set', 'Material': '100% poliester', 'Caracteristici': 'set de ploaie, 20000 mm, reflectorizant, bretele reglabile', 'Cod produs': 'LW19910'})

w(11752,
  f'<p>{A("/brand/puma/", "Puma")} T7 Quilted Puffer Jacket 694632 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, roz, matlasată, cu izolație sintetică medie și țesătură exterioară durabilă, pentru activitățile de iarnă afară. Gluga integrată și gulerul ridicat apără de vânt și frig.</p>'
  '<p>Croiala e regulară, cu mâneci raglan și lungimea până la șolduri, iar căptușeala completă o face ușor de îmbrăcat peste alte straturi.</p>'
  '<p>Alte detalii utile:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale, cu închidere.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 116-176 sunt pentru copii de 6-16 ani, de obicei.</p>',
  [('model', 'Puma Geacă petrecută pentru copii T7 Quilted Puffer Jacket roz 694632'), ('matlasat', 'structură matlasată'), ('izolație', 'Izolație sintetică medie'),
   ('țesătură', 'Țesătură exterioară durabilă'), ('iarnă', 'activități de iarnă în aer liber'), ('glugă', 'Glugă integrată'), ('guler', 'Guler ridicat'), ('croială', 'Croială regulară'),
   ('raglan', 'Mâneci raglan'), ('lungime', 'Lungime până la șolduri'), ('căptușeală', 'Căptușeală completă care sporește confortul la purtare, facilitând îmbrăcarea peste alte straturi'),
   ('fermoar', 'Închidere cu fermoar'), ('buzunare', 'Buzunare laterale cu închidere'), ('material', '100% Poliester')],
  {'Model': 'Puma T7 Quilted Puffer Jacket', 'Material': '100% poliester', 'Caracteristici': 'matlasată, izolație medie, glugă integrată, mâneci raglan', 'Cod produs': '694632'})

w(11754,
  f'<p>{A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} LVCKSJD02B este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă scurtă din denim unisex")}, albastră, cu croială clasică trucker, efect prespălat, print cu monogramă și patch cu logo. E din bumbac 100% și se poartă în sezonul de tranziție.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, deci nu încurcă la joacă. Gulerul e ascuțit, clasic.</p>'
  '<p>La purtat, contează și:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'la piept, cu clape, și deschise în talie.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Calvin Klein Jeans Jachetă scurtă pentru copii, din denim albastră LVCKSJD02B'), ('trucker', 'Croială clasică tip trucker'), ('prespălat', 'Efect prespălat modern'),
   ('logo', 'printul cu monogramă și patch-ul'), ('bumbac', 'realizat 100% din bumbac'), ('tranziție', 'sezonului de tranziție'), ('croială', 'Croială regulară'),
   ('lungime', 'Lungime până la șolduri'), ('guler', 'Guler ascuțit'), ('nasturi', 'Închidere cu nasturi'), ('buzunare piept', 'Buzunare la piept cu clape'),
   ('buzunare talie', 'Buzunare deschise la nivelul taliei')],
  {'Model': 'Calvin Klein Jeans LVCKSJD02B', 'Material': '100% bumbac (denim)', 'Caracteristici': 'trucker, prespălată, monogramă, nasturi', 'Cod produs': 'LVCKSJD02B'})

w(11760,
  f'<p>{A("/brand/donsje/", "Donsje")} Damian Jacket 4123700 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de tranziție unisex")}, maro, uni, din material neted combinat cu imitație moale de blană. Nu e izolată termic, deci se poartă în zilele mai calde din sezonul de tranziție.</p>'
  '<p>Croiala e regular fit, cu lungimea până la șolduri. Gluga nu se detașează și apără capul pe vânt, iar căptușeala sintetică o face ușor de îmbrăcat.</p>'
  '<p>Pentru zi de zi, are:</p>'
  + L(('Închidere', 'dublă, fermoar și capse.'), ('Material', '100% nailon, cu inserții din poliester.'), ('Căptușeală', 'completă, sintetică.'))
  + '<p>Mărimile 86-128 sunt pentru copii de aproximativ 1-8 ani.</p>',
  [('model', 'Donsje Geacă de tranziție pentru copii Damian Jacket maro 4123700'), ('uni', 'Model uni'), ('materiale', 'modelul combină materialul neted cu imitația moale de blană'),
   ('neizolat', 'Fără izolație termică – construcția ușoară este potrivită pentru a fi purtată în zilele mai calde ale sezonului de tranziție'), ('croială', 'Croială regular fit'),
   ('lungime', 'Lungime până la șolduri'), ('glugă', 'Glugă nedetașabilă'), ('căptușeală', 'Căptușeală sintetică'), ('închidere', 'combinația de fermoar și capse'),
   ('material', '100% Nailon')],
  {'Model': 'Donsje Damian Jacket', 'Material': '100% nailon, inserții poliester, căptușeală poliester', 'Caracteristici': 'neizolată, imitație de blană, fermoar și capse, glugă fixă', 'Cod produs': '4123700'})

w(11761,
  f'<p>Pantalonii de trening {TH} KG0KG09448 sunt {A("/categorie/pantaloni-treninguri/", "pantaloni de trening pentru fete")}, bleumarin, din tricot moale de bumbac cu elastan, pentru joacă și relaxare. Cracii sunt conici, fără elastic jos, pentru un aspect modern.</p>'
  '<p>Croiala e regulară, iar talia normală are elastic și șnur, deci se strânge pe un copil mai slab, fără curea. Materialul elastic se mișcă odată cu copilul.</p>'
  '<p>Mai sunt câteva detalii:</p>'
  + L(('Talie', 'normală, cu elastic și șnur.'), ('Craci', 'conici.'), ('Material', '78% bumbac, 18% poliester, 4% elastan.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, în general.</p>',
  [('model', 'Tommy Hilfiger Pantaloni de trening pentru copii, cu bumbac bleumarin regular waist KG0KG09448'), ('bumbac', 'Bumbac moale'), ('joacă', 'ideali pentru joacă și relaxare'),
   ('craci', 'Craci conici fără elastic'), ('croială', 'Croială regulară'), ('talie', 'Elastic și șnururi în talie'), ('talie normală', 'Talie normală'), ('elastic', 'Material elastic'),
   ('material', '78% Bumbac, 18% Poliester, 4% Elastan')],
  {'Model': 'Tommy Hilfiger KG0KG09448', 'Material': '78% bumbac, 18% poliester, 4% elastan', 'Caracteristici': 'talie cu elastic și șnur, craci conici', 'Cod produs': 'KG0KG09448'})

w(11763,
  f'<p>Pantofii de iarnă {A("/brand/geox/", "Geox")} SHAYLAX J46EYA sunt {A("/categorie/incaltaminte-pantofi/", "încălțăminte de iarnă pentru fete")}, maro, din nubuc (piele întoarsă), izolați, cu indice mediu de izolare termică și interior moale căptușit. Sunt pentru zilele reci.</p>'
  '<p>Fermoarul lateral îi face ușor de încălțat și de scos, iar bucla de la spate ajută la tras pe picior. Partea de sus ridicată rigidizează glezna pe teren denivelat.</p>'
  '<p>Ce mai are, de la vârf la călcâi:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Vârf', 'rotund.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 28-35 sunt pentru copii de în jur de 4-11 ani.</p>',
  [('model', 'Geox Pantofi de iarnă din nubuc pentru copii SHAYLAX culoarea maro, J46EYA.00022'), ('nubuc', 'Model Izolat confecționat din piele nabuc'),
   ('indice', 'Indicele de izolare termică'), ('mediu', 'MEDIU'), ('interior', 'Interiorul moale căptușit asigură un confort ridicat la purtare și un confort termic optim'),
   ('fermoar', 'Un fermoar lateral convenabil îl face ușor de pus și scos'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('teren', 'suprafețe neuniforme'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('vârf', 'Varf rotund'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox SHAYLAX', 'Material': 'nubuc, interior textil căptușit, talpă din cauciuc', 'Caracteristici': 'izolați (indice mediu), fermoar lateral, Geox Respira', 'Cod produs': 'J46EYA.00022'},
  notes=['Au partea de sus ridicată și sunt de iarnă, listați la Pantofi.'])

w(11769,
  f'<p>{A("/brand/konges-slojd/", "Konges Sløjd")} COLLETTE DRESS KS104750 este o {A("/categorie/rochii-fuste/", "rochie de lână pentru fete")}, bej, mini, fără mâneci, din tricot de lână merinos, ușoară, cu imprimeu, broderie și finisaje decorative. Decolteul e clasic, rotund.</p>'
  '<p>Croiala e dreaptă, simplă, deci se poartă singură sau peste o bluză cu mânecă lungă în zilele mai reci. Are două buzunare în față.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Material', '100% lână.'), ('Lungime', 'mini.'), ('Detalii', 'broderie și finisaje decorative.'))
  + '<p>Mărimile 98 până la 134-140 sunt pentru copii de aproximativ 3-10 ani.</p>',
  [('model', 'Konges Sløjd Rochie de lână pentru copii COLLETTE DRESS culoarea bej, mini, drept, KS104750'), ('mini', 'Lungime: mini'), ('fără mâneci', 'Maneca: fara maneci'),
   ('merinos', 'Lâna merinos este ușoară'), ('tricot', 'Material: tricotaj'), ('imprimeu', 'Model: imprimeu'), ('broderie', 'Broderie decorativa'), ('finisaje', 'Finisaje decorative'),
   ('decolteu', 'Decolteu clasic, rotund'), ('croială', 'Fit: drept'), ('buzunare', 'Două buzunare în față'), ('material', '100% Lana')],
  {'Model': 'Konges Sløjd COLLETTE DRESS', 'Material': '100% lână (merinos)', 'Caracteristici': 'mini, fără mâneci, croială dreaptă, buzunare', 'Cod produs': 'KS104750'},
  notes=['„Peste o bluză cu mânecă lungă” e dedus din faptul că rochia e fără mâneci.'])

w(11771,
  f'<p>{TH} KG0KG09241 este un {A("/categorie/bluze-tricouri-hanorace/", "hanorac cu glugă pentru fete")}, roz, fără fermoar, din amestec moale de bumbac tip buclă cu elastan, cu logo texturat pe piept. E lejer, pentru activitățile zilnice și momentele de relaxare.</p>'
  '<p>Croiala e lejeră, cu umerii căzuți, iar materialul ușor elastic se adaptează la corp. Manșetele și baza cu nervuri strâng ușor.</p>'
  '<p>Elementele practice:</p>'
  + L(('Glugă', 'integrată.'), ('Material', '66% bumbac, 28% nailon, 4% lyocell, 2% elastan.'), ('Logo', 'texturat, pe piept.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, aproximativ.</p>',
  [('model', 'Tommy Hilfiger Hanorac cu glugă pentru copii, cu bumbac roz KG0KG09241'), ('fără fermoar', 'Hanoracul cu glugă fără fermoar'), ('buclă', 'Amestec de bumbac tip buclă cu elastan'),
   ('logo', 'Logo-ul texturat Tommy Hilfiger pe piept'), ('zilnic', 'activitățile zilnice'), ('croială', 'Croiala lejeră cu linia umerilor căzută'), ('elastic', 'Materialul ușor elastic'),
   ('nervuri', 'Manșetele și baza cu nervuri'), ('glugă', 'Gluga integrată'), ('material', '66% Bumbac, 28% Nailon, 4% Lyocell, 2% Elastan')],
  {'Model': 'Tommy Hilfiger KG0KG09241', 'Material': '66% bumbac, 28% nailon, 4% lyocell, 2% elastan', 'Caracteristici': 'glugă, croială lejeră, logo texturat', 'Cod produs': 'KG0KG09241'})

w(11772,
  f'<p>{A("/brand/diesel/", "Diesel")} JOSIP JACKET J02883 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "vestă fără mâneci unisex")}, neagră, ușor izolată cu umplutură sintetică, cu glugă și logo decorativ, pentru zilele mai reci din sezonul de tranziție. Țesătura e rezistentă și se îngrijește ușor.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar fără mâneci lasă brațele libere. Căptușeala integrală o face ușor de îmbrăcat peste un hanorac.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 132-175 sunt pentru copii de 9-16 ani, de regulă.</p>',
  [('model', 'Diesel Jachetă fără mâneci cu glugă pentru copii JOSIP JACKET neagră J02883'), ('izolație', 'Izolație sintetică ușoară'), ('umplutură', 'Umplutura din material sintetic'),
   ('glugă', 'Glugă integrată'), ('logo', 'Logo decorativ'), ('tranziție', 'sezonul de tranziție'), ('țesătură', 'Confecționată dintr-o țesătură rezistentă'),
   ('croială', 'Croiala regulară'), ('lungime', 'Lungime până la șolduri'), ('căptușeală', 'Căptușeală integrală la interior'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'),
   ('buzunare', 'Buzunare laterale practice'), ('material', '100% Poliamidă')],
  {'Model': 'Diesel JOSIP JACKET', 'Material': '100% poliamidă', 'Caracteristici': 'vestă, ușor izolată, glugă, fermoar', 'Cod produs': 'J02883'})
