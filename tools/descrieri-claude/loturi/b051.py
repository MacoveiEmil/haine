import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(11027,
  f'<p>Botinele {GEOX} KIDDARTAH J56NDA sunt {A("/categorie/ghete-cizme/", "ghete din piele întoarsă pentru fete")}, negre, ușor izolate, cu partea de sus ridicată, care rigidizează glezna. Se leagă cu șiret clasic, care se strânge după forma piciorului.</p>'
  '<p>Contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece, iar vârful e o cutie rotundă, întărită.</p>'
  '<p>Dedesubt și înăuntru:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc, rezistentă la uzură.'), ('Branț', 'textil, se ține ușor curat.'), ('Interior', 'material sintetic și textil.'))
  + '<p>Numerele 28-35 sunt pentru copii de 4-11 ani, în mare.</p>',
  [('model', 'Geox Cizme din piele întoarsă pentru copii KIDDARTAH culoarea negru, J56NDA.00022'), ('piele întoarsă', 'Model confectionat din piele intoarsa'),
   ('izolat', 'Izolare: usor izolat'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea piciorului la gleznă'), ('șiret', 'Șiretul clasic permite ajustarea individuală a piciorului'),
   ('călcâi', 'Contorul de călcâi rigid'), ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('vârf', 'Cutie rotunda, intarita'),
   ('talpă', 'talpă flexibilă din cauciuc, care este durabilă și rezistentă la deteriorare'), ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'),
   ('interior', 'Interiorul: Material sintetic, Material textil')],
  {'Model': 'Geox KIDDARTAH', 'Material': 'piele întoarsă, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'ușor izolate, șiret clasic, gleznă rigidizată', 'Cod produs': 'J56NDA.00022'})

w(11043,
  f'<p>{A("/brand/liewood/", "Liewood")} Jesse Thermo Rainboot LW13042 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de ploaie unisex")} (multicolor pe site, albe la magazin), impermeabile și căptușite termic, pentru zilele reci și ploioase de toamnă și iarnă. Profilul înalt trece de gleznă și ține apa și noroiul afară.</p>'
  '<p>Sunt de tip slip-on, deci copilul le trage singur pe picior, fără închideri. Călcâiul și gulerul întărit țin piciorul în cizmă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Partea de sus', 'sintetică, se curăță ușor.'), ('Căptușeală și branț', 'textile.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 22-35 sunt pentru copii de 1-11 ani, aproximativ.</p>',
  [('model', 'Liewood Cizme Wellington pentru copii Jesse Thermo Rainboot albe LW13042'), ('impermeabil', 'Materialul exterior impermeabil'), ('termic', 'Interiorul căptușit termic'),
   ('ploaie', 'zilele reci și ploioase'), ('sezon', 'aventurile de toamnă și iarnă'), ('profil', 'Profilul înalt al cizmelor de ploaie contribuie la protecția împotriva apei și noroiului, ajungând deasupra gleznei'),
   ('slip-on', 'Construcția slip-on permite încălțarea rapidă și autonomă de către copii'), ('călcâi', 'Călcâiul întărit'), ('guler', 'Gulerul superior întărit'),
   ('sintetic', 'Partea superioară sintetică facilitează curățarea'), ('căptușeală', 'Căptușeala și branțul textil'), ('talpă', 'Talpa din cauciuc')],
  {'Model': 'Liewood Jesse Thermo Rainboot', 'Material': 'sintetic, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'impermeabile, căptușite termic, slip-on', 'Cod produs': 'LW13042'},
  notes=['Titlul de pe site spune multicolor; magazinul le arată albe.'])

w(11054,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261125 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete de iarnă pentru bebeluși")}, bleumarin, înalte, din piele naturală, cu căptușeală și branț din lână, care țin căldura în zilele reci. Sunt pentru plimbările de iarnă.</p>'
  '<p>Aricii cu curea reglabilă permit încălțatul ușor și strâng gheata exact pe picior. Stabilizatorul lateral și călcâiul moale țin piciorul în poziție.</p>'
  '<p>Pe scurt:</p>'
  + L(('Vârf', 'rotund, cauciucat, apără de lovituri.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Parteneriat', 'Biomecanics Podology.'))
  + '<p>Numerele 18-25 sunt pentru cei mici de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii din piele bleumarin 261125'), ('înalt', 'încălțăminte înaltă'), ('piele', 'Partea superioară din piele naturală'),
   ('lână', 'Căptușeala interioară și branțul din lână ajută la menținerea căldurii în zilele reci'), ('plimbări', 'plimbările de iarnă'),
   ('arici', 'Sistemul de închidere cu arici cu o curea reglabilă'), ('stabilizator', 'Stabilizatorul lateral și călcâiul moale'),
   ('vârf', 'Vârful rotund, cauciucat asigură protecția degetelor împotriva loviturilor'), ('talpă', 'Talpa flexibilă din cauciuc'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261125', 'Material': 'piele naturală, căptușeală din lână, talpă din cauciuc', 'Caracteristici': 'arici cu curea, vârf cauciucat, lână', 'Cod produs': '261125'})

w(11058,
  f'<p>Ghetele de iarnă {A("/brand/primigi/", "Primigi")} PRK 23909 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} galbene, înalte, din piele nubuc, care cuprind glezna. Sunt făcute după sistemul Primigi × SIPeP, dezvoltat cu podologi, pentru zilele mai reci.</p>'
  '<p>Închiderea e dublă, cu fermoar și șireturi: șiretul se reglează după picior, iar fermoarul ajută la încălțat. Vârful rotund lasă degetele libere.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Shock Absorber', 'limitează transferul șocurilor la mers.'), ('Vârf și călcâi', 'rigidizat, respectiv întărit.'))
  + '<p>Numerele 27-35 sunt pentru copii de în jur de 3-11 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii din nubuck galbenă PRK 23909'), ('nubuc', 'Partea superioară înaltă din piele nubuc'), ('gleznă', 'asigură susținerea gleznei'),
   ('SIPeP', 'Sistemul Primigi × SIPeP , dezvoltat în colaborare cu podologi'), ('reci', 'zilele mai reci'), ('închidere', 'Închidere dublă cu fermoar și șireturi'),
   ('vârf', 'Vârf rotund oferă libertate de mișcare degetelor'), ('talpă', 'Talpă plată din cauciuc'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă'),
   ('șocuri', 'limitând transferul șocurilor la mers'), ('întărit', 'Vârf rigidizat și călcâi întărit')],
  {'Model': 'Primigi PRK 23909', 'Material': 'piele nubuc, interior textil, talpă din cauciuc', 'Caracteristici': 'fermoar și șireturi, Shock Absorber, Primigi × SIPeP', 'Cod produs': 'PRK 23909'})

w(11066,
  f'<p>{GEOX} WASHIBA FAST IN J65NRA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albi, ușori, cu profil scurt, cu aspect de piele întoarsă, pentru purtat zilnic. Talpa are sistemul Geox Respira, în trei straturi cu perforări.</p>'
  '<p>Talpa exterioară din cauciuc are caneluri, deci prinde bine pe asfalt, iar vârful e rotund, cu loc pentru degete.</p>'
  '<p>Pe scurt:</p>'
  + L(('Partea de sus', 'material sintetic.'), ('Interior', 'material textil.'), ('Talpă', 'din cauciuc, cu caneluri.'))
  + '<p>Numerele 28-39 sunt pentru copii de la 4 ani în sus, în general.</p>',
  [('model', 'Geox Sneakers pentru copii WASHIBA FAST IN culoarea alb, J65NRA.05415'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('piele întoarsă', 'confecționat din piele întoarsă'), ('zilnic', 'purtarea zilnică'), RESPIRA, ('caneluri', 'Talpa exterioară din cauciuc cu caneluri este durabilă și oferă o tracțiune bună'),
   ('vârf', 'Varf rotund'), ('parte de sus', 'Gamba: Material sintetic'), ('interior', 'Interiorul: Material textil')],
  {'Model': 'Geox WASHIBA FAST IN', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'talpă cu caneluri, Geox Respira', 'Cod produs': 'J65NRA.05415'})

w(11075,
  f'<p>{A("/brand/colmar/", "Colmar")} REPUNK 3487A.8V este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de puf pentru băieți")}, galbenă, matlasată, din material neted de poliamidă, cu umplutură ușoară de puf și pene (90/10). Gulerul ridicat și gluga fixă apără gâtul și capul de frig.</p>'
  '<p>Croiala e simplă, dreaptă, deci se poartă comod peste un hanorac. Puful light o face ușoară, potrivită pentru zilele reci.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 154-172 sunt pentru adolescenți de 12-15 ani, aproximativ.</p>',
  [('model', 'Colmar Geaca de puf pentru copii REPUNK culoarea galben, 3487A.8V'), ('matlasat', 'Matlasare'), ('neted', 'material neted'), ('puf', '90% Puf, 10% Pene'),
   ('light', 'Izolare: puf light'), ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('croială', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('material', '100% Poliamida')],
  {'Model': 'Colmar REPUNK', 'Material': '100% poliamidă; umplutură 90% puf, 10% pene', 'Caracteristici': 'puf light, glugă fixă, matlasată', 'Cod produs': '3487A.8V'})

w(11081,
  f'<p>{GEOX} BIGLIA B044CC sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} roz, ușori, din piele, cu interior din piele, pentru purtat zilnic. Membrana impermeabilă Geox Respira scade umezeala din pantof și ține apa afară, iar talpa preia șocurile.</p>'
  '<p>Velcro-ul se închide repede și strânge pantoful pe picior, iar branțul Light Flexy lasă piciorul să se miște. Vârful e rotund.</p>'
  '<p>Pe scurt:</p>'
  + L(('Branț', 'din piele, previne frecarea și mirosul.'), ('Partea de sus', 'piele.'), ('Talpă', 'material sintetic.'))
  + '<p>Numerele 18-26 sunt pentru copii de 1-4 ani, de regulă.</p>',
  [('model', 'Geox Încălțăminte din piele pentru copii BIGLIA culoarea roz, B044CC.007BC'), ('piele', 'confecționat din piele naturală'), ('ușor', 'Model ușor'), ('zilnic', 'purtarea zilnică'),
   ('interior', 'Interiorul: Piele'), ('membrană', 'Membrana unica si impermeabila a tehnologiei Geox Respira ajuta la scaderea umezelii excesive si asigura impermeabilitatea'),
   ('șocuri', 'Tehnologie moale pentru amortizare perfecta a socurilor'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('Light Flexy', 'Light Flexy Sistem de brant pentru libertatea de miscare'), ('vârf', 'Varf rotund'),
   ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'), ('talpă', 'Material sintetic')],
  {'Model': 'Geox BIGLIA', 'Material': 'piele, interior din piele, talpă sintetică', 'Caracteristici': 'velcro, membrană impermeabilă Geox Respira, Light Flexy', 'Cod produs': 'B044CC.007BC'})

w(11083,
  f'<p>Puloverul {TH} KB0KB10307 este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "pulover pentru băieți")} albastru, clasic, din bumbac 100% elastic, care se îmbracă peste cap. E simplu, fără buzunare, iar mâneca lungă ține de cald în zilele mai răcoroase.</p>'
  '<p>Croiala e regulară, nici strâmtă, nici largă, iar bordurile elastice de la decolteu, manșete și bază strâng ușor și țin puloverul în formă după spălare și purtare.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'rotund.'), ('Buzunare', 'nu are.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, aproximativ.</p>',
  [('model', 'Tommy Hilfiger Pulover pentru copii din bumbac albastru KB0KB10307'), ('peste cap', 'Puloverul clasic, ce se îmbracă peste cap'), ('bumbac', 'Confecționat din bumbac 100%'),
   ('elastic', 'Materialul elastic'), ('fără buzunare', 'Model fără buzunare'), ('mânecă', 'Mâneca lungă, clasică asigură protecție împotriva frigului în zilele mai răcoroase'),
   ('croială', 'Croiala regulară'), ('borduri', 'Bordurile elastice de la decolteu, manșete și bază'), ('decolteu', 'Decolteul rotund')],
  {'Model': 'Tommy Hilfiger KB0KB10307', 'Material': '100% bumbac', 'Caracteristici': 'pulover clasic, decolteu rotund, borduri elastice', 'Cod produs': 'KB0KB10307'})

w(11084,
  f'<p>Cămașa {TH} KG0KG09391 este o {A("/categorie/bluze-tricouri-hanorace/", "cămașă cu dungi pentru fete")}, albastră, din bumbac pur, cu mânecă lungă, în stil casual, pentru zilele obișnuite și ieșirile cu prietenii. La piept are un buzunar.</p>'
  '<p>Croiala e relaxată, cu umerii coborâți pe mânecă, deci cămașa stă lejer, nu strânge la umeri și se poartă ușor și deschisă, peste un tricou.</p>'
  '<p>Pe scurt, despre cămașă:</p>'
  + L(('Material', '100% bumbac.'), ('Model', 'cu dungi.'), ('Buzunar', 'la piept.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, în general.</p>',
  [('model', 'Tommy Hilfiger Cămașă pentru copii din bumbac albastră cu dungi KG0KG09391'), ('prieteni', 'întâlnirile cu prietenii'), ('bumbac', 'Confecționată din bumbac pur'), ('casual', 'Stilul casual'),
   ('croială', 'Croiala relaxată'), ('mânecă', 'Mâneca lungă cu linia umerilor coborâtă'), ('dungi', 'Modelul cu dungi'), ('buzunar', 'Buzunarul la piept')],
  {'Model': 'Tommy Hilfiger KG0KG09391', 'Material': '100% bumbac', 'Caracteristici': 'dungi, croială relaxată, buzunar la piept', 'Cod produs': 'KG0KG09391'},
  notes=['„Peste un tricou” e dedus din croiala relaxată.'])

w(11093,
  f'<p>Cămașa {TH} 8720637748299 este o {A("/categorie/bluze-tricouri-hanorace/", "cămașă din bumbac pentru fete")}, albă, cu model, din bumbac organic 100%, cu guler stand-up și mânecă lungă. Merge și la ținute casual, și la ocazii elegante.</p>'
  '<p>Fasonul e regular, nici mulat, nici larg, iar manșetele cu nasturi se încheie pe încheietură, deci mânecile nu atârnă la un braț mai subțire. Se închide cu nasturi în față.</p>'
  '<p>Pe scurt:</p>'
  + L(('Guler', 'stand-up.'), ('Material', '100% bumbac organic.'), ('Manșete', 'cu nasturi.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, cu aproximație.</p>',
  [('model', 'Tommy Hilfiger Camasa de bumbac pentru copii culoarea alb, 8720637748299'), ('model imprimat', 'Model: cu modele'), ('organic', '100% Bumbac organic'),
   ('guler', 'Model cu un guler stand-up'), ('mânecă', 'Maneca lunga'), ('ocazie', 'Ocazie: elegant'), ('casual', 'Ocazie: casual'), ('fason', 'Fason regular'),
   ('manșete', 'Manșete cu nasturi'), ('nasturi', 'Închiderea convenabilă cu buton')],
  {'Model': 'Tommy Hilfiger 8720637748299', 'Material': '100% bumbac organic', 'Caracteristici': 'guler stand-up, mânecă lungă, nasturi', 'Cod produs': '8720637748299'})
