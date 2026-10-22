import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
DID = A('/brand/didriksons/', 'Didriksons')
GU = '/categorie/unisex-imbracaminte-geci-jachete/'
SAL = '/categorie/unisex-imbracaminte-salopete-compleuri/'
VANDUT = 'Pagina magazinului arată produsul ca VÂNDUT și nu dă culoarea; culoarea e cea din titlul site-ului.'

w(14020,
  f'<p>Salopeta de iarnă {REIMA} KURIKKA roz este un {A(SAL, "combinezon unisex")} cu imprimeu și aer sportiv, din material respirabil, rezistent la apă și vânt, cu suprafață care respinge murdăria. Pe spate și pe picioare, sub genunchi, materialul e mai rezistent.</p>'
  '<p>Membrana Reimatec are cusături sigilate, finisajul BIONIC-FINISH ECO e fără fluorocarburi, iar izolația Fellex e din poliester 100% reciclat. Gluga se detașează, manșetele sunt elastice, iar benzile elastice peste încălțăminte se scot.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Coloană de apă', '10.000 mm.'), ('Respirabilitate', '7 000 g/m2/24 h.'), ('Buzunare', 'două, cu fermoar.'), ('Greutate', '1 kg.'))
  + '<p>Pe site a rămas doar mărimea 128, potrivită orientativ pe la 7-8 ani.</p>',
  [('model', 'REIMA KURIKKA'), ('imprimeu', 'beneficiază de un imprimeu distinctiv'), ('respirabil', 'material respirabil, complet rezistent la apă și vânt'),
   ('murdărie', 'cu o suprafață care respinge murdăria'), ('genunchi', 'Pe spate și pe picioare, de la genunchi în jos'), ('Reimatec', 'Reimatec'), ('sigilate', 'sigilate ermetic'),
   ('BIONIC', 'BIONIC-FINISH®ECO fără fluorocarburi'), ('Fellex', 'materialul termoizolant Fellex® realizat din fibre de poliester 100% reciclate'), ('glugă', 'detașabilă'),
   ('manșete', 'manșete elastice'), ('benzi', 'benzi elastice detașabile peste încălțăminte'), ('coloană', '10.000 mm'), ('respirabilitate', '7 000 g/m2/24 h'),
   ('buzunare', '2x cu fermoar'), ('greutate', '1 kg')],
  {'Model': 'Reima KURIKKA', 'Material': '100% poliester, peliculă TPU', 'Caracteristici': 'Reimatec, Fellex, glugă detașabilă', 'Cod produs': '259978'},
  notes=[VANDUT], varsta_txt='7-8 ani')

w(14275,
  f'<p>Căciula {REIMA} PAMPULA gri închis este un {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "accesoriu unisex")} de iarnă, tricotat jacquard pe toată suprafața, din amestec moale de lână merino, cu ciucure. Lâna ține de cald și reglează temperatura.</p>'
  '<p>Căștile rezistente la vânt apără urechile, iar căptușeala integrală din fleece e moale și caldă. Mărimea indică circumferința capului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '50% lână merino, 50% poliester reciclat.'), ('Căptușeală', 'fleece.'), ('Greutate', '200 g.'))
  + '<p>Mărimile 52-54 și 56-58 sunt circumferințe ale capului, potrivite orientativ copiilor de la 3 ani în sus.</p>',
  [('model', 'REIMA PAMPULA'), ('jacquard', 'tricot jacquard pe toată suprafața'), ('merino', 'amestec moale de lână merino'), ('ciucure', 'ciucure'),
   ('reglare', 'reglare termică optimă'), ('căști', 'Căștile rezistente la vânt protejează urechile mici'), ('fleece', 'căptușeală integrală: fleece moale și cald'),
   ('circumferință', 'mărimea indică circumferința capului'), ('material', '50 % lână (Merino), 50 % poliester reciclat'), ('greutate', '200 g')],
  {'Model': 'Reima PAMPULA', 'Material': '50% lână merino, 50% poliester reciclat', 'Caracteristici': 'jacquard, ciucure, căptușeală fleece', 'Cod produs': '260058'},
  notes=[VANDUT, 'Vârsta calculată automat era nefolositoare; „de la 3 ani” e estimat din circumferința capului.'], varsta_txt='de la 3 ani în sus')

