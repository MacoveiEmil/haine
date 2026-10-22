import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9191,
  f'<p>{GEOX} ECLYPER sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} albi, cu profil scurt, din imitație de piele și material sintetic. Talpa are tehnologia patentată GEOX Respira™, cu membrană microporoasă, care elimină umezeala.</p>'
  '<p>Închiderea cu arici îl lasă pe copil să se încalțe singur, iar gulerul ușor întărit se așază pe gleznă fără să strângă. Se poartă la ținute casual și streetwear.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'ușor întărit.'), ('Căptușeală', 'textilă, moale.'), ('Material', 'imitație de piele și sintetic.'))
  + '<p>Numerele 20-27 sunt pentru copii de aproximativ 1-4 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi B665MA.000BC'), ('profil', 'cu profil scurt'), ('material', 'Imitația de piele și materialul sintetic'),
   ('Respira', 'Talpă patentată cu membrană microporoasă'), ('arici', 'Închidere practică cu arici'), ('guler', 'Gulerul superior ușor întărit'),
   ('casual', 'ținute casual și streetwear'), ('talpă', 'Construcția plată asigură o bună aderență'), ('călcâi', 'Călcâi ușor întărit'), ('căptușeală', 'Căptușeala din material textil')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele și sintetic, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'GEOX Respira™, arici, profil scurt', 'Cod produs': 'B665MA.000BC'})

w(9192,
  f'<p>{A("/brand/lego/", "LEGO")} LWJERI 701 este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă de iarnă pentru bebeluși")} și copii mici, roz, izolată, cu confort termic declarat între -5°C și -20°C. Toate cusăturile sunt lipite, iar impermeabilitatea e de 10000 mm, deci ține la zăpadă și ploaie.</p>'
  '<p>Fermoarul pe toată lungimea are apărătoare pentru bărbie, ca să nu zgârie fața copilului, iar gulerul ridicat și gluga detașabilă apără de frig.</p>'
  '<p>Mai are:</p>'
  + L(('Elemente reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Respirabilitate', '6000 g/m2/24h.'), ('Tratament', 'BIONIC-FINISH ECO, hidrofob.'), ('Buzunare', 'două, laterale.'))
  + '<p>Mărimile 80-104 se potrivesc copiilor de cam 1-4 ani.</p>',
  [('model', 'Lego Geacă copii LWJERI 701 culoarea roz, 11010977'), ('izolat', 'Model izolat cu captuseala'), ('temperatură', 'Oferă confort termic de la -5°C până la -20°C'),
   ('cusături', 'Toate cusăturile sunt lipite'), ('impermeabilitate', 'Impermeabilitate: 10000 mm/m2/24h'), ('bărbie', 'apărătoare pentru bărbie'),
   ('glugă, guler', 'Gulerul ridicat și gluga detașabilă'), ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'), ('respirabilitate', 'Respirabilitate: 6000 g/m2/24h'),
   ('BIONIC', 'BIONIC-FINISH ECO este o finisare hidrofoba'), ('buzunare', 'Două buzunare laterale'), ('iarnă', 'Sporturi de iarnă')],
  {'Model': 'LEGO LWJERI 701', 'Material': '100% poliester', 'Caracteristici': 'izolată, -5°C...-20°C, cusături lipite, 10000 mm, reflectorizante', 'Cod produs': '11010977'})

