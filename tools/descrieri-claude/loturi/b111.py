import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
REIMA = A('/brand/reima/', 'Reima')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
GU = '/categorie/unisex-imbracaminte-geci-jachete/'

w(8901,
  f'<p>Geaca {TH} KB0KB09957 maro este o {A(GB, "geacă reversibilă pentru băieți")}: modelul are două fețe, deci se poate purta pe oricare parte. E subțire, din material neted, cu umplutură sintetică și căptușeală completă.</p>'
  '<p>Tăietura e simplă, fără glugă, iar fermoarul o face ușor de pus și de scos. Buzunarele exterioare sunt oblice, iar mânecile se termină cu manșetă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 se potrivesc orientativ copiilor de 8-16 ani.</p>',
  [('cod', 'KB0KB09957'), ('culoare', 'culoarea maro'), ('două fețe', 'Model cu doua fete'), ('subțire', 'Model subțire confecționat din material neted'),
   ('umplutură', 'sintetică'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('tăiere', 'Tăiere simplă, fără blocare'), ('glugă', 'fără glugă'),
   ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'), ('buzunare', 'Buzunare oblice exterioare'), ('manșetă', 'Finisaj din manseta'),
   ('material', '100% Poliester'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB09957', 'Material': '100% poliester', 'Caracteristici': 'două fețe, subțire, fermoar', 'Cod produs': 'KB0KB09957'})

w(8940,
  f'<p>Cizmele de cauciuc {TH} T3XC.34145 negre sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} din masă plastică mată, netedă, cu talpă flexibilă din cauciuc, durabilă și rezistentă la deteriorare. Sunt rezistente la apă, iar fața nu se înmoaie ușor.</p>'
  '<p>Vârful e rotund, ușor întărit, iar contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece. Sus, circumferința se reglează cu șnur cu opritor, iar interiorul textil e confortabil și se păstrează ușor curat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Lungime branț', '22 cm la numărul 30.'), ('Profil', 'înalt.'))
  + '<p>Numerele 30-34 sunt pentru copii de aproximativ 6-11 ani.</p>',
  [('cod', 'T3XC.34145'), ('culoare', 'culoarea negru'), ('plastic', 'Model confecționat din masă plastică mat, neted'),
   ('talpă', 'talpă flexibilă din cauciuc, care este durabilă și rezistentă la deteriorare'), ('apă', 'Rezistența la apă înseamnă o protecție sporită'),
   ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'), ('vârf', 'Cutie rotunda, usor intarita'),
   ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece în timpul mișcării'), ('șnur', 'Reglarea circumferinței superioare cu șnururi cu opritoare'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('gambă', 'Material sintetic, Material textil'),
   ('branț', 'Lungimea brantului pentru marimea este de: 22 cm'), ('mărime', 'Dimensiunile date pentru marimea: 30'), ('profil', 'înalt')],
  {'Model': 'Tommy Hilfiger T3XC.34145', 'Material': 'masă plastică, talpă din cauciuc', 'Caracteristici': 'rezistente la apă, șnur de reglare, interior textil', 'Cod produs': 'T3XC.34145'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(8945,
  f'<p>Geaca de schi {A("/brand/lego/", "LEGO")} LWJAZ 808 roz este o {A(GU, "geacă unisex")} izolată, pentru sporturi de iarnă, cu umplutură sintetică medie spre groasă. Exteriorul are BIONIC-FINISH ECO, e rezistent la vânt și apă, iar materialul e respirabil, cu 4000 g/m2/24h.</p>'
  '<p>Gulerul ridicat și gluga detașabilă apără de frig. Pe mânecă are buzunar cu fermoar pentru skipass, la manșete găuri pentru degetul mare, iar reflectorizantele 3M Scotchlite și fermoarele YKK completează geaca.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două laterale cu fermoar, unul pe mânecă.'), ('Coloană de apă', '10000 mm.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 98-164 sunt pentru copii de cam 3-14 ani.</p>',
  [('cod', 'LWJAZ 808'), ('culoare', 'culoarea roz'), ('izolat', 'Model izolat'), ('iarnă', 'Sporturi de iarnă'), ('groasă', 'medie, groasă'), ('BIONIC', 'BIONIC-FINISH® ECO'),
   ('vânt', 'Materialul exterior este rezistent la vânt și apă'), ('respirabil', 'Respirabilitate: 4000 g/m2/24h'), ('guler', 'Gulerul ridicat și gluga detașabilă'),
   ('skipass', 'Buzunar funcțional pentru permis de schi, cu fermoar, pe mânecă'), ('degetul', 'Găurile pentru degetul mare din partea de jos a mânecilor'),
   ('3M', '3M ™ Scotchlite'), ('YKK', 'Fermoarele YKK®'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('coloană', 'Impermeabilitate: 10000 mm'),
   ('material', '100% Poliester')],
  {'Model': 'LEGO LWJAZ 808', 'Material': '100% poliester', 'Caracteristici': 'BIONIC-FINISH ECO, 10000 mm, buzunar skipass', 'Cod produs': '11010967'})

w(8998,
  f'<p>Adidașii {A("/brand/biomecanics/", "Biomecanics")} 262271 roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} ușori și confortabili, pentru purtat zilnic, creați împreună cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia. Se închid cu velcro și au deschidere largă, deci se încalță ușor.</p>'
  '<p>Inserția Plantilla are perforații care lasă aerul să circule și păstrează piciorul uscat. Vârful e rotund, întărit, contrafortul rigidizat sprijină glezna și călcâiul, iar bucla de la spate ajută la pus și la scos.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Talpă', 'gumă, profilată.'), ('Lungime branț', '18 cm la numărul 28.'), ('Profil', 'scurt.'))
  + '<p>Numerele 24-34 se potrivesc orientativ copiilor de 2-11 ani.</p>',
  [('cod', '262271'), ('culoare', 'culoarea roz'), ('ușor', 'Model ușor și confortabil, ideal pentru purtarea zilnică'),
   ('pediatri', 'create in cooperare cu medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'), ('velcro', 'Închiderea cu velcro facilitează încălțarea'),
   ('deschidere', 'Deschidere larga pentru incaltarea usoara'), ('Plantilla', 'Inserția Plantilla cu perforații asigură o circulație adecvată a aerului, uscăciune și confort'),
   ('vârf', 'Cutie rotunda, intarita'), ('contrafort', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('talpă', 'Talpa: Guma'), ('profilată', 'profilată'),
   ('branț', 'Lungimea brantului pentru marimea este de: 18 cm'), ('mărime', 'Dimensiunile date pentru marimea: 28'), ('profil', 'scurt')],
  {'Model': 'Biomecanics 262271', 'Talpă': 'gumă', 'Caracteristici': 'velcro, inserție perforată, vârf întărit', 'Cod produs': '262271'},
  notes=['Compoziția spune piele naturală, iar descrierea și atributele spun material sintetic și textil; nu am scris materialul feței.'])

w(9012,
  f'<p>Geaca {A("/brand/elisabetta-franchi/", "Elisabetta Franchi")} EFGB131 neagră este o {A(GF, "geacă de iarnă pentru fete")} izolată, din material neted, cu izolație sintetică medie spre groasă pentru temperaturi mai scăzute. Căptușeala e completă, din poliamidă.</p>'
  '<p>Croiala e simplă, fără glugă, cu închidere cu fermoar. Mânecile și marginea de jos sunt finisate cu bătături, iar cele două buzunare laterale au fermoar. Mărimile sunt italienești, raportate la cele europene.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliester.'), ('Material 2', '98% poliester, 2% elastan.'), ('Lungime', '48 cm la mărimea 152.'))
  + '<p>Mărimile 140-158 sunt pentru copii de aproximativ 10-13 ani.</p>',
  [('cod', 'EFGB131'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat confecționat din material neted'),
   ('izolație', 'Un model cu izolație sintetică care va oferi un confort suplimentar la temperaturi mai scăzute'), ('groasă', 'medie, groasă'), ('poliamidă', '100% Poliamida'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('glugă', 'fără glugă'), ('fermoar', 'Incheiere cu fermoar'), ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian, raportate la dimensiunile europene standard'),
   ('material1', '100% Poliester'), ('material2', '98% Poliester , 2% Elastan'), ('lungime', 'Lungimea: 48 cm'), ('mărime', '152 cm')],
  {'Model': 'Elisabetta Franchi EFGB131', 'Material': 'poliester, căptușeală din poliamidă', 'Caracteristici': 'izolată, buzunare cu fermoar, bătături', 'Cod produs': 'EFGB131.C.NY297'})

w(9050,
  f'<p>Pantofii {REIMA} Hyppii albaștri sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} cu profil înalt și talpă din gumă canelată, care prinde bine solul. Fața e din Vegan PU și textil, cu acoperire PFC Repellent fără compuși perfluorurați, rezistentă la apă.</p>'
  '<p>Partea de sus ridicată sprijină glezna pe teren denivelat, contrafortul rigid ține călcâiul, iar vârful e rotund, ușor întărit. Se închid cu velcro, au buclă la spate și elemente reflectorizante.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Izolație', 'nu au.'))
  + '<p>Numerele 22-31 sunt pentru copii de aproximativ 1-7 ani.</p>',
  [('model', 'Hyppii'), ('culoare', 'albastru'), ('profil', 'înalt'), ('talpă', 'Talpa din guma'), ('canelată', 'Modelul cu talpa exterioara canelata asigura o aderenta ridicata la sol'),
   ('Vegan PU', 'Vegan PU este o alternativă ecologică la PVC'), ('PFC', 'Modelul cu acoperire ecologica PFC Repellent cu apa libera, care asigura rezistenta la apa'),
   ('glezna', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('neuniforme', 'atunci când se deplasează pe suprafețe neuniforme'), ('călcâi', 'Contorul de călcâi rigid'),
   ('vârf', 'Cutie rotunda, usor intarita'), ('velcro', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea'),
   ('gambă', 'Material sintetic, Material textil'), ('interior', 'Material textil'), ('neizolat', 'Izolare: neizolat')],
  {'Model': 'Reima Hyppii', 'Material': 'Vegan PU, textil', 'Caracteristici': 'PFC Repellent, velcro, profil înalt', 'Cod produs': '5400144A'},
  notes=['Titlul site-ului are „Hyppii” în locul culorii; culoarea e cea de la magazin (albastru).',
         'Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(9063,
  f'<p>Bluza {TH} KG0KG08558 albă este un hanorac cu glugă, printre {A("/categorie/bluze-tricouri-hanorace/", "bluzele pentru fete")}, din tricot cu imprimeu, cu sigle brodate. Compoziția are bumbac și poliester.</p>'
  '<p>Tăietura e simplă, iar mânecile și marginea de jos se termină cu elastic confortabil. Gluga e integrată în decolteu, iar croiala e regular fit, ușor de purtat zi de zi.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '68% bumbac, 32% poliester.'), ('Glugă', 'integrată.'), ('Detalii', 'imprimeu, sigle brodate.'))
  + '<p>Mărimile 128-176 se potrivesc orientativ copiilor de 8-16 ani.</p>',
  [('cod', 'KG0KG08558'), ('culoare', 'culoarea alb'), ('tricot', 'Model confectionat din tricot cu imprimeu'), ('glugă', 'Bluza pentru copii cu gluga'),
   ('sigle', 'Sigle brodate'), ('tăiere', 'Tăiere simplă, fără blocare'), ('mâneci', 'Mâneci și marginea inferioară finisate cu o coadă elastică confortabilă'),
   ('decolteu', 'Decolteu: integrat cu glugă'), ('croială', 'Croială: regular fit'), ('material', '68% Bumbac, 32% Poliester'), ('integrată', 'integrată')],
  {'Model': 'Tommy Hilfiger KG0KG08558', 'Material': '68% bumbac, 32% poliester', 'Caracteristici': 'glugă, imprimeu, sigle brodate', 'Cod produs': 'KG0KG08558'})

w(9146,
  f'<p>Geaca {A("/brand/adidas-performance/", "adidas Performance")} AJAX JN0245 neagră este o {A(GU, "geacă unisex")} de tranziție, neizolată, din material textil cu imprimeu, cu glugă și căptușeală din plasă. Poliesterul o face rezistentă la îndoire.</p>'
  '<p>Fasonul e drept, se închide cu fermoar, iar mânecile se termină cu elastic. Cele două buzunare laterale au fermoar, ca lucrurile mici să nu cadă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliester.'), ('Material 2', '100% poliuretan termoplastic.'), ('Lungime', '60 cm la mărimea 152.'))
  + '<p>Mărimile 116-164 sunt pentru copii de cam 6-14 ani.</p>',
  [('model', 'AJAX'), ('cod', 'JN0245'), ('culoare', 'culoarea negru'), ('neizolat', 'Model neizolat confecționat din material textil cu imprimeu'),
   ('glugă', 'Model cu gluga'), ('plasă', 'Model captusit cu plasa'), ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'), ('fason', 'Fason drept'),
   ('fermoar', 'Incheiere cu fermoar'), ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('material1', '100% Poliester'), ('material2', '100% Poliuretan termoplastic'), ('lungime', 'Lungimea: 60 cm'), ('mărime', '152 cm')],
  {'Model': 'adidas Performance AJAX', 'Material': 'poliester, poliuretan termoplastic', 'Caracteristici': 'glugă, căptușeală din plasă, buzunare cu fermoar', 'Cod produs': 'JN0245'},
  notes=['Modelul e legat de clubul Ajax doar după numele din titlu; magazinul nu spune mai mult.'])

w(9185,
  f'<p>Geaca {A("/brand/marc-jacobs/", "Marc Jacobs")} W60800 neagră este o {A(GB, "geacă de tranziție pentru băieți")} neizolată, din țesătură cu aplicații, cu glugă integrată și căptușeală completă. Poliesterul o face mai rezistentă la îndoire.</p>'
  '<p>Tăietura e lejeră, se închide cu fermoar, iar buzunarele exterioare sunt oblice. Magazinul precizează că nu este impermeabilă, deci e mai degrabă pentru zilele uscate de primăvară sau toamnă, fără ploaie.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'nu are.'), ('Croială', 'lejeră.'))
  + '<p>Mărimile 114-150 se potrivesc orientativ copiilor de 6-12 ani.</p>',
  [('cod', 'W60800'), ('culoare', 'culoarea negru'), ('neizolat', 'Model neizolat confecționat din țesătură cu aplicații'), ('glugă', 'integrată'),
   ('căptușeală', 'Model neizolat cu captuseala'), ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'), ('lejeră', 'Tăiere lejeră, fără blocare'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare oblice exterioare'), ('impermeabil', 'fără impermeabilitate'), ('material', '100% Poliester'),
   ('umplutură', 'fără umplutură'), ('croială', 'Croială: lejeră')],
  {'Model': 'Marc Jacobs W60800', 'Material': '100% poliester', 'Caracteristici': 'neizolată, glugă, aplicații', 'Cod produs': 'W60800'})

w(9218,
  f'<p>Geaca {REIMA} Sydvest roz este o {A(GF, "geacă de iarnă pentru fete")} cu membrană ReimaTec, care apără de ploaie și vânt și rămâne respirabilă. Cusăturile principale sunt sigilate cu bandă, iar izolația e groasă.</p>'
  '<p>Căptușeala se poate purta și separat. Gulerul ridicat și gluga detașabilă apără de frig, iar fermoarul pe toată lungimea are clapă interioară și exterioară. Tăietura e simplă, fără blocare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliester cu strat de poliuretan.'), ('Umplutură', '100% poliester.'), ('Glugă', 'detașabilă.'))
  + '<p>Mărimile 92-140 sunt pentru copii de aproximativ 2-10 ani.</p>',
  [('model', 'Sydvest'), ('culoare', 'culoarea roz'), ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului, asigurând în același timp o respirabilitate ridicată'),
   ('cusături', 'Cusăturile principale cu bandă etanșează'), ('groasă', 'groasă'), ('membrană', 'membrană impermeabilă'),
   ('căptușeală', 'Model cu captuseala care poate fi purtata separat'), ('guler', 'Gulerul ridicat și gluga detașabilă'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea, cu clapă interioară și exterioară'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('material', '100% Poliester cu strat de poliuretan'), ('umplutură', '100% Poliester'), ('detașabilă', 'detașabilă')],
  {'Model': 'Reima Sydvest', 'Material': 'poliester cu strat de poliuretan', 'Caracteristici': 'ReimaTec, cusături sigilate, căptușeală detașabilă', 'Cod produs': '5100158A'},
  notes=['Descrierea scurtă spune „ușor izolat”, caracteristicile „izolație groasă”; am urmat caracteristicile.'])
