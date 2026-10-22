import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
HEAD = A('/brand/head/', 'Head')
GECI = '/categorie/unisex-imbracaminte-geci-jachete/'
GHETE = '/categorie/unisex-incaltaminte-ghete-cizme/'
MANUSI = '/categorie/unisex-accesorii-caciuli-manusi-accesorii/'

w(14743,
  f'<p>Mănușile {REIMA} VANUKKO negre sunt {A(MANUSI, "mănuși unisex")} de iarnă care țin mâinile calde: materialul e respirabil, rezistent la vânt, impermeabil și rezistent la murdărie, iar inserția Hipora adaugă încă un strat de protecție.</p>'
  '<p>Pe dos au izolație dublă cu PrimaLoft, înăuntru o căptușeală moale din fleece, iar la încheietură o curea care se reglează ușor.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat, laminare TPU reciclată.'), ('Coloană de apă', '10.000 mm.'), ('Respirabilitate', '7.000 g/m²/24 h.'), ('Greutate', '150 g.'))
  + '<p>Mărimile 5Y-8Y se potrivesc orientativ copiilor de 5-8 ani.</p>',
  [('model', 'REIMA VANUKKO'), ('culoare', 'Negru (negru / argintiu)'), ('calde', 'vor menține mâinile calde'),
   ('respirabil', 'Materialul respirabil și rezistent la vânt este impermeabil și rezistent la murdărie'), ('Hipora', 'inserția impermeabilă Hipora adaugă un strat suplimentar de protecție'),
   ('dublă', 'izolație dublă în partea superioară de pe exterior'), ('PrimaLoft', 'izolație PrimaLoft® de înaltă calitate'), ('fleece', 'căptușeală moale, călduroasă din fleece'),
   ('curea', 'curea pentru reglare ușoară pe încheietura mâinii'), ('material', '100% poliester reciclat, laminare TPU reciclată'), ('coloană', '10.000 mm'),
   ('respirabilitate', '7.000 g/m²/24 h'), ('greutate', '150 g')],
  {'Model': 'Reima VANUKKO', 'Material': '100% poliester reciclat', 'Caracteristici': 'Hipora, PrimaLoft, curea la încheietură', 'Cod produs': '199965'},
  notes=['Vârsta calculată automat era nefolositoare (1-1 ani); am trecut 5-8 ani după mărimile 5Y-8Y.'], varsta_txt='5-8 ani')

w(14745,
  f'<p>Adidașii {REIMA} KIIRUS roz sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} de toamnă și primăvară, cu membrană Reimatec care ține piciorul uscat. Fața, din plasă și material sintetic, e impermeabilă, dar respirabilă, iar talpa din Reima EVA, cu întărituri din cauciuc termoplastic, e moale și flexibilă.</p>'
  '<p>Se prind pe picior cu benzi velcro, deci se încalță ușor. Branțul anatomic detașabil are imprimeu Happy Fit pentru alegerea numărului. Sunt vegani și fără fluorocarbon.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', '61% poliester, 39% poliuretan.'), ('Talpă', '80% EVA, 20% cauciuc.'), ('Greutate', '260 g.'))
  + '<p>Numerele 24-28 sunt pentru copii de aproximativ 2-5 ani.</p>',
  [('model', 'REIMA KIIRUS'), ('culoare', 'Roz (roz / bej)'), ('toamnă', 'pantofi impermeabili de toamnă/primăvară'), ('membrană', 'sunt prevăzuți cu membrană care menține picioarele uscate'),
   ('plasă', 'parte superioară de plasă și material sintetic'), ('respirabil', 'Partea superioară impermeabilă, dar respirabilă'),
   ('EVA', 'Talpa este confecționată din elastomer sintetic Reima EVA cu întărituri din cauciuc termoplastic'), ('flexibilă', 'talpă moale și flexibilă'),
   ('velcro', 'Pe căpută se află benzi velcro'), ('Happy Fit', 'branț detașabil și anatomic EVA, cu căptușeală din jerseu și imprimeu Happy Fit'), ('vegani', 'vegani'),
   ('fluor', 'fără fluorocarbon'), ('față', '61 % poliester, 39 % poliuretan'), ('talpă', '80% EVA, 20% cauciuc'), ('greutate', '260 g'), ('Reimatec', 'Reimatec')],
  {'Model': 'Reima KIIRUS', 'Membrană': 'Reimatec', 'Caracteristici': 'velcro, branț Happy Fit, vegani', 'Cod produs': '277956'})

