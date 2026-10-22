import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
GECI = '/categorie/unisex-imbracaminte-geci-jachete/'
GHETE = '/categorie/unisex-incaltaminte-ghete-cizme/'
MANUSI = '/categorie/unisex-accesorii-caciuli-manusi-accesorii/'

w(14620,
  f'<p>Mănușile de iarnă {REIMA} HAVAITA negre sunt {A(MANUSI, "mănuși unisex")} impermeabile, cu inserție Hipora și membrană Reimatec, rezistente la vânt. Palma și degetul mare sunt întărite, iar pe partea de sus izolația e dublă, cu PrimaLoft.</p>'
  '<p>Căptușeala e din fleece moale și călduros, iar materialul exterior respinge apa și murdăria. Pe partea superioară au material reflectorizant, util când se întunecă devreme.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat, tratament poliuretanic.'), ('Coloană de apă', '12.000 mm.'), ('Respirabilitate', '7.000 g/m²/24 h.'), ('Greutate', '35 g.'))
  + '<p>Mărimile 3Y-6Y sunt gândite pentru copii de aproximativ 3-6 ani.</p>',
  [('model', 'REIMA HAVAITA'), ('culoare', 'Negru (negru / gri)'), ('Hipora', 'inserție impermeabilă Hipora'), ('vânt', 'sunt rezistente la vânt'),
   ('întărite', 'palma și degetul mare întărite'), ('dublă', 'izolație dublă în partea superioară de pe exterior'), ('PrimaLoft', 'izolație PrimaLoft® de înaltă calitate'),
   ('fleece', 'căptușeală moale, călduroasă din fleece'), ('resping', 'resping apa și murdăria'), ('reflectorizant', 'material reflectorizant utilizat pe partea superioară a mănușilor'),
   ('material', '100% poliester reciclat, tratament poliuretanic'), ('coloană', '12.000 mm'), ('respirabilitate', '7.000 g/m²/24 h'), ('greutate', '35 g'), ('Reimatec', 'Reimatec')],
  {'Model': 'Reima HAVAITA', 'Material': '100% poliester reciclat', 'Caracteristici': 'Reimatec, PrimaLoft, palmă întărită', 'Cod produs': '199967'},
  notes=['Vârsta calculată automat era nefolositoare (1-1 ani); am trecut 3-6 ani după mărimile 3Y-6Y.'], varsta_txt='3-6 ani')

w(14621,
  f'<p>Cizmele de iarnă {REIMA} LAPLANDER 2.0 negre sunt {A(GHETE, "ghete unisex")} cu membrană Reimatec, omologate pentru temperaturi de -40 °C. Fața combină material textil și sintetic, are cusături etanșate, iar talpa Vibram Arctic Grip ține bine chiar și pe gheață.</p>'
  '<p>Se încalță repede datorită șireturilor elastice. Vârful e mai lat și căputa mai înaltă, deci degetele au loc, iar branțul detașabil Happy Fit ajută la alegerea numărului. Sunt vegane și au elemente reflectorizante.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'poliester, poliuretan.'), ('Talpă', '100% cauciuc.'), ('Izolație', 'vată.'), ('Greutate', '500 g.'))
  + '<p>Numerele 28-40 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'REIMA LAPLANDER 2.0'), ('culoare', 'Negru (negru / alb)'), ('-40', 'omologate pentru temperaturi de - 40 °C'), ('textil', 'combinație de material textil și sintetic'),
   ('etanșate', 'construcție impermeabilă cu inserții cu cusături etanșate'), ('Vibram', 'Talpa Vibram Arctic Grip asigură o aderență excelentă chiar și pe gheață'),
   ('șireturi', 'șireturi elastice pentru strângere rapidă'), ('vârf', 'datorită unui vârf mai lat și unei căpute mai înalte'), ('Happy Fit', 'branțuri detașabile cu un imprimeu Happy Fit'),
   ('vegane', 'vegane'), ('reflectorizant', 'elemente reflectorizante'), ('față', 'poliester, poliuretan'), ('talpă', '100% cauciuc'), ('vată', 'vată'), ('greutate', '500 g'), ('Reimatec', 'Reimatec')],
  {'Model': 'Reima LAPLANDER 2.0', 'Talpă': 'Vibram Arctic Grip', 'Caracteristici': 'membrană Reimatec, -40 °C, șireturi elastice', 'Cod produs': '178397'})

