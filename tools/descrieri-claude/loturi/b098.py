import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
UV_NOTE = 'Mărimile sunt circumferința capului în cm (44-46 … 52-54); vârsta e dată orientativ.'

w(13828,
  f'<p>Ghetuțele {REIMA} KIRITIN albastre sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} de primăvară și toamnă, cu membrană impermeabilă, care țin piciorul uscat și la temperatură bună pe orice vreme. Detaliile reflectorizante îl fac pe copil mai vizibil seara.</p>'
  '<p>Talpa moale și flexibilă din Phylon e gândită să urmeze mișcarea naturală a piciorului.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Branț', 'textil, detașabil, cu imprimeu Happy Fit pentru mărime.'), ('Față', 'material sintetic și textil.'), ('Talpă', 'Phylon.'))
  + '<p>Numerele 28-35 se potrivesc copiilor de aproximativ 4-11 ani.</p>',
  [('model', 'REIMA KIRITIN'), ('culoare', 'Albastru (albastru / verde deschis)'), ('sezon', 'Ghetuțele pentru copii Reima KIRITIN sunt indicate pentru anotimpul de primăvară și toamnă'),
   ('membrană', 'membrană impermeabilă'), ('uscat', 'asigură piciorului confortul termic și uscat pe orice fel de vreme'), ('reflectorizant', 'detalii reflectorizante'),
   ('talpă', 'talpă moale și flexibilă din material Phylon'), ('natural', 'designul tălpii susține mișcarea naturală a piciorului'),
   ('branț', 'Au branț detașabil de textil, cu imprimeu Happy Fit'), ('față', 'material sintetic și textil')],
  {'Model': 'Reima KIRITIN', 'Material': 'sintetic și textil, talpă Phylon', 'Caracteristici': 'membrană impermeabilă, reflectorizante, Happy Fit', 'Cod produs': '220326'})

w(13832,
  f'<p>Tenișii {REIMA} TOMERA roz sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} pentru copiii mici, cu partea de sus din textil și material sintetic și căptușeală textilă, fără fluorură de carbon. Velcro-ul îl ajută pe copil să se încalțe singur.</p>'
  '<p>Talpa EVA e moale și flexibilă și ține foarte bine pe teren, iar branțul se scoate ușor.</p>'
  '<p>Ce mai au tenișii:</p>'
  + L(('Branț', 'EVA, detașabil, cu suprafață textilă și imprimeu Happy Fit.'), ('Căptușeală', 'textilă.'), ('Închidere', 'velcro.'))
  + '<p>Numerele 22-28 sunt pentru copii de în jur de 1-5 ani.</p>',
  [('model', 'REIMA TOMERA'), ('culoare', 'Roz (roz / alb)'), ('mici', 'Tenișii Reima TOMERA sunt indicați pentru copiii mici'),
   ('material', 'Partea superioară este din textil și material sintetic'), ('căptușeală', 'căptușeală din textil'), ('fluor', 'fără fluorură de carbon'),
   ('velcro', 'Încheierea cu velcro facilitează copilului încălțarea'), ('talpă', 'Au talpă moale și flexibilă EVA, care asigură o aderență foarte bună în teren'),
   ('branț', 'Au branț detașabil EVA cu suprafață de textil și imprimeu Happy Fit')],
  {'Model': 'Reima TOMERA', 'Material': 'textil și sintetic, talpă EVA', 'Caracteristici': 'velcro, branț Happy Fit, fără fluorură de carbon', 'Cod produs': '198079'})

w(13838,
  f'<p>Șapca de soare {REIMA} KILPIKONNA portocalie, din gama SunProof, e una dintre {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "accesoriile unisex")} pentru vară: material ușor și elastic, care elimină umezeala și se usucă repede, cu protecție UV 50+. Cozorocul moale și apărătoarea de la spate feresc fața și gâtul de soare.</p>'
  '<p>Banda elastică o ține pe cap și la joacă. Nu are căptușeală, deci e ușoară.</p>'
  '<p>Detaliile de protecție:</p>'
  + L(('UPF', '50+, testat după EN 13758-1 +A1.'), ('UVA și UVB', 'oxid de titan integrat în fibre.'), ('Material', '80% poliamidă reciclată, 20% elastan.'))
  + '<p>Mărimile 44-46, 48-50 și 52-54 sunt circumferința capului, pentru copii de la aproximativ 1 an în sus.</p>',
  [('model', 'REIMA KILPIKONNA'), ('culoare', 'Portocaliu (portocaliu / negru / alb)'), ('SunProof', 'acest model ușor din gama Reima SunProof'), ('ușor', 'Materialul ușor și respirabil'),
   ('umezeală', 'elimină eficient umezeala'), ('uscare', 'proprietăților sale de uscare rapidă'), ('UPF', 'protecția UV ridicată UPF 50+'), ('cozoroc', 'Cozorocul moale'),
   ('spate', 'Are o protecție la spate'), ('elastic', 'Banda elastică asigură o adaptare perfectă formei capului'), ('căptușeală', 'croială ușoară, fără căptușeală'),
   ('EN', 'factor de protecție UV 50+, testat conform standardului EN 13758-1 +A1'), ('TiO2', 'protecție împotriva razelor UVA și UVB datorită TiO₂ (oxidului de titan) integrat în fibre'),
   ('material', '80% poliamidă (reciclată), 20% elastan')],
  {'Model': 'Reima KILPIKONNA', 'Material': '80% poliamidă reciclată, 20% elastan', 'Caracteristici': 'UPF 50+, SunProof, uscare rapidă', 'Cod produs': '278406'},
  varsta_txt='de la 1 an în sus', notes=[UV_NOTE])