w(14749,
  f'<p>Geaca softshell {A("/brand/lewro/", "Lewro")} CHISOMO neagră este o {A(GECI, "geacă unisex")} pentru purtat zilnic, din softshell elastic cu interior din fleece periat, care apără de vânt și frig. Are membrană, coloană de apă de 8.000 mm și respirabilitate de 3 000 g/m²/24h.</p>'
  '<p>Mânecile, marginea de jos și conturul glugii fixe sunt finisate cu elastic plat. Fermoarul principal are clapetă și protecție la bărbie, iar elementele reflectorizante se văd bine.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două în față, cu fermoar.'), ('Material', '94% poliester, 6% elastan.'), ('Interior', 'etichetă pentru nume.'))
  + '<p>Mărimile 116-122 până la 164-170 se potrivesc orientativ copiilor de 6-15 ani.</p>',
  [('model', 'Lewro CHISOMO'), ('culoare', 'Negru (negru / verde deschis)'), ('zilnic', 'confort în utilizarea zilnică'), ('fleece', 'material softshell elastic cu interior din fleece periat'),
   ('vânt', 'oferă protecție împotriva vântului și frigului'), ('coloană', '8.000 mm'), ('respirabilitate', '3 000 g/m²/24h'),
   ('elastic', 'mânecile, marginea inferioară și circumferința glugii sunt finisate cu elastic plat'), ('glugă', 'glugă fixă'),
   ('fermoar', 'fermoar principal cu clapetă și protecție la bărbie'), ('reflectorizant', 'elemente reflectorizante'), ('buzunare', '2 în față cu fermoar'),
   ('material', '94% poliester, 6% elastan'), ('etichetă', 'etichetă pentru nume în interior')],
  {'Model': 'Lewro CHISOMO', 'Material': '94% poliester, 6% elastan', 'Caracteristici': 'softshell cu fleece, membrană, glugă fixă', 'Cod produs': '252390'})

w(14784,
  f'<p>Geaca de schi {A("/brand/loap/", "LOAP")} CUWIELO portocalie este o {A(GECI, "geacă unisex")} cu glugă, membrană AQUA PRO, coloană de apă de 3000 mm și cusături critice lipite. Exteriorul STORMEX rezistă la zăpadă, ploaie și vânt, iar umplutura POLYTHERM din fibre tubulare ține de cald.</p>'
  '<p>Croiala e mulată, cu spatele ușor alungit. Mânecile se ajustează cu velcro și au manșete elastice cu orificiu pentru deget, iar fermoarul principal are capac la bărbie.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'trei, două laterale cu fermoar și unul pe antebrațul stâng.'), ('Căptușeală', 'tafta 100% poliester.'), ('Respirabilitate', '3000 g/m2/24h.'))
  + '<p>Mărimile 112-116 până la 158-164 sunt pentru copii de cam 5-14 ani.</p>',
  [('model', 'LOAP CUWIELO'), ('culoare', 'Portocaliu (portocaliu / albastru / argintiu)'), ('coloană', 'are o coloană de apă de 3000 mm'), ('lipite', 'cusături critice lipite'),
   ('AQUA PRO', 'membrană AQUA PRO impermeabilă'), ('STORMEX', 'Materialul exterior STORMEX este rezistent împotriva zăpezii, a ploii și a vântului'),
   ('POLYTHERM', 'umplutura călduroasă este realizată din fibre tubulare POLYTHERM'), ('mulată', 'Dispune de croială mulată, cu partea din spate ușor alungită'),
   ('mâneci', 'Mânecile se ajustează cu bandă velcro și au manșete elastice cu orificiu pentru deget'), ('fermoar', 'Fermoarul principal cu capac practic protejează bărbia'),
   ('buzunare', 'două buzunare laterale cu fermoar și un buzunar pe antebrațul stâng'), ('tafta', 'tafta 100% poliester'), ('respirabilitate', '3000 g/m2/24h')],
  {'Model': 'LOAP CUWIELO', 'Material': '100% poliester (Stormex)', 'Caracteristici': 'membrană Aqua Pro, umplutură Polytherm, orificiu pentru deget', 'Cod produs': '143648'})

