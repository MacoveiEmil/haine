import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

KL = A('/brand/karl-lagerfeld/', 'Karl Lagerfeld')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
KS = A('/brand/konges-slojd/', 'Konges Sløjd')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
ITAL = 'Mărimile sunt italienești, raportate la cele europene, deci merită verificat tabelul magazinului.'

w(10667,
  f'<p>Geaca de blugi {A("/brand/emporio-armani/", "Emporio Armani")} EB001254 albastră este o {A(GB, "geacă de tranziție pentru băieți")} din denim de bumbac, neizolată și fără căptușeală, cu țesătură ornamentată. Are guler și se încheie cu nasturi.</p>'
  '<p>Tăietura e simplă, iar pe laterale are două buzunare. Magazinul precizează că nu e impermeabilă, deci e o geacă pentru zilele uscate. ' + ITAL + '</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Lungime', '61 cm la mărimea 176.'), ('Lățime la umeri', '44 cm.'))
  + '<p>Singura mărime, 164, se potrivește orientativ pe la 13-14 ani.</p>',
  [('cod', 'EB001254'), ('culoare', 'Culoare albastru'), ('denim', 'Model neizolat confecționat din denim de bumbac'), ('căptușeală', 'Model neizolat fara captuseala'),
   ('ornament', 'Tesatura ornamentata'), ('guler', 'Model cu guler'), ('nasturi', 'Incheiere cu nasturi'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('buzunare', 'Două buzunare laterale'), ('impermeabil', 'fără impermeabilitate'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'),
   ('material', '100% Bumbac'), ('lungime', 'Lungimea: 61 cm'), ('mărime', '176 cm'), ('umeri', 'Latimea in umeri: 44 cm')],
  {'Model': 'Emporio Armani EB001254', 'Material': '100% bumbac (denim)', 'Caracteristici': 'denim, guler, nasturi', 'Cod produs': 'EB001254'},
  notes=['Titlul site-ului are „blugi” în locul culorii; culoarea e cea de la magazin (albastru).', 'Măsurătorile magazinului sunt date pentru mărimea 176, dar pe site e doar 164.'],
  varsta_txt='13-14 ani')

w(10681,
  f'<p>Geaca de ploaie {A("/brand/reima/", "Reima")} Soukka violet este o {A(GF, "geacă de tranziție pentru fete")} fără izolație, deci ușoară și bună de purtat și în zilele mai calde. Toate cusăturile sunt sudate, membrana TPU ține apa afară, cu 10 000 mm H2O, iar respirabilitatea ajunge la 7000 g/m²/24h.</p>'
  '<p>Gluga detașabilă vine cu guler înalt, buzunarele sunt deschise sau cu fermoar, iar tivul de jos se strânge cu șnur elastic și opritoare. Manșetele sunt elastice, croiala e dreaptă, iar căptușeala din plasă lasă aerul să circule.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester, strat TPU.'), ('Sezon', 'primăvară, vară, toamnă.'), ('Lungime', 'până la șold.'))
  + '<p>Mărimile 92-110 merg cu aproximație la 2-5 ani.</p>',
  [('model', 'Soukka'), ('culoare', 'Culoare violet'), ('ploaie', 'Geaca de ploaie mov Reima'), ('izolație', 'Lipsa izolației termice'), ('calde', 'permițând purtarea în zilele mai calde'),
   ('sudate', 'Toate cusăturile sudate impermeabil'), ('TPU', 'Membrana TPU'), ('coloană', 'Impermeabilitate de 10 000 mm H2O'), ('respirabil', 'Respirabilitate de 7000 g/m²/24h'),
   ('glugă', 'Gluga detașabilă cu guler înalt'), ('buzunare', 'Buzunarele practice, deschise și cu fermoar'), ('tiv', 'Tivul inferior cu șnur elastic și opritoare'),
   ('manșete', 'Manșetele elastice'), ('dreaptă', 'Croiala dreaptă'), ('plasă', 'Căptușeala din plasă'), ('material', 'Material de bază:100% Poliester'),
   ('sezon', 'primăvară, vară și toamnă'), ('șold', 'Lungimea până la șolduri')],
  {'Model': 'Reima Soukka', 'Material': '100% poliester, membrană TPU', 'Caracteristici': '10 000 mm, cusături sudate, glugă detașabilă', 'Cod produs': '5100429B'})

