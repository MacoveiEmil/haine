import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
CURAT = ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')
PODO = ('Podology', 'Tehnologia Biomecanics Podology Partnership')

w(12832,
  f'<p>Adidașii {TH} T3A9-34263 roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din material textil, piele ecologică și piele întoarsă ecologică, ușori, pentru purtarea zilnică. Șireturile plate nu apasă pe arcada piciorului.</p>'
  '<p>Cutia rotundă e moale, spatele călcâiului e rigidizat, iar branțul e profilat.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, durabilă.'), ('Branț', 'profilat.'))
  + '<p>Numerele 35-40 sunt pentru fete de la aproximativ 10 ani în sus; la 38 branțul are 24 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea roz, T3A9-34263'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatie de material textil, piele ecologica si piele intoarsa'),
   ('ușor', 'Model ușor și confortabil'), ('șireturi', 'Sireturile plate elimina punctele de presiune de pe arcada piciorului'), ('vârf', 'Cutie rotunda si moale'),
   ('călcâi', 'Spatele calcaiului rigidizat'), ('branț', 'Brant profilat'), CURAT, TALPA, ('lungime', 'Lungimea brantului pentru marimea este de: 24 cm')],
  {'Model': 'Tommy Hilfiger T3A9-34263', 'Material': 'textil, piele ecologică și imitație de piele întoarsă, talpă din cauciuc', 'Caracteristici': 'șireturi plate, branț profilat', 'Cod produs': 'T3A9-34263'})

w(12834,
  f'<p>Adidașii {TH} T3A9-35086 maro sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} uni, cu profil jos și guler ușor întărit, din imitație de piele ușor de curățat, în stil casual. Se leagă cu șiret clasic, care se reglează după forma piciorului.</p>'
  '<p>Talpa plată din cauciuc, groasă de 2-4 cm, lasă piciorul în poziție naturală la mers, iar călcâiul întărit îl ține pe loc.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textilă.'), ('Branțuri', 'textile, detașabile, se pot înlocui.'), ('Închidere', 'șiret.'))
  + '<p>Numerele 35-40 se potrivesc copiilor de la vreo 10 ani în sus, orientativ.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii maro T3A9-35086'), ('uni', 'Model uni al părții superioare'), ('profil', 'Profilul jos al părții superioare asigură libertatea de mișcare, iar gulerul ușor întărit susține glezna'),
   ('imitație', 'Partea superioară din imitație de piele conferă încălțămintei un aspect estetic și facilitează menținerea curățeniei'), ('casual', 'Stilul lor casual'),
   ('șiret', 'Închidere clasică cu șiret permite ajustarea individuală'), ('talpă', 'Talpă plată cu o grosime de 2 până la 4 cm favorizează poziția naturală a piciorului'),
   ('călcâi', 'Călcâi întărit'), ('căptușeală', 'Interior căptușit cu material textil'), ('branț', 'Branțuri detașabile din material textil facilitează igiena și permit înlocuirea')],
  {'Model': 'Tommy Hilfiger T3A9-35086', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'șiret, branțuri detașabile', 'Cod produs': 'T3A9-35086'})