w(14786,
  f'<p>Geaca {HEAD} FLORINA albastru deschis este o {A(GECI, "geacă unisex")} pentru zilele reci, la școală sau la plimbare. Materialul e călduros, gluga fixă apără de vânt, iar cusăturile decorative îi dau un aspect modern.</p>'
  '<p>Fantele de pe lateral lasă copilul să se miște ușor. Fermoarul principal are protecție la vânt și la bărbie, în față e logoul, iar înăuntru o etichetă pentru nume.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două în față, cu fermoar.'), ('Material', '96% nailon, 4% elastan (Spandex).'), ('Umplutură', '100% poliester.'))
  + '<p>Mărimile 116-122 până la 164-170 sunt pentru copii de aproximativ 6-15 ani.</p>',
  [('model', 'Head FLORINA'), ('culoare', 'Albastru deschis (albastru deschis / negru)'), ('rece', 'activități zilnice și activități de agrement pe vreme rece'),
   ('călduros', 'Materialul călduros oferă confortul adecvat'), ('glugă', 'gluga protejează împotriva vântului'), ('modern', 'Cusăturile interesante îi conferă un aspect modern'),
   ('fante', 'Fantele practice pe lateral permit mișcarea liberă'), ('fermoar', 'fermoar principal cu protecție împotriva vântului și protecție la bărbie'),
   ('logo', 'logo pe partea din față'), ('etichetă', 'etichetă pentru nume în interior'), ('buzunare', '2 în față cu fermoar'), ('material', '96 % nailon, 4 % elastan (Spandex)'),
   ('umplutură', '100 % poliester'), ('fixă', 'fixă')],
  {'Model': 'Head FLORINA', 'Material': '96% nailon, 4% elastan', 'Caracteristici': 'glugă fixă, fante laterale, protecție la bărbie', 'Cod produs': '186551'})

w(14797,
  f'<p>Geaca matlasată {A("/brand/umbro/", "Umbro")} ROBONI neagră este o {A(GECI, "geacă unisex")} ușoară, cu glugă fixă, material dens și moale și umplutură din microfibre. Fermoarele sunt YKK, iar cel principal are clapetă și protecție la bărbie.</p>'
  '<p>Marginea glugii, mânecile și tivul sunt finisate cu elastic plat. Elementele reflectorizante ajută la vizibilitate, iar înăuntru e o etichetă pentru numele copilului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două în față, cu fermoar.'), ('Material', '100% poliester.'), ('Căptușeală', '100% poliester.'))
  + '<p>Mărimile 112-116 până la 164-170 se potrivesc orientativ copiilor de 5-15 ani.</p>',
  [('model', 'Umbro ROBONI'), ('culoare', 'Negru (negru / albastru închis / alb)'), ('ușoară', 'cu glugă și greutate redusă'), ('țesătură', 'material cu țesătură densă și moale'),
   ('YKK', 'fermoare de calitate YKK'), ('microfibre', 'umplutură din micro fibre'), ('fermoar', 'fermoarul principal cu clapetă și protecție la bărbie'), ('glugă', 'glugă fixă'),
   ('elastic', 'marginea glugii, a mânecilor și tivul cu elastic plat'), ('reflectorizant', 'elemente reflectorizante'), ('etichetă', 'etichetă pentru nume în interior'),
   ('buzunare', '2 în față cu fermoar'), ('material', '100 % poliester')],
  {'Model': 'Umbro ROBONI', 'Material': '100% poliester', 'Caracteristici': 'umplutură din microfibre, fermoare YKK, glugă fixă', 'Cod produs': '192599'})

