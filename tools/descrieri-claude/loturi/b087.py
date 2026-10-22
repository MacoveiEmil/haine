import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
LEVIS = A('/brand/levis/', "Levi's")
LEVN = "Levi's"
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')

w(13130,
  f'<p>Adidașii {TH} T1X9-35253 bleumarin sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt și guler ușor întărit, din imitație de piele și material textil, rezistenți la purtarea zilnică, în stil casual și streetwear. Aricii fac încălțatul și descălțatul rapid.</p>'
  '<p>Călcâiul întărit ține piciorul în poziție corectă, iar talpa plată din cauciuc ține bine pe diverse suprafețe. Căptușeala moale e confortabilă toată ziua.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Branț', 'textil, stabil.'), ('Închidere', 'arici.'))
  + '<p>Numerele 24-29 sunt pentru copii de aproximativ 2-5 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bleumarin T1X9-35253'), ('profil', 'Profilul scurt al părții superioare și gulerul ușor întărit'),
   ('material', 'din imitație de piele și material textil, rezistentă la utilizarea zilnică'), ('stil', 'ținutelor casual și streetwear'), ('arici', 'Sistem de închidere practic, cu arici'),
   ('călcâi', 'Călcâi întărit care stabilizează piciorul, sprijinind poziționarea corectă'), ('talpă', 'Talpă plată din cauciuc asigură stabilitate și aderență pe diverse suprafețe'),
   ('căptușeală', 'Căptușeală moale , din material textil'), ('branț', 'Branț din material textil asigură confortul, oferind un suport stabil')],
  {'Model': 'Tommy Hilfiger T1X9-35253', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, profil scurt', 'Cod produs': 'T1X9-35253'})

w(13132,
  f'<p>Modelul {TH} T1A9-35064 bej vine și în numerele mici, 24-29: {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} scunzi, din imitație de piele, cu închidere cu arici care îi lasă pe copii să se încalțe singuri. Nuanța bej se potrivește cu multe haine.</p>'
  '<p>Glezna rămâne liberă datorită profilului scurt, iar călcâiul întărit ține piciorul în pantof. Talpa din cauciuc are profil plat și ține bine pe sol.</p>'
  '<p>Talpa și căptușeala:</p>'
  + L(('Căptușeală', 'material textil.'), ('Branț', 'textil.'), ('Talpă', 'cauciuc cu profil plat.'))
  + '<p>Se potrivesc copiilor de pe la 2 până pe la 5 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bej T1A9-35064'), ('imitație', 'Partea superioară din imitație de piele'), ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă'),
   ('bej', 'Cromatica bej facilitează asortarea cu multe ținute'), ('profil', 'Profilul scurt al părții superioare permite libertatea de mișcare a gleznei'),
   ('călcâi', 'Călcâi întărit susține stabilitatea piciorului'), ('interior', 'Interior din material textil'), ('branț', 'Branț textil'), ('talpă', 'Talpa din cauciuc cu profil plat favorizează aderența la sol')],
  {'Model': 'Tommy Hilfiger T1A9-35064', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, profil scurt', 'Cod produs': 'T1A9-35064'})

w(13133,
  f'<p>{GEOX} ACTIVART bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu profil jos, din material textil și sintetic, ușori, cu membrana Geox Respira, care scade umezeala din interior. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos.</p>'
  '<p>Bucla de la spate ajută la încălțat, vârful rotund lasă loc degetelor, iar contrafortul rigid ține călcâiul pe loc.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'spumă moale și cauciuc durabil.'), ('Branț', 'textil, se păstrează curat ușor.'), ('Interior', 'sintetic și textil.'))
  + '<p>Numerele 32-35 sunt pentru băieți de cam 8-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ACTIVART culoarea bleumarin, J56LYA.02A9J'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu cel sintetic'),
   ('ușor', 'Model ușor și confortabil'), ('Respira', 'Membrana unica si impermeabila a tehnologiei Geox Respira ajuta la scaderea umezelii excesive'),
   ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('călcâi', 'Contorul de călcâi rigid'), ('spumă', 'Talpa din spumă oferă o senzație mai moale'), TALPA,
   ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'), ('interior', 'Material sintetic, Material textil')],
  {'Model': 'Geox ACTIVART', 'Material': 'textil și sintetic, interior sintetic și textil, talpă din spumă și cauciuc', 'Caracteristici': 'membrană Geox Respira, șireturi elastice cu cârlig', 'Cod produs': 'J56LYA.02A9J'})

w(13141,
  f'<p>Cizmele de zăpadă {A("/brand/biomecanics/", "Biomecanics")} 261257 bleumarin sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} de iarnă înalte, din material textil și sintetic, cu izolație interioară și membrană climatică BioTEX, care ține apa afară și scoate umiditatea.</p>'
  '<p>Talpa din cauciuc, tip platformă, izolează de solul rece și ține bine pe zăpadă. Aricii fac încălțatul rapid, chiar de către copil, iar construcția impermeabilă cu membrană ține picioarele uscate.</p>'
  '<p>Construcția, în trei puncte:</p>'
  + L(('Vârf', 'rigidizat.'), ('Călcâi', 'întărit.'), ('Interior', 'textil, izolat.'))
  + '<p>Numerele 24-34 merg la copii de aproximativ 2-11 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii bleumarin 261257'), ('zăpadă', 'Cizmele de zăpadă Biomecanics 261257 sunt cizme de iarnă înalte'),
   ('material', 'Profilul înalt al carâmbului din material textil și sintetic'), ('izolație', 'Izolația interioară din material textil favorizează menținerea căldurii'),
   ('BioTEX', 'Tehnologia BioTEX , o membrană climatică, favorizează evacuarea umidității și blochează pătrunderea apei din exterior'),
   ('platformă', 'Talpa din cauciuc cu profil de platformă favorizează izolarea de solul rece și oferă aderență'), ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă, favorizând independența'),
   ('vârf', 'Călcâiul întărit și vârful rigidizat'), ('impermeabil', 'Construcția impermeabilă cu membrană susține menținerea picioarelor uscate')],
  {'Model': 'Biomecanics 261257', 'Material': 'textil și sintetic, interior izolat, talpă din cauciuc', 'Caracteristici': 'BioTEX, izolate, arici, talpă platformă', 'Cod produs': '261257'})

