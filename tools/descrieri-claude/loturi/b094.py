import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
REIMA = A('/brand/reima/', 'Reima')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')

w(13534,
  f'<p>În numerele cele mai mici, 20-23, {GEOX} NASHIK B465NA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albaștri, din piele naturală, piele întoarsă și textil, în stil casual. Branțul are imprimeu cu care vedeți repede dacă piciorul a crescut.</p>'
  '<p>Gulerul ușor întărit sprijină glezna fără să o strângă, iar aricii îl lasă pe copil să se încalțe singur. Talpa plată din cauciuc ține bine pe diverse suprafețe.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'piele naturală și textil.'), ('Călcâi', 'întărit.'), ('Talpă', 'cauciuc plat.'))
  + '<p>Se potrivesc băieților de aproximativ 1-3 ani.</p>',
  [('model', 'Geox NASHIK sneakers pentru copii din piele albastri B465NA.0CL22'), ('culoare', 'Culoare albastru'), ('material', 'Partea superioară din combinație de piele naturală, piele întoarsă și material textil'),
   ('casual', 'cu un stil casual'), ('branț', 'Branț cu imprimeu pentru verificarea mărimii'), ('guler', 'Gulerul ușor întărit al părții superioare sprijină glezna, fără a limita libertatea de mișcare'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea independentă'), ('căptușeală', 'Interiorul finisat cu piele naturală și material textil'),
   ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpa plată realizată din cauciuc favorizează stabilitatea pe diverse suprafețe')],
  {'Model': 'Geox NASHIK', 'Material': 'piele naturală, piele întoarsă și textil, interior din piele și textil', 'Caracteristici': 'arici, branț cu verificare de mărime', 'Cod produs': 'B465NA.0CL22'})

w(13537,
  f'<p>Cizmele de zăpadă {A("/brand/columbia/", "Columbia")} SNOWTROT MID sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} în culoarea negru pe site (bej la magazin), izolate, din material textil și sintetic, care se trag pe picior fără închidere. Tehnologia Omni-Tech, cu membrană microporoasă și cusături sudate, apără de schimbările bruște de vreme.</p>'
  '<p>Talpa intermediară Techlite e ușoară și preia șocurile, iar talpa exterioară din cauciuc e flexibilă și durabilă.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Vârf', 'cutie rotundă, moale.'), ('Călcâi', 'contrafort rigidizat.'))
  + '<p>Numerele 32-39 se poartă de pe la 8 ani în sus; la 32 branțul are 19 cm.</p>',
  [('model', 'Columbia Cizme de iarnă copii SNOWTROT MID culoarea negru, 2078911'), ('culoare', 'Culoare bej'), ('izolat', 'Izolare: izolat'), ('material', 'combinația materialului textil cu cel sintetic'),
   ('fixare', 'Fixare: fara fixare'), ('Omni-Tech', 'Tehnologia Omni-tech® ofera protectie completa impotriva schimbarilor bruste ale vremii'), ('sudate', 'cusaturilor sudate'),
   ('Techlite', 'Talpa intermediară ușoară Techlite ™ oferă confort de lungă durată'), ('talpă', 'talpă flexibilă din cauciuc, care este durabilă'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('vârf', 'Cutie rotunda si moale'),
   ('călcâi', 'Contorul de călcâi rigidizat'), ('lungime', 'Lungimea brantului pentru marimea este de: 19 cm')],
  {'Model': 'Columbia SNOWTROT MID', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Omni-Tech, Techlite, izolate, fără închidere', 'Cod produs': '2078911'},
  notes=['Titlul spune negru, magazinul dă culoarea bej; am scris ambele.'])

w(13538,
  f'<p>Geaca {A("/brand/vans/", "Vans")} MTE Hillgate Puffer neagră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, izolată, din linia All Weather MTE, cu material mai rezistent la umezeală. Gulerul ridicat și gluga fixă apără de frig.</p>'
  '<p>Fermoarul merge pe toată lungimea și are clapă interioară contra vântului, iar mânecile și tivul au margine elastică.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'două, laterale.'), ('Căptușeală', 'da.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 129-139.5 până la 165-173 sunt pentru băieți de aproximativ 8-15 ani; la 151/165 cm geaca are 58 cm lungime.</p>',
  [('model', 'Vans Geacă copii MTE Hillgate Puffer BY culoarea negru, VN000PKYBLK1'), ('matlasat', 'Model matlasat cu izolație sintetică'), ('izolat', 'Model izolat cu captuseala'),
   ('MTE', 'Model din linia All Weather MTE. Produsul este realizat dintr-un material cu rezistenta sporita la umiditate'), ('glugă', 'Gulerul ridicat și gluga fixă'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară împotriva furtunii'), ('margini', 'Mânecile și marginea inferioară sunt finisate cu bătături'),
   ('buzunare', 'Două buzunare laterale'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 58 cm')],
  {'Model': 'Vans MTE Hillgate Puffer', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'All Weather MTE, glugă fixă, clapă la fermoar', 'Cod produs': 'VN000PKYBLK1'})

w(13540,
  f'<p>{GEOX} LIGHTYLOO x Spiderman sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, cu branțuri luminoase și personajul Spiderman, din material textil și piele ecologică, ușori, pentru purtarea zilnică. Curelele cu velcro permit o strângere după picior.</p>'
  '<p>Bucla ajută la încălțat și la descălțat, iar cutia rotundă e întărită și apără degetele. Interiorul textil e confortabil pe tot parcursul zilei.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Interior', 'textil, ușor de ținut curat.'), ('Profil', 'jos.'))
  + '<p>Numerele 20-27 se potrivesc băieților de cam 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii LIGHTYLOO x Spiderman culoarea bleumarin, B655ZC.0BC14'), ('lumini', 'Pantofi cu branturi luminoase'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('velcro', 'Curelele cu velcro pentru prindere ușoară permit o potrivire personalizată'), ('buclă', 'Bucla ușurează să pui pantoful în picior'),
   ('vârf', 'Cutie rotunda, intarita'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('profil', 'Înălțime: mic de statură')],
  {'Model': 'Geox LIGHTYLOO x Spiderman', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'branțuri luminoase, velcro, Geox Respira', 'Cod produs': 'B655ZC.0BC14'})

w(13541,
  f'<p>Bluza cu mânecă lungă {TH} KG0KG09538 roz este o {A("/categorie/bluze-tricouri-hanorace/", "bluză pentru fete")} din bumbac 100%, moale și elastic, cu dungi și imprimeu cu inscripție, pentru ținute casual de fiecare zi. Croiala lejeră nu încurcă la joacă.</p>'
  '<p>Decolteul are guler și închidere, iar materialul elastic face bluza ușor de îmbrăcat și lasă copilul să se miște liber. Bumbacul e delicat cu pielea sensibilă.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Model', 'dungi, inscripție.'), ('Decolteu', 'cu guler și închidere.'))
  + '<p>Mărimile 128-176 sunt pentru fete de aproximativ 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Longsleeve pentru copii din bumbac roz KG0KG09538'), ('bumbac', '100% bumbac este moale și delicat'), ('elastic', 'Material elastic facilitează îmbrăcarea și favorizează libertatea de mișcare'),
   ('dungi', 'Modelul cu dungi și imprimeu cu inscripție'), ('casual', 'Stilul casual se potrivește cu ținutele zilnice'), ('croială', 'Croială lejeră favorizează joaca nestânjenită'),
   ('decolteu', 'Decolteu cu guler și închidere'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG09538', 'Material': '100% bumbac', 'Caracteristici': 'dungi, inscripție, guler cu închidere', 'Cod produs': 'KG0KG09538'})

w(13567,
  f'<p>Codul LVCKTJM15B de la {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} vine și în negru: o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, cu izolație sintetică ușoară, pentru primăvară și toamnă. Gluga e prinsă de geacă și apără capul de vânt și frig.</p>'
  '<p>Croiala regulară, cu mâneci clasice, lasă brațele libere, iar geaca ajunge până la șolduri. Se închide repede, cu fermoar.</p>'
  '<p>Ce trebuie știut:</p>'
  + L(('Exterior', 'țesătură rezistentă, ușor de întreținut.'), ('Căptușeală', 'completă.'), ('Buzunare', 'laterale.'), ('Compoziție', 'integral poliester.'))
  + '<p>Numerele 128-176 sunt pentru băieți de pe la 8 până pe la 16 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă petrecută pentru copii neagră LVCKTJM15B'), ('matlasat', 'Geaca matlasată Calvin Klein Jeans'), ('izolație', 'Izolație sintetică ușoară'),
   ('tranziție', 'sezonul de tranziție'), ('glugă', 'Glugă integrată – elementul practic protejează capul de vânt și frig'), ('croială', 'Croială regulară'),
   ('mânecă', 'Mânecă de tip clasic'), ('lungime', 'Lungime până la șolduri'), ('fermoar', 'Închidere cu fermoar'),
   ('țesătură', 'Țesătură rezistentă – materialul exterior contribuie la durabilitate și ușurință în întreținere'), ('căptușeală', 'Căptușeală completă'),
   ('buzunare', 'Buzunare laterale funcționale'), ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans LVCKTJM15B', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, glugă integrată, fermoar', 'Cod produs': 'LVCKTJM15B'})