w(10695,
  f'<p>Geaca {A("/brand/liewood/", "Liewood")} Anemone Long Jacket bleumarin este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} lungă, ușor izolată, din material ornamentat, din poliester reciclat certificat GRS. Căptușeala e completă, sintetică.</p>'
  '<p>Se închide cu fermoar, deci se pune și se scoate ușor, iar mânecile sunt finisate cu manșetă. Elementele reflectorizante o fac mai vizibilă după lăsarea întunericului. Tăietura e simplă, fără blocare, iar izolația ușoară o face potrivită pentru zilele răcoroase.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Umplutură', '100% poliester.'), ('Izolație', 'ușoară.'))
  + '<p>Între 98 și 140, mărimile acoperă cam 3-10 ani.</p>',
  [('model', 'Anemone Long Jacket'), ('culoare', 'culoarea bleumarin'), ('izolat', 'Model ușor izolat confecționat din material ornamentat'), ('GRS', 'GRS (Global Recycle Standard)'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('manșetă', 'Finisaj din manseta'),
   ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('material', '100% Poliester reciclat'), ('umplutură', '100% Poliester'), ('ușoară', 'ușoară')],
  {'Model': 'Liewood Anemone Long Jacket', 'Material': '100% poliester reciclat', 'Caracteristici': 'lungă, ușor izolată, reflectorizante', 'Cod produs': 'LW20194'},
  notes=['Atributele spun „cu glugă”, caracteristicile „fără glugă”; nu am scris despre glugă. Culoarea producătorului e „Cherr...”, magazinul dă bleumarin.'])

w(10710,
  f'<p>Puloverul {TH} KG0KG08922 bej este din {A("/categorie/bluze-tricouri-hanorace/", "bluzele pentru fete")}, tricotat din bumbac reciclat 100%, cu model ornamentat și grosime medie. Fibrele vin din procese de producție durabile, iar materialul e foarte plăcut la purtare.</p>'
  '<p>Tăietura e lejeră, decolteul e clasic, rotund, iar mânecile și marginea de jos se termină cu o bandă elastică. Tricotul are o grosime medie, nici prea subțire, nici prea gros.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac reciclat.'), ('Tricot', 'grosime medie.'), ('Decolteu', 'rotund.'))
  + '<p>Mărimile 128-176 sunt potrivite orientativ între 8 și 16 ani.</p>',
  [('cod', 'KG0KG08922'), ('culoare', 'culoarea bej'), ('tricot', 'confecționat din tricot ornamentat'), ('bumbac', 'material bumbac extrem de confortabil'),
   ('durabil', 'produse folosind procese de productie durabile'), ('lejeră', 'Tăiere lejeră, fără blocare'), ('decolteu', 'Decolteu clasic, rotund'),
   ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('material', '100% Bumbac reciclat'), ('grosime', 'Tricotaje: grosime medie')],
  {'Model': 'Tommy Hilfiger KG0KG08922', 'Material': '100% bumbac reciclat', 'Caracteristici': 'tricot ornamentat, decolteu rotund', 'Cod produs': 'KG0KG08922'},
  notes=[])

w(10712,
  f'<p>Geaca {KL} Z31072 bej este o {A(GB, "geacă subțire pentru băieți")} din bumbac 100% cu imprimeu, moale și plăcută la atingere, neizolată și fără căptușeală. Are guler, fără glugă.</p>'
  '<p>Se închide cu fermoar, buzunarele sunt decorate cu clape, iar manșetele mânecilor se încheie. Tăietura e simplă, potrivită pentru zilele calde de primăvară. ' + ITAL + '</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Umplutură', 'nu are.'), ('Căptușeală', 'nu are.'))
  + '<p>Mărimile 114-150 țin cam de vârsta 6-12 ani.</p>',
  [('cod', 'Z31072'), ('culoare', 'culoarea bej'), ('imprimeu', 'Model confecționat din material textil cu imprimeu'), ('moale', 'material moale și plăcut la atingere'),
   ('neizolat', 'Izolare: neizolat'), ('căptușeală', 'fără căptușeală'), ('guler', 'Model cu guler'), ('glugă', 'fără glugă'), ('fermoar', 'Incheiere cu fermoar'),
   ('clape', 'Model cu buzunare, decorat cu clape'), ('manșete', 'Maneci cu mansete incheiate'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '100% Bumbac'), ('umplutură', 'fără umplutură')],
  {'Model': 'Karl Lagerfeld Z31072', 'Material': '100% bumbac', 'Caracteristici': 'imprimeu, fermoar, buzunare cu clape', 'Cod produs': 'Z31072'},
  notes=['„Zilele calde de primăvară” e dedus din „neizolat, fără căptușeală”.'])

