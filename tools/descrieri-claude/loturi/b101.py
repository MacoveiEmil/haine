import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')

w(14192,
  f'<p>Pantofii sport {A("/brand/geox/", "Geox")} MAWAZY B bej sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} cu aspect modern și casual, din piele întoarsă moale, piele Nappa, material textil și sintetic. Preiau șocurile la pas și lasă aerul să circule, fiind gândiți pentru școală și joacă.</p>'
  '<p>Talpa e din cauciuc termoplastic, iar culoarea bej are detalii roz și albastru deschis.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Față', '42% sintetic, 27% textil, 21% piele întoarsă, 10% piele Nappa.'), ('Talpă', 'TPR.'), ('Stil', 'casual, modern.'))
  + '<p>Numerele 28-35 se potrivesc copiilor de aproximativ 4-11 ani.</p>',
  [('model', 'Geox MAWAZY B'), ('culoare', 'bej (bej / roz / albastru deschis)'), ('modern', 'moderni și casual'), ('material', 'Sunt confecționați din piele întoarsă moale și țesătură'),
   ('respirabil', 'beneficiază de amortizare și oferă respirabilitate'), ('școală', 'fiind ideali pentru școală și joacă'),
   ('față', '42% sintetic; 27% textil, 21% piele întoarsă, 10% piele Nappa'), ('talpă', 'TPR (cauciuc termoplastic)')],
  {'Model': 'Geox MAWAZY B', 'Material': 'sintetic, textil, piele întoarsă și piele Nappa, talpă TPR', 'Caracteristici': 'casual, respirabili', 'Cod produs': '192424'},
  notes=['Pagina nu spune tipul de închidere.'])

w(14196,
  f'<p>Geaca matlasată {A("/brand/willard/", "Willard")} LESS albastru închis este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} căptușită cu microfibre Dupont, care țin de cald, din țesătură fină și densă. Pe vreme urâtă se poate purta ca strat intermediar sub o geacă impermeabilă.</p>'
  '<p>Fermoarul e acoperit și are protecție la bărbie, gluga fixă și mânecile au elastic, iar partea de jos se reglează. Spatele e mai lung.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două, în față, cu fermoar.'), ('Reflectorizante', 'da.'), ('Material', '100% nailon, căptușeală din poliester.'))
  + '<p>Mărimile 122-170 sunt pentru copii de aproximativ 7-15 ani.</p>',
  [('model', 'Willard LESS'), ('culoare', 'Albastru închis (albastru închis / albastru)'), ('Dupont', 'microfibre Dupont care garantează confort termic'),
   ('țesătură', 'țesătură fină și densă'), ('strat', 'poate fi utilizată ca strat intermediar sub o geacă impermeabilă'),
   ('fermoar', 'Fermoarul principal este acoperit și dotat cu protecție la bărbie'), ('glugă', 'glugă fixă'), ('elastic', 'mânecile și gluga sunt cu elastic'),
   ('jos', 'posibilitate de ajustare a părții de jos'), ('spate', 'partea din spate este prelungită'), ('buzunare', 'două buzunare frontale cu fermoar'),
   ('reflectorizant', 'elemente reflectorizante'), ('material', '100% nailon'), ('căptușeală', '100% poliester')],
  {'Model': 'Willard LESS', 'Material': '100% nailon, căptușeală din poliester, microfibre Dupont', 'Caracteristici': 'matlasată, glugă fixă, protecție la bărbie', 'Cod produs': '1168017549'})

w(14203,
  f'<p>Ghetele barefoot {REIMA} HYPPII kaki sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} vegani pentru micii exploratori, cu membrană impermeabilă și căptușeală confortabilă, care țin picioarele uscate. Drop zero ține piciorul în poziție naturală, iar vârful lat lasă loc degetelor.</p>'
  '<p>Velcro-ul face încălțatul ușor, iar talpa flexibilă din cauciuc ține bine pe sol. Elementele reflectorizante ajută seara.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Inserție', 'detașabilă.'), ('Față', 'cauciuc, poliester, poliuretan.'), ('Greutate', '240 g, fără fluorocarbon și PVC.'))
  + '<p>Numerele 22-31 se potrivesc copiilor de aproximativ 1-7 ani.</p>',
  [('model', 'REIMA HYPPII'), ('culoare', 'Kaki (kaki / verde închis)'), ('barefoot', 'Ghetele barefoot pentru copii Reima HYPPII sunt concepute pentru micii exploratori'),
   ('vegan', 'vegane'), ('membrană', 'Oferă o membrană impermeabilă și o căptușeală confortabilă'), ('drop', 'drop zero pentru o poziție naturală'),
   ('vârf', 'vârful lat oferă spațiu suplimentar pentru degete'), ('velcro', 'Închiderea velcro asigură o utilizare ușoară'), ('talpă', 'talpă din cauciuc pentru o aderență mai bună'),
   ('reflectorizant', 'elemente reflectorizante'), ('inserție', 'inserție detașabilă'), ('față', 'cauciuc, poliester, poliuretan'), ('greutate', '240 g'), ('PVC', 'fără fluorocarbon și PVC')],
  {'Model': 'Reima HYPPII', 'Material': 'cauciuc, poliester, poliuretan', 'Caracteristici': 'barefoot, membrană impermeabilă, velcro, drop zero', 'Cod produs': '220332'},
  notes=['Magazinul le numește ghete; pe site sunt la Pantofi.'])