w(14802,
  f'<p>Geaca de schi fond {A("/brand/swix/", "Swix")} CROSS somon este o {A(GECI, "geacă unisex")} din softshell stretch, gândită pentru antrenamentele de zi cu zi ale copiilor și juniorilor care schiază repede. E respirabilă, iar în față are membrană rezistentă la vânt.</p>'
  '<p>Spatele și laturile sunt din material elastic fără membrană. Izolația termică e ușoară, iar elementele reflectorizante ajută la vizibilitate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două în față, cu fermoar.'), ('Material', '100% poliester; 85% poliester, 15% spandex.'), ('Culoare', 'somon cu albastru închis.'))
  + '<p>Mărimile 128-164 sunt pentru copii de cam 8-14 ani.</p>',
  [('model', 'Swix CROSS'), ('culoare', 'Somon (somon / albastru închis)'), ('schi fond', 'Geacă de schi fond copii'), ('juniori', 'pentru copiii și juniorii, care apreciază viteza'),
   ('antrenament', 'Este ideală pentru antrenamentele intense de zi cu zi'), ('softshell', 'țesătura principală din softshell stretch'),
   ('membrană', 'este respirabilă, iar în față are membrană rezistentă la vânt'), ('spate', 'spatele și părțile laterale sunt din material elastic fără membrană'),
   ('izolație', 'Izolația termică cu greutatea redusă'), ('reflectorizant', 'elemente reflectorizante'), ('buzunare', '2 în față cu fermoar'), ('material', '100 % poliester'),
   ('spandex', '85 % poliester, 15 % spandex')],
  {'Model': 'Swix CROSS', 'Material': 'softshell stretch, poliester și spandex', 'Caracteristici': 'membrană în față, schi fond, reflectorizante', 'Cod produs': '142180'},
  notes=['Specificațiile spun „2 în față cu fermoar”, iar lista de caracteristici „două buzunare laterale”; am folosit specificațiile.'])

w(14805,
  f'<p>Geaca matlasată {HEAD} NISSA vișinie este o {A(GECI, "geacă unisex")} ușoară, cu umplutură călduroasă, bună pentru oraș, școală și plimbări pe vreme rece. Gluga e fixă și se reglează cu un șnur elastic.</p>'
  '<p>Fermoarul are protecție în zona bărbiei, iar înăuntru e o etichetă pentru nume. Magazinul o prezintă ca geacă pentru fete, cu un design elegant.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două, cu fermoar.'), ('Material', '75% nailon, 25% elastan.'), ('Căptușeală', '100% poliester.'))
  + '<p>Mărimile 116-122 până la 164-170 sunt pentru copii de aproximativ 6-15 ani.</p>',
  [('model', 'Head NISSA'), ('culoare', 'Vișiniu (vișiniu / roz)'), ('ușoară', 'în același timp, foarte ușoară'), ('umplutură', 'umplutură călduroasă'),
   ('oraș', 'Este potrivită pentru purtare în oraș, la școală, dar și pentru plimbări pe vreme rece'), ('glugă', 'glugă fixă, reglabilă cu ajutorul șnurului elastic'),
   ('fermoar', 'fermoar cu protecție în zona bărbiei'), ('etichetă', 'etichetă interioară pentru nume'), ('fete', 'Geaca matlasată pentru fete Head NISSA'),
   ('design', 'Beneficiază de un design elegant'), ('buzunare', '2 buzunare cu fermoar'), ('material', '75 % nailon, 25 % elastan'), ('căptușeală', '100 % poliester')],
  {'Model': 'Head NISSA', 'Material': '75% nailon, 25% elastan', 'Caracteristici': 'matlasată, glugă reglabilă, protecție la bărbie', 'Cod produs': '130278'},
  notes=['Magazinul o descrie ca geacă pentru fete; pe site e unisex.'])

