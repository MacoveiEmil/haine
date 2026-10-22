import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
VALENCIA = ('Valencia', 'Acestea au fost create in cooperare cu medici pediatri si ingineri de la Institutul de Biomecanica din Valencia')

w(12378,
  f'<p>Balerinii {GEOX} negri sunt {A("/categorie/incaltaminte-pantofi/", "balerini pentru fete")} din piele naturală și piele ecologică, cu un detaliu decorativ în față, ușor de curățat și de întreținut. Talpa NON-MARKING, din gumă, nu lasă urme pe parchet sau pe gresie.</p>'
  '<p>Vârful e rotund, ușor rigid, deci degetele se așază liber, iar contrafortul rigid ține călcâiul în pantof, ca să nu iasă la mers.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț Geox', 'din piele perforată, antibacterian, conturat.'), ('Geox Respira', 'talpă în trei straturi, perforată.'), ('Interior', 'textil și piele naturală.'))
  + '<p>Numerele 29-34 sunt pentru fete de 4-11 ani, în general.</p>',
  [('model', 'Geox Balerini copii culoarea negru'), ('material', 'combinatia pielii naturale cu cea ecologica'), ('întreținere', 'Modelul este ușor de curățat și întreținut'),
   ('decor', 'Detaliu decorativ in fata'), ('NON-MARKING', 'Talpa NON-MARKING: talpa exterioara din guma, care nu se mudareste'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('degete', 'degetele se pot aranja liber în pantof'), ('călcâi', 'Contorul de călcâi rigid'), ('branț', 'brant din piele cu perforari'), ('antibacterian', 'Are proprietati antibacteriene'),
   ('contur', 'Este conturat corespunzator'), RESPIRA, ('interior', 'Material textil, Piele naturala')],
  {'Model': 'Geox (balerini)', 'Material': 'piele naturală și ecologică, interior textil și piele, talpă din gumă', 'Caracteristici': 'talpă NON-MARKING, branț Geox, Geox Respira', 'Cod produs': ''})

w(12388,
  f'<p>Pantofii {BIO} 262121 sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} albi, ușori, din material textil și piele naturală, fără nichel și crom, creați cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia. Deschiderea largă face încălțatul ușor.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, iar velcro-ul se strânge după picior. Tăietura în formă de U la spate lasă glezna liberă și nu apasă pe tendonul lui Ahile.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Vârf', 'securizat, apără degetele.'), ('Stabilizator', 'lateral.'), ('Branț', 'detașabil, antibacterian, profilat.'), ('Talpă', 'tip „picior de elefant” la călcâi.'))
  + '<p>Numerele 19-25 se poartă, cu aproximație, între 1 și 3 ani.</p>',
  [('model', 'Biomecanics Pantofi copii culoarea alb, 262121'), ('material', 'combinația materialului textil cu pielea naturală'), ('ușor', 'Model ușor'),
   ('nichel', 'Fabricat numai din materiale naturale, fara nichel si crom'), VALENCIA, ('deschidere', 'Deschidere larga pentru incaltarea usoara a pantofilor'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('velcro', 'Usor de imbracat si se potriveste bine datorita fixarii cu velcro'),
   ('U', 'taieturi in forma de U care impiedica exercitarea presiunii asupra tendonului lui Ahile'), ('vârf', 'Degetul securizat protejeaza degetele'),
   ('stabilizator', 'Au un stabilizator lateral'), ('branț', 'Brant detasabil si antibacterian, profilat la mijlocul piciorului'), ('talpă', 'Talpa in forma de „picior de elefant” peste calcaie')],
  {'Model': 'Biomecanics 262121', 'Material': 'textil și piele naturală, fără nichel și crom', 'Caracteristici': 'velcro, cutie lată, branț detașabil antibacterian', 'Cod produs': '262121'})

w(12389,
  f'<p>Bocancii {GEOX} negri sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} neizolați, cu partea de sus neporoasă, care se curăță cu o cârpă umedă, pentru sezonul de tranziție. Interiorul e textil, iar branțul moale e profilat.</p>'
  '<p>Au șiret cu fermoar lateral și închidere cu Velcro, deci se reglează o dată după picior și apoi se încalță repede. Bucla de la spate ajută la tras bocancul.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Călcâi', 'contrafort rigid.'), ('Geox Respira', 'talpă în trei straturi, perforată.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 28-35 sunt pentru copii de 4-11 ani, de regulă.</p>',
  [('model', 'Geox Bocanci copii culoarea negru'), ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'), ('neizolat', 'Izolare: neizolat'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('branț', 'Branțul moale și profilat'),
   ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid'), RESPIRA, ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox (bocanci)', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'neizolați, șiret, fermoar lateral și Velcro, Geox Respira', 'Cod produs': ''},
  notes=['Magazinul scrie „piele întoarsă” în descriere, dar compoziția dă material sintetic; nu am pomenit materialul.'])