w(13850,
  f'<p>Adidașii {REIMA} ENKKARI roz sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} vegani, impermeabili, de primăvară-toamnă, cu membrană laminată pe partea de sus, din poliester și poliuretan, care ține picioarele uscate și pe ploaie. Elementele reflectorizante ajută seara.</p>'
  '<p>Velcro-ul și șireturile elastice fac încălțatul ușor, iar talpa din Phylon și cauciuc e ușoară și flexibilă, ca piciorul să se miște ușor. Sunt făcuți pentru perioadele de tranziție.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Căptușeală', 'textilă, elastică.'), ('Talpă', 'EVA și cauciuc.'), ('Greutate', '450 g.'))
  + '<p>Numerele 28-35 se potrivesc copiilor de cam 4-11 ani.</p>',
  [('model', 'REIMA ENKKARI'), ('culoare', 'Roz (roz / vișiniu / alb)'), ('vegan', 'produs vegan'), ('sezon', 'încălțăminte impermeabilă de primăvară-toamnă'),
   ('membrană', 'Datorită unei membrane impermeabile laminate la partea superioară realizată dintr-o combinație de poliester și poliuretan, picioarele rămân uscate chiar și în zilele ploioase'),
   ('reflectorizant', 'Elementele reflectorizante îmbunătățesc siguranța'), ('închidere', 'Fixarea practică cu velcro în combinație cu șireturile elastice facilitează încălțarea'),
   ('talpă', 'talpă flexibilă și ușoară din Phylon/cauciuc'), ('căptușeală', 'căptușeala elastică asigură confort'), ('talpă 2', 'EVA, cauciuc'), ('greutate', '450 g'), ('tranziție', 'Sunt ideali pentru perioadele de tranziție'), ('ușor', 'designul tălpii le permite copiilor să se miște cu ușurință')],
  {'Model': 'Reima ENKKARI', 'Material': 'poliester și poliuretan, talpă EVA și cauciuc', 'Caracteristici': 'membrană impermeabilă, velcro și șireturi elastice, reflectorizante', 'Cod produs': '240084'})

w(13862,
  f'<p>Sandalele {REIMA} KORALLI galbene sunt {A("/categorie/unisex-incaltaminte-sandale/", "sandale unisex")} ușoare, vegane, din EVA, bune și pe plajă sau în apă. Se spală la mașină, la 30°C, pe ciclu delicat, deci se întrețin ușor.</p>'
  '<p>Talpa e ușoară, moale și flexibilă, iar vârful lat lasă degetele să se miște liber. Se închid cu două benzi velcro, deci se pun și se scot repede.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față și talpă', '100% EVA.'), ('Greutate', '120 g.'), ('Închidere', 'două benzi velcro.'))
  + '<p>Gama 22-35 acoperă copii de aproximativ 1-11 ani.</p>',
  [('model', 'REIMA KORALLI'), ('culoare', 'Galben (galben / negru)'), ('plajă', 'Sandalele ușoare pentru copii Reima KORALLI sunt potrivite și pe plajă sau în apă'),
   ('vegan', 'vegani'), ('spălare', 'se pot spăla la mașină, ciclu delicat la 30 °C'), ('talpă', 'Au o talpă ușoară și flexibilă'), ('EVA', 'talpă ușoară și moale EVA'),
   ('vârf', 'un vârf lat pentru mișcarea liberă a degetelor'), ('velcro', 'se închid cu două benzi velcro'), ('material', '100% acetat de etilenă și vinil (EVA)'), ('greutate', '120 g')],
  {'Model': 'Reima KORALLI', 'Material': '100% EVA', 'Caracteristici': 'pentru apă, lavabile la 30°C, velcro', 'Cod produs': '240078'})