w(14643,
  f'<p>Șortul {REIMA} ELOISIN UVF50 albastru închis se găsește printre {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantalonii unisex")} de vară: are cracul până deasupra genunchiului și protecție UV 50+. Materialul conține fibre reciclate certificate, se întreține ușor și se usucă repede.</p>'
  '<p>Talia e elastică și se ajustează, cu închidere din velcro și capsă. Are două buzunare laterale și unul cusut pe picior, cu fermoar.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Buzunare', 'două laterale și unul pe picior, cu fermoar.'), ('Protecție', 'UV 50+.'))
  + '<p>Mărimile 116-164 se potrivesc orientativ copiilor de 6-14 ani.</p>',
  [('model', 'REIMA ELOISIN UVF50'), ('culoare', 'Albastru închis'), ('genunchi', 'are lungimea cracului până deasupra genunchiului'), ('UV', 'factor de protecție UV 50+'),
   ('reciclat', 'conține fibre reciclate certificate'), ('uscare', 'Are întreținere ușoară, uscare rapidă'), ('talie', 'Talie elastică ajustabilă, care se încheie cu velcro și capsă'),
   ('buzunare', 'Două buzunare laterale și unu cusut pe picior cu fermoar'), ('material', '100 % poliamidă')],
  {'Model': 'Reima ELOISIN UVF50', 'Material': '100% poliamidă', 'Caracteristici': 'UV 50+, talie ajustabilă, uscare rapidă', 'Cod produs': '198029'})

w(14649,
  f'<p>Geaca {A("/brand/head/", "Head")} LANS mov este o {A(GECI, "geacă unisex")} pentru vreme urâtă, cu membrană TPU, coloană de apă de 5.000 mm și respirabilitate de 3.000 g/m²24h. Gluga e fixă, iar fermoarul are protecție la bărbie și e acoperit cu o clapetă.</p>'
  '<p>Mânecile se termină cu elastic, iar marginea de jos se ajustează. Elementele reflectorizante ajută la vizibilitate când lumina e slabă, iar înăuntru e o etichetă pentru nume.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'trei cu fermoar, două în față și unul la piept.'), ('Material', '100% poliester.'), ('Căptușeală', '100% poliester.'))
  + '<p>Mărimile 116-122 până la 164-170 sunt pentru copii de aproximativ 6-15 ani.</p>',
  [('model', 'Head LANS'), ('culoare', 'Mov (mov / albastru deschis)'), ('vreme', 'activități pe vreme nefavorabilă'), ('TPU', 'TPU'), ('coloană', '5.000 mm'),
   ('respirabilitate', '3.000 g/m²24h'), ('glugă', 'glugă fixă'), ('fermoar', 'fermoarul are protecție la bărbie și este acoperit cu clapetă'), ('mâneci', 'mâneci cu finisaj elastic'),
   ('margine', 'margine inferioară ajustabilă'), ('reflectorizant', 'Detaliile reflectorizante sporesc siguranța în condiții slabe de lumină'), ('etichetă', 'etichetă pentru nume în interior'),
   ('buzunare', '3 cu fermoar (2x frontale, 1x la piept)'), ('material', '100 % poliester')],
  {'Model': 'Head LANS', 'Material': '100% poliester, membrană TPU', 'Caracteristici': 'coloană de apă 5.000 mm, glugă fixă, reflectorizante', 'Cod produs': '252671'},
  notes=['Magazinul o descrie ca geacă pentru băieți; pe site e unisex.'])

