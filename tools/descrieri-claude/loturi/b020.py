import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
CKJ = A('/brand/calvin-klein-jeans/', 'Calvin Klein Jeans')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9319,
  f'<p>{GEOX} FLEXYPER J569BA sunt ghete de iarnă verzi, listate pe site la {A("/categorie/baieti-incaltaminte-pantofi/", "încălțămintea de iarnă pentru băieți")}, din nubuc, imitație de piele și material textil, cu membrana microporoasă GEOX Respira™, care elimină umezeala. Magazinul precizează că nu au impermeabilitate dedicată, deci sunt pentru zilele uscate de iarnă.</p>'
  '<p>Se închid cu arici, deci se încalță repede, iar vârful rigidizat protejează degetele la joacă.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'spumă și cauciuc, cu profil plat.'), ('Călcâi', 'întărit.'), ('Interior', 'material textil și sintetic.'))
  + '<p>Numerele 36-39 sunt pentru copii mari, de la aproximativ 12 ani în sus.</p>',
  [('model', 'Geox Încălțăminte pentru copii FLEXYPER verde J569BA.0ME32'), ('iarnă', 'Ghetele de iarnă Geox FLEXYPER'), ('material', 'Partea superioară din nubuc, imitație de piele și materiale textile'),
   ('Respira', 'Tehnologia GEOX Respira™ cu o membrană microporoasă'), ('zile uscate', 'Absența impermeabilității dedicate înseamnă că modelul este conceput pentru zilele uscate de iarnă'),
   ('arici', 'Închidere cu arici'), ('vârf', 'Vârful rigidizat contribuie la protejarea degetelor'), ('talpă', 'Talpă din spumă și cauciuc cu profil plat'),
   ('călcâi', 'Călcâiul întărit'), ('interior', 'Material textil, Material sintetic')],
  {'Model': 'Geox FLEXYPER J569BA', 'Material': 'nubuc, imitație de piele și textil, talpă din spumă și cauciuc', 'Caracteristici': 'ghete de iarnă, GEOX Respira™, arici, fără impermeabilitate dedicată', 'Cod produs': 'J569BA.0ME32'},
  notes=['Pe site e la Pantofi; produsul e ghetă de iarnă.'])

w(9322,
  f'<p>{CKJ} IG0IG02988 este o {A("/categorie/geci-jachete/", "geacă de iarnă pentru fete")}, portocalie, matlasată, din poliamidă netedă, izolată cu umplutură din poliester reciclat și căptușită. E făcută pentru temperaturile mai reci, iar gluga apără capul.</p>'
  '<p>Croiala e simplă, iar fermoarul e dublat de capse, ca geaca să se închidă bine pe vânt; banda elastică de la mâneci le strânge pe încheieturi.</p>'
  '<p>Pe scurt:</p>'
  + L(('Buzunare', 'două, laterale.'), ('Glugă', 'are.'), ('Material', '100% poliamidă, căptușeală poliester.'), ('Umplutură', '100% poliester reciclat.'))
  + '<p>Mărimile de pe site, 116-170, sunt pentru copii de aproximativ 6-15 ani.</p>',
  [('cod', 'IG0IG02988'), ('culoare', 'culoarea portocaliu'), ('izolat', 'Model izolat'), ('matlasat', 'Model matlasat'), ('temperaturi', 'temperaturi mai reci'),
   ('glugă', 'Gluga: cu gluga'), ('croială', 'Tăiere simplă'), ('fermoar, capse', 'Fixare cu fermoar și snap'), ('bandă elastică', 'Banda elastica: 97% Poliester , 3% Elastan'),
   ('buzunare', 'Două buzunare laterale'), ('material', 'Materialul de baza: 100% Poliamida'), ('umplutură', 'Umplutura: 100% Poliester reciclat'), ('căptușeală', 'Captuseala: 100% Poliester')],
  {'Model': 'Calvin Klein Jeans IG0IG02988', 'Material': '100% poliamidă, umplutură poliester reciclat', 'Caracteristici': 'izolată, matlasată, glugă, fermoar și capse', 'Cod produs': 'IG0IG02988'})

