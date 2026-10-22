import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9126,
  f'<p>{A("/brand/lego/", "LEGO")} LWJAZ 806 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de schi unisex")}, roz, izolată și căptușită, pentru sporturi de iarnă. Materialul exterior e rezistent la vânt și la apă, cu tratamentul BIONIC-FINISH® ECO și respirabilitate de 4000 g/m2/24h, deci geaca merge și la efort pe pârtie.</p>'
  '<p>Manșetele elastice au găuri pentru degetul mare, care țin mânecile pe mâini și opresc zăpada să intre; croiala e simplă, cu loc pentru un strat cald dedesubt.</p>'
  '<p>Detaliile de pârtie:</p>'
  + L(('Buzunar ski-pass', 'pe mânecă, cu fermoar.'), ('Elemente reflectorizante', '3M™ Scotchlite.'), ('Fermoare', 'YKK®.'), ('Glugă', 'detașabilă, cu guler ridicat.'))
  + '<p>Mărimile 98-164 sunt pentru copii de aproximativ 3-14 ani.</p>',
  [('model', 'Lego Geacă copii LWJAZ 806 culoarea roz, 11010966'), ('izolat', 'Model izolat cu captuseala'), ('iarnă', 'Sporturi de iarnă'),
   ('vânt, apă', 'Materialul exterior este rezistent la vânt și apă'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('respirabilitate', 'Respirabilitate: 4000 g/m2/24h'),
   ('degetar', 'Manșete elastice cu găuri pentru degetul mare'), ('croială', 'Tăiere simplă'), ('ski-pass', 'Buzunar funcțional pentru permis de schi, cu fermoar, pe mânecă'),
   ('reflectorizante', '3M ™ Scotchlite'), ('YKK', 'Fermoarele YKK'), ('glugă, guler', 'Gulerul ridicat și gluga detașabilă'), ('nu complet', 'nu garantează impermeabilitatea completă')],
  {'Model': 'LEGO LWJAZ 806', 'Material': '100% poliester', 'Caracteristici': 'geacă de schi, BIONIC-FINISH® ECO, manșete cu degetar, buzunar ski-pass, 3M Scotchlite', 'Cod produs': '11010966'})

w(9130,
  f'<p>{A("/brand/guess/", "GUESS")} J6YL01 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, roz, cu izolație sintetică medie și căptușeală integrală, pentru zilele mai reci de tranziție. Gluga integrată apără capul de vânt și de frigul ușor.</p>'
  '<p>Croiala e regulară, cu lungime până la șolduri, iar tivul cu șnur și manșetele cu nervuri strâng geaca jos și la încheieturi, ca să stea bine și pe un copil mai slab.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Închidere', 'fermoar și capse.'), ('Buzunare', 'laterale.'), ('Logo', 'model decorativ Guess.'), ('Material', '100% poliester.'))
  + '<p>Mărimile de pe site încep la 122-125 și ajung la 167, pentru copii de pe la 7 până pe la 14 ani.</p>',
  [('cod', 'Geacă petrecută pentru copii roz J6YL01 W2607'), ('matlasat', 'Geaca matlasată Guess'), ('izolație', 'Izolație sintetică medie'), ('căptușeală', 'Căptușeală integrală'),
   ('tranziție', 'sezonul de tranziție'), ('glugă', 'Glugă integrată'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'),
   ('tiv, manșete', 'Tiv cu șnur și manșete cu nervuri'), ('închidere', 'Închidere cu fermoar și capse'), ('buzunare', 'Buzunare laterale cu deschidere'),
   ('logo', 'Model decorativ cu logo'), ('material', '100% Poliester')],
  {'Model': 'GUESS J6YL01', 'Material': '100% poliester, izolație sintetică medie', 'Caracteristici': 'matlasată, glugă integrată, tiv cu șnur, fermoar și capse', 'Cod produs': 'J6YL01.W2607'})

