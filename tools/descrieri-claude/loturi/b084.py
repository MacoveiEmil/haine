import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')
CANEL = ('caneluri', 'Talpa exterioară din cauciuc cu caneluri este durabilă și oferă o tracțiune bună')
CURAT = ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')

w(13019,
  f'<p>{GEOX} CIBERDRON x Spiderman sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, cu personajul Spiderman, din material sintetic și textil, ușori, pentru purtarea zilnică. Se închid cu velcro, deci copilul se încalță singur.</p>'
  '<p>Talpa exterioară din cauciuc are caneluri care țin bine pe sol, iar talpa Geox Respira are trei straturi cu perforări, pentru aerisire. Interiorul textil e comod toată ziua.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Vârf', 'rotund.'), ('Interior', 'confortabil, textil.'), ('Profil', 'jos.'))
  + '<p>Gama 24-35 acoperă băieți de aproximativ 2-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii CIBERDRON x Spiderman culoarea bleumarin, J65LBC.014CE'), ('personaj', 'Personaje de basm'), ('material', 'combinația materialului sintetic cu cel textil'),
   ('ușor', 'Model ușor și confortabil'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), CANEL, RESPIRA,
   ('vârf', 'Varf rotund'), ('interior', 'Interior confortabil'), ('textil', 'Interiorul: Material textil'), ('profil', 'Înălțime: mic de statură')],
  {'Model': 'Geox CIBERDRON x Spiderman', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira, talpă cu caneluri', 'Cod produs': 'J65LBC.014CE'})

w(13020,
  f'<p>Varianta cu Superman a modelului {GEOX} CIBERDRON: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} în culoarea albastru, joși, făcuți din textil și material sintetic. Velcro-ul îi permite copilului să se descurce singur la încălțat.</p>'
  '<p>Dedesubt e cauciuc cu caneluri, care rezistă mult și nu alunecă, peste o talpă Geox Respira cu trei straturi perforate. Vârful e rotunjit, iar pe dinăuntru pantoful e comod.</p>'
  '<p>Materialele folosite:</p>'
  + L(('Exterior', 'sintetic și textil.'), ('Căptușeală', 'textilă.'), ('Talpă', 'cauciuc cu caneluri.'))
  + '<p>Numerele 24-35 se potrivesc băieților de cam 2-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii CIBERDRON x Superman J65LBB.01454'), ('culoare', 'Culoare albastru'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului sintetic cu cel textil'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), CANEL, RESPIRA,
   ('vârf', 'Varf rotund'), ('interior', 'Interior confortabil'), ('textil', 'Interiorul: Material textil')],
  {'Model': 'Geox CIBERDRON x Superman', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira, talpă cu caneluri', 'Cod produs': 'J65LBB.01454'})

w(13033,
  f'<p>{GEOX} PERTH J367RE bej, în numerele 28-35, sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu profil jos, ușori, din textil și piele ecologică, pentru fiecare zi. N-au nevoie de legat: șireturile sunt elastice și se prind cu cârlig.</p>'
  '<p>La spate, contrafortul rigidizat sprijină călcâiul și glezna. Vârful e rotunjit, iar căptușeala textilă ajută pantoful să rămână curat.</p>'
  '<p>Talpa și căptușeala:</p>'
  + L(('Geox Respira', 'trei straturi, perforate.'), ('Căptușeală', 'textilă, se curăță ușor.'), ('Talpă exterioară', 'cauciuc durabil.'))
  + '<p>Se potrivesc băieților de pe la 4 până pe la 11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii PERTH culoarea bej, J367RE.054FU'), ('profil', 'Înălțime: mic de statură'), ('ușor', 'Model ușor și confortabil'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('închidere', 'Șireturile elastice și închiderea cu cârlig'),
   ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), ('vârf', 'Varf rotund'), RESPIRA, CURAT, TALPA],
  {'Model': 'Geox PERTH', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J367RE.054FU'})

w(13039,
  f'<p>Și în maro, {GEOX} PERTH J367RE.0MEMS vin în numerele 28-35: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} scunzi, cu exterior din imitație de piele care se îngrijește ușor. Membrana specială nu lasă apa să intre, iar talpa microporoasă lasă umezeala să iasă.</p>'
  '<p>Arici plus șireturi elastice: încălțat rapid, potrivire după picior. Gulerul moale reduce riscul de roadere.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Călcâi', 'întărit, pentru pași siguri.'), ('Talpă', 'cauciuc plat.'))
  + '<p>Mărimile sunt gândite pentru băieți de cam 4-11 ani.</p>',
  [('model', 'Geox PERTH sneakers pentru copii maro J367RE.0MEMS'), ('profil', 'cu profil scurt'), ('imitație', 'Partea superioară din imitație de piele , care oferă încălțămintei un aspect estetic și facilitează întreținerea'),
   ('apă', 'Protecție împotriva apei datorită unei membrane speciale'), ('membrană', 'Talpă respirabilă cu membrană microporoasă, care facilitează eliminarea umidității la exterior'),
   ('arici', 'Închidere practică cu arici'), ('șireturi', 'Șireturi elastice'), ('guler', 'Guler moale al părții superioare , care minimizează riscul de abraziuni'),
   ('căptușeală', 'Căptușeală moale din material textil'), ('călcâi', 'Călcâi întărit , care stabilizează piciorul, permițând pași mai siguri'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici și șireturi elastice', 'Cod produs': 'J367RE.0MEMS'})

w(13040,
  f'<p>În numerele mici, 24-27, {GEOX} ECLYPER J66LRG albi sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu detalii cu sclipici, din imitație de piele și material textil, ușori și rezistenți. Tehnologia GEOX Respira scoate umiditatea și ține pantoful uscat pe dinăuntru.</p>'
  '<p>Aricii fac încălțatul și descălțatul rapid, iar talpa plată din cauciuc ține piciorul sigur la fiecare pas. Sclipiciul dă pantofului un aer vesel.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Interior', 'material textil, moale.'), ('Branț', 'textil, aerisit.'), ('Închidere', 'arici.'))
  + '<p>Se potrivesc fetițelor de aproximativ 2-4 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi J66LRG.0BCKC'), ('sclipici', 'Detaliile cu sclipici'), ('material', 'Partea superioară din imitație de piele și material textil contribuie la durabilitate și lejeritate'),
   ('Respira', 'Tehnologia GEOX Respira™ sprijină respirabilitatea piciorului, eliminând umiditatea'), ('arici', 'Închiderea practică cu arici'),
   ('talpă', 'Talpa plată din cauciuc contribuie la stabilitate în timpul fiecărui pas'), ('interior', 'Interiorul din material textil permite o învăluire moale'), ('branț', 'Branțul respirabil din material textil')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici, detalii cu sclipici', 'Cod produs': 'J66LRG.0BCKC'})

w(13045,
  f'<p>Ghetele scurte {A("/brand/biomecanics/", "Biomecanics")} 261161 roz sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} tip chelsea, din piele naturală, cu motiv animal, fără izolație, pentru sezonul de tranziție și vremea schimbătoare. Urcă peste gleznă și apără de frig și de murdărie.</p>'
  '<p>Se închid cu arici și fermoar, deci se pun repede. Vârful și călcâiul sunt întărite.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'plată, din cauciuc, subțire, de 0-2 cm.'), ('Căptușeală', 'textilă, cu branțuri detașabile.'), ('Podology Partnership', 'creată cu podologi.'))
  + '<p>Numerele 19-23 se potrivesc fetițelor de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Ghete scurte pentru copii din piele roz 261161'), ('chelsea', 'Model botine chelsea'), ('piele', 'Partea superioară confecționată din piele naturală'),
   ('animal', 'Motiv animal'), ('izolație', 'Fără izolație interioară'), ('tranziție', 'potrivit pentru sezonul de tranziție'), ('gleznă', 'Înălțime peste gleznă , ce asigură protecție împotriva frigului și a murdăriei'),
   ('închidere', 'Model echipat cu închidere cu arici și fermoar'), ('vârf', 'Vârf întărit și călcâi întărit'), ('talpă', 'Talpă plată din cauciuc cu o grosime de 0-2 cm'),
   ('căptușeală', 'Interior cu căptușeală textilă și branțuri detașabile'), ('Podology', 'Tehnologia Biomecanics Podology Partnership , creată în colaborare cu podologii')],
  {'Model': 'Biomecanics 261161 (chelsea)', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici și fermoar, fără izolație, peste gleznă', 'Cod produs': '261161'})

w(13049,
  f'<p>Același model {A("/brand/primigi/", "Primigi")} 23918, în numerele 36-40: {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} sport de trekking, bleumarin, pentru hiking pe orice vreme. Apa nu trece de membrana GORE-TEX, iar piciorul rămâne aerisit.</p>'
  '<p>Înșiretarea rapidă se strânge dintr-o mișcare. Șocurile de la pas sunt preluate de Shock Absorber, iar gulerul și călcâiul întărit țin piciorul pe loc. Talpa cu bandă de rulare se prinde bine de teren.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Exterior', 'piele întoarsă și sintetic.'), ('Branț', 'textil.'), ('Talpă', 'cu bandă de rulare.'))
  + '<p>Se potrivesc copiilor de pe la 12 ani în sus.</p>',
  [('model', 'Primigi Încălțăminte sport pentru copii bleumarin PPTGT 23918'), ('trekking', 'Ghetele de trekking Primigi sunt încălțăminte sport pentru copii'), ('hiking', 'potrivit pentru hiking și trekking în condiții meteorologice variate'),
   ('GORE-TEX', 'Membrana GORE-TEX® menține picioarele uscate, blocând apa și permițând respirabilitatea'), ('înșiretare', 'Sistemul de înșiretare rapidă'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă'), ('călcâi', 'Călcâiul întărit și gulerul superior sprijină stabilizarea piciorului'),
   ('material', 'Partea superioară din piele întoarsă și material sintetic'), ('branț', 'Branțul din material textil'), ('talpă', 'Talpa cu bandă de rulare asigură o bună aderență pe suprafețe variate')],
  {'Model': 'Primigi 23918', 'Material': 'piele întoarsă și sintetic, interior textil', 'Caracteristici': 'GORE-TEX, Shock Absorber, înșiretare rapidă', 'Cod produs': 'PPTGT 23918'},
  notes=['Magazinul îi descrie drept ghete de trekking; pe site sunt la Pantofi.'])

