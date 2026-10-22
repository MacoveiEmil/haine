import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9884,
  f'<p>{GEOX} GISLI B461NA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, în stil casual, cu profil înalt și guler întărit în jurul gleznei. Partea de sus e din imitație de piele și material textil, iar membrana Geox Respira™ scoate umezeala din pantof.</p>'
  '<p>Aricii cu șireturi elastice se închid repede, fără nod. Branțul textil cu imprimeu se scoate, iar pe el se verifică ușor dacă piciorul a crescut.</p>'
  '<p>Pentru primii ani de mers, pantoful are:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'textil și sintetic.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-23 sunt pentru copii mici, de cam 1-3 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii verzi B461NA.054FU'), ('casual', 'stilul casual'), ('profil', 'Profilul înalt al părții superioare cu guler întărit'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia GEOX Respira™ cu membrană'), ('umezeală', 'eliminând umezeala la exterior'),
   ('arici', 'Închiderea cu arici cu șireturi elastice'), ('branț', 'Branțul detașabil din material textil cu imprimeu facilitează controlul mărimii piciorului'),
   ('călcâi', 'Călcâiul întărit'), ('interior', 'Material textil, Material sintetic'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici cu șireturi elastice, branț detașabil, Geox Respira™', 'Cod produs': 'B461NA.054FU'})

w(9886,
  f'<p>{GEOX} FADINLIGHT J46M4C sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil scurt, din material textil și sintetic, cu detalii decorative și lumini încorporate pe care copilul le pornește dintr-un buton. Pe drumul de seară, luminile îl fac ușor de văzut.</p>'
  '<p>Șireturile elastice cu cârlig și bucla de la spate permit încălțatul fără legat. Gulerul și spatele călcâiului sunt ușor rigidizate și țin piciorul în pantof.</p>'
  '<p>Talpa și căptușeala:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Vârf', 'cutie rotundă, ușor întărită.'), ('Căptușeală', 'textilă.'))
  + '<p>Mărimile 24-31 sunt, aproximativ, pentru 2-7 ani.</p>',
  [('model', 'Geox Sneakers pentru copii FADINLIGHT culoarea roz, J46M4C.0EE54'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatia materialului textil cu cel sintetic'),
   ('decor', 'Detalii decorative'), ('lumini', 'Model cu lumini incorporate, activate de un buton'),
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('guler', 'Gulerul gambei usor rigidizat'), ('călcâi', 'Spatele calcaiului usor rigidizat'), RESPIRA, ('vârf', 'Cutie rotunda, usor intarita'), ('căptușeală', 'Model cu captuseala textila')],
  {'Model': 'Geox FADINLIGHT', 'Material': 'textil și sintetic, căptușeală textilă', 'Caracteristici': 'lumini cu buton, șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J46M4C.0EE54'})