w(12397,
  f'<p>{BIO} 262166 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, ușori, cu profil scurt, din piele naturală și piele ecologică, creați cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia. Deschiderea largă face încălțatul ușor.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, deci pantoful merge și la un picior mai plin, iar curelele cu velcro se reglează după picior.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Inserție Plantilla', 'cu perforații, pentru picior uscat.'), ('Închidere', 'curele cu velcro.'), ('Profil', 'scurt.'))
  + '<p>Mărimile 19-23 sunt pentru copii de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii culoarea alb, 262166'), ('material', 'combinația pielii naturale cu pielea ecologică'), ('ușor', 'Model ușor'),
   ('profil', 'Înălțime: mic de statură'), VALENCIA, ('deschidere', 'Deschidere larga pentru incaltarea usoara a pantofilor'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('velcro', 'Curelele cu velcro pentru prindere ușoară permit o potrivire personalizată'),
   ('Plantilla', 'Inserția Plantilla cu perforații asigură o circulație adecvată a aerului, uscăciune')],
  {'Model': 'Biomecanics 262166', 'Material': 'piele naturală și piele ecologică', 'Caracteristici': 'velcro, cutie lată, inserție Plantilla perforată', 'Cod produs': '262166'})

w(12407,
  f'<p>Pantofii {BIO} 262103 sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} roz, din material textil și piele, fără nichel și crom, creați cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia. Se închid cu velcro și se pun ușor.</p>'
  '<p>Bucla de la spate ajută la tras pantoful pe picior, iar tăietura în U de la călcâi lasă glezna liberă. Stabilizatorul lateral ține piciorul drept la mers.</p>'
  '<p>Materialele și talpa, pe rând:</p>'
  + L(('Vârf', 'securizat, apără degetele.'), ('Branț', 'detașabil, antibacterian, profilat.'), ('Talpă', 'tip „picior de elefant” peste călcâi.'))
  + '<p>Numerele 19-25 se potrivesc copiilor de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi copii culoarea roz, 262103'), ('material', 'Material textil, Piele naturala'), ('nichel', 'Fabricat numai din materiale naturale, fara nichel si crom'),
   VALENCIA, ('velcro', 'Usor de imbracat si se potriveste bine datorita fixarii cu velcro'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('U', 'taieturi in forma de U'), ('stabilizator', 'Au un stabilizator lateral care controleaza miscarea piciorului in lateral'), ('vârf', 'Degetul securizat protejeaza degetele'),
   ('branț', 'Brant detasabil si antibacterian, profilat la mijlocul piciorului'), ('talpă', 'Talpa in forma de „picior de elefant” peste calcaie')],
  {'Model': 'Biomecanics 262103', 'Material': 'textil și piele naturală, fără nichel și crom', 'Caracteristici': 'velcro, buclă, stabilizator lateral, branț detașabil', 'Cod produs': '262103'})

