import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
CURAT = ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')
LEVIS = A('/brand/levis/', "Levi's")
PODO = ('Podology', 'Biomecanics Podology Partnership')

w(12960,
  f'<p>Geaca {LEVIS} OVERSIZED WESTERN TRUCKER este o {A("/categorie/geci-jachete/", "geacă pentru fete")} în culoarea albastru, din denim spălăcit decorativ, subțire și fără căptușeală, pentru sezonul de tranziție. Are guler, se închide cu nasturi și nu are glugă.</p>'
  '<p>Manșetele moi se închid tot cu nasturi, iar pe piept sunt două buzunare cu nasturi.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Buzunare', 'oblice, plus două la piept.'), ('Material', '69% bumbac, 26% poliester, 4% viscoză Lenzing Ecovero, 1% elastan.'), ('Croială', 'simplă.'))
  + '<p>Mărimile 98-128 sunt pentru fete de aproximativ 3-8 ani.</p>',
  [('model', "Levi's Geacă copii OVERSIZED WESTERN TRUCKER 3EN567"), ('culoare', 'Culoare albastru'), ('denim', 'Denim spalacit decorativ'), ('subțire', 'Model subțire'),
   ('necăptușit', 'Captuseala: necaptusit'), ('tranziție', 'Izolare: tranzitional'), ('guler', 'Model cu guler'), ('nasturi', 'Incheiere cu nasturi'),
   ('glugă', 'Gluga: fara gluga'), ('manșete', 'Manșete moi cu închidere cu nasturi'), ('buzunare', 'Buzunare oblice'), ('piept', 'Două buzunare la piept cu nasturi'),
   ('material', '69% Bumbac, 26% Poliester , 4% VASCOZA LENZING ECOVERO, 1% Elastan'), ('croială', 'Tăiere simplă, fără blocare')],
  {'Model': "Levi's OVERSIZED WESTERN TRUCKER", 'Material': '69% bumbac, 26% poliester, 4% viscoză, 1% elastan', 'Caracteristici': 'denim spălăcit, nasturi, buzunare la piept', 'Cod produs': '3EN567'})

w(12961,
  f'<p>Pantofii {A("/brand/primigi/", "Primigi")} PTR 24113 roz sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} din piele nubuc netedă, cu design barefoot, care lasă degetele să se miște liber, pentru primăvară și toamnă. Bordura de cauciuc din jurul vârfului îi apără de zgârieturi la joacă.</p>'
  '<p>Vârful lat face loc degetelor, iar aricii fac încălțatul rapid și reglarea după picior.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'piele naturală, moale.'), ('Branț', 'din piele naturală, detașabil.'), ('Talpă', 'din cauciuc, flexibilă.'))
  + '<p>Numerele 25-29 sunt pentru fetițe de cam 2-5 ani.</p>',
  [('model', 'Primigi Pantofi pentru copii din nubuck roz PTR 24113'), ('nubuc', 'Partea superioară din piele nubuc'), ('neted', 'Textura netedă a nubucului'),
   ('barefoot', 'Designul barefoot favorizează poziționarea naturală a piciorului și libertatea de mișcare a degetelor'), ('sezon', 'zilele de primăvară și toamnă'),
   ('bordură', 'Bordura de cauciuc în jurul vârfului protejează încălțămintea împotriva deteriorărilor'), ('vârf', 'Vârful lat asigură spațiu pentru degete'),
   ('arici', 'Sistemul de închidere cu arici permite o încălțare rapidă'), ('interior', 'Interiorul din piele naturală'), ('branț', 'Branțul detașabil din piele naturală'),
   ('talpă', 'Talpa din cauciuc oferă flexibilitate')],
  {'Model': 'Primigi PTR 24113', 'Material': 'piele nubuc, interior și branț din piele naturală, talpă din cauciuc', 'Caracteristici': 'barefoot, bordură de cauciuc, arici', 'Cod produs': 'PTR 24113'})

