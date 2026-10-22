import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(10817,
  f'<p>{TH} KB0KB09666 este un {A("/categorie/baieti-imbracaminte-salopete-compleuri/", "compleu pentru băieți")}, bej, format din tricou și pantaloni scurți, din tricot moale cu bumbac periat, cu logo și steagul Tommy Hilfiger. E bun pentru joacă, sport și relaxare, în zilele calde.</p>'.replace(', în zilele calde', '')
  + '<p>Croiala e regulară, iar talia pantalonilor are elastic și șnur, deci se strânge pe un copil mai slab, fără curea.</p>'
  '<p>Detaliile setului:</p>'
  + L(('Buzunare', 'două în față și unul aplicat la spate, pe pantaloni.'), ('Material', '80% bumbac, 20% poliester.'), ('Textură', 'netedă, cu branding Tommy Hilfiger.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, în general.</p>',
  [('model', 'Tommy Hilfiger Compleu pentru copii, cu bumbac bej KB0KB09666'), ('set', 'Setul format din tricou și pantaloni scurți'), ('tricot', 'Tricot moale din amestec de bumbac'),
   ('periat', 'bumbac periat'), ('logo', 'Logo-ul distinctiv și steagul Tommy Hilfiger'), ('utilizare', 'Utilizare universală pentru joacă, activități sportive și momente de relaxare'),
   ('croială', 'Croială regulară'), ('talie', 'Șnur și elastic în talia pantalonilor scurți'), ('buzunare', 'două slip-on în față și unul aplicat la spate pe pantaloni scurți'),
   ('material', '80% Bumbac, 20% Poliester'), ('textură', 'Textura netedă a materialului cu branding distinctiv Tommy Hilfiger')],
  {'Model': 'Tommy Hilfiger KB0KB09666', 'Material': '80% bumbac, 20% poliester', 'Caracteristici': 'tricou și pantaloni scurți, talie cu șnur și elastic', 'Cod produs': 'KB0KB09666'})

w(10823,
  f'<p>Geaca de blugi {A("/brand/michael-kors/", "Michael Kors")} R30293 este o {A("/categorie/geci-jachete/", "geacă de blugi pentru fete")}, bej, din denim de bumbac 100%, neizolată și fără căptușeală. E pentru zilele de tranziție, ca strat subțire.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile au manșete care se încheie, deci se strâng pe încheietură. Are guler și nu are glugă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'două, la piept, cu nasturi.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 114-150 sunt pentru copii de în jur de 6-12 ani.</p>',
  [('model', 'Michael Kors Geaca de blugi pentru copii culoarea bej, R30293'), ('denim', 'Model neizolat confecționat din denim'), ('material', '100% Bumbac'),
   ('necăptușit', 'Model neizolat fara captuseala'), ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Maneci cu mansete incheiate'),
   ('guler', 'Model cu guler'), ('fără glugă', 'Gluga: fara gluga'), ('nasturi', 'Închiderea convenabilă cu buton'), ('buzunare', 'Două buzunare la piept cu nasturi')],
  {'Model': 'Michael Kors R30293', 'Material': '100% bumbac (denim)', 'Caracteristici': 'neizolată, necăptușită, nasturi, buzunare la piept', 'Cod produs': 'R30293'})

w(10831,
  f'<p>{GEOX} SKYLIN Hello Kitty J668WC sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil înalt și imprimeu Hello Kitty, din imitație de piele și material textil. Membrana Geox Respira™ din talpă scoate umiditatea și ține apa afară, deci talpa rămâne uscată și pe ude.</p>'
  '<p>Șireturile și aricii lucrează împreună: se încalță ușor și se ajustează precis pe picior. Gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Pe scurt:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'plată, din cauciuc, rezistentă la abraziune.'))
  + '<p>Numerele 28-35 sunt pentru copii de 4-11 ani, aproximativ.</p>',
  [('model', 'Geox SKYLIN Hello Kitty sneakers pentru copii roz J668WC.0NFQ6'), ('profil', 'Profilul înalt al părții superioare'), ('Hello Kitty', 'Imprimeu adorabil Hello Kitty'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia GEOX Respira™ cu membrană microporoasă favorizează evacuarea umidității spre exterior'),
   ('apă', 'Talpa respirabilă protejează interiorul încălțămintei împotriva pătrunderii apei'), ('închidere', 'Combinația de șireturi și arici'),
   ('guler', 'Gulerul părții superioare ușor întărit'), ('călcâi', 'Călcâi ușor întărit'), ('interior', 'Interior căptușit cu material textil'),
   ('talpă', 'Talpă plată din cauciuc favorizează aderența la sol și este rezistentă la abraziune')],
  {'Model': 'Geox SKYLIN Hello Kitty', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, șireturi și arici, Geox Respira™', 'Cod produs': 'J668WC.0NFQ6'})

w(10852,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} KS1734 este o {A("/categorie/geci-jachete/", "geacă de blugi pentru fete")}, albastră, din denim de bumbac moale, cu broderii, aplicații decorative și imprimeu. Fără izolație și fără căptușeală, e pentru zilele mai calde din sezonul de tranziție.</p>'
  '<p>Croiala e relaxed fit, cu lungimea până la șolduri, iar baza și manșetele cu nervuri strâng geaca pe corp, ca la un bomber.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'capse, pe un singur rând.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '100% bumbac; inserții 100% poliester.'))
  + '<p>Mărimile 128-170 sunt pentru copii de 8-15 ani, de obicei.</p>',
  [('model', 'adidas Originals Geacă de blugi pentru copii albastră KS1734'), ('denim', 'Confecționată din denim de bumbac'), ('decor', 'Broderii și aplicații decorative'),
   ('imprimeu', 'Îmbogățită cu un imprimeu la modă'), ('neizolat', 'Model fără izolație termică, favorizând purtarea în zilele mai calde ale sezonului de tranziție'),
   ('necăptușit', 'Fără căptușeală'), ('croială', 'Croială relaxed fit'), ('lungime', 'Lungime până la șolduri'), ('nervuri', 'Bază și manșete cu nervuri'),
   ('capse', 'Închidere cu capse pe un singur rând'), ('buzunare', 'buzunare tip slip-on în părțile laterale'), ('material', '100% Bumbac')],
  {'Model': 'adidas Originals KS1734', 'Material': '100% bumbac (denim), inserții poliester', 'Caracteristici': 'neizolată, necăptușită, capse, broderii', 'Cod produs': 'KS1734'})

w(10853,
  f'<p>{GEOX} STEPPIEUP B465WA sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} maro, din piele naturală, cu interior din piele, iar inserția din piele e făcută fără crom. Deschiderea largă face încălțatul ușor, chiar și la un picior mai plin.</p>'
  '<p>Curelele cu velcro se strâng după piciorul copilului, iar cutia lată a degetelor nu le ciupește. Bucla de la spate ajută la tras pantoful pe picior.</p>'
  '<p>Talpa:</p>'.replace('Talpa:', 'Sub picior, pantoful are:')
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Interior', 'piele naturală.'))
  + '<p>Numerele 20-27 sunt pentru copii de 1-4 ani, cu aproximație.</p>',
  [('model', 'Geox Încălțăminte din piele pentru copii STEPPIEUP culoarea maro, B465WA.000CL'), ('piele', 'confecționat din piele naturală'), ('interior', 'Interiorul: Piele naturala'),
   ('crom', 'Inserția din piele a fost realizată fără utilizarea cromului'), ('deschidere', 'Deschidere larga pentru incaltarea usoara a pantofilor'),
   ('velcro', 'Curelele cu velcro pentru prindere ușoară permit o potrivire personalizată'), ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), RESPIRA, ('talpă', 'Talpa flexibilă din cauciuc')],
  {'Model': 'Geox STEPPIEUP', 'Material': 'piele naturală, interior din piele, talpă din cauciuc', 'Caracteristici': 'curele cu velcro, deschidere largă, cutie lată, Geox Respira', 'Cod produs': 'B465WA.000CL'},
  notes=['Titlul și h1 spun maro; atributul de culoare al magazinului spune bleumarin.'])

w(10855,
  f'<p>Ghetele {TH} T4A6-34037 sunt {A("/categorie/ghete-cizme/", "ghete din piele pentru fete")}, negre, din piele naturală neporoasă, care se curăță cu o cârpă umedă. Nu sunt izolate, deci se poartă în sezonul de tranziție.</p>'
  '<p>Fermoarul lateral le face ușor de încălțat și de scos. Contrafortul rigid ține călcâiul pe loc, iar vârful e o cutie rotundă, întărită.</p>'
  '<p>Înăuntru și dedesubt:</p>'
  + L(('Branț', 'din piele, previne frecarea și mirosul.'), ('Interior', 'textil și piele naturală.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 35-40 sunt pentru adolescente de la, în general, 10 ani în sus.</p>',
  [('model', 'Tommy Hilfiger Ghete din piele pentru copii culoarea negru, T4A6-34037'), ('piele', 'confecționat din piele naturală'),
   ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'), ('neizolat', 'Izolare: neizolat'),
   ('fermoar', 'Închiderea laterală convenabilă cu fermoar'), ('călcâi', 'Contorul de călcâi rigid'), ('vârf', 'Cutie rotunda, intarita'),
   ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'), ('interior', 'Material textil, Piele naturala'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Tommy Hilfiger T4A6-34037', 'Material': 'piele naturală, interior textil și piele, talpă din cauciuc', 'Caracteristici': 'neizolate, fermoar lateral, branț din piele', 'Cod produs': 'T4A6-34037'})

w(10857,
  f'<p>Cardiganul {TH} KG0KG09429 este o {A("/categorie/bluze-tricouri-hanorace/", "bluză cardigan pentru fete")}, albă, din tricot moale de bumbac și poliamidă, subțire, cu guler la decolteu și logo discret. E un strat ușor pentru sezoanele de tranziție.</p>'
  '<p>Croiala e regulară, cu umerii coborâți pe mânecă, iar materialul elastic se mișcă odată cu copilul. Tivul și manșetele cu bordură elastică țin forma.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'nasturi.'), ('Decolteu', 'cu guler.'), ('Material', '72% bumbac, 28% poliamidă.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, aproximativ.</p>',
  [('model', 'Tommy Hilfiger Cardigan pentru copii cu bumbac alb KG0KG09429'), ('tricot', 'Tricotul moale din bumbac'), ('subțire', 'Material subțire'),
   ('tranziție', 'ideal pentru sezoanele de tranziție'), ('guler', 'Decolteul cu guler'), ('logo', 'Logo-ul subtil al mărcii'), ('croială', 'Croiala regulară'),
   ('umeri', 'Mâneca lungă cu linia umerilor coborâtă'), ('elastic', 'Materialul elastic'), ('tiv', 'Tivul și manșetele cu bordură elastică'),
   ('nasturi', 'Cardigan deschis cu închidere cu nasturi'), ('material', '72% Bumbac, 28% Poliamidă')],
  {'Model': 'Tommy Hilfiger KG0KG09429', 'Material': '72% bumbac, 28% poliamidă', 'Caracteristici': 'cardigan subțire, nasturi, guler', 'Cod produs': 'KG0KG09429'})

w(10886,
  f'<p>Geaca scurtă {TH} KB0KB10450 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, albă, cu dungi, din țesătură rezistentă, cu căptușeală completă, pentru vremea schimbătoare. Gulerul ridicat apără gâtul de frig și vânt.</p>'
  '<p>Croiala e relaxed fit, cu lungimea până la șolduri, iar tivul cu șnur se strânge pe corp, ca vântul să nu intre pe dedesubt.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar și capse.'), ('Buzunare', 'laterale.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-176 se potrivesc copiilor de 8-16 ani, de regulă.</p>',
  [('model', 'Tommy Hilfiger Jachetă scurtă pentru copii albă KB0KB10450'), ('dungi', 'Model modern cu dungi'), ('țesătură', 'Țesătură rezistentă'), ('căptușeală', 'Căptușeală completă'),
   ('tranziție', 'Construcție de tranziție'), ('guler', 'Guler ridicat – protejează gâtul de frig și vânt'), ('croială', 'Croială relaxed fit'), ('lungime', 'Lungime până la șolduri'),
   ('tiv', 'Tiv cu șnur'), ('închidere', 'Închidere cu fermoar și capse'), ('buzunare', 'Buzunare laterale practice'), ('material', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KB0KB10450', 'Material': '100% poliester', 'Caracteristici': 'de tranziție, căptușită, dungi, tiv cu șnur', 'Cod produs': 'KB0KB10450'})

w(10887,
  f'<p>Șlapii {A("/brand/ugg/", "UGG")} GOLDENGLOW SLIDE 1166513K sunt {A("/categorie/unisex-incaltaminte-papuci/", "șlapi unisex")}, negri, uni, din imitație de piele și material textil, ușor de întreținut, în stil casual. Talpa e din cauciuc.</p>'
  '<p>Se închid cu arici, deci se ajustează repede pe picior, mai îngust sau mai lat, iar copilul îi pune singur, fără ajutor. Modelul e uni, deci merge la hainele de zi cu zi.</p>'
  '<p>Pe scurt:</p>'
  + L(('Branț', 'din material sintetic.'), ('Interior', 'material sintetic și textil.'), ('Talpă', 'din cauciuc.'))
  + '<p>Mărimile 27.5-38 sunt pentru copii de la aproximativ 3 ani în sus.</p>',
  [('model', 'UGG Șlapi pentru copii GOLDENGLOW SLIDE negre 1166513K'), ('uni', 'Model uni'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('întreținere', 'ușurința de întreținere'), ('casual', 'Stil casual'), ('talpă', 'Talpă din cauciuc'), ('arici', 'Sistem de închidere cu arici – permite ajustarea rapidă și ușoară'),
   ('branț', 'Branț din material sintetic'), ('interior', 'Interior din material sintetic și textil')],
  {'Model': 'UGG GOLDENGLOW SLIDE', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'șlapi cu arici', 'Cod produs': '1166513K'})

w(10902,
  f'<p>{GEOX} FADINLIGHT x Disney Princess J65M4B sunt {A("/categorie/adidasi/", "adidași pentru fete")} violet, ușori, cu profil scurt, din material textil și piele ecologică, cu prințese Disney și lumini în talpă care se aprind la mers. Seara, copilul se vede mai bine.</p>'
  '<p>Contrafortul rigid ține călcâiul în pantof, ca piciorul să nu alunece, iar vârful e o cutie rotundă, întărită.</p>'
  '<p>Pe scurt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, perforată.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 24-35 sunt pentru copii de 2-11 ani, cam.</p>'.replace('copii de 2-11 ani, cam.', 'copii de cam 2-11 ani.'),
  [('model', 'Geox Sneakers pentru copii FADINLIGHT x Disney Princess culoarea violet, J65M4B.0ANKC'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('personaje', 'Personaje de basm'), ('lumini', 'Pe talpă, lumini care se aprind în timp ce mergi'),
   ('călcâi', 'Contorul de călcâi rigid'), ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('vârf', 'Cutie rotunda, intarita'), RESPIRA,
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox FADINLIGHT x Disney Princess', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini în talpă, Geox Respira', 'Cod produs': 'J65M4B.0ANKC'})
