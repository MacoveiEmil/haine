import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
PRIM = A('/brand/primigi/', 'Primigi')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
PODO = ('Podology', 'Biomecanics Podology Partnership')
VALENCIA = ('Valencia', 'Acestea au fost create in cooperare cu medici pediatri si ingineri de la Institutul de Biomecanica din Valencia')

w(12486,
  f'<p>Mocasinii {GEOX} bleumarin sunt {A("/categorie/baieti-incaltaminte-pantofi/", "mocasini pentru băieți")} din piele nabuc, cu toc plat, interior din piele și talpă din gumă. Vârful și spatele călcâiului sunt rigidizate, deci pantoful își păstrează forma și ține piciorul pe loc.</p>'
  '<p>Gulerul gambei e ușor rigidizat, ca mocasinul să nu se lărgească la purtare.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări pentru aerisire.'), ('Talpă', 'din gumă.'), ('Interior', 'piele naturală.'))
  + '<p>Numerele 35-41 sunt pentru băieți de la aproximativ 10 ani în sus; la 39 branțul are 26 cm.</p>',
  [('model', 'Geox Mocasini copii'), ('nabuc', 'Model confectionat din piele nabuc'), ('toc', 'Toc: plat'), ('interior', 'Interior din piele'),
   ('vârf', 'Varf rigidizat'), ('călcâi', 'Spatele calcaiului rigidizat'), ('guler', 'Gulerul gambei usor rigidizat'), RESPIRA,
   ('talpă', 'Talpa din guma'), ('lungime', 'Lungimea brantului pentru marimea este de: 26 cm'), ('culoare', 'Culoare bleumarin')],
  {'Model': 'Geox (mocasini)', 'Material': 'piele nabuc, interior din piele, talpă din gumă', 'Caracteristici': 'Geox Respira, vârf și călcâi rigidizate', 'Cod produs': ''})

w(12490,
  f'<p>Bluza {TH} KS0KS00709 gri este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză pentru băieți")} cu imprimeu, din țesătură subțire, ușor elastică, cu decolteu clasic, rotund. Materialul e jumătate bumbac reciclat, făcut din deșeuri textile vechi, și jumătate poliester reciclat.</p>'
  '<p>Mânecile și tivul au margine elastică, care ține bluza pe loc și oprește vântul. Croiala e simplă, dreaptă, fără glugă.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '50% poliester reciclat, 50% bumbac reciclat.'), ('Decolteu', 'rotund.'), ('Model', 'cu imprimeu.'))
  + '<p>Gama 128-176 acoperă băieți de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Bluză copii culoarea gri, cu imprimeu, KS0KS00709'), ('țesătură', 'țesătură subțire, usor elastica'),
   ('regenerat', 'Din deșeuri textile vechi sunt create fibre și fire noi'), ('material', '50% Poliester reciclat, 50% Bumbac reciclat'),
   ('decolteu', 'Decolteu clasic, rotund'), ('margini', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('croială', 'Tăiere simplă, fără blocare'),
   ('glugă', 'Gluga: fara gluga'), ('imprimeu', 'Model cu imprimeu')],
  {'Model': 'Tommy Hilfiger KS0KS00709', 'Material': '50% poliester reciclat, 50% bumbac reciclat', 'Caracteristici': 'imprimeu, decolteu rotund, margini elastice', 'Cod produs': 'KS0KS00709'})