w(14413,
  f'<p>Geaca de iarnă {DID} ENSO roz este o {A(GU, "geacă unisex")} de tranziție, căptușită cu fleece din fibră reciclată, rezistentă la vânt și la apă, cu cusături lipite. Croiala e dreaptă, foarte lejeră, iar funcția Extend Size lungește mânecile cu o mărime.</p>'
  '<p>Gluga se detașează și are interior stretch. Fermoarul are protecție la bărbie, manșetele sunt elastice, tivul se ajustează, iar înăuntru e o etichetă pentru nume. Detaliile reflectorizante se văd seara.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Coloană de apă', '6.000 mm.'), ('Respirabilitate', '4 000 g/m²/24h.'), ('Buzunare', 'două în față cu velcro, unul interior.'))
  + '<p>Mărimile 90-130 se potrivesc pe la 2-8 ani.</p>',
  [('model', 'DIDRIKSONS ENSO'), ('tranziție', 'este model ideal pentru perioada de tranziție'), ('fleece', 'Este căptușită cu fleece, realizat din fibră reciclată'),
   ('vânt', 'Este complet rezistentă la vânt și la apă'), ('lipite', 'are cusături lipite'), ('lejeră', 'croială dreaptă, foarte lejeră'), ('Extend', 'Are funcție „Extend size“'),
   ('glugă', 'Are glugă detașabilă, cu interior stretch'), ('bărbie', 'fermoar cu protecție la bărbie'), ('manșete', 'manșete elastice'), ('tiv', 'tiv ajustabil'),
   ('etichetă', 'etichetă pentru nume'), ('reflectorizant', 'detalii reflectorizante'), ('coloană', '6.000 mm'), ('respirabilitate', '4 000 g/m²/24h'),
   ('buzunare', '2 în față cu velcro'), ('interior', 'unu')],
  {'Model': 'Didriksons ENSO', 'Material': '100% poliester', 'Caracteristici': 'căptușeală fleece, Extend Size, glugă detașabilă', 'Cod produs': '184715'},
  notes=[VANDUT])

w(14419,
  f'<p>Geaca de vânt {A("/brand/unuo/", "UNUO")} FLOWERS mov este o {A(GU, "geacă unisex")} ușoară și respirabilă, care apără de vânt și ploaie ușoară fără să încurce mișcarea, bună pentru excursii, ciclism sau terenul de joacă. Nu are izolație și nici membrană.</p>'
  '<p>Fermoarul e scurt, buzunarul e tip cangur, iar geaca se poate împacheta în propriul buzunar. Croiala e clasică, iar elementele reflectorizante ajută la vizibilitate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '90% poliester, 10% elastan.'), ('Buzunar', 'cangur.'), ('Fermoar', 'scurt.'))
  + '<p>Mărimile 110/116 până la 158-164 corespund aproximativ vârstei de 5-14 ani.</p>',
  [('model', 'UNUO FLOWERS'), ('vânt', 'Geaca de vânt pentru copii UNUO FLOWERS'), ('ușor', 'material ușor și respirabil'),
   ('ploaie', 'protejează împotriva vântului și a ploii ușoare, fără a restricționa mișcarea'), ('activități', 'de la ciclism la drumeții'),
   ('fermoar', 'fermoar scurt'), ('cangur', 'stil cangur'), ('împachetată', 'Poate fi ușor împachetată în propriul buzunar'), ('croială', 'croială clasică'),
   ('reflectorizant', 'elemente reflectorizante pentru siguranță mai mare'), ('material', '90 % poliester, 10 % elastan')],
  {'Model': 'UNUO FLOWERS', 'Material': '90% poliester, 10% elastan', 'Caracteristici': 'geacă de vânt, se împachetează, reflectorizante', 'Cod produs': '287062'},
  notes=[VANDUT])

