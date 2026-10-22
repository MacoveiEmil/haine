import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
PRIMIGI = A('/brand/primigi/', 'Primigi')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
ADU = '/categorie/unisex-incaltaminte-adidasi/'
NOAPA = 'Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'

w(9389,
  f'<p>Adidașii {REIMA} Sankari roz sunt {A(ADU, "adidași unisex")} cu membrană, care îi face respirabili și rezistenți la apă. Fața, din textil și material sintetic, nu se înmoaie ușor, iar fibrele vin din procese de producție durabile.</p>'
  '<p>Vârful lat nu ciupește degetele, iar șireturile rapide cu opritor se strâng și se desfac repede. Contrafortul rigid ține călcâiul pe loc, iar branțul textil detașabil are imprimeu pentru verificarea mărimii. Talpa e din cauciuc flexibil.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'scurt.'))
  + '<p>Numerele 32-40 se poartă de pe la 8 ani în sus.</p>',
  [('model', 'Sankari'), ('culoare', 'culoarea roz'), ('membrană', 'Model cu membrană care asigura respirabilitate și rezistenta la apă'),
   ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'), ('durabil', 'produse folosind procese de productie durabile'),
   ('vârf', 'Cutia lată a degetelor previne ciupirea degetelor'), ('șireturi', 'Sistemul rapid de șireturi cu opritoare'),
   ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece'), ('branț', 'Modelul cu branț textil, detașabil, cu imprimeu'),
   ('talpă', 'Talpa flexibilă din cauciuc'), ('gambă', 'Material sintetic, Material textil'), ('interior', 'Material textil'), ('profil', 'scurt')],
  {'Model': 'Reima Sankari', 'Material': 'textil și material sintetic', 'Caracteristici': 'membrană, șireturi rapide, branț cu imprimeu', 'Cod produs': '5400160A'},
  notes=[NOAPA])

w(9396,
  f'<p>Bocancii {PRIMIGI} 2358411 roz sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete pentru bebeluși")} de tranziție, cu fața din material sintetic cu finisaj strălucitor. Urcă peste gleznă, iar interiorul neizolat îi face potriviți pentru zilele mai călduroase de primăvară sau toamnă.</p>'
  '<p>Se încheie cu fermoar și au șireturi pentru reglaj. Branțul e din piele naturală, călcâiul e întărit, iar talpa plată e din cauciuc. Vârful e rotund.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'material sintetic.'), ('Interior', 'piele naturală, material textil.'), ('Lungime branț', '13 cm la numărul 23.'))
  + '<p>Numerele 21-26 sunt pentru copii de aproximativ 1-4 ani.</p>',
  [('cod', '2358411'), ('culoare', 'culoarea roz'), ('strălucitor', 'Finisaj strălucitor al materialului'), ('sintetic', 'Față din material sintetic'),
   ('tranziție', 'conceput pentru sezoanele de tranziție'), ('gleznă', 'Construcție peste gleznă'), ('neizolat', 'Interior neizolat'),
   ('călduroase', 'potrivit pentru zilele mai călduroase de tranziție'), ('fermoar', 'Închidere cu fermoar'), ('șireturi', 'Șireturi'),
   ('branț', 'Branț din piele naturală'), ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpă plată din cauciuc'), ('vârf', 'rotund'),
   ('interior', 'Interior:Piele naturală, Material textil'), ('lungime', 'Lungimea branțului este: 13 cm'), ('mărime', 'Dimensiuni indicate pentru mărimea: 23')],
  {'Model': 'Primigi 2358411', 'Material': 'material sintetic, branț din piele', 'Caracteristici': 'peste gleznă, fermoar și șireturi, neizolați', 'Cod produs': '2358411'})