w(13903,
  f'<p>Geaca {A("/brand/alpine-pro/", "ALPINE PRO")} KERBO vișinie este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} de iarnă, matlasată, din softshell hidrofug, rezistent la vânt și respirabil, foarte ușor, cu umplutură medie, caldă. Gluga se detașează și e căptușită, cu elastic.</p>'
  '<p>Mânecile au manșetă interioară tricotată, fermoarul are protecție pentru bărbie, iar pe față e un imprimeu modern. Croiala e lejeră.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Fermoare', 'cu șnur, ușor de prins.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-110 până la 152-158 sunt pentru copii de aproximativ 4-13 ani.</p>',
  [('model', 'ALPINE PRO KERBO'), ('culoare', 'Vișiniu (vișiniu / mix)'), ('matlasat', 'Geaca matlasată pentru copii ALPINE PRO KERBO'), ('softshell', 'material hidrofug softshell, rezistent la vânt și respirabil'),
   ('ușor', 'foarte ușor'), ('umplutură', 'umplutură medie, caldă'), ('glugă', 'glugă detașabilă căptușită cu elastic'), ('manșetă', 'mâneci cu manșetă interioară tricotată'),
   ('bărbie', 'protecție pentru bărbie'), ('imprimeu', 'un imprimeu modern pe față'), ('croială', 'croială lejeră'), ('buzunare', '2 (2x laterale cu fermoar)'),
   ('șnur', 'fermoare cu șnur pentru manipulare mai ușoară'), ('material', '100 % poliester'), ('iarnă', 'De copii - De iarnă')],
  {'Model': 'ALPINE PRO KERBO', 'Material': '100% poliester (softshell), umplutură medie', 'Caracteristici': 'glugă detașabilă, protecție pentru bărbie, buzunare cu fermoar', 'Cod produs': '146072'})

w(13916,
  f'<p>{REIMA} TALLUSTELU în mov sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} barefoot cu membrană impermeabilă Reimatec, buni la școală și în excursii, primăvara și toamna. Partea de sus e lată, ca degetele să nu se deformeze, iar talpa plată ține piciorul în poziție naturală.</p>'
  '<p>Talpa e subțire și flexibilă, deci copilul simte terenul și își lucrează mușchii tălpii. Șiretul cu stopper face încălțatul ușor.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Față', 'material sintetic și textil.'), ('Căptușeală', 'textilă.'), ('Talpă', 'cauciuc foarte aderent.'))
  + '<p>Numerele 28-40 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'REIMA TALLUSTELU'), ('culoare', 'Mov (mov / bej)'), ('barefoot', 'Pantofii barefoot pentru copii Reima TALLUSTELU au membrană impermeabilă Reimatec'),
   ('școală', 'sunt ideali atât la școală, cât și în excursii pe timp de primăvară și toamnă'), ('lat', 'Partea superioară este destul de lată, pentru a nu duce la deformarea degetelor'),
   ('plat', 'Talpa este plată, ceea ce duce la poziția naturală a copilului în timpul mersului'), ('subțire', 'talpa este subțire și flexibilă'),
   ('mușchi', 'stimularea mult mai bună a mușchiului din talpă'), ('șiret', 'șiretul cu stopper facilitează încălțarea'), ('față', 'material sintetic și textil'),
   ('căptușeală', 'căptușeală de textil'), ('talpă', 'talpă de cauciuc foarte aderentă')],
  {'Model': 'Reima TALLUSTELU', 'Material': 'sintetic și textil, talpă din cauciuc', 'Caracteristici': 'barefoot, Reimatec, șiret cu stopper', 'Cod produs': '277970'})

w(13925,
  f'<p>Șapca {REIMA} MUSTEKALA roz e unul dintre {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "accesoriile unisex")} de vară, din jerseu elastic, cu protecție UV 50+, ca cei mici să stea mai mult la soare în siguranță. Cozorocul moale apără ochii, iar borul extins la spate apără gâtul.</p>'
  '<p>Nu are căptușeală, deci e ușoară, iar materialul se usucă repede, bun pentru plajă și locul de joacă.</p>'
  '<p>Detaliile de protecție:</p>'
  + L(('UPF', '50+, testat după EN 13758-1 +A1.'), ('UVA și UVB', 'oxid de titan în fibre.'), ('Material', '80% poliamidă reciclată, 20% elastan.'))
  + '<p>Mărimile 44-46 până la 52-54 sunt circumferința capului, pentru copii de la aproximativ 1 an în sus.</p>',
  [('model', 'REIMA MUSTEKALA'), ('culoare', 'Roz'), ('jerseu', 'material jerseu elastic'), ('UPF', 'Datorită protecției ridicate împotriva razelor UV (UPF 50+)'),
   ('cozoroc', 'Cozorocul moale protejează eficient ochii împotriva strălucirii'), ('gât', 'spatele extins al borului protejează zona sensibilă a gâtului'),
   ('căptușeală', 'Nu are căptușeală, astfel încât are o greutate redusă'), ('uscare', 'datorită materialului care se usucă rapid, este ideală pentru plajă, terenul de joacă'),
   ('EN', 'factor de protecție UV 50+, testat conform standardului EN 13758-1 +A1'), ('TiO2', 'protecție împotriva razelor UVA și UVB datorită TiO₂ (oxidului de titan) integrat în fibre'),
   ('material', '80% poliamidă (reciclată), 20% elastan')],
  {'Model': 'Reima MUSTEKALA', 'Material': '80% poliamidă reciclată, 20% elastan', 'Caracteristici': 'UPF 50+, protecție la gât, uscare rapidă', 'Cod produs': '278410'},
  varsta_txt='de la 1 an în sus', notes=[UV_NOTE])

