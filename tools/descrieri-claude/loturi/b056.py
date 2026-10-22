import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(11389,
  f'<p>Geaca {TH} KB0KB10091 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de puf pentru băieți")}, neagră, matlasată, izolată cu puf de rață și pene (70/30), pentru frigul de iarnă. Gulerul ridicat și gluga fixă apără gâtul și capul de vânt.</p>'
  '<p>Croiala e simplă, dreaptă, deci încape un pulover dedesubt, iar mânecile au bandă elastică la capăt, care strânge la încheieturi și ține căldura înăuntru.</p>'
  '<p>Pe scurt, despre geacă:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale.'), ('Material', '100% poliamidă, căptușeală poliester.'))
  + '<p>Mărimile 98-122 sunt pentru copii de 3-7 ani, cu aproximație.</p>',
  [('model', 'Tommy Hilfiger Geacă de puf pentru copii culoarea negru, KB0KB10091'), ('matlasat', 'material matlasat'), ('puf', '70% Puf de rata, 30% Pene'),
   ('frig', 'izolare împotriva frigului'), ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('croială', 'Tăiere simplă, fără blocare'),
   ('elastic', 'Mâneci finisate cu o coadă elastică'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('buzunare', 'Două buzunare laterale'),
   ('material', 'Materialul de baza: 100% Poliamida')],
  {'Model': 'Tommy Hilfiger KB0KB10091', 'Material': '100% poliamidă; umplutură 70% puf, 30% pene', 'Caracteristici': 'puf, matlasată, glugă fixă', 'Cod produs': 'KB0KB10091'})

