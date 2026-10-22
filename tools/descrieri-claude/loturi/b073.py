import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
GUESS = A('/brand/guess/', 'GUESS')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(12692,
  f'<p>{GEOX} GISLI B461NA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, înalți, cu guler ușor întărit care sprijină glezna, din imitație de piele și material textil, pentru joaca de zi cu zi. Branțul detașabil are imprimeu cu care verificați ușor dacă mărimea mai e bună.</p>'
  '<p>Șireturile elastice și aricii fac încălțatul și descălțatul rapid, iar călcâiul întărit ține piciorul așezat corect.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Interior', 'sintetic și textil, moale.'), ('Talpă', 'plată, din cauciuc.'), ('Partea de sus', 'imitație de piele și textil.'))
  + '<p>Numerele 24-27 se potrivesc băieților de aproximativ 2-4 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii verzi B461NA.054FU'), ('înalt', 'Profil înalt al părții superioare , împreună cu un guler ușor întărit, susține glezna'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('zilnic', 'activitățile și jocurile zilnice'),
   ('branț', 'Branț detașabil , cu imprimeu, care facilitează ajustarea precisă a mărimii'), ('închidere', 'Șireturi elastice și închidere cu arici'),
   ('călcâi', 'Călcâi întărit , care susține stabilizarea călcâiului'), ('interior', 'Interiorul din material sintetic și textil'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice și arici, branț cu verificare de mărime', 'Cod produs': 'B461NA.054FU'})

w(12693,
  f'<p>{GEOX} WASHIBA J55LQD sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, cu profil jos și detalii decorative, din piele naturală, piele ecologică și material textil. Se leagă cu șiret clasic, care se reglează după picior.</p>'
  '<p>Partea de sus e rigidizată și ține forma, cutia rotundă e întărită, iar călcâiul întărit are umplutură moale care îl apără de frecare.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, perforată.'), ('Căptușeală', 'textilă.'), ('Inserție', 'detașabilă, ușor de curățat.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 31-35 sunt pentru băieți de cam 6-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii WASHIBA culoarea verde, J55LQD.05422'), ('profil', 'Înălțime: mic de statură'), ('decor', 'Detalii decorative'),
   ('material', 'combinatie de piele naturala, piele ecologica si material textil'), ('șiret', 'Șiretul clasic permite ajustarea individuală a piciorului'),
   ('rigid', 'Partea superioară rigidizată'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'),
   RESPIRA, ('căptușeală', 'Model cu captuseala textila'), ('inserție', 'Inserție detașabilă, ușor de curățat'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox WASHIBA', 'Material': 'piele naturală, piele ecologică și textil, talpă din cauciuc', 'Caracteristici': 'șiret, Geox Respira, inserție detașabilă', 'Cod produs': 'J55LQD.05422'})

w(12694,
  f'<p>În bleumarin, jacheta {REIMA} Vantti este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} softshell de vânt, fără vată, cu imprimeu vegetal integral, bună pentru primăvară și toamnă, cu straturi pe dedesubt. Suprafața e impregnată ca picăturile să alunece, iar membrana ține 10.000 mm H2O.</p>'
  '<p>Căptușeala din polar acoperă doar o parte și adaugă puțină căldură. Gluga se scoate când nu e nevoie de ea.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Buzunar', 'pe piept, cu fermoar.'), ('Manșete', 'cu nervuri, contra vântului.'), ('Siguranță', 'elemente reflectorizante.'), ('Compoziție', 'poliester cu 8% elastan.'))
  + '<p>Între 86 și 140, mărimile acoperă copii de în jur de 1-10 ani.</p>',
  [('model', 'Reima Jachetă pentru copii Vantti bleumarin 5100009D'), ('softshell', 'Material rezistent la vânt softshell'), ('izolație', 'Fără izolație termică'),
   ('imprimeu', 'Imprimeu vegetal integral'), ('straturi', 'permite stratificarea liberă'), ('impregnare', 'Impregnare hidrofobă a suprafeței materialului'),
   ('H2O', 'Impermeabilitate 10.000 mm H2O'), ('polar', 'Căptușeală parțială din polar'), ('glugă', 'Glugă detașabilă'), ('buzunar', 'Buzunar pe piept , închis cu fermoar'),
   ('manșete', 'Manșete cu nervuri'), ('reflectorizant', 'Elemente reflectorizante'), ('material', '92% Poliester, 8% Elastan')],
  {'Model': 'Reima Vantti', 'Material': '92% poliester, 8% elastan, căptușeală parțială din polar', 'Caracteristici': 'softshell, 10000 mm H2O, glugă detașabilă', 'Cod produs': '5100009D'})

w(12696,
  f'<p>Geaca {GUESS} N6YL03 neagră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, cu model geometric și logo Guess, cu umplutură sintetică de grosime medie, pentru zilele reci de tranziție. Gluga integrată apără de vânt și de ploaia ușoară.</p>'
  '<p>Tivul are șnur elastic, iar manșetele elastice țin căldura și nu lasă mânecile să se ridice. Croiala regulară lasă loc de mișcare.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'completă.'), ('Buzunare', 'imitații, decorative.'), ('Material', '100% poliester.'), ('Croială', 'regulară.'))
  + '<p>Mărimile 88-96 până la 122-125 sunt pentru băieți de vreo 1-7 ani, orientativ.</p>',
  [('model', 'Guess Jachetă pentru copii neagră N6YL03 W2661'), ('matlasat', 'Construcție matlasată cu model geometric'), ('logo', 'Modelul cu logo Guess'),
   ('umplutură', 'Umplutură sintetică de grosime medie'), ('tranziție', 'zilele mai reci de tranziție'), ('glugă', 'Gluga integrată oferă protecție suplimentară împotriva vântului și a ploii ușoare'),
   ('tiv', 'Marginea de jos cu șnur elastic'), ('manșete', 'Manșetele cu elastic contribuie la menținerea căldurii și previn rularea mânecilor'),
   ('căptușeală', 'Căptușeală completă'), ('buzunare', 'Imitația de buzunare'), ('material', '100% Poliester'), ('croială', 'Croiala regulară')],
  {'Model': 'GUESS N6YL03', 'Material': '100% poliester, umplutură sintetică', 'Caracteristici': 'matlasată, glugă integrată, tiv cu șnur elastic', 'Cod produs': 'N6YL03 W2661'})

w(12698,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261242 în bleumarin sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} înalți, de iarnă, izolați, descriși de magazin ca ghete pentru joaca afară pe frig. Membrana BioTEX scoate umezeala și ține un microclimat uscat, iar impregnarea hidrofobă respinge apa.</p>'
  '<p>Șireturile elastice și aricii fac încălțatul ușor, iar vârful și călcâiul întărite țin piciorul în poziție corectă.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Flexi Lite', 'talpă care urmează mișcarea naturală a piciorului.'), ('Talpă', 'plată, din spumă, ușoară.'), ('Podology Partnership', 'lucrat cu podologi.'))
  + '<p>Numerele 28-34 merg la copii de în jur de 4-11 ani.</p>',
  [('model', 'Biomecanics Încălțăminte pentru copii bleumarin 261242'), ('iarnă', 'Ghetele înalte Biomecanics pentru copii sunt încălțăminte de iarnă izolată termic'),
   ('aer liber', 'activitățile de iarnă în aer liber'), ('BioTEX', 'Membrana BioTEX contribuie la menținerea unui microclimat uscat, evacuând umiditatea spre exterior'),
   ('hidrofob', 'Impregnarea hidrofobă a materialului exterior ajută la respingerea apei'), ('închidere', 'Șireturi elastice și închidere cu arici facilitează încălțarea ușoară'),
   ('vârf', 'Vârful și călcâiul întărit'), ('Flexi Lite', 'Sistemul Flexi Lite susține mișcarea naturală a piciorului'), ('talpă', 'Talpa plată din spumă contribuie la lejeritatea încălțămintei'),
   ('Podology', 'Tehnologia Biomecanics Podology Partnership favorizează dezvoltarea corectă a piciorului copilului, datorită colaborării cu podologi')],
  {'Model': 'Biomecanics 261242', 'Material': 'sintetic și textil, interior textil, talpă din spumă', 'Caracteristici': 'izolați, membrană BioTEX, Flexi Lite, șireturi elastice și arici', 'Cod produs': '261242'},
  notes=['Magazinul îi descrie drept ghete înalte de iarnă, izolate; pe site sunt la Pantofi.'])