w(10942,
  f'<p>Geaca de blugi {KL} Z31133 albă este o {A(GF, "geacă de blugi pentru fete")}, din țesătură netedă de bumbac cu puțin elastan, de calitate și durabilă. E neizolată și fără căptușeală, cu guler moale.</p>'
  '<p>Se închide cu fermoar, manșetele moi au nasturi, iar buzunarele sunt patru: două laterale și două la piept. Are detalii decorative și nu e impermeabilă. ' + ITAL + '</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '98% bumbac, 2% elastan.'), ('Glugă', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 156-162 corespund aproximativ vârstei de 13-14 ani.</p>',
  [('cod', 'Z31133'), ('culoare', 'culoarea alb'), ('netedă', 'Model confecționat din țesătură netedă'), ('durabil', 'material de înaltă calitate, durabil'),
   ('neizolat', 'Izolare: neizolat'), ('căptușeală', 'fără căptușeală'), ('guler', 'Model cu guler moale'), ('fermoar', 'Incheiere cu fermoar'),
   ('manșete', 'Manșete moi cu închidere cu nasturi'), ('buzunare', 'Două buzunare laterale și două buzunare la piept'), ('decorativ', 'Detalii decorative'),
   ('impermeabil', 'fără impermeabilitate'), ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '98% Bumbac, 2% Elastan'),
   ('glugă', 'fără glugă'), ('croială', 'Croială: regular fit')],
  {'Model': 'Karl Lagerfeld Z31133', 'Material': '98% bumbac, 2% elastan', 'Caracteristici': 'blugi, 4 buzunare, manșete cu nasturi', 'Cod produs': 'Z31133'})

w(11012,
  f'<p>Cardiganul {TH} KG0KG09378 alb e printre {A("/categorie/bluze-tricouri-hanorace/", "bluzele pentru fete")}: un pulover cu nasturi din bumbac pur, cu împletitură torsadată și ajurată. E un strat aerisit, cu croială lejeră, supradimensionată, și umeri căzuți.</p>'
  '<p>Bumbacul e plăcut la atingere și lasă pielea să respire, iar materialul elastic urmează silueta. Decolteul e rotund, manșetele și tivul striate își păstrează forma, iar pe piept e brodat steagul Tommy Hilfiger.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Închidere', 'nasturi.'), ('Mânecă', 'lungă.'))
  + '<p>Mărimile 128-176 merg cam la 8-16 ani.</p>',
  [('cod', 'KG0KG09378'), ('culoare', 'Culoare alb'), ('nasturi', 'este un pulover cu nasturi'), ('bumbac', 'confecționarea sa din bumbac pur'),
   ('torsadat', 'Împletitura torsadată și ajurată'), ('aerisit', 'strat aerisit'), ('lejeră', 'Croiala lejeră cu umerii căzuți'), ('supradimensionat', 'Croială: supradimensionat'),
   ('respire', 'permite pielii să respire'), ('elastic', 'Materialul elastic'), ('decolteu', 'Decolteul rotund'), ('striate', 'Manșetele și tivul striate'),
   ('steag', 'Steagul Tommy Hilfiger brodat pe piept'), ('material', 'Material principal:100% Bumbac'), ('mânecă', 'Mânecă: lungă')],
  {'Model': 'Tommy Hilfiger KG0KG09378', 'Material': '100% bumbac', 'Caracteristici': 'cardigan, împletitură torsadată, nasturi', 'Cod produs': 'KG0KG09378'})

w(11218,
  f'<p>Bluza {KS} LOUMILLA SWEAT SHIRT albastră este printre {A("/categorie/bebe-imbracaminte-bluze-tricouri-hanorace/", "bluzele pentru bebeluși")}, din tricot cu imprimeu și mult bumbac organic, foarte confortabil. Fibra are decorațiuni cu paiete.</p>'
  '<p>Croiala e lejeră, cu umerii lăsați și decolteu rotund, fără glugă. Mânecile și marginea de jos se termină cu o bandă elastică confortabilă, ca bluza să stea bine pe corp.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '75% bumbac organic, 25% poliester.'), ('Decolteu', 'rotund.'), ('Model', 'imprimeu cu paiete.'), ('Glugă', 'nu are.'))
  + '<p>De la 80 la 134-140, mărimile acoperă orientativ 1-10 ani.</p>',
  [('model', 'LOUMILLA SWEAT SHIRT'), ('culoare', 'Culoare albastru'), ('tricot', 'confecționat din tricot cu imprimeu'), ('bumbac', 'conținut ridicat de bumbac'),
   ('paiete', 'Fibra decorata cu paiete'), ('lejeră', 'Croială lejeră'), ('umeri', 'Linia umerilor lasata'), ('decolteu', 'Decolteu rotund'), ('glugă', 'fără glugă'),
   ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('material', '75% Bumbac organic, 25% Poliester')],
  {'Model': 'Konges Sløjd LOUMILLA SWEAT SHIRT', 'Material': '75% bumbac organic, 25% poliester', 'Caracteristici': 'imprimeu, paiete, croială lejeră', 'Cod produs': 'KS104948'},
  notes=['Titlul site-ului are „SWEAT” în locul culorii; culoarea e cea de la magazin (albastru).'])