w(9131,
  f'<p>{GEOX} GISLI sunt ghete de iarnă maro, listate pe site la {A("/categorie/baieti-incaltaminte-pantofi/", "încălțămintea de iarnă pentru băieți")}, din imitație de piele și material textil, cu tehnologia GEOX Respira™, care ține picioarele uscate la joacă. Se poartă în zilele reci, la ținute casual.</p>'
  '<p>Se închid cu arici, deci se încalță și se descalță repede; gulerul ușor întărit stă fix pe gleznă, iar călcâiul e ușor întărit.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Branț', 'din material textil.'), ('Interior', 'textil.'))
  + '<p>Numerele 28-39 se potrivesc copiilor de la aproximativ 4 ani în sus.</p>',
  [('model', 'Geox Încălțăminte pentru copii GISLI maro J465CC.0MEFU'), ('iarnă', 'Ghetele de iarnă pentru copii Geox GISLI'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('Respira', 'Tehnologia GEOX Respira'), ('uscat', 'menținând picioarele uscate'), ('casual', 'stilizațiile casual și streetwear în zilele reci'),
   ('arici', 'Închidere practică cu arici'), ('guler', 'Gulerul superior ușor întărit'), ('călcâi', 'Călcâi ușor întărit'), ('talpă', 'Talpă plată din cauciuc'),
   ('branț', 'Branț din material textil')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'ghete de iarnă, GEOX Respira™, arici', 'Cod produs': 'J465CC.0MEFU'},
  notes=['Pe site e la Pantofi; magazinul o descrie ca ghetă de iarnă.'])

w(9132,
  f'<p>{GEOX} WASHIBA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, din material sintetic, ușori și făcuți pentru purtat zilnic. Au profil scurt și sistemul Geox Respira în talpă, cu perforații.</p>'
  '<p>Talpa exterioară e din cauciuc cu caneluri, care ține bine pe asfalt și pe teren de joacă, iar vârful e rotund și lasă loc degetelor.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', 'sintetic, la exterior.'), ('Interior', 'textil.'), ('Talpă', 'din cauciuc, cu caneluri.'), ('Profil', 'scurt.'))
  + '<p>Numerele 28-35 sunt pentru copii de cam 4-11 ani.</p>',
  [('model', 'Sneakers pentru copii WASHIBA culoarea bleumarin, J65LQA.054FU'), ('sintetic', 'confecționat din material sintetic'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('profil', 'Înălțime: mic de statură'), RESPIRA, ('talpă', 'Talpa exterioară din cauciuc cu caneluri este durabilă și oferă o tracțiune bună'), ('vârf', 'Varf rotund'),
   ('interior', 'Interiorul: Material textil')],
  {'Model': 'Geox WASHIBA', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, talpă cu caneluri, profil scurt', 'Cod produs': 'J65LQA.054FU'})

w(9133,
  f'<p>{A("/brand/reima/", "Reima")} Sankari sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi de trekking unisex")}, gri, de tip barefoot, cu membrană impermeabilă și tehnologia ReimaTec. Sunt făcuți pentru drumeții și activități în aer liber, pe vreme schimbătoare.</p>'
  '<p>Construcția barefoot lasă piciorul într-o poziție naturală și degetele libere, iar branțurile detașabile Happy Fit ajută la alegerea mărimii.</p>'
  '<p>Pentru teren și pentru seară:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Călcâi', 'întărit.'), ('Detalii reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Închidere', 'șireturi elastice.'))
  + '<p>Numerele 32-40 îi fac potriviți pentru copii de 8 ani și peste, în general.</p>',
  [('model', 'Reima Pantofi pentru copii Sankari gri 5400160B'), ('trekking', 'Pantofii de trekking pentru copii Reima Sankari'), ('barefoot', 'Construcția de tip barefoot'),
   ('membrană', 'Membrana impermeabilă'), ('ReimaTec', 'Tehnologia ReimaTec'), ('aer liber', 'activități în aer liber'), ('degete', 'libertatea de mișcare a degetelor'),
   ('Happy Fit', 'Branțurile detașabile Happy Fit'), ('talpă', 'Talpa flexibilă din cauciuc'), ('călcâi', 'Călcâiul întărit'), ('reflectorizante', 'Detalii reflectorizante'),
   ('șireturi', 'șireturi elastice')],
  {'Model': 'Reima Sankari', 'Material': 'sintetic și textil, talpă din cauciuc', 'Caracteristici': 'barefoot, membrană impermeabilă, ReimaTec, Happy Fit, reflectorizante', 'Cod produs': '5400160B'})

