import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')

w(14097,
  f'<p>Geaca de schi {A("/brand/spyder/", "Spyder")} IMPULSE albastră este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} cu umplutură din puf sintetic, bună și în oraș, și pe pârtie. Țesătura elastică Exo Shield, din poliester reciclat, are membrană și tratament DWR, coloană de apă de 10.000 mm și cusături lipite.</p>'
  '<p>Gluga e compatibilă cu casca, iar centura de zăpadă elastică oprește zăpada. Mânecile se reglează cu benzi și au manșete interioare cu orificii pentru degetul mare.</p>'
  '<p>Buzunarele și închiderea:</p>'
  + L(('Fermoar', 'YKK Arrow Vislon.'), ('Buzunare', 'pentru mâini, ski-pass, interior și pentru ochelari.'), ('Material', '55% poliester, 45% poliester reciclat.'))
  + '<p>Mărimile 10-16 sunt date în ani, deci pentru copii de aproximativ 10-16 ani.</p>',
  [('model', 'Spyder IMPULSE'), ('culoare', 'Albastru (albastru / gri / roșu)'), ('puf', 'Geaca din puf sintetic Spyder IMPULSE'), ('oraș', 'confort optim în oraș și pe pârtii'),
   ('Exo', 'țesătură elastică exo shield fabricată din poliester reciclat cu membrană și peliculă dwr'), ('coloană', '10.000 mm'), ('lipite', 'cusături lipite'),
   ('cască', 'glugă fixă compatibilă cu casca'), ('centură', 'centură de zăpadă elastică și rezistentă'),
   ('mâneci', 'mâneci reglabile cu benzi și manșete interioare elastice cu orificii pentru degetul mare'), ('YKK', 'fermoarul principal ykk® arrow vislon®'),
   ('buzunare', 'buzunar pentru permis de schi, buzunar interior și buzunar pentru ochelari de protecție din plasă'), ('mâini', 'buzunare cu fermoar pentru mâini'),
   ('material', '55 % poliester, 45 % poliester reciclat')],
  {'Model': 'Spyder IMPULSE', 'Material': 'poliester, parțial reciclat, puf sintetic', 'Caracteristici': '10.000 mm, cusături lipite, centură de zăpadă, glugă pentru cască', 'Cod produs': '157424'},
  varsta_txt='10-16 ani', notes=['Mărimile sunt date în ani (10-16).', 'Descrierea scurtă spune glugă detașabilă, lista spune glugă fixă compatibilă cu casca; n-am scris dacă se detașează.'])

w(14108,
  f'<p>Sandalele {REIMA} LOMALLA maro sunt {A("/categorie/unisex-incaltaminte-sandale/", "sandale unisex")} pentru vară, acoperite la vârf și la călcâi, bune pentru activitățile de zi cu zi. Se prind cu șireturi elastice și bandă velcro, deci se încalță repede.</p>'
  '<p>Talpa moale din Phylon e ușoară, iar căptușeala elastică e lejeră pe picior. Vârful acoperit apără degetele, iar călcâiul închis ține sandala pe picior.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Branț', 'detașabil, cu imprimeu Happy Fit.'), ('Față', 'material sintetic.'), ('Talpă', 'Phylon.'))
  + '<p>Numerele 20-26 se potrivesc copiilor de aproximativ 1-4 ani.</p>',
  [('model', 'REIMA LOMALLA'), ('culoare', 'Maro (maro / negru / alb)'), ('vară', 'model universal pentru sezonul de vară'), ('acoperit', 'Sunt acoperite în vârf și la călcâi'),
   ('zilnic', 'activităților de zi cu zi'), ('închidere', 'se încheie cu șireturi elastice și bandă velcro'), ('talpă', 'talpă moale din material Phylon'),
   ('căptușeală', 'căptușeală elastică lejeră'), ('branț', 'branț detașabil cu imprimeu Happy Fit'), ('față', 'material sintetic')],
  {'Model': 'Reima LOMALLA', 'Material': 'sintetic, talpă Phylon', 'Caracteristici': 'șireturi elastice și velcro, vârf acoperit, Happy Fit', 'Cod produs': '240080'})

