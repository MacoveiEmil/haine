import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(8977,
  f'<p>{REIMA} Vantti este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă ușor izolată unisex")}, violet, cu umplutură sintetică și rezistență sporită la apă, pentru temperaturile mai reci de toamnă și de primăvară. Materialul principal are 8% elastan, deci se întinde odată cu mișcarea copilului.</p>'
  '<p>Gulerul ridicat și gluga detașabilă apără gâtul și capul pe frig; gluga se scoate când nu e nevoie de ea.</p>'
  '<p>Mai are:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'cu închidere.'), ('Căptușeală', 'are.'), ('Material', '92% poliester, 8% elastan și 100% poliester.'))
  + '<p>Mărimile 92-140 sunt potrivite, în general, pentru copii de 2-10 ani.</p>',
  [('model', 'Geacă copii Vantti culoarea violet, 5100009C'), ('ușor izolat', 'Model ușor izolat'), ('izolație', 'izolatie sintetică'),
   ('apă', 'Model cu rezistență sporita la apă'), ('temperaturi', 'temperaturi mai reci'), ('elastan', 'Material 1: 92% Poliester , 8% Elastan'),
   ('glugă, guler', 'Gulerul ridicat și gluga detașabilă'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare incheiate'), ('căptușeală', 'Captuseala: cu captuseala'),
   ('material 2', 'Material 2: 100% Poliester')],
  {'Model': 'Reima Vantti', 'Material': '92% poliester, 8% elastan; 100% poliester', 'Caracteristici': 'ușor izolată, rezistentă la apă, glugă detașabilă, guler ridicat', 'Cod produs': '5100009C'})

w(8996,
  f'<p>{REIMA} Hiivin sunt ghete de iarnă violet, listate pe site la {A("/categorie/unisex-incaltaminte-pantofi/", "încălțăminte de iarnă unisex")}, izolate și cu membrana ReimaTec, care oprește ploaia și vântul. Magazinul declară confort termic până la -10°C, deci sunt pentru zăpadă și pentru zilele umede de iarnă.</p>'
  '<p>Inserțiile detașabile Happy Fit ajută la alegerea mărimii: le scoți și verifici cât loc are piciorul. Se închid cu arici, iar bucla de la spate ajută la încălțat.</p>'
  '<p>Pentru iernile scurte și drumurile pe întuneric:</p>'
  + L(('Elemente reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Talpă', 'exterioară, din cauciuc.'), ('Interior', 'textil și sintetic.'))
  + '<p>Numerele 24-36 acoperă copii de la cam 2 ani în sus.</p>',
  [('model', 'Pantofi copii Hiivin culoarea violet, 5400145A'), ('ghete', 'Ghete copii'), ('izolat', 'Izolare: izolat'), ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'),
   ('-10°C', 'Oferă confort termic până la -10°C'), ('nu complet', 'nu garantează impermeabilitatea completă'), ('Happy Fit', 'Inserțiile detașabile Happy Fit'),
   ('arici', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'), ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'),
   ('talpă', 'Talpa exterioară din cauciuc'), ('interior', 'Interiorul: Material sintetic, Material textil')],
  {'Model': 'Reima Hiivin', 'Material': 'sintetic și textil, talpă din cauciuc', 'Caracteristici': 'izolate, ReimaTec, până la -10°C, Happy Fit, arici, reflectorizante', 'Cod produs': '5400145A'},
  notes=['Pe site e la Pantofi; produsul e ghetă de iarnă izolată.'])

w(9004,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261241 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași înalți pentru băieți")}, bleumarin, din imitație de piele și material textil, cu talpă Flexi Lite, ușoară și flexibilă. Sunt adidași sport, pentru joacă și activitățile zilnice, din programul Biomecanics Podology Partnership.</p>'
  '<p>Profilul e înalt, cu guler ușor întărit, iar aricii se prind repede; branțurile textile detașabile se scot pentru curățat și pentru verificat lungimea piciorului.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'plată, din spumă, Flexi Lite.'), ('Călcâi', 'întărit.'), ('Căptușeală', 'textilă, moale.'))
  + '<p>Numerele 28-34 sunt pentru copii de cam 4-11 ani.</p>',
  [('cod', 'Sneakers pentru copii bleumarin 261241'), ('material', 'combinația de imitație de piele și material textil'), ('Flexi Lite', 'tălpii Flexi Lite'),
   ('sport', 'încălțăminte sport pentru copii'), ('zilnic', 'activităților zilnice și al jocurilor'), ('Podology', 'Biomecanics Podology Partnership'),
   ('profil', 'Profil înalt cu guler ușor întărit'), ('arici', 'Închidere practică cu arici'), ('branț', 'Branțuri detașabile din material textil'),
   ('talpă', 'Talpă plată confecționată din spumă'), ('călcâi', 'Călcâi întărit'), ('căptușeală', 'Căptușeală moale din material textil')],
  {'Model': 'Biomecanics 261241', 'Material': 'imitație de piele și textil, talpă din spumă', 'Caracteristici': 'profil înalt, Flexi Lite, arici, branț detașabil', 'Cod produs': '261241'})

w(9013,
  f'<p>{A("/brand/burton/", "Burton")} HILLSLOPE este o {A("/categorie/geci-jachete/", "geacă de schi pentru fete")}, izolată și căptușită, cu umplutură din poliester în mare parte reciclat (verde pe site, albastră la magazin). E făcută pentru sporturile de iarnă și pentru pârtie.</p>'
  '<p>În interior are o centură flexibilă, cauciucată, care oprește zăpada să intre pe dedesubt, iar gulerul ridicat și gluga fixă apără gâtul și capul.</p>'
  '<p>Detaliile de pârtie:</p>'
  + L(('Buzunar ski-pass', 'pe mânecă.'), ('Buzunare', 'exterioare, cu închidere.'), ('Închidere', 'fermoar.'), ('Certificări', 'Bluesign®; Burton e companie B Corporation.'))
  + '<p>Mărimile de pe site, de la 116-122 la 164-166, sunt pentru copii de aproximativ 6-14 ani.</p>',
  [('model', 'Burton Geaca copii HILLSLOPE 243131'), ('izolat', 'Model izolat cu captuseala'), ('umplutură', 'Umplutura: 95% Poliester reciclat, 5% Poliester'),
   ('sporturi de iarnă', 'Sporturi de iarnă'), ('centură', 'centura flexibila, cauciucata'), ('glugă, guler', 'Gulerul ridicat și gluga fixă'),
   ('ski-pass', 'Buzunar ski-pass pe maneca'), ('buzunare', 'Buzunare exterioare incheiata'), ('fermoar', 'Incheiere cu fermoar'),
   ('Bluesign', 'Model certificat Bluesign'), ('B Corp', 'B Corporation'), ('culoare magazin', 'albastru')],
  {'Model': 'Burton HILLSLOPE', 'Material': '100% poliester, umplutură 95% poliester reciclat', 'Caracteristici': 'geacă de schi, centură anti-zăpadă, buzunar ski-pass, glugă fixă', 'Cod produs': '243131'},
  notes=['Titlul de pe site spune verde; magazinul dă albastru.'])

w(9036,
  f'<p>{A("/brand/hugo/", "HUGO")} G00238 este o {A("/categorie/geci-jachete/", "geacă de iarnă pentru fete")}, roz, matlasată, izolată și căptușită, cu glugă. E din 100% poliester și e făcută pentru zilele reci, pentru copiii mari.</p>'
  '<p>Croiala e simplă, iar matlasarea ține umplutura distribuită uniform; fermoarul închide geaca până sus. Fiind căptușită, se îmbracă ușor și peste un hanorac gros.</p>'
  '<p>Detaliile gecii:</p>'
  + L(('Glugă', 'are.'), ('Buzunare', 'în față.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester.'))
  + '<p>Pe site sunt doar mărimile 156 și 162, potrivite cam pentru 13-14 ani.</p>',
  [('cod', 'Geaca copii culoarea roz, G00238'), ('izolat', 'Model izolat cu captuseala'), ('matlasare', 'Matlasare'), ('glugă', 'Model cu gluga'),
   ('croială', 'Tăiere simplă'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'In fata buzunare'), ('material', '100% Poliester')],
  {'Model': 'HUGO G00238', 'Material': '100% poliester', 'Caracteristici': 'izolată, matlasată, glugă, fermoar', 'Cod produs': 'G00238'})

w(9037,
  f'<p>{GEOX} PERTH în varianta verde sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași înalți pentru băieți")}, din imitație de piele și material textil, cu logo Geox. Talpa are membrană microporoasă și tehnologia Geox Respira™, care țin apa afară și elimină umezeala.</p>'
  '<p>Șiretul se combină cu o închidere cu arici, deci pantoful se ajustează ușor pe picior; profilul e înalt, cu guler ușor rigidizat la gleznă.</p>'
  '<p>Ce mai are:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'ușor întărit.'), ('Branț', 'detașabil, textil.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Numerele 28-41 îi fac potriviți pentru copii de 4 ani și peste, în general.</p>',
  [('model', 'Geox PERTH sneakers pentru copii verzi J367RF.0MEMS'), ('material', 'Fața superioară din imitație de piele și material textil'), ('logo', 'logo-ul mărcii Geox'),
   ('membrană', 'Membrana microporoasă din talpă protejează împotriva apei'), ('Respira', 'Tehnologia Geox Respira'), ('închidere', 'Combinația de șiret și închidere cu arici'),
   ('profil', 'Profilul înalt al feței superioare cu un guler ușor rigidizat'), ('talpă', 'Talpa plată din cauciuc'), ('călcâi', 'Călcâiul ușor întărit'),
   ('branț', 'Branțurile detașabile textile'), ('interior', 'Interiorul căptușit cu material textil')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, șiret și arici, membrană în talpă, Geox Respira™', 'Cod produs': 'J367RF.0MEMS'})

w(9038,
  f'<p>{GEOX} CASEY sunt {A("/categorie/incaltaminte-pantofi/", "mocasini pentru fete")}, negri și lăcuiți, din imitație de piele cu interior din piele naturală și textil. Sunt pantofi slip-on clasici, pentru serbări, evenimente școlare sau ieșiri, care merg și cu ținute casual.</p>'
  '<p>Fiind fără închidere, numărul trebuie ales exact, iar gulerul ușor întărit ține piciorul în pantof; vârful e rotund și lasă loc degetelor.</p>'
  '<p>Detaliile care contează la un pantof elegant:</p>'
  + L(('Branț', 'din piele naturală.'), ('Talpă', 'din cauciuc, flexibilă.'), ('Călcâi', 'întărit.'), ('Finisaj', 'lăcuit, uni.'))
  + '<p>Pe site sunt numerele 28-35, adică pentru copii de pe la 4 până pe la 11 ani.</p>',
  [('model', 'Geox Mocasini pentru copii CASEY negri J6620C.000HH'), ('lăcuit', 'Partea superioară din imitație de piele , cu finisaj lăcuit'),
   ('interior', 'Interior din piele naturală și material textil'), ('slip-on', 'Construcție slip-on'), ('ocazii', 'de la evenimente școlare la întâlniri cu prietenii'),
   ('casual', 'atât cu ținute casual, cât și cu cele mai elegante'), ('guler', 'Gulerul superior ușor întărit'), ('vârf', 'Vârf rotund, rigidizat , care oferă spațiu pentru degete'),
   ('branț', 'Branț din piele naturală'), ('talpă', 'Talpa din cauciuc'), ('călcâi', 'Călcâi întărit'), ('uni', 'Model uni , cu textură lăcuită')],
  {'Model': 'Geox CASEY', 'Material': 'imitație de piele lăcuită, interior piele naturală și textil, talpă din cauciuc', 'Caracteristici': 'mocasini slip-on, branț din piele', 'Cod produs': 'J6620C.000HH'},
  notes=['Titlul de pe site nu are culoare; magazinul arată negru.'])

w(9040,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} T1X9-35219 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, sport, cu profil scurt, din imitație de piele ușor de curățat. Sunt gândiți pentru jocurile și activitățile zilnice ale copiilor activi.</p>'
  '<p>Aricii îi lasă pe copii să se încalțe singuri, iar gulerul ușor întărit înconjoară glezna; profilul scurt nu o restricționează.</p>'
  '<p>Pe dedesubt și înăuntru:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Interior', 'material textil.'))
  + '<p>Cu numere de la 20 la 34, modelul se găsește pentru copii de aproximativ 1-11 ani.</p>',
  [('model', 'Sneakers pentru copii albi T1X9-35219'), ('sport', 'încălțăminte sport cu profil scurt'), ('material', 'Materialul exterior din imitație de piele'),
   ('curățenie', 'facilitează întreținerea curățeniei'), ('zilnic', 'jocurile și activitățile zilnice'), ('arici', 'Sistemul practic de închidere cu arici'),
   ('guler', 'gulerul ușor întărit'), ('talpă', 'Talpa plată din cauciuc'), ('călcâi', 'Călcâiul întărit'), ('interior', 'Interiorul din material textil')],
  {'Model': 'Tommy Hilfiger T1X9-35219', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'profil scurt, arici', 'Cod produs': 'T1X9-35219'})