w(14219,
  f'<p>Geaca {A("/brand/loap/", "LOAP")} URANIX roz este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} pentru activități în aer liber pe vreme rece, cu partea de sus din TECNOSOFT, rezistent la frecare și murdărie, care oprește vântul. Fața și gluga fixă sunt izolate cu fleece STORMEX Ultrasonic.</p>'
  '<p>Croiala e clasică, cu spatele ușor prelungit, iar fermoarul are capac la bărbie. Mânecile și tivul sunt elastice.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două, cu fermoar.'), ('Reflectorizante', 'da.'), ('Material', '92% poliester, 8% elastan (Tecnosoft).'))
  + '<p>Mărimile 112-116 până la 158-164 sunt pentru copii de cam 5-14 ani.</p>',
  [('model', 'LOAP URANIX'), ('culoare', 'Roz (roz / negru)'), ('aer liber', 'să se bucure de orice activitate în aer liber, chiar și pe vreme rece'),
   ('Tecnosoft', 'Partea superioară TECNOSOFT nu este doar rezistentă la abraziune și murdărie, ci protejează în mod eficient împotriva vântului'),
   ('Stormex', 'Partea din față și gluga sunt izolate cu fleece STORMEX Ultrasonic'), ('glugă', 'glugă fixă'), ('croială', 'croială clasică, cu spate ușor extins'),
   ('fermoar', 'Fermoarul este prevăzut cu capac care previne ciupirea dureroasă a pielii la nivelul bărbiei'), ('elastic', 'Mâneca și tivul inferior sunt elastice'),
   ('buzunare', '2 buzunare cu fermoar'), ('reflectorizant', 'elemente reflectorizante'), ('material', '92 % poliester, 8 % elastan (Tecnosoft)')],
  {'Model': 'LOAP URANIX', 'Material': 'Tecnosoft (poliester cu elastan), fleece Stormex', 'Caracteristici': 'izolată în față și la glugă, fermoar cu capac', 'Cod produs': '164670'})

w(14235,
  f'<p>Ghetele outdoor {REIMA} EHTII maro sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} impermeabile, pe gleznă, cu membrană, pentru oraș și pentru ieșiri în natură. Talpa Vibram ține foarte bine pe toate suprafețele, iar partea de sus e ușoară și respirabilă.</p>'
  '<p>Se leagă cu șireturi și se încalță ușor. Stratul exterior, fără fluorocarbon, respinge apa și murdăria.</p>'
  '<p>Din ce sunt făcute:</p>'
  + L(('Branț', 'anatomic, detașabil, cu imprimeu Happy Fit.'), ('Căptușeală', 'textilă, 100% poliester.'), ('Talpă', '50% EVA, 50% cauciuc.'))
  + '<p>Numerele 28-38 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'REIMA EHTII'), ('culoare', 'Maro (maro / roșu / bej)'), ('impermeabil', 'Ghetele impermeabile pentru copii'), ('membrană', 'ghete pe gleznă cu membrană'),
   ('oraș', 'sunt concepute pentru oraș și pentru activități în aer liber'), ('Vibram', 'Talpa Vibram este foarte aderentă pe toate suprafețele'),
   ('ușor', 'parte superioară ușoară și respirabilă'), ('șireturi', 'fixare cu șireturi'), ('fluor', 'strat superior fără fluorocarbon care respinge apa și murdăria'),
   ('branț', 'Branțul anatomic detașabil'), ('Happy Fit', 'imprimeu Happy Fit'), ('căptușeală', 'căptușeală din textil'), ('talpă', '50 % EVA, 50 % cauciuc')],
  {'Model': 'Reima EHTII', 'Material': 'poliester, poliuretan, nailon, talpă EVA și cauciuc', 'Caracteristici': 'membrană, talpă Vibram, Happy Fit', 'Cod produs': '178377'},
  notes=['Descrierea magazinului scrie o dată ENTII; modelul e EHTII.'])