w(13946,
  f'<p>Bluza cu mânecă lungă {REIMA} VIISAS e un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "tricou unisex")} în culoarea gri pe site (mix la magazin), complet imprimat, moale, călduros și plăcut la atingere, pentru purtarea de zi cu zi. Absoarbe umezeala, deci merge și înăuntru, și afară.</p>'
  '<p>Croiala e dreaptă, cu mâneci raglan, care lasă brațele libere.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '48% bumbac, 43% viscoză din bambus, 9% poliamidă.'), ('Greutate', '130 g.'), ('Mânecă', 'lungă, raglan.'))
  + '<p>Mărimile 110-164 sunt pentru copii de aproximativ 5-14 ani.</p>',
  [('model', 'REIMA VIISAS'), ('culoare', 'Mix'), ('imprimat', 'material complet imprimat'), ('moale', 'moale, călduros, foarte plăcut la atingere'),
   ('zilnic', 'este indicat pentru purtarea de zi cu zi'), ('umezeală', 'absoarbe umezeala'), ('indoor', 'orice activitate indoor și outdoor'),
   ('croială', 'croială dreaptă'), ('raglan', 'mânecă raglan'), ('mânecă', 'are mâneca lungă'), ('material', '48 % bumbac, 43 % viscoză (bambus), 9 % poliamidă'), ('greutate', '130 g')],
  {'Model': 'Reima VIISAS', 'Material': '48% bumbac, 43% viscoză din bambus, 9% poliamidă', 'Caracteristici': 'imprimeu integral, mâneci raglan', 'Cod produs': '178250'},
  notes=['Titlul spune gri, magazinul dă culoarea „Mix”.', 'Descrierea pomenește lână Merino, dar compoziția nu conține lână; am scris compoziția din specificații.'])

w(13962,
  f'<p>Pantalonii {REIMA} VIRRAT roșii sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")} de drumeție, cu crac detașabil cu fermoar, deci se fac rapid pantaloni scurți. Materialul Anti-Bite are finisajul netoxic și biodegradabil Si Repel Mosquito, care ține la distanță căpușele și țânțarii cel puțin o sută de spălări.</p>'
  '<p>Au protecție UV 50+, iar materialul stretch se usucă repede. Genunchiul e anatomic, iar talia se reglează.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Reflectorizante', 'da.'), ('Material', '100% poliester, 200 g.'))
  + '<p>Mărimile 116-164 sunt pentru copii de cam 6-14 ani.</p>',
  [('model', 'REIMA VIRRAT'), ('culoare', 'Roșu'), ('crac', 'Pantalonii pentru copii Reima VIRRAT au cracul detașabil ceea ce ajută la transformarea rapidă în pantaloni scurți'),
   ('Anti-Bite', 'Materialul Reima Anti-Bite are finisaj non-toxic și biodegradabil Si Repel Mosquito'), ('insecte', 'Acesta respinge în mod eficient căpușele, țânțarii'),
   ('spălări', 'Efectul repelent durează cel puțin o sută de cicluri de spălare'), ('UV', 'Sunt echipați cu protecție UV factor 50+'),
   ('stretch', 'Materialul stretch este foarte plăcut în contact cu pielea, este respirabil și se usucă rapid'), ('natură', 'Sunt ideali pentru plimbările în natură'),
   ('genunchi', 'genunchi anatomic'), ('talie', 'talie ajustabilă'), ('buzunare', '2 laterale cu fermoar'), ('material', '100 % poliester'), ('greutate', '200 g')],
  {'Model': 'Reima VIRRAT', 'Material': '100% poliester', 'Caracteristici': 'crac detașabil, Anti-Bite, UPF 50+', 'Cod produs': '198023'},
  notes=['Magazinul notează că insectele pot ajunge pe părțile descoperite ale corpului.'])