w(11390,
  f'<p>Geaca {TH} KS0KS00775 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, bleumarin, ușoară, fără izolație termică, cu căptușeală completă, pentru vremea schimbătoare. Gluga integrată apără de vânt și ploaie ușoară, iar gulerul ridicat apără gâtul.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar manșetele cu nervuri strâng la încheieturi.</p>'
  '<p>Mai sunt câteva detalii:</p>'
  + L(('Închidere', 'fermoar și capse.'), ('Buzunare', 'laterale, slip-on și cu clapă.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 80-122 sunt pentru copii de în jur de 1-7 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă de tranziție pentru copii bleumarin KS0KS00775'), ('neizolat', 'Fără izolație termică permite purtarea în perioadele de tranziție'),
   ('căptușeală', 'Căptușeală completă'), ('glugă', 'Glugă integrată oferă protecție capului împotriva vântului și a ploii ușoare'), ('guler', 'Guler ridicat oferă protecție gâtului împotriva vântului'),
   ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'), ('manșete', 'Manșete cu nervuri'), ('închidere', 'Închidere cu fermoar și capse'),
   ('buzunare', 'Buzunare laterale , slip-on și cu clapă'), ('material', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KS0KS00775', 'Material': '100% poliester', 'Caracteristici': 'neizolată, căptușită, glugă integrată, fermoar și capse', 'Cod produs': 'KS0KS00775'})

w(11395,
  f'<p>{A("/brand/liewood/", "Liewood")} Jesse Cat Thermo Rainboot LW20370 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de ploaie unisex")}, portocalii, izolate, din masă plastică mată, cu modele. Sunt făcute pentru zilele ude și reci, iar interiorul e textil.</p>'
  '<p>Bucla de la spate ajută copilul să tragă cizma pe picior și să o scoată singur. Talpa exterioară din cauciuc rezistă la uzură.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Partea de sus', 'material sintetic, finisaj mat.'), ('Interior', 'material textil.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 22-29 sunt pentru copii de 1-5 ani, de regulă.</p>',
  [('model', 'Liewood Cizme copii Jesse Cat Thermo Rainboot culoarea portocaliu, LW20370'), ('izolat', 'Model izolat'), ('plastic', 'masa plastica mat, cu modele'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior și ajută la scoaterea acestuia'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('interior', 'Interiorul: Material textil'), ('mat', 'Finisare: mat')],
  {'Model': 'Liewood Jesse Cat Thermo Rainboot', 'Material': 'sintetic mat, interior textil, talpă din cauciuc', 'Caracteristici': 'izolate, buclă la spate', 'Cod produs': 'LW20370'},
  notes=['„Zile ude” e dedus din numele modelului (Rainboot) și materialul plastic.'])

w(11408,
  f'<p>{A("/brand/konges-slojd/", "Konges Sløjd")} ISA CARDIGAN KS103829 este o {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "bluză cardigan unisex")}, portocalie, uni, din tricot ajurat subțire, jumătate lână, jumătate poliamidă. Poliamida îl face mai rezistent la purtat des.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile raglan lasă brațele să se miște liber. Se închide cu nasturi, deci se pune și se dă jos ușor.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Material', '50% poliamidă, 50% lână.'), ('Tricot', 'ajurat, subțire.'), ('Închidere', 'nasturi.'))
  + '<p>Mărimile 92 până la 122-128 sunt pentru copii de în jur de 2-8 ani.</p>',
  [('model', 'Konges Sløjd Cardigan de lână pentru copii ISA CARDIGAN culoarea portocaliu, light, KS103829'), ('uni', 'Model: uni'), ('ajurat', 'tricot ajurat'),
   ('subțire', 'Tricotaje: subtiri'), ('material', '50% Poliamida, 50% Lana'), ('poliamidă', 'Adaosul de poliamidă asigură o durabilitate mai mare'),
   ('croială', 'Tăiere simplă, fără blocare'), ('raglan', 'Mânecile raglan'), ('nasturi', 'Închiderea convenabilă cu buton')],
  {'Model': 'Konges Sløjd ISA CARDIGAN', 'Material': '50% poliamidă, 50% lână', 'Caracteristici': 'cardigan ajurat, mâneci raglan, nasturi', 'Cod produs': 'KS103829'})

w(11416,
  f'<p>Rochia {TH} KG0KG09264 este o {A("/categorie/rochii-fuste/", "rochie din denim pentru fete")}, bej, cu imprimeu, scurtă (mini), din bumbac 100% aerisit, pentru anotimpurile mai calde. Are bretele reglabile și decolteu în V.</p>'
  '<p>Croiala e dreaptă, simplă, iar bretelele se strâng sau se lungesc după înălțimea copilului. Nu e căptușită, deci rămâne ușoară, iar vara se poartă singură, peste un tricou sau direct.</p>'
  '<p>Elementele practice:</p>'
  + L(('Închidere', 'nasturi.'), ('Lungime', 'mini.'), ('Material', '100% bumbac (denim).'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, aproximativ.</p>',
  [('model', 'Tommy Hilfiger Rochie din denim pentru copii culoarea bej, mini, drept, KG0KG09264'), ('imprimeu', 'Model: imprimeu'), ('mini', 'Lungime: mini'), ('bumbac', '100% Bumbac'),
   ('cald', 'perfect pentru anotimpurile mai calde'), ('bretele', 'Model cu bretele reglabile'), ('decolteu', 'Decolteu în V'), ('croială', 'Fit: drept'),
   ('necăptușit', 'Model fara captuseala'), ('nasturi', 'Închiderea convenabilă cu buton')],
  {'Model': 'Tommy Hilfiger KG0KG09264', 'Material': '100% bumbac (denim)', 'Caracteristici': 'mini, bretele reglabile, decolteu în V', 'Cod produs': 'KG0KG09264'})

w(11417,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} KQ8906 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă bomber din denim unisex")}, neagră, uni, cu efect prespălat și logo discret, din denim de bumbac, fără izolație și fără căptușeală. E pentru zilele mai călduroase de tranziție.</p>'
  '<p>Croiala e lejeră, supradimensionată, cu mâneci raglan și lungimea până la șolduri. Tivul și manșetele cu bordură elastică strâng bomberul pe corp, ca să nu stea larg la încheieturi.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Închidere', 'fermoar.'), ('Guler', 'ridicat.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 104-128 sunt pentru copii de 4-8 ani, în mare.</p>',
  [('model', 'adidas Originals Geacă bomber pentru copii din denim neagră KQ8906'), ('uni', 'Modelul uni cu efect prespălat'), ('logo', 'un logo subtil al brandului'),
   ('denim', 'Denimul din bumbac'), ('neizolat', 'Fără izolație favorizează purtarea în zilele mai călduroase'), ('necăptușit', 'Fără căptușeală'),
   ('croială', 'Croiala lejeră, supradimensionată'), ('raglan', 'Mâneca raglan'), ('lungime', 'Lungimea până la șolduri'), ('elastic', 'Tivul și manșetele cu bordură elastică'),
   ('fermoar', 'Sistemul de închidere cu fermoar'), ('guler', 'Gulerul ridicat'), ('material', '100% Bumbac')],
  {'Model': 'adidas Originals KQ8906', 'Material': '100% bumbac (denim)', 'Caracteristici': 'bomber, prespălat, neizolat, oversize', 'Cod produs': 'KQ8906'})

w(11428,
  f'<p>{TH} KB0KB10506 este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")}, bleumarin, cu imprimeu expresiv, fără închidere, din tricot moale și subțire de bumbac 100%, elastic. Stilul e casual și streetwear.</p>'
  '<p>Croiala e regulară, iar bordurile elastice de la bază și manșete strâng ușor pe corp. Decolteul rotund are bordură elastică, deci hanoracul se trage ușor peste cap.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'rotund, cu bordură elastică.'), ('Închidere', 'nu are, se îmbracă peste cap.'))
  + '<p>Mărimile 104-122 sunt pentru copii de 4-7 ani, de regulă.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii, din bumbac bleumarin KB0KB10506'), ('imprimeu', 'Imprimeu expresiv'), ('fără închidere', 'Construcție fără închidere'),
   ('tricot', 'Tricot moale din bumbac'), ('subțire', 'Material subțire'), ('elastic', 'Material elastic'), ('casual', 'Stil casual și streetwear'), ('croială', 'Croială regulară'),
   ('borduri', 'Borduri elastice la bază și la manșete'), ('decolteu', 'Decolteu rotund cu bordură elastică'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB10506', 'Material': '100% bumbac', 'Caracteristici': 'fără închidere, imprimeu, borduri elastice', 'Cod produs': 'KB0KB10506'})

w(11439,
  f'<p>Cămașa {TH} KB0KB09554 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "cămașă cu mânecă scurtă pentru băieți")}, albastră, din bumbac natural cu puțin elastan, cu guler clasic tip kent. Mâneca scurtă o face bună pentru zilele mai calde.</p>'
  '<p>Croiala e regulară, iar elastanul o lasă să se miște cu copilul. Se închide cu nasturi și se poartă casual, singură sau peste un tricou.</p>'
  '<p>Câteva detalii practice:</p>'
  + L(('Guler', 'kent, clasic.'), ('Material', '97% bumbac, 3% elastan.'), ('Închidere', 'nasturi.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, în general.</p>',
  [('model', 'Tommy Hilfiger Cămașă pentru copii, din bumbac albastră KB0KB09554'), ('bumbac', 'Confecționată din bumbac natural'), ('material', '97% Bumbac, 3% Elastan'),
   ('guler', 'Guler clasic tip kent'), ('mânecă', 'Mânecă scurtă favorizează confortul în zilele mai calde'), ('croială', 'Croială regulară'), ('casual', 'Stil casual'),
   ('nasturi', 'Închidere cu nasturi')],
  {'Model': 'Tommy Hilfiger KB0KB09554', 'Material': '97% bumbac, 3% elastan', 'Caracteristici': 'mânecă scurtă, guler kent, nasturi', 'Cod produs': 'KB0KB09554'})

w(11457,
  f'<p>Papucii {A("/brand/ugg/", "UGG")} T TASMAN II 1019066T sunt {A("/categorie/unisex-incaltaminte-papuci/", "papuci unisex")} negri, slip-on, din piele întoarsă cu material textil, cu interior și branț din UGGplush™ (lână și TENCEL™ Lyocell), care țin piciorul cald. Merg și prin casă, și la ieșiri scurte afară.</p>'
  '<p>Construcția slip-on îi face ușor de încălțat și de scos, iar vârful e închis și apără degetele la joacă.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Talpă', 'din spumă EVA din trestie de zahăr, ușoară.'), ('Guler', 'cu proprietăți anti-miros.'), ('Detaliu', 'împletitură UGG din fibre reciclate.'))
  + '<p>Numerele 21-30 sunt pentru copii de 1-7 ani, cu aproximație.</p>',
  [('model', 'UGG Papuci copii piele întoarsă T TASMAN II negri 1019066T'), ('slip-on', 'Construcție de tip slip-on'), ('material', 'Partea superioară din piele întoarsă cu material textil'),
   ('UGGplush', 'Interior din lână UGGplush™ și TENCEL™ Lyocell, ce favorizează menținerea căldurii'), ('branț', 'Branț moale UGGplush™'),
   ('casă', 'potriviți atât pentru casă, cât și pentru exterior'), ('vârf', 'Vârf închis , ce ajută la protejarea degetelor'),
   ('talpă', 'Talpă din spumă EVA din trestie de zahăr'), ('anti-miros', 'Guler cu proprietăți anti-miros'), ('împletitură', 'Împletitură decorativă UGG din fibre reciclate')],
  {'Model': 'UGG T TASMAN II', 'Material': 'piele întoarsă și textil, interior UGGplush™, talpă EVA', 'Caracteristici': 'slip-on, UGGplush™, vârf închis', 'Cod produs': '1019066T'})

w(11476,
  f'<p>Pantalonii de trening {TH} KB0KB10593 sunt {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "pantaloni de trening pentru băieți")}, albi, din bumbac 100% elastic, cu broderii discrete. Se poartă casual și streetwear, la joacă și la ieșiri.</p>'
  '<p>Croiala e regulară, iar talia normală are bandă elastică și șnur, deci se strânge pe un copil mai slab, fără curea.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'laterale și unul la spate.'), ('Material', '100% bumbac.'), ('Detalii', 'broderii Tommy Hilfiger.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Pantaloni de trening pentru copii, din bumbac albi regular waist KB0KB10593'), ('bumbac', 'Confecționați din bumbac 100%'), ('elastic', 'Material elastic'),
   ('broderii', 'Decorate cu broderii subtile'), ('casual', 'Ideali pentru stilizații casual și streetwear'), ('croială', 'Pantaloni de trening cu croială regulară'),
   ('talie', 'Talie normală cu bandă elastică și șnururi în talie'), ('buzunare', 'buzunare practice laterale și unul la spate')],
  {'Model': 'Tommy Hilfiger KB0KB10593', 'Material': '100% bumbac', 'Caracteristici': 'talie elastică cu șnur, buzunare, broderii', 'Cod produs': 'KB0KB10593'})
