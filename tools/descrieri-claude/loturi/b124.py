import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
GU = '/categorie/unisex-imbracaminte-geci-jachete/'
PIELE = 'Descrierea spune „piele”, iar compoziția și atributele indică material sintetic, imitație de piele; am scris doar compoziția.'

w(12499,
  f'<p>Adidașii {PRIMIGI} 1421455 bleumarin sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} ușori, de tip barefoot, care lasă piciorul să se miște natural și să simtă solul. Talpa Vibram din cauciuc e flexibilă și preia șocurile, iar branțul anatomic se mulează pe picior.</p>'
  '<p>Fața e din imitație de piele, ușor de întreținut, interiorul e textil, iar vârful lat lasă loc degetelor. Contrafortul e ușor rigidizat, iar șireturile elastice și velcro-ul fac încălțatul rapid.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'imitație de piele.'), ('Branț', 'piele.'), ('Interior', 'material textil.'), ('Profil', 'scurt.'))
  + '<p>Numerele 26-29 corespund aproximativ vârstei de 3-5 ani.</p>',
  [('cod', '1421455'), ('culoare', 'Culoare bleumarin'), ('barefoot', 'pantofi barefoot'), ('natural', 'permite mișcarea naturală a piciorului'), ('Vibram', 'Tehnologia Vibram'),
   ('flexibilă', 'absorbție a șocurilor, flexibilă, cauciuc'), ('branț', 'Branțul anatomic'), ('față', 'Partea superioară:100% Imitație de piele'),
   ('întreținut', 'este ușor de întreținut'), ('interior', 'Interiorul din material textil'), ('lată', 'Croiala lată în zona degetelor'),
   ('contrafort', 'Contravortul ușor rigidizat'), ('velcro', 'Șireturile elastice și închiderea cu velcro'), ('piele', 'Branţ:100% Piele'), ('profil', 'scurt')],
  {'Model': 'Primigi 1421455', 'Talpă': 'Vibram, cauciuc', 'Caracteristici': 'barefoot, branț anatomic, velcro', 'Cod produs': '1421455'})

w(12500,
  f'<p>Geaca de schi {A("/brand/lego/", "LEGO")} 22881 albastră este o {A(GU, "geacă unisex")} matlasată, cu dungi, pentru activități de iarnă și ținute de oraș. Umplutura sintetică de grosime medie ține de cald fără să o îngreuneze, iar finisajul DWR limitează absorbția apei.</p>'
  '<p>Gluga e integrată, gulerul e înalt, iar închiderea se face cu fermoar. Are buzunare exterioare, iar croiala regular fit lasă loc de mișcare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Izolație', 'medie, sintetică.'), ('Tehnologie', 'DWR.'))
  + '<p>Mărimile 104-164 se potrivesc pe la 4-14 ani.</p>',
  [('cod', '22881'), ('culoare', 'Culoare albastru'), ('schi', 'Geaca de schi Lego'), ('matlasat', 'Construcția matlasată'), ('dungi', 'Modelul cu dungi'),
   ('iarnă', 'concepută pentru activități de iarnă și ținute casual'), ('umplutură', 'Umplutura sintetică asigură izolație termică fără a adăuga greutate inutilă'),
   ('medie', 'Izolația sintetică medie'), ('DWR', 'Finisajul hidrofob DWR ajută la limitarea absorbției apei'), ('glugă', 'Gluga integrată'), ('guler', 'Gulerul înalt'),
   ('fermoar', 'Închiderea cu fermoar'), ('buzunare', 'Buzunarele exterioare practice'), ('croială', 'Croiala regular fit'), ('material', 'Întregul produs:100% Poliester')],
  {'Model': 'LEGO 22881', 'Material': '100% poliester', 'Caracteristici': 'matlasată, DWR, glugă integrată', 'Cod produs': '22881'},
  notes=['Titlul site-ului nu are culoare („Unisex”); culoarea e cea de la magazin (albastru).', 'Atributele spun „necăptușit”, caracteristicile „fără căptușeală, sintetică”; nu am scris despre căptușeală.'])

