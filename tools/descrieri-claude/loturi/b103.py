import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
GECI = '/categorie/unisex-imbracaminte-geci-jachete/'
GHETE = '/categorie/unisex-incaltaminte-ghete-cizme/'
VANDUT = 'Pagina magazinului arată produsul ca VÂNDUT și nu dă culoarea; culoarea e cea din titlul site-ului.'

w(14485,
  f'<p>Geaca {REIMA} ANISE roșie este o {A(GECI, "geacă unisex")} de vânt, din material respirabil, tratat cu BIONIC-FINISH ECO fără fluorocarburi, care respinge apa și murdăria. Cusăturile principale sunt lipite, iar materialul conține fibre reciclate certificate.</p>'
  '<p>Gluga se detașează, iar căptușeala netedă de poliester face îmbrăcatul ușor. Elementele reflectorizante îl fac pe copil vizibil, iar materialul e rezistent la joacă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două, în față.'), ('Material', '100% poliester.'), ('Tehnologie', 'Reimatec.'))
  + '<p>Mărimile 116-152 sunt pentru copii de aproximativ 6-12 ani.</p>',
  [('model', 'REIMA ANISE'), ('culoare', 'Roșu (roșu / roz / negru)'), ('vânt', 'Geaca pentru copii Reima ANISE protejează de vânt'),
   ('BIONIC', 'respinge apa și murdăria datorită materialului BIONIC-FINISH®ECO fără fluor de carburi'), ('lipite', 'cusăturile principale sunt lipite'),
   ('reciclat', 'conține fibre reciclate de calitate, certificate'), ('glugă', 'glugă detașabilă'), ('căptușeală', 'Căptușeala netedă de poliester facilitează îmbrăcarea'),
   ('reflectorizant', 'elemente reflectorizante'), ('buzunare', '2 în față'), ('material', '100 % poliester'), ('Reimatec', 'REIMATEC'), ('rezistent', 'material rezistent')],
  {'Model': 'Reima ANISE', 'Material': '100% poliester', 'Caracteristici': 'cusături lipite, glugă detașabilă, BIONIC-FINISH ECO', 'Cod produs': '198020'})

w(14486,
  f'<p>Tricoul de baie {REIMA} SUKELTAJA roz e un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "tricou unisex")} cu mânecă lungă raglan, din material elastic Reima SunProof, cu protecție UV 50+, bun pentru plajă. Se întreține ușor, se usucă repede și elimină umezeala.</p>'
  '<p>Partea din față e căptușită, pentru o acoperire mai bună, iar croiala e potrivită pe corp. Materialul conține fibre reciclate certificate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '83% poliester, 17% elastan.'), ('Mânecă', 'lungă, raglan.'), ('Greutate', '130 g.'))
  + '<p>Mărimile 104-140 sunt pentru copii de cam 4-10 ani.</p>',
  [('model', 'REIMA SUKELTAJA'), ('culoare', 'Roz (roz / galben)'), ('baie', 'Tricoul de baie pentru copii REIMA SUKELTAJA'), ('SunProof', 'material elastic Reima SunProof'),
   ('UV', 'factor de protecție UV 50+'), ('plajă', 'Indicat pentru purtarea la plajă'), ('întreținere', 'Materialul se întreține ușor, are uscare rapidă și elimină perfect umezeala'),
   ('căptușit', 'Partea din față este căptușită'), ('croială', 'croială potrivită'), ('raglan', 'mânecă raglan'), ('reciclat', 'conține fibre reciclate certificate'), ('material', '83 % poliester, 17 % elastan'), ('greutate', '130 g')],
  {'Model': 'Reima SUKELTAJA', 'Material': '83% poliester, 17% elastan', 'Caracteristici': 'UV 50+, mânecă lungă, uscare rapidă', 'Cod produs': '239990'})