w(9135,
  f'<p>{A("/brand/guess/", "GUESS")} L6RL11 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, bej, din pânză de bumbac rezistentă, care se usucă repede, ușor izolată cu umplutură din poliester. E pentru temperaturile mai scăzute de primăvară și toamnă.</p>'
  '<p>Marginea de jos are două capse care o strâng după talia copilului, iar manșetele moi se închid cu clic, deci geaca se ajustează și pe un copil mai slab.</p>'
  '<p>Detaliile:</p>'
  + L(('Guler', 'moale.'), ('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Material', 'bumbac 100%, căptușeală poliester și bumbac.'))
  + '<p>Mărimile de pe site încep la 122-125 și urcă până la 175, adică pentru copii de cam 7-16 ani.</p>',
  [('cod', 'L6RL11 WJ740'), ('culoare', 'culoarea bej'), ('pânză', 'material de pânză care este foarte durabil'), ('uscare', 'proprietăți de uscare rapidă'),
   ('ușor izolat', 'Model ușor izolat'), ('umplutură', 'Umplutura: 100% Poliester'), ('tranziție', 'Izolare: tranzitional'), ('temperaturi', 'temperaturi mai scăzute'),
   ('capse', 'Marginea inferioară cu două butoane de apăsare permite o potrivire personalizată'), ('manșete', 'Manșete moi cu închidere cu clic'), ('guler', 'Model cu guler moale'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('bumbac', 'Materialul de baza: 100% Bumbac'),
   ('căptușeală', 'Captuseala: 80% Poliester , 20% Bumbac')],
  {'Model': 'GUESS L6RL11', 'Material': '100% bumbac, căptușeală poliester și bumbac', 'Caracteristici': 'ușor izolată, uscare rapidă, capse la bază, manșete cu clic', 'Cod produs': 'L6RL11.WJ740'})

w(9140,
  f'<p>{A("/brand/primigi/", "Primigi")} PHR 23729 sunt {A("/categorie/ghete-cizme/", "botine de tranziție pentru fete")}, bej, din material sintetic ușor de curățat, cu talpă plată din cauciuc. Se poartă pe vremea schimbătoare de primăvară și toamnă, la ținute casual.</p>'
  '<p>Se închid cu fermoar, deci se încalță și se descalță repede, iar vârful rotund lasă loc degetelor. Branțul se scoate, pentru curățat sau pentru verificat lungimea piciorului.</p>'
  '<p>Ce mai au:</p>'
  + L(('Shock Absorber', 'tehnologie în talpă.'), ('Călcâi', 'întărit.'), ('Interior', 'finisat cu material textil.'), ('Colaborare', 'Primigi × SIPeP, pentru anatomia piciorului de copil.'))
  + '<p>Numerele 31-40 sunt, de obicei, pentru copii de la 6 ani în sus.</p>',
  [('model', 'Primigi Botine pentru copii bej PHR 23729'), ('tranziție', 'Botine ca încălțăminte de tranziție sunt potrivite pentru vremea schimbătoare de primăvară și toamnă'),
   ('sintetic', 'Partea superioară din material sintetic'), ('curățenie', 'facilitează menținerea curățeniei'), ('talpă', 'Talpa plată, confecționată din cauciuc'),
   ('casual', 'ținutele casual'), ('fermoar', 'Prinderea practică cu fermoar'), ('vârf', 'Vârful rotund oferă spațiu pentru degete'), ('branț', 'Posibilitatea de a scoate branțul'),
   ('Shock Absorber', 'Tehnologia Shock Absorber'), ('călcâi', 'Călcâiul întărit'), ('interior', 'Interiorul finisat cu material textil'), ('SIPeP', 'Colaborarea Primigi × SIPeP')],
  {'Model': 'Primigi PHR 23729', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'botine de tranziție, fermoar, Shock Absorber, branț detașabil', 'Cod produs': '23729'})

w(9142,
  f'<p>{GEOX} INEK în bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași cu lumini pentru băieți")}, din material textil și piele ecologică, cu membrana impermeabilă Geox Respira. Luminile se aprind de la un buton, deci seara copilul se vede mai bine.</p>'
  '<p>Șireturile elastice și închiderea cu cârlig se strâng fără nod, iar bucla de la spate ajută la încălțat; căptușeala textilă e moale și nu irită.</p>'
  '<p>Construcția:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Vârf', 'rotund.'), ('Partea de sus', 'rigidizată.'), ('Profil', 'jos.'))
  + '<p>Pe site sunt numerele 24-27, pentru copii de aproximativ 2-4 ani.</p>',
  [('model', 'Sneakers pentru copii INEK culoarea bleumarin, J569CC.05411'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('membrană', 'Membrana unica si impermeabila a tehnologiei Geox Respira'), ('lumini', 'Model cu lumini incorporate, activate de un buton'),
   ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('buclă', 'Bucla de la spate'), ('căptușeală', 'Căptușeala moale din material textil previne iritația'),
   ('talpă', 'Talpa exterioară din cauciuc'), ('vârf', 'Varf rotund'), ('rigidizat', 'Partea superioară rigidizată'), ('profil', 'Înălțime: jos')],
  {'Model': 'Geox INEK', 'Material': 'textil și piele ecologică, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'lumini, membrană Geox Respira, șireturi elastice', 'Cod produs': 'J569CC.05411'})

w(9149,
  f'<p>{GEOX} ECLYPER sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași înalți pentru bebeluși")}, bleumarin, din material textil și sintetic, cu logo Geox. Talpa GEOX Respira™ are membrană microporoasă, care elimină umezeala și ține piciorul uscat.</p>'
  '<p>Profilul înalt, cu guler ușor întărit, ține glezna fixă, iar aricii permit încălțatul rapid, chiar și când copilul se foiește. Interiorul textil ține piciorul într-un climat plăcut.</p>'
  '<p>Pe dinăuntru și pe dedesubt:</p>'
  + L(('Talpă', 'din cauciuc, plată.'), ('Călcâi', 'ușor întărit.'), ('Branț', 'textil.'), ('Interior', 'textil.'))
  + '<p>Numerele 20-27 sunt pentru copii de cam 1-4 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii bleumarin B665LB.000BC'), ('material', 'Partea superioară din material textil și sintetic'), ('logo', 'Modelul cu logo'),
   ('Respira', 'Tehnologia GEOX Respira'), ('membrană', 'membranei microporoase'), ('profil', 'Profilul înalt al părții superioare'), ('guler', 'Gulerul superior ușor întărit'),
   ('arici', 'Închiderea cu arici'), ('talpă', 'Talpa din cauciuc se caracterizează printr-un profil plat'), ('călcâi', 'Călcâiul ușor întărit'),
   ('branț', 'Branțul din material textil'), ('interior', 'Interiorul din material textil')],
  {'Model': 'Geox ECLYPER', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici, GEOX Respira™', 'Cod produs': 'B665LB.000BC'})

w(9150,
  f'<p>{GEOX} CIUFCIUF sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} maro, din piele întoarsă și material textil, cu talpă ușoară din spumă și tehnologia Geox Respira™, cu talpă perforată și membrană. Sunt pentru activitățile zilnice, la joacă și la plimbare.</p>'
  '<p>Aricii au inserție elastică, deci pantoful se pune repede și se strânge bine pe picior; profilul e scurt, cu guler ușor întărit.</p>'
  '<p>Ce mai au:</p>'
  + L(('Căptușeală', 'textilă, moale.'), ('Călcâi', 'întărit.'), ('Talpă', 'din spumă, plată.'))
  + '<p>Numerele 20-27 se potrivesc copiilor între aproximativ 1 și 4 ani.</p>',
  [('model', 'Geox CIUFCIUF sneakers pentru copii maro B455RB.0FU22'), ('material', 'Partea superioară din piele întoarsă , în combinație cu material textil'),
   ('talpă', 'Talpa ușoară din spumă'), ('Respira', 'Tehnologia Geox Respira™ cu talpă perforată și membrană'), ('zilnic', 'activitățile zilnice'),
   ('arici', 'Închiderea practică cu arici , cu inserție elastică'), ('profil', 'Profilul scurt al părții superioare'), ('guler', 'guler ușor întărit'),
   ('căptușeală', 'Căptușeala moale din material textil'), ('călcâi', 'Călcâiul întărit')],
  {'Model': 'Geox CIUFCIUF', 'Material': 'piele întoarsă și textil, talpă din spumă', 'Caracteristici': 'Geox Respira™, arici cu elastic, profil scurt', 'Cod produs': 'B455RB.0FU22'})
print('lot 15 scris')
