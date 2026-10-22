import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
CURAT = ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')

w(12796,
  f'<p>{GEOX} LOFTUS J46M2A sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, cu profil scurt, din imitație de piele și material textil, ușor de întreținut, pentru ținute casual și streetwear. Sistemul Amphibiox ține apa afară, iar GEOX Respira scoate umiditatea spre exterior.</p>'
  '<p>Aricii și inserția elastică fac încălțatul rapid și ajută pantoful să stea bine pe picior. Talpa plată din spumă e ușoară.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Căptușeală', 'textilă, aerisită.'), ('Călcâi', 'întărit.'), ('Guler', 'ușor întărit.'))
  + '<p>Numerele 24-27 sunt pentru fetițe de în jur de 2-4 ani.</p>',
  [('model', 'Geox LOFTUS sneakers pentru copii albi J46M2A.0FUNF'), ('profil', 'Profilul scurt al părții superioare împreună cu gulerul ușor întărit'),
   ('material', 'Partea superioară din imitație de piele și material textil creează un aspect estetic și este ușor de întreținut'), ('stil', 'atât casual, cât și streetwear'),
   ('Amphibiox', 'Sistemul Amphibiox contribuie la protecția împotriva apei'), ('Respira', 'Tehnologia GEOX Respira™ favorizează termoreglarea naturală a piciorului, eliminând umiditatea spre exterior'),
   ('arici', 'Închiderea practică cu arici'), ('elastic', 'Inserția elastică susține ajustarea încălțămintei la picior'), ('talpă', 'Talpa plată din spumă contribuie la lejeritatea încălțămintei'),
   ('căptușeală', 'Interiorul căptușit cu material textil favorizează ventilația'), ('călcâi', 'Călcâiul întărit')],
  {'Model': 'Geox LOFTUS', 'Material': 'imitație de piele și textil, interior textil, talpă din spumă', 'Caracteristici': 'Amphibiox, Geox Respira, arici cu inserție elastică', 'Cod produs': 'J46M2A.0FUNF'})

w(12797,
  f'<p>În verde, salopeta {REIMA} Mjosa e aceeași {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopetă unisex")} de softshell pentru cei mici, gândită pentru zile ploioase și cu vânt. Ploaia nu trece de membrana de 10000 mm H2O, iar țesătura întârzie absorbția apei.</p>'
  '<p>Pe dinăuntru are polar și o umplutură sintetică subțire. Gluga se scoate, iar manșetele de la picioare se reglează și țin cracii pe loc.</p>'
  '<p>Detaliile practice:</p>'
  + L(('Buzunare', 'cu fermoar, nu se pierd lucrurile.'), ('Reflectorizante', 'vizibil după lăsarea întunericului.'), ('Murdărie', 'se curăță ușor.'), ('Lungime', 'peste genunchi.'))
  + '<p>Mărimile 74-98 acoperă aproximativ 9 luni - 3 ani.</p>',
  [('model', 'Reima Salopetă pentru copii Mjosa verde 5100006D'), ('softshell', 'confecționat din softshell tehnic'), ('membrană', 'Membrană impermeabilă (10000 mm H2O)'),
   ('absorbție', 'întârziind absorbția acesteia de către țesătură'), ('vânt', 'Construcția softshell rezistentă la vânt'), ('polar', 'Umplutură sintetică ușoară și căptușeală din polar'),
   ('glugă', 'Glugă detașabilă'), ('manșete', 'manșete reglabile la picioare'), ('buzunare', 'Buzunare practice cu fermoar'), ('reflectorizant', 'Detalii reflectorizante sporesc vizibilitatea copilului după lăsarea întunericului'),
   ('murdărie', 'Material rezistent la murdărie'), ('lungime', 'Lungime peste genunchi')],
  {'Model': 'Reima Mjosa', 'Material': 'softshell 92% poliester și 8% elastan, căptușeală din polar', 'Caracteristici': '10000 mm H2O, glugă detașabilă, manșete reglabile', 'Cod produs': '5100006D'},
  varsta_txt='9 luni - 3 ani')