w(12835,
  f'<p>{GEOX} LOFTUS J65M2B albi sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din material textil și sintetic, ușori, pentru purtarea zilnică. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos, fără legat.</p>'
  '<p>Cutia rotundă, ușor întărită, apără degetele, iar contrafortul rigid ține călcâiul în pantof.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 28-35 se potrivesc fetelor de cam 4-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii LOFTUS culoarea alb, J65M2B.0BC14'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu cel sintetic'),
   ('ușor', 'Model ușor și confortabil'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('vârf', 'Cutie rotunda, usor intarita'), ('călcâi', 'Contorul de călcâi rigid'), RESPIRA, CURAT, TALPA],
  {'Model': 'Geox LOFTUS', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J65M2B.0BC14'})

w(12846,
  f'<p>Codul IG0IG02056 de la {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} vine și în roz: o {A("/categorie/geci-jachete/", "geacă pentru fete")} matlasată, ușor izolată, din material neted, cu croială lejeră care nu încurcă mișcarea. Are glugă și logo brodat pe față.</p>'
  '<p>Se închide cu fermoar, iar mânecile se termină cu manșetă. Izolația ușoară e prinsă pe căptușeală, iar exteriorul e matlasat.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '100% poliester.'), ('Glugă', 'da.'), ('Logo', 'brodat pe față.'))
  + '<p>Au mai rămas mărimile 104-116, pentru fete de aproximativ 4-6 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă copii culoarea roz, IG0IG02056'), ('matlasat', 'Matlasat'), ('izolat', 'Model usor izolat pe captuseala'), ('neted', 'Material neted'),
   ('croială', 'Croială lejeră pentru libertate totală de mișcare'), ('glugă', 'Model cu gluga'), ('logo', 'Logo-ul mărcii brodat pe față'),
   ('fermoar', 'Incheiere cu fermoar'), ('manșetă', 'Finisaj din manseta'), ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans IG0IG02056', 'Material': '100% poliester, izolație ușoară', 'Caracteristici': 'matlasată, glugă, logo brodat', 'Cod produs': 'IG0IG02056'})

w(12848,
  f'<p>{GEOX} WASHIBA J45HXB albi sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din material textil și piele ecologică, ușori, care se închid cu velcro, deci se încalță și se descalță repede. Cutia rotundă e întărită și apără degetele.</p>'
  '<p>Contrafortul rigidizat sprijină călcâiul și glezna, iar interiorul textil se păstrează curat ușor.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, perforată.'), ('Talpă exterioară', 'din cauciuc, rezistentă.'), ('Partea de sus', 'imitație de piele și textil.'))
  + '<p>Numerele 28-35 merg la fete de în jur de 4-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii WASHIBA culoarea alb, J45HXB.0003W'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), CURAT, RESPIRA, TALPA],
  {'Model': 'Geox WASHIBA', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira', 'Cod produs': 'J45HXB.0003W'})

w(12850,
  f'<p>Pantofii {BIO} 261152 maro sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} din piele naturală și material sintetic, ușor de îngrijit, în stil casual, clasic și streetwear. Tehnologia BioTEX îi face mai rezistenți la umezeală pe ploaie ușoară.</p>'
  '<p>Vârful lat, rotund și întărit lasă degetele să se miște liber, iar aricii cu curea reglabilă fac încălțatul rapid. Talpa flexibilă din cauciuc urmează mișcarea piciorului.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Branțuri', 'textile, detașabile, antibacteriene și anti-miros.'), ('Interior', 'material textil moale.'), ('Călcâi', 'întărit.'), ('Podology Partnership', 'tehnologia Biomecanics.'))
  + '<p>Numerele 19-23 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele maro 261152'), ('material', 'Partea superioară din combinație de piele naturală și materiale sintetice contribuie la durabilitate și ușurință în îngrijire'),
   ('stil', 'Stil universal casual, clasic și streetwear'), ('BioTEX', 'Tehnologia BioTEX contribuie la rezistența crescută la umiditate în precipitații ușoare'),
   ('vârf', 'Vârf lat și rotund cu întărire'), ('arici', 'Închidere cu arici și curea reglabilă'), ('talpă', 'Talpă flexibilă din cauciuc permite mișcarea liberă a piciorului'),
   ('branț', 'Branțuri detașabile din material textil , antibacteriene și anti-miros'), ('interior', 'Interior din material textil contribuie la moliciune'), ('călcâi', 'Călcâi întărit'), PODO],
  {'Model': 'Biomecanics 261152', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'BioTEX, arici cu curea reglabilă, branț antibacterian', 'Cod produs': '261152'})

w(12859,
  f'<p>{BIO} 261210 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, cu profil înalt care susține glezna, din piele naturală și material sintetic. Stabilizatorii laterali și călcâiul întărit țin piciorul în poziție corectă la mișcare.</p>'
  '<p>Aricii cu curea reglabilă fac încălțatul rapid, iar talpa din cauciuc are bandă de rulare care ține bine pe diverse suprafețe. Pielea dă pantofului un aspect îngrijit.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Branț', 'detașabil, aerisit.'), ('Interior', 'material textil.'), ('Podology Partnership', 'sprijin pentru dezvoltarea piciorului.'))
  + '<p>Numerele 28-34 se potrivesc băieților de cam 4-11 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele verzi 261210'), ('profil', 'Profilul înalt al părții superioare susține glezna copilului'),
   ('material', 'Partea superioară din piele naturală și sintetică contribuie la durabilitatea și estetica'), ('stabilizatori', 'Stabilizatori laterali ajută la menținerea piciorului într-o poziție corectă'),
   ('călcâi', 'Călcâi întărit'), ('arici', 'Închidere cu arici și curea reglabilă'), ('talpă', 'Talpă de cauciuc cu bandă de rulare asigură o aderență bună pe diverse suprafețe'),
   ('branț', 'Branț detașabil, respirabil'), ('interior', 'Material textil'), PODO],
  {'Model': 'Biomecanics 261210', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'stabilizatori laterali, arici cu curea reglabilă, profil înalt', 'Cod produs': '261210'})

