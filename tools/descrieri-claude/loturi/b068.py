import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
GUESS = A('/brand/guess/', 'GUESS')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
BIO = A('/brand/biomecanics/', 'Biomecanics')

w(12579,
  f'<p>{GEOX} WASHIBA bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu profil înalt și guler ușor întărit care susține glezna, din imitație de piele și material textil, cu logo Geox. Tehnologia GEOX Respira scoate umezeala și ține interiorul uscat.</p>'
  '<p>Aricii îl lasă pe copil să se încalțe singur, iar inserția elastică ajută pantoful să stea bine pe picior.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'material textil.'), ('Branț', 'textil, detașabil.'), ('Talpă', 'plată, din cauciuc, rezistentă la abraziune.'), ('Călcâi', 'ușor întărit.'))
  + '<p>Numerele 32-35 se potrivesc băieților de aproximativ 8-11 ani.</p>',
  [('model', 'Geox WASHIBA sneakers pentru copii bleumarin J66LQJ.0BC15'), ('profil', 'Profilul înalt al părții superioare , împreună cu gulerul ușor întărit, susține glezna copilului'),
   ('material', 'Combinația de imitație de piele și material textil'), ('logo', 'Modelul cu logo-ul mărcii Geox'), ('Respira', 'Tehnologia GEOX Respira™ favorizează eliminarea umidității'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea autonomă'), ('elastic', 'Inserția elastică favorizează o mai bună ajustare la picior'),
   ('căptușeală', 'Interiorul căptușit cu material textil'), ('branț', 'Branțurile detașabile din material textil'), ('talpă', 'Talpa plată din cauciuc'),
   ('abraziune', 'este rezistentă la abraziune'), ('călcâi', 'Călcâiul ușor întărit')],
  {'Model': 'Geox WASHIBA', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici, inserție elastică, profil înalt', 'Cod produs': 'J66LQJ.0BC15'})

w(12580,
  f'<p>{A("/brand/ugg/", "UGG")} LOWMEL bej sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} joși și căptușiți, din piele întoarsă și material textil, pentru zilele mai reci de oraș. Căptușeala UGGplush, din lână și lyocell, ține căldura în pantof.</p>'
  '<p>Se leagă cu șiret și au și șireturi de schimb, ca să schimbați aspectul legăturii. Vârful rotund lasă loc degetelor.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Călcâi', 'contrafort rigidizat, cu guler.'), ('Talpă', 'plată, din cauciuc.'), ('Interior', 'material textil.'))
  + '<p>Numerele 31-36 se poartă de pe la 6 ani în sus.</p>',
  [('model', 'UGG Încălțăminte pentru copii LOWMEL bej 1152410K'), ('jos', 'încălțăminte joasă și căptușită'), ('material', 'Partea superioară din piele întoarsă și material textil'),
   ('frig', 'zilele mai reci'), ('urban', 'condiții meteorologice urbane'), ('UGGplush', 'Căptușeala UGGplush din lână și lyocell asigură menținerea căldurii'),
   ('șiret', 'Fixare: cu snur'), ('șireturi', 'Șireturile suplimentare facilitează schimbarea aspectului legăturii'), ('vârf', 'Vârful rotund oferă degetelor spațiu adecvat'),
   ('călcâi', 'Contrefortul rigidizat , împreună cu gulerul'), ('talpă', 'Talpa plată din cauciuc'), ('interior', 'Material textil')],
  {'Model': 'UGG LOWMEL', 'Material': 'piele întoarsă și textil, căptușeală UGGplush din lână și lyocell, talpă din cauciuc', 'Caracteristici': 'șiret, șireturi de schimb, căptușiți', 'Cod produs': '1152410K'})

w(12582,
  f'<p>Geaca {GUESS} L6YL01 bej este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, uni, cu izolație sintetică medie, pentru sezonul de tranziție și joaca afară. Structura matlasată ține umplutura întinsă uniform, iar gluga integrată are guler ridicat contra vântului.</p>'
  '<p>Căptușeala integrală o face ușor de îmbrăcat, iar lungimea până la șolduri nu încurcă la mișcare.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Închidere', 'fermoar.'), ('Manșete și tiv', 'elastice.'), ('Buzunare', 'laterale, slip-on.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 122-125 până la 175 sunt gândite pentru băieți de cam 7-16 ani.</p>',
  [('model', 'Guess Geacă petrecută pentru copii bej L6YL01 W2655'), ('matlasat', 'Structura matlasată asigură o distribuție uniformă a izolației termice'), ('uni', 'Model uni în culoarea bej'),
   ('izolație', 'izolația termică sintetică medie'), ('tranziție', 'sezonul de tranziție'), ('aer liber', 'activități în aer liber'), ('glugă', 'Glugă integrată cu guler ridicat protejează împotriva vântului'),
   ('căptușeală', 'Căptușeala integrală facilitează îmbrăcarea'), ('lungime', 'Lungimea până la șolduri'), ('fermoar', 'Închidere cu fermoar'),
   ('elastic', 'Manșete și bază elastică'), ('buzunare', 'Buzunare laterale slip-on'), ('material', '100% Poliester')],
  {'Model': 'GUESS L6YL01', 'Material': '100% poliester, izolație sintetică medie', 'Caracteristici': 'matlasată, glugă integrată, fermoar', 'Cod produs': 'L6YL01 W2655'})

w(12584,
  f'<p>Adidașii {TH} T1X9-35260 albi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} sport, cu profil scurt, din material textil și sintetic. Combină șireturile cu scaiul, deci se reglează ușor și copilul se poate încălța singur.</p>'
  '<p>Talpa din spumă și cauciuc e ușoară și preia șocurile, iar călcâiul întărit ține piciorul pe loc la alergat.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Partea de sus', 'textil și material sintetic.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'spumă și cauciuc.'))
  + '<p>Numerele 30-34 sunt pentru copii de în jur de 6-11 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii albi T1X9-35260'), ('sport', 'încălțăminte sport cu profil scurt'), ('material', 'Combinația de material textil și sintetic în partea superioară'),
   ('închidere', 'Sistemul de șireturi și scai facilitează ajustarea ușoară și încălțarea independentă'), ('talpă', 'Talpa din spumă și cauciuc'),
   ('șocuri', 'Talpa ușoară din spumă favorizează absorbția șocurilor'), ('călcâi', 'Călcâi întărit susține stabilizarea piciorului'), ('interior', 'Interiorul căptușit cu material textil')],
  {'Model': 'Tommy Hilfiger T1X9-35260', 'Material': 'textil și sintetic, talpă din spumă și cauciuc', 'Caracteristici': 'șireturi și scai, profil scurt', 'Cod produs': 'T1X9-35260'})

