import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
MAXCO = A('/brand/maxco/', 'Max&amp;Co.')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
GU = '/categorie/unisex-imbracaminte-geci-jachete/'
ITAL = 'Mărimile sunt italienești, convertite la cele europene, deci merită verificat tabelul magazinului.'

w(10436,
  f'<p>Geaca de tranziție {REIMA} Salmi bej este o {A(GU, "geacă unisex")} ușoară, neizolată, cu membrană TPU și cusături sudate, care apără de ploaie și vânt. Coloana de apă e de 10 000 mm H₂O, iar respirabilitatea de 7000 g/m²/24h, deci umezeala de pe piele iese afară.</p>'
  '<p>Materialul e rezistent la murdărie, croiala e dreaptă, până la șold, iar gluga se detașează. Manșetele sunt elastice, tivul se reglează, buzunarele laterale se închid, iar căptușeala e din plasă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester, strat TPU.'), ('Izolație', 'nu are.'), ('Sezon', 'primăvară, vară, toamnă.'))
  + '<p>Mărimile 104-164 se potrivesc pe la 4-14 ani.</p>',
  [('model', 'Salmi'), ('culoare', 'Culoare bej'), ('tranziție', 'geacă de tranziție ușoară'), ('TPU', 'Membrană TPU'), ('sudate', 'Cusături sudate impermeabil'),
   ('vânt', 'Construcție rezistentă la vânt'), ('coloană', 'Impermeabilitate de 10 000 mm H₂O'), ('respirabil', 'Respirabilitate de 7000 g/m²/24h'),
   ('murdărie', 'Material rezistent la murdărie'), ('dreaptă', 'Croială dreaptă'), ('șold', 'Lungime până la șolduri'), ('glugă', 'Glugă detașabilă'),
   ('manșete', 'Manșete elastice'), ('tiv', 'Tiv reglabil'), ('buzunare', 'Buzunare laterale cu închidere'), ('plasă', 'Căptușeală din plasă'),
   ('material', 'Material de bază:100% Poliester'), ('izolație', 'fără izolație'), ('sezon', 'primăvară, vară și toamnă')],
  {'Model': 'Reima Salmi', 'Material': '100% poliester, membrană TPU', 'Caracteristici': '10 000 mm, cusături sudate, glugă detașabilă', 'Cod produs': '5100432A'})

w(10458,
  f'<p>Geaca bomber {A("/brand/karl-lagerfeld/", "Karl Lagerfeld")} Z30568 bej este o {A(GB, "geacă de tranziție pentru băieți")} neizolată, din material textil cu aplicație, cu căptușeală din poliester și viscoză. Poliesterul o face rezistentă la îndoire.</p>'
  '<p>Se închide cu cleme, buzunarele exterioare sunt oblice, iar mânecile și marginea de jos au bătături, ca la orice bomber. Nu are glugă și nu e impermeabilă. ' + ITAL + '</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', '53% poliester, 47% viscoză.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 162-174 corespund orientativ vârstei de 14-16 ani.</p>',
  [('cod', 'Z30568'), ('culoare', 'culoarea bej'), ('bomber', 'Geacă bomber pentru copii din colecția Karl Lagerfeld'), ('neizolat', 'Model neizolat confecționat din din material textil cu aplicatie'),
   ('căptușeală', '53% Poliester , 47% Viscoza'), ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'), ('cleme', 'Incheiere cu cleme'),
   ('buzunare', 'Buzunare oblice exterioare'), ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('glugă', 'fără glugă'),
   ('impermeabil', 'fără impermeabilitate'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '100% Poliester'), ('croială', 'Croială: regular fit')],
  {'Model': 'Karl Lagerfeld Z30568', 'Material': '100% poliester', 'Caracteristici': 'bomber, aplicație, cleme', 'Cod produs': 'Z30568'})