w(14119,
  f'<p>Pantalonii impermeabili {REIMA} KAURA mov sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")} de ploaie, cu membrană Reimatec, 10 000 mm coloană de apă și 7000 g/m2/24 h respirabilitate, pentru primăvară și toamnă. Toate cusăturile sunt lipite și sigilate.</p>'
  '<p>Materialul rezistent respinge apa și murdăria și face față jocurilor mai dure, iar talia se reglează. Se pot usca în uscător.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'poliester neted.'), ('Reflectorizante', 'da.'), ('Material', 'poliester reciclat și poliester, laminat cu poliuretan.'))
  + '<p>Mărimile 92-140 sunt pentru copii de cam 2-10 ani.</p>',
  [('model', 'REIMA KAURA'), ('culoare', 'Mov'), ('Reimatec', 'Pantalonii impermeabili REIMA KAURA au membrană Reimatec'), ('coloană', '10 000 mm'), ('respirabilitate', '7000 g/m2/24 h'),
   ('sezon', 'Ideali pentru sezonul de primăvară și toamnă'), ('lipite', 'toate cusăturile sunt lipite și sigilate pentru impermeabilitate'), ('murdărie', 'resping apa și murdăria'),
   ('rezistent', 'material rezistent pe exterior, care face față la jocurile neglijente ale copiilor'), ('talie', 'talie ajustabilă'), ('uscător', 'se pot usca în uscător'),
   ('căptușeală', 'căptușeală din poliester neted'), ('reflectorizant', 'elemente reflectorizante'), ('material', '55 % poliester reciclat, 45 % poliester, laminare de poliuretan')],
  {'Model': 'Reima KAURA', 'Material': 'poliester parțial reciclat, laminat PU', 'Caracteristici': 'Reimatec, 10 000 mm, cusături lipite, talie reglabilă', 'Cod produs': '278373'})

w(14123,
  f'<p>Hanoracul {A("/brand/gap/", "GAP")} FASHION LOGO este listat la {A("/categorie/unisex-imbracaminte-geci-jachete/", "geci unisex")}, dar e un hanorac roz cu logo, cu decolteu rotund și mânecă lungă cu manșetă. Croiala dreaptă e comodă la purtare.</p>'
  '<p>E din bumbac cu poliester. Pagina magazinului dă puține detalii, iar produsul apare ca vândut.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '77% bumbac, 23% poliester.'), ('Decolteu', 'rotund.'), ('Mâneci', 'lungi, cu manșetă.'))
  + '<p>Mărimile, de la L la XXL, corespund de obicei copiilor mai mari, de aproximativ 10-16 ani; verificați tabelul magazinului.</p>',
  [('model', 'GAP FASHION LOGO'), ('logo', 'beneficiază de logo'), ('decolteu', 'Are un decolteu rotund'), ('mâneci', 'mânecă lungă cu manșetă'),
   ('croială', 'Croiala dreaptă este foarte confortabilă'), ('material', '77 % bumbac, 23 % poliester'), ('vândut', 'VÂNDUT')],
  {'Model': 'GAP FASHION LOGO', 'Material': '77% bumbac, 23% poliester', 'Caracteristici': 'logo, decolteu rotund, croială dreaptă', 'Cod produs': '213644'},
  varsta_txt='10-16 ani', notes=['Pagina magazinului nu dă culoarea și arată produsul ca vândut; culoarea e cea din titlu.', 'Mărimile sunt în litere (L-XXL), fără tabel; vârsta e estimată.', 'E hanorac, listat la Geci.'])