w(12964,
  f'<p>{BIO} 261015 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} bleumarin, din piele naturală, cu profil scurt și guler ușor întărit, făcuți cu podologi, în stil casual. Spațiul mărit în zona degetelor le lasă loc, iar talpa flexibilă din cauciuc urmează rularea naturală a piciorului.</p>'
  '<p>Aricii fac încălțatul rapid, iar călcâiul moale cuprinde piciorul fără să irite. Pielea naturală lasă aerul să treacă și ține mult.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Interior', 'material textil.'), ('Branț', 'aerisit.'), ('Podology Partnership', 'colaborare cu podologi.'))
  + '<p>Au rămas numerele 24-26, pentru copii de aproximativ 2-4 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele bleumarin 261015'), ('piele', 'Partea superioară din piele naturală permite o ventilație adecvată și durabilitatea'), ('profil', 'Profil scurt al părții superioare , cu guler ușor întărit'),
   ('podologi', 'creat în colaborare cu podologi'), ('casual', 'stilul casual'), ('degete', 'Spațiu mărit în zona degetelor'), ('talpă', 'Talpă flexibilă din cauciuc , cu profil plat, susține rulajul natural'),
   ('arici', 'Închidere practică cu arici'), ('călcâi', 'Călcâi moale , care îmbrățișează delicat călcâiul'), ('interior', 'Interior din material textil'),
   ('branț', 'Branț respirabil'), PODO],
  {'Model': 'Biomecanics 261015', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, spațiu mărit la degete, călcâi moale', 'Cod produs': '261015'})

w(12965,
  f'<p>Ghetele de iarnă {BIO} 261167 roz sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} înalte, din piele naturală, cu gulerul moale care cuprinde glezna. Membrana BioTEX ține umezeala de afară și lasă transpirația să iasă.</p>'
  '<p>Aricii fac încălțatul rapid și reglarea după picior, iar vârful rotund și moale lasă degetele libere. Talpa plată din cauciuc ține bine pe sol la mers.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Interior', 'material textil.'), ('Podology Partnership', 'pe baza cunoștințelor podologilor.'))
  + '<p>Numerele 24-26 se potrivesc fetițelor de cam 2-4 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii roz 261167'), ('înalt', 'Partea superioară înaltă din piele naturală îmbrățișează glezna, iar gulerul moale'),
   ('BioTEX', 'Membrana BioTEX creează o barieră împotriva umezelii externe, permițând în același timp evacuarea transpirației'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă a încălțămintei, precum și ajustarea la picior'),
   ('vârf', 'Vârful rotund și moale permite așezarea liberă a degetelor'), ('talpă', 'Talpa plată din cauciuc asigură o bună aderență la sol și stabilitate în timpul mersului'), ('călcâi', 'Călcâiul întărit'),
   ('interior', 'Material textil'), ('Podology', 'Tehnologia Biomecanics Podology Partnership susține dezvoltarea corectă a piciorului copilului, bazându-se pe cunoștințele podologilor')],
  {'Model': 'Biomecanics 261167', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'ghete de iarnă, BioTEX, arici', 'Cod produs': '261167'})