w(10482,
  f'<p>Geaca bomber {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KB0KB10079 bleumarin este o {A(GB, "geacă subțire pentru băieți")}, neizolată, din material neted, realizată pe jumătate din poliester reciclat. Are căptușeală completă, sintetică, și nu are glugă.</p>'
  '<p>Tăietura e simplă, se încheie cu cleme, iar mânecile sunt finisate cu manșetă. E o geacă ușoară, pentru zilele mai blânde de primăvară sau toamnă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '50% poliester, 50% poliester reciclat.'), ('Umplutură', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 128-176 merg cam la 8-16 ani.</p>',
  [('cod', 'KB0KB10079'), ('culoare', 'culoarea bleumarin'), ('bomber', 'Geacă bomber pentru copii din colecția Tommy Hilfiger'), ('neizolat', 'Model neizolat confecționat din material neted'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('glugă', 'fără glugă'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('cleme', 'Incheiere cu cleme'), ('manșetă', 'Finisaj din manseta'), ('material', '50% Poliester , 50% Poliester reciclat'),
   ('umplutură', 'fără umplutură'), ('croială', 'Croială: regular fit')],
  {'Model': 'Tommy Hilfiger KB0KB10079', 'Material': 'poliester, parțial reciclat', 'Caracteristici': 'bomber, neizolată, cleme', 'Cod produs': 'KB0KB10079'},
  notes=['„Primăvară sau toamnă” e dedus din „neizolat”.'])

w(10487,
  f'<p>Jacheta matlasată {A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 313B15070001 roz este o {A(GF, "geacă de tranziție pentru fete")}, din nailon, cu izolație sintetică ușoară pentru zilele mai reci. Țesătura matlasată e durabilă, iar căptușeala completă ajută la îmbrăcat peste alte haine.</p>'
  '<p>Nu are glugă, are guler clasic și mâneci clasice, iar lungimea ajunge până la șold. Se închide cu fermoar, iar în față are buzunare. Magazinul precizează că nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% nailon.'), ('Umplutură', '100% poliester.'), ('Croială', 'regular fit.'))
  + '<p>Între 130-134 și 155-159, vârsta e cam de 8-13 ani.</p>',
  [('cod', '313B15070001'), ('culoare', 'Culoare roz'), ('matlasat', 'Țesătură matlasată durabilă'), ('ușoară', 'Izolație sintetică ușoară'), ('reci', 'zilele mai reci ale sezonului de tranziție'),
   ('căptușeală', 'Căptușeală completă'), ('peste', 'facilitează îmbrăcarea peste alte haine'), ('glugă', 'Fără glugă'), ('guler', 'Guler clasic'),
   ('mâneci', 'Croială clasică a mânecilor'), ('șold', 'Lungime până la șolduri'), ('fermoar', 'Sistem de închidere cu fermoar'), ('buzunare', 'Buzunare practice în față'),
   ('impermeabil', 'fără impermeabilitate'), ('material', 'Material principal:100% Nailon'), ('umplutură', 'Umplutură:100% Poliester'), ('croială', 'Croială: regular fit')],
  {'Model': 'Polo Ralph Lauren 313B15070001', 'Material': '100% nailon', 'Caracteristici': 'matlasată, izolație ușoară, guler clasic', 'Cod produs': '313B15070001'})

w(10492,
  f'<p>Paltonul {MAXCO} MAXJ1F JACKET roșu, listat la {A(GF, "geci pentru fete")}, e făcut din lână 100%, un material neted care ajută la termoreglare: ține de cald la frig și nu încălzește prea tare când e cald. Modelul e neizolat, cu design simplu.</p>'
  '<p>Se închide cu nasturi, are revere clasice, două buzunare în față și o curea textilă atașată. Magazinul precizează că nu e impermeabil. ' + ITAL + '</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% lână.'), ('Închidere', 'nasturi.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 156-175 țin orientativ de vârsta 13-16 ani.</p>',
  [('cod', 'MAXJ1F'), ('culoare', 'Culoare rosu'), ('lână', '100% Lână'), ('termoreglare', 'Proprietățile ridicate de termoreglare ale lânii'), ('neted', 'confecționat dintr-un material neted'),
   ('neizolat', 'Acest model neizolat'), ('simplu', 'Design simplu și ușor de purtat'), ('nasturi', 'Închiderea convenabilă cu nasturi'), ('revere', 'Revere clasice'),
   ('buzunare', 'Două buzunare frontale'), ('curea', 'Curea textilă atașată'), ('impermeabil', 'fără impermeabilitate'),
   ('italian', 'Mărimile disponibile sunt convertite din sistemul italian'), ('croială', 'Croială: regular fit')],
  {'Model': 'Max&Co. MAXJ1F', 'Material': '100% lână', 'Caracteristici': 'palton, nasturi, curea textilă', 'Cod produs': 'MX0001.MX052'},
  notes=['Titlul site-ului are „JACKET” în locul culorii; culoarea e cea de la magazin (roșu).', 'Descrierea spune „fără căptușeală”, caracteristicile „căptușeală sintetică”; nu am scris despre căptușeală.'])