w(14520,
  f'<p>Cămașa în carouri {A("/brand/gap/", "GAP")} FASHION roșie, listată la {A(GU, "geci unisex")}, are mânecă scurtă și croială dreaptă, din bumbac cu poliester. Gulerul se încheie cu nasturi, iar pe piept are un buzunar mic.</p>'
  '<p>Pe cămașă e brodat micul ursuleț Brannan, semnul GAP. Cu mânecă scurtă, e o piesă pentru zilele calde.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '77% bumbac, 23% poliester.'), ('Mânecă', 'scurtă.'), ('Buzunar', 'unul, la piept.'))
  + '<p>Pe site a rămas doar mărimea XS, care la GAP corespunde, cu aproximație, vârstei de 4-5 ani.</p>',
  [('model', 'GAP FASHION'), ('carouri', 'Cămașa în carouri pentru copii GAP FASHION'), ('mânecă', 'are mânecă scurtă și croială dreaptă'), ('guler', 'guler cu închidere cu nasturi'),
   ('buzunar', 'Pe piept este cusut un buzunar mic'), ('ursuleț', 'broderie mică cu ursulețul Brannan'), ('material', '77 % bumbac, 23 % poliester'), ('piept', '1 buzunar la piept')],
  {'Model': 'GAP FASHION', 'Material': '77% bumbac, 23% poliester', 'Caracteristici': 'carouri, mânecă scurtă, ursuleț brodat', 'Cod produs': '213489'},
  notes=[VANDUT, 'Pe site e la Geci, deși e o cămașă.', 'Vârsta 4-5 ani pentru XS e estimată după tabelul obișnuit GAP.'], varsta_txt='4-5 ani')

w(14527,
  f'<p>Combinezonul de iarnă {REIMA} TUOHI verde este un {A(SAL, "combinezon unisex")} din material reciclat, respirabil, rezistent la vânt și la apă, care respinge murdăria. Umplutura Fellex ține de cald, iar cusăturile sunt ermetice.</p>'
  '<p>Gluga se detașează, gulerul e înalt, mânecile sunt raglan, iar fermoarul lung, de la gât la picior, are clapetă cu capse. Talia are elastic la spate, mânecile și cracul se termină cu elastic, iar buclele din silicon pentru încălțăminte se scot.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Coloană de apă', '10.000 mm.'), ('Respirabilitate', '6 000 g/m²/24h.'), ('Greutate', '700 g.'))
  + '<p>Mărimile 80-98 sunt gândite pentru cam 1-3 ani.</p>',
  [('model', 'REIMA TUOHI'), ('respirabil', 'material respirabil, rezistent la vânt și la apă, care respinge murdăria'), ('reciclat', 'Materialul utilizat este reciclat'),
   ('Fellex', 'Umplutura Fellex® asigură un confort termic excelent'), ('ermetice', 'cusături ermetice'), ('glugă', 'Are o glugă detașabilă, un guler înalt și mâneci raglan'),
   ('fermoar', 'fermoar pe toată lungimea, de la gât până la picior, acoperit cu o clapetă cu capse'), ('talie', 'talie elastică în partea din spate'),
   ('elastic', 'Mânecile și cracul sunt finisate cu manșete elastice'), ('bucle', 'bucle detașabile din silicon pentru încălțăminte'), ('coloană', '10.000 mm'),
   ('respirabilitate', '6 000 g/m²/24h'), ('greutate', '700 g')],
  {'Model': 'Reima TUOHI', 'Material': '100% poliester reciclat', 'Caracteristici': 'Fellex, glugă detașabilă, fermoar lung', 'Cod produs': '178236'},
  notes=[VANDUT])