w(12969,
  f'<p>Pentru băieții mai mari, {GEOX} INEK J669CD vin în numerele 32-35: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albaștri, cu lumini încorporate care se aprind la fiecare pas. Partea de sus, din textil și material sintetic, e ușoară și rezistă bine.</p>'
  '<p>Șireturile elastice ajută la reglare, iar aricii la încălțatul rapid. Interiorul, din textil și sintetic, lasă aerul să circule.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('GEOX Respira', 'ține pantoful uscat pe dinăuntru.'), ('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Se potrivesc băieților de cam 8-11 ani.</p>',
  [('model', 'Geox INEK sneakers pentru copii albaștri J669CD.01454'), ('lumini', 'Lumini încorporate adaugă dinamism fiecărui pas'),
   ('material', 'Partea superioară din material textil și sintetic contribuie la ușurința și durabilitatea'), ('închidere', 'Șireturi elastice facilitează ajustarea, iar închiderea cu arici favorizează încălțarea rapidă'),
   ('interior', 'Interior căptușit cu material textil și sintetic favorizează o bună circulație a aerului'), ('Respira', 'Tehnologia GEOX Respira™ favorizează eliminarea umidității, menținând uscăciunea'),
   ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox INEK', 'Material': 'textil și sintetic, interior textil și sintetic, talpă din cauciuc', 'Caracteristici': 'lumini încorporate, Geox Respira, șireturi elastice și arici', 'Cod produs': 'J669CD.01454'})

w(12978,
  f'<p>Geaca bomber {TH} KB0KB10571 bleumarin este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} cu croială regulară și glugă detașabilă, pentru vremea schimbătoare din sezonul de tranziție. Se închide cu capse, iar decolteul și manșetele au nervuri.</p>'
  '<p>Tivul are șnur reglabil, iar lungimea până la șolduri nu încurcă mișcarea. Mânecile clasice lasă brațele să se miște natural, iar materialul textil e durabil și ușor de întreținut.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'tip slit, în față.'), ('Mâneci', 'clasice.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-176 sunt pentru băieți de aproximativ 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă bomber pentru copii bleumarin KB0KB10571'), ('croială', 'Croială regulară favorizează libertatea de mișcare'),
   ('glugă', 'Glugă detașabilă permite ajustarea jachetei la condițiile meteorologice schimbătoare'), ('tranziție', 'sezonul de tranziție'),
   ('capse', 'Sistem de închidere cu capse'), ('decolteu', 'Decolteu cu nervuri'), ('manșete', 'Manșete cu nervuri'), ('tiv', 'Tiv reglabil cu șnur'),
   ('lungime', 'Lungime până la șolduri'), ('buzunare', 'Buzunare practice tip slit în față'), ('mâneci', 'Tip de mânecă clasică susține o gamă naturală de mișcare a brațelor'), ('material', '100% Poliester'), ('textil', 'Confecționată din material textil favorizează durabilitatea și ușurința în întreținere')],
  {'Model': 'Tommy Hilfiger KB0KB10571 (bomber)', 'Material': '100% poliester', 'Caracteristici': 'glugă detașabilă, capse, tiv cu șnur', 'Cod produs': 'KB0KB10571'})

w(12981,
  f'<p>Sandalele {A("/brand/columbia/", "Columbia")} TECHSUN ADVENTURE bej sunt {A("/categorie/unisex-incaltaminte-sandale/", "sandale unisex")} sport, ușoare, din material sintetic durabil și ușor de întreținut, pentru aventurile de vară. Vârful decupat lasă piciorul să se aerisească în zilele calde.</p>'
  '<p>Scaiul permite o strângere rapidă și precisă, iar talpa de cauciuc, groasă de 2-4 cm, ține bine pe sol.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'căptușit cu material textil.'), ('Talpă', 'din cauciuc.'), ('Închidere', 'scai.'))
  + '<p>Numerele 32-39 se potrivesc copiilor de la vreo 8 ani în sus, orientativ.</p>',
  [('model', 'Columbia Sandale pentru copii TECHSUN ADVENTURE bej 2148731'), ('sport', 'Sandale pentru copii cu un caracter sportiv'), ('ușor', 'o încălțăminte ușoară și rezistentă'),
   ('sintetic', 'Partea superioară din material sintetic asigură durabilitate și este ușor de întreținut'), ('vară', 'aventurile și activitățile de vară'),
   ('vârf', 'Vârful decupat permite ventilarea liberă a piciorului'), ('scai', 'Închiderea cu scai permite ajustarea rapidă și precisă'),
   ('talpă', 'Talpa de cauciuc cu o grosime de 2-4 cm susține stabilitatea și asigură o bună aderență la sol'), ('interior', 'Interiorul căptușit cu material textil')],
  {'Model': 'Columbia TECHSUN ADVENTURE', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'scai, vârf decupat', 'Cod produs': '2148731'})

w(12982,
  f'<p>Tot B561MG, dar în numerele 24-27: {GEOX} GISLI aurii sunt {A("/categorie/adidasi/", "adidași pentru fete")} înalți, cu guler întărit care susține glezna, din imitație de piele și materiale textile. Talpa GEOX Respira ajută la păstrarea picioarelor uscate.</p>'
  '<p>Aricii o lasă pe fetiță să se încalțe singură, iar călcâiul întărit ține piciorul în poziție corectă. Nuanța aurie iese în evidență în orice ținută.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textil, confortabil pe durată lungă.'), ('Talpă', 'plată, din cauciuc, ține bine pe diverse suprafețe.'), ('Închidere', 'arici.'))
  + '<p>Se potrivesc fetițelor de aproximativ 2-4 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii aurii B561MG.0AUAJ'), ('culoare', 'Culoare aur'), ('înalt', 'Profil înalt cu guler întărit oferă suport suplimentar pentru glezna delicată'),
   ('material', 'Partea superioară din imitație de piele și materiale textile'), ('Respira', 'Tehnologia GEOX Respira™ favorizează respirabilitatea tălpii, ajutând la menținerea picioarelor uscate'),
   ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă și independentă'), ('călcâi', 'Călcâi întărit susține stabilitatea piciorului, ajutând la menținerea unei poziții corecte'),
   ('auriu', 'Culoarea aurie adaugă strălucire'), ('căptușeală', 'Interior căptușit cu material textil favorizează confortul la purtare pe termen lung'),
   ('talpă', 'Talpă plată din cauciuc favorizează o bună aderență pe diverse suprafețe')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici, profil înalt', 'Cod produs': 'B561MG.0AUAJ'})