w(13143,
  f'<p>Geaca din denim {LEVIS} este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} în culoarea albastru, din bumbac 100%, cu tipar drept, neizolată și fără căptușeală. Se închide cu nasturi și nu are glugă.</p>'
  '<p>Are un buzunar pe piept și buzunare oblice. Magazinul precizează că o parte din produsele {LEVN} vin cu eticheta roșie fără logo („blank tab”), tot originale.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '100% bumbac (denim).'), ('Închidere', 'nasturi.'), ('Croială', 'dreaptă.'))
  + '<p>Mărimile 92-128 se potrivesc băieților de cam 2-8 ani.</p>',
  [('model', "Levi's Geacă din denim pentru copii"), ('culoare', 'Culoare albastru'), ('bumbac', '100% Bumbac'), ('tipar', 'Tipar drept'), ('neizolat', 'Izolare: neizolat'),
   ('necăptușit', 'Captuseala: necaptusit'), ('nasturi', 'Incheiere cu nasturi'), ('glugă', 'Gluga: fara gluga'), ('piept', 'Buzunar pe piept'), ('oblice', 'Buzunare oblice'),
   ('blank tab', 'aproximativ 10% din sortiment este')],
  {'Model': "Levi's (geacă din denim)", 'Material': '100% bumbac (denim)', 'Caracteristici': 'nasturi, buzunar pe piept, neizolată', 'Cod produs': ''})