w(14668,
  f'<p>Pantofii de apă {REIMA} LEAN albastru închis sunt listați la {A("/categorie/unisex-incaltaminte-sandale/", "sandale unisex")} și sunt făcuți pentru plajă și înot, cu protecție UV ridicată. Fața e din textil, sunt ușori, iar talpa flexibilă are drop zero, pentru o poziție naturală a piciorului.</p>'
  '<p>Branțul detașabil are imprimeu Happy Fit, care ajută la alegerea numărului. Materialul de sus lasă piciorul să se aerisească.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'material textil.'), ('Talpă', 'TPR, cauciuc termoplastic.'), ('Cod produs', '198073.'))
  + '<p>Numerele 24-35 sunt pentru copii de cam 2-11 ani.</p>',
  [('model', 'REIMA LEAN'), ('culoare', 'Albastru închis (albastru închis / albastru / portocaliu)'), ('plajă', 'sunt ideali pentru plajă și înot'), ('UV', 'au un grad ridicat de protecție UV'),
   ('textil', 'cu partea superioară de textil'), ('ușori', 'Au greutatea redusă și talpă flexibilă'), ('drop', 'drop zero pentru o poziție naturală'),
   ('Happy Fit', 'Au branț detașabil, cu imprimeu Happy Fit, care ajută la alegerea mărimii corecte'), ('respirabil', 'pantof respirabil'), ('talpă', 'TPR (cauciuc termoplastic)')],
  {'Model': 'Reima LEAN', 'Talpă': 'TPR', 'Caracteristici': 'protecție UV, branț Happy Fit, drop zero', 'Cod produs': '198073'},
  notes=['Pe site e la Sandale; magazinul îi descrie ca pantofi de apă.'])

w(14670,
  f'<p>Geaca outdoor {A("/brand/kilpi/", "KILPI")} ORLETI-JB albastră este o {A(GECI, "geacă unisex")} din material SIBERIUM în două straturi, cu coloană de apă de 10.000 mm și respirabilitate de 8.000 g/m²/24h, care ține ploaia și vântul afară. Cusăturile critice sunt întărite cu bandă.</p>'
  '<p>Gluga e fixă, cu cozoroc întărit, iar gulerul înalt apără gâtul. Manșetele sunt elastice, jos are șnur de strângere, iar eticheta interioară ajută la identificare la școală sau în tabără.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Material', '100% poliester, 100% nailon.'), ('Siguranță', 'elemente reflectorizante.'))
  + '<p>Mărimile 98-158 se potrivesc orientativ copiilor de 3-13 ani.</p>',
  [('model', 'KILPI ORLETI-JB'), ('culoare', 'Albastru (albastru / albastru închis / galben)'), ('SIBERIUM', 'Materialul SIBERIUM în două straturi'), ('coloană', '10.000 mm'),
   ('respirabilitate', '8.000 g/m²/24h'), ('ploaie', 'protecție eficientă împotriva ploii și vântului'), ('bandă', 'cusăturile critice sunt întărite cu bandă'),
   ('cozoroc', 'Are o glugă fixă, cu cozoroc întărit și guler înalt, care protejează gâtul de intemperii'), ('manșete', 'Manșetele elastice și șnurul de strângere din partea inferioară'),
   ('etichetă', 'eticheta interioară facilitează identificarea la școală sau în tabără'), ('buzunare', '2 laterale cu fermoar'), ('material', '100 % poliester'), ('nailon', '100 % nailon'),
   ('reflectorizant', 'elemente reflectorizante')],
  {'Model': 'KILPI ORLETI-JB', 'Material': '100% poliester, 100% nailon', 'Caracteristici': 'SIBERIUM, coloană de apă 10.000 mm, glugă cu cozoroc', 'Cod produs': '290918'},
  notes=['Titlul site-ului nu are numele modelului (ORLETI-JB); magazinul o descrie ca geacă pentru băieți.'])

