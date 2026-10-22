import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(10295,
  f'<p>{A("/brand/new-balance/", "New Balance")} LAKB0287 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă matlasată unisex")}, neagră, cu izolație sintetică medie și impregnare hidrofobă, pentru zilele mai reci de tranziție și ploile ușoare. Materialul de bază e un amestec de bumbac și nailon.</p>'
  '<p>Croiala e regulară, cu loc pentru straturi în plus pe dedesubt, iar manșetele cu nervuri strâng la încheieturi și opresc frigul. Gluga integrată apără de vânt și burniță.</p>'
  '<p>Pentru lucrurile mici, geaca are:</p>'
  + L(('Buzunare laterale', 'cu fermoar.'), ('Buzunar interior', 'aproape de corp.'), ('Căptușeală', 'sintetică, completă.'), ('Material', '60% bumbac, 40% nailon.'))
  + '<p>Mărimile 122-128 până la 170-176 sunt pentru copii de în jur de 7-16 ani.</p>',
  [('model', 'New Balance Geacă petrecută pentru copii neagră LAKB0287'), ('matlasat', 'Construcția matlasată'), ('izolație', 'Izolația sintetică medie'),
   ('hidrofob', 'Impregnarea hidrofobă a materialului favorizează rezistența crescută la umiditate în timpul ploilor ușoare'), ('tranziție', 'zilele mai reci de tranziție'),
   ('material', '60% Bumbac, 40% Nailon'), ('croială', 'Croiala regulară favorizează libertatea de mișcare, permițând purtarea confortabilă a straturilor suplimentare'),
   ('manșete', 'Manșetele cu nervuri'), ('glugă', 'Gluga integrată oferă protecție suplimentară capului împotriva vântului și ploii ușoare'),
   ('buzunare', 'Buzunarele laterale cu fermoar'), ('buzunar interior', 'Buzunarul interior'), ('căptușeală', 'Căptușeala sintetică completă')],
  {'Model': 'New Balance LAKB0287', 'Material': '60% bumbac, 40% nailon; căptușeală 100% nailon', 'Caracteristici': 'matlasată, izolație medie, impregnare hidrofobă, glugă integrată', 'Cod produs': 'LAKB0287'})

w(10306,
  f'<p>Pantofii {GEOX} din piele sunt {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi pentru băieți")} negri, din piele naturală, cu interior din material textil și piele. Branțul Geox e din piele perforată, antibacterian, cu sistem anti-shock și conturat pentru așezarea piciorului.</p>'
  '<p>Scaiul se închide repede și se strânge după picior, iar spatele călcâiului rigidizat ține piciorul în pantof. Vârful e rotund.</p>'
  '<p>Talpa are și ea ceva de spus:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Talpă', 'din material sintetic.'), ('Partea de sus', 'piele naturală.'))
  + '<p>Numerele 28-35 sunt, de regulă, pentru copii de 4-11 ani.</p>',
  [('model', 'Geox Incaltaminte din piele pentru copii culoarea negru'), ('piele', 'Model confectionat din piele naturala'), ('interior', 'Material textil, Piele naturala'),
   ('branț', 'brant din piele cu perforari'), ('antibacterian', 'Are proprietati antibacteriene'), ('anti-shock', 'sistemului anti-shockl'),
   ('contur', 'Este conturat corespunzator pentru o asezare corecta a piciorului'), ('scai', 'Incheiere cu scai'), ('călcâi', 'Spatele calcaiului rigidizat'),
   ('vârf', 'Varf rotund'), RESPIRA, ('talpă', 'Material sintetic')],
  {'Model': 'Geox (pantofi din piele)', 'Material': 'piele naturală, interior textil și piele', 'Caracteristici': 'scai, branț din piele antibacterian, Geox Respira', 'Cod produs': ''})