w(14531,
  f'<p>Geaca impermeabilă {REIMA} KALLAHTI albastru închis este o {A(GU, "geacă unisex")} ușoară, cu membrană Reimatec care ține copilul uscat pe ploaie. Materialul e impermeabil și respirabil, cusăturile sunt lipite, iar căptușeala din plasă lasă corpul să respire.</p>'
  '<p>Gluga se detașează, manșetele sunt elastice, tivul se ajustează, iar fermoarul merge pe toată lungimea. Are două buzunare laterale cu fermoar.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '50% poliester reciclat, 50% poliester, laminare PU.'), ('Coloană de apă', '3.000 mm.'), ('Respirabilitate', '3 000g/m²/24h.'), ('Greutate', '300 g.'))
  + '<p>Mărimile 110-140 merg orientativ la 5-10 ani.</p>',
  [('model', 'REIMA KALLAHTI'), ('ușoară', 'Geaca cu greutatea redusă'), ('membrană', 'dispune de membrană care asigură copilului climatul uscat pe timp de ploaie'),
   ('impermeabil', 'material impermeabil și respirabil'), ('lipite', 'cusăturile lipite sunt rezistente la apă'), ('plasă', 'căptușeală de plasă'), ('glugă', 'glugă detașabilă'),
   ('manșete', 'manșete elastice'), ('tiv', 'tiv ajustabil'), ('fermoar', 'pe toată lungimea'), ('buzunare', 'două buzunare cu fermoar'),
   ('material', '50 % poliester (reciclat), 50 % poliester, laminare PU'), ('coloană', '3.000 mm'), ('respirabilitate', '3 000g/m²/24h'), ('greutate', '300 g'), ('Reimatec', 'REIMATEC')],
  {'Model': 'Reima KALLAHTI', 'Material': 'poliester, laminare PU', 'Caracteristici': 'Reimatec, cusături lipite, glugă detașabilă', 'Cod produs': '166222'},
  notes=[VANDUT])

w(14654,
  f'<p>Geaca shell {DID} PILVI roz este o {A(GU, "geacă unisex")} de vânt pentru toate anotimpurile, rezistentă la vânt și apă, cu cusături lipite, material respirabil și tratament impermeabil fără PFC. Funcția Extend Size lungește mânecile cu până la o mărime.</p>'
  '<p>Gluga se detașează și se reglează, cu margini elastice, manșetele au bucle pentru mănuși, iar tivul se strânge cu șnur. Are fermoar pe față, buzunare laterale cu velcro, reflectorizante pe mâneci și etichetă pentru mai multe nume.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Coloană de apă', '6.000 mm.'), ('Respirabilitate', '4.000 g/m2/24h.'), ('Material', '100% poliester; 100% poliamidă.'))
  + '<p>Mărimile 90-140 acoperă orientativ 2-10 ani.</p>',
  [('model', 'DIDRIKSONS PILVI'), ('shell', 'Geaca Shell versatilă pentru copii Didriksons PILVI'), ('anotimpuri', 'ideală pentru toate anotimpurile'),
   ('vânt', 'Este rezistentă la vânt și apă, are cusături lipite'), ('PFC', 'tratament impermeabil fără PFC'), ('Extend', 'se pot extinde mânecile cu până la o mărime'),
   ('glugă', 'glugă reglabilă cu margini elastice'), ('mănuși', 'bucle de siguranță pentru mănuși'), ('tiv', 'tiv inferior cu șnur ajustabil'), ('fermoar', 'fermoar pe partea din față'),
   ('velcro', 'buzunare laterale cu velcro'), ('reflectorizant', 'mâneci cu detalii reflectorizante'), ('etichetă', 'o etichetă pentru nume cu spațiu pentru mai multe nume'),
   ('coloană', '6.000 mm'), ('respirabilitate', '4.000 g/m2/24h'), ('material', '100 % poliester'), ('poliamidă', '100% poliamidă')],
  {'Model': 'Didriksons PILVI', 'Material': 'poliester, poliamidă', 'Caracteristici': 'shell, Extend Size, glugă detașabilă', 'Cod produs': '236931'},
  notes=[VANDUT])