w(14687,
  f'<p>Geaca {A("/brand/umbro/", "Umbro")} TARMO neagră este o {A(GECI, "geacă unisex")} ușoară și călduroasă, cu material fin, dens țesut, și umplutură din microfibre. Membrana o apără de intemperii, cu o coloană de apă de 1.000 mm, deci e mai degrabă pentru zile reci decât pentru ploaie puternică.</p>'
  '<p>Fermoarul principal are clapetă și, sus, protecție la bărbie. Gluga e fixă, mânecile sunt ușor strânse cu elastic, iar elementele reflectorizante ajută la amurg și pe întuneric.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două în față, cu fermoar.'), ('Material', '100% poliester reciclat.'), ('Respirabilitate', '500 g/m²/24h.'), ('Interior', 'etichetă pentru nume.'))
  + '<p>Mărimile 112-116 până la 164-170 sunt pentru copii de aproximativ 5-15 ani.</p>',
  [('model', 'Umbro TARMO'), ('culoare', 'Negru (negru / portocaliu)'), ('ușoară', 'este ușoară, călduroasă'), ('țesut', 'material moale cu țesătură densă'),
   ('microfibră', 'umplutură din microfibre'), ('membrană', 'datorită membranei, protejează în mod fiabil împotriva intemperiilor'), ('coloană', '1.000 mm'),
   ('fermoar', 'fermoarul principal este prevăzut cu o clapetă'), ('glugă', 'glugă fixă'), ('mâneci', 'mâneci ușor strânse cu elastic'),
   ('reflectorizant', 'Elementele reflectorizante sporesc siguranța copilului în condiții de întuneric și amurg'), ('buzunare', '2 în față cu fermoar'),
   ('material', '100 % poliester reciclat'), ('respirabilitate', '500 g/m²/24h'), ('etichetă', 'etichetă pentru nume în interior')],
  {'Model': 'Umbro TARMO', 'Material': '100% poliester reciclat', 'Caracteristici': 'umplutură din microfibre, glugă fixă, reflectorizante', 'Cod produs': '232970'})

w(14703,
  f'<p>Mănușile cu un deget {REIMA} AVAUS negre sunt {A(MANUSI, "mănuși unisex")} de iarnă pentru copii mici, cu inserție impermeabilă și o coloană de apă de 7.000 mm. Sunt flexibile, au întărituri pentru o prindere mai bună și se închid ușor cu velcro.</p>'
  '<p>Căptușeala e din tricotaj de poliester periat, iar izolația Fellex e 100% reciclată. După spălare pot merge în uscător, ca să se usuce mai repede, iar imprimeul reflectorizant le face vizibile.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '60% poliester reciclat, 40% poliester, strat de poliuretan.'), ('Respirabilitate', '5.000 g/m²/24h.'), ('Greutate', '100 g.'))
  + '<p>Magazinul nu dă o mărime în cifre; sunt pentru copii mici, orientativ cam 1-3 ani.</p>',
  [('model', 'REIMA AVAUS'), ('culoare', 'Negru (negru / alb)'), ('copii mici', 'Mănușile de iarnă pentru copii mici Reima AVAUS'), ('impermeabil', 'inserție impermeabilă'),
   ('coloană', '7.000 mm'), ('flexibile', 'Sunt flexibile, cu întărituri pentru o prindere mai bună'), ('velcro', 'închidere ușoară cu velcro'),
   ('căptușeală', 'căptușeală din tricotaj de poliester periat'), ('Fellex', 'izolație 100% reciclată Fellex®'), ('uscător', 'După spălare, se pot introduce în uscător'),
   ('reflectorizant', 'imprimeu reflectorizant'), ('material', '60 % poliester reciclat, 40 % poliester, strat de poliuretan'), ('respirabilitate', '5.000 g/m²/24h'), ('greutate', '100 g')],
  {'Model': 'Reima AVAUS', 'Material': '60% poliester reciclat, 40% poliester', 'Caracteristici': 'inserție impermeabilă, izolație Fellex, velcro', 'Cod produs': '260038'},
  notes=['Produsul nu are mărimi în catalog (magazinul arată doar „O”); vârsta 1-3 ani e estimată din „copii mici”.'], varsta_txt='1-3 ani')