w(9404,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8883533 roz sunt {A("/categorie/ghete-cizme/", "cizme de iarnă pentru fete")} izolate, din textil și piele întoarsă, cu membrană GORE-TEX foarte subțire, impermeabilă, rezistentă la vânt și respirabilă. Talpa din cauciuc e groasă, profilată, antiderapantă și rezistentă la deteriorare.</p>'
  '<p>Partea de sus ridicată sprijină glezna pe teren denivelat, vârful lat nu ciupește degetele, iar velcro-ul le face ușor de pus. Inserția textilă detașabilă se curăță ușor, iar branțul e anatomic.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele întoarsă.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 31-35 sunt pentru copii de cam 6-11 ani.</p>',
  [('cod', '8883533'), ('culoare', 'culoarea roz'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Izolare: izolat'),
   ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant si respirabila'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('groasă', 'groasă, profilată'), ('antiderapantă', 'antiderapantă'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('vârf', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('velcro', 'Închiderea cu velcro'), ('inserție', 'Inserție textilă detașabilă, ușor de curățat'), ('anatomic', 'anatomic'),
   ('gambă', 'Material textil, Piele intoarsa'), ('interior', 'Material textil'), ('profil', 'înalt')],
  {'Model': 'Primigi 8883533', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, velcro, talpă antiderapantă', 'Cod produs': '8883533'},
  notes=['Descrierea pomenește un interior din lână, dar compoziția interiorului e material textil; nu am scris lână.'])

w(9413,
  f'<p>Adidașii {REIMA} Kiritin violet pe site (albaștri la magazin) sunt {A(ADU, "adidași unisex")} ușori, din textil și piele ecologică, pentru purtat zilnic. Fața are finisaj hidrofob, care ține umezeala afară pe vreme urâtă.</p>'
  '<p>Inserțiile detașabile Happy Fit ajută la alegerea numărului, iar șireturile rapide cu opritor și bucla de la spate fac încălțatul mai ușor. Elementele reflectorizante se văd după lăsarea întunericului, iar talpa din cauciuc rezistă la deteriorare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material sintetic, material textil.'), ('Profil', 'scurt.'))
  + '<p>Numerele 28-38 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'Kiritin'), ('culoare', 'Culoare: Albastru'), ('ușor', 'Model ușor și confortabil, ideal pentru purtarea zilnică'), ('piele', 'pielea ecologică'),
   ('hidrofob', 'Finisajul hidrofob al feței superioare nu permite umezelii să pătrundă în interior'), ('Happy Fit', 'Inserțiile detașabile Happy Fit'),
   ('șireturi', 'Sistemul rapid de șireturi cu opritoare'), ('buclă', 'Bucla de la spate'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('gambă', 'Material sintetic, Material textil'), ('profil', 'scurt')],
  {'Model': 'Reima Kiritin', 'Material': 'textil, piele ecologică', 'Caracteristici': 'hidrofobi, Happy Fit, reflectorizante', 'Cod produs': '5400134B'},
  notes=['Culoarea din titlul site-ului (violet) nu se potrivește cu cea a magazinului (albastru).', NOAPA])

