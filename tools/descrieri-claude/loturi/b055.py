import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
COLMAR = A('/brand/colmar/', 'Colmar')

w(11324,
  f'<p>{COLMAR} OUTCOME 3434.7XT este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de puf pentru băieți")}, neagră, matlasată, din poliamidă netedă, umplută cu puf și pene (90/10), cu rezistență sporită la apă. E pentru iarnă, iar gulerul ridicat și gluga fixă apără gâtul și capul.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri pe corp, deci încape un pulover gros dedesubt și vine comod și unui copil mai plinuț.</p>'
  '<p>Pe scurt, despre geacă:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere.'), ('Căptușeală', '100% poliamidă.'))
  + '<p>Mărimile 106-172 sunt pentru copii de 4-15 ani, cu aproximație.</p>',
  [('model', 'Colmar Geaca de puf pentru copii OUTCOME culoarea negru, 3434.7XT'), ('matlasat', 'Matlasare'), ('neted', 'material neted'), ('puf', '90% Puf, 10% Pene'),
   ('apă', 'Model cu rezistenta sporita la apa'), ('frig', 'izolare impotriva frigului'), ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('croială', 'Tăiere simplă, fără blocare'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'), ('căptușeală', 'Captuseala: 100% Poliamida')],
  {'Model': 'Colmar OUTCOME', 'Material': '100% poliamidă; umplutură 90% puf, 10% pene', 'Caracteristici': 'puf, matlasată, glugă fixă, rezistentă la apă', 'Cod produs': '3434.7XT'})

w(11333,
  f'<p>{GEOX} BIGLIA B564CA sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} (bleumarin pe site, aurii la magazin), din piele naturală și piele întoarsă, cu căptușeală din piele. Tehnologia Geox Respira™ scoate umiditatea, iar sistemul Flexy din talpă lasă piciorul să se îndoaie natural.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, iar branțul moale, căptușit, face pasul mai comod.</p>'
  '<p>Pentru purtat zilnic, contează și:</p>'
  + L(('Partea de sus', 'piele naturală și piele întoarsă.'), ('Căptușeală', 'piele naturală.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 18-26 sunt pentru copii de în jur de 1-4 ani.</p>',
  [('model', 'Geox BIGLIA sneakers pentru copii din piele aurii B564CA.085CF'), ('material', 'Partea superioară din piele naturală și piele întoarsă'),
   ('căptușeală', 'Căptușeala din piele naturală'), ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală, eliminând umiditatea'),
   ('Flexy', 'Sistemul Flexy din talpă susține flexiunea naturală a piciorului'), ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă'),
   ('branț', 'Branțul moale și căptușit'), ('talpă', 'Talpa de cauciuc')],
  {'Model': 'Geox BIGLIA', 'Material': 'piele naturală și piele întoarsă, căptușeală din piele, talpă din cauciuc', 'Caracteristici': 'arici, Geox Respira™, Flexy', 'Cod produs': 'B564CA.085CF'},
  notes=['Titlul de pe site spune bleumarin; magazinul spune aurii.'])

w(11341,
  f'<p>{A("/brand/diesel/", "Diesel")} JOSIPLS JACKET J02884 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă scurtă unisex")}, neagră, cu izolație sintetică ușoară, căptușeală completă și model cu logo Diesel, pentru sezoanele de tranziție. Gluga integrată apără de vânt și ploaie ușoară.</p>'
  '<p>Croiala e regulară, cu loc pentru un hanorac sau un pulover dedesubt, iar lungimea ajunge până la șolduri, deci acoperă spatele la joacă. Gulerul ridicat apără gâtul de frig.</p>'
  '<p>Material și închidere, pe rând:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 120-175 sunt pentru copii de 7-16 ani, de obicei.</p>',
  [('model', 'Diesel Jachetă scurtă pentru copii JOSIPLS JACKET neagră J02884'), ('izolație', 'Izolație sintetică ușoară'), ('căptușeală', 'Căptușeală completă'),
   ('logo', 'Model cu logo adaugă jachetei un accent distinctiv, recunoscut al brandului Diesel'), ('tranziție', 'sezoanele de tranziție'),
   ('glugă', 'Glugă integrată oferă protecție suplimentară împotriva vântului și a ploii ușoare'), ('croială', 'Croială regulară favorizează libertatea de mișcare, permițând purtarea confortabilă a straturilor suplimentare'),
   ('lungime', 'Lungime până la șolduri'), ('guler', 'Guler ridicat'), ('fermoar', 'Închidere cu fermoar'), ('buzunare', 'Buzunare laterale practice'), ('material', '100% Poliamidă')],
  {'Model': 'Diesel JOSIPLS JACKET', 'Material': '100% poliamidă', 'Caracteristici': 'izolație ușoară, glugă integrată, guler ridicat', 'Cod produs': 'J02884'})

w(11350,
  f'<p>{GEOX} FADINLIGHT Lilo &amp; Stitch J66M4E sunt {A("/categorie/adidasi/", "adidași pentru fete")} bleumarin, cu imprimeu Lilo și Stitch și lumini în talpă, care îl fac pe copil mai vizibil. Tehnologia Geox Respira™ ține interiorul uscat.</p>'
  '<p>Șireturile elastice nu trebuie legate, iar aricii permit încălțatul rapid, de către copil. Călcâiul întărit ține piciorul în pantof.</p>'
  '<p>Alte detalii utile:</p>'
  + L(('Partea de sus', 'imitație de piele și material sintetic, ușor de întreținut.'), ('Interior', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 28-35 sunt pentru copii de 4-11 ani, în general.</p>',
  [('model', 'Geox FADINLIGHT Lilo & Stitch sneakers pentru copii bleumarin J66M4E.05402'), ('imprimeu', 'Imprimeu decorativ cu motivul Lilo & Stitch'),
   ('lumini', 'Lumini încorporate în talpă adaugă veselie și vizibilitate'), ('Respira', 'Tehnologia Geox Respira™ susține eliminarea umidității, menținând interiorul pantofului uscat'),
   ('șireturi', 'Șireturi elastice facilitează ajustarea la picior, fără a fi nevoie de legare'), ('arici', 'Închidere practică cu arici permite încălțarea rapidă și independentă'),
   ('călcâi', 'Călcâi întărit'), ('material', 'Material exterior din imitație de piele și material sintetic, ușor de întreținut'), ('interior', 'Interior din material textil'),
   ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox FADINLIGHT Lilo & Stitch', 'Material': 'imitație de piele și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini în talpă, șireturi elastice și arici, Geox Respira™', 'Cod produs': 'J66M4E.05402'})

w(11355,
  f'<p>{A("/brand/konges-slojd/", "Konges Sløjd")} NUKA JACKET KS103522 este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă matlasată pentru bebeluși")}, verde, izolată cu THERMOLITE® EcoMade din sticle reciclate, cu finisaj BIONIC-FINISH® ECO, rezistent la apă. E pentru temperaturile mai reci.</p>'
  '<p>Croiala e simplă, dreaptă, iar fermoarul e lateral, deci geaca se îmbracă ușor pe un copil mic. Gulerul ridicat și gluga fixă apără gâtul și capul de frig.</p>'
  '<p>Ce merită știut în plus:</p>'
  + L(('Buzunare', 'oblice.'), ('Respirabilitate', '3000 g/m2.'), ('Căptușeală', 'din poliester reciclat.'))
  + '<p>Mărimile 74 până la 134-140 sunt pentru copii de la cam 9 luni la 10 ani.</p>',
  [('model', 'Konges Sløjd Geacă copii NUKA JACKET GRS culoarea verde, KS103522'), ('matlasat', 'Matlasat'), ('THERMOLITE', 'Izolatia THERMOLITE® EcoMade este fabricata din sticle de plastic reciclate 100%'),
   ('BIONIC', 'BIONIC-FINISH® ECO'), ('apă', 'Rezistența la apă înseamnă o protecție sporită'), ('reci', 'temperaturi mai reci'), ('croială', 'Tăiere simplă, fără blocare'),
   ('fermoar', 'Închiderea laterală convenabilă cu fermoar'), ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('buzunare', 'Buzunare oblice'),
   ('respirabilitate', 'Respirabilitate: 3000 g/m2'), ('căptușeală', '100% Poliester reciclat')],
  {'Model': 'Konges Sløjd NUKA JACKET', 'Material': 'poliester și bumbac, căptușeală din poliester reciclat', 'Caracteristici': 'THERMOLITE® EcoMade, BIONIC-FINISH® ECO, glugă fixă, fermoar lateral', 'Cod produs': 'KS103522'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(11361,
  f'<p>Botinele {A("/brand/primigi/", "Primigi")} PROGT 23746 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} bej, din piele întoarsă, cu interior textil izolat termic, care ține căldura în zilele reci. Stilul e casual, pentru purtat zi de zi.</p>'
  '<p>Vârful rotund lasă loc degetelor, iar călcâiul întărit ține piciorul stabil. Colaborarea Primigi × SIPeP ține cont de anatomia piciorului copilului.</p>'
  '<p>Mai sunt câteva lucruri de știut:</p>'
  + L(('Shock Absorber', 'tehnologie în talpă care reduce șocurile.'), ('Interior', 'material textil, izolat.'), ('Partea de sus', 'piele întoarsă.'))
  + '<p>Numerele 31-35 sunt pentru copii de 6-11 ani, cu aproximație.</p>',
  [('model', 'Primigi Botine pentru copii din piele întoarsă bej PROGT 23746'), ('piele întoarsă', 'Partea superioară din piele întoarsă'),
   ('izolat', 'Interiorul izolat termic din material textil ajută la menținerea căldurii în zilele reci'), ('casual', 'stilul casual'),
   ('vârf', 'Vârful rotund oferă spațiu pentru degete'), ('călcâi', 'Călcâiul întărit'), ('SIPeP', 'Colaborarea Primigi × SIPeP ține cont de dezvoltarea și anatomia piciorului copilului'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă ajută la reducerea șocurilor')],
  {'Model': 'Primigi PROGT 23746', 'Material': 'piele întoarsă, interior textil izolat', 'Caracteristici': 'izolate, Shock Absorber, Primigi × SIPeP', 'Cod produs': 'PROGT 23746'})

w(11376,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} DOWNACKET IX7493 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de puf unisex")}, neagră, matlasată, cu puf de rață și pene, din poliester parțial reciclat și căptușeală din bumbac. E pentru temperaturile scăzute, iar gluga se detașează.</p>'
  '<p>Croiala e simplă, dreaptă, deci încape un strat gros dedesubt. Mânecile și tivul sunt simplu tăiate.</p>'
  '<p>Alte detalii utile:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale, cu capse.'), ('Umplutură', '55% puf de rață, 45% pene.'))
  + '<p>Mărimile 62-104 sunt pentru cei mici, de cam 3 luni până la 4 ani.</p>',
  [('model', 'adidas Originals Geaca de puf pentru copii DOWNACKET culoarea negru, IX7493'), ('matlasat', 'material matlasat'), ('puf', '55% Duck Down, 45% Pene'),
   ('reciclat', 'realizat partial din poliester reciclat'), ('căptușeală', 'Captuseala: 100% Bumbac'), ('scăzute', 'temperaturi mai scăzute'), ('glugă', 'Gluga detasabila'),
   ('croială', 'Tăiere simplă, fără blocare'), ('mâneci', 'Mâneci și marginea inferioară finisate cu tăiere'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare')],
  {'Model': 'adidas Originals DOWNACKET', 'Material': 'poliester reciclat, căptușeală bumbac; umplutură 55% puf, 45% pene', 'Caracteristici': 'puf, matlasată, glugă detașabilă', 'Cod produs': 'IX7493'})

w(11384,
  f'<p>{COLMAR} GLOWER 3476.8XV este o {A("/categorie/geci-jachete/", "geacă de puf pentru fete")}, roz, matlasată, din poliamidă netedă, cu puf de rață și pene (90/10) și rezistență sporită la apă. E pentru frigul de iarnă.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri pe corp, deci încape un pulover gros dedesubt. Fiindcă nu are glugă, merge purtată cu o căciulă.</p>'
  '<p>La purtat, contează și:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', '100% poliamidă, căptușeală poliamidă.'))
  + '<p>Mărimile 154-172 sunt pentru adolescente de aproximativ 12-15 ani.</p>',
  [('model', 'Colmar Geaca de puf pentru copii GLOWER culoarea roz, 3476.8XV'), ('matlasat', 'Matlasat'), ('neted', 'material neted'), ('puf', '90% Puf de rata, 10% Pene de rață'),
   ('apă', 'Model cu rezistenta sporita la apa'), ('frig', 'izolare impotriva frigului'), ('fără glugă', 'Gluga: fara gluga'), ('croială', 'Tăiere simplă, fără blocare'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'), ('material', 'Materialul de baza: 100% Poliamida')],
  {'Model': 'Colmar GLOWER', 'Material': '100% poliamidă; umplutură 90% puf, 10% pene', 'Caracteristici': 'puf, matlasată, rezistentă la apă', 'Cod produs': '3476.8XV'})

w(11385,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KG0KG09446 este un {A("/categorie/bluze-tricouri-hanorace/", "hanorac pentru fete")}, bleumarin, cu logo discret, din tricot subțire de bumbac 100%, fără glugă, fără închidere și fără buzunare. Materialul subțire îl face bun pentru zilele mai calde.</p>'
  '<p>Croiala e lejeră, cu mâneci raglan, iar materialul elastic se mișcă odată cu copilul. Bordurile elastice de la manșete și bază țin forma.</p>'
  '<p>Pentru zi de zi, are:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'rotund.'), ('Mâneci', 'raglan.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, de regulă.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac bleumarin KG0KG09446'), ('logo', 'logo-ul subtil'), ('bumbac', 'Bumbacul moale , cu structură tricotată'),
   ('fără glugă', 'Croiala clasică fără închidere și glugă'), ('fără buzunare', 'Lipsa buzunarelor'), ('subțire', 'Materialul subțire asigură confort la purtare în zilele mai calde'),
   ('croială', 'Croiala lejeră regulară'), ('raglan', 'Mâneci raglan'), ('elastic', 'Materialul elastic'), ('borduri', 'Borduri elastice la manșete și la bază'), ('decolteu', 'Decolteu rotund'),
   ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG09446', 'Material': '100% bumbac', 'Caracteristici': 'subțire, mâneci raglan, fără glugă', 'Cod produs': 'KG0KG09446'})
