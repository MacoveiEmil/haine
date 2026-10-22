import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
PRIMIGI = A('/brand/primigi/', 'Primigi')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'

w(12353,
  f'<p>Același cod {A("/brand/guess/", "GUESS")} K5YL04, aici în bleumarin, este o {A(GF, "geacă de tranziție pentru fete")} fără izolație proprie, dar cu o vestă izolată înăuntru. Materialul neted are impregnare hidrofobă și rezistă la apă, fără să fie complet impermeabil.</p>'
  '<p>Gluga e integrată, închiderea e cu cleme, iar pe laterale are două buzunare. Mânecile se termină cu o bandă elastică, iar talia se strânge cu un șnur.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', 'completă, sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Pe site sunt doar 96-104 și 122-125, adică aproximativ 3-7 ani.</p>',
  [('cod', 'K5YL04'), ('culoare', 'culoarea albastru marin'), ('neizolat', 'Model neizolat confecționat din din material neted'), ('vestă', 'Are vesta izolata'),
   ('hidrofob', 'impregnare hidrofobă'), ('apă', 'Rezistent la apa'), ('impermeabil', 'nu garantează impermeabilitatea completă'), ('glugă', 'integrată'),
   ('cleme', 'Incheiere cu cleme'), ('buzunare', 'Două buzunare laterale'), ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('talie', 'Talia este reglabila cu snur'),
   ('material', '100% Poliester'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('croială', 'Croială: regular fit')],
  {'Model': 'GUESS K5YL04', 'Material': '100% poliester', 'Caracteristici': 'vestă izolată, glugă, talie cu șnur', 'Cod produs': 'K5YL04.WFVK0'},
  notes=['Produsul e marcat și „pentru bebe”; pe site e la geci pentru fete.'])

w(12385,
  f'<p>Modelul {PRIMIGI} 1420022, în varianta multicoloră cu numere mai mari, intră la {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")}: are membrană GORE-TEX contra umezelii și vântului, iar talpa Vibram din cauciuc ține bine pe multe tipuri de teren.</p>'
  '<p>Fața combină textil și material sintetic, gulerul din jurul gleznei e moale, iar vârful are loc în plus pentru degete. Se închid cu șireturi elastice și velcro, iar branțurile din piele naturală se scot.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Interior', 'material textil.'), ('Branț', 'piele naturală, detașabil.'), ('Sezon', 'primăvară, vară, toamnă.'))
  + '<p>Numerele 30-35 merg, cu aproximație, la 6-11 ani.</p>',
  [('cod', '1420022'), ('culoare', 'multicolor'), ('GORE-TEX', 'Membrana GORE-TEX® oferă protecție împotriva umidității și a vântului'),
   ('Vibram', 'Talpa Vibram oferă o aderență bună pe diverse tipuri de suprafețe'), ('față', 'Partea superioară din material textil și sintetic'),
   ('guler', 'Gulerul moale din jurul gleznei'), ('degete', 'Spațiul mărit în zona degetelor'), ('velcro', 'Șireturile elastice și închiderea cu velcro'),
   ('branț', 'Branțurile detașabile din piele naturală'), ('interior', 'Interior:100% Material textil'), ('sezon', 'primăvară, vară și toamnă')],
  {'Model': 'Primigi 1420022', 'Membrană': 'GORE-TEX', 'Caracteristici': 'talpă Vibram, branț din piele, velcro', 'Cod produs': '1420022'})