w(13056,
  f'<p>Cămașa {TH} KB0KB10601 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "cămașă pentru băieți")} în culoarea albastru, simplă, cu mânecă lungă, din bumbac moale cu puțin elastan, în stil casual-elegant. Are logo brodat, discret, și guler clasic, moale.</p>'
  '<p>Croiala regulară lasă loc de mișcare, iar stilul casual-elegant se potrivește cu multe combinații. Bumbacul e moale și plăcut la purtare toată ziua.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '97% bumbac, 3% elastan.'), ('Mânecă', 'lungă, clasică.'), ('Guler', 'clasic, moale.'))
  + '<p>Mărimile 128-176 sunt pentru băieți de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Cămașă pentru copii cu bumbac albastră simplă KB0KB10601'), ('culoare', 'Culoare albastru'), ('mânecă', 'Mânecă lungă, clasică'),
   ('bumbac', 'Confecționată din bumbac moale'), ('stil', 'Un stil universal casual-elegant'), ('logo', 'Logo brodat al mărcii reprezintă un accent discret'),
   ('guler', 'Guler moale, clasic'), ('croială', 'Croială regulară favorizează libertatea de mișcare'), ('material', '97% Bumbac, 3% Elastan')],
  {'Model': 'Tommy Hilfiger KB0KB10601', 'Material': '97% bumbac, 3% elastan', 'Caracteristici': 'logo brodat, guler clasic, mânecă lungă', 'Cod produs': 'KB0KB10601'})