w(9418,
  f'<p>Geaca {TH} KG0KG08861 albă este o {A("/categorie/geci-jachete/", "geacă de iarnă pentru fete")} izolată, din material matlasat cu izolație sintetică groasă, realizată parțial din poliester reciclat. Gulerul ridicat și gluga încorporată adaugă căldură.</p>'
  '<p>Fermoarul pe toată lungimea are clapă antifurtună prinsă cu velcro, iar mânecile sunt finisate cu manșetă. Tăietura e simplă, fără blocare, iar căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 sunt pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'KG0KG08861'), ('culoare', 'culoarea alb'), ('izolat', 'Model izolat confecționat din material matlasat cu izolatie sintetica'), ('groasă', 'groasă'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('glugă', 'Gluga încorporată'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă antifurtună cu velcro'), ('manșetă', 'Finisaj din manseta'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('material', '100% Poliester'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KG0KG08861', 'Material': '100% poliester', 'Caracteristici': 'izolație groasă, glugă, clapă antifurtună', 'Cod produs': 'KG0KG08861'})

w(9432,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8858911 bleumarin sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} ușor izolate, din piele naturală, piele întoarsă și textil, cu membrană GORE-TEX subțire, impermeabilă, rezistentă la vânt și respirabilă. Talpa din cauciuc e antiderapantă și durabilă.</p>'
  '<p>Partea de sus ridicată sprijină glezna pe suprafețe neuniforme, vârful e lat și rigidizat, iar contrafortul rigid ține călcâiul pe loc. Se închid cu velcro, deci se încalță ușor.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele naturală, piele întoarsă.'), ('Interior', 'material sintetic.'), ('Profil', 'înalt.'))
  + '<p>Numerele 25-29 se potrivesc orientativ copiilor de 2-5 ani.</p>',
  [('cod', '8858911'), ('culoare', 'culoarea bleumarin'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Izolare: usor izolat'),
   ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant si respirabila'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('antiderapantă', 'cu bandă de rulare, antiderapantă'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('neuniforme', 'suprafețe neuniforme'), ('vârf', 'Cutia lată a degetelor'),
   ('rigidizat', 'rigidizat'), ('călcâi', 'Contorul de călcâi rigid'), ('velcro', 'Închiderea cu velcro'), ('gambă', 'Material textil, Piele naturala, Piele intoarsa'),
   ('interior', 'Material sintetic'), ('profil', 'înalt')],
  {'Model': 'Primigi 8858911', 'Membrană': 'GORE-TEX', 'Caracteristici': 'ușor izolate, velcro, talpă antiderapantă', 'Cod produs': '8858911'},
  notes=['Magazinul descrie membrana ca 100% impermeabilă, dar are și formula că nu garantează impermeabilitatea completă.'])

w(9437,
  f'<p>Adidașii {A("/brand/biomecanics/", "Biomecanics")} 262133 roz sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} ușori, din textil și piele ecologică, creați împreună cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia. Se pun ușor și se potrivesc bine datorită închiderii cu velcro.</p>'
  '<p>Vârful e protejat, iar tăietura în formă de U lasă glezna să se miște liber. Inserția perforată ajută la confortul termic, iar branțul detașabil e antibacterian, profilat la mijloc. Bucla de la spate ajută la încălțat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Lungime branț', '14 cm la numărul 22.'), ('Talpă', 'material sintetic, profilată.'))
  + '<p>Numerele 19-25 sunt pentru copii de cam 1-3 ani.</p>',
  [('cod', '262133'), ('culoare', 'culoarea roz'), ('ușor', 'Model ușor și confortabil'), ('piele', 'pielea ecologică'),
   ('pediatri', 'create in cooperare cu medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'), ('velcro', 'Usor de imbracat si se potriveste bine datorita fixarii cu velcro'),
   ('vârf', 'Degetul securizat protejeaza degetele'), ('U', 'taieturi in forma de U'), ('glezna', 'permit gleznei sa se miste liber'),
   ('perforată', 'confort termic datorita capacitatii de evaporare si a insertiei perforate'), ('branț', 'Brant detasabil si antibacterian, profilat la mijlocul piciorului'),
   ('buclă', 'Bucla de la spate'), ('gambă', 'Material sintetic, Material textil'), ('lungime', 'Lungimea brantului pentru marimea este de: 14 cm'),
   ('mărime', 'Dimensiunile date pentru marimea: 22'), ('profilată', 'profilată')],
  {'Model': 'Biomecanics 262133', 'Material': 'textil, piele ecologică', 'Caracteristici': 'velcro, branț antibacterian, tăietură în U', 'Cod produs': '262133'})

