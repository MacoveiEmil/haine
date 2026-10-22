import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
CURAT = ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')

w(12652,
  f'<p>{GEOX} THELEVEN gri sunt {A("/categorie/adidasi/", "adidași pentru fete")} joși, din piele naturală și piele ecologică, ușori, pentru purtarea zilnică. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos, fără legat.</p>'
  '<p>Cutia rotundă, întărită, apără degetele, iar contrafortul rigid ține călcâiul în pantof, ca să nu alunece la mers.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Partea de sus', 'piele naturală și material sintetic.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 24-27 se potrivesc fetițelor de cam 2-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii THELEVEN culoarea gri, J56HTA.077BC'), ('profil', 'Înălțime: jos'), ('material', 'combinația pielii naturale cu cea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid stabilizează călcâiul'), ('gamba', 'Material sintetic, Piele naturala'), CURAT, TALPA],
  {'Model': 'Geox THELEVEN', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, vârf întărit', 'Cod produs': 'J56HTA.077BC'})

w(12653,
  f'<p>{GEOX} CIUFCIUF sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz pentru cei mai mici, din piele întoarsă și material textil, cu elemente sintetice care întăresc construcția. Talpa are membrana microporoasă GEOX Respira, care scoate umezeala și ține piciorul uscat.</p>'
  '<p>Aricii o lasă pe fetiță să se încalțe și să se descalțe singură, iar talpa plată ține bine pe sol la joacă.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Branț', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Aici sunt numerele mici, 20-23, adică în jur de 1-3 ani.</p>',
  [('model', 'Geox CIUFCIUF sneakers pentru copii roz B455QB.0FU22'), ('material', 'Partea superioară din piele întoarsă și material textil'),
   ('sintetic', 'adăugarea de material sintetic contribuie la întărirea construcției pantofului'), ('Respira', 'talpă cu o membrană microporoasă care favorizează eliminarea umezelii, menținând picioarele uscate'),
   ('arici', 'facilitează încălțarea și descălțarea independentă'), ('căptușeală', 'căptușeala moale asigură confort'), ('branț', 'Branț din material textil'), ('talpă', 'Talpă plată din cauciuc'), ('aderență', 'contribuie la stabilitate și aderență')],
  {'Model': 'Geox CIUFCIUF', 'Material': 'piele întoarsă, textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici', 'Cod produs': 'B455QB.0FU22'})

w(12654,
  f'<p>{GEOX} PERTH J367RE sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} în culoarea albastru, cu profil jos, din material textil și piele ecologică, ușori, pentru purtarea zilnică. Șireturile elastice și cârligul permit încălțatul rapid, fără să mai legați.</p>'
  '<p>Talpa Geox Respira are trei straturi și perforări, pentru aerisirea piciorului.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Partea de sus', 'imitație de piele, sintetic și textil.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă.'))
  + '<p>Numerele 36-41 sunt pentru băieți de la aproximativ 12 ani în sus.</p>',
  [('model', 'Geox Sneakers pentru copii PERTH J367RE.054FU'), ('culoare', 'Culoare albastru'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), RESPIRA, CURAT, TALPA],
  {'Model': 'Geox PERTH', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice cu cârlig', 'Cod produs': 'J367RE.054FU'})

w(12655,
  f'<p>Adidașii {TH} T1X9-35219 bleumarin sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} sport, cu profil scurt și guler ușor întărit, din imitație de piele, ușor de ținut curată. Aricii le permit copiilor să se încalțe și să se descalțe singuri.</p>'
  '<p>Talpa plată din cauciuc are 2-4 cm grosime și izolează piciorul de sol, iar călcâiul întărit ține piciorul așezat corect.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Interior', 'material textil, aerisit.'), ('Închidere', 'arici.'), ('Partea de sus', 'material sintetic.'))
  + '<p>Numerele 30-34 merg la copii de vreo 6-11 ani, orientativ.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bleumarin T1X9-35219'), ('profil', 'Partea superioară cu profil scurt sprijină libertatea de mișcare, iar gulerul ușor întărit'),
   ('imitație', 'Material exterior din imitație de piele oferă încălțămintei un aspect estetic și facilitează menținerea curățeniei'),
   ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă de către copii'), ('talpă', 'Talpă plată din cauciuc'),
   ('grosime', 'Grosimea tălpii între 2-4 cm favorizează o izolare corespunzătoare de sol'), ('călcâi', 'Călcâi întărit favorizează stabilizarea piciorului'),
   ('interior', 'Interior din material textil favorizează ventilația')],
  {'Model': 'Tommy Hilfiger T1X9-35219', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, profil scurt, guler întărit', 'Cod produs': 'T1X9-35219'})

w(12658,
  f'<p>Adidașii {TH} T1AH-34225 roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu croială până la gleznă, din imitație de piele ușor de întreținut, pentru primăvară, vară și toamnă. Velcro-ul face încălțatul rapid și se reglează după picior.</p>'
  '<p>Gulerul moale cuprinde glezna fără să irite, iar contrafortul ușor rigidizat ține piciorul pe loc.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'din piele naturală, se adaptează la picior.'), ('Interior', 'textil și piele.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-26 se poartă cam între 1 și 4 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii roz T1AH-34225'), ('gleznă', 'Croiala până la gleznă'), ('imitație', 'Partea superioară din imitație de piele conferă pantofilor un aspect estetic, fiind ușor de întreținut'),
   ('sezon', 'zilele de primăvară și vară, precum și pentru aventurile de toamnă'), ('velcro', 'Închiderea practică cu velcro facilitează încălțarea și descălțarea rapidă, permițând ajustarea'),
   ('guler', 'Gulerul moale învăluie delicat glezna, minimizând riscul de iritații'), ('contrafort', 'Contravortul ușor rigidizat'),
   ('branț', 'Branțul din piele naturală asigură igiena și confortul, adaptându-se la forma piciorului'), ('interior', 'Piele naturală, Material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Tommy Hilfiger T1AH-34225', 'Material': 'imitație de piele, interior textil și piele, talpă din cauciuc', 'Caracteristici': 'velcro, branț din piele, croială până la gleznă', 'Cod produs': 'T1AH-34225'})

w(12659,
  f'<p>În mărimile 24-27, {GEOX} CIUFCIUF sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz cu profil scurt, dintr-un amestec de piele întoarsă, material textil și sintetic. Membrana GEOX Respira ajută la evacuarea umidității, deci piciorul rămâne uscat în pantof.</p>'
  '<p>Închiderea cu arici e rapidă și o ajută pe fetiță să se descurce singură, iar culoarea roz merge cu multe ținute.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Interior', 'căptușit cu textil, moale.'), ('Branț', 'textil, lasă aerul să circule.'), ('Talpă', 'plată, din cauciuc, ține bine pe diverse suprafețe.'))
  + '<p>Sunt pentru fetițe de în jur de 2-4 ani.</p>',
  [('model', 'Geox CIUFCIUF sneakers pentru copii roz B455QB.0FU22'), ('profil', 'Profilul scurt al încălțămintei'), ('material', 'inclusiv piele întoarsă și material textil'),
   ('sintetic', 'Piele întoarsă, Material textil, Material sintetic'), ('Respira', 'Tehnologia GEOX Respira™ cu membrană ajută la evacuarea umidității'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă, susținând independența'), ('culoare', 'Culoarea roz universală facilitează asortarea cu numeroase ținute'),
   ('interior', 'Interiorul căptușit cu material textil'), ('branț', 'Branțul din material textil susține circulația aerului'), ('talpă', 'Talpa plată din cauciuc contribuie la stabilitate și aderență pe diverse suprafețe')],
  {'Model': 'Geox CIUFCIUF', 'Material': 'piele întoarsă, textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici, profil scurt', 'Cod produs': 'B455QB.0FU22'})