w(9194,
  f'<p>{A("/brand/guess/", "GUESS")} L6YL01 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, verde, uni, cu izolație sintetică medie și căptușeală completă, pentru zilele mai reci de tranziție și activitățile în aer liber.</p>'
  '<p>Croiala e regulară și ajunge până la șolduri, iar manșetele și tivul cu nervuri o strâng la încheieturi și jos, ca să stea bine pe corp.</p>'
  '<p>Detaliile:</p>'
  + L(('Glugă', 'integrată, cu guler ridicat.'), ('Buzunare', 'laterale, tip slip-on.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester.'))
  + '<p>Mărimile de pe site, de la 122-125 la 175, sunt pentru copii de aproximativ 7-16 ani.</p>',
  [('cod', 'Geacă petrecută pentru copii verde L6YL01 W2655'), ('matlasat', 'Structura matlasată'), ('izolație', 'izolația termică sintetică medie'), ('căptușeală', 'Căptușeală completă'),
   ('tranziție', 'sezonul de tranziție'), ('aer liber', 'activități în aer liber'), ('croială', 'Croiala regulară'), ('lungime', 'Lungimea până la șolduri'),
   ('nervuri', 'Manșete și tiv cu nervuri'), ('glugă', 'Glugă integrată cu guler ridicat'), ('buzunare', 'Buzunare laterale tip slip-on'), ('fermoar', 'Închidere cu fermoar'),
   ('uni', 'Model uni'), ('material', '100% Poliester')],
  {'Model': 'GUESS L6YL01', 'Material': '100% poliester, izolație sintetică medie', 'Caracteristici': 'matlasată, glugă integrată, manșete și tiv cu nervuri', 'Cod produs': 'L6YL01.W2655'})

w(9195,
  f'<p>{GEOX} FLEXYPER sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")}, albaștri, din piele întoarsă, piele naturală și material textil, ușori și făcuți pentru purtat zilnic. Au sistemul Geox Respira în talpă și un finisaj antibacterian în interior, care previne mirosurile.</p>'
  '<p>Aricii fac încălțatul rapid, iar branțul din piele previne frecarea; profilul e scurt, sub gleznă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Branț', 'din piele.'), ('Interior', 'textil și piele naturală, antibacterian.'))
  + '<p>Numerele 20-27 se potrivesc în mare copiilor de 1-4 ani.</p>',
  [('model', 'Sneakers pentru copii FLEXYPER B656GC.01422'), ('material', 'combinație de piele întoarsă, piele naturală și material textil'), ('zilnic', 'ideal pentru purtarea zilnică'),
   RESPIRA, ('antibacterian', 'Finisajul antibacterian din interiorul încălțămintei'), ('arici', 'Închiderea cu velcro'), ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'),
   ('profil', 'Înălțime: mic de statură'), ('talpă', 'Talpa exterioară din cauciuc'), ('interior', 'Interiorul: Material textil, Piele naturala'), ('culoare', 'albastru')],
  {'Model': 'Geox FLEXYPER', 'Material': 'piele întoarsă, piele naturală și textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, finisaj antibacterian, arici, branț din piele', 'Cod produs': 'B656GC.01422'},
  notes=['Titlul de pe site nu are culoare; magazinul arată albastru.'])