w(12805,
  f'<p>Geaca varsity {TH} KG0KG09444 albă este o {A("/categorie/geci-jachete/", "geacă pentru fete")} fără izolație și fără umplutură, din bumbac moale cu poliester, cu imprimeu expresiv, pentru sezonul de tranziție. Croiala e lejeră, cu mâneci raglan, și nu are glugă.</p>'
  '<p>Se închide cu capse, iar tivul și manșetele au borduri elastice. Lungimea ajunge până la șolduri.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Buzunare', 'laterale.'), ('Material', '68% bumbac, 32% poliester.'), ('Închidere', 'capse.'))
  + '<p>Mărimile 128-176 sunt pentru fete de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă varsity pentru copii albă KG0KG09444'), ('izolație', 'Model fără izolație termică'), ('umplutură', 'Construcție fără umplutură'),
   ('bumbac', 'Confecționată din bumbac moale'), ('imprimeu', 'Decorată cu un imprimeu expresiv'), ('tranziție', 'potrivit pentru sezoanele de tranziție'),
   ('croială', 'Croiala lejeră'), ('raglan', 'Mâneci raglan'), ('glugă', 'Model fără glugă'), ('capse', 'Închidere cu capse'),
   ('borduri', 'Tivul și manșetele finisate cu borduri elastice'), ('lungime', 'Lungime până la șolduri'), ('buzunare', 'Buzunare laterale practice'), ('material', '32% Poliester, 68% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG09444 (varsity)', 'Material': '68% bumbac, 32% poliester', 'Caracteristici': 'fără izolație, capse, mâneci raglan, imprimeu', 'Cod produs': 'KG0KG09444'})

w(12806,
  f'<p>Geaca bomber {A("/brand/mini-rodini/", "Mini Rodini")} Soccerball violetă este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} în stil college și varsity, cu broderii cu minge de fotbal pe piept și pe spate. Are izolație termică ușoară, pentru zilele mai răcoroase de primăvară și toamnă.</p>'
  '<p>Se închide cu capse, iar gulerul, manșetele și tivul au borduri striate. Mânecile raglan și croiala lejeră lasă loc de mișcare.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'completă.'), ('Buzunare', 'laterale, oblice.'), ('Material', '100% poliester, țesătură rezistentă.'))
  + '<p>Mărimile 80-86 până la 140-146 sunt pentru copii de aproximativ 1-11 ani.</p>',
  [('model', 'Mini Rodini Geacă bomber copii Soccerball violetă 26210106'), ('college', 'Design inspirat de stilul college și varsity'),
   ('broderii', 'Broderiile distinctive cu motiv de minge de fotbal de pe piept și spate'), ('izolație', 'Izolația termică ușoară asigură confort în zilele mai răcoroase de primăvară și toamnă'),
   ('capse', 'Închiderea comodă cu capse'), ('borduri', 'Bordurile striate de la guler, manșete și din partea de jos'), ('raglan', 'Mânecile raglan'),
   ('croială', 'Croiala lejeră permite stratificarea liberă'), ('căptușeală', 'Are căptușeală completă'), ('buzunare', 'Buzunare laterale oblice'),
   ('țesătură', 'Confecționată dintr-o țesătură rezistentă'), ('material', '100% Poliester')],
  {'Model': 'Mini Rodini Soccerball (bomber)', 'Material': '100% poliester, izolație ușoară', 'Caracteristici': 'broderii minge de fotbal, capse, mâneci raglan', 'Cod produs': '26210106'})

