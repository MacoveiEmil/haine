import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
KS = A('/brand/konges-slojd/', 'Konges Sløjd')

w(11170,
  f'<p>Ghetele de iarnă {A("/brand/primigi/", "Primigi")} PTIGT 23549 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} galbene, înalte, din piele naturală și imitație de piele, cu interior izolat termic și membrana GORE-TEX®, care apără de apă și vânt. Sunt pentru aventurile de iarnă și joaca zilnică afară.</p>'
  '<p>Aricii permit încălțatul și descălțatul de către copil, fără ajutor. Vârful și călcâiul întărite, împreună cu gulerul ușor întărit, țin piciorul stabil.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Shock Absorber', 'reduce șocurile la mers.'), ('Branțuri', 'textile, detașabile, se curăță ușor.'))
  + '<p>Numerele 25-29 sunt pentru copii de în jur de 2-5 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii galbenă PTIGT 23549'), ('înalt', 'încălțăminte înaltă pentru copii'),
   ('material', 'Partea superioară din piele naturală și imitație de piele , cu interior izolat termic'), ('GORE-TEX', 'Membrana GORE-TEX® contribuie la menținerea uscăciunii și a căldurii, protejând împotriva apei și a vântului'),
   ('iarnă', 'aventurilor de iarnă și al jocurilor cotidiene'), ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă a încălțămintei de către copii'),
   ('întărit', 'Vârful și călcâiul întărite , împreună cu gulerul ușor întărit'), ('talpă', 'Talpa plată din cauciuc'), ('Shock Absorber', 'Elementul Shock Absorber din talpă ajută la reducerea șocurilor'),
   ('branțuri', 'Branțurile detașabile din material textil permit o curățare ușoară')],
  {'Model': 'Primigi PTIGT 23549', 'Material': 'piele naturală și imitație de piele, interior izolat', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber, branțuri detașabile', 'Cod produs': 'PTIGT 23549'})

w(11181,
  f'<p>{A("/brand/geox/", "Geox")} ECLYPER x Looney Tunes J65LSE sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albi, ușori, cu profil scurt, din material sintetic, cu personaje Looney Tunes, pentru purtat zilnic. Interiorul e textil.</p>'
  '<p>Talpa exterioară din cauciuc are caneluri, deci prinde bine pe asfalt și se uzează greu. Vârful e rotund și lasă loc degetelor.</p>'
  '<p>Pe scurt, din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'material sintetic.'), ('Interior', 'material textil.'), ('Talpă', 'din cauciuc, cu caneluri.'))
  + '<p>Numerele 24-35 sunt pentru copii de 2-11 ani, cu aproximație.</p>',
  [('model', 'Geox Sneakers pentru copii ECLYPER x Looney Tunes culoarea alb, J65LSE.054FU'), ('sintetic', 'confecționat din material sintetic'), ('ușor', 'Model ușor'),
   ('profil', 'Înălțime: mic de statură'), ('zilnic', 'purtarea zilnică'), ('interior', 'Interiorul: Material textil'),
   ('caneluri', 'Talpa exterioară din cauciuc cu caneluri este durabilă și oferă o tracțiune bună'), ('vârf', 'Varf rotund')],
  {'Model': 'Geox ECLYPER x Looney Tunes', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'talpă cu caneluri, vârf rotund', 'Cod produs': 'J65LSE.054FU'})

w(11183,
  f'<p>Cămașa {TH} KB0KB10601 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "cămașă albă pentru băieți")}, simplă, din bumbac moale cu puțin elastan, cu mânecă lungă clasică și logo brodat discret. Stilul e casual-elegant, deci merge și la ocazii, și la purtat obișnuit.</p>'
  '<p>Croiala e regulară, cu aspect clasic, iar elastanul o lasă să se miște ușor la joacă. Gulerul e moale și clasic.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', '97% bumbac, 3% elastan.'), ('Guler', 'moale, clasic.'), ('Logo', 'brodat.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, de regulă.</p>',
  [('model', 'Tommy Hilfiger Cămașă pentru copii cu bumbac albă simplă KB0KB10601'), ('bumbac', 'Confecționată din bumbac moale'), ('material', '97% Bumbac, 3% Elastan'),
   ('mânecă', 'Mânecă lungă clasică'), ('logo', 'Logo brodat al mărcii'), ('stil', 'Un stil casual-elegant versatil'), ('croială', 'Croială regulară'), ('guler', 'Guler moale, clasic')],
  {'Model': 'Tommy Hilfiger KB0KB10601', 'Material': '97% bumbac, 3% elastan', 'Caracteristici': 'mânecă lungă, guler clasic, logo brodat', 'Cod produs': 'KB0KB10601'})

w(11194,
  f'<p>Geaca {TH} KB0KB10451 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, bleumarin, cu izolație sintetică ușoară și căptușeală completă, pentru zilele mai reci și vremea schimbătoare. Gulerul înalt apără gâtul de vânt.</p>'
  '<p>Croiala e regular fit, cu lungimea până la șolduri, iar manșetele și tivul elastic strâng geaca pe corp și opresc aerul rece. Nu are glugă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale, deschise.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 116-122 sunt pentru copii de în jur de 6-7 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă de tranziție pentru copii bleumarin KB0KB10451'), ('izolație', 'Izolație sintetică ușoară'), ('căptușeală', 'Căptușeală completă din material sintetic'),
   ('reci', 'zilele mai reci'), ('guler', 'Guler înalt – protejează gâtul de vânt'), ('croială', 'Croială regular fit'), ('lungime', 'Lungime până la șolduri'),
   ('manșete', 'Manșete elastice'), ('tiv', 'Tiv elastic'), ('fără glugă', 'Fără glugă'), ('fermoar', 'Închidere cu fermoar'), ('buzunare', 'Buzunare laterale deschise'),
   ('material', '100% Poliamidă')],
  {'Model': 'Tommy Hilfiger KB0KB10451', 'Material': '100% poliamidă', 'Caracteristici': 'izolație ușoară, manșete și tiv elastice, guler înalt', 'Cod produs': 'KB0KB10451'})