w(13568,
  f'<p>Hanoracul {TH} KB0KB10766 bleumarin e un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")} clasic, tras pe cap, fără glugă și fără închidere, din bumbac 100%. E uni, cu un logo mic, și merge cu multe ținute casual și streetwear.</p>'
  '<p>N-are căptușeală, deci e ușor. Decolteul rotund și bordurile elastice de la bază și manșete îl țin bine pe corp, iar croiala simplă stă lejer.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', 'bumbac moale.'), ('Croială', 'simplă, lejeră.'), ('Logo', 'discret.'))
  + '<p>Mărimile 104-122 sunt pentru băieți de vreo 4-7 ani, orientativ.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac bleumarin KB0KB10766'), ('pulover', 'Modelul fără glugă și fără închidere este un hanorac clasic tip pulover'),
   ('bumbac', 'Confecționat din bumbac 100%'), ('logo', 'Modelul uni cu logo subtil'), ('stil', 'Stilul casual și streetwear se potrivește cu multe ținute'),
   ('căptușeală', 'Lipsa căptușelii permite o construcție ușoară'), ('decolteu', 'Decolteu rotund cu bordură elastică'), ('borduri', 'Bordurile elastice la bază și manșete'),
   ('croială', 'Croiala simplă permite o așezare lejeră'), ('moale', 'Materialul moale asigură o senzație plăcută pe piele')],
  {'Model': 'Tommy Hilfiger KB0KB10766', 'Material': '100% bumbac', 'Caracteristici': 'fără glugă și închidere, logo discret', 'Cod produs': 'KB0KB10766'})