w(14489,
  f'<p>Cizmele de iarnă {REIMA} SOPHIS negre sunt {A(GHETE, "ghete unisex")} impermeabile, cu membrană Reimatec, izolație din vatelină și căptușeală moale din fleece și lână. Branțul din pâslă are un strat izolator din aluminiu, care ține căldura înăuntru și frigul afară.</p>'
  '<p>Carâmbul are cauciuc cusut în două locuri, ca să se încalțe ușor, iar talpa din cauciuc termoplastic ține bine. Stratul exterior, fără fluor, respinge apa și murdăria.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'poliester, poliuretan, poliamidă, elastan.'), ('Izolație', '84% poliester, 16% lână.'), ('Greutate', '910 g.'))
  + '<p>Numerele 28-38 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'REIMA SOPHIS'), ('culoare', 'Negru'), ('impermeabil', 'ghete de iarnă impermeabile'), ('membrană', 'sunt prevăzute cu membrană și izolație din vatelină'),
   ('Reimatec', 'Reimatec'), ('fleece', 'căptușeală confecționată dintr-un amestec de lână și fleece'), ('pâslă', 'Branțul este confecționat din pâslă'),
   ('aluminiu', 'materialul termoizolant pe bază de aluminiu ajută la menținerea căldurii înăuntru și a frigului afară'),
   ('carâmb', 'Carâmbul superior este cusut cu cauciuc în două locuri, astfel încât încălțămintea se poate încălța ușor'),
   ('talpă', 'talpă din cauciuc termoplastic cu aderență bună'), ('fluor', 'strat superior fără fluorocarbon care respinge apa și murdăria'),
   ('reflectorizant', 'elemente reflectorizante'), ('față', '84 % poliester, 11 % poliuretan, 5 % poliamidă, 1 % elastan'), ('izolație', '84 % poliester, 16 % lână'), ('greutate', '910 g')],
  {'Model': 'Reima SOPHIS', 'Material': 'poliester și poliuretan, izolație cu lână, talpă TPR', 'Caracteristici': 'Reimatec, branț din pâslă cu aluminiu, fleece', 'Cod produs': '178394'})

w(14507,
  f'<p>Sandalele barefoot {REIMA} RANTAAN roz, listate la {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")}, sunt foarte ușoare, fără PFAS, cu partea de sus din textil fără PVC, bune pentru plajă și alte activități de vară. Drop zero și forma lată, cu loc pentru degete, țin piciorul în poziție naturală.</p>'
  '<p>Velcro-ul face încălțatul ușor, iar talpa subțire și flexibilă din cauciuc ține piciorul sigur și pe teren accidentat. Se spală la mașină, la 30 °C.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Branț', 'detașabil, Happy Fit.'), ('Față', 'material textil.'), ('Talpă', 'cauciuc.'))
  + '<p>Numerele 24-32 se potrivesc copiilor de aproximativ 2-9 ani.</p>',
  [('model', 'REIMA RANTAAN'), ('culoare', 'Roz (roz / alb)'), ('ușor', 'Sandale barefoot pentru copii Reima RANTAAN sunt foarte ușoare și confortabile'),
   ('PFAS', 'fără conținut de PFAS'), ('PVC', 'partea superioară fără PVC, confecționată din material textil'), ('plajă', 'ideale pentru plajă și toate celelalte activități de vară'),
   ('drop', 'drop zero pentru o poziție naturală'), ('lat', 'încălțăminte lată cu spațiu suplimentar pentru degete'), ('velcro', 'se încheie cu velcro'),
   ('talpă', 'Talpa flexibilă și subțire conferă stabilitate pe diferite suprafețe'), ('accidentat', 'plimbări pe teren accidentat'),
   ('spălare', 'se pot spăla la mașina de spălat, program delicat la 30 °C'), ('branț', 'branțul detașabil Happy Fit'), ('cauciuc', 'talpă din cauciuc pentru o aderență mai bună')],
  {'Model': 'Reima RANTAAN', 'Material': 'textil, talpă din cauciuc', 'Caracteristici': 'barefoot, velcro, lavabile la 30 °C', 'Cod produs': '277962'},
  notes=['Magazinul le numește sandale; pe site sunt la Pantofi.'])

w(14508,
  f'<p>Adidașii {A("/brand/geox/", "Geox")} J THELEVEN negri sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} cu două benzi velcro, care se încalță ușor și se fixează bine pe picior. Construcția robustă și talpa texturată țin pasul sigur la fiecare mișcare, chiar și la alergat.</p>'
  '<p>Partea de sus e din material sintetic rezistent și arată elegant, iar adidașii merg și la activitățile de zi cu zi, și la sport.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Închidere', 'două benzi velcro.'), ('Față', 'sintetic.'), ('Talpă', 'cauciuc, texturată.'))
  + '<p>Numerele 27-35 se potrivesc copiilor de aproximativ 3-11 ani.</p>',
  [('model', 'Geox J THELEVEN'), ('culoare', 'Negru'), ('velcro', 'au un sistem de închidere practic cu două benzi velcro, se încălță ușor și se fixează bine'),
   ('robust', 'Construcția robustă cu talpă texturată asigură stabilitate la fiecare pas'), ('rezistent', 'Materialul este rezistent și elegant'),
   ('activități', 'Sunt potriviți pentru activități cotidiene și activități sportive'), ('față', 'sintetic'), ('talpă', 'cauciuc')],
  {'Model': 'Geox J THELEVEN', 'Material': 'sintetic, talpă din cauciuc', 'Caracteristici': 'două benzi velcro, talpă texturată', 'Cod produs': '253670'})

