import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
BIO = A('/brand/biomecanics/', 'Biomecanics')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(12636,
  f'<p>Și această pereche {GEOX} SPRINTYE roz e din gama de {A("/categorie/adidasi/", "adidași pentru fete")}, de data asta cu șireturi elastice și cârlig, deci fără velcro. Sunt ușori, din material textil și piele ecologică, tăiați sub gleznă, ca piciorul să se miște liber.</p>'
  '<p>Bucla de la spate ajută la încălțat, vârful rotund, ușor rigid, lasă loc degetelor, iar contrafortul rigid ține călcâiul.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Talpă', 'din spumă, moale.'), ('Interior', 'textil, ușor de ținut curat.'))
  + '<p>Numerele 20-27 se potrivesc fetițelor de cam 1-4 ani; la 26 branțul are 17 cm.</p>',
  [('model', 'Geox Sneakers pentru copii SPRINTYE culoarea roz'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('ușor', 'Model ușor și confortabil'), ('material', 'combinatia materialului textil cu pielea ecologica'), ('gleznă', 'Pantoful de sub gleznă nu restricționează mișcarea piciorului'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('vârf', 'Degetul rotund, ușor rigid'), ('călcâi', 'Contorul de călcâi rigid'),
   RESPIRA, ('talpă', 'Talpa din spumă oferă o senzație mai moale'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 17 cm')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil și piele ecologică, interior textil, talpă din spumă', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira, buclă la spate', 'Cod produs': ''})

w(12637,
  f'<p>{REIMA} Intona bleumarin sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")} de exterior, tip jogger, cu croială relaxed fit, gândiți pentru drumeții și trekking, în stil sport techwear. Membrana impermeabilă are 10000 mm H2O, iar respirabilitatea e de 7000 g/m²/24h, cu rezistență la vânt.</p>'
  '<p>Genunchii și șezutul sunt întărite, iar cusăturile sunt lipite. Talia elastică se reglează din interior.</p>'
  '<p>Ce mai au, pe lângă croială:</p>'
  + L(('Craci', 'largi, cu șnur de strângere.'), ('Reflectorizante', 'pentru vizibilitate.'), ('Căptușeală', 'plasă sintetică, rezistentă la murdărie.'), ('Material', 'poliester acoperit cu TPU.'))
  + '<p>Mărimile 104-164 merg la copii de aproximativ 4-14 ani.</p>',
  [('model', 'Reima Pantaloni pentru copii Intona bleumarin 5100431A'), ('jogger', 'Joggeri outdoor pentru copii , cu croială relaxed fit'), ('drumeții', 'Concepuți pentru drumeții și trekking , în stil sportiv techwear'),
   ('membrană', 'Membrană impermeabilă 10000 mm H2O'), ('respirabilitate', 'Respirabilitate 7000 g/m²/24h și rezistență la vânt'),
   ('întărituri', 'Întăriri la genunchi și la șezut și cusături lipite'), ('talie', 'Talie elastică cu ajustare internă'),
   ('craci', 'Craci largi cu șnur de strângere și elemente reflectorizante'), ('căptușeală', 'Căptușeală sintetică tip plasă , din material rezistent la murdărie'),
   ('material', '100% Poliester acoperit cu TPU')],
  {'Model': 'Reima Intona', 'Material': 'poliester acoperit cu TPU, căptușeală plasă', 'Caracteristici': '10000 mm H2O, cusături lipite, întărituri la genunchi', 'Cod produs': '5100431A'})

w(12638,
  f'<p>Geaca {A("/brand/lego/", "LEGO Wear")} bleumarin este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} izolată, matlasată, cu fason drept, din material ornamentat și impermeabilitate de 3000 mm. Gluga se detașează, iar gulerul ridicat apără gâtul.</p>'
  '<p>Detaliile reflectorizante 3M Scotchlite îl fac pe copil mai ușor de văzut pe orice vreme. Geaca e căptușită și izolată, iar matlasajul ține umplutura la locul ei.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'exterioare, cu închidere.'), ('Căptușeală', 'da, geaca e căptușită.'), ('Material', '100% poliester.'))
  + '<p>Gama e foarte largă, 80-164, deci acoperă cam 1-14 ani.</p>',
  [('model', 'Lego Wear geaca copii culoarea albastru marin'), ('izolat', 'Izolare: izolat'), ('matlasat', 'Matlasare'), ('fason', 'Fason drept'),
   ('ornamentat', 'material ornamentat'), ('impermeabil', 'Impermeabilitate: 3000 mm'), ('glugă', 'Gluga detasabila'), ('guler', 'Guler ridicat'),
   ('3M', 'Materialele reflectorizante 3M ™ Scotchlite'), ('buzunare', 'Buzunare exterioare incheiata'), ('căptușeală', 'Captuseala: cu captuseala'), ('material', '100% Poliester')],
  {'Model': 'LEGO Wear (geacă)', 'Material': '100% poliester, izolată', 'Caracteristici': 'glugă detașabilă, 3000 mm, reflectorizante 3M', 'Cod produs': ''})

w(12639,
  f'<p>Modelul {BIO} 262165 în varianta pentru fetițe: {A("/categorie/adidasi/", "adidași pentru fete")} albi, cu partea de sus până la gleznă, gândiți împreună cu podologi pentru primăvară, vară și toamnă. Au spațiu mărit în zona degetelor, deci degetele se așază natural.</p>'
  '<p>Contrafortul e ușor rigidizat, iar velcro-ul o lasă pe fetiță să se încalțe singură. Partea de sus, înaltă până la gleznă, ține piciorul bine pe loc la mers.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'antibacterian, detașabil.'), ('Talpă', 'din cauciuc.'), ('Partea de sus', 'textil și material sintetic.'))
  + '<p>Numerele 19-23 sunt, orientativ, pentru 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii albi 262165'), ('gleznă', 'Partea superioară până la gleznă'), ('podologi', 'creat în colaborare cu podologi'),
   ('sezon', 'primăvară, vară și toamnă'), ('degete', 'Spațiu mărit în zona degetelor'), ('contrafort', 'Contrefort ușor rigidizat'),
   ('velcro', 'Închidere comodă cu velcro'), ('branț', 'Branț antibacterian'), ('detașabil', 'Branțuri detașabile'), ('talpă', 'Talpă din cauciuc'),
   ('material', 'Material textil, Material sintetic')],
  {'Model': 'Biomecanics 262165', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, branț antibacterian, spațiu mărit la degete', 'Cod produs': '262165'})

w(12641,
  f'<p>Geaca {REIMA} Trekkeri verde este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} de tranziție, ușoară, rezistentă la apă și vânt, pentru primăvară, vară și toamnă. Țesătura conține fibre Seawool, din cochilii de stridii reciclate, iar izolația sintetică ușoară ține de cald fără să încurce la mișcare.</p>'
  '<p>Nu are glugă, are croială dreaptă și lungime până la șolduri. Se închide cu fermoar.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'laterale, cu închidere.'), ('Tiv și mâneci', 'cu elastic.'), ('Reflectorizante', 'integrate.'), ('Material', 'poliamidă, poliester și elastan.'))
  + '<p>Gama 104-164 acoperă copii de în jur de 4-14 ani.</p>',
  [('model', 'Reima Jachetă copii Trekkeri verde 5100451A'), ('tranziție', 'Geaca de tranziție Reima'), ('ușor', 'ușoară și rezistentă la apă'), ('vânt', 'rezistență la vânt'),
   ('sezon', 'primăvara, vara și toamna'), ('Seawool', 'Utilizarea fibrelor Seawool® din cochilii de stridii reciclate'), ('izolație', 'Izolația sintetică ușoară'),
   ('glugă', 'Model fără glugă'), ('croială', 'Croiala dreaptă a gecii'), ('lungime', 'Lungimea gecii până la șolduri'), ('fermoar', 'Închiderea principală cu fermoar'),
   ('buzunare', 'Buzunare laterale practice cu închidere'), ('elastic', 'Mânecile și marginea inferioară sunt finisate cu un tiv elastic'),
   ('reflectorizant', 'Elementele reflectorizante integrate'), ('material', '100% Poliamidă'), ('material 2', '92% Poliester, 8% Elastan')],
  {'Model': 'Reima Trekkeri', 'Material': 'poliamidă, poliester cu elastan, izolație din poliester', 'Caracteristici': 'Seawool, rezistentă la apă și vânt, reflectorizante', 'Cod produs': '5100451A'})

w(12642,
  f'<p>{BIO} 261108 în bleumarin sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} plați, cu imprimeu decorativ, din piele naturală și imitație de piele, cu finisaj de piele întoarsă, în stil casual și streetwear. Vârful rotund e cauciucat și apără degetele de lovituri.</p>'
  '<p>Velcro-ul cu curea reglabilă se strânge exact cât trebuie, iar gulerul moale nu irită glezna.</p>'
  '<p>Cum e făcut pantoful:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc, de 1 cm.'), ('Interior', 'căptușit cu textil.'), ('Branț', 'textil, detașabil.'), ('Călcâi', 'întărit.'))
  + '<p>Numerele 19-25 se poartă cam între 1 și 3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii bleumarin 261108'), ('plat', 'Sneakerși flat pentru copii'), ('imprimeu', 'Imprimeu decorativ'),
   ('material', 'Partea superioară dintr-o combinație de piele naturală și imitație de piele cu finisaj din piele întoarsă'), ('stil', 'Stil casual și streetwear'),
   ('vârf', 'Vârf rotund, cauciucat'), ('velcro', 'Închidere cu velcro și curea reglabilă'), ('guler', 'guler moale al părții superioare'),
   ('talpă', 'Talpă flexibilă din cauciuc cu o grosime de 1 cm'), ('interior', 'Interior căptușit cu material textil'), ('branț', 'Branț detașabil din material textil'),
   ('călcâi', 'Călcâi întărit')],
  {'Model': 'Biomecanics 261108', 'Material': 'piele naturală și imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro cu curea reglabilă, vârf cauciucat, branț detașabil', 'Cod produs': '261108'})