w(13145,
  f'<p>Hanoracul {TH} KB0KB10509 bleumarin este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")} tip pulover, fără glugă și fără fermoar, din bumbac 100%, cu croială lejeră și umeri coborâți. Logo-ul brodat e discret, iar modelul uni merge la ieșiri în oraș și întâlniri informale.</p>'
  '<p>Decolteul rotund, baza și manșetele au borduri elastice care țin forma.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac, elastic.'), ('Închidere', 'nu are, se trage pe cap.'), ('Decor', 'logo brodat.'))
  + '<p>Mărimile 128-176 sunt pentru băieți de aproximativ 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac bleumarin KB0KB10509'), ('tip pulover', 'Hanorac fără glugă și fără fermoar , un model clasic, tip pulover'),
   ('bumbac', 'Material din bumbac pur'), ('croială', 'Croiala lejeră'), ('umeri', 'Mâneci cu linia umerilor coborâtă'), ('logo', 'Model uni cu logo brodat'),
   ('urban', 'activitățile urbane și întâlnirile informale'), ('decolteu', 'Decolteu rotund cu bordură elastică'), ('borduri', 'Borduri elastice la bază și la manșete ajută la menținerea formei'),
   ('elastic', 'Material elastic'), ('închidere', 'Fără sistem de închidere'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB10509', 'Material': '100% bumbac', 'Caracteristici': 'fără glugă și fermoar, logo brodat, croială lejeră', 'Cod produs': 'KB0KB10509'})

w(13146,
  f'<p>Geaca bomber {A("/brand/donsje/", "Donsje")} 3048501 bej este o {A("/categorie/geci-jachete/", "geacă pentru fete")} ușoară, fără umplutură, cu bumbac, pentru sezonul de tranziție și zilele mai calde. Combină finisajul neted cu matlasajul și are broderie decorativă.</p>'
  '<p>Se închide cu capse pe toată lungimea, iar baza are bandă elastică. Croiala relaxed fit lasă loc de mișcare.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Exterior', '57% bumbac, 43% poliester.'), ('Căptușeală', '100% bumbac.'), ('Mâneci', '100% poliester.'), ('Buzunare', 'laterale, slip-on.'))
  + '<p>Mărimile 74-92 sunt pentru fetițe de aproximativ 9 luni - 2 ani.</p>',
  [('model', 'Donsje Geacă bomber pentru copii, cu bumbac bej 3048501'), ('umplutură', 'Lipsa umpluturii face ca modelul să fie ușor și aerisit'), ('tranziție', 'Ideală pentru sezonul de tranziție'),
   ('bumbac', 'Material cu bumbac'), ('matlasat', 'Combinația de finisaj neted și matlasat'), ('broderie', 'Broderia decorativă'),
   ('capse', 'Sistemul de închidere cu capse pe toată lungimea'), ('bandă', 'Banda elastică de la bază'), ('croială', 'Croiala relaxed fit'),
   ('exterior', '57% Bumbac, 43% Poliester'), ('căptușeală', 'Căptușeala completă din bumbac'), ('mâneci', '100% Poliester'), ('buzunare', 'Buzunarele practice tip slip-on pe laterale')],
  {'Model': 'Donsje 3048501 (bomber)', 'Material': '57% bumbac, 43% poliester, căptușeală din bumbac', 'Caracteristici': 'fără umplutură, capse, broderie', 'Cod produs': '3048501'},
  varsta_txt='9 luni - 2 ani')

w(13150,
  f'<p>Mănușile de schi {A("/brand/reima/", "Reima")} Vanukko negre sunt {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "mănuși unisex")} cu două degete, din material impermeabil și respirabil, tratat cu BIONIC-FINISH ECO. Umplutura PrimaLoft, din fibre reciclate, ține mâinile calde.</p>'
  '<p>Palma are întărituri din PU, iar interiorul e căptușit cu material moale. Mănușile sunt certificate Bluesign și GRS.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Exterior', '100% poliester reciclat.'), ('Întărituri', '60% poliuretan, 40% poliester.'), ('Umplutură', 'PrimaLoft, poliester reciclat.'))
  + '<p>Pe site sunt mărimi între 2-4ani și 12-14 ani, adică pentru copii de aproximativ 2-14 ani. Căptușeala moale mărește protecția împotriva frigului.</p>',
  [('model', 'Reima Mănuși de schi pentru copii Vanukko 5300281A'), ('culoare', 'Culoare negru'), ('degete', 'Model cu design cu 2 degete'),
   ('impermeabil', 'Material impermeabil și respirabil'), ('BIONIC', 'BIONIC-FINISH® ECO - o alternativa ecologica la acoperirea traditionala, hidrofoba DWR'),
   ('PrimaLoft', 'Umplutura PrimaLoft® realizata din fibre reciclate'), ('PU', 'Întăriri suplimentare pe interiorul mâinii din PU'),
   ('căptușeală', 'Interiorul este căptușit cu un material moale'), ('Bluesign', 'Model certificat Bluesign® Standard'), ('GRS', 'GRS (Global Recycle Standard)'),
   ('material', 'Material 1: 100% Poliester reciclat'), ('material 2', 'Material 2: 60% Poliuretan, 40% Poliester')],
  {'Model': 'Reima Vanukko', 'Material': 'poliester reciclat, umplutură PrimaLoft', 'Caracteristici': 'impermeabile, două degete, Bluesign, GRS', 'Cod produs': '5300281A'},
  varsta_txt='2-14 ani', notes=['Mărimile sunt date în ani (2-4 ani … 12-14 ani); vârsta e luată direct din ele.'])