w(14722,
  f'<p>Geaca de iarnă {A("/brand/loap/", "LOAP")} INPAL neagră este o {A(GECI, "geacă unisex")} matlasată, cu fața din STORMEX și strat impermeabil DryTech, făcută să reziste la zăpadă, ploaie și vânt. Umplutura din fibre tubulare POLYTHERM ține de cald și își păstrează bine forma.</p>'
  '<p>Gluga e fixă, iar marginea de jos și capetele mânecilor sunt elastice. Fermoarul are capac la bărbie, ca să nu ciupească pielea la îmbrăcat, iar elementele reflectorizante ajută pe drum prin oraș.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două, exterioare.'), ('Material', '100% poliester (Stormex).'), ('Căptușeală', 'tafta din poliester.'), ('Croială', 'clasică.'))
  + '<p>Mărimile 112-116 până la 158-164 se potrivesc orientativ copiilor de 5-14 ani.</p>',
  [('model', 'LOAP INPAL'), ('culoare', 'Negru (negru / albastru deschis)'), ('STORMEX', 'părții superioare STORMEX din material întărit cu strat impermeabil DryTech'),
   ('zăpadă', 'poate face față zăpezii, ploii și vântului'), ('POLYTHERM', 'Umplutura izolatoare din fibre tubulare POLYTHERM'), ('formă', 'are o memorie excelentă a formei'),
   ('glugă', 'Are o glugă fixă iar marginea inferioară și capetele mânecilor sunt elastice'), ('bărbie', 'capac la bărbie, prevenind astfel ciupirea dureroasă a pielii'),
   ('matlasat', 'Aspectul elegant matlasat'), ('reflectorizant', 'geaca este echipată cu elemente reflectorizante'), ('buzunare', '2 buzunare exterioare'),
   ('material', '100 % poliester (Stormex)'), ('tafta', '100 % poliester (tafta)'), ('croială', 'croială clasică')],
  {'Model': 'LOAP INPAL', 'Material': '100% poliester (Stormex)', 'Caracteristici': 'DryTech, umplutură Polytherm, glugă fixă', 'Cod produs': '163445'})

w(14740,
  f'<p>Geaca de snowboard {A("/brand/lewro/", "Lewro")} BUXLEY mix (cu albastru închis) este o {A(GECI, "geacă unisex")} care merge și la schi. Are umplutură termoizolantă, centură de zăpadă, spate prelungit și fermoar principal rezistent la apă, susținut de clapetă și cu protecție pentru bărbie.</p>'
  '<p>Gluga e fixă și ajustabilă, iar mânecile și marginea de jos se reglează. Pe mâneca stângă are buzunar pentru skipass, iar înăuntru un buzunar cu velcro și o etichetă pentru nume.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare exterioare', 'patru cu fermoar, trei frontale și unul la piept.'), ('Coloană de apă', '2.000 mm.'), ('Respirabilitate', '2.000 g/m²/24h.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 116-122 până la 164-170 sunt pentru copii de aproximativ 6-15 ani.</p>',
  [('model', 'Lewro BUXLEY'), ('culoare', 'Mix (mix / albastru închis)'), ('schi', 'Geaca de snowboard pentru copii Lewro BUXLEY este potrivită și pentru schi'),
   ('umplutură', 'umplutură din material termoizolant'), ('centură', 'centură de zăpadă'), ('spate', 'spate prelungit'),
   ('fermoar', 'fermoarul principal rezistent la apă este susținut de o clapetă și este acoperit cu o protecție pentru bărbie'), ('glugă', 'glugă ajustabilă'),
   ('mâneci', 'mâneci ajustabile'), ('margine', 'margine inferioară ajustabilă'), ('skipas', 'buzunar pentru skipas cu fermoar pe mâneca stângă'),
   ('velcro', 'în interior dispune de buzunar cu velcro'), ('etichetă', 'etichetă interioară pentru nume'), ('buzunare', '4 (3x frontale cu fermoar, 1x la piept cu fermoar)'),
   ('coloană', '2.000 mm'), ('respirabilitate', '2.000 g/m²/24h'), ('material', '100% poliester')],
  {'Model': 'Lewro BUXLEY', 'Material': '100% poliester', 'Caracteristici': 'centură de zăpadă, buzunar skipass, glugă ajustabilă', 'Cod produs': '163366'})