w(12809,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261162 sunt {A("/categorie/adidasi/", "adidași pentru fete")} bleumarin, din piele naturală, cu motiv animalier, pentru joaca de zi cu zi. Talpa flexibilă tip barefoot, din cauciuc, lasă piciorul să se miște natural, iar spațiul extins de la degete le lasă să stea liber.</p>'
  '<p>Aricii cu curea reglabilă îi permit fetiței să se încalțe singură, iar gulerul moale nu irită glezna.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Călcâi', 'întărit.'), ('Podology Partnership', 'sprijin pentru dezvoltarea piciorului.'))
  + '<p>Numerele 20-23 se potrivesc fetițelor de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele bleumarin 261162'), ('piele', 'Partea superioară rezistentă din piele naturală'), ('animal', 'Motiv animalier adorabil'),
   ('zilnic', 'activităților zilnice'), ('barefoot', 'Talpă flexibilă tip barefoot din cauciuc'), ('degete', 'Spațiu extins în zona degetelor'),
   ('arici', 'Închidere practică cu arici și curea reglabilă, care facilitează încălțarea autonomă'), ('guler', 'Gulerul moale al părții superioare'),
   ('căptușeală', 'Căptușeală moale din material textil'), ('călcâi', 'Călcâiul întărit'), ('Podology', 'Suportul Parteneriatului Biomecanics Podology')],
  {'Model': 'Biomecanics 261162', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'talpă barefoot, arici cu curea reglabilă', 'Cod produs': '261162'})

w(12819,
  f'<p>{GEOX} INEK J56ASA roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu branțuri luminoase, din material textil și piele ecologică, ușori, pentru purtarea zilnică. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos, iar bucla de la spate ajută la încălțat.</p>'
  '<p>Vârful rotund, ușor rigid, lasă loc degetelor, iar contrafortul rigid ține călcâiul pe loc.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 24-27 merg la fetițe de cam 2-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii INEK culoarea roz, J56ASA.0BCKC'), ('lumini', 'Pantofi cu branturi luminoase'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('vârf', 'Degetul rotund, ușor rigid'), ('călcâi', 'Contorul de călcâi rigid'),
   RESPIRA, CURAT, ('talpă', 'Talpa exterioară din cauciuc este durabilă')],
  {'Model': 'Geox INEK', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'branțuri luminoase, șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J56ASA.0BCKC'},
  notes=['Magazinul dă „Înălțime: jos”, dar și o parte superioară ridicată care rigidizează glezna; n-am precizat profilul.'])

w(12821,
  f'<p>Adidașii {TH} T3A9-35076 bej sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt, din imitație de piele cu finisaj nubuc, cu interior căptușit care ține de cald în zilele mai reci. Se leagă cu șireturi tradiționale, pentru o strângere precisă.</p>'
  '<p>Vârful rotund e rigidizat și lasă degetele să se așeze liber, iar călcâiul întărit ține piciorul drept. Gulerul moale nu roade glezna.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Interior', 'textil, căptușit.'), ('Talpă', 'din cauciuc, cu profil plat.'), ('Închidere', 'șireturi.'))
  + '<p>Numerele 35-39 sunt pentru copii de la vreo 10 ani în sus, orientativ.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bej T3A9-35076'), ('profil', 'încălțăminte elegantă, cu profil scurt'), ('nubuc', 'Partea superioară din imitație de piele, cu finisaj nubuc'),
   ('căldură', 'Interiorul căptușit, din material textil, contribuie la menținerea căldurii'), ('șireturi', 'Șireturile tradiționale permit o ajustare precisă'),
   ('vârf', 'Vârful rigidizat și călcâiul întărit susțin stabilizarea piciorului'), ('degete', 'Vârful rotund permite o așezare liberă a degetelor'),
   ('guler', 'Gulerul moale al părții superioare contribuie la confortul din jurul gleznei'), ('talpă', 'Talpa din cauciuc, cu profil plat')],
  {'Model': 'Tommy Hilfiger T3A9-35076', 'Material': 'imitație de piele cu finisaj nubuc, interior textil căptușit, talpă din cauciuc', 'Caracteristici': 'șireturi, interior căptușit, vârf rigidizat', 'Cod produs': 'T3A9-35076'})

