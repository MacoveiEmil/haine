import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
PANT = '/categorie/unisex-imbracaminte-pantaloni-treninguri/'

w(14333,
  f'<p>Pantalonii {REIMA} SAMPU albastru închis sunt {A(PANT, "pantaloni unisex")} impermeabili și respirabili, pentru orice vreme, cu membrană Reimatec, 10.000 mm coloană de apă și 7.000 g/m²/24 h respirabilitate. Toate cusăturile sunt lipite.</p>'
  '<p>Genunchii, șezutul și capetele cracilor sunt întărite cu material foarte rezistent, iar marginea cracului se strânge cu șnur. Căptușeala e din plasă respirabilă.</p>'
  '<p>Buzunarele și materialul:</p>'
  + L(('Buzunare', 'două laterale și unul pe coapsă, cu fermoar.'), ('Material', '100% SORONA.'), ('Greutate', '160 g.'))
  + '<p>Mărimile 116-164 sunt pentru copii de aproximativ 6-14 ani.</p>',
  [('model', 'REIMA SAMPU'), ('culoare', 'Albastru închis (albastru închis / negru)'), ('impermeabil', 'Sunt respirabili și impermeabili'), ('vreme', 'în orice condiții meteorologice'),
   ('Reimatec', 'Reimatec'), ('coloană', '10.000 mm'), ('respirabilitate', '7.000 g/m²/24 h'), ('lipite', 'Toate cusăturile sunt lipite'),
   ('întărituri', 'beneficiază de întărituri la nivelul genunchilor, șezutului și extremităților picioarelor'), ('șnur', 'Marginea inferioară a cracului poate fi strânsă cu un șnur'),
   ('plasă', 'Au o căptușeală din plasă respirabilă'), ('buzunare', '3 (2x laterale cu fermoar, 1x pe crac cu fermoar)'), ('material', '100% SORONA®'), ('greutate', '160 g')],
  {'Model': 'Reima SAMPU', 'Material': '100% SORONA, membrană Reimatec', 'Caracteristici': '10.000 mm, cusături lipite, întărituri, crac reglabil', 'Cod produs': '199936'})

w(14334,
  f'<p>Sandalele barefoot {REIMA} VALOA roz sunt {A("/categorie/unisex-incaltaminte-sandale/", "sandale unisex")} vegane, cu partea de sus tricotată, respirabilă și elastică, care se mulează pe picior. Drop zero și forma lată, cu loc pentru degete, țin piciorul în poziție sănătoasă.</p>'
  '<p>Șiretul elastic le face foarte rapide de pus și de scos, iar talpa flexibilă din cauciuc ține bine pe multe suprafețe.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Branț', 'detașabil, ușor de întreținut.'), ('Față', 'poliester.'), ('Greutate', '200 g.'))
  + '<p>Numerele 28-40 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'REIMA VALOA'), ('culoare', 'Roz (roz / alb)'), ('barefoot', 'Sandalele barefoot pentru copii REIMA VALOA'), ('vegan', 'vegane'),
   ('tricot', 'Partea superioară tricotată respirabilă și elastică asigură o ventilație optimă și adaptarea la forma piciorului'),
   ('drop', 'Dropul zero la nivelul călcâiului'), ('lat', 'designul lat cu spațiu suplimentar pentru degete'), ('șiret', 'șiret elastic pentru încălțare rapidă și ușoară'),
   ('talpă', 'Talpa flexibilă din cauciuc asigură o aderență excelentă pe o varietate de suprafețe'), ('branț', 'Branțul detașabil facilitează întreținerea'),
   ('față', 'poliester'), ('greutate', '200 g')],
  {'Model': 'Reima VALOA', 'Material': 'poliester tricotat, talpă din cauciuc', 'Caracteristici': 'barefoot, drop zero, șiret elastic, vegane', 'Cod produs': '240091'})

w(14358,
  f'<p>Șortul {REIMA} VALOISIN UVF50 roșu e unul dintre {A(PANT, "pantalonii unisex")} de vară, din poliamidă cu fibre reciclate, cu protecție UV 50+. Se întreține ușor, se usucă repede și elimină umezeala.</p>'
  '<p>Talia elastică se reglează și se închide cu velcro și capsă. Pe laterale sunt două buzunare, iar materialul se întreține ușor și se usucă repede după spălare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Protecție', 'UV 50+.'), ('Talie', 'elastică, cu velcro și capsă.'))
  + '<p>Mărimile 116-164 sunt pentru copii de cam 6-14 ani.</p>',
  [('model', 'REIMA VALOISIN UVF50'), ('culoare', 'Roșu'), ('șort', 'Șortul pentru copii Reima VALOISIN UVF50'), ('poliamidă', 'este realizat din 100 % poliamidă'),
   ('reciclat', 'conține fibre reciclate certificate'), ('UV', 'factor de protecție UV 50+'), ('întreținere', 'Are întreținere ușoară, uscare rapidă și elimină fiabil umezeala'),
   ('talie', 'Talie elastică ajustabilă, care se încheie cu velcro și capsă'), ('buzunare', 'Dispune de două buzunare laterale')],
  {'Model': 'Reima VALOISIN UVF50 (șort)', 'Material': '100% poliamidă', 'Caracteristici': 'UV 50+, uscare rapidă, talie reglabilă', 'Cod produs': '198027'})

