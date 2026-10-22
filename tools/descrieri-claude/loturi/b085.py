import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')

w(13061,
  f'<p>Bluza cu mânecă lungă {TH} KS0KS00768 roșie este o {A("/categorie/bluze-tricouri-hanorace/", "bluză pentru fete")} din tricot de bumbac 100%, moale, cu dungi și grafică Peanuts. Materialul subțire și elastic urmează corpul fără să strângă la joacă.</p>'
  '<p>Decolteul are guler și închidere, care ușurează îmbrăcatul. Croiala e regulară și lasă loc de mișcare, iar bumbacul subțire e plăcut pe pielea copilului.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Model', 'dungi și grafică Peanuts.'), ('Decolteu', 'cu guler și închidere.'))
  + '<p>Mărimile 98-122 sunt pentru fete de aproximativ 3-7 ani.</p>',
  [('model', 'Tommy Hilfiger Longsleeve pentru copii din bumbac roșu KS0KS00768'), ('tricot', 'Tricotul din bumbac 100% este moale la atingere'),
   ('dungi', 'Modelul în dungi și grafica Peanuts®'), ('subțire', 'Materialul subțire'), ('elastic', 'Materialul elastic permite ajustarea la siluetă, fără a restricționa mișcările'),
   ('decolteu', 'Decolteul cu guler și închidere facilitează îmbrăcarea'), ('croială', 'Croiala regulară favorizează libertatea de mișcare'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KS0KS00768', 'Material': '100% bumbac', 'Caracteristici': 'dungi, grafică Peanuts, guler cu închidere', 'Cod produs': 'KS0KS00768'})

w(13063,
  f'<p>Cizmele de iarnă {TH} T3A5-34052 negre sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} izolate, cu gamba ridicată, din material textil și sintetic. Au șiret și fermoar lateral, deci se reglează o dată și apoi se încalță repede.</p>'
  '<p>Cutia rotundă e întărită, iar spatele călcâiului e puternic rigidizat.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, durabilă.'), ('Închidere', 'șiret și fermoar lateral.'))
  + '<p>Numerele 35-39 se potrivesc fetelor de la aproximativ 10 ani în sus; la 35 branțul are 21,5 cm.</p>',
  [('model', 'Tommy Hilfiger Cizme de iarnă pentru copii culoarea negru, T3A5-34052'), ('izolat', 'Izolare: izolat'), ('gambă', 'Gamba ridicata'),
   ('material', 'combinația materialului textil cu cel sintetic'), ('închidere', 'Model cu siret cu fermoar lateral'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Spatele calcaiului peternic rigidizat'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), TALPA,
   ('lungime', 'Lungimea brantului pentru marimea este de: 21,5 cm')],
  {'Model': 'Tommy Hilfiger T3A5-34052', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'izolate, șiret și fermoar lateral, gambă ridicată', 'Cod produs': 'T3A5-34052'})

w(13074,
  f'<p>Adidașii {TH} T1A9-35064 bej sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt, din imitație de piele ușor de curățat, cu închidere triplă: șireturi, arici și fermoar, pentru o reglare precisă. Merg la locul de joacă și la plimbările prin oraș.</p>'
  '<p>Gulerul întărit cuprinde glezna, iar călcâiul întărit ține piciorul pe loc.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textilă, aerisită.'), ('Talpă', 'din cauciuc, plată, groasă de 2-4 cm.'), ('Partea de sus', 'material sintetic.'))
  + '<p>Numerele 30-34 se potrivesc copiilor de aproximativ 6-11 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bej T1A9-35064'), ('profil', 'Profilul scurt al părții superioare'), ('imitație', 'Partea superioară din imitație de piele , care oferă încălțămintei un aspect estetic și facilitează întreținerea curățeniei'),
   ('închidere', 'Sistem de închidere triplu – șireturi, arici și fermoar – permite o ajustare precisă'), ('joacă', 'locul de joacă, cât și pentru aventurile urbane'),
   ('guler', 'Gulerul superior întărit , care îmbrățișează delicat glezna'), ('călcâi', 'Călcâi întărit'), ('căptușeală', 'Interiorul căptușit cu material textil'),
   ('talpă', 'Talpă de cauciuc cu profil plat'), ('grosime', 'Grosimea tălpii între 2-4 cm')],
  {'Model': 'Tommy Hilfiger T1A9-35064', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi, arici și fermoar', 'Cod produs': 'T1A9-35064'})

w(13082,
  f'<p>Puloverul {TH} KG0KG08848 roz este un {A("/categorie/bluze-tricouri-hanorace/", "pulover pentru fete")} din bumbac 100%, cu croială relaxed fit, umeri coborâți și broderie discretă, pentru ținute casual. Țesătura împletită dă materialului textură.</p>'
  '<p>Decolteul rotund, baza și manșetele au bordură elastică, deci puloverul își ține forma. Materialul are și elasticitate, așa că se așază bine pe corp, iar croiala lejeră nu strânge la mișcare.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Mâneci', 'lungi, cu umeri coborâți.'), ('Decor', 'broderie discretă.'))
  + '<p>Mărimile 128-176 sunt pentru fete de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Pulover pentru copii din bumbac roz KG0KG08848'), ('bumbac', 'Bumbacul 100% este plăcut la atingere'), ('croială', 'Croiala relaxed fit favorizează confortul și nu restricționează mișcările'), ('elastic', 'Materialul elastic ajută la ajustarea pe siluetă'),
   ('umeri', 'Mâneca lungă cu linia umerilor coborâtă'), ('broderie', 'Broderia subtilă'), ('casual', 'stilizările casual'), ('împletit', 'Splotul împletit oferă țesăturii o textură'),
   ('decolteu', 'Decolteul rotund cu bordură elastică'), ('benzi', 'Benzile elastice de la bază și de la manșete ajută la menținerea formei'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG08848', 'Material': '100% bumbac', 'Caracteristici': 'relaxed fit, broderie, decolteu rotund', 'Cod produs': 'KG0KG08848'})

w(13090,
  f'<p>Cizmele de zăpadă {A("/brand/ugg/", "UGG")} CLASSIC MICRO negre sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} joase, izolate, din piele întoarsă, cu interior din lână, care se trag pe picior fără închidere. Căptușeala UGGplush, din lână și TENCEL Lyocell, ajută și la eliminarea umidității.</p>'
  '<p>Impregnarea hidrofobă le apără de precipitații ușoare. Contrafortul și vârful rotund sunt rigidizate, deci cizma își ține forma și călcâiul stă corect.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'plată, din spumă, ușoară.'), ('Guler', 'ușor rigidizat.'), ('Interior', 'lână.'))
  + '<p>Numerele 31-36 se poartă de pe la 6 ani în sus.</p>',
  [('model', 'UGG Cizme de zăpadă pentru copii din piele întoarsă CLASSIC MICRO negre 1174410K'), ('jos', 'cu profil redus'), ('izolat', 'Izolare: izolat'),
   ('piele', 'Partea superioară din piele întoarsă'), ('lână', 'interior moale din lână'), ('slip-on', 'construcție practică de tip slip-on'),
   ('UGGplush', 'Tehnologia UGGplush™ combină lâna și TENCEL™ Lyocell, susținând eliminarea umidității'), ('hidrofob', 'Impregnarea hidrofobă limitează pătrunderea umidității în timpul precipitațiilor ușoare'),
   ('contrafort', 'Contrefortul rigidizat ajută la menținerea corectă a călcâiului copilului în pantof'), ('vârf', 'Vârful rotund, rigidizat'), ('talpă', 'Talpa plată din spumă asigură un pas ușor'), ('guler', 'Gulerul ușor rigidizat'), ('interior', 'Lână')],
  {'Model': 'UGG CLASSIC MICRO', 'Material': 'piele întoarsă, interior din lână, talpă din spumă', 'Caracteristici': 'izolate, UGGplush, impregnare hidrofobă, fără închidere', 'Cod produs': '1174410K'})

w(13093,
  f'<p>{GEOX} FLEXYPER J569BA bleumarin sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme pentru băieți")} numite de magazin „de iarnă”, dar neizolate, din piele ecologică, piele naturală și material textil. Se închid cu scai, iar bucla de la spate ajută la încălțat.</p>'
  '<p>Vârful rotund, ușor rigid, lasă loc degetelor, iar partea de sus rigidizată ține forma. Talpa absoarbe șocurile.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Căptușeală', 'textilă.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 28-35 se potrivesc băieților de cam 4-11 ani.</p>',
  [('model', 'Geox Cizme de iarnă pentru copii FLEXYPER culoarea bleumarin, J569BA.0ME32'), ('neizolat', 'Izolare: neizolat'),
   ('material', 'combinatie de piele ecologica, piele naturala si material textil'), ('scai', 'Incheiere cu scai'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('rigid', 'Partea superioară rigidizată'), ('șoc', 'Absorbtia socului'), RESPIRA, ('căptușeală', 'Model cu captuseala textila'), TALPA],
  {'Model': 'Geox FLEXYPER', 'Material': 'piele ecologică, piele naturală și textil, talpă din cauciuc', 'Caracteristici': 'scai, Geox Respira, neizolate', 'Cod produs': 'J569BA.0ME32'},
  notes=['Titlul spune „cizme de iarnă”, dar atributele dau „neizolat”; am scris ambele.'])

w(13096,
  f'<p>{GEOX} FOOT-RUN Barefoot sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, cu profil scurt, din piele întoarsă și material textil, cu design simplu și logo discret. Talpa plată din spumă e ușoară și lasă piciorul să se miște natural.</p>'
  '<p>Aricii și inserția elastică fac încălțatul rapid și ajută pantoful să stea bine. Membrana microporoasă GEOX Respira din talpă scoate umezeala, ca piciorul să rămână uscat.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textilă, aerisită.'), ('Guler', 'ușor întărit.'), ('Călcâi', 'ușor întărit.'))
  + '<p>Gama 20-35 acoperă băieți de aproximativ 1-11 ani.</p>',
  [('model', 'Geox FOOT-RUN Barefoot sneakers pentru copii verzi B660KA.0FU22'), ('profil', 'Profilul scurt al părții superioare'),
   ('material', 'Partea superioară, realizată dintr-o combinație de piele întoarsă și material textil'), ('logo', 'Designul simplu cu logo-ul subtil al mărcii'),
   ('talpă', 'Talpa plată, din spumă , contribuie la ușurința încălțămintei și susține mișcarea naturală a piciorului'), ('arici', 'Închiderea practică cu arici'),
   ('elastic', 'Inserția elastică'), ('Respira', 'Tehnologia GEOX Respira™ asigură picioare uscate, datorită membranei microporoase din talpă'),
   ('căptușeală', 'Interiorul căptușit cu material textil'), ('guler', 'Gulerul superior ușor întărit'), ('călcâi', 'Călcâi ușor întărit')],
  {'Model': 'Geox FOOT-RUN Barefoot', 'Material': 'piele întoarsă și textil, interior textil, talpă din spumă', 'Caracteristici': 'barefoot, Geox Respira, arici cu inserție elastică', 'Cod produs': 'B660KA.0FU22'})