w(12491,
  f'<p>{BIO} 261242 sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} maro, sport, cu profil înalt și guler întărit care susține glezna, buni pentru joaca activă afară. Membrana BioTEX ține umezeala de afară, dar lasă transpirația să iasă.</p>'
  '<p>Tehnologia Flexi Lite face talpa ușoară și flexibilă, iar talpa din spumă are 2 cm. Aricii îl lasă pe copil să se încalțe singur.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Partea de sus', 'imitație de piele și material textil.'), ('Călcâi', 'întărit.'), ('Branț', 'textil, detașabil.'), ('Podology Partnership', 'lucrat cu podologi.'))
  + '<p>Numerele 28-34 se potrivesc, orientativ, copiilor de 4-11 ani.</p>',
  [('model', 'Biomecanics Încălțăminte pentru copii maro 261242'), ('profil', 'Profilul înalt al părții superioare cu guler întărit susține glezna'),
   ('aer liber', 'jocurilor active în aer liber'), ('BioTEX', 'Membrana BioTEX cu structură microporoasă protejează împotriva umidității externe, eliminând în același timp transpirația'),
   ('Flexi Lite', 'Tehnologia Flexi Lite favorizează lejeritatea și flexibilitatea tălpii'), ('talpă', 'Talpa din spumă cu o grosime de 2 cm'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă'), ('material', 'Partea superioară confecționată din imitație de piele și material textil'),
   ('călcâi', 'Călcâiul întărit stabilizează călcâiul'), ('branț', 'Branțurile detașabile din material textil'), PODO],
  {'Model': 'Biomecanics 261242', 'Material': 'imitație de piele și textil, interior textil, talpă din spumă', 'Caracteristici': 'membrană BioTEX, Flexi Lite, arici, profil înalt', 'Cod produs': '261242'})

w(12493,
  f'<p>Pantofii {PRIM} 23548 maro sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} casual, din piele întoarsă și material textil, cu membrană GORE-TEX, care apără de umezeală și vânt. Talpa din spumă și cauciuc e ușoară și flexibilă, cu sistemul Shock Absorber, care preia șocurile la fiecare pas.</p>'
  '<p>Vârful rotund lasă loc degetelor, iar aricii permit încălțatul rapid și reglarea după picior.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Primigi × SIPeP', 'gândit după anatomia piciorului copilului.'), ('Interior', 'material textil moale.'), ('Branț', 'textil.'))
  + '<p>Mărimile 25-29 sunt pentru copii de în jur de 2-5 ani.</p>',
  [('model', 'Primigi Pantofi pentru copii maro PTIGT 23548'), ('casual', 'Stilul casual al pantofilor'), ('material', 'Partea superioară din piele întoarsă și material textil'),
   ('GORE-TEX', 'Membrana GORE-TEX® în construcția încălțămintei asigură protecție împotriva umezelii și vântului'), ('talpă', 'Talpa din spumă și cauciuc este ușoară și flexibilă'),
   ('Shock Absorber', 'Tehnologia Shock Absorber din talpă'), ('vârf', 'Vârful rotund oferă spațiu pentru degete'),
   ('arici', 'Închiderea cu arici permite încălțarea și descălțarea rapidă, precum și ajustarea la picior'), ('SIPeP', 'Colaborarea Primigi × SIPeP'),
   ('interior', 'Interiorul din material textil este moale'), ('branț', 'Branțul textil')],
  {'Model': 'Primigi 23548', 'Material': 'piele întoarsă și textil, interior textil, talpă din spumă și cauciuc', 'Caracteristici': 'GORE-TEX, Shock Absorber, arici', 'Cod produs': 'PTIGT 23548'})