w(12539,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8879800 bej sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} izolate, din textil și piele întoarsă, cu membrană GORE-TEX subțire, rezistentă la vânt și respirabilă, care ține piciorul uscat pe ploaie moderată. Căptușeala textilă e moale.</p>'
  '<p>Fața rezistă la înmuiere, are o inserție de ventilație, iar vârful rotund lasă degetele să se așeze liber. Se leagă cu șiret, bucla de la spate ajută la încălțat, iar talpa din cauciuc e durabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele întoarsă.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 31-35 merg cu aproximație la 6-11 ani.</p>',
  [('cod', '8879800'), ('culoare', 'culoarea bej'), ('izolat', 'Model Izolat din combinația materialului textil cu pielea întoarsă'), ('GORE-TEX', 'Model cu membrana GORE-TEX®'),
   ('vânt', 'rezistenta la vant si respirabila'), ('ploaie', 'Vă menține uscat în condiții de ploaie moderată'), ('căptușeală', 'căptușeală moale din material textil'),
   ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'), ('ventilație', 'Insertie de ventilatie'), ('vârf', 'degetele se pot aranja liber în pantof'),
   ('buclă', 'Bucla de la spate'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('gambă', 'Material textil, Piele intoarsa'), ('profil', 'înalt')],
  {'Model': 'Primigi 8879800', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, șiret, inserție de ventilație', 'Cod produs': '8879800'})

w(12553,
  f'<p>Geaca {TH} KB0KB10114 neagră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")} izolată, matlasată, din material neted cu izolație sintetică groasă. Finisajul hidrofob lasă apa să se adune pe suprafață și să se scurgă, fără să fie absorbită.</p>'
  '<p>Gluga e integrată, se închide cu fermoar și capsă, iar pe laterale are două buzunare. Căptușeala e completă, sintetică, iar tăietura e simplă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Izolație', 'groasă.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 țin cam de 8-16 ani.</p>',
  [('cod', 'KB0KB10114'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat confecționat din material neted'), ('matlasat', 'Model matlasat cu izolație sintetica'),
   ('groasă', 'groasă'), ('hidrofob', 'Finisajul hidrofob al materialului oferă rezistență la apă'), ('scurgă', 'permite apei să se acumuleze pe suprafața materialului și să se scurgă fără a fi absorbită'),
   ('glugă', 'integrată'), ('fermoar', 'Fixare cu fermoar si snap'), ('buzunare', 'Două buzunare laterale'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('material', '100% Poliester'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB10114', 'Material': '100% poliester', 'Caracteristici': 'izolație groasă, hidrofobă, glugă', 'Cod produs': 'KB0KB10114'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(12561,
  f'<p>Adidașii {GEOX} SPRINTYE argintii sunt {A("/categorie/adidasi/", "adidași pentru fete")} ușori, pentru purtat zilnic, cu sistemul Geox Respira: talpa în trei straturi are perforații care ajută ventilarea. Se închid cu velcro, deci se pun și se scot repede.</p>'
  '<p>Talpa exterioară din cauciuc e durabilă și rezistentă la deteriorare, branțul textil e confortabil și ține încălțămintea curată mai ușor, iar bucla de la spate ajută la încălțat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'scurt.'))
  + '<p>Numerele 24-27 se poartă cam la 2-4 ani.</p>',
  [('model', 'SPRINTYE'), ('culoare', 'culoarea argintiu'), ('ușor', 'Model ușor și confortabil, ideal pentru purtarea zilnică'), ('Respira', 'Sistemul Geox Respira'),
   ('straturi', 'talpei in trei straturi cu sistemul de perforari'), ('velcro', 'Închiderea cu velcro'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'),
   ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'), ('buclă', 'Bucla de la spate'), ('gambă', 'Material sintetic, Material textil'),
   ('profil', 'scurt')],
  {'Model': 'Geox SPRINTYE', 'Material': 'material sintetic, textil', 'Caracteristici': 'Geox Respira, velcro, ușori', 'Cod produs': 'J55FWA.0ASAJ'},
  notes=[PIELE])

w(12595,
  f'<p>Adidașii {GEOX} SKETLITE roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil înalt și tehnologia GEOX Respira, care ajută la termoreglarea piciorului și scoate umezeala în afară. Fața combină imitație de piele cu textil.</p>'
  '<p>Închiderea e multiplă, cu șireturi, arici și fermoar, pentru o potrivire exactă. Călcâiul și gulerul sunt ușor întărite, talpa plată e din cauciuc, iar branțurile textile se scot.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 28-31 se potrivesc orientativ la 4-7 ani.</p>',
  [('model', 'SKETLITE'), ('culoare', 'Culoare roz'), ('profil', 'Profilul înalt'), ('Respira', 'Tehnologia GEOX Respira'), ('termoreglare', 'favorizează termoreglarea piciorului, eliminând umezeala la exterior'),
   ('față', 'Partea superioară din imitație de piele și material textil'), ('închidere', 'Închiderea multiplă, care combină șireturi, arici și fermoar'),
   ('călcâi', 'Călcâiul ușor întărit'), ('guler', 'Gulerul ușor întărit'), ('talpă', 'Talpa plată din cauciuc'), ('branț', 'Branțurile detașabile din material textil'),
   ('interior', 'Interior:Material textil')],
  {'Model': 'Geox SKETLITE', 'Material': 'imitație de piele, textil', 'Caracteristici': 'Geox Respira, profil înalt, șiret, arici și fermoar', 'Cod produs': 'J66NWB.0NFKN'})

w(12597,
  f'<p>Adidașii {TH} T1X9-34347 albi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} ușori, pentru purtat zilnic, realizați parțial din poliester reciclat. Vârful rotund e întărit, iar contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece.</p>'
  '<p>Șireturile plate stau bine pe rist, iar velcro-ul face încălțatul rapid. Talpa exterioară din cauciuc e durabilă, plată, iar interiorul textil se păstrează ușor curat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic.'), ('Interior', 'material textil.'), ('Lungime branț', '19.5 cm la numărul 30.'))
  + '<p>Numerele 30-34 se potrivesc cam între 6 și 11 ani.</p>',
  [('cod', 'T1X9-34347'), ('culoare', 'culoarea alb'), ('ușor', 'Model ușor și confortabil, ideal pentru purtarea zilnică'), ('reciclat', 'realizat partial din poliester reciclat'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece'), ('șireturi', 'Sireturile plate'),
   ('velcro', 'Închiderea cu velcro'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('plată', 'plată'), ('interior', 'Interiorul textil este confortabil'),
   ('gambă', 'Material sintetic'), ('lungime', 'Lungimea brantului pentru marimea este de: 19.5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 30')],
  {'Model': 'Tommy Hilfiger T1X9-34347', 'Material': 'material sintetic', 'Caracteristici': 'șireturi plate, velcro, vârf întărit', 'Cod produs': 'T1X9.34347'},
  notes=[PIELE, 'Caracteristicile spun profil „înalt”, atributele „jos”; nu am scris despre înălțime.'])

w(12616,
  f'<p>Pantofii {GEOX} MAGNETAR ABX albaștri sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} izolați, cu profil înalt, din textil și piele ecologică, cu membrana Amphibiox, respirabilă, care apără talpa și fața de apă. Sistemul Geox Respira ajută ventilarea prin talpa perforată în trei straturi.</p>'
  '<p>Talpa din cauciuc are caneluri și ține bine pe teren, iar vârful cauciucat protejează degetele. Partea de sus ridicată sprijină glezna, iar șireturile rapide și bucla de la spate ajută la încălțat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 36-39 se poartă orientativ de la 12 ani în sus.</p>',
  [('model', 'MAGNETAR. ABX'), ('culoare', 'Culoare albastru'), ('izolat', 'Model izolat confectionat din combinatia materialului textil cu pielea ecologica'),
   ('Amphibiox', 'Tehnologia Amphibiox®'), ('membrană', 'Membrana special respirabila si nepermeabila protejeaza atat talpa exterioara, cat si cea superioara'),
   ('Respira', 'Sistemul Geox Respira'), ('caneluri', 'Talpa exterioară din cauciuc cu caneluri este durabilă și oferă o tracțiune bună'),
   ('vârf', 'Zona cauciucata de pe degete ofera protectie suplimentara'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('șireturi', 'Sistemul rapid de șireturi cu comutatoare'), ('buclă', 'Bucla de la spate'), ('gambă', 'Material sintetic, Material textil'), ('profil', 'înalt')],
  {'Model': 'Geox MAGNETAR ABX', 'Membrană': 'Amphibiox', 'Caracteristici': 'izolați, Geox Respira, șireturi rapide', 'Cod produs': 'J464LB.050FU'},
  notes=['Titlul site-ului are „MAGNETAR” în locul culorii; culoarea e cea de la magazin (albastru).', 'Magazinul îi numește „impermeabili”, dar spune și că nu garantează impermeabilitatea completă.'])

w(12619,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8934422 verzi sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme de iarnă pentru băieți")} izolate, din textil și piele ecologică, cu membrană GORE-TEX subțire, rezistentă la vânt și respirabilă. Interiorul e din fleece moale.</p>'
  '<p>Fața e rigidizată, vârful lat nu ciupește degetele, iar talpa groasă din cauciuc, cu bandă de rulare antiderapantă, preia șocurile. Se închid cu velcro.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele artificială.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 30-35 sunt gândite pentru aproximativ 6-11 ani.</p>',
  [('cod', '8934422'), ('culoare', 'culoarea verde'), ('izolat', 'Izolare: izolat'), ('GORE-TEX', 'Model cu membrana GORE-TEX®'), ('vânt', 'rezistenta la vant si respirabila'),
   ('fleece', 'Interior fleece'), ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('antiderapantă', 'absorbție a șocurilor, cu bandă de rulare, antiderapantă'), ('groasă', 'groasă, profilată'),
   ('velcro', 'Închiderea cu velcro'), ('gambă', 'Material textil, Piele artificiala'), ('profil', 'înalt')],
  {'Model': 'Primigi 8934422', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, interior fleece, velcro', 'Cod produs': '8934422'},
  notes=['Magazinul descrie membrana ca 100% impermeabilă; nu am scris „impermeabile”.'])

w(12677,
  f'<p>Același model {A("/brand/colmar/", "Colmar")} CAPTION, în varianta bleumarin, rămâne o {A(GU, "geacă unisex")} pentru copiii mici: matlasată, cu puf în umplutură și o izolație ușoară. Căptușeala acoperă tot interiorul și e sintetică.</p>'
  '<p>Închiderea combină fermoarul cu o capsă, gulerul stă ridicat, iar buzunarele de la exterior se încheie. Nu are glugă, așa că merge cu o căciulă pe vreme rece.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliester.'), ('Material 3', '90% poliamidă, 10% puf.'), ('Material 4', '99% poliester, 1% elastan.'))
  + '<p>Mărimile 86-98 merg cam la 1-3 ani.</p>',
  [('model', 'CAPTION'), ('culoare', 'culoarea bleumarin'), ('matlasat', 'Model ușor izolat confecționat din material matlasat'), ('puf', 'puf'), ('ușoară', 'ușoară'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('fermoar', 'Fixare cu fermoar si snap'), ('guler', 'Guler ridicat'), ('buzunare', 'Buzunare exterioare incheiata'),
   ('glugă', 'fără glugă'), ('material1', '100% Poliester'), ('material3', '90% Poliamida, 10% Puf'), ('material4', '99% Poliester , 1% Elastan')],
  {'Model': 'Colmar CAPTION', 'Material': 'poliester, poliamidă cu puf', 'Caracteristici': 'matlasată, puf, guler ridicat', 'Cod produs': '3484.2XX'},
  notes=['„Merge cu o căciulă” e o sugestie, dedusă din lipsa glugii.'])