w(9328,
  f'<p>{A("/brand/reima/", "Reima")} Tallustelu sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași rezistenți la apă unisex")}, bej, cu fața din textil combinat cu imitație de piele și finisaj hidrofob pe fața superioară, care ține umezeala afară. Sunt ușori și făcuți pentru purtat zilnic, inclusiv toamna.</p>'
  '<p>Au șireturi rapide cu opritor, care se strâng dintr-o tragere, și cutia degetelor lată, cu loc pentru un picior mai plin. Inserțiile detașabile Happy Fit ajută la alegerea mărimii.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Buclă', 'la spate, pentru încălțat.'), ('Talpă', 'exterioară, din cauciuc.'), ('Apă', 'rezistență sporită, fără impermeabilitate completă.'))
  + '<p>Numerele 28-40 sunt pentru copii de la 4 ani în sus, cu aproximație.</p>',
  [('model', 'Sneakers pentru copii Tallustelu culoarea bej, 5400137C'), ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('hidrofob', 'Finisajul hidrofob al feței superioare'), ('șireturi', 'Sistemul rapid de șireturi cu opritoare'), ('cutie lată', 'Cutia lată a degetelor'),
   ('Happy Fit', 'Inserțiile detașabile Happy Fit'), ('buclă', 'Bucla ușurează să pui pantoful în picior'), ('talpă', 'Talpa exterioară din cauciuc'),
   ('nu complet', 'nu garantează impermeabilitatea completă')],
  {'Model': 'Reima Tallustelu', 'Material': 'textil și piele ecologică, talpă din cauciuc', 'Caracteristici': 'finisaj hidrofob, șireturi rapide, Happy Fit, cutie lată', 'Cod produs': '5400137C'})