w(11198,
  f'<p>{KS} EVI THERMO SET KS105198 este un {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "compleu termo unisex")}, verde, uni, ușor izolat, din material neted, cu rezistență sporită la apă datorită finisajului BIONIC-FINISH® ECO. E pentru vreme nefavorabilă, ploaie ușoară și răcoare.</p>'
  '<p>Croiala e simplă, dreaptă, iar talia are bandă elastică, care se strânge pe un copil mai slab. Mânecile se termină cu manșetă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Talie', 'bandă elastică.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 74 până la 134-140 sunt pentru copii de la cam 9 luni la 10 ani.</p>',
  [('model', 'Konges Sløjd Compleu copii EVI THERMO SET culoarea verde, KS105198'), ('uni', 'Model: uni'), ('izolat', 'Model usor cu izolatie'), ('neted', 'material neted'),
   ('apă', 'Un model cu rezistență sporită la apă, ideal pentru condiții meteorologice nefavorabile'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('croială', 'Tăiere simplă, fără blocare'),
   ('talie', 'Banda elastica in talie'), ('manșetă', 'Finisaj din manseta'), ('fermoar', 'Incheiere cu fermoar'), ('material', '100% Bumbac')],
  {'Model': 'Konges Sløjd EVI THERMO SET', 'Material': '100% bumbac', 'Caracteristici': 'compleu termo, ușor izolat, rezistent la apă, talie elastică', 'Cod produs': 'KS105198'},
  notes=['„Ploaie ușoară” e dedus din rezistența sporită la apă.'])

w(11212,
  f'<p>Vesta {KS} JODY TEDDY VEST KS103481 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "vestă din fleece unisex")}, bej, din poliester reciclat certificat GRS, fără căptușeală. Gulerul ridicat apără gâtul de frig, iar fără mâneci lasă brațele libere.</p>'
  '<p>Croiala e simplă, dreaptă, deci se poartă peste un tricou sau un hanorac. Se închide cu fermoar și nu are glugă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', 'fleece, 100% poliester reciclat.'), ('Închidere', 'fermoar.'), ('Guler', 'ridicat.'))
  + '<p>Mărimile 74 până la 134-140 sunt pentru copii de aproximativ 9 luni - 10 ani.</p>',
  [('model', 'Konges Sløjd Vestă copii JODY TEDDY VEST GRS culoarea bej, KS103481'), ('fleece', 'material fleece'), ('reciclat', '100% Poliester reciclat'),
   ('GRS', 'GRS (Global Recycle Standard)'), ('necăptușit', 'Captuseala: necaptusit'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('croială', 'Tăiere simplă, fără blocare'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('fără glugă', 'Gluga: fara gluga')],
  {'Model': 'Konges Sløjd JODY TEDDY VEST', 'Material': '100% poliester reciclat (fleece, GRS)', 'Caracteristici': 'vestă fleece, guler ridicat, fermoar', 'Cod produs': 'KS103481'},
  notes=['„Peste un tricou sau un hanorac” e dedus din faptul că e vestă fără mâneci.'])

w(11220,
  f'<p>{TH} KG0KG08520 este un {A("/categorie/bluze-tricouri-hanorace/", "hanorac cu glugă pentru fete")}, bleumarin, cu imprimeu, din tricot moale de bumbac 100%, cu mânecă lungă și buzunar cangur în față.</p>'
  '<p>Croiala e lejeră, cu umerii coborâți pe mânecă, deci stă larg și vine comod și peste o bluză. Mânecile și tivul au bandă elastică, care strânge la încheieturi și jos.</p>'
  '<p>Pe scurt:</p>'
  + L(('Glugă', 'da.'), ('Buzunar', 'cangur, în față.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, aproximativ.</p>',
  [('model', 'Tommy Hilfiger Hanorac de bumbac pentru copii culoarea bleumarin, cu glugă, cu imprimeu, KG0KG08520'), ('imprimeu', 'Model cu imprimeu'),
   ('tricot', 'tricotaje moi'), ('bumbac', '100% Bumbac'), ('mânecă', 'Maneca lunga'), ('buzunar', 'Un buzunar cangur practic'), ('croială', 'Croială lejeră'),
   ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'), ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('glugă', 'Model cu gluga')],
  {'Model': 'Tommy Hilfiger KG0KG08520', 'Material': '100% bumbac', 'Caracteristici': 'glugă, buzunar cangur, croială lejeră', 'Cod produs': 'KG0KG08520'})

w(11225,
  f'<p>{A("/brand/liewood/", "Liewood")} Runa Jacket LW20841 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de tranziție unisex")}, bleumarin, din fleece moale, cu izolație la mâneci, pentru zilele mai reci și vremea schimbătoare. Fără glugă, se poartă ușor și sub o geacă mai groasă.</p>'
  '<p>Croiala e regulară, cu mâneci raglan și lungimea până la șolduri. Manșetele cu nervuri strâng la încheieturi și țin aerul rece afară.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '100% poliester (fleece).'))
  + '<p>Mărimile 80-140 sunt pentru copii de în jur de 1-10 ani.</p>',
  [('model', 'Liewood Geacă de tranziție pentru copii Runa Jacket bleumarin LW20841'), ('fleece', 'Materialul fleece ajută la menținerea căldurii'), ('izolație', 'Izolația la mâneci'),
   ('reci', 'zilele mai reci'), ('fără glugă', 'Fără glugă contribuie la lejeritatea gecii și facilitează purtarea ei sub alte articole de îmbrăcăminte exterioară'),
   ('croială', 'Croiala regulară'), ('raglan', 'Croiala raglan a mânecilor'), ('lungime', 'Lungimea până la șolduri'), ('manșete', 'Manșetele cu nervuri'),
   ('fermoar', 'Sistemul de închidere cu fermoar'), ('buzunare', 'Buzunare laterale tip slip-on'), ('material', '100% Poliester')],
  {'Model': 'Liewood Runa Jacket', 'Material': '100% poliester (fleece)', 'Caracteristici': 'fleece, mâneci raglan, izolație la mâneci, fermoar', 'Cod produs': 'LW20841'})

w(11237,
  f'<p>Blugii {TH} FLARE KG0KG09419 sunt {A("/categorie/pantaloni-treninguri/", "blugi evazați pentru fete")}, albaștri, din denim elastic de bumbac, în stil casual și vintage. Cracii se lărgesc de la genunchi în jos, pentru un aspect modern.</p>'
  '<p>Talia e normală și stă bine pe șolduri, iar denimul elastic se adaptează la corp, deci se mișcă odată cu copilul.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar și nasture.'), ('Buzunare', 'aplicate și cu închidere.'), ('Material', '99% bumbac, 1% elastan.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, de obicei.</p>',
  [('model', 'Tommy Hilfiger Blugi flared pentru copii FLARE albaștri KG0KG09419'), ('denim', 'Denim elastic'), ('vintage', 'Stil casual și vintage'),
   ('evazat', 'craci evazați de la genunchi în jos'), ('talie', 'Talie normală'), ('închidere', 'Închidere cu fermoar și nasture'), ('buzunare', 'aplicate și cu închidere'),
   ('material', '99% Bumbac, 1% Elastan')],
  {'Model': 'Tommy Hilfiger FLARE', 'Material': '99% bumbac, 1% elastan', 'Caracteristici': 'evazați, denim elastic, talie normală', 'Cod produs': 'KG0KG09419'})

w(11265,
  f'<p>{A("/brand/columbia/", "Columbia")} Holcomb Grove 2133751 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de schi unisex")}, portocalie, izolată, cu Omni-Heat™ Infinity pentru căldură și Omni-tech® cu cusături sudate pentru vreme rea. E pentru pârtie și sporturile de iarnă.</p>'
  '<p>Sistemul OUTGROWN o face să țină mai multe sezoane, iar spatele mai lung acoperă la mișcare. Centura de zăpadă din interior oprește zăpada să intre sub geacă, chiar la căzătură.</p>'
  '<p>Pentru pârtie, mai are:</p>'
  + L(('Mâneci', 'reglabile cu Velcro, cu găuri pentru degetul mare.'), ('Ventilație', 'deschideri cu fermoar sub axile.'), ('Glugă', 'fixă, cu guler ridicat și protecție pentru bărbie.'), ('Buzunare', 'sistem extins.'))
  + '<p>Mărimile 104-164 sunt pentru copii de 4-14 ani, în general.</p>',
  [('model', 'Columbia Geacă de schi pentru copii Holcomb Grove culoarea portocaliu, 2133751'), ('izolat', 'Izolare: izolat'), ('Omni-Heat', 'Omni-Heat ™ Infinity este o membrana speciala de aur care va mentine cald'),
   ('Omni-tech', 'Tehnologia Omni-tech®'), ('cusături', 'cusaturilor sudate acoperite cu un strat impermeabil'), ('iarnă', 'Tip de activitate: Sporturi de iarnă'),
   ('OUTGROWN', 'Sistemul OUTGROWN Grow de la Columbia'), ('spate', 'Spatele mai lung oferă acoperire atunci când vă mișcați'), ('centură', 'o centură de zăpadă încorporată'),
   ('cădere', 'chiar și în caz de cădere'), ('velcro', 'Marginile inferioare ale mânecilor sunt reglabile cu Velcro'), ('deget', 'Găurile pentru degetul mare'),
   ('ventilație', 'Deschideri de ventilatie cu fermoar sub axile'), ('glugă', 'Gulerul ridicat și gluga fixă'), ('bărbie', 'guler ridicat cu barbie'),
   ('buzunare', 'Sistemul extins de buzunare')],
  {'Model': 'Columbia Holcomb Grove', 'Material': '100% poliester; umplutură 85% poliester reciclat', 'Caracteristici': 'geacă de schi, Omni-Heat™ Infinity, Omni-tech®, OUTGROWN, centură de zăpadă', 'Cod produs': '2133751'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])