w(10528,
  f'<p>Geaca 3 în 1 {A("/brand/jack-wolfskin/", "Jack Wolfskin")} CANVEY KIDS bleumarin este o {A(GU, "geacă unisex")} izolată, cu izolație sintetică medie spre groasă și material TEXAPORE: exterior durabil, hidrofug, cu membrană impermeabilă și strat PU pe interior. E rezistentă la vânt și respirabilă.</p>'
  '<p>Gluga e încorporată, fermoarul pe toată lungimea are clapă rezistentă la vânt, cu capse, iar elementele reflectorizante se văd după lăsarea întunericului. E produsă după principiile Fair Wear și conține fibre reciclate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două laterale.'), ('Material', '100% poliester.'), ('Căptușeală', 'completă, sintetică.'))
  + '<p>Mărimile 116-152 se potrivesc, cu aproximație, la 6-12 ani.</p>',
  [('model', '3IN1 CANVEY KIDS'), ('culoare', 'culoarea bleumarin'), ('izolat', 'Model izolat confecționat din material neted cu izolatie sintetica'), ('groasă', 'medie, groasă'),
   ('TEXAPORE', 'Materialul TEXAPORE este impermeabil, rezistent la vant si respirabil'), ('PU', 'o membrană impermeabilă sau un strat PU pe interior'),
   ('glugă', 'Gluga încorporată'), ('fermoar', 'Închidere cu fermoar pe toată lungimea, cu clapă rezistentă la vânt, cu capse'),
   ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea după lăsarea întunericului'), ('Fair Wear', 'Fair Wear Foundation'),
   ('reciclat', 'Produsul contine materiale realizate din fibre reciclate'), ('buzunare', 'Două buzunare laterale'), ('material', '100% Poliester'),
   ('căptușeală', 'cu căptușeală completă, sintetică')],
  {'Model': 'Jack Wolfskin 3IN1 CANVEY KIDS', 'Material': '100% poliester, TEXAPORE', 'Caracteristici': '3 în 1, membrană, reflectorizante', 'Cod produs': 'A65315'},
  notes=['Numele spune „3 în 1”, dar magazinul nu descrie cum se separă straturile; nu am detaliat.'])

w(10539,
  f'<p>Geaca {MAXCO} MAXJ49F JACKET albastră este o {A(GF, "geacă subțire pentru fete")}, ușor izolată, din nailon neted, cu căptușeală completă. Poliamida o face mai durabilă.</p>'
  '<p>Are guler moale, fără glugă, și se închide cu capse, deci se pune și se scoate ușor. Manșetele mânecilor se încheie. Croiala e simplă. ' + ITAL + '</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% nailon.'), ('Izolație', 'ușoară.'), ('Închidere', 'capse.'))
  + '<p>Mărimile 156-172 corespund cam vârstei de 13-15 ani.</p>',
  [('cod', 'MAXJ49F'), ('culoare', 'Culoare albastru'), ('subțire', 'Model subțire confecționat din țesătură netedă'), ('ușor', 'Izolare: usor izolat'),
   ('căptușeală', 'cu căptușeală completă'), ('poliamidă', 'Poliamida asigură o durabilitate mai mare'), ('guler', 'Model cu guler moale'), ('glugă', 'fără glugă'),
   ('capsă', 'Închiderea convenabilă cu capsă'), ('manșete', 'Maneci cu mansete incheiate'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '100% Nailon'), ('ușoară', 'ușoară')],
  {'Model': 'Max&Co. MAXJ49F', 'Material': '100% nailon', 'Caracteristici': 'subțire, guler moale, capse', 'Cod produs': 'MX0276.MX099'},
  notes=['Titlul site-ului are „JACKET” în locul culorii; culoarea e cea de la magazin (albastru).'])