w(9329,
  f'<p>{GEOX} IUPIDOO B3555C sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")}, bleumarin, lucrați din textil și imitație de piele, cu interior din piele naturală, care previne frecarea și mirosurile. Au sistemul Geox Respira în talpă.</p>'
  '<p>Se închid cu arici, deci se încalță repede, iar partea de sus e rigidizată, cu vârf rotund; talpa din cauciuc absoarbe șocurile la primii pași prin casă și prin parc.</p>'
  '<p>Pe scurt:</p>'
  + L(('Interior', 'piele naturală.'), ('Talpă', 'din cauciuc.'), ('Închidere', 'arici.'), ('Profil', 'scurt.'))
  + '<p>Numerele 18-26 se potrivesc copiilor de cam 1-4 ani.</p>',
  [('model', 'Sneakers pentru copii IUPIDOO culoarea bleumarin, B3555C.01454'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('interior', 'Un model cu interior din piele care este confortabil pentru picior și previne frecarea'), RESPIRA, ('arici', 'Închiderea cu velcro'),
   ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Varf rotund'), ('talpă', 'Talpă din cauciuc'), ('absorbție', 'Absorbtia socului'), ('profil', 'Înălțime: mic de statură')],
  {'Model': 'Geox IUPIDOO B3555C', 'Material': 'textil și piele ecologică, interior din piele naturală', 'Caracteristici': 'Geox Respira, arici, interior din piele', 'Cod produs': 'B3555C.01454'})

w(9339,
  f'<p>{GEOX} THELEVEN sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași înalți pentru băieți")}, bej, din piele întoarsă, imitație de piele și material textil, cu talpa GEOX Respira™ cu membrană, care elimină umezeala și ține apa afară. Merg de la joaca afară la școală.</p>'
  '<p>Se închid cu fermoar și șireturi elastice: fermoarul deschide gheata la încălțat, iar șireturile rămân strânse. Profilul e înalt, cu guler ușor rigidizat la gleznă.</p>'
  '<p>Pe dinăuntru și pe dedesubt:</p>'
  + L(('Interior', 'piele naturală, material sintetic și textil.'), ('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'))
  + '<p>Numerele 28-39 se potrivesc copiilor de la aproximativ 4 ani în sus.</p>',
  [('model', 'Geox THELEVEN sneakers pentru copii bej J46LDC.05422'), ('material', 'Combinația de piele întoarsă, imitație de piele și material textil'),
   ('Respira', 'Tehnologia GEOX Respira™ cu membrană favorizează respirabilitatea, eliminând umezeala și protejând împotriva apei'), ('școală', 'de la joaca în aer liber la provocările școlare'),
   ('închidere', 'Închiderea cu fermoar și șireturi elastice'), ('profil', 'Profilul înalt al părții superioare cu un guler ușor rigidizat'),
   ('interior', 'Interiorul din piele naturală, material sintetic și material textil'), ('talpă', 'Talpa plată din cauciuc'), ('călcâi', 'Călcâiul întărit')],
  {'Model': 'Geox THELEVEN', 'Material': 'piele întoarsă, imitație de piele și textil, interior cu piele naturală', 'Caracteristici': 'profil înalt, fermoar și șireturi elastice, GEOX Respira™', 'Cod produs': 'J46LDC.05422'})

w(9344,
  f'<p>{GEOX} INEK J659CB sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, cu exteriorul din piele ecologică și textil, interior textil și sistemul Geox Respira în talpă. Au profil scurt și detalii decorative.</p>'
  '<p>Se închid cu arici, iar bucla de la spate ajută la încălțat, așa că pantofii se pun repede; partea de sus e rigidizată, cu vârf rotund.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'din cauciuc.'), ('Interior', 'textil, ușor de ținut curat.'), ('Închidere', 'arici.'))
  + '<p>Numerele 28-35 sunt, de regulă, pentru copii de 4-11 ani.</p>',
  [('model', 'Sneakers pentru copii INEK culoarea bleumarin, J659CB.01454'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), RESPIRA, ('profil', 'Înălțime: mic de statură'),
   ('decorative', 'Detalii decorative'), ('arici', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'), ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Varf rotund'),
   ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox INEK J659CB', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici, buclă la spate', 'Cod produs': 'J659CB.01454'})

w(9348,
  f'<p>{CKJ} IB0IB02570 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")}, neagră, matlasată și izolată, din material ornamentat, cu glugă și căptușeală. E pentru frig, iar gulerul ridicat are o bandă pe fermoar, ca să nu atingă bărbia.</p>'
  '<p>Croiala e simplă, iar mânecile se termină cu bandă elastică, care le strânge pe încheieturi. Căptușeala o face ușor de îmbrăcat peste un pulover.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Glugă', 'are.'), ('Material', '100% poliester.'))
  + '<p>Mărimile de pe site, 128-170, se potrivesc copiilor de cam 8-15 ani.</p>',
  [('cod', 'IB0IB02570'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat cu captuseala'), ('matlasat', 'Matlasat'), ('ornamentat', 'Material ornamentat'),
   ('glugă', 'Model cu gluga'), ('guler', 'Guler ridicat cu membrana pe fermoar'), ('croială', 'Tăiere simplă'), ('elastic', 'Mâneci finisate cu o coadă elastică'),
   ('fermoar', 'Incheiere cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans IB0IB02570', 'Material': '100% poliester', 'Caracteristici': 'izolată, matlasată, glugă, guler cu protecție la fermoar', 'Cod produs': 'IB0IB02570'})

w(9350,
  f'<p>{A("/brand/primigi/", "Primigi")} PIM 24565 sunt ghete de trekking înalte, verzi, listate pe site la {A("/categorie/unisex-incaltaminte-pantofi/", "încălțăminte unisex")}, create împreună cu asociația italiană de podologi SIPeP. Sunt pentru copiii activi, la drumeții și joacă afară.</p>'
  '<p>Șireturile elastice se combină cu arici, deci gheata se ajustează rapid pe picior; călcâiul și gulerul ușor întărite țin glezna, iar sistemul Anti-Shock are o cameră de aer în talpă.</p>'
  '<p>Pe dinăuntru și pe dedesubt:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare.'), ('Branț', 'detașabil, din piele naturală.'), ('Material', 'imitație de piele cu finisaj de piele întoarsă.'))
  + '<p>Numerele 26-37 sunt pentru copii de la cam 3 ani în sus.</p>',
  [('model', 'Primigi Încălțăminte pentru copii verde PIM 24565'), ('trekking', 'Încălțămintea de trekking Primigi'), ('înaltă', 'încălțăminte înaltă pentru copii'),
   ('SIPeP', 'asociația italiană de podologi SIPeP'), ('activi', 'creată pentru micuții activi'), ('închidere', 'Șireturi elastice în combinație cu închiderea cu arici'),
   ('călcâi, guler', 'Călcâiul întărit și gulerul superior ușor întărit'), ('Anti-Shock', 'Sistemul Anti-Shock cu o cameră de aer în talpă'),
   ('talpă', 'Talpa de cauciuc cu bandă de rulare'), ('branț', 'Branțul detașabil din piele naturală'), ('material', 'Partea superioară din imitație de piele cu finisaj din piele întoarsă')],
  {'Model': 'Primigi PIM 24565', 'Material': 'imitație de piele, interior textil și piele naturală, talpă din cauciuc', 'Caracteristici': 'trekking, SIPeP, Anti-Shock, șireturi elastice și arici', 'Cod produs': '24565'},
  notes=['Pe site e la Pantofi; produsul e încălțăminte înaltă de trekking.'])