w(12872,
  f'<p>Geaca bomber {TH} KB0KB10451 bleumarin este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} uni, ușor vătuită, cu umplutură sintetică subțire, pentru sezoanele de tranziție. Croiala regular fit lasă loc de mișcare, iar gluga integrată apără de vânt și de ploaia ușoară.</p>'
  '<p>Fermoarul merge pe toată lungimea, iar manșetele reglabile cu bandă elastică și tivul cu elastic se strâng după copil.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Căptușeală', 'sintetică, completă.'), ('Buzunare', 'laterale.'), ('Lungime', 'până la șolduri.'), ('Material', '100% nailon.'))
  + '<p>Gama e largă, 98-176, deci acoperă copii de aproximativ 3-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă bomber pentru copii bleumarin KB0KB10451'), ('uni', 'Modelul uni bleumarin'), ('vătuit', 'un model ușor vătuit pentru băieți'),
   ('umplutură', 'Umplutura sintetică subțire ajută la menținerea căldurii în timpul sezoanelor de tranziție'), ('croială', 'Croiala regular fit favorizează libertatea de mișcare'),
   ('glugă', 'Gluga integrată oferă protecție suplimentară împotriva vântului și a ploii ușoare'), ('fermoar', 'Închiderea cu fermoar pe toată lungimea'),
   ('manșete', 'Manșetele reglabile cu bandă elastică și tivul cu elastic'), ('căptușeală', 'Căptușeala completă sintetică'), ('buzunare', 'Buzunarele laterale practice'),
   ('lungime', 'Lungimea până la șolduri'), ('material', '100% Nailon')],
  {'Model': 'Tommy Hilfiger KB0KB10451 (bomber)', 'Material': '100% nailon, umplutură sintetică subțire', 'Caracteristici': 'glugă integrată, fermoar, manșete reglabile', 'Cod produs': 'KB0KB10451'})

w(12873,
  f'<p>Pantofii {BIO} 261127 bleumarin sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} sport din piele naturală netedă, gândiți împreună cu podologi, în stil casual și streetwear. Vârful rotund e cauciucat și apără de zgârieturi, iar stabilizatorii laterali și călcâiul întărit țin piciorul corect.</p>'
  '<p>Banda reglabilă cu arici se strânge rapid după picior.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare, groasă de 1 cm.'), ('Branț', 'textil, detașabil, antibacterian.'), ('Interior', 'material textil.'))
  + '<p>Numerele 18-25 se potrivesc copiilor de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele bleumarin 261127'), ('sport', 'combină stilul sportiv cu funcționalitatea'), ('piele', 'Partea superioară din piele naturală'),
   ('neted', 'Textura netedă a materialului'), ('podologi', 'Concepuți în colaborare cu podologii'), ('stil', 'Stil universal casual și streetwear'),
   ('vârf', 'Vârf rotund, cauciucat , care permite mișcarea liberă a degetelor și protejează suplimentar împotriva abraziunilor'),
   ('stabilizatori', 'Stabilizatori laterali și călcâi întărit'), ('arici', 'Închidere cu bandă reglabilă cu arici'), ('talpă', 'Talpă de cauciuc cu bandă de rulare'),
   ('grosime', 'Talpă cu o grosime de 1 cm'), ('branț', 'Branț detașabil din material textil , respirabil și antibacterian'), ('interior', 'Interior din material textil')],
  {'Model': 'Biomecanics 261127', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'vârf cauciucat, stabilizatori laterali, bandă cu arici', 'Cod produs': '261127'})

w(12878,
  f'<p>{BIO} 261154 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albaștri, din piele naturală, cu motiv animal, gândiți împreună cu podologi pentru etapele de creștere ale piciorului. Spațiul extins de la degete le lasă să stea liber, iar talpa flexibilă din cauciuc urmează mișcarea piciorului.</p>'
  '<p>Baretele reglabile cu arici fac încălțatul rapid, iar călcâiul moale nu roade pielea.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Stabilizatori', 'laterali, pentru poziția corectă.'), ('Branț', 'antibacterian și anti-miros.'), ('Interior', 'material textil.'))
  + '<p>Au mai rămas numerele 24-26, pentru copii de aproximativ 2-4 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele albastri 261154'), ('piele', 'Partea superioară din piele naturală'), ('animal', 'Modelul cu motiv animal'),
   ('podologi', 'Proiectați în colaborare cu podologi, ținând cont de etapele de dezvoltare ale piciorului copilului'), ('degete', 'Spațiu extins în zona degetelor'),
   ('talpă', 'Talpă flexibilă din cauciuc susține mișcarea naturală a piciorului'), ('arici', 'Barete reglabile cu închidere cu arici'),
   ('călcâi', 'Călcâi moale mărește confortul la purtare și protejează călcâiul delicat împotriva abraziunilor'), ('stabilizatori', 'Stabilizatori laterali'),
   ('branț', 'Branț antibacterian și anti-miros'), ('interior', 'Material textil')],
  {'Model': 'Biomecanics 261154', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, stabilizatori laterali, branț antibacterian', 'Cod produs': '261154'})