w(14393,
  f'<p>Cizmele de cauciuc {REIMA} AMFIBI galbene sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} din EVA, foarte ușoare, impermeabile și vegane, pentru sezoanele de tranziție. Orificiile de pe gambă ajută la tras cizma pe picior.</p>'
  '<p>Forma lată lasă loc degetelor să crească normal, iar în talpă e o canelură unde se prind buclele pantalonilor de ploaie. Nu conțin materiale de origine animală.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', 'EVA.'), ('Greutate', '100 g.'), ('Construcție', 'impermeabilă.'))
  + '<p>Mărimile 22/23 până la 34/35 se potrivesc copiilor de aproximativ 1-11 ani.</p>',
  [('model', 'REIMA AMFIBI'), ('culoare', 'Galben'), ('ușor', 'Cizmele pentru copii Reima AMFIBI sunt extrem de ușoare'), ('EVA', 'Sunt confecționate din material EVA'),
   ('impermeabil', 'construcție impermeabilă'), ('vegan', 'vegane'), ('tranziție', 'potrivite pentru sezoanele de tranziție'), ('orificii', 'Datorită orificiilor de pe gambe, se pot încălța ușor'), ('animal', 'Nu conțin materiale de origine animală'),
   ('lat', 'construcție lată - spațiu suplimentar pentru degete'), ('canelură', 'Există o canelură în talpă unde se prind buclele pantalonilor de ploaie'), ('greutate', '100 g')],
  {'Model': 'Reima AMFIBI', 'Material': 'EVA', 'Caracteristici': 'impermeabile, foarte ușoare, canelură pentru buclele pantalonilor', 'Cod produs': '198059'})

w(14408,
  f'<p>Tricoul UV {REIMA} JOONIA roz e un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "tricou unisex")} cu mânecă scurtă, pentru apă și uscat, cu factor UV 50+ care apără de razele soarelui. Cusăturile plate nu freacă, iar croiala profilată, cu căptușeală suplimentară, acoperă mai bine.</p>'
  '<p>Se usucă repede, deci e bun pentru zilele de vară. Imprimeul acoperă toată suprafața, iar croiala lejeră lasă loc de mișcare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '83% poliester reciclat, 17% elastan.'), ('Croială', 'lejeră.'), ('Greutate', '120 g.'))
  + '<p>Mărimile 104-140 sunt pentru copii de cam 4-10 ani.</p>',
  [('model', 'REIMA JOONIA'), ('culoare', 'Roz (roz / alb / galben)'), ('UV', 'Materialul cu factor UV 50+ protejează împotriva razelor solare dăunătoare'),
   ('acvatic', 'activități acvatice și terestre'), ('cusături', 'cusăturile plate asigură un confort maxim'), ('croială', 'Croiala profilată și căptușeala suplimentară asigură o acoperire mai bună'),
   ('uscare', 'Se usucă rapid'), ('imprimeu', 'pe toată suprafața'), ('mânecă', 'scurt'), ('material', '83 % poliester reciclat, 17 % elastan'), ('lejer', 'lejeră'), ('greutate', '120 g')],
  {'Model': 'Reima JOONIA', 'Material': '83% poliester reciclat, 17% elastan', 'Caracteristici': 'UV 50+, uscare rapidă, cusături plate', 'Cod produs': '239989'})