w(12661,
  f'<p>Adidașii {TH} T1X9-35218 bej sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt, din imitație de piele cu finisaj de piele întoarsă, pentru ținute casual. Aricii cu curea reglabilă fac reglarea și încălțatul rapid, chiar de către copil.</p>'
  '<p>Gulerul ușor întărit cuprinde glezna, iar călcâiul întărit ține piciorul pe loc la joacă.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare, înaltă de 2 cm.'), ('Interior', 'material textil.'), ('Partea de sus', 'material sintetic.'))
  + '<p>Numerele 20-29 sunt pentru copii de aproximativ 1-5 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bej T1X9-35218'), ('profil', 'cu profil scurt'), ('imitație', 'Partea superioară din imitație de piele , cu finisaj de piele întoarsă'),
   ('casual', 'ținute casual'), ('arici', 'Închiderea cu arici , împreună cu o curea reglabilă, facilitează ajustarea și încălțarea rapidă'),
   ('guler', 'Gulerul ușor întărit al părții superioare îmbrățișează delicat glezna'), ('călcâi', 'Călcâiul întărit'),
   ('talpă', 'Talpa din cauciuc cu bandă de rulare'), ('înălțime', 'Talpă cu înălțimea de 2 cm'), ('interior', 'Interiorul din material textil')],
  {'Model': 'Tommy Hilfiger T1X9-35218', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, guler întărit', 'Cod produs': 'T1X9-35218'})

w(12662,
  f'<p>{REIMA} Tallustelu sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} în culoarea albastru, cu profil jos, din material textil și piele ecologică, ușori, pentru zi de zi. Fața are un finisaj hidrofob care ține umezeala afară, deci merg și pe vreme urâtă, deși impermeabilitatea completă nu e garantată.</p>'
  '<p>Șireturile rapide cu opritor și bucla de la spate fac încălțatul ușor, iar cutia lată nu ciupește degetele.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Inserții Happy Fit', 'detașabile, pentru mărimea potrivită.'), ('Interior', 'sintetic și textil.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Gama 28-40 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'Reima Sneakers pentru copii Tallustelu 5400137C'), ('culoare', 'Culoare albastru'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('hidrofob', 'Finisajul hidrofob al feței superioare nu permite umezelii să pătrundă în interior'), ('apă', 'nu garantează impermeabilitatea completă'),
   ('șireturi', 'Sistemul rapid de șireturi cu opritoare'), ('buclă', 'Bucla ușurează să pui pantoful în picior'), ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('Happy Fit', 'Inserțiile detașabile Happy Fit vă permit să alegeți dimensiunea potrivită'), ('interior', 'Material sintetic, Material textil'), TALPA],
  {'Model': 'Reima Tallustelu', 'Material': 'textil și piele ecologică, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'finisaj hidrofob, șireturi rapide, inserții Happy Fit', 'Cod produs': '5400137C'})

w(12667,
  f'<p>{GEOX} BISLI sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} în culoarea negru (bleumarin la magazin), din piele ecologică și material textil, cu membrana Geox Respira, care lasă umezeala să iasă și ține apa afară. Rezistă la apă, dar magazinul nu garantează impermeabilitatea completă.</p>'
  '<p>Șireturile elastice și velcro-ul fac încălțatul ușor, iar călcâiul întărit ține piciorul în pantof, ca să nu alunece la mers.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Vârf', 'rotund.'), ('Căptușeală', 'textilă, se curăță ușor.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 24-27 sunt pentru băieți de cam 2-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii BISLI culoarea negru, B461NA.054FU'), ('culoare', 'Culoare bleumarin'), ('material', 'combinație de piele ecologică și material textil'),
   ('Respira', 'Tehnologia Geox Respira, datorită unei membrane speciale respirabile și impermeabile'), ('apă', 'nu garantează impermeabilitate completă'),
   ('închidere', 'Șireturile elastice și închiderea cu velcro facilitează încălțarea și descălțarea pantofilor'), ('călcâi', 'Un fulger întărit pentru călcâi stabilizează călcâiul'),
   ('vârf', 'Vârf rotund'), ('căptușeală', 'Căptușeala textilă este confortabilă pentru picior și facilitează curățarea pantofilor'), TALPA],
  {'Model': 'Geox BISLI', 'Material': 'piele ecologică și textil, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, șireturi elastice și velcro', 'Cod produs': 'B461NA.054FU'},
  notes=['Titlul spune negru, magazinul dă culoarea bleumarin; am scris ambele.', 'Descrierea spune „ușor izolat”, atributele dau „neizolat”; n-am pomenit izolația.'])