w(12496,
  f'<p>Adidașii {BIO} bleumarin sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} ușori, cu profil jos, din material textil și piele ecologică, creați cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia. Se pun ușor și se strâng bine pe picior cu velcro.</p>'
  '<p>Vârful securizat apără degetele de lovituri, iar tăietura în U de la spate lasă glezna liberă și nu apasă pe tendonul lui Ahile.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Inserție', 'perforată, pentru confort termic.'), ('Branț', 'detașabil, antibacterian, profilat.'), ('Talpă', 'elastică.'))
  + '<p>Numerele 18-25 se poartă, aproximativ, între 1 și 3 ani; la 24 branțul are 14 cm.</p>',
  [('model', 'Biomecanics Sneakers pentru copii culoarea albastru marin'), ('ușor', 'Model ușor și confortabil'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinatia materialului textil cu pielea ecologica'), VALENCIA, ('velcro', 'Usor de imbracat si se potriveste bine datorita fixarii cu velcro'),
   ('vârf', 'Degetul securizat protejeaza degetele de la picioare impotriva ranilor'), ('U', 'taieturi in forma de U care impiedica exercitarea presiunii asupra tendonului lui Ahile'),
   ('inserție', 'insertiei perforate'), ('branț', 'Brant detasabil si antibacterian, profilat la mijlocul piciorului'), ('talpă', 'Talpa elastica'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 14 cm')],
  {'Model': 'Biomecanics (adidași)', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'velcro, vârf securizat, branț antibacterian detașabil', 'Cod produs': ''})

w(12506,
  f'<p>{BIO} 261273 sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu fața din material textil care lasă aerul să circule, gândiți împreună cu podologi pentru joaca și activitățile de zi cu zi. Călcâiul întărit ține piciorul drept la mers, iar gulerul ușor întărit cuprinde glezna fără să strângă.</p>'
  '<p>Aricii îi permit fetiței să se încalțe și să se descalțe singură.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Interior', 'căptușit cu material textil.'), ('Talpă', 'din cauciuc, durabilă, groasă de 2-4 cm.'), ('Branț', 'textil, detașabil.'), ('Podology Partnership', 'tehnologia Biomecanics.'))
  + '<p>Numerele merg de la 24 la 34, adică fete de cam 2-11 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii roz 261273'), ('textil', 'Fața superioară din material textil permite circulația aerului'),
   ('podologi', 'Proiectați în colaborare cu podologi'), ('zilnic', 'activitățile și jocurile zilnice'), ('călcâi', 'Călcâiul întărit stabilizează piciorul'),
   ('guler', 'Gulerul superior ușor întărit îmbrățișează delicat glezna, oferind suport fără a strânge'), ('arici', 'Sistemul practic de închidere cu arici'),
   ('interior', 'Interiorul căptușit cu material textil'), ('talpă', 'Talpa din cauciuc se caracterizează prin durabilitate'), ('grosime', 'Grosimea tălpii în intervalul 2-4 cm'),
   ('branț', 'Branțurile detașabile din material textil'), ('Podology', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261273', 'Material': 'textil, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, călcâi întărit, branț detașabil', 'Cod produs': '261273'})

w(12508,
  f'<p>Pantofii {GEOX} JISLI bleumarin sunt {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi pentru băieți")} din material textil și piele ecologică, cu membrana Geox Respira, care scade umezeala din interior. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos, fără legat.</p>'
  '<p>Vârful e rotund, iar contrafortul rigidizat sprijină călcâiul și glezna. Rezistă la apă, dar nu sunt complet impermeabili.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, durabilă.'), ('Partea de sus', 'textil și material sintetic.'))
  + '<p>Numerele 36-39 se potrivesc băieților de la 12 ani în sus, orientativ.</p>',
  [('model', 'Geox Pantofi copii JISLI culoarea albastru marin, J465CC.0MEFU'), ('material', 'combinatia materialului textil cu pielea ecologica'),
   ('Respira', 'Membrana unica si impermeabila a tehnologiei Geox Respira ajuta la scaderea umezelii excesive'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('vârf', 'Varf rotund'), ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), ('apă', 'nu garantează impermeabilitatea completă'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'),
   ('gamba', 'Material sintetic, Material textil')],
  {'Model': 'Geox JISLI', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice cu cârlig, rezistenți la apă', 'Cod produs': 'J465CC.0MEFU'},
  notes=['Magazinul descrie membrana ca impermeabilă, dar precizează și că produsul nu garantează impermeabilitatea completă; am scris varianta prudentă.'])

w(12526,
  f'<p>Adidașii {A("/brand/wheat/", "Wheat")} WF641 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} în culoarea albastru, ușori, din piele întoarsă și material textil, cu croială până la gleznă, pentru ținute casual și sport. Pielea are certificare LWG, pentru o producție responsabilă.</p>'
  '<p>Șireturile elastice cu opritor fac încălțatul rapid, iar plasa lasă aerul să circule în pantof.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'din bumbac organic, moale.'), ('Branț', 'din piele naturală.'), ('Călcâi', 'ușor întărit.'), ('Talpă exterioară', 'din spumă EVA și cauciuc.'))
  + '<p>Gama 24-35 merge cam de la 2 la 11 ani.</p>',
  [('model', 'Wheat Sneakers pentru copii albaștri WF641-01'), ('ușor', 'încălțăminte sportivă ușoară'), ('material', 'Partea superioară dintr-o combinație de piele întoarsă și material textil'),
   ('gleznă', 'Croiala până la gleznă'), ('ținute', 'ținutele casual și sportive'), ('LWG', 'Pielea certificată LWG atestă un proces de producție responsabil'),
   ('șireturi', 'Șireturile elastice cu opritor facilitează încălțarea rapidă'), ('plasă', 'Plasa respirabilă sprijină circulația aerului'),
   ('căptușeală', 'Căptușeala din bumbac organic'), ('branț', 'Piele naturală'), ('călcâi', 'Calcaiarul ușor întărit'), ('talpă', 'Talpa exterioară din spumă EVA și cauciuc')],
  {'Model': 'Wheat WF641', 'Material': 'piele întoarsă și textil, căptușeală din bumbac organic, talpă EVA și cauciuc', 'Caracteristici': 'șireturi elastice cu opritor, piele LWG', 'Cod produs': 'WF641-01'})

w(12527,
  f'<p>{PRIM} PBZ 23532 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albaștri, cu profil înalt, din piele întoarsă și material textil, pentru cei mai mici. Profilul înalt sprijină glezna, iar călcâiul întărit ține piciorul în poziție corectă.</p>'
  '<p>Talpa plată din cauciuc are sistemul Shock Absorber, care limitează șocurile la mers. Aricii îl lasă pe copil să se încalțe singur.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Interior', 'căptușit cu piele naturală și textil.'), ('Branț', 'din piele naturală, detașabil.'), ('Primigi × SIPeP', 'construcție după anatomia piciorului.'))
  + '<p>Numerele 19-24 sunt pentru băieți de aproximativ 1-3 ani.</p>',
  [('model', 'Primigi Sneakers pentru copii albastri PBZ 23532'), ('profil', 'Profilul înalt al părții superioare ajută la stabilizarea gleznei'),
   ('material', 'Partea superioară din piele întoarsă și material textil'), ('cei mici', 'conceput pentru cei mai mici'), ('călcâi', 'Călcâiul întărit stabilizează călcâiul'),
   ('talpă', 'Talpa plată din cauciuc'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă'), ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea autonomă'),
   ('interior', 'Interior căptușit cu piele naturală'), ('branț', 'Branțuri detașabile din piele naturală'), ('SIPeP', 'Colaborarea Primigi × SIPeP')],
  {'Model': 'Primigi PBZ 23532', 'Material': 'piele întoarsă și textil, interior din piele naturală, talpă din cauciuc', 'Caracteristici': 'Shock Absorber, arici, profil înalt', 'Cod produs': 'PBZ 23532'})