w(13098,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261102 sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, din piele naturală, cu imprimeu decorativ, în stil casual și streetwear, făcuți cu podologi. Vârful rotund are întăritură din cauciuc care apără degetele, iar spațiul extins de acolo le lasă să se miște.</p>'
  '<p>Aricii fac încălțatul rapid, iar călcâiul moale și gulerul ușor întărit sunt confortabile.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branțuri', 'detașabile, aerisite.'), ('Interior', 'material textil.'), ('Talpă', 'flexibilă, din cauciuc.'))
  + '<p>Numerele 18-25 sunt pentru fetițe de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele roz 261102'), ('piele', 'Partea superioară din piele naturală'), ('imprimeu', 'Imprimeu decorativ în culoarea roz'),
   ('stil', 'caracter casual și streetwear'), ('podologi', 'creat în colaborare cu podologi'), ('vârf', 'Vârf rotund, rigidizat cu întăritură din cauciuc asigură protecția degetelor'),
   ('degete', 'Spațiu extins în zona degetelor'), ('arici', 'Închidere practică cu arici'), ('călcâi', 'Călcâi moale și gulerul superior ușor întărit'),
   ('branț', 'Branțuri detașabile, respirabile'), ('interior', 'Interior din material textil'), ('talpă', 'Talpă flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261102', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, vârf cauciucat, branț detașabil', 'Cod produs': '261102'})

w(13100,
  f'<p>Bocancii {A("/brand/primigi/", "Primigi")} PFS 24120 negri sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} din piele, fără izolație, pentru zilele de tranziție, cu înălțime peste gleznă care apără de frig și murdărie. Se închid cu fermoar, deci copilul se încalță singur.</p>'
  '<p>Vârful e rigidizat, iar călcâiul întărit și gulerul ușor întărit sprijină glezna. Căptușeala din piele naturală e plăcută la purtare.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'plată, din cauciuc, cu bandă de rulare.'), ('Branț', 'din imitație de piele.'), ('Primigi × SIPeP', 'dezvoltată cu podologi.'))
  + '<p>Numerele 25-29 se potrivesc fetițelor de cam 2-5 ani.</p>',
  [('model', 'Primigi Bocanci pentru copii din piele negri PFS 24120'), ('piele', 'Partea superioară din piele naturală'), ('izolație', 'Fără izolație'),
   ('tranziție', 'zilele de tranziție'), ('gleznă', 'Înălțimea peste gleznă ajută la protecția împotriva frigului și a murdăriei minore'),
   ('fermoar', 'Închiderea cu fermoar facilitează încălțarea și descălțarea rapidă și independentă'), ('vârf', 'Vârf rigidizat și călcâi întărit'),
   ('guler', 'Gulerul superior ușor întărit'), ('căptușeală', 'Căptușeala din piele naturală'), ('talpă', 'Talpă plată din cauciuc cu bandă de rulare'),
   ('branț', 'Branț din imitație de piele'), ('SIPeP', 'Tehnologia Primigi × SIPeP , dezvoltată împreună cu podologi')],
  {'Model': 'Primigi PFS 24120', 'Material': 'piele (piele acoperită), căptușeală din piele, talpă din cauciuc', 'Caracteristici': 'fermoar, fără izolație, peste gleznă', 'Cod produs': 'PFS 24120'})

w(13103,
  f'<p>Pantofii {GEOX} STEPPIEUP violet sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} din piele naturală, cu interior tot din piele, ușori, pentru purtarea zilnică. Velcro-ul și bucla de la spate fac încălțatul rapid, iar cutia lată nu ciupește degetele.</p>'
  '<p>Branțul Geox, din piele perforată, e antibacterian și conturat pentru așezarea corectă a piciorului.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, perforată.'), ('Călcâi', 'contrafort rigid.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 20-27 sunt pentru fetițe de aproximativ 1-4 ani.</p>',
  [('model', 'Geox Încălțăminte din piele pentru copii STEPPIEUP culoarea violet, B4663A.000CL'), ('piele', 'confecționat din piele naturala'), ('interior', 'Interiorul: Piele naturala'),
   ('ușor', 'Model ușor și confortabil'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('branț', 'brant din piele cu perforari'), ('antibacterian', 'Are proprietati antibacteriene'),
   ('contur', 'Este conturat corespunzator pentru o asezare corecta a piciorului'), RESPIRA, ('călcâi', 'Contorul de călcâi rigid'), TALPA],
  {'Model': 'Geox STEPPIEUP', 'Material': 'piele naturală, interior din piele, talpă din cauciuc', 'Caracteristici': 'velcro, branț Geox antibacterian, Geox Respira', 'Cod produs': 'B4663A.000CL'})