w(12669,
  f'<p>Adidașii {TH} T1A9-33932 aurii sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din material textil și piele naturală, cu șireturi, fermoar lateral și închidere rapidă. Vin cu o pereche suplimentară de șireturi, ca să le puteți schimba.</p>'
  '<p>Cutia rotundă, întărită, apără degetele, iar contrafortul rigidizat sprijină călcâiul și glezna.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Interior', 'din piele, previne frecarea.'), ('Talpă exterioară', 'din cauciuc, durabilă, rezistentă la deteriorare.'), ('Partea de sus', 'textil și piele naturală.'))
  + '<p>Numerele 24-29 se potrivesc fetițelor de aproximativ 2-5 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea auriu, T1A9-33932'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatia materialului textil cu pielea naturala'),
   ('închidere', 'Model dantelat cu fermoar lateral și închidere rapidă'), ('șireturi', 'Include o pereche suplimentara de sireturi'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), ('interior', 'interior din piele care este confortabil pentru picior și previne frecarea'), TALPA],
  {'Model': 'Tommy Hilfiger T1A9-33932', 'Material': 'textil și piele naturală, interior din piele, talpă din cauciuc', 'Caracteristici': 'șireturi cu fermoar lateral, șireturi de schimb', 'Cod produs': 'T1A9-33932'})