w(9889,
  f'<p>{A("/brand/columbia/", "Columbia")} Rainy Trails 2154901 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de ploaie pentru băieți")}, bleumarin, subțire și ușoară, cu tehnologia Omni-tech®: membrană microporoasă și cusături sudate acoperite cu strat impermeabil. Căptușeala moale din fleece adaugă puțină căldură, pentru sezonul de tranziție.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile au bandă elastică la capăt, care strânge la încheieturi și ține ploaia afară.</p>'
  '<p>Pentru drumurile pe ploaie și pe întuneric:</p>'
  + L(('Fermoar', 'frontal, cu protecție pentru bărbie și clapă interioară împotriva vântului.'), ('Glugă', 'da.'), ('Elemente reflectorizante', 'copilul se vede după lăsarea serii.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-164 merg la copii de pe la 4 până pe la 14 ani.</p>',
  [('model', 'Columbia Geacă copii Rainy Trails culoarea bleumarin, 2154901'), ('subțire', 'Model subțire confecționat material ușor'), ('Omni-tech', 'Tehnologia Omni-tech®'),
   ('membrană', 'membranei microporoase, respirabile si a cusaturilor sudate acoperite cu un strat impermeabil'), ('fleece', 'Căptușeala moale din fleece'),
   ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă, fără blocare'), ('elastic', 'Mâneci finisate cu o coadă elastică'),
   ('fermoar', 'Fermoar frontal cu barbie și clapă interioară rezistentă la vânt'), ('glugă', 'Gluga: cu gluga'),
   ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'), ('material', '100% Poliester')],
  {'Model': 'Columbia Rainy Trails', 'Material': '100% poliester, căptușeală fleece (72% nailon, 28% poliester)', 'Caracteristici': 'Omni-tech®, cusături sudate, glugă, reflectorizante', 'Cod produs': '2154901'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(9908,
  f'<p>{A("/brand/lego/", "LEGO")} LWJERI 702 este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă de iarnă pentru bebeluși")}, roz, izolată și căptușită, cu confort termic de la -5°C la -20°C. Cusăturile lipite opresc vântul și umezeala, iar impermeabilitatea de 10000 mm o face bună pentru zăpadă și lapoviță.</p>'
  '<p>Croiala e simplă, dreaptă, deci încape un strat gros dedesubt. Gulerul ridicat și gluga detașabilă apără gâtul și capul de frig.</p>'
  '<p>Pentru zilele scurte de iarnă, mai are:</p>'
  + L(('Elemente reflectorizante', 'pentru drumurile pe întuneric.'), ('BIONIC-FINISH® ECO', 'finisaj hidrofob, alternativă la DWR.'), ('Buzunare', 'interioare, oblice, cu închidere.'), ('Respirabilitate', '6000 g/m2/24h.'))
  + '<p>Mărimile 80-104 sunt pentru cei mici de aproximativ 1-4 ani.</p>',
  [('model', 'Lego Geacă copii LWJERI 702 culoarea roz, 11010978'), ('izolat', 'Model izolat cu captuseala'), ('temperatură', 'Oferă confort termic de la -5°C până la -20°C'),
   ('cusături', 'Toate cusăturile sunt lipite'), ('vânt', 'împiedică pătrunderea vântului și a umezelii'), ('impermeabil', 'Impermeabilitate: 10000 mm/m2/24h'),
   ('croială', 'Tăiere simplă, fără blocare'), ('guler, glugă', 'Gulerul ridicat și gluga detașabilă'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('BIONIC', 'BIONIC-FINISH® ECO - o alternativa ecologica la acoperirea traditionala, hidrofoba DWR'), ('buzunare', 'Buzunare interioare oblice, incheiate'),
   ('respirabilitate', 'Respirabilitate: 6000 g/m2/24h')],
  {'Model': 'LEGO LWJERI 702', 'Material': '100% poliester', 'Caracteristici': 'izolată (-5°C până la -20°C), cusături lipite, 10000 mm, glugă detașabilă, reflectorizante', 'Cod produs': '11010978'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(9914,
  f'<p>{GEOX} PUFFYPOP J55MRA sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, cu profil scurt și detalii decorative, cu interior din piele naturală. Branțul detașabil din piele e făcut fără crom, iar talpa are sistemul Geox Respira, în trei straturi perforate.</p>'
  '<p>Șiretul clasic se reglează după piciorul fiecărui copil, mai îngust sau mai plin. Călcâiul întărit are o umplutură moale, care îl ferește de frecare.</p>'
  '<p>Pe scurt:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Branț', 'detașabil, se scoate la uscat.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 28-39 sunt pentru copii de la, în general, 4 ani în sus.</p>',
  [('model', 'Geox Sneakers pentru copii PUFFYPOP culoarea alb, J55MRA.000BC'), ('profil', 'Înălțime: mic de statură'), ('decor', 'Detalii decorative'),
   ('interior', 'Interiorul: Piele naturala'), ('branț', 'Branțul detașabil din piele a fost realizat fără utilizarea cromului'), RESPIRA,
   ('șiret', 'Șiretul clasic permite ajustarea individuală a piciorului'), ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'),
   ('vârf', 'Cutie rotunda, intarita'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox PUFFYPOP', 'Material': 'sintetic, interior din piele naturală, talpă din cauciuc', 'Caracteristici': 'șiret clasic, branț din piele fără crom, Geox Respira', 'Cod produs': 'J55MRA.000BC'})

w(9920,
  f'<p>{GEOX} STEPPIEUP B655WA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} galbeni, cu profil scurt, din material textil și piele naturală, cu detalii decorative. Branțul din piele previne frecarea și mirosul neplăcut, iar căptușeala textilă moale nu irită piciorul.</p>'
  '<p>Velcro-ul se închide și se deschide repede, deci încălțatul durează puțin. Partea de sus e rigidizată și își păstrează forma pe picior.</p>'
  '<p>Talpa și vârful:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Vârf', 'rotund.'), ('Talpă', 'din cauciuc.'))
  + '<p>Mărimile 20-27 sunt pentru copii de aproximativ 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii STEPPIEUP culoarea galben, B655WA.08514'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea naturală'),
   ('decor', 'Detalii decorative'), ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'), ('miros', 'aparitia unui miros neplacut'),
   ('căptușeală', 'Căptușeala moale din material textil previne iritația'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('rigidizat', 'Partea superioară rigidizată'), RESPIRA, ('vârf', 'Varf rotund'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox STEPPIEUP', 'Material': 'textil și piele naturală, branț din piele, talpă din cauciuc', 'Caracteristici': 'velcro, branț din piele, Geox Respira', 'Cod produs': 'B655WA.08514'})

w(9921,
  f'<p>{GEOX} INEK J659CA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, cu profil scurt, din material textil și piele ecologică, cu elemente luminoase care se aprind dintr-un buton de pe partea de sus. Seara, pe drum, copilul se vede mai ușor.</p>'
  '<p>Au șiret care se închide cu velcro, deci pantoful se reglează o dată și apoi se pune repede. Contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece.</p>'
  '<p>Înăuntru și dedesubt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'din cauciuc, rezistentă la uzură.'), ('Vârf', 'rotund.'))
  + '<p>Numerele 28-31 sunt, de obicei, pentru 4-7 ani.</p>',
  [('model', 'Geox Sneakers pentru copii INEK culoarea negru, J659CA.01454'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('lumini', 'Elemente luminoase, activate de un buton pe partea superioară'), ('șiret', 'Model cu siret cu inchidere Velcro'), ('călcâi', 'Contorul de călcâi rigid'),
   ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), RESPIRA,
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Un model cu talpă din cauciuc care este durabilă și rezistentă la deteriorare'), ('vârf', 'Varf rotund')],
  {'Model': 'Geox INEK', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini cu buton, șiret cu velcro, Geox Respira', 'Cod produs': 'J659CA.01454'})

w(9922,
  f'<p>Ghetele de iarnă {GEOX} LAQUINNY J66M3D sunt {A("/categorie/ghete-cizme/", "ghete înalte pentru fete")} (negru pe site, albe la magazin), din imitație de piele și material textil, cu branț din piele naturală. Membrana din talpă scoate umezeala și blochează apa, deci talpa rămâne etanșă pe zăpadă.</p>'
  '<p>Au și șireturi, și fermoar: șiretul se reglează după picior, iar fermoarul ajută la încălțat repede. Vârful rotund lasă degetele să se așeze liber.</p>'
  '<p>Pentru zilele reci, gheata are:</p>'
  + L(('Partea de sus', 'înaltă, ține frigul departe.'), ('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc, perforată (Original Breathing System).'))
  + '<p>Numerele 28-39 se poartă, cu aproximație, de la 4 ani în sus.</p>',
  [('model', 'Geox Încălțăminte de iarnă pentru copii LAQUINNY albă J66M3D.05402'), ('înalt', 'ghete înalte pentru fete'), ('material', 'Partea superioară înaltă din imitație de piele și material textil'),
   ('branț', 'Piele naturală'), ('membrană', 'Membrana în talpă ajută la eliminarea umidității, blocând în același timp pătrunderea apei'),
   ('închidere', 'Închiderea cu șireturi și fermoar'), ('vârf', 'Vârful rotund permite așezarea liberă a degetelor'), ('frig', 'sprijină protecția împotriva frigului'),
   ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpa plată din cauciuc'), ('perforat', 'Sistemul Original Breathing System cu talpă perforată')],
  {'Model': 'Geox LAQUINNY', 'Material': 'imitație de piele și textil, branț din piele naturală, talpă din cauciuc', 'Caracteristici': 'membrană în talpă, șireturi și fermoar', 'Cod produs': 'J66M3D.05402'},
  notes=['Titlul de pe site spune negru; magazinul arată albă.'])

w(9923,
  f'<p>{GEOX} LIGHTYLOO Hello Kitty B6661B sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, cu partea de sus joasă, cu motive Hello Kitty și lumini încorporate. Luminile îi fac pe cei mici mai ușor de văzut, iar membrana Geox Respira™ din talpă scoate umezeala.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, deci copilul învață să se descurce singur, iar călcâiul întărit ține piciorul să nu alunece.</p>'
  '<p>Înăuntru și sub picior:</p>'
  + L(('Interior', 'căptușit cu material textil.'), ('Branț', 'textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 20-27 sunt, de regulă, pentru 1-4 ani.</p>',
  [('model', 'Geox LIGHTYLOO Hello Kitty sneakers pentru copii roz B6661B.05402'), ('jos', 'Partea superioară joasă'), ('Hello Kitty', 'Motivele Hello Kitty'),
   ('lumini', 'Luminile încorporate'), ('vizibilitate', 'ce încurajează joaca copiilor și vizibilitatea'), ('Respira', 'membranei microporoase din talpă, care elimină umezeala'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă'), ('independent', 'utilizarea independentă'),
   ('călcâi', 'Călcâiul întărit'), ('alunecare', 'previne alunecarea'), ('interior', 'Interiorul căptușit cu material textil'), ('branț', 'Branțul din material textil'),
   ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox LIGHTYLOO Hello Kitty', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini încorporate, arici, Geox Respira™', 'Cod produs': 'B6661B.05402'})

w(9925,
  f'<p>Geaca de blugi {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KS0KS00753 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de blugi pentru băieți")}, albastră, din denim de bumbac, cu imprimeu și guler clasic. Nu are căptușeală, deci e ușoară, pentru zilele mai calde din sezonul de tranziție.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar manșetele cu nasturi se strâng pe încheietură, după cât de subțire e brațul copilului.</p>'
  '<p>Ca orice geacă de blugi clasică, are:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'la piept și laterale, tip slit.'), ('Glugă', 'nu are.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 128-176 sunt, în mare, pentru copii de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă de blugi pentru copii albastră KS0KS00753'), ('denim', 'denim de bumbac'), ('imprimeu', 'modelul cu imprimeu'), ('guler', 'Gulerul clasic'),
   ('necăptușit', 'Modelul fără căptușeală este ușor'), ('tranziție', 'zilele mai călduroase de tranziție'), ('croială', 'Croiala regulară'),
   ('lungime', 'Lungimea până la șolduri'), ('manșete', 'Manșetele cu nasturi permit ajustarea individuală la încheietura mâinii'),
   ('nasturi', 'Sistemul de închidere cu nasturi'), ('buzunare', 'Buzunare practice la piept și buzunare laterale tip slit'), ('fără glugă', 'Designul fără glugă'),
   ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KS0KS00753', 'Material': '100% bumbac (denim)', 'Caracteristici': 'necăptușită, nasturi, manșete cu nasturi, imprimeu', 'Cod produs': 'KS0KS00753'})