w(14134,
  f'<p>Hanoracul cu glugă {REIMA} VARMISTUS verde e un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} din tricot moale, neperiat, de bumbac organic, ușor și confortabil, pentru serile de vară. Finisajul Anti-Bite, netoxic și ecologic, ține insectele la distanță și nu irită pielea.</p>'
  '<p>Fermoarul merge pe toată lungimea, gluga e fixă, iar talia și manșetele sunt din tricot ușor elastic. Materialul e natural și parțial reciclat, deci o alegere ecologică.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două laterale.'), ('Material', '100% bumbac.'), ('Greutate', '250 g.'))
  + '<p>Mărimile 116-164 sunt pentru copii de aproximativ 6-14 ani.</p>',
  [('model', 'REIMA VARMISTUS'), ('culoare', 'Verde (verde / albastru / verde închis)'), ('organic', 'tricot moale ne periat din bumbac organic'), ('ecologic', 'Este o opțiune ecologică deoarece materialul este natural și reciclat'), ('ușor', 'are greutatea redusă și este confortabil'),
   ('seri', 'este ideal pentru serile de vară'), ('Anti-Bite', 'suprafața finisată Anti-Bite respinge insectele'), ('netoxic', 'substanța non toxică, ecologică și nu irită pielea'),
   ('fermoar', 'pe toată lungimea'), ('glugă', 'fixă'), ('talie', 'talie și manșete din tricot ușor elastic'), ('buzunare', '2 laterale'), ('material', '100 % bumbac'), ('greutate', '250 g')],
  {'Model': 'Reima VARMISTUS', 'Material': '100% bumbac organic', 'Caracteristici': 'Anti-Bite, glugă fixă, fermoar întreg', 'Cod produs': '166242'})

w(14137,
  f'<p>Salopeta softshell {REIMA} MJOSA roz, listată la {A("/categorie/unisex-imbracaminte-geci-jachete/", "geci unisex")}, e un overal complet izolat cu fleece pe interior, tratat cu Teflon EcoElite, care respinge apa și murdăria. Are 10.000 mm coloană de apă și 3.000 g/m²/24h respirabilitate.</p>'
  '<p>Fermoarul lung, cu protecție pentru bărbie, coboară în diagonală de la gât la picior, iar gluga se detașează. Partea de jos e întărită, iar benzile elastice se prind sub pantofi.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunar', 'lateral, cu fermoar.'), ('Reflectorizante', 'da.'), ('Material', '92% poliester, 8% elastan.'))
  + '<p>Mărimile 80-98 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'REIMA MJOSA'), ('culoare', 'Roz (roz / negru)'), ('overal', 'Overal softshell pentru copii'), ('fleece', 'Este complet izolată cu căptușeală din fleece'),
   ('Teflon', 'tratamentul Teflon EcoEliteTM respinge apa și murdăria'), ('coloană', '10.000 mm'), ('respirabilitate', '3.000 g/m²/24h'),
   ('fermoar', 'are un fermoar lung în față, cu o protecție pentru bărbie care se întinde în diagonală de la gât până la picior'), ('glugă', 'glugă sigură, detașabilă'),
   ('întărit', 'Cracul este întărit în partea de jos'), ('benzi', 'benzi elastice detașabile peste pantofi'), ('buzunar', '1 buzunar lateral cu fermoar'),
   ('reflectorizant', 'Beneficiază de elemente reflectorizante'), ('material', '92 % poliester, 8 % elastan')],
  {'Model': 'Reima MJOSA (overal)', 'Material': '92% poliester, 8% elastan, căptușeală fleece', 'Caracteristici': 'Teflon EcoElite, 10.000 mm, glugă detașabilă', 'Cod produs': '166215'},
  notes=['E salopetă (overal), listată la Geci.'])

