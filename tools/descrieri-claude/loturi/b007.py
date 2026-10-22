import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(8722,
  f'<p>{GEOX} J45HXB sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, din material textil și piele ecologică, cu interior textil și tehnologia Geox Respira. Sunt tăiați sub gleznă și au o deschidere largă, ușor de încălțat.</p>'
  '<p>Vârful e rotund și ușor rigid, cu loc ca degetele să stea liber, iar inserția textilă detașabilă se scoate pentru curățat și pentru verificat lungimea piciorului.</p>'
  '<p>La încălțat contează:</p>'
  + L(('Închidere', 'arici.'), ('Călcâi', 'contor rigid.'), ('Deschidere', 'largă.'), ('Inserție', 'textilă, detașabilă.'))
  + '<p>Numerele 28-39 acoperă copii de la aproximativ 4 ani în sus.</p>',
  [('cod', 'J45HXB.000BC'), ('material', 'combinația materialului textil cu pielea ecologică'), ('interior', 'interior textil'), RESPIRA,
   ('sub gleznă', 'Pantoful de sub gleznă'), ('deschidere', 'Deschidere larga'), ('vârf', 'Degetul rotund, ușor rigid'), ('degete', 'degetele se pot aranja liber'),
   ('inserție', 'Inserție textilă detașabilă, ușor de curățat'), ('arici', 'Închiderea cu velcro'), ('călcâi', 'Contorul de călcâi rigid')],
  {'Model': 'Geox J45HXB', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'Geox Respira, arici, deschidere largă, inserție detașabilă', 'Cod produs': 'J45HXB.000BC'},
  notes=['Titlul de pe site spune alb; pagina magazinului din link dă culoarea roz.'])

w(8731,
  f'<p>{A("/brand/reima/", "Reima")} Alppi sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni de iarnă unisex")}, violet, cu umplutură din poliester reciclat și protecția ReimaTec împotriva ploii și a vântului. Sunt făcuți pentru sporturi de iarnă și pentru joaca în zăpadă.</p>'
  '<p>Se închid cu un fermoar scurt, iar mărimea se alege după înălțime, cu loc pentru un strat subțire de corp dedesubt.</p>'
  '<p>Datele tehnice declarate:</p>'
  + L(('Impermeabilitate', '12 000 mm.'), ('Respirabilitate', '7000 g/m2/24h.'), ('Tratament', 'BIONIC-FINISH ECO, hidrofob.'), ('Material', 'poliamidă reciclată și poliamidă acoperită cu poliuretan.'))
  + '<p>Pantalonii au mărimile 92-140, în general pentru 2-10 ani.</p>',
  [('model', 'Reima Alppi violet 5100051B'), ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'), ('frig', 'protejează împotriva frigului'),
   ('umplutură', 'Umplutura: 100% Poliester reciclat'), ('sporturi de iarnă', 'Sporturi de iarnă'), ('fermoar', 'Închiderea cu fermoar scurt'),
   ('impermeabilitate', 'Impermeabilitate: 12 000 mm'), ('respirabilitate', 'Respirabilitate: 7000 g/m2/24h'), ('BIONIC', 'BIONIC-FINISH ECO este o finisare hidrofoba'),
   ('material', '59% Poliamida reciclata, 41% Poliamidă acoperită cu poliuretan')],
  {'Model': 'Reima Alppi', 'Material': 'poliamidă reciclată, umplutură poliester reciclat', 'Caracteristici': 'ReimaTec, impermeabilitate 12 000 mm, BIONIC-FINISH ECO', 'Cod produs': '5100051B'})