w(10316,
  f'<p>{GEOX} STEPPIEUP B6563A sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} albi, ușori, cu profil scurt, din material textil și piele naturală, pentru purtat zi de zi. Inserția din piele e făcută fără crom, iar talpa are sistemul Geox Respira.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, deci pantoful vine bine și pe un picior mai plin. Scaiul se închide repede, iar contrafortul rigidizat ține călcâiul.</p>'
  '<p>Pentru purtat zilnic, contează și:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, perforată.'), ('Interior', 'material textil.'), ('Partea de sus', 'textil și piele naturală.'))
  + '<p>Numerele 20-27 sunt pentru copii de pe la 1 până pe la 4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii STEPPIEUP culoarea alb, B6563A.08514'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea naturală'), ('zilnic', 'purtarea zilnică'), ('crom', 'Inserția din piele a fost realizată fără utilizarea cromului'),
   RESPIRA, ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('scai', 'Incheiere cu scai'), ('călcâi', 'Contorul de călcâi rigidizat'),
   ('interior', 'Interiorul: Material textil')],
  {'Model': 'Geox STEPPIEUP', 'Material': 'textil și piele naturală, interior textil', 'Caracteristici': 'scai, cutie lată, Geox Respira', 'Cod produs': 'B6563A.08514'})

w(10325,
  f'<p>Paltonul {A("/brand/marc-jacobs/", "Marc Jacobs")} W60566 este un {A("/categorie/geci-jachete/", "palton pentru fete")}, negru, subțire, din material ornamentat cu lână, acril și poliester, căptușit. E pentru sezonul de tranziție, cu mânecă lungă și guler moale.</p>'
  '<p>Croiala e simplă, dreaptă, deci cade lejer peste o rochie sau un pulover subțire. Nu are glugă, iar gulerul moale stă bine la gât.</p>'
  '<p>Pe scurt, despre palton:</p>'
  + L(('Material', '38% acril, 31% lână, 30% poliester, 1% modacril.'), ('Căptușeală', '53% poliester, 47% viscoză.'), ('Guler', 'moale.'))
  + '<p>Mărimile 114-150 sunt pentru copii de cam 6-12 ani.</p>',
  [('model', 'MARC JACOBS Palton copii culoarea negru, W60566'), ('subțire', 'Model subțire confecționat din material ornamentat'), ('căptușit', 'Captuseala: cu captuseala'),
   ('tranziție', 'Izolare: tranzitional'), ('mânecă', 'Maneca lunga'), ('guler', 'Model cu guler moale'), ('croială', 'Tăiere simplă, fără blocare'), ('fără glugă', 'Gluga: fara gluga'),
   ('material', '38% Acril, 31% Lana, 30% Poliester , 1% Modacril'), ('căptușeală', '53% Poliester , 47% Viscoza')],
  {'Model': 'Marc Jacobs W60566', 'Material': '38% acril, 31% lână, 30% poliester, 1% modacril; căptușeală poliester și viscoză', 'Caracteristici': 'palton subțire, căptușit, guler moale', 'Cod produs': 'W60566'})

w(10338,
  f'<p>{A("/brand/wheat/", "Wheat")} 0659-366-GOTS este o {A("/categorie/bluze-tricouri-hanorace/", "bluză cu mânecă lungă pentru fete")}, bej, din bumbac organic 100%, cu broderie anglaise și încrețituri delicate. Se poartă singură sau sub un pulover, în orice anotimp.</p>'
  '<p>Croiala e lejeră, iar spatele e puțin mai lung, deci acoperă spatele când copilul se apleacă. Materialul nu e elastic, așa că bluza își păstrează forma după purtare.</p>'
  '<p>La îmbrăcat, contează:</p>'
  + L(('Decolteu', 'rotund, nu strânge.'), ('Închidere', 'buclă elastică cu nasture la spate.'), ('Material', '100% bumbac organic.'))
  + '<p>Mărimile 98-152 sunt pentru copii de, în general, 3-12 ani.</p>'.replace('de, în general, 3-12 ani', 'de 3-12 ani, în general'),
  [('model', 'Wheat Longsleeve pentru copii din bumbac bej 0659-366-GOTS'), ('bumbac', '100% Bumbac organic'), ('broderie', 'Adorabila broderie anglaise și încrețiturile delicate'),
   ('straturi', 'ideal pentru a crea ținute stratificate sau ca piesă de sine stătătoare'), ('anotimp', 'se va potrivi în orice anotimp'), ('croială', 'Croiala lejeră'),
   ('spate', 'Spatele puțin mai lung'), ('neelastic', 'Materialul neelastic ajută la menținerea formei'),
   ('decolteu', 'Decolteul rotund se așază confortabil, fără a strânge'), ('buclă', 'bucla elastică cu nasture')],
  {'Model': 'Wheat 0659-366-GOTS', 'Material': '100% bumbac organic', 'Caracteristici': 'mânecă lungă, broderie anglaise, croială lejeră, spate mai lung', 'Cod produs': '0659-366-GOTS'})