w(10553,
  f'<p>Geaca bomber {A("/brand/diesel/", "Diesel")} JSTART JACKET neagră este o {A(GB, "geacă de tranziție pentru băieți")} subțire, din poliamidă cu broderie decorativă, cu căptușeală sintetică. Tăietura e lejeră, iar mânecile și marginea de jos se termină cu o bandă elastică.</p>'
  '<p>Se încheie cu cleme, iar în față are buzunare. Nu are glugă. E o geacă pentru zilele mai blânde, peste un tricou sau o bluză.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Bandă elastică', '98% poliester, 2% elastan.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 156-175 țin cam de vârsta 13-16 ani.</p>',
  [('model', 'JSTART JACKET'), ('culoare', 'culoarea negru'), ('bomber', 'Geaca bomber pentru copii din colectia Diesel'), ('subțire', 'Model subtire confectionat din material cu broderie decorativă'),
   ('căptușeală', 'Model cu captuseala'), ('lejeră', 'Tăiere lejeră, fără blocare'), ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'),
   ('cleme', 'Incheiere cu cleme'), ('buzunare', 'In fata buzunare'), ('glugă', 'fără glugă'), ('material', '100% Poliamida'), ('bandă', '98% Poliester , 2% Elastan'),
   ('croială', 'Croială: regular fit')],
  {'Model': 'Diesel JSTART JACKET', 'Material': '100% poliamidă', 'Caracteristici': 'bomber, broderie, cleme', 'Cod produs': 'J02185'},
  notes=['„Peste un tricou sau o bluză” e dedus din „model subțire”.'])

w(10573,
  f'<p>Pantalonii de schi {REIMA} Vuonelo roz sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni unisex")} izolați, cu membrană ReimaTec și finisaj BIONIC-FINISH ECO, care apără de ploaie și vânt. Coloana de apă e de 10000 mm, respirabilitatea de 7000 g/m2/24h, iar produsul are certificare Bluesign.</p>'
  '<p>Talia e înaltă și se reglează, cracul e drept, iar căptușeala e din poliester parțial reciclat. Materialul e neelastic, din pânză uni.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Căptușeală', '55% poliester reciclat, 45% poliester.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 104-164 se potrivesc orientativ între 4 și 14 ani.</p>',
  [('model', 'Vuonelo'), ('culoare', 'culoarea roz'), ('schi', 'Pantaloni de schi copii din colectia Reima'), ('izolat', 'Model izolat cu captuseala'),
   ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('coloană', 'Impermeabilitate: 10000 mm/m2/24h'),
   ('respirabil', 'Respirabilitate: 7000 g/m2/24h'), ('Bluesign', 'Model certificat Bluesign® Standard'), ('talie', 'Talie reglabilă'), ('înalt', 'Brâu: înalt'),
   ('drept', 'Tip de picior de pantalon: drept'), ('căptușeală', '55% Poliester reciclat, 45% Poliester'), ('neelastic', 'neelastic'), ('uni', 'Model: uni'),
   ('material', '100% Poliester reciclat'), ('croială', 'Croială: regular fit')],
  {'Model': 'Reima Vuonelo', 'Material': '100% poliester reciclat', 'Caracteristici': 'ReimaTec, 10000 mm, talie reglabilă', 'Cod produs': '5100394A'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(10632,
  f'<p>Geaca {A("/brand/bobo-choses/", "Bobo Choses")} Modern 126AC151 albastră (multicoloră la producător) este o {A(GU, "geacă unisex")} ușoară, neizolată, din poliamidă în mai multe culori, cu căptușeală completă. Croiala e supradimensionată, lejeră, cu umeri coborâți.</p>'
  '<p>Gulerul ridicat apără de frig, fermoarul are protecție pentru bărbie, iar mânecile și marginea de jos au tiv elastic, ca geaca să stea bine pe corp. Pe laterale are două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Căptușeală', '100% poliester.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 89/98 până la 149/155 acoperă cu aproximație 1-12 ani.</p>',
  [('model', 'Modern'), ('cod', '126AC151'), ('culoare', 'Culoare albastru'), ('multicolor', '991.MULTIC'), ('ușor', 'Model ușor confecționat din stofă in diferite culori'),
   ('neizolat', 'Izolare: neizolat'), ('căptușeală', 'cu căptușeală completă'), ('supradimensionat', 'Croială: supradimensionat'), ('lejeră', 'Tăiere lejeră'),
   ('umeri', 'linie coborâtă a umerilor'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('fermoar', 'Inchidere cu fermoar echipat cu barbie'),
   ('tiv', 'Mânecile și marginea inferioară sunt finisate cu un tiv elastic'), ('buzunare', 'Două buzunare laterale'), ('material', '100% Poliamida'),
   ('poliester', '100% Poliester'), ('glugă', 'fără glugă')],
  {'Model': 'Bobo Choses Modern', 'Material': '100% poliamidă', 'Caracteristici': 'oversize, neizolată, guler ridicat', 'Cod produs': '126AC151'},
  notes=['Titlul site-ului are „Modern” în locul culorii; magazinul dă „albastru”, producătorul „MULTIC”. Produsul e marcat și „pentru bebe”.'])
