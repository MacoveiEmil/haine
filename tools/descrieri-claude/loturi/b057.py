import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
REIMA = A('/brand/reima/', 'Reima')

w(11514,
  f'<p>{TH} KG0KG09441 este un {A("/categorie/bluze-tricouri-hanorace/", "hanorac cu glugă pentru fete")}, bleumarin, din tricot moale cu bumbac, cu imprimeu cu logo Tommy Hilfiger și buzunar cangur. Nu e căptușit, deci e ușor, bun pentru zilele mai calde.</p>'
  '<p>Croiala e lejeră, relaxed fit, cu umerii coborâți pe mânecă, deci stă larg și vine comod și peste o bluză. Manșetele și baza cu nervuri țin hanoracul la locul lui.</p>'
  '<p>Material și închidere, pe rând:</p>'
  + L(('Glugă', 'integrată.'), ('Buzunar', 'cangur, pentru mâini.'), ('Material', '78% bumbac, 18% poliester, 4% elastan.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Hanorac cu glugă pentru copii cu bumbac bleumarin KG0KG09441'), ('tricot', 'Tricot moale cu bumbac'), ('logo', 'Imprimeu expresiv cu logo-ul Tommy Hilfiger'),
   ('buzunar', 'Buzunar tip cangur practic'), ('necăptușit', 'Fără căptușeală , favorizează lejeritatea și respirabilitatea, ideală pentru zilele mai calde'),
   ('croială', 'Croială lejeră relaxed fit'), ('umeri', 'Mâneci cu linia umerilor coborâtă'), ('nervuri', 'Manșete și bază cu nervuri'), ('glugă', 'Glugă integrată'),
   ('material', '78% Bumbac, 18% Poliester, 4% Elastan')],
  {'Model': 'Tommy Hilfiger KG0KG09441', 'Material': '78% bumbac, 18% poliester, 4% elastan', 'Caracteristici': 'glugă, buzunar cangur, relaxed fit', 'Cod produs': 'KG0KG09441'})

w(11529,
  f'<p>{A("/brand/konges-slojd/", "Konges Sløjd")} JUNO BOMBER JACKET KS105725 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă bomber unisex")}, verde, matlasată, ușor izolată, cu motiv animalier și membrană impermeabilă, pentru anotimpurile de tranziție. Finisajul BIONIC-FINISH® ECO o face rezistentă la apă și vânt.</p>'
  '<p>Croiala e lejeră, iar tivul are șnur elastic, care se strânge ca să nu intre aerul rece. Manșetele cu bordură elastică țin căldura în mâneci.</p>'
  '<p>Ce merită știut în plus:</p>'
  + L(('Închidere', 'fermoar.'), ('Căptușeală', '100% bumbac.'), ('Material', '100% nailon.'))
  + '<p>Mărimile 74 până la 134-140 sunt pentru copii de aproximativ 9 luni - 10 ani.</p>',
  [('model', 'Konges Sløjd Geacă bomber pentru copii JUNO BOMBER JACKET verde KS105725'), ('matlasat', 'Finisajul matlasat'), ('izolație', 'Izolația termică ușoară'),
   ('motiv', 'Modelul cu motiv animalier'), ('membrană', 'Membrană impermeabilă'), ('tranziție', 'anotimpurile de tranziție'),
   ('BIONIC', 'Finisajul BIONIC-FINISH® ECO susține rezistența la apă și vânt'), ('croială', 'Croiala lejeră'), ('tiv', 'Tivul cu șnur elastic'),
   ('manșete', 'Manșetele cu bordură elastică'), ('fermoar', 'Închiderea cu fermoar'), ('căptușeală', 'Căptușeala din bumbac'), ('material', '100% Nailon')],
  {'Model': 'Konges Sløjd JUNO BOMBER JACKET', 'Material': '100% nailon, căptușeală 100% bumbac', 'Caracteristici': 'bomber, membrană impermeabilă, BIONIC-FINISH® ECO, tiv cu șnur', 'Cod produs': 'KS105725'})