w(13057,
  f'<p>Salopeta de blugi {A("/brand/liewood/", "Liewood")} Delani Stripe Denim Dungarees e listată la {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")}: are talie înaltă și e din denim cu model în dungi, 100% bumbac, în culoarea bleumarin. Bretelele se reglează și se pot detașa.</p>'
  '<p>Are un buzunar în față și două buzunare laterale, pentru mărunțișurile de la joacă. Bumbacul e plăcut pe piele, iar bretelele se scot când nu e nevoie de ele.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Bretele', 'detașabile, reglabile.'), ('Buzunare', 'unul în față, două laterale.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 92-116 se potrivesc copiilor de aproximativ 2-6 ani.</p>',
  [('model', 'Liewood Jeans copii Delani Stripe Denim Dungarees LW20579'), ('salopetă', 'Tip produs: salopetă'), ('talie', 'fason cu talia înaltă'), ('denim', 'denim din model'),
   ('model', 'Model: cu modele'), ('culoare', 'Culoare bleumarin'), ('bretele', 'Model cu bretele detasabile'), ('reglabil', 'Caracter: reglabil'),
   ('buzunar', 'In fata buzunar'), ('laterale', 'Două buzunare laterale'), ('material', '100% Bumbac')],
  {'Model': 'Liewood Delani (salopetă)', 'Material': '100% bumbac (denim)', 'Caracteristici': 'bretele detașabile, talie înaltă, buzunare', 'Cod produs': 'LW20579'},
  notes=['Produsul e o salopetă de blugi, listată la Pantaloni.'])

w(13060,
  f'<p>Puloverul {TH} KB0KB09753 albastru este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "pulover pentru băieți")} clasic, din bumbac 100% cu țesătură împletită, cu decolteu rotund, pentru zilele mai răcoroase de toamnă și iarnă. Croiala simplă se îmbracă ușor pe cap.</p>'
  '<p>Decolteul, baza și manșetele au borduri elastice, care țin forma. Nu are buzunare, iar bumbacul e plăcut pe piele. Mânecile lungi țin de cald în zilele reci.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Mâneci', 'lungi, clasice.'), ('Textură', 'împletită.'))
  + '<p>Mărimile 104-122 sunt pentru băieți de în jur de 4-7 ani.</p>',
  [('model', 'Tommy Hilfiger Pulover pentru copii din bumbac albastru KB0KB09753'), ('clasic', 'Stilul clasic'), ('bumbac', 'Confecționat din 100% bumbac'),
   ('împletit', 'Țesătura împletită'), ('decolteu', 'Decolteul rotund cu bordură elastică'), ('sezon', 'zilele de toamnă și iarnă'),
   ('pe cap', 'facilitează îmbrăcarea și dezbrăcarea pe cap'), ('borduri', 'Bordurile elastice de la bază și manșete contribuie la menținerea formei'),
   ('buzunare', 'Lipsa buzunarelor'), ('mâneci', 'Mâneci lungi, clasice'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB09753', 'Material': '100% bumbac', 'Caracteristici': 'decolteu rotund, țesătură împletită, borduri elastice', 'Cod produs': 'KB0KB09753'})