w(9465,
  f'<p>Geaca {TH} KB0KB09814 bleumarin este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")} ușoară, matlasată, neizolată, dintr-un material foarte confortabil. Are guler moale, fără glugă, și căptușeală completă.</p>'
  '<p>Fermoarul pe toată lungimea are clapă de furtună prinsă cu capse. Buzunarele sunt decorate cu clape, iar înăuntru e un buzunar în plus pentru lucrurile mici. Magazinul precizează că nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 se potrivesc orientativ copiilor de 8-16 ani.</p>',
  [('cod', 'KB0KB09814'), ('culoare', 'culoarea bleumarin'), ('ușor', 'Model ușor confecționat din material matlasat'), ('neizolat', 'Model neizolat cu captuseala'),
   ('confortabil', 'material excepțional de confortabil'), ('guler', 'Model cu guler moale'), ('glugă', 'fără glugă'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă de furtună prinsă cu capse'), ('clape', 'Model cu buzunare, decorat cu clape'),
   ('interior', 'Un buzunar interior suplimentar'), ('impermeabil', 'fără impermeabilitate'), ('material', '100% Poliester'), ('umplutură', 'fără umplutură'),
   ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB09814', 'Material': '100% poliester', 'Caracteristici': 'matlasată, neizolată, clapă cu capse', 'Cod produs': 'KB0KB09814'})

w(9485,
  f'<p>Adidașii {A("/brand/geox/", "Geox")} FADINLIGHT bleumarin sunt {A("/categorie/adidasi/", "adidași pentru fete")} ușori, din textil și piele ecologică, cu lumini în talpă care se aprind la mers. Sistemul Geox Respira are talpă în trei straturi, perforată, pentru ventilare.</p>'
  '<p>Vârful e rotund și ușor rigid, iar degetele au loc. Contrafortul rigid ține călcâiul, iar velcro-ul și bucla de la spate îi fac ușor de pus și de scos. Talpa exterioară din cauciuc rezistă la deteriorare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'scurt.'))
  + '<p>Numerele 32-35 sunt pentru copii de aproximativ 8-11 ani.</p>',
  [('model', 'FADINLIGHT'), ('culoare', 'culoarea bleumarin'), ('ușor', 'Model ușor și confortabil'), ('piele', 'pielea ecologica'),
   ('lumini', 'Pe talpă, lumini care se aprind în timp ce mergi'), ('Respira', 'Sistemul Geox Respira'), ('straturi', 'talpei in trei straturi cu sistemul de perforari'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('călcâi', 'Contorul de călcâi rigid'), ('velcro', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('gambă', 'Material sintetic, Material textil'), ('profil', 'scurt')],
  {'Model': 'Geox FADINLIGHT', 'Talpă': 'cauciuc, cu lumini, Geox Respira', 'Caracteristici': 'lumini în talpă, velcro, ușori', 'Cod produs': 'J56M4F.054AJ'})

w(9504,
  f'<p>Geaca {REIMA} Alaniva albastră este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} ușor izolată, din poliester parțial reciclat, cu certificare Bluesign și finisaj hidrofob BIONIC-FINISH ECO. Membrana ReimaTec apără de ploaie și vânt, iar cusăturile sudate țin umezeala afară.</p>'
  '<p>Gulerul ridicat și gluga detașabilă apără de frig, iar fermoarul are apărătoare pentru bărbie. Înăuntru are centură de zăpadă și o etichetă pentru adresă, iar buzunarele sunt multe.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Glugă', 'detașabilă.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 104-164 sunt pentru copii de cam 4-14 ani.</p>',
  [('model', 'Alaniva'), ('culoare', 'Culoare albastru'), ('izolat', 'Model usor izolat confecționat material textil cu model'), ('reciclat', 'realizat partial din poliester reciclat'),
   ('Bluesign', 'Model certificat Bluesign® Standard'), ('BIONIC', 'BIONIC-FINISH ECO este o finisare hidrofoba ecologica'),
   ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'), ('sudate', 'Cusăturile sudate măresc protecția împotriva umezelii'),
   ('guler', 'Gulerul ridicat și gluga detașabilă'), ('bărbie', 'apărătoare pentru bărbie'), ('centură', 'o centură de zăpadă încorporată'),
   ('etichetă', 'Înăuntru este cusută o etichetă cu adresa'), ('buzunare', 'Sistemul extins de buzunare'), ('material', '100% Poliester reciclat'), ('croială', 'Croială: regular fit')],
  {'Model': 'Reima Alaniva', 'Material': '100% poliester reciclat', 'Caracteristici': 'ReimaTec, cusături sudate, centură de zăpadă', 'Cod produs': '5100392A'},
  notes=['Titlul site-ului are „Alaniva” în locul culorii; culoarea e cea de la magazin (albastru).', NOAPA])