w(12401,
  f'<p>Adidașii {A("/brand/geox/", "Geox")} J36FWB roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} foarte ușori, din plasă respirabilă, pentru purtat zi de zi. Sistemul Geox Respira are talpă în trei straturi, cu perforații pentru ventilare, iar talpa din spumă e moale.</p>'
  '<p>Șireturile elastice cu cârlig îi fac ușor de pus și de scos, bucla de la spate ajută la încălțat, iar vârful rotund lasă degetele să se așeze liber. Branțul textil se scoate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Lungime branț', '22,5 cm la numărul 36.'), ('Profil', 'scurt.'))
  + '<p>Numerele 36-39 se poartă de pe la 12 ani în sus.</p>',
  [('cod', 'J36FWB'), ('culoare', 'culoarea roz'), ('plasă', 'confecționat din plasă ușoară, respirabilă'), ('ușor', 'Model ultraușor ideal pentru purtarea de zi cu zi'),
   ('Respira', 'Sistemul Geox Respira'), ('straturi', 'talpei in trei straturi cu sistemul de perforari'), ('spumă', 'Talpa din spumă oferă o senzație mai moale'),
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig'), ('buclă', 'Bucla de la spate'), ('vârf', 'degetele se pot aranja liber în pantof'),
   ('branț', 'Brant textil, detasabil'), ('gambă', 'Material sintetic, Material textil'), ('lungime', 'Lungimea brantului pentru marimea este de: 22,5 cm'),
   ('mărime', 'Dimensiunile date pentru marimea: 36'), ('profil', 'scurt')],
  {'Model': 'Geox J36FWB', 'Material': 'plasă, material sintetic', 'Caracteristici': 'Geox Respira, șireturi elastice, ultraușori', 'Cod produs': 'J36FWB.01454'},
  notes=['Pagina magazinului dă în titlu „culoarea roz”, iar în datele produsului „alb”.'])