w(13570,
  f'<p>Geaca cu puf {TH} KS0KS00652 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} albă, uni, cu logo, ușor izolată cu puf natural de rață și pene, pentru zilele mai reci de tranziție. Puful ține de cald fără să facă geaca grea, iar gulerul ridicat apără gâtul de vânt.</p>'
  '<p>Croiala regulară lasă loc de mișcare, iar manșetele cu elastic țin frigul afară.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'sintetică.'), ('Buzunare', 'laterale, slip-on.'), ('Exterior', '100% nailon.'), ('Umplutură', '90% puf de rață, 10% pene.'))
  + '<p>Mărimile 128-176 se potrivesc băieților de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă cu puf pentru copii albă KS0KS00652'), ('culoare', 'Culoare alb'), ('uni', 'Modelul uni cu logo'), ('puf', 'Izolație ușoară din puf natural'),
   ('greutate', 'păstrând în același timp o greutate redusă a produsului'), ('tranziție', 'zilele mai reci de tranziție'), ('guler', 'Gulerul ridicat ajută la protejarea gâtului împotriva vântului'),
   ('croială', 'Croiala regulară'), ('manșete', 'Manșete cu elastic'), ('căptușeală', 'Căptușeala sintetică'), ('buzunare', 'Buzunare laterale tip slip-on'),
   ('exterior', '100% Nailon'), ('umplutură', '90% Puf de rață, 10% Pene')],
  {'Model': 'Tommy Hilfiger KS0KS00652', 'Material': '100% nailon, umplutură 90% puf de rață', 'Caracteristici': 'puf natural, guler ridicat, manșete elastice', 'Cod produs': 'KS0KS00652'})