w(14429,
  f'<p>{REIMA} SILLAT în albastru închis sunt {A(PANT, "pantaloni unisex")} de drumeție care devin scurți: cracul se desface cu fermoar. Tratamentul Anti-Bite, netoxic și biodegradabil, alungă căpușele, țânțarii și alte insecte vreme de cel puțin o sută de spălări, fără să le facă rău.</p>'
  '<p>Stretch-ul e plăcut pe piele și se usucă repede, iar factorul UV 50+ apără de soare. Talia se reglează, genunchiul e anatomic, iar elementele reflectorizante îl arată pe copil seara.</p>'
  '<p>Buzunarele și materialul:</p>'
  + L(('Buzunare', 'două laterale și unul pe picior, cu fermoar.'), ('Material', 'poliester 100%.'), ('Greutate', '250 g.'))
  + '<p>Se potrivesc copiilor de pe la 6 până pe la 14 ani (116-164).</p>',
  [('model', 'REIMA SILLAT'), ('culoare', 'Albastru închis (albastru închis / argintiu)'), ('crac', 'lung, detașabil cu fermoar'),
   ('Anti-Bite', 'Materialul Reima Anti-Bite are finisaj non-toxic și biodegradabil Si Repel Mosquito'), ('insecte', 'Acesta respinge în mod eficient căpușele, țânțarii'),
   ('spălări', 'Efectul repelent durează cel puțin o sută de cicluri de spălare'), ('stretch', 'Materialul stretch este foarte plăcut în contact cu pielea, este respirabil și se usucă rapid'),
   ('UV', 'factor de protecție UV 50+'), ('talie', 'talie ajustabilă'), ('genunchi', 'genunchi anatomic'), ('reflectorizant', 'Reflectorizant (da/nu)'),
   ('buzunare', '3 (2x laterale, 1x pe picior cu fermoar)'), ('material', '100 % poliester'), ('greutate', '250 g')],
  {'Model': 'Reima SILLAT', 'Material': '100% poliester', 'Caracteristici': 'crac detașabil, Anti-Bite, UV 50+', 'Cod produs': '166234'},
  notes=['Magazinul notează că insectele pot ajunge pe părțile descoperite ale corpului.'])

w(14441,
  f'<p>Ghetele outdoor {REIMA} EHDI maro sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} impermeabile, pe gleznă, cu membrană și cusături lipite, pentru toamnă și ierni mai blânde. Talpa din cauciuc e flexibilă și ține bine pe toate suprafețele.</p>'
  '<p>Velcro-ul le face ușor de încălțat, iar elementele reflectorizante îl arată pe copil seara. Nu conțin compuși cu fluor sau materiale de origine animală.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'EVA turnat, detașabil, cu Happy Fit.'), ('Căptușeală', 'plasă și poliester.'), ('Talpă', '50% EVA, 50% cauciuc.'))
  + '<p>Numerele 20-28 se potrivesc copiilor de aproximativ 1-5 ani.</p>',
  [('model', 'REIMA EHDI'), ('culoare', 'Maro (maro / alb)'), ('impermeabil', 'Ghetele impermeabile pentru copii REIMA EHDI'), ('membrană', 'ghete pe gleznă cu membrană'),
   ('sezon', 'concepute pentru zilele de toamnă sau pentru iernile mai blânde'), ('lipite', 'inserție impermeabilă, cu cusături lipite și căptușeală din plasă'),
   ('talpă', 'talpă din cauciuc pentru o aderență mai bună'), ('velcro', 'închidere practică cu velcro'), ('reflectorizant', 'elemente reflectorizante'),
   ('fluor', 'nu conțin compuși cu fluor sau materiale de origine animală'), ('branț', 'branț detașabil, turnat EVA și căptușeală din jerseu'), ('Happy Fit', 'imprimeu Happy Fit'),
   ('izolație', 'căptușeală: 100 % poliester'), ('talpă 2', '50 % EVA, 50 % cauciuc')],
  {'Model': 'Reima EHDI', 'Material': 'poliester, poliuretan, nailon, talpă EVA și cauciuc', 'Caracteristici': 'membrană, cusături lipite, velcro, Happy Fit', 'Cod produs': '178389'})

w(14464,
  f'<p>Hanoracul cu glugă {REIMA} LUPAUS verde e un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} din material plăcut și elastic, din poliester reciclat, care se usucă repede. Are glugă fixă, buzunar cangur și logo.</p>'
  '<p>E un strat intermediar bun pentru școală sau ieșiri afară și poate fi purtat ca strat exterior ușor vara. Marginea de jos e liberă, iar materialul elastic urmează mișcările.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '89% poliester reciclat, 11% elastan.'), ('Mâneci', 'lungi.'), ('Greutate', '230 g.'))
  + '<p>Mărimile 116-158 sunt pentru copii de aproximativ 6-13 ani.</p>',
  [('model', 'REIMA LUPAUS'), ('culoare', 'Verde (verde / verde închis)'), ('elastic', 'material foarte plăcut și elastic, care se usucă rapid'),
   ('reciclat', 'Este fabricat din fibre de poliester reciclate'), ('glugă', 'Este prevăzut cu o glugă fixă și buzunar cangur'), ('logo', 'logo'),
   ('strat', 'Este un strat intermediar excelent pentru mersul la școală sau pentru activități în aer liber'), ('vară', 'un strat exterior ușor în zilele de vară'),
   ('material', '89 % poliester reciclat, 11 % elastan'), ('mâneci', 'lungi'), ('greutate', '230 g'), ('margine', 'liberă')],
  {'Model': 'Reima LUPAUS', 'Material': '89% poliester reciclat, 11% elastan', 'Caracteristici': 'glugă fixă, buzunar cangur, uscare rapidă', 'Cod produs': '166238'})