w(13151,
  f'<p>Cizmele de iarnă {GEOX} HIMALAYA ABX sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme pentru băieți")} în culoarea negru pe site (gri la magazin), izolate, din material textil și piele ecologică, cu tehnologia patentată AMPHIBIOX, rezistentă la apă și vânt, dar respirabilă. Se închid cu scai.</p>'
  '<p>Bucla de la spate ajută la încălțat, cutia rotundă e întărită, iar partea de sus rigidizată ține forma.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Căptușeală', 'textilă.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 24-35 se potrivesc băieților de cam 2-11 ani.</p>',
  [('model', 'Geox Cizme de iarnă copii HIMALAYA ABX J46FRE.0FU50'), ('culoare', 'Culoare gri'), ('izolat', 'Model izolat'), ('material', 'combinatia materialului textil cu pielea ecologica'),
   ('AMPHIBIOX', 'Tehnologia patentata AMPHIBIOX asigura impermeabilitate, permeabilitate la aer, respirabilitate si rezistenta la vant'), ('scai', 'Incheiere cu scai'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('vârf', 'Cutie rotunda, intarita'), ('rigid', 'Partea superioară rigidizată'),
   RESPIRA, ('căptușeală', 'Model cu captuseala textila'), TALPA],
  {'Model': 'Geox HIMALAYA ABX', 'Material': 'textil și piele ecologică, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'AMPHIBIOX, Geox Respira, izolate, scai', 'Cod produs': 'J46FRE.0FU50'},
  notes=['Titlul spune negru, magazinul dă culoarea gri; am scris ambele.'])

w(13153,
  f'<p>Cizmele cowboy {A("/brand/primigi/", "Primigi")} PHR 23729 negre sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} din piele, peste gleznă, fără izolație, pentru zilele mai calde ale sezonului de tranziție. Cusăturile fine le dau un aer clasic, iar fermoarul face încălțatul rapid.</p>'
  '<p>Shock Absorber din talpă absoarbe șocurile și reduce presiunea pe articulații. Vârful rigidizat și călcâiul întărit țin piciorul corect.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branțuri', 'textile, detașabile.'), ('Interior', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 31-35 sunt pentru fete de aproximativ 6-11 ani.</p>',
  [('model', 'Primigi Cizme cowboy pentru copii din piele negre PHR 23729'), ('piele', 'Partea superioară, realizată din piele naturală'), ('gleznă', 'Croiala peste gleznă'),
   ('izolație', 'Lipsa izolației interioare face modelul potrivit pentru zilele mai calde din sezonul de tranziție'), ('cusături', 'Cusăturile delicate conferă modelului un caracter clasic'),
   ('fermoar', 'Închiderea cu fermoar facilitează încălțarea și descălțarea rapidă'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă favorizează absorbția șocurilor, contribuind la reducerea presiunii asupra articulațiilor'),
   ('vârf', 'Vârful rigidizat și călcâiul întărit'), ('branț', 'Branțurile detașabile din material textil'), ('interior', 'Interiorul, finisat cu material textil'),
   ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Primigi PHR 23729 (cowboy)', 'Material': 'piele (piele acoperită), interior textil, talpă din cauciuc', 'Caracteristici': 'fermoar, Shock Absorber, fără izolație', 'Cod produs': 'PHR 23729'})