w(9352,
  f'<p>{A("/brand/columbia/", "Columbia")} Mighty Mogul este o {A("/categorie/geci-jachete/", "geacă de schi pentru fete")}, bordo, izolată, cu două tehnologii Columbia: Omni-tech®, cu membrană și cusături sudate, și Omni-Heat™ Infinity, căptușeala aurie care păstrează căldura. E făcută pentru sporturile de iarnă.</p>'
  '<p>Are sistemul OUTGROWN, care permite prelungirea mânecilor pe măsură ce copilul crește, deci geaca ține mai multe sezoane. Fasonul e drept, iar în interior o curea elastică, cauciucată, oprește zăpada.</p>'
  '<p>Pentru pârtie:</p>'
  + L(('Buzunar', 'pe mânecă, plus două laterale cu fermoar.'), ('Închidere', 'fermoar și arici.'), ('Glugă', 'are.'))
  + '<p>Mărimile 104-164 sunt pentru copii de aproximativ 4-14 ani.</p>',
  [('model', 'Geacă copii Mighty Mogul culoarea bordo, 2089611'), ('izolat', 'Model izolat cu captuseala'), ('Omni-tech', 'Tehnologia Omni-tech'),
   ('cusături', 'membranei microporoase, respirabile si a cusaturilor sudate'), ('Omni-Heat', 'Omni-Heat ™ Infinity este o membrana speciala de aur'),
   ('iarnă', 'Sporturi de iarnă'), ('OUTGROWN', 'Sistemul OUTGROWN Grow de la Columbia'), ('fason', 'Fason drept'),
   ('curea', 'curea elastică, cauciucată'), ('buzunar mânecă', 'Un buzunar suplimentar pe mânecă'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('închidere', 'Fixarea cu fermoar si velcro'), ('glugă', 'Model cu gluga')],
  {'Model': 'Columbia Mighty Mogul', 'Material': 'poliester, nailon și poliester reciclat', 'Caracteristici': 'Omni-tech®, Omni-Heat™ Infinity, OUTGROWN, centură anti-zăpadă', 'Cod produs': '2089611'})

w(9354,
  f'<p>{GEOX} ECLYPER B365LA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")}, albi pe site și albaștri la magazin, din piele întoarsă, ușori și făcuți pentru purtat zilnic, cu sistemul Geox Respira în talpă.</p>'
  '<p>Au sistemul Check Your Feet, care ajută la verificarea mărimii, iar aricii se prind repede; profilul sub gleznă nu restricționează mișcarea, iar contorul de călcâi rigid ține piciorul în pantof.</p>'
  '<p>Pe scurt:</p>'
  + L(('Vârf', 'rotund, ușor întărit.'), ('Talpă', 'exterioară, din cauciuc.'), ('Interior', 'textil.'))
  + '<p>Numerele 20-27 sunt pentru copii de pe la 1 până pe la 4 ani.</p>',
  [('model', 'Geox ECLYPER albastru B365LA.000BC'), ('material', 'confecționat din piele intoarsa'), ('zilnic', 'ideal pentru purtarea zilnică'), RESPIRA,
   ('Check Your Feet', 'Check Your Feet ajuta la ajustarea pantofilor'), ('arici', 'Închiderea cu velcro'), ('sub gleznă', 'Pantoful de sub gleznă'),
   ('călcâi', 'Contorul de călcâi rigid'), ('vârf', 'Cutie rotunda, usor intarita'), ('talpă', 'Talpa exterioară din cauciuc'), ('interior', 'Interiorul textil')],
  {'Model': 'Geox ECLYPER B365LA', 'Material': 'piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, Check Your Feet, arici', 'Cod produs': 'B365LA.000BC'},
  notes=['Titlul de pe site spune alb; magazinul arată albastru.'])
print('lot 20 scris')