w(14511,
  f'<p>Cizmele impermeabile {REIMA} TALVES, albastre după titlul de pe site, sunt {A(GHETE, "ghete unisex")} de iarnă, cu membrană care ține degetele uscate și căptușeală izolată din fleece și puf, testată până la -20 °C. Talpa Rolling Steps face pasul ușor, iar cauciucul termoplastic ține bine.</p>'
  '<p>Velcro-ul și șireturile elastice permit o fixare după picior. Detaliile reflectorizante ajută pe lumină slabă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Branț', 'din pâslă, detașabil, cu Happy Fit.'), ('Cusături', 'etanșate.'), ('Greutate', '450 g.'))
  + '<p>Numerele 28-38 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'REIMA TALVES'), ('impermeabil', 'Cizmele impermeabile pentru copii Reima TALVES'), ('membrană', 'Au o membrană impermeabilă care menține degetele uscate'),
   ('-20', 'căptușeala izolată din fleece/puf asigură căldură testată până la -20 °C'), ('Rolling', 'designul tălpii Rolling Steps facilitează mersul copiilor'),
   ('talpă', 'talpă din cauciuc termoplastic cu aderență bună'), ('velcro', 'Sistemul de închidere ușor cu velcro, împreună cu șireturile elastice'),
   ('reflectorizant', 'detaliile reflectorizante îmbunătățesc vizibilitatea în condiții de lumină slabă'), ('branț', 'branț detașabil din pâslă cu imprimeu Happy Fit'),
   ('cusături', 'inserție impermeabilă cu cusături etanșate'), ('greutate', '450 g')],
  {'Model': 'Reima TALVES', 'Material': 'sintetic și textil, căptușeală fleece', 'Caracteristici': 'impermeabile, -20 °C, velcro și șireturi elastice', 'Cod produs': '259944'},
  notes=[VANDUT])

w(14516,
  f'<p>Pălăria {REIMA} RANTSU albastru închis e unul dintre {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "accesoriile unisex")} de vară, cu stil simplu și bor prelungit la spate, care apără de soare și fața, și gâtul. Materialul ușor are protecție UV 50+.</p>'
  '<p>Se leagă cu șnur sub bărbie, deci rămâne pe cap la joacă. Borul modelat la spate acoperă și ceafa.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Protecție', 'UV 50+.'), ('Prindere', 'șnur sub bărbie.'))
  + '<p>Mărimile 46-52 sunt circumferința capului, pentru copii de la aproximativ 1 an în sus.</p>',
  [('model', 'REIMA RANTSU'), ('culoare', 'Albastru închis'), ('bor', 'Pălăria pentru copii REIMA RANTSU are borul la spate modelat'),
   ('gât', 'Nu protejează de soare numai fața, ci și gâtul'), ('UV', 'factor de protecție UV 50+'), ('ușor', 'Materialul ușor dispune de factor de protecție UV'),
   ('șnur', 'Se leagă cu șnur sub bărbie'), ('simplu', 'stil simplu'), ('material', '100 % poliester reciclat')],
  {'Model': 'Reima RANTSU', 'Material': '100% poliester reciclat', 'Caracteristici': 'UV 50+, bor prelungit la spate, șnur', 'Cod produs': '240012'},
  varsta_txt='de la 1 an în sus', notes=['Mărimile sunt circumferința capului în cm; vârsta e dată orientativ.'])

w(14558,
  f'<p>Geaca de schi {A("/brand/picture/", "Picture")} SEADY bej este o {A(GECI, "geacă unisex")} în două straturi, color-block, din poliester reciclat, cu membrană 10K/10K și finisaj hidrofug fără PFC. Umplutura din puf sintetic e foarte caldă, iar cusăturile critice sunt lipite.</p>'
  '<p>Gluga ergonomică se reglează, manșetele au velcro și lycra cu orificii pentru degetul mare, iar geaca se prinde de pantaloni. Sistemul Grow-with-me o lasă să crească odată cu copilul.</p>'
  '<p>Buzunarele:</p>'
  + L(('Piept', 'cu fermoar YKK.'), ('Ski-pass', 'buzunar dedicat.'), ('Interior', 'buzunar din plasă.'))
  + '<p>Mărimile 116-164 sunt pentru copii de aproximativ 6-14 ani.</p>',
  [('model', 'Picture SEADY'), ('culoare', 'bej (bej / portocaliu)'), ('straturi', 'Geaca în două straturi Picture SEADY'), ('schi', 'tinerii schiori și snowboarderi'),
   ('reciclat', 'Fabricată din poliester reciclat sustenabil'), ('membrană', 'membrană 10K/10K'), ('PFC', 'un finisaj hidrofug durabil fără PFC'),
   ('puf', 'geaca călduroasă din puf sintetic'), ('color-block', 'stilul său clasic color-block'), ('lipite', 'cusături critice lipite'), ('glugă', 'glugă ergonomică ajustabilă'),
   ('manșete', 'manșete ajustabile cu velcro'), ('lycra', 'tricot din lycra cu orificii pentru degetul mare'), ('pantaloni', 'se poate conecta cu pantalonii'),
   ('Grow', 'sistem Grow-with-me'), ('piept', 'buzunar la piept cu fermoar YKK'), ('ski-pass', 'buzunar pentru permis de schi'), ('interior', 'buzunar de plasă pe interior')],
  {'Model': 'Picture SEADY', 'Material': '52% poliester reciclat, 48% poliester', 'Caracteristici': '10K/10K, Grow-with-me, puf sintetic', 'Cod produs': '187046'})