w(12587,
  f'<p>{BIO} 261241 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, sport, cu profil înalt și guler ușor întărit, din imitație de piele și material textil, pentru joaca de fiecare zi. Talpa Flexi Lite e ușoară și flexibilă, deci piciorul se mișcă liber.</p>'
  '<p>Aricii fac încălțatul și descălțatul rapid, iar călcâiul întărit ține piciorul așezat corect.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Branț', 'textil, detașabil.'), ('Talpă', 'plată, din spumă.'), ('Podology Partnership', 'dezvoltată cu experți.'))
  + '<p>Numerele 28-34 se potrivesc băieților de cam 4-11 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii verzi 261241'), ('profil', 'Profil înalt cu guler ușor întărit'), ('material', 'combinația de imitație de piele și material textil'),
   ('zilnic', 'rezistentă la utilizarea zilnică'), ('Flexi Lite', 'Ușurința și flexibilitatea tălpii Flexi Lite'), ('arici', 'Închidere practică cu arici'),
   ('călcâi', 'Călcâi întărit stabilizează piciorul'), ('căptușeală', 'Căptușeală moale din material textil'), ('branț', 'Branțuri detașabile din material textil'),
   ('talpă', 'Talpă plată realizată din spumă'), ('Podology', 'tehnologiei Biomecanics Podology Partnership, dezvoltată cu experți')],
  {'Model': 'Biomecanics 261241', 'Material': 'imitație de piele și textil, interior textil, talpă din spumă', 'Caracteristici': 'Flexi Lite, arici, profil înalt, branț detașabil', 'Cod produs': '261241'})