w(12643,
  f'<p>Aceeași geacă {A("/brand/colmar/", "Colmar")} GLOWER neagră, în mărimile mici: o {A("/categorie/geci-jachete/", "geacă pentru fete")} cu puf de rață și pene, căptușită, pentru iernile reci. Gluga, gulerul ridicat și fermoarul țin vântul departe.</p>'
  '<p>Exteriorul neted e din poliamidă, iar croiala e simplă, dreaptă. Magazinul spune că umplutura naturală dă un nivel ridicat de izolare.</p>'
  '<p>Ce trebuie știut despre ea:</p>'
  + L(('Umplutură', '90% puf de rață, 10% pene de rață.'), ('Căptușeală', '100% poliamidă.'), ('Buzunare', 'laterale, cu fermoar.'))
  + '<p>Numerele 106-142 se potrivesc fetelor de vreo 4-10 ani, orientativ.</p>',
  [('model', 'Colmar Geacă copii GLOWER culoarea negru, 3475.8XV'), ('puf', 'Umplutura din puf si pene'), ('izolat', 'Model izolat cu captuseala'),
   ('frig', 'garantează un nivel ridicat de izolare împotriva frigului'), ('glugă', 'Model cu gluga'), ('închidere', 'Are inchidere cu fermoar si guler ridicat'), ('neted', 'material neted'),
   ('exterior', 'Material de bază: 100% Poliamida'), ('croială', 'Tăiere simplă, fără blocare'), ('umplutură', '90% Duck Down, 10% Pene de rață'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar')],
  {'Model': 'Colmar GLOWER', 'Material': '100% poliamidă, umplutură 90% puf de rață și 10% pene', 'Caracteristici': 'glugă, guler ridicat, fermoar', 'Cod produs': '3475.8XV'})

w(12645,
  f'<p>{REIMA} Vantti este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} în culoarea albastru, softshell și windbreaker, cu imprimeu vegetal pe toată suprafața, fără izolație, pentru sezonul de tranziție. Are 10000 mm H2O, impregnare care respinge apa și material rezistent la vânt și la murdărie.</p>'
  '<p>Gluga se detașează, iar căptușeala parțială din polar adaugă puțină căldură. Fermoarul merge pe toată lungimea.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunar', 'la piept, cu închidere.'), ('Manșete', 'cu bordură elastică.'), ('Reflectorizante', 'pentru întuneric.'), ('Material', '92% poliester, 8% elastan.'))
  + '<p>Mărimile 86-140 sunt pentru copii de cam 1-10 ani.</p>',
  [('model', 'Reima Jachetă pentru copii Vantti albastră 5100009D'), ('culoare', 'Culoare albastru'), ('softshell', 'jachetă softshell ușoară și o geacă windbreaker'),
   ('imprimeu', 'Imprimeu vegetal pe toată suprafața'), ('izolație', 'Fără izolație termică'), ('tranziție', 'sezonul de tranziție'), ('H2O', 'Impermeabilitate 10 000 mm H2O'),
   ('impregnare', 'Impregnare hidrofobă a suprafeței materialului'), ('vânt', 'Material softshell rezistent la vânt'), ('murdărie', 'Rezistență la murdărie'),
   ('glugă', 'Glugă detașabilă'), ('polar', 'Căptușeală parțială din polar'), ('fermoar', 'Fermoar cu un singur rând pe toată lungimea'),
   ('buzunar', 'Buzunar la piept , cu închidere'), ('manșete', 'Manșete cu bordură elastică'), ('reflectorizant', 'Elemente reflectorizante'), ('material', '92% Poliester, 8% Elastan')],
  {'Model': 'Reima Vantti', 'Material': '92% poliester, 8% elastan, căptușeală parțială din polar', 'Caracteristici': 'softshell, 10000 mm H2O, glugă detașabilă', 'Cod produs': '5100009D'})