w(14238,
  f'<p>Geaca impermeabilă {A("/brand/kilpi/", "KILPI")} JALUU-J galbenă este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} de ploaie, cu membrană SIBERIUM 10 000 2L, 10 000 mm coloană de apă și 5 000 g/m²/24h respirabilitate. Cusăturile sunt lipite, iar gluga fixă, reglabilă în adâncime, are guler mai înalt.</p>'
  '<p>Orificiile de aerisire de pe spate și de la subraț reduc transpirația, iar tivul se ajustează. Se împachetează în săculețul inclus.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Reflectorizante', 'da.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 98-164 sunt pentru copii de aproximativ 3-14 ani.</p>',
  [('model', 'KILPI JALUU-J'), ('culoare', 'Galben (galben / negru)'), ('impermeabil', 'Geaca impermeabilă pentru copii KILPI JALUU-J'), ('Siberium', 'SIBERIUM 10000 2L'),
   ('coloană', 'material impermeabil cu o coloană de apă de 10 000 mm'), ('respirabilitate', 'respirabilitate de 5 000 g/m²/24h pentru confort'), ('lipite', 'cusături lipite pentru o protecție mai bună'),
   ('glugă', 'gluga robustă, cu adâncime reglabilă și guler mai înalt'), ('aerisire', 'Orificiile de aerisire de pe spate și de la subraț'), ('tiv', 'tivul inferior ajustabil'),
   ('săculeț', 'Se poate împacheta ușor în săculețul inclus'), ('buzunare', '2 laterale cu fermoar'), ('reflectorizant', 'elemente reflectorizante pentru siguranță mai mare'),
   ('material', '100 % poliester')],
  {'Model': 'KILPI JALUU-J', 'Material': '100% poliester, membrană Siberium', 'Caracteristici': '10 000 mm, cusături lipite, aerisiri, se împachetează', 'Cod produs': '290924'})

w(14265,
  f'<p>Setul termo {REIMA} TAITOA, roz după titlul de pe site, e listat la {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopete unisex")}, dar e un strat de bază din tricot cu două fețe: Tencel moale, care absoarbe umezeala, și lână, care ține de cald chiar dacă copilul transpiră. E potrivit pentru vremea rece.</p>'
  '<p>Cusăturile plate și moi nu freacă pielea, iar talia e elastică. Imprimeul acoperă toată suprafața.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '48% lână, 43% lyocell, 9% poliamidă.'), ('Greutate', '270 g.'), ('Talie', 'elastică.'))
  + '<p>Mărimile 100-150 sunt pentru copii de aproximativ 3-12 ani.</p>',
  [('model', 'REIMA TAITOA'), ('set', 'Set termo pentru copii'), ('Tencel', 'Tencel® moale și mătăsos pentru absorbția umezelii'), ('lână', 'lână pentru asigurarea căldurii la nivelul stratului de bază'),
   ('transpiră', 'menține căldura, chiar dacă copilul transpiră'), ('rece', 'adecvat pentru vremea rece'), ('cusături', 'cusături plate moi pentru un plus de confort - fără frecare'),
   ('talie', 'talie elastică'), ('imprimeu', 'imprimeu pe toată suprafața'), ('material', '48% lână, 43% lyocel, 9% poliamidă'), ('greutate', '270 g')],
  {'Model': 'Reima TAITOA (set termo)', 'Material': '48% lână, 43% lyocell, 9% poliamidă', 'Caracteristici': 'strat de bază, lână și Tencel, cusături plate', 'Cod produs': '260009'},
  notes=['Pagina magazinului arată VÂNDUT și nu dă culoarea; culoarea e cea din titlu.', 'E set termo (strat de bază), listat la Salopete.'])