w(8735,
  f'<p>{A("/brand/guess/", "GUESS")} N6YL03 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, deschisă la culoare (bej pe site, albă la magazin), cu izolație sintetică medie, pentru zilele mai reci de tranziție. Matlasarea are model geometric, iar logo-ul Guess e la vedere.</p>'
  '<p>Croiala e regulară, iar tivul cu șnur și manșetele cu nervuri strâng geaca jos și la încheieturi, ca să rămână caldă și pe un copil mai slab.</p>'
  '<p>Ce mai are geaca:</p>'
  + L(('Glugă', 'integrată, pentru vânt și ploaie ușoară.'), ('Căptușeală', 'completă.'), ('Buzunare', 'false, decorative.'), ('Material', '100% poliester.'))
  + '<p>Mărimile duble, de la 88-96 până la 122-125, sunt pentru copii de cam 1-7 ani.</p>',
  [('model', 'Jachetă pentru copii albă N6YL03 W2661'), ('izolație', 'Izolație sintetică medie'), ('tranziție', 'zilele mai reci de tranziție'),
   ('matlasare', 'Construcție matlasată cu model geometric'), ('logo', 'Model cu logo Guess'), ('croială', 'Croială regulară'), ('tiv', 'Tiv cu șnur'),
   ('manșete', 'Manșete cu nervuri'), ('glugă', 'Glugă integrată oferă protecție suplimentară împotriva vântului și ploii ușoare'),
   ('căptușeală', 'Căptușeală completă'), ('buzunare', 'Buzunare false'), ('material', '100% Poliester')],
  {'Model': 'GUESS N6YL03', 'Material': '100% poliester, izolație sintetică medie', 'Caracteristici': 'matlasată geometric, glugă integrată, tiv cu șnur, manșete cu nervuri', 'Cod produs': 'N6YL03.W2661'},
  notes=['Titlul de pe site spune bej; magazinul o descrie ca albă.'])

w(8736,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 262103 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} roz, din material textil și piele naturală, fabricați fără nichel și crom. Au fost gândiți împreună cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia.</p>'
  '<p>Aricii fixează pantoful pe picior, iar tăietura în formă de U de la spate lasă glezna să se miște; bucla de la călcâi ajută la încălțat.</p>'
  '<p>Detaliile tălpii și ale interiorului:</p>'
  + L(('Talpă', 'în formă de „picior de elefant” la călcâi.'), ('Branț', 'detașabil, antibacterian.'), ('Vârf', 'protejat.'), ('Inserție', 'perforată.'))
  + '<p>Numerele 19-25 se potrivesc în mare copiilor de 1-3 ani.</p>',
  [('cod', 'Pantofi copii culoarea roz, 262103'), ('material', 'Gamba: Material textil, Piele naturala'), ('nichel', 'fara nichel si crom'),
   ('Valencia', 'medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'), ('arici', 'fixarii cu velcro'), ('U', 'taieturi in forma de U'),
   ('buclă', 'Bucla de la spate'), ('talpă', 'Talpa in forma de „picior de elefant” peste calcaie'), ('branț', 'Brant detasabil si antibacterian'),
   ('vârf', 'Degetul securizat'), ('inserție', 'insertiei perforate')],
  {'Model': 'Biomecanics 262103', 'Material': 'textil și piele naturală, fără nichel și crom', 'Caracteristici': 'arici, tăietură în U, branț antibacterian detașabil', 'Cod produs': '262103'})