w(12701,
  f'<p>Cizmele de iarnă {GEOX} negre sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} izolate, din material textil și sintetic, cu fermoar. Tehnologia Amphibiox are o membrană care ține apa afară și lasă aerul să circule, atât în talpă, cât și în partea de sus.</p>'
  '<p>Cutia rotundă e întărită, iar spatele călcâiului e rigidizat, deci cizma își ține forma. Interiorul e confortabil.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Talpă', 'din gumă.'), ('Interior', 'material textil.'))
  + '<p>Numerele 36-39 se potrivesc fetelor de la aproximativ 12 ani în sus.</p>',
  [('model', 'Geox Cizme de iarnă copii culoarea negru'), ('izolat', 'Model Izolat confectionat din combinatia materialului textil cu cel sintetic'), ('fermoar', 'Fixare: cu fermoar'),
   ('Amphibiox', 'Tehnologia Amphibiox®. Membrana special respirabila si nepermeabila protejeaza atat talpa exterioara, cat si cea superioara'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Spatele calcaiului rigidizat'), ('interior', 'Interior confortabil'), RESPIRA, ('talpă', 'Talpa din guma'), ('material', 'Material textil')],
  {'Model': 'Geox (cizme de iarnă)', 'Material': 'textil și sintetic, interior textil, talpă din gumă', 'Caracteristici': 'Amphibiox, Geox Respira, izolate, fermoar', 'Cod produs': ''})

w(12703,
  f'<p>{GEOX} THELEVEN bej sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} înalți, din piele întoarsă, material sintetic și textil, cu gulerul ușor întărit care sprijină glezna. Membrana microporoasă GEOX Respira scoate umezeala și ține picioarele uscate.</p>'
  '<p>Au șireturi elastice și fermoar, deci se încalță și se descalță rapid, fără să desfaceți șiretul. Talpa plată din cauciuc ține bine pe diverse suprafețe.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'piele naturală și textil.'), ('Branț', 'din piele naturală.'), ('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'))
  + '<p>Numerele 28-35 sunt pentru băieți de aproximativ 4-11 ani.</p>',
  [('model', 'Geox THELEVEN sneakers pentru copii bej J46LDC.05422'), ('înalt', 'Profil înalt al părții superioare împreună cu gulerul ușor întărit susține glezna'),
   ('material', 'Partea superioară din combinație de piele întoarsă și materiale sintetice'), ('Respira', 'Tehnologia GEOX Respira™ cu membrană microporoasă favorizează eliminarea umezelii'),
   ('șireturi', 'Șireturi elastice facilitează ajustarea'), ('fermoar', 'Închidere practică cu fermoar permite încălțarea și descălțarea rapidă'),
   ('căptușeală', 'Interior căptușit cu piele naturală și material textil'), ('branț', 'Branț din piele naturală'), ('talpă', 'Talpă plată din cauciuc oferă o bună aderență pe diverse suprafețe'), ('călcâi', 'Călcâi întărit')],
  {'Model': 'Geox THELEVEN', 'Material': 'piele întoarsă, sintetic și textil, interior cu piele, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice și fermoar, branț din piele', 'Cod produs': 'J46LDC.05422'})

w(12704,
  f'<p>Varianta violet a modelului {GEOX} IUPIDOO: {A("/categorie/adidasi/", "adidași pentru fete")} joși, ușori, cu velcro, din textil, piele întoarsă și piele ecologică, pentru fiecare zi. Branțul Geox, din piele cu perforații, e antibacterian și conturat pentru așezarea corectă a piciorului.</p>'
  '<p>Datorită sistemului anti-shock din branț, pașii sunt mai moi. Contrafortul rigid ține călcâiul, iar vârful e ușor întărit.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi cu perforări.'), ('Interior', 'textil și piele naturală.'), ('Talpă exterioară', 'din cauciuc, rezistentă.'))
  + '<p>Numerele încep la 18 și se opresc la 26, pentru fetițe de cam 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii IUPIDOO culoarea violet, B3558C.02214'), ('profil', 'Înălțime: mic de statură'), ('ușor', 'Model ușor și confortabil'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('material', 'combinatie de material textil, piele întoarsă și piele ecologică'),
   ('branț', 'brant din piele cu perforari'), ('antibacterian', 'Are proprietati antibacteriene'), ('contur', 'Este conturat corespunzator pentru o asezare corecta a piciorului'),
   ('anti-shock', 'sistemului anti-shockl'), ('călcâi', 'Contorul de călcâi rigid'), ('vârf', 'Cutie rotunda, usor intarita'), RESPIRA,
   ('interior', 'Material textil, Piele naturala'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox IUPIDOO', 'Material': 'textil, piele întoarsă și piele ecologică, interior textil și piele', 'Caracteristici': 'velcro, branț Geox antibacterian, Geox Respira', 'Cod produs': 'B3558C.02214'})

w(12705,
  f'<p>{GEOX} PERTH J367RE maro sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu partea de sus din imitație de piele, ușor de întreținut, și guler moale care cuprinde glezna. Membrana microporoasă scoate umezeala și oprește apa din exterior, prin tehnologia patentată GEOX Respira.</p>'
  '<p>Aricii, combinați cu șireturi elastice, fac încălțatul rapid. Călcâiul întărit ține piciorul drept.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Interior', 'textil moale.'), ('Talpă', 'plată, din cauciuc.'), ('Partea de sus', 'sintetic și textil.'))
  + '<p>Numerele 36-41 se potrivesc băieților de la vreo 12 ani în sus, orientativ.</p>',
  [('model', 'Geox PERTH sneakers pentru copii maro J367RE.0MEMS'), ('imitație', 'Partea superioară din imitație de piele , care oferă rezistență și un aspect estetic, ușor de întreținut'),
   ('guler', 'Gulerul superior moale , care îmbracă delicat glezna'), ('membrană', 'Membrană microporoasă care elimină eficient umezeala, protejând în același timp împotriva apei din exterior'),
   ('Respira', 'Tehnologia patentată GEOX Respira™'), ('închidere', 'Închidere cu arici , în combinație cu șireturi elastice'), ('călcâi', 'Călcâi întărit'),
   ('interior', 'Interior din material textil'), ('talpă', 'Talpă plată din cauciuc'), ('material', 'Material sintetic, Material textil')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici și șireturi elastice', 'Cod produs': 'J367RE.0MEMS'})

w(12706,
  f'<p>Același model {TH} T1A9-35063, în numere mai mici: {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, uni, cu profil scurt, din imitație de piele care se curăță ușor. Aricii le permit celor mici să se încalțe și să se descalțe repede.</p>'
  '<p>Profilul scurt lasă glezna să se miște liber, iar călcâiul întărit ține piciorul în poziție bună. Talpa plată ține bine pe diverse suprafețe.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil, aerisit.'), ('Talpă', 'plată, din cauciuc.'), ('Model', 'uni, alb.'))
  + '<p>Numerele 24-29 se potrivesc copiilor de aproximativ 2-5 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii albi T1A9-35063'), ('uni', 'Modelul uni în culoarea albă'), ('profil', 'Profilul scurt al feței superioare permite libertate de mișcare a gleznei'),
   ('imitație', 'Fața superioară din imitație de piele conferă încălțămintei un aspect estetic și facilitează curățarea'),
   ('arici', 'Sistemul practic de închidere cu arici facilitează încălțarea și descălțarea rapidă'), ('călcâi', 'Călcâiul întărit stabilizează piciorul'),
   ('interior', 'Interiorul din material textil favorizează circulația aerului'), ('talpă', 'Talpa plată din cauciuc oferă stabilitate și aderență pe diverse suprafețe')],
  {'Model': 'Tommy Hilfiger T1A9-35063', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, profil scurt', 'Cod produs': 'T1A9-35063'})
