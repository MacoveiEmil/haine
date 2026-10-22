import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
CKJ = A('/brand/calvin-klein-jeans/', 'Calvin Klein Jeans')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
PRIM = A('/brand/primigi/', 'Primigi')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')
CURAT = ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')

w(12755,
  f'<p>Geaca {CKJ} neagră este o {A("/categorie/geci-jachete/", "geacă pentru fete")} izolată, matlasată, cu glugă și căptușeală, parțial din poliester reciclat, cu fibră REPREVE făcută din sticle de plastic reciclate. Interiorul gulerului e căptușit cu fleece moale.</p>'
  '<p>Mânecile și tivul au margine elastică, care ține vântul afară. Se închide cu fermoar.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Buzunare', 'exterioare, cu închidere.'), ('Buzunar interior', 'cu velcro.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-176 sunt pentru fete de aproximativ 8-16 ani; la 128 cm geaca are 50 cm lungime.</p>',
  [('model', 'Calvin Klein Jeans Geaca copii culoarea negru'), ('izolat', 'Model izolat confecționat din din material matlasat'), ('glugă', 'Gluga: cu gluga'),
   ('căptușeală', 'Captuseala: cu captuseala'), ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('REPREVE', 'Fibra REPREVE este fabricata din sticle de plastic reciclate'),
   ('fleece', 'Partea interioara a gulerului este captusita cu un material moale, fleece'), ('margini', 'Mânecile și marginea inferioară finisate cu bătături'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'), ('interior', 'Buzunar interior cu velcro'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 50 cm')],
  {'Model': 'Calvin Klein Jeans (geacă matlasată)', 'Material': '100% poliester, parțial reciclat (REPREVE)', 'Caracteristici': 'izolată, glugă, guler cu fleece, buzunar interior', 'Cod produs': ''})

w(12757,
  f'<p>Geaca {CKJ} IB0IB02639 neagră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} de tranziție, neizolată, din material imprimat, din poliester reciclat. Gulerul ridicat și gluga detașabilă apără de vânt și de frigul ușor.</p>'
  '<p>Are un strat de căptușeală care o face mai plăcută la purtare, iar mânecile și tivul se termină cu margine elastică.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Croială', 'simplă, dreaptă.'), ('Glugă', 'detașabilă.'))
  + '<p>Au mai rămas mărimile 104-116, pentru băieți de cam 4-6 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă copii culoarea negru, IB0IB02639'), ('tranziție', 'Izolare: tranzitional'), ('neizolat', 'Model neizolat confecționat din material imprimat'),
   ('reciclat', 'Produsul contine materiale realizate din fibre reciclate'), ('glugă', 'Gulerul ridicat și gluga detașabilă oferă protecție suplimentară împotriva frigului'),
   ('căptușeală', 'Un strat suplimentar de material sub formă de căptușeală'), ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică confortabilă'),
   ('material', '100% Poliester reciclat'), ('croială', 'Tăiere simplă, fără blocare')],
  {'Model': 'Calvin Klein Jeans IB0IB02639', 'Material': '100% poliester reciclat', 'Caracteristici': 'neizolată, glugă detașabilă, margini elastice', 'Cod produs': 'IB0IB02639'})