w(13572,
  f'<p>Hanoracul cu fermoar {REIMA} Kerros roz este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} din micro fleece Polartec, ușor, catifelat, care se usucă repede și ține de cald. Fermoarul merge pe toată lungimea și are protecție pentru bărbie; nu are glugă.</p>'
  '<p>Mânecile raglan și croiala lejeră lasă brațele libere, iar hanoracul se prinde de alte haine Reima prin sistemul Zip-in.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'laterale.'), ('Material', '100% poliester, elastic.'), ('Straturi', 'bun ca strat de mijloc.'))
  + '<p>Mărimile 104-164 sunt pentru copii de aproximativ 4-14 ani.</p>',
  [('model', 'Reima Hanorac cu fermoar pentru copii din polar Kerros roz 5200508A'), ('Polartec', 'Tehnologia Polartec® micro fleece contribuie la lejeritate, catifelare și respirabilitate'),
   ('uscare', 'Funcția de uscare rapidă'), ('cald', 'contribuie la menținerea căldurii'), ('fermoar', 'Fermoarul pe toată lungimea cu protecție pentru bărbie'),
   ('glugă', 'Modelul descheiat fără glugă'), ('raglan', 'Mâneci raglan'), ('croială', 'Croiala lejeră'), ('Zip-in', 'Compatibilitatea cu sistemul Reima Zip-in'),
   ('buzunare', 'Buzunarele laterale practice'), ('material', '100% Poliester'), ('elastic', 'Materialul elastic'), ('straturi', 'îmbrăcarea în straturi')],
  {'Model': 'Reima Kerros', 'Material': '100% poliester (Polartec micro fleece)', 'Caracteristici': 'fermoar întreg, Zip-in, uscare rapidă', 'Cod produs': '5200508A'})

w(13574,
  f'<p>Hanoracul cu glugă {REIMA} Muhkea violet este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} descheiat, din polar moale, cu uscare rapidă, cu model abstract și logo, în stil casual și streetwear. Gluga fixă are șnur și apără capul de frig și vânt.</p>'
  '<p>Croiala lejeră și materialul elastic lasă loc de mișcare, iar manșetele cu nervuri și tivul cu șnur țin căldura.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'laterale, cu închidere.'), ('Față', '100% poliester.'), ('Spate', '92% poliester, 8% elastan.'))
  + '<p>Mărimile 104-164 se potrivesc copiilor de cam 4-14 ani.</p>',
  [('model', 'Reima Hanorac cu glugă pentru copii din polar Muhkea violet 5200496A'), ('descheiat', 'Construcția descheiată'), ('polar', 'Materialul moale din polar'),
   ('uscare', 'Tricotul cu uscare rapidă'), ('model abstract', 'Modelul abstract și logo-ul mărcii'), ('stil', 'ținute casual și streetwear'),
   ('glugă', 'Gluga fixă cu șnur protejează capul de frig și vânt'), ('croială', 'Croiala lejeră'), ('elastic', 'Materialul elastic'),
   ('manșete', 'Manșetele cu nervuri și tivul cu șnur'), ('buzunare', 'Buzunarele laterale cu închidere'), ('față', '100% Poliester'), ('spate', '92% Poliester, 8% Elastan')],
  {'Model': 'Reima Muhkea', 'Material': 'polar din poliester, spate cu elastan', 'Caracteristici': 'glugă fixă cu șnur, uscare rapidă, buzunare cu închidere', 'Cod produs': '5200496A'})