w(14812,
  f'<p>Ghetele {REIMA} EDISTYS negre sunt {A(GHETE, "ghete unisex")} pe gleznă, cu membrană și fața din microfibră impermeabilă și respirabilă, cu cusături lipite. Talpa Vibram XS Trek e durabilă și ține bine pe tot felul de suprafețe.</p>'
  '<p>Se încalță repede cu șiretul elastic. Branțul Ortholite e anatomic și detașabil, cu imprimeu Happy Fit pentru alegerea numărului. Au elemente reflectorizante și nu conțin compuși cu fluor sau materiale de origine animală.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', '82% poliester, 18% poliuretan.'), ('Talpă', '50% EVA, 50% cauciuc.'), ('Căptușeală', 'plasă, 100% poliester.'), ('Greutate', '400 g.'))
  + '<p>Numerele 28-35 se potrivesc orientativ copiilor de 4-11 ani.</p>',
  [('model', 'REIMA EDISTYS'), ('culoare', 'Negru (negru / gri / alb)'), ('gleznă', 'ghete pe gleznă cu membrană'), ('microfibră', 'microfibră impermeabilă respirabilă'),
   ('lipite', 'inserție impermeabilă, cu cusături lipite și căptușeală din plasă'), ('Vibram', 'talpa Vibram XS Trek are durabilitate și aderență excelente pe toate suprafețele'),
   ('șiret', 'șiret elastic pentru încălțare rapidă și ușoară'), ('Ortholite', 'branț detașabil Ortholite'), ('Happy Fit', 'Branțul anatomic detașabil'), ('imprimeu', 'imprimeu Happy Fit'),
   ('reflectorizant', 'elemente reflectorizante'), ('fluor', 'nu conțin compuși cu fluor sau materiale de origine animală'), ('față', '82 % poliester, 18 % poliuretan'),
   ('talpă', '50 % EVA, 50 % cauciuc'), ('căptușeală', 'căptușeală: 100 % poliester'), ('greutate', '400 g')],
  {'Model': 'Reima EDISTYS', 'Talpă': 'Vibram XS Trek', 'Caracteristici': 'membrană, branț Ortholite, șiret elastic', 'Cod produs': '178376'})

w(14864,
  f'<p>Geaca de iarnă {A("/brand/didriksons/", "Didriksons")} NEPTUN mov este o {A(GECI, "geacă unisex")} izolată, pentru sporturile de iarnă, din poliamidă reciclată cu coloană de apă de 10.000 mm. Croiala e ergonomică, iar gulerul înalt și protecția pentru bărbie adaugă confort.</p>'
  '<p>Tivul de jos și mânecile au margine elastică, iar manșetele au orificii pentru degete. Gluga e fixă, iar detaliile reflectorizante ajută când lumina e slabă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Material', '100% poliamidă (reciclată), 115 g/m².'), ('Respirabilitate', '4.000 g/m²/24h.'))
  + '<p>Mărimile 100-140 sunt pentru copii de cam 3-10 ani.</p>',
  [('model', 'DIDRIKSONS NEPTUN'), ('culoare', 'Mov (mov / roz / alb)'), ('izolată', 'Geaca izolată Didriksons NEPTUN este ideală pentru sporturile de iarnă'),
   ('material', '100 % poliamidă (reciclată)'), ('coloană', '10.000 mm'), ('ergonomică', 'Croiala ergonomică și elementele elastice'),
   ('guler', 'Este prevăzută cu guler înalt și protecție pentru bărbie'), ('tiv', 'margine elastică în jurul tivului inferior'), ('mâneci', 'mâneci cu tiv elastic'),
   ('degete', 'orificii pentru degete'), ('reflectorizant', 'Detaliile reflectorizante sporesc siguranța în condiții slabe de lumină'), ('greutate', '115 g/m²'),
   ('respirabilitate', '4.000 g/m²/24h'), ('buzunare', '2 laterale cu fermoar'), ('glugă', 'fixă')],
  {'Model': 'Didriksons NEPTUN', 'Material': '100% poliamidă reciclată', 'Caracteristici': 'coloană de apă 10.000 mm, orificii pentru degete, glugă fixă', 'Cod produs': '252760'})