w(10352,
  f'<p>{PRIMIGI} PTIGT 23549 sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")}, roz, din nubuc și material sintetic, cu izolație textilă și membrana GORE-TEX®, care ține apa afară. Sunt pentru joaca de iarnă, în zilele reci și ude.</p>'
  '<p>Vârful e moale și rotund, cu loc pentru degete, iar aricii permit încălțatul rapid, fără ajutor. Călcâiul ușor întărit și gulerul țin piciorul în cizmă.</p>'
  '<p>Pe zăpadă, contează talpa:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare.'), ('Shock Absorber', 'tehnologie în talpă care preia șocurile.'), ('Primigi × SIPeP', 'ține cont de anatomia piciorului.'))
  + '<p>Numerele 20-29 sunt pentru copii de aproximativ 1-5 ani.</p>',
  [('model', 'Primigi Cizme de zăpadă pentru copii roz PTIGT 23549'), ('material', 'Partea superioară din nubuc și material sintetic cu izolație textilă'),
   ('GORE-TEX', 'Membrana GORE-TEX® ajută la menținerea picioarelor uscate, blocând apa din exterior'), ('iarnă', 'jocurilor de iarnă'),
   ('vârf', 'Vârful moale, rotund favorizează libertatea de mișcare a degetelor'), ('arici', 'Sistemul de închidere cu arici permite încălțarea și descălțarea rapidă'),
   ('călcâi', 'Călcâiul ușor întărit și gulerul superior'), ('talpă', 'Talpa de cauciuc cu bandă de rulare'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă'),
   ('SIPeP', 'Colaborarea Primigi × SIPeP ține cont de anatomia piciorului copilului')],
  {'Model': 'Primigi PTIGT 23549', 'Material': 'nubuc și sintetic, izolație textilă', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber', 'Cod produs': 'PTIGT 23549'})

w(10353,
  f'<p>{PRIMIGI} PGYGT 23632 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "cizme de zăpadă pentru bebeluși")}, roz, înalte, cu fețe izolate termic din materiale sintetice și textile. Membrana GORE-TEX® apără de umezeală și vânt, pentru jocurile de iarnă și plimbările din zilele reci.</p>'
  '<p>Aricii fac încălțatul ușor, iar banda se strânge după picior. Profilul înalt și călcâiul întărit țin piciorul bine în cizmă la primii pași prin zăpadă.</p>'
  '<p>Mai sunt de știut:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare.'), ('Shock Absorber', 'limitează transferul șocurilor.'), ('Primigi × SIPeP', 'ține cont de anatomia piciorului.'))
  + '<p>Numerele 20-24 se potrivesc celor mici de în jur de 1-3 ani.</p>',
  [('model', 'Primigi Cizme de zăpadă pentru copii roz PGYGT 23632'), ('înalt', 'încălțăminte înaltă de iarnă'),
   ('izolat', 'Fețe izolate termic dintr-un amestec de materiale sintetice și textile'), ('GORE-TEX', 'Membrana GORE-TEX® ajută la protejarea împotriva umezelii și vântului'),
   ('iarnă', 'jocurile de iarnă și activitățile cotidiene în zilele reci'), ('arici', 'Închidere cu arici facilitează încălțarea și descălțarea ușoară'),
   ('profil', 'Călcâi întărit și profil înalt'), ('talpă', 'Talpă de cauciuc cu bandă de rulare'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă limitează transferul șocurilor'),
   ('SIPeP', 'Colaborarea Primigi × SIPeP ține cont de anatomia piciorului copilului')],
  {'Model': 'Primigi PGYGT 23632', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, izolate, arici, Shock Absorber', 'Cod produs': 'PGYGT 23632'})

w(10355,
  f'<p>{A("/brand/united-colors-of-benetton/", "United Colors of Benetton")} 41EXCT01C este o {A("/categorie/salopete-compleuri/", "salopetă pentru fete")}, verde, din material textil ușor, neted, cu finisaj plisat. Merge la întâlniri casual și la evenimente mai festive, inclusiv vara.</p>'
  '<p>Croiala e cambrată, cu șnur elastic în talie, care se strânge pe un copil mai slab. Mânecile sunt scurte și căzute, iar cracii sunt lungi și drepți, fără elastic.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Închidere', 'nasture.'), ('Căptușeală', 'parțială, sintetică.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 122-168 sunt pentru copii de pe la 7 până pe la 15 ani.</p>',
  [('model', 'United Colors of Benetton Salopetă copii verde 41EXCT01C'), ('ușor', 'Confecționat dintr-un material textil ușor , cu textură netedă și finisaj plisat'),
   ('ocazii', 'de la întâlniri casual la evenimente mai festive'), ('vară', 'petreceri de vară'), ('croială', 'Croială cambrată cu șnur elastic în talie'),
   ('mâneci', 'Mâneci scurte, căzute'), ('craci', 'Picior de pantalon lung, drept , fără elastic'), ('nasture', 'Sistem de închidere practic cu nasture'),
   ('căptușeală', 'Căptușeală parțială din material sintetic'), ('material', '100% Poliester')],
  {'Model': 'United Colors of Benetton 41EXCT01C', 'Material': '100% poliester', 'Caracteristici': 'plisată, talie cu șnur elastic, mâneci scurte, craci drepți', 'Cod produs': '41EXCT01C'})

w(10357,
  f'<p>Cizmele de iarnă {GEOX} HIMALAYA AB J46FTA sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")}, bordo, izolate, din material sintetic și textil, cu gambă ridicată. Tehnologia AMPHIBIOX le face impermeabile și rezistente la vânt, deci sunt pentru zăpadă și lapoviță.</p>'
  '<p>Gura cizmei se strânge cu șnur cu opritor, ca zăpada să nu intre pe sus, iar interiorul căptușit moale ține de cald.</p>'
  '<p>Sub și în față:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Talpă', 'exterioară, din cauciuc, rezistentă la uzură.'), ('Geox Respira', 'talpă în trei straturi, cu perforări.'))
  + '<p>Numerele 28-35 sunt, de obicei, pentru copii de 4-11 ani.</p>',
  [('model', 'Geox Cizme de iarnă copii HIMALAYA AB culoarea bordo, J46FTA.0FU50'), ('zăpadă', 'Cizme de zăpadă pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinația materialului sintetic cu cel textil'), ('gambă', 'Gamba ridicata'), ('AMPHIBIOX', 'Tehnologia patentata AMPHIBIOX asigura impermeabilitate'),
   ('vânt', 'rezistenta la vant'), ('șnur', 'Reglarea circumferinței superioare cu șnururi cu opritoare'), ('interior', 'Interiorul moale căptușit'),
   ('vârf', 'Cutie rotunda, intarita'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), RESPIRA],
  {'Model': 'Geox HIMALAYA AB', 'Material': 'sintetic și textil, interior căptușit', 'Caracteristici': 'AMPHIBIOX, izolate, șnur cu opritor, Geox Respira', 'Cod produs': 'J46FTA.0FU50'},
  notes=['Titlul și h1 spun bordo; atributul de culoare al magazinului spune negru.'])

w(10364,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} LVCKTJM15B este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")} (violet pe site, neagră la magazin), cu izolație termică medie, pentru zilele mai reci de tranziție. Lungimea ajunge până la genunchi, deci acoperă bine corpul.</p>'
  '<p>Croiala e regulară, iar manșetele cu nervuri strâng la încheieturi și țin frigul afară. Gluga integrată apără de vânt și de ploaie ușoară.</p>'
  '<p>Geaca mai are:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale.'), ('Căptușeală', 'completă, sintetică.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-176 sunt pentru copii de, aproximativ, 4-16 ani.</p>'.replace('de, aproximativ, 4-16 ani', 'de aproximativ 4-16 ani'),
  [('model', 'Calvin Klein Jeans Geacă petrecută pentru copii neagră LVCKTJM15B'), ('matlasat', 'Geaca matlasată neagră Calvin Klein Jeans'), ('izolație', 'Izolație termică medie'),
   ('reci', 'zilele mai reci'), ('tranziție', 'zilele de tranziție'), ('lungime', 'Lungime până la genunchi'), ('croială', 'Croială regulară'), ('manșete', 'Manșete cu nervuri'),
   ('glugă', 'Glugă integrată oferă protecție suplimentară împotriva vântului și a ploii ușoare'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'),
   ('buzunare', 'Buzunare laterale practice'), ('căptușeală', 'Căptușeală completă, sintetică'), ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans LVCKTJM15B', 'Material': '100% poliester', 'Caracteristici': 'matlasată, izolație medie, lungă până la genunchi, glugă integrată', 'Cod produs': 'LVCKTJM15B'},
  notes=['Titlul de pe site spune violet; magazinul spune neagră.'])