w(12822,
  f'<p>{GEOX} INEK J659CB bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu profil jos și detalii decorative, din material textil și piele ecologică, care se închid cu velcro. Partea de sus e rigidizată și ține forma, iar bucla de la spate ajută la încălțat.</p>'
  '<p>Vârful e rotund, iar interiorul textil e confortabil și se păstrează curat ușor.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi cu perforări.'), ('Talpă', 'din cauciuc.'), ('Închidere', 'velcro.'))
  + '<p>Numerele 24-27 se potrivesc băieților de în jur de 2-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii INEK culoarea bleumarin, J659CB.01454'), ('profil', 'Înălțime: mic de statură'), ('decor', 'Detalii decorative'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('rigid', 'Partea superioară rigidizată'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('vârf', 'Varf rotund'),
   CURAT, RESPIRA, ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox INEK', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira, buclă la spate', 'Cod produs': 'J659CB.01454'})

w(12824,
  f'<p>Hanoracul {REIMA} Neulomus albastru este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} din polar melanj, moale și plăcut la atingere, în mare parte din poliester reciclat. Fermoarul îl face ușor de pus și de scos, iar gulerul ridicat apără de frig.</p>'
  '<p>Mânecile raglan lasă brațele libere, iar mânecile și tivul au margine elastică, care ține vântul afară. Croiala e simplă și dreaptă, iar modelul uni se poartă ușor cu restul hainelor.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două, laterale.'), ('Material', '90% poliester reciclat, 10% poliester.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 104-164 merg cam la 4-14 ani.</p>',
  [('model', 'Reima Neulomus albastru 5200365A'), ('polar', 'Material: polar'), ('melanj', 'Model: melanj'), ('moale', 'Model realizat din material moale si placut la atingere'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('raglan', 'Maneca raglan'), ('margini', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('buzunare', 'Două buzunare laterale'),
   ('material', '90% Poliester reciclat, 10% Poliester'), ('croială', 'Tăiere simplă, fără blocare'), ('glugă', 'Gluga: fara gluga'), ('uni', 'Model: uni')],
  {'Model': 'Reima Neulomus', 'Material': '90% poliester reciclat, 10% poliester (polar)', 'Caracteristici': 'fermoar, guler ridicat, mâneci raglan', 'Cod produs': '5200365A'},
  notes=['Descrierea scurtă spune „material de lână”, compoziția e poliester (polar); am scris polar.'])

w(12825,
  f'<p>Sandalele sport {REIMA} Valoa negre sunt {A("/categorie/unisex-incaltaminte-sandale/", "sandale unisex")} vegane, de tip Barefoot, cu talpă plată și flexibilă din cauciuc, care ține bine pe diferite suprafețe. Partea de sus e din material textil care lasă aerul să circule.</p>'
  '<p>Interiorul are căptușeală elastică, care ușurează încălțatul, iar stilul sport merge la jocuri și excursii.</p>'
  '<p>Ce mai au sandalele:</p>'
  + L(('Branțuri Happy Fit', 'detașabile, pentru mărime și igienă.'), ('Interior', 'sintetic și textil.'), ('Construcție', 'Barefoot, pentru postura naturală.'))
  + '<p>Numerele 28-40 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'Reima Sandale sport pentru copii Valoa negre 5400157C'), ('vegan', 'Produs vegan'), ('Barefoot', 'Construcție de tip Barefoot cu talpă plată'),
   ('talpă', 'Talpă flexibilă din cauciuc , permite o aderență bună pe diferite suprafețe'), ('textil', 'Partea superioară din material textil respirabil'),
   ('elastic', 'cu o căptușeală elastică ce facilitează încălțarea'), ('sport', 'Stil sportiv , potrivit pentru copiii activi în timpul diverselor jocuri și excursii'),
   ('Happy Fit', 'Branțuri detașabile Happy Fit'), ('interior', 'Interior din material sintetic și textil')],
  {'Model': 'Reima Valoa', 'Material': 'textil, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'Barefoot, branțuri Happy Fit, vegane', 'Cod produs': '5400157C'})