w(12591,
  f'<p>Adidașii {TH} T1A9-34231 bej sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, cu partea de sus din material sintetic, care se închid cu velcro, deci se încalță și se descalță ușor. Cutia rotundă, întărită, apără degetele la joacă.</p>'
  '<p>Contrafortul rigidizat sprijină călcâiul și glezna, iar interiorul textil se păstrează curat ușor.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Talpă exterioară', 'din cauciuc, durabilă.'), ('Interior', 'material textil.'), ('Închidere', 'velcro.'))
  + '<p>Numerele 30-34 merg, orientativ, la fete de 6-11 ani; la 30 branțul are 19,5 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea bej, T1A9-34231'), ('profil', 'Înălțime: mic de statură'), ('gamba', 'Gamba: Material sintetic'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('lungime', 'Lungimea brantului pentru marimea este de: 19,5 cm')],
  {'Model': 'Tommy Hilfiger T1A9-34231', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, vârf întărit, contrafort rigidizat', 'Cod produs': 'T1A9-34231'},
  notes=['Descrierea magazinului spune piele întoarsă, dar compoziția și atributele dau material sintetic (imitație de piele); am scris material sintetic.'])

w(12594,
  f'<p>Geaca {GUESS} J6YL01 maro este o {A("/categorie/geci-jachete/", "geacă pentru fete")} matlasată, cu izolație sintetică medie, pentru zilele mai răcoroase de tranziție, cu un model decorativ cu logo Guess. Gluga integrată apără capul de vânt și de frigul ușor.</p>'
  '<p>Se închide cu fermoar și capse, iar tivul cu șnur și manșetele cu nervuri se strâng după copil.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'completă.'), ('Buzunare', 'laterale, inserate.'), ('Lungime', 'până la șolduri.'), ('Material', '100% poliester.'))
  + '<p>Mărimile încep la 122-125 și se opresc la 167, pentru fete de aproximativ 7-14 ani.</p>',
  [('model', 'Guess Geacă petrecută pentru copii maro J6YL01 W2607'), ('matlasat', 'Geaca matlasată Guess'), ('izolație', 'Izolație sintetică medie'),
   ('tranziție', 'sezonul de tranziție'), ('logo', 'Model decorativ cu logo'), ('glugă', 'Glugă integrată – contribuie la protejarea capului împotriva vântului și a frigului ușor'),
   ('închidere', 'Închidere cu fermoar și capse'), ('tiv', 'Tiv cu șnur și manșete cu nervuri'), ('căptușeală', 'Căptușeală completă'),
   ('buzunare', 'Buzunare laterale inserate'), ('lungime', 'Lungime până la șolduri'), ('material', '100% Poliester')],
  {'Model': 'GUESS J6YL01', 'Material': '100% poliester, izolație sintetică medie', 'Caracteristici': 'matlasată, glugă integrată, fermoar și capse, tiv cu șnur', 'Cod produs': 'J6YL01 W2607'})