w(12760,
  f'<p>{GEOX} PERTH J367RE în albastru sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} casual-streetwear, cu partea de sus din imitație de piele, ușor de întreținut. Șireturile elastice nu trebuie legate, iar aricii fac încălțatul rapid.</p>'
  '<p>Gulerul moale cuprinde glezna, iar călcâiul întărit ține piciorul în poziție corectă. Tehnologia GEOX Respira scoate umiditatea spre exterior.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Interior', '100% material textil, plăcut la atingere.'), ('Talpă', 'din cauciuc, cu profil plat.'), ('Închidere', 'șireturi elastice și arici.'))
  + '<p>Numerele 36-41 se potrivesc băieților de la vreo 12 ani în sus, orientativ.</p>',
  [('model', 'Geox PERTH sneakers pentru copii albastru J367RE.0BCFU'), ('stil', 'Caracterul lor casual și streetwear'), ('imitație', 'Partea superioară din imitație de piele prezintă un aspect estetic, ușor de întreținut'),
   ('șireturi', 'Șireturi elastice susțin ajustarea pantofului la picior, fără a necesita legare'), ('arici', 'Închiderea practică cu arici'),
   ('guler', 'Gulerul moale al părții superioare îmbrățișează delicat glezna'), ('călcâi', 'Călcâiul întărit stabilizează piciorul copilului'),
   ('Respira', 'Tehnologia GEOX Respira™ asigură respirabilitatea piciorului, eliminând umiditatea spre exterior'), ('interior', '100% Material textil'),
   ('talpă', 'Talpa de cauciuc cu profil plat')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice și arici', 'Cod produs': 'J367RE.0BCFU'})

w(12764,
  f'<p>Pentru băieții mai mici, {GEOX} PERTH J367RE vin în bleumarin și în numerele 28-35: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu profil scurt și talpă cu membrană microporoasă, care lasă umezeala să iasă și oprește apa să intre. Fața din imitație de piele se îngrijește ușor.</p>'
  '<p>Combinația de arici și șireturi elastice permite încălțatul rapid și reglajul după picior. Gulerul moale nu irită glezna.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Căptușeală', 'textilă, moale.'), ('Călcâi', 'întărit, pentru pas sigur.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Se potrivesc băieților de în jur de 4-11 ani.</p>',
  [('model', 'Geox PERTH sneakers pentru copii bleumarin J367RE.0MEMS'), ('profil', 'cu profil scurt'), ('membrană', 'Talpa respirabilă cu membrană microporoasă facilitează eliminarea umidității la exterior'),
   ('apă', 'protejează interiorul pantofului împotriva pătrunderii apei'), ('imitație', 'Partea superioară din imitație de piele oferă încălțămintei un aspect estetic și facilitează îngrijirea acesteia'),
   ('arici', 'Închiderea practică cu arici permite încălțarea și descălțarea rapidă'), ('șireturi', 'Șireturi elastice ajută la ajustarea pantofului'),
   ('guler', 'Gulerul moale al părții superioare minimizează riscul de iritații'), ('căptușeală', 'Căptușeala textilă moale'), ('călcâi', 'Călcâiul întărit stabilizează piciorul, ceea ce permite un pas mai sigur'),
   ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici și șireturi elastice', 'Cod produs': 'J367RE.0MEMS'})

w(12767,
  f'<p>Adidașii {TH} T3X9-34355 albi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil jos, din piele ecologică și imitație de piele întoarsă, ușori, pentru purtarea zilnică. Se leagă cu șiret clasic, care se reglează după picior.</p>'
  '<p>Vârful e rigidizat, iar contrafortul de la călcâi sprijină glezna și călcâiul.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil, se păstrează curat ușor.'), ('Talpă exterioară', 'din cauciuc, durabilă.'), ('Partea de sus', 'material sintetic.'))
  + '<p>Numerele 35-41 sunt pentru copii de la aproximativ 10 ani în sus; la 37 branțul are 23,5 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea alb, T3X9-34355'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația de piele ecologică cu imitatia de piele întoarsă'),
   ('ușor', 'Model ușor și confortabil'), ('șiret', 'Șiretul clasic permite ajustarea individuală a piciorului'), ('vârf', 'Varf rigidizat'),
   ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), CURAT, TALPA, ('gamba', 'Gamba: Material sintetic'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 23,5 cm')],
  {'Model': 'Tommy Hilfiger T3X9-34355', 'Material': 'piele ecologică și imitație de piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'șiret, vârf rigidizat', 'Cod produs': 'T3X9-34355'})

w(12769,
  f'<p>Tot T3X9-34355, dar în bleumarin: {TH} face aceiași {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} joși, cu fața din imitație de piele întoarsă combinată cu piele ecologică. Șiretul clasic permite strângerea exactă, iar vârful rigidizat ține forma pantofului.</p>'
  '<p>La spate, contrafortul rigidizat susține călcâiul și glezna. Interiorul textil se curăță ușor.</p>'
  '<p>Materialele folosite:</p>'
  + L(('Exterior', 'sintetic.'), ('Căptușeală', 'textilă.'), ('Talpă', 'cauciuc rezistent la deteriorare.'))
  + '<p>Gama 35-41 e gândită pentru copii de pe la 10 ani în sus. Branțul măsoară 23,5 cm la numărul 37.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea bleumarin, T3X9-34355'), ('material', 'combinația de piele ecologică cu imitatia de piele întoarsă'),
   ('profil', 'Înălțime: mic de statură'), ('șiret', 'Șiretul clasic permite ajustarea individuală a piciorului'), ('vârf', 'Varf rigidizat'),
   ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), CURAT, ('gamba', 'Gamba: Material sintetic'), TALPA,
   ('lungime', 'Lungimea brantului pentru marimea este de: 23,5 cm')],
  {'Model': 'Tommy Hilfiger T3X9-34355', 'Material': 'piele ecologică și imitație de piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'șiret, vârf rigidizat', 'Cod produs': 'T3X9-34355'})

w(12771,
  f'<p>Ghetele de iarnă {PRIM} 23791 roz sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} înalte, cu interior izolat termic și membrană GORE-TEX, care apără de umezeală și vânt și lasă piciorul să respire. Partea de sus e din piele întoarsă și material textil.</p>'
  '<p>Aricii fac încălțatul și descălțatul rapid, iar vârful rotund, rigidizat, apără degetele. Călcâiul întărit ține piciorul în poziție corectă.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă exterioară', 'din cauciuc, pentru drumurile de iarnă.'), ('Călcâi', 'întărit.'), ('Interior', 'textil, izolat.'))
  + '<p>Numerele 25-30 se potrivesc fetițelor de aproximativ 2-7 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii roz PWIGT 23791'), ('înalt', 'încălțăminte înaltă pentru copii'), ('izolat', 'Interior izolat termic'),
   ('GORE-TEX', 'Membrana GORE-TEX® ajută la protecția împotriva umezelii și a vântului'), ('material', 'Partea superioară, din combinație de piele întoarsă și material textil'),
   ('arici', 'Închidere practică cu arici , facilitează încălțarea și descălțarea rapidă'), ('vârf', 'Vârful rotund, rigidizat , asigură protecția degetelor'),
   ('talpă', 'Talpa exterioară din cauciuc asigură aderența la sol, ceea ce este util pe drumurile de iarnă'), ('călcâi', 'Călcâiul întărit'), ('interior', 'Material textil')],
  {'Model': 'Primigi 23791', 'Material': 'piele întoarsă și textil, interior izolat, talpă din cauciuc', 'Caracteristici': 'GORE-TEX, arici, izolate termic', 'Cod produs': 'PWIGT 23791'})