w(14565,
  f'<p>Geaca de vânt {REIMA} SOUTU, roz după titlul de pe site, este o {A(GECI, "geacă unisex")} clasică pentru primăvară și toamnă, din material respirabil, rezistent la apă și vânt, care respinge murdăria. Materialul conține fibre de poliester reciclate, certificate bluesign, iar cusăturile sunt lipite.</p>'
  '<p>Gluga se detașează, iar manșetele și tivul se reglează după copil, ca vântul să nu intre pe dedesubt.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două, în față, cu fermoar.'), ('Material', '100% poliester.'), ('Tehnologie', 'Reimatec.'))
  + '<p>Mărimile 104-164 sunt pentru copii de cam 4-14 ani.</p>',
  [('model', 'REIMA SOUTU'), ('vânt', 'Geaca rezistentă la vânt pentru copii Reima SOUTU'), ('sezon', 'ideal pentru zilele de primăvară și toamnă'),
   ('material', 'material funcțional respirabil, rezistent la apă și vânt și care respinge murdăria'), ('bluesign', 'certificată de societatea bluesign®'),
   ('reciclat', 'Materialul conține fibră de poliester reciclată'), ('lipite', 'Are cusături lipite, rezistente la apă'), ('glugă', 'glugă detașabilă'),
   ('manșete', 'manșete și tiv ajustabile'), ('buzunare', '2 în față cu fermoar'), ('poliester', '100 % poliester'), ('Reimatec', 'REIMATEC')],
  {'Model': 'Reima SOUTU', 'Material': '100% poliester', 'Caracteristici': 'cusături lipite, glugă detașabilă, bluesign', 'Cod produs': '239977'},
  notes=[VANDUT])

w(14591,
  f'<p>Geaca de schi {A("/brand/loap/", "LOAP")} OKSA albastru închis este o {A(GECI, "geacă unisex")} cu croială îngustă în talie, din material impermeabil STORMEX, cu 5000 mm coloană de apă și 5000 g/m²/24h respirabilitate. Membrana AQUAPRO și umplutura POLYTHERM țin copilul uscat și la cald.</p>'
  '<p>Gluga are guler din blană artificială, mânecile se reglează cu velcro și au manșete elastice, iar pe interior e o centură de zăpadă. Fermoarul are protecție la bărbie.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'două laterale și unul pe mânecă.'), ('Tiv', 'ajustabil.'), ('Reflectorizante', 'da.'))
  + '<p>Mărimile 128-164 sunt pentru copii de aproximativ 8-14 ani.</p>',
  [('model', 'LOAP OKSA'), ('culoare', 'Albastru închis (albastru închis / roz)'), ('croială', 'croială îngustă în talie'), ('Stormex', 'material impermeabil STORMEX cu o coloană de apă de 5000 mm'),
   ('respirabilitate', 'o respirabilitate de 5000 g/m²/24h'), ('AQUAPRO', 'Membrana AQUAPRO, căptușeala și umplutura POLYTHERM asigură un climat uscat și confortul termic'),
   ('blană', 'Gluga cu guler din blană artificială'), ('velcro', 'mâneci ajustabile cu velcro'), ('manșete', 'manșete elastice'), ('centură', 'centură de zăpadă'),
   ('bărbie', 'fermoar cu protecție la bărbie'), ('buzunare', '3 (2x laterale, 1x pe mânecă)'), ('tiv', 'tiv ajustabil'), ('reflectorizant', 'elemente reflectorizante')],
  {'Model': 'LOAP OKSA', 'Material': '100% poliester (Stormex), umplutură Polytherm', 'Caracteristici': 'AQUAPRO, 5000 mm, centură de zăpadă, glugă cu blană artificială', 'Cod produs': '1503018081'})