w(12422,
  f'<p>Geaca {TH} KB0KB09852, acum în negru și în mărimi mici, este o {A(GB, "geacă subțire pentru băieți")}, fără umplutură, din material neted cu poliamidă parțial reciclată. Căptușeala e completă, din poliamidă.</p>'
  '<p>Gulerul e ridicat, nu are glugă, se închide cu fermoar, iar mânecile au manșetă. Croiala e simplă, fără blocare, potrivită pentru zilele de tranziție, primăvara și toamna.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă reciclată.'), ('Căptușeală', '100% poliamidă.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 98-122 țin cam de 3-7 ani.</p>',
  [('cod', 'KB0KB09852'), ('culoare', 'culoarea negru'), ('neizolat', 'Model neizolat confecționat din material neted'), ('reciclat', 'realizat partial din poliamida reciclata'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('guler', 'Guler ridicat'), ('glugă', 'fără glugă'), ('fermoar', 'Incheiere cu fermoar'), ('manșetă', 'Finisaj din manseta'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('material', '100% Poliamida reciclata'), ('poliamidă', '100% Poliamida'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB09852', 'Material': '100% poliamidă reciclată', 'Caracteristici': 'subțire, guler ridicat, fermoar', 'Cod produs': 'KB0KB09852'},
  notes=['Produsul e marcat și „pentru bebe”; pe site e la geci pentru băieți.'])

w(12434,
  f'<p>Adidașii {PRIMIGI} 1420000 albi sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu membrană GORE-TEX, care ajută contra umezelii și rămâne respirabilă, și talpă Vibram rezistentă la abraziune. Fața e din piele întoarsă și textil.</p>'
  '<p>Talpa din cauciuc are striații contra alunecării, branțul preia șocurile, iar contrafortul e rigidizat. Se închid cu velcro și șireturi, iar gulerul e ușor rigidizat în jurul gleznei.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'material textil, piele întoarsă.'), ('Interior', 'material textil.'), ('Profil', 'scurt.'))
  + '<p>Numerele 30-35 corespund aproximativ vârstei de 6-11 ani.</p>',
  [('cod', '1420000'), ('culoare', 'Culoare alb'), ('GORE-TEX', 'Tehnologia GORE-TEX®'), ('umezeală', 'ajută la protejarea împotriva umezelii, menținând în același timp respirabilitatea'),
   ('Vibram', 'Talpă Vibram®'), ('abraziune', 'rezistență la abraziune'), ('față', 'Partea superioară:Material textil, Piele întoarsă'), ('striații', 'Talpă cu striații'),
   ('alunecare', 'minimizând riscul de alunecare'), ('branț', 'Branț cu amortizare'), ('contrafort', 'Contrefort rigidizat'), ('velcro', 'Închidere cu velcro și șireturi'),
   ('guler', 'Guler ușor rigidizat'), ('interior', 'Interior:Material textil'), ('profil', 'scurt')],
  {'Model': 'Primigi 1420000', 'Membrană': 'GORE-TEX', 'Caracteristici': 'talpă Vibram, velcro și șireturi, piele întoarsă', 'Cod produs': '1420000'},
  notes=['Titlul site-ului nu are culoare („Fete”); culoarea e cea de la magazin (alb, producătorul: JUTE.SAND).'])

w(12446,
  f'<p>Geaca {TH} KS0KS00620 bleumarin, în mărimile pentru cei mici, este o {A(GF, "geacă matlasată pentru fete")}, subțire, din nailon, cu căptușeală completă. Logoul mărcii e brodat în față.</p>'
  '<p>Nu are glugă, buzunarele sunt oblice, iar mânecile se termină cu manșetă. Fermoarul o face ușor de pus și de scos, iar croiala e simplă. Fiind subțire, e o geacă pentru zilele răcoroase, nu pentru ger.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% nailon.'), ('Glugă', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 104-122 se potrivesc pe la 4-7 ani.</p>',
  [('cod', 'KS0KS00620'), ('culoare', 'culoarea albastru marin'), ('subțire', 'Model subtire confectionat din material matlasat'), ('matlasat', 'Matlasare'),
   ('căptușeală', 'Model cu captuseala'), ('logo', 'Logo-ul mărcii brodat pe față'), ('glugă', 'fără glugă'), ('buzunare', 'Buzunare oblice'), ('manșetă', 'Finisaj din manseta'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('croială', 'croială simplă, fără blocare'), ('material', '100% Nailon')],
  {'Model': 'Tommy Hilfiger KS0KS00620', 'Material': '100% nailon', 'Caracteristici': 'matlasată, logo brodat, fermoar', 'Cod produs': 'KS0KS00620'})

w(12455,
  f'<p>Compleul de trening {TH} KS0KS00708 bleumarin, în mărimi mici, se găsește printre {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "treningurile pentru băieți")}. E tricotat dintr-un amestec cu bumbac regenerat, refăcut din deșeuri textile, și poliester parțial reciclat, foarte confortabil.</p>'
  '<p>Bluza are decolteu rotund, clasic, mânecă lungă terminată cu manșetă, iar tăietura e simplă. Modelul e uni, într-o singură culoare, ușor de purtat acasă sau afară.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '50% poliester reciclat, 50% bumbac regenerativ.'), ('Mânecă', 'lungă.'), ('Model', 'uni, tricotaj.'))
  + '<p>Mărimile 104-122 acoperă orientativ 4-7 ani.</p>',
  [('cod', 'KS0KS00708'), ('culoare', 'culoarea bleumarin'), ('trening', 'Compleu de trening din colecția Tommy Hilfiger confecționat din tricot'),
   ('regenerat', 'Modelul conține fibre de bumbac regenerate'), ('deșeuri', 'Din deșeuri textile vechi sunt create fibre și fire noi'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('confortabil', 'material extrem de confortabil'), ('decolteu', 'Decolteu clasic, rotund'),
   ('mânecă', 'Maneca lunga'), ('manșetă', 'Finisaj din manseta'), ('tăiere', 'Tăiere simplă, fără blocare'), ('uni', 'Model: uni'),
   ('material', '50% Poliester reciclat, 50% Bumbac regenerativ')],
  {'Model': 'Tommy Hilfiger KS0KS00708', 'Material': '50% poliester reciclat, 50% bumbac', 'Caracteristici': 'trening, tricot, decolteu rotund', 'Cod produs': 'KS0KS00708'})

w(12459,
  f'<p>Botinele {TH} T4A5-34028 negre sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} din material sintetic, cu toc gros și talpă plată din cauciuc, durabilă și rezistentă la deteriorare. Vârful e rotund și rigidizat, iar contrafortul rigidizat sprijină glezna și călcâiul.</p>'
  '<p>Au șireturi plate, fermoar lateral și velcro, deci se pun ușor. Bucla de la spate ajută la încălțat, iar interiorul e textil. Nu sunt izolate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic.'), ('Interior', 'material textil.'), ('Lungime branț', '24,5 cm la numărul 39.'))
  + '<p>Numerele 35-40 se poartă cam de la 10 ani în sus.</p>',
  [('cod', 'T4A5-34028'), ('culoare', 'culoarea negru'), ('sintetic', 'confecționat din material sintetic'), ('toc', 'toc gros'), ('plată', 'plată'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('vârf', 'Varf rigidizat'), ('rotund', 'rotund'),
   ('contrafort', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), ('șireturi', 'Sireturile plate'),
   ('fermoar', 'Închidere cu fermoar lateral și cu velcro'), ('buclă', 'Bucla de la spate'), ('interior', 'Material textil'), ('neizolat', 'Izolare: neizolat'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 24,5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 39')],
  {'Model': 'Tommy Hilfiger T4A5-34028', 'Talpă': 'cauciuc, toc gros', 'Caracteristici': 'șireturi, fermoar lateral, velcro', 'Cod produs': 'T4A5.34028'})

w(12470,
  f'<p>Botinele {TH} T1A5-34005 bleumarin sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} cu fața neporoasă, care se curăță ușor cu o cârpă umedă, și talpă groasă, plată, din cauciuc durabil. Conțin materiale din fibre reciclate.</p>'
  '<p>Vârful e rotund și întărit, călcâiul puternic rigid ține piciorul să nu alunece, iar închiderea combină șiretul, fermoarul lateral și velcro-ul. Interiorul e confortabil. Nu sunt izolate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic.'), ('Interior', 'material sintetic, material textil.'), ('Lungime branț', '21,5 cm la numărul 34.'))
  + '<p>Numerele 30-34 merg pe la 6-11 ani.</p>',
  [('cod', 'T1A5-34005'), ('culoare', 'culoarea bleumarin'), ('neporoasă', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'), ('groasă', 'groasă, plată'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('reciclat', 'Produsul contine materiale realizate din fibre reciclate'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'),
   ('interior', 'Interior confortabil'), ('neizolat', 'Izolare: neizolat'), ('gambă', 'Material sintetic'), ('interior2', 'Material sintetic, Material textil'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 21,5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 34')],
  {'Model': 'Tommy Hilfiger T1A5-34005', 'Talpă': 'cauciuc, groasă', 'Caracteristici': 'șiret, fermoar lateral, velcro', 'Cod produs': 'T1A5.34005'},
  notes=['Descrierea spune „piele întoarsă”, iar compoziția indică material sintetic, imitație de piele; am scris doar compoziția.'])

w(12481,
  f'<p>Parka {A("/brand/columbia/", "Columbia")} 2090241 bordo (burgundy) este o {A(GF, "geacă de iarnă pentru fete")} izolată, cu umplutură în mare parte reciclată, de grosime medie spre mare. Omni-Tech are membrană microporoasă, respirabilă, cu cusături sigilate, iar Omni-Heat Thermal Reflective ajută la reglarea temperaturii.</p>'
  '<p>Sistemul OUTGROWN o ajută să țină mai multe sezoane, odată cu creșterea copilului. Gulerul înalt și gluga fixă au garnitură de blană artificială detașabilă, se închide cu fermoar și velcro, iar talia e elastică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'exterioare, cu fermoar.'), ('Material', '72% nailon, 28% poliester.'), ('Lungime', '57 cm în față, 60 cm la spate, la 116.'))
  + '<p>Mărimile 104-164 se potrivesc cu aproximație la 4-14 ani.</p>',
  [('cod', '2090241'), ('culoare', 'culoarea burgundy'), ('parka', 'Parka pentru copii din colecția Columbia'), ('izolat', 'Model izolat confecționat din material termo-regulator'),
   ('reciclat', 'Acest produs conține materiale fabricate din fibre reciclate'), ('groasă', 'medie, groasă'), ('Omni-Tech', 'Tehnologia Omni-Tech®'),
   ('membrană', 'membrane microporoase, respirabile și cusăturilor sigilate'), ('Omni-Heat', 'Tehnologia Omni-Heat Thermal Reflective'), ('OUTGROWN', 'Sistemul OUTGROWN Grow'),
   ('guler', 'Gulerul înalt și gluga fixă'), ('blană', 'Glugă cu garnitură detașabilă din blană artificială'), ('fermoar', 'Închidere cu fermoar și velcro'),
   ('talie', 'Talie elastică'), ('buzunare', 'Buzunare exterioare cu fermoar'), ('material', '72% Nailon, 28% Poliester'), ('față', 'Lungimea părții din față: 57 cm'),
   ('spate', 'Lungimea părții din spate: 60 cm'), ('mărime', 'Măsurători bazate pe înălțime: 116 cm')],
  {'Model': 'Columbia 2090241 (parka)', 'Material': '72% nailon, 28% poliester', 'Caracteristici': 'Omni-Tech, Omni-Heat, OUTGROWN, blană detașabilă', 'Cod produs': '2090241'},
  notes=['Titlul site-ului are „parka” în locul culorii; culoarea e cea de la magazin (burgundia).'])
