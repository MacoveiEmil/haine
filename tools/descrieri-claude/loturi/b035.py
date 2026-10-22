import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
COLUMBIA = A('/brand/columbia/', 'Columbia')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9967,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KS0KS00707 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză cu glugă pentru băieți")}, bleumarin, cu imprimeu, din țesătură subțire, ușor elastică, jumătate poliester reciclat, jumătate bumbac reciclat. Gluga încorporată ține de cald când bate vântul.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile și tivul au bordură care strânge la încheieturi și pe șolduri, ca bluza să nu se ridice când copilul se întinde.</p>'
  '<p>Pentru purtat la școală sau afară, bluza are:</p>'.replace('la școală sau afară', 'zi de zi')
  + L(('Buzunar', 'tip cangur, în față.'), ('Material', '50% poliester reciclat, 50% bumbac reciclat.'), ('Elasticitate', 'țesătură ușor elastică.'))
  + '<p>Mărimile 128-176 se potrivesc copiilor de pe la 8 până pe la 16 ani.</p>',
  [('model', 'Tommy Hilfiger Bluză copii culoarea bleumarin, cu glugă, cu imprimeu, KS0KS00707'), ('subțire', 'țesătură subțire, usor elastica'),
   ('material', '50% Poliester reciclat, 50% Bumbac reciclat'), ('glugă', 'Gluga încorporată oferă un plus de căldură'), ('croială', 'Tăiere simplă, fără blocare'),
   ('bordură', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('buzunar', 'Un buzunar cangur practic'), ('imprimeu', 'Model cu imprimeu')],
  {'Model': 'Tommy Hilfiger KS0KS00707', 'Material': '50% poliester reciclat, 50% bumbac reciclat', 'Caracteristici': 'glugă, buzunar cangur, ușor elastică, imprimeu', 'Cod produs': 'KS0KS00707'})

w(9976,
  f'<p>Botinele {PRIMIGI} PRX 23584 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete pentru bebeluși")} negre, din imitație de piele cu finisaj lăcuit și o aplicație discretă, pentru sezonul de tranziție. Sunt făcute după sistemul Primigi × SIPeP, creat în colaborare cu podologi.</p>'
  '<p>Închiderea e dublă, cu șireturi și fermoar: șiretul strânge botina după picior, iar fermoarul o deschide larg la încălțat.</p>'
  '<p>Înăuntru și dedesubt, botina are:</p>'
  + L(('Branț', 'din piele naturală.'), ('Căptușeală', 'textilă.'), ('Vârf și călcâi', 'întărite.'), ('Talpă', 'plată, din cauciuc, cu Shock Absorber.'))
  + '<p>Numerele 21-26 se poartă, în jur de, de la 1 la 4 ani.</p>'.replace('se poartă, în jur de, de la 1 la 4 ani', 'sunt pentru copii de în jur de 1-4 ani'),
  [('model', 'Primigi Botine pentru copii negre PRX 23584'), ('lăcuit', 'Partea superioară din imitație de piele , cu finisaj lăcuit'), ('aplicație', 'Aplicație subtilă'),
   ('tranziție', 'sezonul de tranziție'), ('SIPeP', 'Sistemul Primigi × SIPeP'), ('podologi', 'creat în colaborare cu podologi'),
   ('închidere', 'Închidere dublă , combinând șireturi și fermoar'), ('branț', 'Branț din piele naturală'), ('căptușeală', 'Căptușeală textilă'),
   ('vârf', 'Vârf rotund, întărit'), ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpă plată din cauciuc'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă')],
  {'Model': 'Primigi PRX 23584', 'Material': 'imitație de piele lăcuită, branț din piele naturală, căptușeală textilă', 'Caracteristici': 'șireturi și fermoar, Shock Absorber, Primigi × SIPeP', 'Cod produs': 'PRX 23584'})