w(11244,
  f'<p>Geaca {A("/brand/didriksons/", "Didriksons")} NEPTUN KIDS JKT 4 roșie pe site (albastră la magazin) este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, cu umplutură sintetică medie spre groasă. Materialul exterior rezistă la vânt și apă, cu 10000 mm coloană de apă și 4 000 g/m2/24h respirabilitate.</p>'
  '<p>Gluga se detașează, gulerul e ridicat, iar fermoarul are clapă de furtună cu capse. Mânecile se reglează cu velcro și au manșete elastice cu găuri pentru degetul mare. Spatele e mai lung, iar reflectorizantele ajută seara.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Material', '100% poliamidă.'), ('Umplutură', '100% poliester.'))
  + '<p>Mărimile 90-140 se potrivesc cu aproximație la 2-10 ani.</p>',
  [('model', 'NEPTUN KIDS JKT 4'), ('culoare', 'Culoare albastru'), ('izolat', 'Model izolat'), ('groasă', 'medie, groasă'), ('vânt', 'Materialul exterior este rezistent la vânt și apă'),
   ('coloană', 'Impermeabilitate: 10000 mm'), ('respirabil', 'Respirabilitate: 4 000 g/m2/24h'), ('glugă', 'Gulerul ridicat și gluga detașabilă'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă de furtună prinsă cu capse'), ('velcro', 'Marginile inferioare ale mânecilor sunt reglabile cu Velcro'),
   ('degetul', 'Manșete elastice cu găuri pentru degetul mare'), ('spate', 'Spatele mai lung'), ('reflectorizant', 'Elementele reflectorizante'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material', '100% Poliamida'), ('umplutură', '100% Poliester')],
  {'Model': 'Didriksons NEPTUN KIDS JKT 4', 'Material': '100% poliamidă', 'Caracteristici': '10000 mm, glugă detașabilă, găuri pentru deget', 'Cod produs': '505985'},
  notes=['Culoarea din titlul site-ului (roșu) nu se potrivește cu cea a magazinului (albastru, Sapphire).', 'Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(11274,
  f'<p>Blugii {KS} ELBA FLARE JEANS bleumarin sunt {A("/categorie/pantaloni-treninguri/", "pantaloni pentru fete")} din denim confortabil, din bumbac organic certificat GOTS, cultivat fără îngrășăminte și pesticide. Sunt ușor mulați pe șolduri, iar materialul e elastic.</p>'
  '<p>Se încheie cu nasture și fermoar, iar talia are bandă elastică, utilă la copiii mici. Tipul de blugi e „clopot”, ca în numele modelului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac organic.'), ('Brâu', 'normal.'), ('Închidere', 'nasture și fermoar.'))
  + '<p>Mărimile 86 până la 134-140 sunt gândite, cu aproximație, pentru 1-10 ani.</p>',
  [('model', 'ELBA FLARE JEANS'), ('culoare', 'Culoare bleumarin'), ('denim', 'Model confectionat din denim confortabil'), ('organic', 'bumbac organic certificat'),
   ('pesticide', 'fara utilizarea ingrasamintelor sau pesticidelor'), ('mulați', 'Blugi usor mulati in zona soldurilor'), ('elastic', 'elastic'),
   ('nasture', 'Incheiere cu nasture si fermoar'), ('talie', 'Banda elastica in talie'), ('clopot', 'Tip de blugi: clopot'), ('material', '100% Bumbac organic'), ('brâu', 'Brâu: normal')],
  {'Model': 'Konges Sløjd ELBA FLARE JEANS', 'Material': '100% bumbac organic', 'Caracteristici': 'evazați, talie elastică, nasture și fermoar', 'Cod produs': 'KS104394'},
  notes=['Titlul site-ului are „ELBA” în locul culorii; culoarea e cea de la magazin (bleumarin).', 'Descrierea spune „picior conic”, caracteristicile „clopot” și numele „FLARE”; am urmat numele și caracteristicile.'])