w(12530,
  f'<p>Pantalonii {A("/brand/reima/", "Reima")} Oikotie verzi sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")} de exterior, uni, din pânză tratată cu Teflon EcoElite, primul tratament de origine vegetală pentru rezistență durabilă la apă. Au impermeabilitate de 10000 g/m2 și respirabilitate de 3000 g/m2/24h.</p>'
  '<p>Talia e înaltă, cu bandă elastică, iar picioarele se termină cu tiv elastic, îngust. Magazinul precizează că nu garantează impermeabilitatea completă.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '92% poliamidă, 8% elastan.'), ('Croială', 'clasică, simplă.'), ('Model', 'uni.'))
  + '<p>Mărimile 92-140 se potrivesc copiilor de cam 2-10 ani.</p>',
  [('model', 'Reima Pantaloni copii Oikotie culoarea verde, 5100010B'), ('uni', 'Model: uni'), ('pânză', 'Material: panza'),
   ('Teflon', 'Teflon EcoElite este prima tesatura de origine vegetala care asigura o rezistenta durabila la apa'), ('impermeabilitate', 'Impermeabilitate: 10000 g/m2'),
   ('respirabilitate', 'Respirabilitate: 3000 g/m2/24h'), ('talie', 'Talie inalta cu banda elastica in talie'), ('tiv', 'Picioarele sunt finisate cu un tiv elastic, îngust'),
   ('apă', 'nu garantează impermeabilitatea completă'), ('material', '92% Poliamida, 8% Elastan'), ('croială', 'Croiala clasică, simplă')],
  {'Model': 'Reima Oikotie', 'Material': '92% poliamidă, 8% elastan', 'Caracteristici': 'Teflon EcoElite, 10000 mm impermeabilitate, talie elastică', 'Cod produs': '5100010B'})