w(8740,
  f'<p>{GEOX} J16FAB sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} maro, din piele naturală și piele ecologică, cu sistemul Geox Respira. Magazinul îi trece la încălțămintea de iarnă, dar nu au izolație, așa că se potrivesc mai ales toamna și primăvara.</p>'
  '<p>Se închid cu șnur și fermoar: fermoarul deschide pantoful la încălțat, iar șnurul rămâne reglat pe picior.</p>'
  '<p>Construcția pantofului:</p>'
  + L(('Vârf', 'rotund, întărit.'), ('Călcâi', 'rigidizat la spate.'), ('Interior', 'sintetic și textil.'))
  + '<p>Pe site sunt numerele 28-35, pentru copii de aproximativ 4-11 ani.</p>',
  [('cod', 'Geox maro J16FAB.032BC'), ('material', 'combinatia pielii naturale cu pielea ecologica'), RESPIRA, ('iarnă', 'Pantofi de iarna pentru copii'),
   ('neizolat', 'Izolare: neizolat'), ('fermoar', 'Fixare: cu fermoar'), ('șnur', 'Fixare: cu snur'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Spatele calcaiului rigidizat'),
   ('interior', 'Interiorul: Material sintetic, Material textil')],
  {'Model': 'Geox J16FAB', 'Material': 'piele naturală și piele ecologică, interior sintetic și textil', 'Caracteristici': 'Geox Respira, șnur și fermoar, neizolați', 'Cod produs': 'J16FAB.032BC'})

w(8745,
  f'<p>{A("/brand/liewood/", "Liewood")} Denisa sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} roz, din material textil, cu design simplu și neted. Magazinul îi propune pentru jocurile în aer liber și pentru activitățile de la grădiniță.</p>'
  '<p>Aricii le permit copiilor să se încalțe singuri, iar gulerul și călcâiul întărite țin piciorul în pantof.</p>'
  '<p>Din ce e făcut:</p>'
  + L(('Exterior', 'textil.'), ('Căptușeală', 'textilă, moale.'), ('Talpă', 'din cauciuc.'))
  + '<p>Cu numere de la 22 la 35, modelul se găsește pentru copii de cam 1 an până la 11 ani.</p>',
  [('model', 'Liewood Denisa Sneakers pentru copii roz LW20059'), ('exterior', 'Exteriorul din material textil'), ('neted', 'design simplu, neted'),
   ('utilizare', 'jocurilor în aer liber și al activităților preșcolare'), ('arici', 'Sistemul practic de închidere cu arici'), ('guler', 'Gulerul întărit'),
   ('călcâi', 'Călcâi întărit'), ('căptușeală', 'Căptușeala textilă moale'), ('talpă', 'Talpa din cauciuc')],
  {'Model': 'Liewood Denisa', 'Material': 'textil, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'arici, guler și călcâi întărite', 'Cod produs': 'LW20059'})

w(8746,
  f'<p>{GEOX} SPRINTYE sunt {A("/categorie/adidasi/", "adidași pentru fete")} argintii, ușori, din material textil și piele ecologică, de purtat zilnic. Talpa are sistemul Geox Respira, în trei straturi, cu perforații, iar exteriorul combină sinteticul cu textilul.</p>'
  '<p>Se închid cu arici și au o buclă la spate, deci copilul îi pune singur; profilul e scurt, sub gleznă, iar branțul textil ține pantoful mai ușor curat.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Branț', 'textil.'), ('Interior', 'textil.'))
  + '<p>Numerele de pe site, 28-35, sunt pentru copii de aproximativ 4-11 ani.</p>',
  [('model', 'Sneakers pentru copii SPRINTYE culoarea argintiu, J55FWA.0ASAJ'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('zilnic', 'ideal pentru purtarea zilnică'), RESPIRA, ('arici', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'), ('profil', 'Înălțime: mic de statură'),
   ('talpă', 'Talpa exterioară din cauciuc'), ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'), ('interior', 'Interiorul: Material textil'), ('material', 'Gamba: Material sintetic, Material textil')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil și piele ecologică, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici, buclă la spate', 'Cod produs': 'J55FWA.0ASAJ'})

w(8748,
  f'<p>{TH} T3X9-35233 în varianta bleumarin sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} din imitație de piele, cu profil scurt și închidere cu șiret. Se poartă ușor la ținute casual.</p>'
  '<p>Șiretul permite strângerea exactă pe picior, iar gulerul ușor întărit înconjoară glezna fără margini tari.</p>'
  '<p>Ce are pe dinăuntru și pe dedesubt:</p>'
  + L(('Talpă', 'din cauciuc, plată.'), ('Călcâi', 'întărit.'), ('Interior', 'căptușit cu material textil.'), ('Branț', 'textil.'))
  + '<p>Numerele 30-41 îi fac potriviți, în general, pentru copii de la 6 ani în sus.</p>',
  [('model', 'Sneakers pentru copii bleumarin T3X9-35233'), ('material', 'Partea superioară din imitație de piele'), ('profil', 'profil scurt și închidere cu șiret'),
   ('casual', 'ținute casual'), ('șiret', 'Închiderea cu șiret permite o ajustare precisă'), ('guler', 'Gulerul superior ușor întărit'),
   ('talpă', 'Talpa din cauciuc cu profil plat'), ('călcâi', 'Călcâiul întărit'), ('interior', 'Interiorul căptușit cu material textil'), ('branț', 'Branțul din material textil')],
  {'Model': 'Tommy Hilfiger T3X9-35233', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'profil scurt, șiret, călcâi întărit', 'Cod produs': 'T3X9-35233'})

w(8750,
  f'<p>Cizmele {GEOX} de aici sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")}, roz, izolate, din material textil și piele ecologică, cu sistemul Geox Tex Waterproof pentru rezistență la apă. Magazinul precizează că nu garantează impermeabilitate completă.</p>'
  '<p>Partea de sus se strânge cu șnur, deci cizma se închide pe gambă și ține zăpada afară pe sus.</p>'
  '<p>Pentru zăpadă, contează și:</p>'
  + L(('Talpă', 'sculptată.'), ('Vârf', 'rotund, întărit.'), ('Călcâi', 'rigidizat.'), ('Geox Respira', 'talpă în trei straturi.'))
  + '<p>Numerele 36-39 sunt pentru copii mari, de obicei de la 12 ani în sus.</p>',
  [('tip', 'Cizme de zapada pentru copii'), ('izolat', 'Model izolat'), ('material', 'combinatia materialului textil cu pielea ecologica'),
   ('Geox Tex', 'Geox Tex Waterproof'), ('nu complet', 'nu garantează impermeabilitatea completă'), ('șnur', 'Partea superioara este cu snur'),
   ('talpă', 'Talpa sculptata'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Spatele calcaiului rigidizat'), RESPIRA, ('culoare', 'roz')],
  {'Model': 'Geox, cizme de zăpadă', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'izolate, Geox Tex Waterproof, șnur la gambă, Geox Respira', 'Cod produs': ''},
  notes=['Titlul de pe site nu are culoare; magazinul arată roz.'])

w(8754,
  f'<p>{TH} T3A3-32580 sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} negri, din piele întoarsă, cu talpă din cauciuc și branț din piele. Interiorul combină textilul cu pielea naturală.</p>'
  '<p>Se închid cu arici, deci se fixează repede, la un picior îngust sau lat, iar contorul de călcâi, foarte rigid, ține piciorul în pantof, ca să nu alunece la mers.</p>'
  '<p>Ce îi ține în formă:</p>'
  + L(('Vârf', 'rotund, întărit.'), ('Călcâi', 'foarte rigid.'), ('Branț', 'din piele.'), ('Talpă', 'exterioară, din cauciuc.'))
  + '<p>Pe site sunt numerele 28-39, de obicei pentru copii de 4 ani și peste.</p>',
  [('cod', 'Pantofi copii culoarea negru, T3A3-32580'), ('material', 'confecționat din piele intoarsa'), ('talpă', 'Talpa exterioară din cauciuc'),
   ('branț', 'Brantul din piele'), ('interior', 'Interiorul: Material textil, Piele naturala'), ('arici', 'Închiderea cu velcro'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Călcâiul puternic rigid'), ('nu alunecă', 'ține piciorul în pantof, astfel încât să nu alunece')],
  {'Model': 'Tommy Hilfiger T3A3-32580', 'Material': 'piele întoarsă, interior textil și piele naturală, talpă din cauciuc', 'Caracteristici': 'arici, branț din piele, călcâi rigid', 'Cod produs': 'T3A3-32580'})
print('lot 7 scris')