w(14465,
  f'<p>Ghetele de iarnă {REIMA} KONKARI negre sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} vegane, impermeabile, testate până la -20 °C, care fac față și zăpezii umede. Au șosete interioare detașabile, cu căptușeală fleece, ușor de curățat.</p>'
  '<p>Velcro-ul face încălțatul ușor, iar talpa rotunjită, din EVA și cauciuc reciclat, face pasul fluid. Detaliile reflectorizante ajută pe întuneric.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Branțuri', 'detașabile, cu Happy Fit.'), ('Cusături', 'cu inserție impermeabilă.'), ('Greutate', '325 g, fără fluorocarbon și PVC.'))
  + '<p>Numerele 30-38 se poartă de pe la 6 ani în sus.</p>',
  [('model', 'REIMA KONKARI'), ('culoare', 'Negru (negru / alb)'), ('vegan', 'vegane'), ('zăpadă', 'oferă protecție și confort chiar în zăpadă umedă'),
   ('impermeabil', 'Sunt impermeabile și au șosete detașabile pentru o curățare ușoară'), ('-20', 'Sunt testate pentru izolare împotriva frigului până la -20 °C'),
   ('fleece', 'căptușeală fleece'), ('velcro', 'închidere ușoară cu velcro'), ('talpă', 'talpă flexibilă și ușoară Reima EVA/cauciuc'),
   ('rotunjit', 'Designul rotunjit al tălpii le permite copiilor să se bucure de o deplasare mai fluidă'), ('reciclat', 'cauciuc reciclat'),
   ('reflectorizant', 'Detaliile reflectorizante sporesc vizibilitatea'), ('Happy Fit', 'branțuri detașabile cu imprimeu Happy Fit'),
   ('cusături', 'inserție impermeabilă în cusături'), ('greutate', '325 g'), ('PVC', 'fără fluorocarbon și PVC')],
  {'Model': 'Reima KONKARI', 'Material': 'sintetic, căptușeală fleece, talpă EVA și cauciuc', 'Caracteristici': 'impermeabile, -20 °C, șosete detașabile, velcro', 'Cod produs': '259924'})

w(14471,
  f'<p>Pantofii barefoot {REIMA} VAELLUS negri sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} vegani, fără PFAS și PVC, gândiți pentru creșterea sănătoasă a piciorului: drop zero la călcâi, talpă flexibilă și vârf lat, cu loc pentru degete.</p>'
  '<p>Șireturile elastice fac încălțatul rapid, iar talpa din cauciuc are protecție la vârf contra loviturilor și ține bine pe sol.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Branțuri', 'EVA modelate, cu căptușeală tricotată și Happy Fit.'), ('Față', 'material sintetic.'), ('Talpă', 'cauciuc.'))
  + '<p>Numerele 30-38 se potrivesc copiilor de la aproximativ 6 ani în sus.</p>',
  [('model', 'REIMA VAELLUS'), ('culoare', 'Negru (negru / gri)'), ('vegan', 'vegani'), ('PFAS', 'fără conținut de PFAS, PVC'),
   ('creștere', 'sunt concepuți pentru a favoriza creșterea sănătoasă și mișcarea liberă a picioarelor'), ('drop', 'drop zero pentru o poziție naturală'),
   ('flexibil', 'talpă flexibilă pentru libertate de mișcare'), ('vârf', 'Pantofii cu vârf lat oferă spațiu suplimentar pentru degetele de la picioare'),
   ('șiret', 'șireturile elastice permit încălțarea rapidă și ușoară'), ('protecție', 'talpă cu protecție împotriva loviturilor la degetele de la picioare'),
   ('talpă', 'talpă flexibilă din cauciuc pentru o aderență optimă'), ('branț', 'inserțiile din EVA, cu căptușeală din tricot și imprimeu Happy Fit'), ('față', 'material sintetic')],
  {'Model': 'Reima VAELLUS', 'Material': 'sintetic, talpă din cauciuc', 'Caracteristici': 'barefoot, drop zero, șireturi elastice, Happy Fit', 'Cod produs': '277977'})