w(12409,
  f'<p>{BIO} 261213 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, uni, cu profil înalt, din piele naturală și material sintetic, pentru ținutele de zi cu zi. Profilul înalt cuprinde glezna, iar călcâiul întărit ține piciorul în pantof.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, iar branțurile textile se scot, deci se curăță ușor și arată cât a crescut piciorul.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Partea de sus', 'piele naturală și material sintetic.'), ('Interior', 'material textil.'), ('Talpă', 'din cauciuc, cu profil plat.'))
  + '<p>Numerele 28-34 sunt pentru copii de 4-11 ani, în general.</p>',
  [('model', 'Biomecanics Sneakers pentru copii bleumarin 261213'), ('uni', 'Modelul uni'), ('profil', 'Profilul înalt al părții superioare'),
   ('material', 'Partea superioară din piele naturală'), ('sintetic', 'Utilizarea materialelor sintetice în partea superioară'), ('zilnic', 'ținutele zilnice'),
   ('călcâi', 'Călcâi întărit'), ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă'), ('branțuri', 'Branțuri detașabile din material textil'),
   ('interior', 'Interiorul din material textil'), ('talpă', 'Talpa din cauciuc cu profil plat')],
  {'Model': 'Biomecanics 261213', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici, branțuri detașabile', 'Cod produs': '261213'})

w(12410,
  f'<p>{A("/brand/reima/", "Reima")} Mutka 5100037B este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, roz, izolată și căptușită, pentru sporturi de iarnă. Cusăturile sudate opresc vântul și umezeala, iar impermeabilitatea de 10000 mm o face bună pentru zăpadă.</p>'
  '<p>Croiala e simplă, dreaptă, cu loc pentru un strat gros dedesubt. Gulerul ridicat și gluga detașabilă apără gâtul și capul de frig.</p>'
  '<p>Ce merită știut în plus:</p>'.replace(' în plus', ' despre material')
  + L(('Respirabilitate', '7000 g/m2/24h.'), ('Material', 'poliester reciclat, certificat Bluesign®.'), ('Finisaj', 'BIONIC-FINISH® ECO.'), ('Buzunare', 'interioare, oblice, cu închidere.'))
  + '<p>Mărimile 74-110 sunt pentru cei mici, de cam 9 luni până la 5 ani.</p>',
  [('model', 'Reima Mutka roz 5100037B'), ('izolat', 'Model izolat cu captuseala'), ('iarnă', 'Tip de activitate: Sporturi de iarnă'),
   ('cusături', 'Cusăturile sudate etanșează și împiedică pătrunderea vântului și a umezelii'), ('impermeabil', 'Impermeabilitate: 10000 mm/m2/24h'),
   ('croială', 'Tăiere simplă, fără blocare'), ('guler, glugă', 'Gulerul ridicat și gluga detașabilă'), ('respirabilitate', 'Respirabilitate: 7000 g/m2/24h'),
   ('reciclat', '100% Poliester reciclat'), ('Bluesign', 'Model certificat Bluesign® Standard'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('buzunare', 'Buzunare interioare oblice, incheiate')],
  {'Model': 'Reima Mutka', 'Material': '100% poliester reciclat; căptușeală poliester', 'Caracteristici': '10000 mm, cusături sudate, glugă detașabilă, Bluesign®', 'Cod produs': '5100037B'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(12411,
  f'<p>Bocancii {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} T3A5-34046 sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} negri, ușor izolați, cu aspect de piele întoarsă, făcuți parțial din poliester reciclat. Talpa exterioară din cauciuc rezistă la uzură.</p>'
  '<p>Au șiret cu fermoar lateral și închidere cu Velcro, deci se strâng o dată după picior și apoi se încalță repede. Vârful e rigidizat, iar contrafortul ține călcâiul.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Branț', 'textil, ușor de ținut curat.'), ('Interior', 'material sintetic și textil.'), ('Partea de sus', 'material sintetic și textil.'))
  + '<p>Numerele 30-34 sunt pentru copii de 6-11 ani, aproximativ.</p>',
  [('model', 'Tommy Hilfiger Bocanci copii culoarea negru, T3A5-34046'), ('izolat', 'Model usor cu izolatie'), ('piele întoarsă', 'confecționat din piele intoarsa'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'),
   ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('vârf', 'Varf rigidizat'), ('călcâi', 'Contorul de călcâi rigidizat'),
   ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'), ('interior', 'Material sintetic, Material textil')],
  {'Model': 'Tommy Hilfiger T3A5-34046', 'Material': 'sintetic și textil, talpă din cauciuc', 'Caracteristici': 'ușor izolați, șiret, fermoar și Velcro', 'Cod produs': 'T3A5-34046'})

w(12415,
  f'<p>{GEOX} J45HXB sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil scurt, cu aspect de piele întoarsă, ușor de curățat și întreținut. Talpa are sistemul Geox Respira, în trei straturi cu perforări.</p>'
  '<p>Velcro-ul se închide repede și se strânge după picior. Vârful rotund, ușor rigid, lasă degetele să se așeze liber, iar contrafortul rigid ține călcâiul.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'material sintetic și textil.'), ('Interior', 'textil, se ține ușor curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 36-39 sunt pentru adolescente de la 12 ani în sus, de obicei.</p>',
  [('model', 'Geox Sneakers pentru copii J45HXB.000BC'), ('culoare', 'roz'), ('profil', 'Înălțime: mic de statură'), ('piele întoarsă', 'confecționat din piele întoarsă'),
   ('întreținere', 'Modelul este ușor de curățat și întreținut'), RESPIRA, ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('degete', 'degetele se pot aranja liber în pantof'), ('călcâi', 'Contorul de călcâi rigid'),
   ('parte de sus', 'Gamba: Material sintetic, Material textil'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox J45HXB', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira', 'Cod produs': 'J45HXB.000BC'},
  notes=['Titlul nu are culoare; magazinul dă roz (vezi și 8722, același cod cu titlu Alb).'])