w(11538,
  f'<p>{A("/brand/lego/", "LEGO")} LWSAKU 612 11010985 este un set de {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă și pantaloni unisex")}, bleumarin, matlasat, căptușit, pentru sezonul de tranziție. E impermeabil, respirabil și rezistent la vânt, cu finisajul BIONIC-FINISH ECO® contra ploii.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile se termină cu manșetă. Genunchii și spatele pantalonilor sunt întărite, pentru joacă pe jos.</p>'
  '<p>Pentru zilele ude:</p>'
  + L(('Fermoar', 'pe toată lungimea, cu protecție pentru bărbie.'), ('Elemente reflectorizante', 'pentru vizibilitate seara.'), ('Buzunare', 'oblice, exterioare.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 92-140 sunt pentru copii de 2-10 ani, în mare.</p>',
  [('model', 'Lego Jachetă și pantaloni pentru copii LWSAKU 612 culoarea bleumarin, 11010985'), ('matlasat', 'Matlasat'), ('căptușeală', 'Model cu captuseala'), ('tranziție', 'Izolare: tranzitional'),
   ('impermeabil', 'Produsul este impermeabil, respirabil și rezistent la vânt'), ('BIONIC', 'Finisajul impermeabil BIONIC-FINISH ECO® oferă protecție împotriva ploii'),
   ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Finisaj din manseta'), ('întărituri', 'Întărituri în zona genunchilor și pe partea din spate'),
   ('fermoar', 'Închiderea cu fermoar pe toată lungimea cu apărătoare pentru bărbie'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('buzunare', 'Buzunare oblice exterioare'), ('fără glugă', 'Gluga: fara gluga')],
  {'Model': 'LEGO LWSAKU 612', 'Material': '100% poliester', 'Caracteristici': 'set geacă și pantaloni, impermeabil, reflectorizant, genunchi întăriți', 'Cod produs': '11010985'},
  notes=['E set de geacă și pantaloni, listat la Geci.'])

w(11547,
  f'<p>{A("/brand/geox/", "Geox")} ACTIVART ILLUMINUS x Looney Tunes J65LYA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} negri, ușori, cu profil scurt, din material textil și sintetic, cu personaje Looney Tunes și lumini încorporate pe care le pornește copilul dintr-un buton.</p>'
  '<p>Talpa exterioară din cauciuc are caneluri, deci prinde bine pe asfalt și rezistă mult. Vârful e rotund și lasă loc degetelor.</p>'
  '<p>Detaliile de material și talpă:</p>'
  + L(('Partea de sus', 'material sintetic și textil.'), ('Interior', 'material textil.'), ('Talpă', 'din cauciuc, cu caneluri.'))
  + '<p>Numerele 24-35 sunt pentru copii de 2-11 ani, de obicei.</p>',
  [('model', 'Geox Sneakers pentru copii ACTIVART ILLUMINUS x Looney Tunes culoarea negru, J65LYA.011CE'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu cel sintetic'), ('lumini', 'Model cu lumini incorporate, activate de un buton'),
   ('caneluri', 'Talpa exterioară din cauciuc cu caneluri este durabilă și oferă o tracțiune bună'), ('vârf', 'Varf rotund'), ('interior', 'Interiorul: Material textil')],
  {'Model': 'Geox ACTIVART ILLUMINUS x Looney Tunes', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini cu buton, talpă cu caneluri', 'Cod produs': 'J65LYA.011CE'})

w(11578,
  f'<p>{REIMA} Syddi 5100147C este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă 3 în 1 unisex")} (turcoaz pe site, neagră la magazin), pentru hiking, trekking, iarnă și tranziție. Membrana impermeabilă de 10 000 mm H2O, cusăturile lipite și construcția rezistentă la vânt o fac bună pentru ploaie puternică și zăpadă udă.</p>'
  '<p>Izolația sintetică ușoară ține de cald de la 0 la -20°C. Croiala e regulară, cu lungimea până la genunchi, deci acoperă și picioarele de frig.</p>'
  '<p>Pentru vreme schimbătoare, geaca are:</p>'
  + L(('Construcție', '3 în 1, compatibilă cu sistemul Reima Zip-in.'), ('Glugă', 'detașabilă, reglabilă.'), ('Buzunare', 'în față, cu fermoar.'), ('Respirabilitate', '7000 g/m²/24h.'))
  + '<p>Mărimile 104-164 sunt pentru copii de în jur de 4-14 ani.</p>',
  [('model', 'Reima Geacă 3 în 1 pentru copii Syddi neagră 5100147C'), ('3 în 1', 'Construcție 3 în 1'), ('activități', 'hiking și trekking'), ('membrană', 'Membrană impermeabilă'),
   ('impermeabil', 'Impermeabilitate 10 000 mm H2O , protejează împotriva ploii puternice și a zăpezii umede'), ('cusături', 'Toate cusăturile lipite'), ('vânt', 'Construcție rezistentă la vânt'),
   ('izolație', 'Izolație sintetică ușoară , asigură căldură în intervalul de temperaturi de la 0 la -20°C'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la genunchi'),
   ('Zip-in', 'Compatibilitate cu sistemul Reima Zip-in'), ('glugă', 'Glugă detașabilă , cu posibilitate de ajustare'), ('buzunare', 'Buzunare în față, cu fermoar'),
   ('respirabilitate', 'Respirabilitate 7000 g/m²/24h')],
  {'Model': 'Reima Syddi', 'Material': 'poliester acoperit cu TPU, poliamidă; umplutură poliester', 'Caracteristici': '3 în 1, 10 000 mm, cusături lipite, 0 la -20°C, Reima Zip-in', 'Cod produs': '5100147C'},
  notes=['Titlul de pe site spune turcoaz; magazinul spune neagră.'])

w(11592,
  f'<p>Cardiganul {TH} KG0KG09361 este o {A("/categorie/bluze-tricouri-hanorace/", "bluză cardigan pentru fete")}, bleumarin, din bumbac pur, cu model ajurat pointelle pe toată suprafața și volănașe, pentru zilele mai reci. Decolteul în V are logo brodat.</p>'
  '<p>Croiala e regulară, cu umerii ușor coborâți, iar mânecile lungi, mulate, au manșete elastice. Materialul elastic se adaptează la corp și nu încurcă la joacă.</p>'
  '<p>Alte detalii utile:</p>'
  + L(('Închidere', 'nasturi.'), ('Material', '100% bumbac.'), ('Model', 'ajurat pointelle, volănașe.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Cardigan pentru copii, din bumbac Bleumarin KG0KG09361'), ('bumbac', 'Bumbac pur'), ('ajurat', 'Model ajurat tip pointelle pe toată suprafața'),
   ('volănașe', 'Stil casual cu volănașe'), ('reci', 'zilele mai reci'), ('decolteu', 'Decolteu în V cu logo Tommy Hilfiger brodat'),
   ('croială', 'Croială regulară cu linia umerilor ușor coborâtă'), ('mâneci', 'Mânecă lungă, mulată cu manșete elastice'), ('elastic', 'Material elastic'),
   ('nasturi', 'Închidere cu nasturi')],
  {'Model': 'Tommy Hilfiger KG0KG09361', 'Material': '100% bumbac', 'Caracteristici': 'cardigan pointelle, volănașe, decolteu în V', 'Cod produs': 'KG0KG09361'})

w(11597,
  f'<p>{A("/brand/united-colors-of-benetton/", "United Colors of Benetton")} 2WU0CN017 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de puf pentru băieți")}, neagră, matlasată, umplută cu puf și pene (50/50), cu rezistență sporită la apă. E din linia Dress Safely, fără metale grele sau coloranți nocivi.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile lungi au manșetă elastică. Gulerul ridicat și gluga detașabilă apără de frig, iar fermoarul are clapă împotriva vântului.</p>'
  '<p>La purtat, contează și:</p>'
  + L(('Buzunare', 'două, laterale, cu capse.'), ('Certificări', 'RCS și ICEA.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 120-170 sunt pentru copii de 7-15 ani, de obicei.</p>',
  [('model', 'United Colors of Benetton Geacă de puf pentru copii culoarea negru, 2WU0CN017'), ('matlasat', 'material matlasat'), ('puf', '50% Pene, 50% Puf'),
   ('apă', 'Model cu rezistenta sporita la apa'), ('Dress Safely', 'Dress Safely este o linie de produse'), ('metale', 'metalele grele sau colorantii nocivi'),
   ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Mâneci lungi finisate cu o manșetă confortabilă, elastică'), ('guler, glugă', 'Gulerul ridicat și gluga detașabilă'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea, cu clapă rezistentă la vânt'), ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'),
   ('RCS', 'Standardul de revendicare reciclat (RCS)'), ('ICEA', 'Produs certificat de ICEA'), ('material', 'Materialul de baza: 100% Poliester')],
  {'Model': 'United Colors of Benetton 2WU0CN017', 'Material': '100% poliester; umplutură 50% pene, 50% puf', 'Caracteristici': 'puf, glugă detașabilă, Dress Safely, rezistentă la apă', 'Cod produs': '2WU0CN017'},
  notes=['Mărimile sunt italiene; magazinul atenționează că pot diferi de cele europene.', 'Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(11601,
  f'<p>{A("/brand/primigi/", "Primigi")} PNL 24001 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete de iarnă pentru bebeluși")}, bleumarin, din piele întoarsă, cu interior textil izolat, care ține căldura în zilele reci. Sunt făcute după tehnologia Primigi × SIPeP, creată cu podologii.</p>'
  '<p>Scaiul permite încălțatul rapid și ajustarea pe picior, iar vârful rotund, moale, lasă degetele să se miște liber. Călcâiul întărit ține piciorul stabil.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Talpă', 'din cauciuc, pentru zăpadă și gheață.'.replace(', pentru zăpadă și gheață', '')), ('Interior', 'material textil, izolat.'), ('Partea de sus', 'piele întoarsă.'))
  + '<p>Numerele 19-30 sunt pentru copii de în jur de 1-7 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii din piele întoarsă bleumarin PNL 24001'), ('piele întoarsă', 'Partea superioară din piele întoarsă'),
   ('izolat', 'Interior izolat din material textil care favorizează menținerea căldurii în zilele reci'), ('SIPeP', 'Tehnologia Primigi × SIPeP , creată în colaborare cu podologii'),
   ('scai', 'Închidere cu scai care facilitează încălțarea și descălțarea rapidă a ghetelor, precum și ajustarea'), ('vârf', 'Vârf rotund, moale'), ('călcâi', 'Călcâi întărit'),
   ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Primigi PNL 24001', 'Material': 'piele întoarsă, interior textil izolat, talpă din cauciuc', 'Caracteristici': 'scai, izolate, Primigi × SIPeP', 'Cod produs': 'PNL 24001'})

w(11604,
  f'<p>Ghetele de iarnă {A("/brand/geox/", "Geox")} OMAR B462DC sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete pentru bebeluși")} negre, ușor izolate, din piele naturală și piele întoarsă rezistente la înmuiere, cu interior din lână. Talpa Geox Respira, în trei straturi perforate, ventilează gheata.</p>'
  '<p>Velcro-ul se închide repede, iar partea de sus ridicată rigidizează glezna pe teren denivelat. Contrafortul rigid ține piciorul în gheată.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Light Flexy', 'branț care lasă piciorul să se miște.'), ('Talpă', 'exterioară, din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 20-27 sunt pentru copii de în jur de 1-4 ani.</p>',
  [('model', 'Geox Ghete de iarnă pentru copii din piele OMAR culoarea negru, B462DC.04322'), ('izolare', 'Izolare ușoară'), ('material', 'combinația pielii naturale cu pielea intoarsa'),
   ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'), ('lână', 'Un model cu interior din lână'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('teren', 'suprafețe neuniforme'),
   ('călcâi', 'Contorul de călcâi rigid'), ('vârf', 'Cutie rotunda, intarita'), ('Light Flexy', 'Light Flexy Sistem de brant pentru libertatea de miscare'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox OMAR', 'Material': 'piele naturală și piele întoarsă, interior din lână, talpă din cauciuc', 'Caracteristici': 'ușor izolate, velcro, Geox Respira, Light Flexy', 'Cod produs': 'B462DC.04322'})

w(11616,
  f'<p>Sandalele {REIMA} Talsi 5400132B sunt {A("/categorie/unisex-incaltaminte-sandale/", "sandale cu degetele acoperite unisex")}, negre, din piele sintetică și material textil. Vârful închis apără degetele la joacă și la explorări, iar talpa din spumă e ușoară și flexibilă.</p>'
  '<p>Se închid cu șnur elastic cu opritor, care se ajustează repede și precis pe picior. Branțul anatomic ține piciorul bine așezat.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Partea de sus', '50% textil, 50% sintetic.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'din spumă.'))
  + '<p>Numerele 29-38 sunt pentru copii de la 4 ani în sus, în general.</p>',
  [('model', 'Reima Sandale cu degetele acoperite pentru copii Talsi negre 5400132B'), ('material', 'Partea superioară din piele sintetică și material textil'),
   ('vârf', 'Vârf închis – protecție suplimentară împotriva accidentărilor'), ('talpă', 'Talpă din spumă – lejeritate și flexibilitate'),
   ('șnur', 'Închidere cu șnur elastic și opritor – permite o ajustare rapidă și precisă'), ('branț', 'Branț anatomic'), ('compoziție', '50% Material textil, 50% Material sintetic'),
   ('interior', 'Interior căptușit cu material textil')],
  {'Model': 'Reima Talsi', 'Material': 'piele sintetică și textil, interior textil, talpă din spumă', 'Caracteristici': 'vârf închis, șnur elastic cu opritor, branț anatomic', 'Cod produs': '5400132B'})