w(12780,
  f'<p>Geaca {A("/brand/guess/", "GUESS")} J6YL01, în negru, este o {A("/categorie/geci-jachete/", "geacă pentru fete")} matlasată din țesătură rezistentă, cu izolație sintetică medie care o ține ușoară, pentru toamnă și primăvară. Are glugă integrată și un model decorat cu logo Guess.</p>'
  '<p>Închiderea cu fermoar și capse e rapidă, iar bordurile elastice de la bază și de la manșete țin frigul afară.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'completă.'), ('Buzunare', 'slip-on, pe laterale.'), ('Lungime', 'până la șolduri.'), ('Compoziție', 'integral poliester.'))
  + '<p>Mărimile 122-125 până la 167 sunt pentru fete de cam 7-14 ani.</p>',
  [('model', 'Guess Geacă petrecută pentru copii neagră J6YL01 W2607'), ('matlasat', 'Geaca matlasată Guess'), ('țesătură', 'Țesătură rezistentă'),
   ('izolație', 'Izolație sintetică medie – contribuie la menținerea căldurii în zilele mai reci, păstrând lejeritatea'), ('tranziție', 'sezonul de tranziție'),
   ('glugă', 'Glugă integrată'), ('logo', 'Model decorat cu logo'), ('închidere', 'Închidere cu fermoar și capse'), ('borduri', 'Borduri elastice la bază și la manșete'),
   ('căptușeală', 'Căptușeală completă'), ('buzunare', 'Buzunare laterale tip slip-on'), ('lungime', 'Lungime până la șolduri'), ('material', '100% Poliester')],
  {'Model': 'GUESS J6YL01', 'Material': '100% poliester, izolație sintetică medie', 'Caracteristici': 'matlasată, glugă integrată, fermoar și capse', 'Cod produs': 'J6YL01 W2607'})