w(12596,
  f'<p>{GEOX} PERTH sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, înalți, în stil casual și streetwear, din imitație de piele și material textil, cu logo Geox. Talpa are membrană microporoasă care oprește apa din exterior, iar GEOX Respira scoate umezeala dinăuntru.</p>'
  '<p>Combină șireturile cu aricii, deci se reglează ușor. Gulerul ușor întărit susține glezna.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Căptușeală', 'textilă.'), ('Branț', 'textil, detașabil.'), ('Călcâi', 'ușor întărit.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 28-35 sunt pentru băieți de cam 4-11 ani.</p>',
  [('model', 'Geox PERTH sneakers pentru copii verzi J367RF.0MEMS'), ('înalt', 'încălțăminte înaltă'), ('stil', 'Caracterul lor casual și streetwear'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('logo', 'Modelul cu logo-ul mărcii Geox'),
   ('membrană', 'Membrana microporoasă din talpă protejează împotriva pătrunderii apei din exterior'), ('Respira', 'Tehnologia GEOX Respira™ contribuie la eliminarea umezelii'),
   ('închidere', 'Combinația de șireturi și arici facilitează ajustarea'), ('guler', 'Profilul înalt al părții superioare cu un guler ușor întărit susține glezna'),
   ('căptușeală', 'Căptușeala interioară textilă'), ('branț', 'Branțurile detașabile textile'), ('călcâi', 'Călcâi ușor întărit'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, membrană în talpă, șireturi și arici', 'Cod produs': 'J367RF.0MEMS'})

w(12599,
  f'<p>Adidașii {TH} T1X9-35226 bleumarin sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} uni, cu profil scurt, din material sintetic ușor de întreținut, pentru jocurile și activitățile de zi cu zi. Profilul scurt lasă glezna să se miște liber.</p>'
  '<p>Aricii fac încălțatul și descălțatul rapid, iar călcâiul întărit ține piciorul drept. Talpa plată ține pasul sigur la mers și la joacă, iar culoarea uni merge cu multe ținute.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Interior', 'căptușit cu textil.'), ('Branț', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 24-29 merg la copii de aproximativ 2-5 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bleumarin T1X9-35226'), ('uni', 'Modelul uni al părții superioare permite o asortare ușoară cu multe ținute'), ('mers', 'Talpa plată din cauciuc oferă stabilitate în timpul mersului și al jocurilor'), ('profil', 'Profilul scurt al încălțămintei asigură libertate de mișcare la nivelul gleznei'),
   ('sintetic', 'Partea superioară din material sintetic este ușor de întreținut'), ('zilnic', 'jocurile și activitățile zilnice'),
   ('arici', 'Sistemul practic de închidere cu arici facilitează încălțarea și descălțarea rapidă'), ('călcâi', 'Călcâiul întărit stabilizează piciorul'),
   ('interior', 'Interiorul căptușit cu material textil'), ('branț', 'Branțul din material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Tommy Hilfiger T1X9-35226', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, profil scurt', 'Cod produs': 'T1X9-35226'})

w(12610,
  f'<p>Perechea {REIMA} Ankka în mărimi mari: {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} negre, de ploaie, din masă plastică mată și netedă, care țin piciorul uscat chiar și la precipitații mari. Elementele reflectorizante fac copilul mai vizibil seara.</p>'
  '<p>Inserțiile detașabile Happy Fit ajută la alegerea mărimii potrivite, iar bucla din spate ușurează încălțatul și descălțatul.</p>'
  '<p>Ce mai trebuie știut:</p>'
  + L(('Interior', 'sintetic și textil.'), ('Talpă exterioară', 'din cauciuc, rezistentă.'), ('Apă', 'impermeabile, dar fără garanția impermeabilității complete.'))
  + '<p>Sunt disponibile doar numerele 39-40, de la 12 ani în sus, orientativ.</p>',
  [('model', 'Reima Cizme copii Ankka culoarea negru, 5400158A'), ('plastic', 'Model confecționat din masa plastica mat, neted'),
   ('uscat', 'Modelul este realizat din materiale care asigură uscăciunea în timpul precipitațiilor mari'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('Happy Fit', 'Inserțiile detașabile Happy Fit vă permit să alegeți dimensiunea potrivită'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('interior', 'Material sintetic, Material textil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('apă', 'nu garantează impermeabilitatea completă')],
  {'Model': 'Reima Ankka', 'Material': 'masă plastică, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'cizme de ploaie, reflectorizante, inserții Happy Fit', 'Cod produs': '5400158A'})