w(14139,
  f'<p>Ghetele barefoot {REIMA} LOIKKII, maro după titlul de pe site, sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} impermeabili, vegani, cu membrană care ține degetele uscate și detalii reflectorizante. Drop zero și spațiul extins pentru degete lasă piciorul în poziție naturală.</p>'
  '<p>Talpa flexibilă din cauciuc ține bine pe sol, iar șireturile elastice fac încălțatul rapid. Sunt bune pentru sezoanele de tranziție, pe orice vreme.</p>'
  '<p>Din ce sunt făcute:</p>'
  + L(('Față', 'cauciuc, poliester, poliuretan.'), ('Branț', 'detașabil, cu materiale reciclate.'), ('Greutate', '440 g, fără fluorocarbon și PVC.'))
  + '<p>Numerele 32-40 se poartă de pe la 8 ani în sus.</p>',
  [('model', 'REIMA LOIKKII'), ('barefoot', 'Ghetele barefoot pentru copii Reima LOIKKII sunt impermeabile'), ('membrană', 'Au o membrană impermeabilă care menține degetele uscate'),
   ('reflectorizant', 'detalii reflectorizante pentru o vizibilitate mai bună'), ('vegan', 'vegane'), ('drop', 'drop zero pentru o poziție naturală'),
   ('degete', 'spațiul extins pentru degete'), ('talpă', 'talpa din cauciuc asigură o aderență optimă'), ('șireturi', 'se fixează cu șireturi elastice'),
   ('tranziție', 'Sunt ideale pentru sezoanele de tranziție în orice vreme'), ('față', 'cauciuc, poliester, poliuretan'), ('branț', 'branțul conține materiale reciclate'),
   ('greutate', '440 g'), ('PVC', 'fără fluorocarbon și PVC')],
  {'Model': 'Reima LOIKKII', 'Material': 'cauciuc, poliester, poliuretan', 'Caracteristici': 'barefoot, impermeabile, drop zero, șireturi elastice', 'Cod produs': '220327'},
  notes=['Pagina magazinului nu dă culoarea; culoarea e cea din titlul site-ului.', 'Magazinul le numește ghete; pe site sunt la Pantofi.'])

w(14143,
  f'<p>Ghetuțele {A("/brand/geox/", "Geox")} WILLABOOM GIRL B roz sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} cu tehnologia patentată AMPHIBIOX, cu membrană microporoasă în talpa perforată, care elimină transpirația și nu lasă apa să intre. Membrana creează un microclimat bun și ține piciorul la temperatură potrivită.</p>'
  '<p>Rezistă la apă, iar partea de sus e din poliuretan și poliamidă. Talpa e din IPEVA, iar AMPHIBIOX păstrează respirabilitatea în orice vreme.</p>'
  '<p>Din ce sunt făcute:</p>'
  + L(('Față', '50% poliuretan, 50% poliamidă.'), ('Talpă', '100% IPEVA.'), ('Tehnologie', 'AMPHIBIOX.'))
  + '<p>Numerele 20-23 se potrivesc fetițelor de aproximativ 1-3 ani.</p>',
  [('model', 'Geox WILLABOOM GIRL B'), ('culoare', 'Roz (roz / alb)'), ('AMPHIBIOX', 'Tehnologia patentată AMPHIBIOX asigură impermeabilitatea'),
   ('membrană', 'Talpa acestora este perforată și dispune de membrană specială microporoasă care absoarbe și elimină transpirația fără a permite pătrunderea apei'),
   ('microclimat', 'Membrana special impermeabilă asigură piciorului un micro climat de înaltă calitate'), ('termic', 'garantează respirabilitatea și confortul termic'),
   ('apă', 'membrană rezistentă la apă'), ('vreme', 'garantând totodată o respirabilitate persistentă, în orice vreme'), ('față', '50 % poliuretan, 50 % poliamidă'), ('talpă', '100 % IPEVA')],
  {'Model': 'Geox WILLABOOM GIRL B', 'Material': 'poliuretan și poliamidă, talpă IPEVA', 'Caracteristici': 'AMPHIBIOX, membrană microporoasă', 'Cod produs': '166011'},
  notes=['Magazinul le numește ghete; pe site sunt la Pantofi. Pagina nu spune tipul de închidere.'])