w(9985,
  f'<p>{COLUMBIA} Hikebound 2115921 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de ploaie pentru băieți")}, portocalie, neizolată, din material impermeabil cu tehnologia Omni-tech®: membrană microporoasă și cusături sudate acoperite cu strat impermeabil. E pentru ploaie și zilele de tranziție.</p>'
  '<p>Croiala e simplă, dreaptă, cu loc pentru un pulover, iar mânecile au bandă elastică la capăt, care strânge la încheieturi și ține apa afară.</p>'
  '<p>La drum pe vreme urâtă, contează:</p>'
  + L(('Glugă', 'da.'), ('Închidere', 'fermoar și velcro.'), ('Căptușeală', 'din plasă.'), ('Buzunare', 'două, laterale, cu fermoar.'))
  + '<p>Mărimile 104-164 sunt pentru copii de în general 4-14 ani.</p>'.replace('de în general 4-14 ani', 'de 4-14 ani, în general'),
  [('model', 'Columbia Geacă copii Hikebound culoarea portocaliu, 2115921'), ('neizolat', 'Model neizolat'), ('impermeabil', 'material impermeabil'), ('Omni-tech', 'Tehnologia Omni-tech®'),
   ('membrană', 'membranei microporoase, respirabile si a cusaturilor sudate acoperite cu un strat impermeabil'), ('tranziție', 'Izolare: tranzitional'),
   ('croială', 'Tăiere simplă, fără blocare'), ('elastic', 'Mâneci finisate cu o coadă elastică'), ('glugă', 'Model cu gluga'), ('închidere', 'Fixarea cu fermoar si velcro'),
   ('plasă', 'Căptușeala este realizată dintr-un material plasă'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar')],
  {'Model': 'Columbia Hikebound', 'Material': '100% poliester, căptușeală din plasă', 'Caracteristici': 'Omni-tech®, cusături sudate, neizolată, glugă', 'Cod produs': '2115921'})

w(9993,
  f'<p>Pantofii {GEOX} ZAPITO B556DA sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} albi, din material textil și piele ecologică, cu partea de sus neporoasă, care se curăță cu o cârpă umedă. Branțul Light Flexy lasă piciorul să se miște, iar talpa are sistemul Geox Respira.</p>'
  '<p>Velcro-ul se închide repede și se strânge după picior, iar contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece în pantof.</p>'
  '<p>Mai sunt de știut:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Interior', 'textil, ușor de ținut curat.'), ('Geox Respira', 'talpă în trei straturi, cu perforări.'))
  + '<p>Numerele 19-26 sunt pentru cei mici de pe la 1 până pe la 4 ani.</p>',
  [('model', 'Geox Pantofi copii ZAPITO culoarea alb, B556DA.0AW54'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'), ('Light Flexy', 'Light Flexy Sistem de brant pentru libertatea de miscare'), RESPIRA,
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('călcâi', 'Contorul de călcâi rigid'),
   ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('vârf', 'Cutie rotunda, intarita'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Geox ZAPITO', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'velcro, branț Light Flexy, Geox Respira', 'Cod produs': 'B556DA.0AW54'})

w(9997,
  f'<p>{PRIMIGI} PYR 14214 sunt {A("/categorie/adidasi/", "adidași barefoot pentru fete")}, albi, cu talpă Vibram flexibilă, care lasă piciorul să simtă solul la fiecare pas. Partea de sus e din imitație de piele, durabilă și ușor de întreținut, pentru activitățile de zi cu zi.</p>'
  '<p>Calapodul e lat și lasă loc degetelor, deci pantoful merge bine și pe un picior mai lat. Șireturile elastice cu scai se strâng repede, fără nod.</p>'
  '<p>Pe dinăuntru, pantoful are:</p>'
  + L(('Branț', 'detașabil, din piele naturală.'), ('Interior', 'material textil moale.'), ('Contrafort', 'ușor rigidizat.'))
  + '<p>Numerele 30-33 sunt, cu aproximație, pentru 6-9 ani.</p>',
  [('model', 'Primigi Sneakers pentru copii albi PYR 14214'), ('barefoot', 'Adidașii barefoot Primigi'), ('Vibram', 'Tehnologia Vibram'), ('flexibil', 'Talpa flexibilă'),
   ('sol', 'simțirea naturală a solului'), ('material', 'Materialul exterior din imitație de piele este durabil și ușor de întreținut'), ('zilnic', 'activitățile de zi cu zi'),
   ('calapod', 'Calapodul lat al pantofului oferă spațiu degetelor'), ('închidere', 'Șireturile elastice și închiderea cu scai facilitează încălțarea rapidă și ajustarea'),
   ('branț', 'Branțul din piele naturală este detașabil'), ('interior', 'Materialul textil moale din interior'), ('contrafort', 'Contrefortul ușor rigidizat')],
  {'Model': 'Primigi PYR 14214', 'Material': 'imitație de piele, interior textil, branț din piele', 'Caracteristici': 'barefoot, talpă Vibram, calapod lat, șireturi elastice cu scai', 'Cod produs': 'PYR 14214'})

w(9999,
  f'<p>Sandalele {GEOX} BOREALIS J450RE sunt {A("/categorie/baieti-incaltaminte-sandale/", "sandale sport pentru băieți")}, negre, ușoare, cu partea de sus din material textil care se usucă repede după ce intră în apă. Sunt pentru vară și joacă în aer liber, la apă sau pe drumuri de vacanță.</p>'.replace(', la apă sau pe drumuri de vacanță', '')
  + '<p>Vârful e decupat, deci degetele au loc și aer, iar baretele cu logo GEOX țin sandala pe picior la alergat.</p>'.replace('iar baretele cu logo GEOX țin sandala pe picior la alergat', 'iar pe baretă e logo-ul GEOX')
  + '<p>Talpa e partea cea mai lucrată:</p>'
  + L(('Talpă exterioară', 'din cauciuc, cu striații.'), ('Talpă profilată', 'pentru mers și alergat.'), ('Geox Respira™', 'tehnologie pentru picioare uscate.'), ('Interior', 'material sintetic.'))
  + '<p>Numerele 36-39 sunt pentru adolescenți de la, de regulă, 12 ani în sus.</p>',
  [('model', 'Geox Sandale copii BOREALIS negre J450RE.01411'), ('sport', 'Sandale sport pentru copii'), ('ușor', 'încălțăminte ușoară'),
   ('textil', 'Partea superioară din material textil favorizează uscarea rapidă după contactul cu apa'), ('vară', 'aventurile de vară'), ('aer liber', 'activitățile în aer liber'),
   ('vârf', 'Vârful decupat'), ('logo', 'Logo-ul GEOX de pe baretă'), ('talpă', 'Talpa exterioară din cauciuc cu striații'),
   ('profilată', 'Talpa profilată susține stabilitatea în timpul mersului și al alergatului'), ('Respira', 'Tehnologia Geox Respira™'), ('interior', 'Material sintetic')],
  {'Model': 'Geox BOREALIS', 'Material': 'textil, interior sintetic, talpă din cauciuc', 'Caracteristici': 'sport, uscare rapidă, vârf decupat, Geox Respira™', 'Cod produs': 'J450RE.01411'})

w(10006,
  f'<p>{GEOX} KALISPERA J664GB sunt {A("/categorie/adidasi/", "adidași înalți pentru fete")}, bej, cu partea de sus din material sintetic și branț din piele naturală, pentru ținutele de zi cu zi. Talpa cu membrană Geox Respira™ scoate umezeala și ține picioarele uscate.</p>'
  '<p>Au trei închideri, șireturi, scai și fermoar, deci pantoful se reglează bine pe picior și se încalță ușor. Profilul înalt cuprinde glezna.</p>'
  '<p>Înăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'din material textil.'), ('Branț', 'din piele naturală.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 24-35 sunt, de obicei, pentru 2-11 ani.</p>',
  [('model', 'Geox KALISPERA sneakers pentru copii bej J664GB.0NFEW'), ('material', 'Partea superioară din material sintetic'), ('branț', 'Branțul din piele naturală'),
   ('zilnic', 'ținute de zi cu zi'), ('Respira', 'Tehnologia GEOX Respira™ asigură picioare uscate, grație tălpii cu membrană, care elimină umezeala'),
   ('închidere', 'Sistemul triplu de închidere (șireturi, scai, fermoar)'), ('profil', 'Profilul înalt al părții superioare'), ('căptușeală', 'Căptușeala din material textil'),
   ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox KALISPERA', 'Material': 'sintetic, căptușeală textilă, branț din piele naturală', 'Caracteristici': 'profil înalt, șireturi, scai și fermoar, Geox Respira™', 'Cod produs': 'J664GB.0NFEW'})

w(10007,
  f'<p>{GEOX} FLEXYPER J459BB sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, ușori, cu profil scurt, din material textil, piele ecologică și piele întoarsă, pentru purtat zilnic. Talpa are sistemul Geox Respira, cu trei straturi perforate.</p>'
  '<p>Șireturile elastice și cârligul permit încălțatul fără legat, iar contrafortul rigid ține călcâiul în pantof, ca piciorul să nu alunece la alergat.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Vârf', 'cutie rotundă, ușor întărită.'), ('Interior', 'textil, se ține ușor curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 28-39 sunt pentru copii de pe la 4 ani în sus.</p>',
  [('model', 'Geox Sneakers pentru copii FLEXYPER culoarea bleumarin, J459BB.0FU22'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinatie de material textil, piele ecologică și piele întoarsă'), ('zilnic', 'purtarea zilnică'), RESPIRA,
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('călcâi', 'Contorul de călcâi rigid'),
   ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('vârf', 'Cutie rotunda, usor intarita'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox FLEXYPER', 'Material': 'textil, piele ecologică și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J459BB.0FU22'})

w(10013,
  f'<p>Pantofii {A("/brand/wheat/", "Wheat")} WF626-02 sunt {A("/categorie/incaltaminte-pantofi/", "pantofi casual pentru fete")}, roz, ușori, din pânză imprimată cu model floral, pentru primăvară și vară. Interiorul e din bumbac imprimat, iar branțul moale din latex e acoperit cu piele fără crom.</p>'
  '<p>Velcro-ul se închide repede și se reglează pe picior, iar vârful rotund, întărit, lasă degetele să se miște. Contrafortul și gulerul sunt ușor rigidizate.</p>'
  '<p>Pe scurt:</p>'
  + L(('Partea de sus', 'pânză (material textil).'), ('Interior', 'bumbac imprimat.'), ('Talpă', 'din cauciuc, flexibilă.'))
  + '<p>Mărimile 21-28 sunt pentru copii de în jur de 1-5 ani.</p>',
  [('model', 'Wheat Pantofi pentru copii roz WF626-02'), ('ușor', 'încălțăminte ușoară'), ('pânză', 'Partea superioară din pânză imprimată'), ('floral', 'model floral delicat'),
   ('sezon', 'activitățile de primăvară și vară'), ('interior', 'Interiorul din bumbac imprimat'), ('branț', 'Branțul moale din latex , acoperit cu piele fără crom'),
   ('velcro', 'Închiderea practică cu velcro facilitează încălțarea rapidă și ajustarea pantofului'), ('vârf', 'Vârful rotund și întărit permite libertatea de mișcare a degetelor'),
   ('călcâi', 'Contragreutatea călcâiului ușor rigidizată'), ('guler', 'Gulerul părții superioare ușor rigidizat'), ('talpă', 'Talpa din cauciuc permite o bună aderență și flexibilitate')],
  {'Model': 'Wheat WF626-02', 'Material': 'pânză imprimată, interior din bumbac, branț din latex cu piele fără crom', 'Caracteristici': 'velcro, model floral, vârf întărit', 'Cod produs': 'WF626-02'})

w(10033,
  f'<p>{COLUMBIA} Powder Lite 2090023 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, neagră, din material neted, cu izolație sintetică groasă și tehnologia OMNI-HEAT™ THERMAL REFLECTIVE, care reflectă căldura corpului înapoi. E pentru activitățile de iarnă și zilele reci.</p>'
  '<p>Croiala e regular fit, cu loc pentru straturi dedesubt, deci peste un pulover gros nu strânge. Gluga nu se detașează și apără capul de frig.</p>'
  '<p>Geaca mai are:</p>'
  + L(('Căptușeală', 'completă, cu imprimeu cu puncte.'), ('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-164 sunt pentru copii de cu aproximație 4-14 ani.</p>'.replace('de cu aproximație 4-14 ani', 'de 4-14 ani, cu aproximație'),
  [('model', 'Columbia Jachetă pentru copii Powder Lite neagră 2090023'), ('neted', 'Materialul negru, neted'), ('izolație', 'izolație sintetică groasă'),
   ('Omni-Heat', 'Tehnologia OMNI-HEAT™ THERMAL REFLECTIVE ajută la menținerea căldurii corpului prin reflectarea radiației acestuia'),
   ('iarnă', 'activitățile de iarnă și utilizarea zilnică în zilele reci'), ('croială', 'Modelul cu croială regular fit favorizează libertatea de mișcare și permite îmbrăcarea în straturi'),
   ('glugă', 'Gluga nedetașabilă oferă o protecție suplimentară pentru cap împotriva frigului'), ('căptușeală', 'Căptușeala completă'),
   ('puncte', 'Imprimeul special cu puncte de pe căptușeală'), ('fermoar', 'Închiderea cu fermoar pe toată lungimea'), ('buzunare', 'Buzunarele laterale practice'),
   ('material', '100% Poliester')],
  {'Model': 'Columbia Powder Lite', 'Material': '100% poliester', 'Caracteristici': 'OMNI-HEAT™ THERMAL REFLECTIVE, izolație groasă, glugă fixă', 'Cod produs': '2090023'})