w(14301,
  f'<p>Salopeta cu membrană {REIMA} TOPPILA albastră este o {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopetă unisex")} din material respirabil, rezistent la apă și vânt, cu membrană Reimatec, 10.000 mm coloană de apă și cusături impermeabile, lipite. Finisajul BIONIC-FINISH ECO respinge apa și murdăria, iar materialele sunt certificate bluesign.</p>'
  '<p>Fermoarul lung, oblic, de la gât la picior, ușurează îmbrăcatul. Gluga se detașează, talia se reglează pe interior, iar cracii au bandă de silicon sub talpă.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'netedă, din poliester reciclat.'), ('Buzunar', 'lateral, cu fermoar.'), ('Reflectorizante', 'da.'))
  + '<p>Mărimile 80-98 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'REIMA TOPPILA'), ('culoare', 'Albastru (albastru / mix)'), ('material', 'material funcțional, respirabil, rezistent la apă și vânt, care respinge murdăria'),
   ('Reimatec', 'Reimatec'), ('coloană', '10.000 mm'), ('cusături', 'impermeabile, lipite'), ('BIONIC', 'finisaj rezistent la apă și murdărie BIONIC-FINISH®ECO fără fluorocarburi'),
   ('bluesign', 'Materialele folosite sunt certificate bluesign®'), ('fermoar', 'fermoar lung, de la gât până la picior, în formă oblică'), ('glugă', 'glugă detașabilă'),
   ('talie', 'Talia este ajustabilă de pe interior'), ('silicon', 'Cracul dispune de bandă de silicon care se poate fixa sub talpa piciorului'),
   ('căptușeală', 'căptușeală netedă din poliester de fibre reciclate'), ('buzunar', 'buzunar cu fermoar'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea')],
  {'Model': 'Reima TOPPILA', 'Material': 'poliester parțial reciclat, laminat PU', 'Caracteristici': 'Reimatec, 10.000 mm, glugă detașabilă, benzi sub talpă', 'Cod produs': ''})

w(14313,
  f'<p>Tricoul {A("/brand/gap/", "GAP")} RAGLAN FASHION gri e listat la {A("/categorie/unisex-imbracaminte-geci-jachete/", "geci unisex")}, dar e un tricou imprimat cu logo GAP 1969, cu mâneci raglan în culoare contrastantă și decolteu rotund cu tiv. Croiala dreaptă și tricotul moale îl fac comod.</p>'
  '<p>E din bumbac 100%, în gri cu detalii roșii și turcoaz.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Mâneci', 'raglan, contrastante.'), ('Decolteu', 'rotund.'))
  + '<p>Mărimile, de la L la XXL, corespund de obicei copiilor mai mari, de aproximativ 10-16 ani; verificați tabelul magazinului.</p>',
  [('model', 'GAP RAGLAN FASHION'), ('culoare', 'Gri (gri / roșu / turcoaz)'), ('imprimat', 'Tricoul imprimat pentru copii GAP RAGLAN FASHION'), ('logo', 'logo GAP 1969'),
   ('raglan', 'mâneci lungi raglan într-o culoare contrastantă'), ('decolteu', 'decolteu rotund cu tiv'), ('croială', 'croială dreaptă'), ('tricot', 'tricot moale'), ('material', '100 % bumbac')],
  {'Model': 'GAP RAGLAN FASHION', 'Material': '100% bumbac', 'Caracteristici': 'mâneci raglan contrastante, logo GAP 1969', 'Cod produs': '213478'},
  varsta_txt='10-16 ani', notes=['Mărimile sunt în litere (L-XXL), fără tabel; vârsta e estimată.', 'Descrierea spune și mânecă scurtă, și mâneci lungi; n-am precizat lungimea mânecii.', 'E tricou, listat la Geci.'])

w(14321,
  f'<p>Cizmele de zăpadă {REIMA} NEFAR mov sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} care apără picioarele de umezeală și frig, cu partea de jos din cauciuc termoplastic și carâmb din material rezistent la apă, cu finisaj hidrofob. Partea de sus se strânge, ca zăpada să nu intre.</p>'
  '<p>Căptușeala din micro fleece ține de cald, iar înșiretarea rapidă face încălțatul ușor. Talpa ține bine pe orice teren.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'textil și sintetic.'), ('Izolație', '100% poliester.'), ('Greutate', '450 g.'))
  + '<p>Gama 20-35 acoperă copii de aproximativ 1-11 ani.</p>',
  [('model', 'REIMA NEFAR'), ('culoare', 'Mov (mov / negru)'), ('zăpadă', 'Cizmele de zăpadă pentru copii REIMA NEFAR protejează fiabil picioarele de umezeală și frig'),
   ('cauciuc', 'Partea inferioară este realizată din cauciuc termoplastic'), ('carâmb', 'Carâmbul cizmei este din material rezistent la apă'), ('hidrofob', 'finisaj hidrofob'),
   ('sus', 'Partea de sus a cizmei este ajustabilă, deci nu permite pătrunderea zăpezii'), ('fleece', 'Căptușeala din micro fleece asigură confortul termic'),
   ('înșiretare', 'înșiretare rapidă'), ('talpă', 'talpă foarte aderentă pe orice suprafață de teren'), ('față', 'material textil și sintetic'), ('izolație', '100 % poliester'), ('greutate', '450 g')],
  {'Model': 'Reima NEFAR', 'Material': 'textil și sintetic, cauciuc termoplastic, micro fleece', 'Caracteristici': 'cizme de zăpadă, înșiretare rapidă, gură reglabilă', 'Cod produs': '259901'})