w(12983,
  f'<p>Adidașii {TH} T3X9-34351 albi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil jos, din material textil și piele ecologică. Șireturile plate nu apasă pe arcada piciorului, deci pantoful se strânge bine și rămâne confortabil.</p>'
  '<p>Cutia rotundă e întărită, iar contrafortul rigidizat sprijină călcâiul și glezna.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Partea de sus', 'textil și imitație de piele.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'din cauciuc, durabilă.'))
  + '<p>Numerele 35-41 sunt pentru copii de la aproximativ 10 ani în sus; la 37 branțul are 23,5 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea alb, T3X9-34351'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('șireturi', 'Sireturile plate elimina punctele de presiune de pe arcada piciorului'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), CURAT, ('talpă', 'talpă din cauciuc care este durabilă'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 23,5 cm')],
  {'Model': 'Tommy Hilfiger T3X9-34351', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi plate, vârf întărit', 'Cod produs': 'T3X9-34351'})

w(12984,
  f'<p>{GEOX} STEPPIEUP bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} pentru cei mici, cu profil jos și detalii decorative, din material textil și piele naturală. Velcro-ul face încălțatul și descălțatul rapid, iar partea de sus rigidizată ține forma pantofului.</p>'
  '<p>Căptușeala moale nu irită pielea, iar branțul din piele previne frecarea și mirosul neplăcut. Interiorul are și piele naturală.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Talpă', 'din cauciuc.'), ('Vârf', 'rotund.'))
  + '<p>Numerele 20-27 se potrivesc băieților de în jur de 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii STEPPIEUP culoarea bleumarin, B655WA.08514'), ('profil', 'Înălțime: mic de statură'), ('decor', 'Detalii decorative'),
   ('material', 'combinația materialului textil cu pielea naturală'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('rigid', 'Partea superioară rigidizată'), ('căptușeală', 'Căptușeala moale din material textil previne iritația'),
   ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea, abraziunile si aparitia unui miros neplacut'), RESPIRA, ('talpă', 'Talpă din cauciuc'), ('vârf', 'Varf rotund'), ('interior', 'Material textil, Piele naturala')],
  {'Model': 'Geox STEPPIEUP', 'Material': 'textil și piele naturală, interior textil și piele, talpă din cauciuc', 'Caracteristici': 'velcro, branț din piele, Geox Respira', 'Cod produs': 'B655WA.08514'})