w(9042,
  f'<p>{GEOX} LOFTUS sunt {A("/categorie/adidasi/", "adidași pentru fete")}, negri, din imitație de piele și material textil, cu logo. Talpa GEOX Respira™ are membrană microporoasă, care ține apa afară și elimină umezeala, deci adidașii merg și în zilele umede.</p>'
  '<p>Aricii sunt combinați cu o inserție elastică, astfel că pantoful se pune și se scoate repede, iar gulerul ușor întărit stă bine pe gleznă.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Căptușeală', 'textilă, moale.'), ('Branț', 'din material textil.'))
  + '<p>Pe site sunt numerele 24-35, pentru copii de cam 2-11 ani.</p>',
  [('model', 'Geox LOFTUS sneakers pentru copii negri J46M2A.0FU54'), ('material', 'Construcția din imitație de piele și material textil'), ('logo', 'modelul cu logo'),
   ('Respira', 'Talpă respirabilă GEOX Respira'), ('membrană', 'Membrana microporoasă din talpă protejează interiorul pantofului împotriva apei'),
   ('arici, elastic', 'Sistem de închidere cu arici în combinație cu o inserție elastică'), ('guler', 'Gulerul superior ușor întărit'),
   ('talpă', 'Talpă plată din cauciuc'), ('călcâi', 'Călcâi întărit'), ('căptușeală', 'Căptușeala moale din material textil'), ('branț', 'Branț din material textil')],
  {'Model': 'Geox LOFTUS', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'GEOX Respira™, membrană în talpă, arici cu elastic', 'Cod produs': 'J46M2A.0FU54'},
  notes=['Titlul de pe site nu are culoare; magazinul arată negru.'])

w(9044,
  f'<p>{GEOX} SPRINTYE sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} albi, din material textil și piele ecologică, cu profil scurt, talpă din cauciuc și sistemul Geox Respira. Interiorul textil e plăcut pentru picior și ușor de ținut curat.</p>'
  '<p>Se închid cu scai, deci se prind și se desprind repede, inclusiv de copilul mic; partea de sus e rigidizată, iar vârful rotund.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'scai.'), ('Talpă', 'din cauciuc.'), ('Interior', 'textil.'), ('Detalii', 'decorative.'))
  + '<p>Mărimile 20-27 sunt, de obicei, pentru copii de 1-4 ani.</p>',
  [('model', 'Sneakers pentru copii SPRINTYE culoarea alb, B654TA.0GNHH'), ('material', 'combinația materialului textil cu pielea ecologică'), ('profil', 'Înălțime: mic de statură'),
   ('talpă', 'Talpă din cauciuc'), RESPIRA, ('interior', 'interior textil care este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('scai', 'Fixare: cu scai'), ('arici', 'Închiderea cu velcro facilitează încălțarea'), ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Varf rotund'), ('decorative', 'Detalii decorative')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, scai, profil scurt', 'Cod produs': 'B654TA.0GNHH'})
print('lot 12 scris')