w(9199,
  f'<p>{A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IB0IB02569 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, albastră, din poliester neted, căptușită, cu glugă și guler ridicat. Se poartă primăvara și toamna, peste un hanorac.</p>'
  '<p>Croiala e simplă, iar mânecile se termină cu bandă elastică, care le strânge pe încheieturi, ca să nu intre vântul. Căptușeala face geaca ușor de îmbrăcat.</p>'
  '<p>Ce mai are:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'cu închidere.'), ('Glugă', 'are.'), ('Material', '100% poliester.'))
  + '<p>Pe site sunt mărimile 128-170, de obicei pentru copii de 8-15 ani.</p>',
  [('cod', 'IB0IB02569'), ('culoare', 'albastru'), ('neted', 'Material neted'), ('căptușeală', 'Captuseala: cu captuseala'), ('tranziție', 'Izolare: tranzitional'),
   ('glugă', 'Model cu gluga'), ('guler', 'Guler ridicat'), ('croială', 'Tăiere simplă'), ('elastic', 'Mâneci finisate cu o coadă elastică'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare incheiate'), ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans IB0IB02569', 'Material': '100% poliester', 'Caracteristici': 'de tranziție, căptușită, glugă, guler ridicat, manșete elastice', 'Cod produs': 'IB0IB02569'},
  notes=['Titlul de pe site nu are culoare; magazinul arată albastru.'])

w(9220,
  f'<p>{A("/brand/emporio-armani/", "Emporio Armani")} EB000097 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă subțire pentru băieți")}, bleumarin, din poliamidă netedă, fără izolație și fără căptușeală, cu glugă. E pentru vremea de tranziție, ca strat exterior peste un hanorac.</p>'
  '<p>Mânecile și marginea de jos sunt finisate cu bătături, care o strâng la încheieturi și jos. Magazinul precizează că mărimile sunt italiene, convertite la cele europene.</p>'
  '<p>Detaliile:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Glugă', 'are.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 130-176 sunt pentru copii între aproximativ 8 și 16 ani.</p>',
  [('cod', 'EB000097 AF12995'), ('culoare', 'culoarea albastru marin'), ('neizolat', 'Model neizolat fara captuseala'), ('neted', 'material neted'), ('glugă', 'Gluga: cu gluga'),
   ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('mărimi italiene', 'Dimensiunile disponibile sunt cele ale producatorul italian'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material', '100% Poliamida')],
  {'Model': 'Emporio Armani EB000097', 'Material': '100% poliamidă', 'Caracteristici': 'subțire, fără căptușeală, glugă, bătături la mâneci și bază', 'Cod produs': 'EB000097'},
  notes=['Mărimi italiene convertite la europene (după magazin).'])

w(9242,
  f'<p>{A("/brand/primigi/", "Primigi")} PMG GTX 89152 sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")}, argintii, izolate, din material textil și piele întoarsă, cu membrana Gore-Tex®, impermeabilă și rezistentă la vânt. Sunt făcute pentru zăpadă și joaca afară pe frig.</p>'
  '<p>Partea de sus urcă pe gleznă, iar circumferința se reglează cu șnururi cu opritoare, ca zăpada să nu intre pe sus; se închid cu scai, iar bucla de la spate ajută la încălțat.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Shock Absorber', 'punct de absorbție în talpă.'), ('Talpă', 'exterioară, din cauciuc.'), ('Vârf', 'rotund.'), ('Interior', 'textil.'))
  + '<p>Numerele 24-29 se potrivesc copiilor de aproximativ 2-5 ani.</p>',
  [('model', 'Primigi Cizme de iarnă copii culoarea argintiu, PMG GTX 89152'), ('zăpadă', 'Cizme de zăpadă pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinația materialului textil cu pielea întoarsă'), ('Gore-Tex', 'Gore-Tex® - o membrană care combină caracteristicile de impermeabilitate, rezistență la vânt'),
   ('gleznă', 'Partea superioară ridicată'), ('șnururi', 'Reglarea circumferinței superioare cu șnururi cu opritoare'), ('scai', 'Fixare: cu scai'), ('buclă', 'Bucla de la spate'),
   ('Shock Absorber', 'Primitor Shock Absorber'), ('talpă', 'Talpa exterioară din cauciuc'), ('vârf', 'Varf rotund'), ('interior', 'Interiorul textil')],
  {'Model': 'Primigi PMG GTX 89152', 'Material': 'textil și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'izolate, Gore-Tex®, șnur cu opritor, scai, Shock Absorber', 'Cod produs': '89152'})

w(9247,
  f'<p>{GEOX} ECLYPER J45LRA sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, în stil sport-casual, din material textil și sintetic, cu talpa perforată Geox Respira, care ține piciorul uscat. Se poartă la ținute sportive și casual, toată ziua.</p>'
  '<p>Partea de sus ajunge până la gleznă, iar aricii se prind repede și îl lasă pe copil să se încalțe singur; contrefortul e ușor rigidizat.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Căptușeală', 'textilă.'), ('Material', 'textil și sintetic, rezistent la uzură.'))
  + '<p>Numerele 28-39 sunt pentru copii de la aproximativ 4 ani în sus.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii roz J45LRA.0QDBC'), ('stil', 'stilul sport-casual'), ('material', 'Combinația de material textil și sintetic'),
   ('Respira', 'Talpa special perforată'), ('uscat', 'menținându-l uscat'), ('gleznă', 'Construcția care ajunge până la gleznă'), ('arici', 'Închidere practică cu velcro'),
   ('contrefort', 'Contrefort ușor rigidizat'), ('talpă', 'Construcția plată din cauciuc'), ('căptușeală', 'Căptușeala din material textil'), ('uzură', 'rezistentă la uzura zilnică')],
  {'Model': 'Geox ECLYPER J45LRA', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici, până la gleznă', 'Cod produs': 'J45LRA.0QDBC'})

w(9248,
  f'<p>{GEOX} ECLYPER B555MA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, din material sintetic și textil, ușori, cu membrana impermeabilă Geox Respira. Profilul e scurt, iar modelul e făcut pentru purtat zilnic.</p>'
  '<p>Vârful e rotund și ușor rigid, deci degetele stau liber, fără să fie strânse, iar contorul de călcâi rigid ține piciorul în pantof. Aricii se prind repede.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Interior', 'textil.'), ('Închidere', 'arici.'))
  + '<p>Numerele 20-27 sunt pentru copii de pe la 1 până pe la 4 ani.</p>',
  [('model', 'Sneakers pentru copii ECLYPER culoarea roz, B555MA.054AJ'), ('material', 'combinația materialului sintetic cu cel textil'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('membrană', 'Membrana unica si impermeabila a tehnologiei Geox Respira'), ('profil', 'Înălțime: mic de statură'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('degete', 'degetele se pot aranja liber'), ('călcâi', 'Contorul de călcâi rigid'), ('arici', 'Închiderea cu velcro'), ('talpă', 'Talpa exterioară din cauciuc'),
   ('interior', 'Interiorul textil')],
  {'Model': 'Geox ECLYPER B555MA', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'membrană Geox Respira, arici, vârf rotund', 'Cod produs': 'B555MA.054AJ'})

w(9249,
  f'<p>{A("/brand/reima/", "Reima")} Sevetti este o {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopetă de iarnă unisex")}, roz, dintr-o singură bucată, cu membrana ReimaTec și cusături lipite, impermeabilitate de 12000 mm și izolație sintetică medie. E făcută pentru joaca în zăpadă și pentru toamnele și primăverile ude.</p>'
  '<p>Talia are reglaj interior, deci se strânge pe un copil mai slab, iar prinderile de la glezne țin salopeta pe loc, ca să nu urce când copilul se joacă.</p>'
  '<p>Pentru joaca afară:</p>'
  + L(('Glugă', 'detașabilă.'), ('Elemente reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Respirabilitate', '7000 g/m²/24h.'), ('Țesătură', 'rezistentă la abraziune, peste 30 000 de cicluri.'))
  + '<p>Mărimile 92-128 sunt pentru copii de cam 2-8 ani.</p>',
  [('model', 'Reima Salopetă pentru copii Sevetti roz 5100124A'), ('o bucată', 'piesă de îmbrăcăminte de protecție dintr-o singură bucată'),
   ('ReimaTec', 'Tehnologia ReimaTec – membrană PU cu cusături lipite'), ('impermeabilitate', 'Impermeabilitate 12000 mm H2O'), ('izolație', 'Izolație sintetică medie'),
   ('zăpadă', 'joaca de iarnă în zăpadă'), ('talie', 'Reglare internă în talie'), ('glezne', 'Prinderi practice la glezne'), ('glugă', 'Glugă detașabilă'),
   ('reflectorizante', 'Elemente reflectorizante'), ('respirabilitate', 'Respirabilitate 7000 g/m²/24h'), ('abraziune', '30 000 de cicluri')],
  {'Model': 'Reima Sevetti', 'Material': 'poliester acoperit cu poliuretan, izolație sintetică', 'Caracteristici': 'ReimaTec, cusături lipite, 12000 mm, glugă detașabilă, reflectorizante', 'Cod produs': '5100124A'})
print('lot 17 scris')