w(12788,
  f'<p>Cizmele de iarnă {PRIM} PPE GTX 89346 verzi sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme pentru băieți")} izolate, din material textil și piele ecologică, cu membrană GORE-TEX contra apei și vântului, care previne și supraîncălzirea. Interiorul are lână, iar piesele metalice nu conțin nichel.</p>'
  '<p>Șireturile rapide cu opritor și bucla de la spate fac încălțatul ușor. Cutia lată nu ciupește degetele.</p>'
  '<p>Talpa și branțul:</p>'
  + L(('Primigi Sky Effect', 'branț căptușit cu piele moale.'), ('Shock Absorber', 'talpă care protejează articulațiile.'), ('Talpă', 'EVA ușoară și cauciuc cu caneluri.'), ('Inserție', 'textilă, detașabilă.'))
  + '<p>Numerele 36-39 sunt pentru băieți de la aproximativ 12 ani în sus.</p>',
  [('model', 'Primigi Cizme de iarnă pentru copii culoarea verde, PPE GTX 89346'), ('izolat', 'Model Izolat confecționat din combinația materialului textil cu pielea ecologică'),
   ('GORE-TEX', 'Membrana GORE-TEX® utilizată în acest model oferă un nivel ridicat de impermeabilitate și protecție împotriva vântului'), ('supraîncălzire', 'ceea ce previne supraîncălzirea'),
   ('lână', 'Lana, Material textil'), ('nichel', 'Piesele metalice nu conțin nichel'), ('șireturi', 'Sistemul rapid de șireturi cu comutatoare'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('Sky Effect', 'Primigi Sky Effect - acest brant este creat cu materiale de cea mai buna calitate, captusit in piele moale'), ('Shock Absorber', 'Primitor Shock Absorber - o talpa cu punct de absorbtie a socurilor. Amelioreaza si protejeaza articulatiile'),
   ('EVA', 'Talpa intermediară este realizată din spumă EVA ușoară'), ('caneluri', 'Talpa exterioară din cauciuc cu caneluri'), ('inserție', 'Inserție textilă detașabilă')],
  {'Model': 'Primigi 89346', 'Material': 'textil și piele ecologică, interior cu lână, talpă EVA și cauciuc', 'Caracteristici': 'GORE-TEX, izolate, Sky Effect, Shock Absorber', 'Cod produs': 'PPE GTX 89346'})

w(12791,
  f'<p>Adidașii {TH} T3X9-35235 bej sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt și guler ușor întărit, din imitație de piele ușor de curățat, pentru ținute casual de oraș. Se leagă cu șireturi clasice, care se reglează după forma piciorului.</p>'
  '<p>Talpa din cauciuc, cu profil plat și grosime de 2-4 cm, ține bine pe diverse suprafețe, iar călcâiul întărit ține piciorul în pantof.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Interior', 'material textil.'), ('Partea de sus', 'material sintetic.'), ('Închidere', 'șireturi.'))
  + '<p>Numerele 35-41 se potrivesc copiilor de la aproximativ 10 ani în sus.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bej T3X9-35235'), ('profil', 'Profilul scurt al părții superioare și gulerul ușor întărit'),
   ('imitație', 'Materialul exterior din imitație de piele este ușor de curățat'), ('urban', 'ținutele urbane'), ('șireturi', 'Sistemul clasic de înșiretare permite ajustarea individuală'),
   ('talpă', 'Talpa din cauciuc cu profil plat favorizează aderența pe diverse suprafețe'), ('grosime', 'Grosimea tălpii de 2-4 cm'), ('călcâi', 'Călcâiul întărit'),
   ('interior', 'Interiorul din material textil')],
  {'Model': 'Tommy Hilfiger T3X9-35235', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi, profil scurt, guler întărit', 'Cod produs': 'T3X9-35235'})