w(12646,
  f'<p>{GEOX} FASTICS sunt {A("/categorie/adidasi/", "adidași pentru fete")} negri, cu buline, din imitație de piele și material textil, ușor de ținut curați, în stil casual și streetwear. Tehnologia GEOX Respira scoate umezeala spre exterior.</p>'
  '<p>Aricii și inserția elastică fac încălțatul și descălțatul rapid, iar călcâiul întărit ține piciorul pe loc. Talpa plată din cauciuc ține bine pe sol, deci pantoful merge și la joacă.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'căptușit cu textil moale.'), ('Branț', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 28-35 sunt pentru fete de aproximativ 4-11 ani.</p>',
  [('model', 'Geox FASTICS sneakers pentru copii negri J46GZB.0BCBL'), ('buline', 'designul atractiv cu buline'), ('material', 'Partea superioară din imitație de piele și material sintetic facilitează menținerea încălțămintei curate'),
   ('stil', 'stilizări casual și streetwear'), ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală a piciorului, eliminând umiditatea spre exterior'),
   ('arici', 'Închidere cu arici și inserție elastică facilitează încălțarea și descălțarea rapidă'), ('călcâi', 'Călcâi întărit'),
   ('interior', 'Interior căptușit cu material textil'), ('branț', 'Branț din material textil'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox FASTICS', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici cu inserție elastică, buline', 'Cod produs': 'J46GZB.0BCBL'},
  notes=['Compoziția magazinului scrie „Piatră sintetică” (probabil eroare pentru piele sintetică); am folosit „imitație de piele” din descriere.'])

w(12648,
  f'<p>{GEOX} SKETLITE sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, cu aplicații decorative și imprimeu, din imitație de piele și material textil, pentru ținute casual de oraș. Membrana microporoasă Geox Respira din talpă scoate umezeala și ține picioarele uscate.</p>'
  '<p>Se închid cu șireturi și fermoar lateral, deci se reglează o dată și apoi se încalță repede. Gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Interior', 'textil moale.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 32-35 merg la fete de în jur de 8-11 ani.</p>',
  [('model', 'Geox SKETLITE sneakers pentru copii albi J66NWA.0NFKN'), ('decor', 'Aplicații decorative și imprimeu'), ('material', 'Față din imitație de piele și material textil'),
   ('urban', 'ținute casual, urbane'), ('Respira', 'Tehnologia Geox Respira™ cu o membrană microporoasă în talpă favorizează eliminarea umidității'),
   ('închidere', 'Închidere cu șireturi și fermoar lateral'), ('guler', 'Gulerul superior ușor întărit îmbracă delicat glezna'), ('călcâi', 'Călcâi ușor întărit'),
   ('interior', 'Interior căptușit cu material textil moale'), ('talpă', 'Talpă plată, din cauciuc')],
  {'Model': 'Geox SKETLITE', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi și fermoar lateral', 'Cod produs': 'J66NWA.0NFKN'})