w(14184,
  f'<p>Geaca {A("/brand/klimatex/", "Klimatex")} GULI verde deschis este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} ultraușoară, de 75 g, gândită pentru ciclism ca al treilea strat de urgență, care încape în buzunarul tricoului. Materialul dens oprește vântul, iar tratamentul o face rezistentă la apă pe ploaie.</p>'
  '<p>Fermoarul e acoperit și are protecție pentru bărbie, iar mânecile și tivul au elastic. Merge și pentru alte sporturi, nu doar pentru bicicletă.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Interior', 'tricotaj cu plasă funcțională.'), ('Reflectorizante', 'da.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 110-158 sunt pentru copii de cam 5-13 ani.</p>',
  [('model', 'Klimatex GULI'), ('culoare', 'Verde deschis (verde deschis / albastru'), ('ușor', 'Geaca ultra ușoară de copii Klimatex GULI'), ('strat', 'este adecvată ca al treilea strat de urgență'),
   ('buzunar', 'Se poate transporta ușor în buzunarul de la tricoul de ciclism'), ('ciclism', 'Este o geacă special creată pentru ciclism, dar poate fi purtată și pentru alte activități sport'), ('vânt', 'Datorită materialului dens, protejează împotriva vântului'),
   ('apă', 'Dispune de tratament pentru rezistență la apă'), ('fermoar', 'fermoar acoperit'), ('bărbie', 'protecție la bărbie'), ('elastic', 'mânecile și partea de jos sunt cu elastic'),
   ('reflectorizant', 'elemente reflectorizante'), ('interior', 'pe interior are tricotaj cu plasă funcțională'), ('material', '100% poliamidă'), ('greutate', '75 g')],
  {'Model': 'Klimatex GULI', 'Material': '100% poliamidă', 'Caracteristici': 'ultraușoară, rezistentă la vânt și apă, reflectorizante', 'Cod produs': '7641003292'})

w(14187,
  f'<p>Geaca de iarnă {A("/brand/alpine-pro/", "ALPINE PRO")} NALANO roz este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} din material cald, impermeabil și rezistent la vânt, cu tratament DWR, umplutură densă, extrem de ușoară, și căptușeală călduroasă. Materialul multicolor are imprimeu în față și un element decorativ pe mânecă.</p>'
  '<p>Gluga are căptușeală caldă și protecție pentru bărbie, iar fermoarul are cursoare lungi, ușor de prins.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Mâneci', 'cu tiv elastic.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-110 până la 152-158 sunt pentru copii de aproximativ 4-13 ani.</p>',
  [('model', 'ALPINE PRO NALANO'), ('culoare', 'Roz (roz / mov)'), ('iarnă', 'Geaca de iarnă pentru copii ALPINE PRO NALANO'), ('material', 'material impermeabil, permeabil la vapori, rezistent la vânt, călduros'),
   ('DWR', 'material cu tratament DWR'), ('umplutură', 'Umplutura extrem de ușoară este călduroasă'), ('căptușeală', 'căptușeală călduroasă'),
   ('multicolor', 'materialul multicolor se remarcă'), ('imprimeu', 'imprimeu în partea din față'), ('mânecă', 'element decorativ pe mânecă'),
   ('glugă', 'glugă detașabilă cu căptușeală din material călduros'), ('bărbie', 'protecție pentru bărbie'), ('cursoare', 'cursoare mai lungi pentru manipulare mai ușoară'),
   ('buzunare', '2 (2x laterale cu fermoar)'), ('mâneci', 'mâneci cu tiv cu elastic'), ('poliester', '100 % poliester')],
  {'Model': 'ALPINE PRO NALANO', 'Material': '100% poliester, umplutură densă', 'Caracteristici': 'DWR, glugă cu căptușeală, protecție la bărbie', 'Cod produs': '146074'},
  notes=['Descrierea scurtă spune glugă fixă, lista spune glugă detașabilă; n-am scris dacă se detașează.'])
