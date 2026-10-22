import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
PRIMIGI = A('/brand/primigi/', 'Primigi')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9484,
  f'<p>{PRIMIGI} PFZGT 88840 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de zăpadă unisex")}, negre, ușor izolate, din material textil, piele naturală și piele întoarsă. Membrana GORE-TEX® e foarte subțire și impermeabilă, oprește vântul, deci piciorul rămâne uscat în zăpadă și pe ploaie rece.</p>'
  '<p>Velcro-ul se reglează pe lățimea piciorului, iar partea de sus ridicată ține glezna pe teren denivelat. Contrafortul rigid de la călcâi ține piciorul pe loc, să nu alunece în cizmă la mers.</p>'
  '<p>Alte detalii de construcție:</p>'
  + L(('Vârf', 'rotund, ușor întărit.'), ('Interior', 'textil, se păstrează ușor curat.'), ('Talpă', 'exterioară, din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 31-40 se poartă de obicei de la 6 ani în sus.</p>',
  [('tip', 'Cizme de zapada pentru copii'), ('material', 'combinație de material textil, piele naturală și piele întoarsă'), ('izolație', 'Izolare: usor izolat'),
   ('membrană', 'Model cu membrana GORE-TEX®'), ('impermeabil', 'extrem de subtire si 100% impermeabila, rezistenta la vant'), ('velcro', 'Închiderea cu velcro'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('vârf', 'Cutie rotunda, usor intarita'), ('călcâi', 'Contorul de călcâi rigid'),
   ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Primigi PFZGT 88840', 'Material': 'textil, piele naturală și piele întoarsă, interior textil', 'Caracteristici': 'GORE-TEX®, ușor izolate, velcro, contrafort rigid', 'Cod produs': 'PFZGT 88840'})

w(9488,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IB0IB02174 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, neagră, ușor izolată, din material neted, cu glugă fixă și guler ridicat care țin frigul departe de gât și de cap.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile se termină cu bandă elastică, care strânge la încheietură și pe brațul unui copil mai subțire. Căptușeala o face ușor de tras peste un hanorac.</p>'
  '<p>Ce mai are geaca:</p>'
  + L(('Buzunare', 'închise.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('cod', 'Calvin Klein Jeans Geaca copii culoarea negru, IB0IB02174'), ('izolat', 'Model usor izolat confecționat din material neted'), ('matlasat', 'Matlasat'),
   ('glugă', 'Gulerul ridicat și gluga fixă'), ('frig', 'protecție suplimentară împotriva frigului'), ('croială', 'Tăiere simplă, fără blocare'),
   ('elastic', 'Mâneci finisate cu o coadă elastică'), ('căptușeală', 'Model cu captuseala'), ('buzunare', 'Buzunare incheiate'), ('fermoar', 'Incheiere cu fermoar'),
   ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans IB0IB02174', 'Material': '100% poliester', 'Caracteristici': 'ușor izolată, matlasată, glugă fixă, căptușită', 'Cod produs': 'IB0IB02174'})

w(9490,
  f'<p>{GEOX} IUPIDOO B3558A sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, cu profil scurt, din material textil și imitație de piele. Interiorul și branțul sunt din piele, care previne frecarea și mirosul neplăcut, iar sistemul Geox Respira din talpă ventilează piciorul.</p>'
  '<p>Velcro-ul îi ajută pe cei mici să se încalțe și să se descalțe repede, iar partea de sus rigidizată păstrează forma pantofului pe picior.</p>'
  '<p>Pe scurt:</p>'
  + L(('Vârf', 'rotund.'), ('Talpă', 'din cauciuc.'), ('Protecție', 'antibacteriană.'))
  + '<p>Mărimile 18-26 sunt, cu aproximație, pentru 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii IUPIDOO culoarea roz, B3558A.01454'), ('material', 'combinația materialului textil cu pielea ecologică'), ('profil', 'Înălțime: mic de statură'),
   ('branț', 'Un model cu branț din piele'), ('frecare', 'previne frecarea, abraziunile și apariția unui miros neplăcut'), ('interior', 'interior din piele'), RESPIRA,
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Varf rotund'),
   ('talpă', 'Talpă din cauciuc'), ('antibacterian', 'Protectie antibacteriana')],
  {'Model': 'Geox IUPIDOO B3558A', 'Material': 'textil și imitație de piele, interior din piele, talpă din cauciuc', 'Caracteristici': 'Geox Respira, velcro, protecție antibacteriană', 'Cod produs': 'B3558A.01454'})

w(9492,
  f'<p>Geaca {A("/brand/guess/", "Guess")} K6YL04 W2597 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, roz, cu izolație sintetică ușoară, pentru zilele de tranziție. Are un motiv animal și logo Guess, iar țesătura rezistentă e gândită pentru purtat zilnic.</p>'
  '<p>Croiala e regulară, cu loc pentru un strat în plus pe dedesubt, iar lungimea e scurtă. Tivul și manșetele cu bordură elastică se strâng pe corp, ca aerul rece să nu intre.</p>'
  '<p>Detaliile:</p>'
  + L(('Glugă', 'protejează capul de vânt.'), ('Buzunare', 'laterale, tip slip-on.'), ('Închidere', 'fermoar și capse.'), ('Căptușeală', 'sintetică, completă.'), ('Material', '100% poliester.'))
  + '<p>Orientativ, mărimile 88-96 până la 122-125 merg la 1-7 ani.</p>',
  [('cod', 'Guess Geacă petrecută pentru copii roz K6YL04 W2597'), ('matlasat', 'Geaca matlasată roz Guess'), ('izolație', 'Izolație sintetică ușoară'),
   ('tranziție', 'zilele de tranziție'), ('motiv', 'Motiv animal și logo Guess'), ('țesătură', 'Țesătură rezistentă'), ('zilnic', 'potrivită pentru utilizare zilnică'),
   ('croială', 'Croială regulară'), ('straturi', 'purtarea cu straturi suplimentare'), ('lungime', 'Lungimea scurtă a modelului'),
   ('elastic', 'Tiv și manșete cu bordură elastică'), ('aer rece', 'limitând pătrunderea aerului rece'), ('glugă', 'Glugă practică'),
   ('buzunare', 'Buzunare laterale tip slip-on'), ('închidere', 'Închidere cu fermoar și capse'), ('căptușeală', 'Căptușeală sintetică completă'), ('material', '100% Poliester')],
  {'Model': 'Guess K6YL04 W2597', 'Material': '100% poliester', 'Caracteristici': 'matlasată, izolație ușoară, glugă, tiv și manșete elastice', 'Cod produs': 'K6YL04 W2597'})

w(9495,
  f'<p>Ghetele de iarnă {PRIMIGI} PTIGT 23547 sunt {A("/categorie/ghete-cizme/", "ghete înalte pentru fete")}, roz, din piele întoarsă și material textil, cu membrana GORE-TEX®, care ține umezeala și vântul afară. Sunt pentru joaca de iarnă, în zilele reci.</p>'
  '<p>Talpa flexibilă lasă piciorul să se miște natural, iar aricii permit încălțatul rapid, fără ajutor. Călcâiul e întărit, deci gheata ține piciorul la mers.</p>'
  '<p>Pentru frig:</p>'
  + L(('Interior', 'cu pluș moale.'), ('Partea de sus', 'înaltă, ține căldura.'), ('Talpă', 'din material sintetic.'))
  + '<p>Numerele 20-29 corespund, în mare, vârstei de 1-5 ani.</p>',
  [('cod', 'Ghetele de iarnă Primigi PTIGT 23547'), ('înalte', 'încălțăminte înaltă pentru copii'), ('material', 'confecționată din piele întoarsă și material textil'),
   ('GORE-TEX', 'Tehnologia GORE-TEX® oferă protecție împotriva umezelii și vântului'), ('iarnă', 'jocurilor de iarnă'), ('talpă flexibilă', 'Talpă flexibilă favorizează mișcarea naturală a piciorului'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă'), ('călcâi', 'Călcâiul întărit'), ('pluș', 'Pluș moale în interiorul ghetelor'),
   ('căldură', 'Partea superioară înaltă , confecționată din piele întoarsă și material textil, ajută la menținerea căldurii'), ('talpă', 'Material sintetic')],
  {'Model': 'Primigi PTIGT 23547', 'Material': 'piele întoarsă și textil, interior textil cu pluș', 'Caracteristici': 'GORE-TEX®, arici, talpă flexibilă', 'Cod produs': 'PTIGT 23547'})

w(9496,
  f'<p>{PRIMIGI} PBYGT 23864 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete de iarnă unisex")}, bleumarin, înalte, din piele întoarsă, cu membrana GORE-TEX®, care păstrează piciorul uscat, și interior izolat pentru zilele reci. Sunt făcute cu tehnologia Primigi × SIPeP, care ține cont de anatomia piciorului copilului.</p>'
  '<p>Au și șireturi, și benzi cu arici, deci se strâng exact pe picior, mai fin decât doar cu arici, inclusiv la un picior mai îngust.</p>'
  '<p>Alte detalii:</p>'
  + L(('Vârf', 'rotund, întărit.'), ('Călcâi', 'întărit.'), ('Branț', 'detașabil, din material textil.'))
  + '<p>Mărimile 25-30 sunt pentru copii de undeva între 2 și 7 ani.</p>',
  [('cod', 'Primigi Încălțăminte de iarnă pentru copii bleumarin PBYGT 23864'), ('înalte', 'încălțăminte înaltă pentru copii'), ('material', 'Piele întoarsă'),
   ('GORE-TEX', 'Membrana GORE-TEX® ajută la menținerea uscăciunii picioarelor'), ('izolat', 'Interiorul izolat al modelului ajută la menținerea căldurii în zilele reci'),
   ('SIPeP', 'Tehnologia Primigi × SIPeP'), ('anatomie', 'ținând cont de anatomia acestuia'), ('închidere', 'Combinația de șireturi și benzi cu arici permite o ajustare precisă'),
   ('vârf', 'Vârf rotund, întărit și călcâi întărit'), ('branț', 'Branțul detașabil din material textil')],
  {'Model': 'Primigi PBYGT 23864', 'Material': 'piele întoarsă, interior textil izolat', 'Caracteristici': 'GORE-TEX®, Primigi × SIPeP, șireturi și arici, branț detașabil', 'Cod produs': 'PBYGT 23864'})

w(9498,
  f'<p>Blugii {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} BAGGY KB0KB10468 sunt {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "blugi pentru băieți")} în culoarea albastru, cu croială lejeră baggy și finisaj cu efect prespălat. Materialul e un amestec de bumbac și lyocell, pentru ținute casual de zi cu zi.</p>'
  '<p>Croiala largă lasă loc pe picior și la un copil mai plinuț, iar talia normală cu bandă elastică se strânge pe un băiat mai slab. Denimul e neelastic și își păstrează forma.</p>'
  '<p>Pe scurt:</p>'
  + L(('Buzunare', 'laterale și la spate.'), ('Talie', 'normală, cu bandă elastică.'), ('Compoziție', '61% bumbac, 39% lyocell.'))
  + '<p>Mărimile 104-176 se potrivesc, în general, copiilor de 4-16 ani.</p>',
  [('model', 'Tommy Hilfiger Blugi pentru copii BAGGY albaștri KB0KB10468'), ('croială', 'Croială lejeră baggy'), ('prespălat', 'Finisaj cu efect prespălat'),
   ('material', 'combinație de bumbac și lyocell'), ('casual', 'ținute casual, de zi cu zi'), ('talie', 'Talie normală cu bandă elastică'),
   ('neelastic', 'Denim neelastic – permite menținerea formei'), ('buzunare', 'Buzunare laterale și la spate'), ('compoziție', '61% Bumbac, 39% Lyocell')],
  {'Model': 'Tommy Hilfiger BAGGY', 'Material': '61% bumbac, 39% lyocell', 'Caracteristici': 'croială baggy, talie elastică, denim neelastic', 'Cod produs': 'KB0KB10468'})

w(9502,
  f'<p>{REIMA} Kumpula este o {A("/categorie/geci-jachete/", "geacă izolată pentru fete")}, neagră, matlasată, din poliester reciclat cu membrană, care o face impermeabilă. Finisajul BIONIC-FINISH® ECO respinge apa fără acoperirea DWR clasică, iar modelul are certificările Bluesign® și GRS.</p>'
  '<p>Croiala e simplă și dreaptă, cu loc pentru un pulover dedesubt. Gulerul ridicat ține gâtul la cald, iar gluga se detașează când nu e nevoie de ea.</p>'
  '<p>Construcția pe scurt:</p>'
  + L(('Închidere', 'fermoar și capsă.'), ('Buzunare', 'în față.'), ('Căptușeală', '100% poliester reciclat.'), ('Umplutură', '100% poliester reciclat.'))
  + '<p>Mărimile 104-164 sunt pentru copii de aproximativ 4-14 ani.</p>',
  [('cod', 'Reima Kumpula negru 5100361A'), ('izolat', 'Model izolat cu captuseala'), ('membrană', 'membrană respirabilă care asigură impermeabilizarea'), ('matlasare', 'Matlasare'),
   ('material', '100% Poliester reciclat cu strat de poliuretan'), ('BIONIC', 'BIONIC-FINISH® ECO - o alternativa ecologica la acoperirea traditionala, hidrofoba DWR'),
   ('Bluesign', 'Model certificat Bluesign® Standard'), ('GRS', 'GRS (Global Recycle Standard)'), ('croială', 'Tăiere simplă, fără blocare'),
   ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('glugă', 'Gluga detasabila'), ('închidere', 'Fixare cu fermoar si snap'),
   ('buzunare', 'In fata buzunare'), ('căptușeală', 'Captuseala: 100% Poliester reciclat'), ('umplutură', 'Umplutura: 100% Poliester reciclat')],
  {'Model': 'Reima Kumpula', 'Material': '100% poliester reciclat cu strat de poliuretan', 'Caracteristici': 'izolată, impermeabilă, glugă detașabilă, Bluesign®, GRS', 'Cod produs': '5100361A'})

w(9513,
  f'<p>{REIMA} Ohitus sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")}, bleumarin, ușori și rezistenți, cu fața din material textil și sintetic, pentru joaca de primăvară, vară și toamnă. Construcția lor e gândită pentru dezvoltarea naturală a picioarelor.</p>'
  '<p>Branțul detașabil are imprimeu cu ghid de mărime, deci se vede ușor dacă piciorul mai are loc. Înșiretarea rapidă îi lasă pe copii să se încalțe singuri, iar găicile de la spate și de pe limbă ajută la tras pe picior.</p>'
  '<p>Mai au:</p>'
  + L(('Călcâi', 'ușor rigidizat.'), ('Înălțime', 'până la gleznă.'), ('Talpă', 'tip platformă, din cauciuc și spumă.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Numerele 28-40 sunt pentru copii de la cam 4 ani în sus.</p>',
  [('model', 'Reima Ohitus sneakers pentru copii bleumarin 5400174A'), ('ușori', 'combină lejeritatea și rezistența'), ('material', 'Material textil, Material sintetic'),
   ('sezon', 'zilele de primăvară, vară și toamnă'), ('dezvoltare', 'sprijină dezvoltarea naturală a picioarelor'), ('branț', 'Branțul detașabil cu imprimeu facilitează ajustarea precisă a mărimii'),
   ('înșiretare', 'Sistemul de înșiretare rapidă permite copiilor să se încalțe și să se descalțe singuri'), ('găici', 'Găicile de la spate și de pe limbă'),
   ('călcâi', 'Contragreutatea călcâiului ușor rigidizată'), ('gleznă', 'Construcția părții superioare până la gleznă'), ('talpă', 'Talpa tip platformă din cauciuc și spumă'),
   ('interior', 'Interiorul căptușit cu material textil')],
  {'Model': 'Reima Ohitus', 'Material': 'textil și sintetic, talpă din cauciuc și spumă', 'Caracteristici': 'branț cu ghid de mărime, înșiretare rapidă, până la gleznă', 'Cod produs': '5400174A'},
  varsta_txt='de la 4 ani în sus')

w(9530,
  f'<p>{REIMA} Valoa sunt {A("/categorie/unisex-incaltaminte-sandale/", "sandale sport unisex")}, bej, de tip barefoot, cu talpă plată și flexibilă din cauciuc, care lasă piciorul să se miște natural. Fața e din material textil, iar stilul sportiv le face bune la joacă și în excursii.</p>'
  '<p>Căptușeala elastică din interior ușurează încălțatul, iar branțurile detașabile Happy Fit ajută la alegerea mărimii și se scot la curățat.</p>'
  '<p>Pe scurt:</p>'
  + L(('Construcție', 'barefoot, cu talpă plată.'), ('Interior', 'material sintetic și textil.'), ('Produs', 'vegan.'))
  + '<p>Numerele 28-40 se poartă, de regulă, de la 4 ani în sus.</p>',
  [('model', 'Reima Sandale sport pentru copii Valoa bej 5400157C'), ('barefoot', 'Construcție de tip Barefoot cu talpă plată'), ('talpă', 'Talpă flexibilă din cauciuc'),
   ('față', 'Față din material textil'), ('sport', 'Stil sportiv'), ('excursii', 'diverselor jocuri și excursii'), ('căptușeală', 'cu o căptușeală elastică ce facilitează încălțarea'),
   ('Happy Fit', 'Branțuri detașabile Happy Fit'), ('igienă', 'potrivirea mărimii și menținerea igienei'), ('interior', 'Interior din material sintetic și textil'),
   ('vegan', 'Produs vegan')],
  {'Model': 'Reima Valoa', 'Material': 'textil, talpă din cauciuc', 'Caracteristici': 'barefoot, Happy Fit, talpă plată flexibilă, vegan', 'Cod produs': '5400157C'})
print('lot 23 scris')
