import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
GUESS = A('/brand/guess/', 'Guess')
REIMA = A('/brand/reima/', 'Reima')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(10158,
  f'<p>Geaca {GUESS} J6YL10 W2622 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, neagră, cu model cu monogramă Guess și izolație sintetică ușoară, pentru zilele mai reci de tranziție. Țesătura e rezistentă și se întreține ușor.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, deci acoperă trunchiul fără să încurce. Gulerul ridicat apără gâtul de frig, iar căptușeala completă nu irită.</p>'
  '<p>Geaca se închide și se poartă simplu:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, cu fermoar.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 122-125 până la 167 sunt pentru copii de în jur de 7-14 ani.</p>',
  [('model', 'Guess Geacă petrecută pentru copii neagră J6YL10 W2622'), ('matlasat', 'Structura matlasată'), ('monogramă', 'Modelul caracteristic cu monogramă'),
   ('izolație', 'Izolație sintetică ușoară'), ('tranziție', 'zilele mai reci de tranziție'), ('țesătură', 'Fabricată din țesătură rezistentă'), ('întreținere', 'ușurință în întreținere'),
   ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'), ('guler', 'Guler ridicat asigură protecție suplimentară gâtului împotriva frigului'),
   ('căptușeală', 'Căptușeală completă în interiorul gecii asigură confort, fără a provoca iritații'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'),
   ('buzunare', 'Buzunare laterale cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'Guess J6YL10 W2622', 'Material': '100% poliester', 'Caracteristici': 'matlasată, izolație ușoară, monogramă, guler ridicat', 'Cod produs': 'J6YL10 W2622'})

w(10161,
  f'<p>{GEOX} BISLI B461MA sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, neizolați, din piele ecologică și material textil, cu talpa Geox Respira, în trei straturi cu perforații. Sunt pentru zilele în care nu e nevoie de încălțăminte de iarnă.</p>'
  '<p>Șireturile elastice și velcro-ul îi lasă pe cei mici să se încalțe și să se descalțe repede, iar vârful e rotund și întărit.</p>'
  '<p>Pe scurt:</p>'
  + L(('Interior', 'textil, ușor de întreținut.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'), ('Partea de sus', 'material textil și piele artificială.'))
  + '<p>Numerele 24-27 sunt pentru copii de, aproximativ, 2-4 ani.</p>'.replace('de, aproximativ, 2-4 ani', 'de aproximativ 2-4 ani'),
  [('model', 'Geox Sneakers pentru copii BISLI culoarea roz, B461MA.5402'), ('neizolat', 'Model neizolat'), ('material', 'combinație de piele ecologică și material textil'),
   ('Respira', 'tălpii cu structură în trei straturi și perforațiilor'), ('închidere', 'Șireturile elastice și închiderea cu velcro facilitează încălțarea și descălțarea'),
   ('vârf', 'Vârf rotund și întărit'), ('interior', 'Interiorul textil este confortabil pentru picior și ușor de întreținut'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('parte de sus', 'Material textil, Piele artificiala')],
  {'Model': 'Geox BISLI', 'Material': 'piele ecologică și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'neizolați, șireturi elastice cu velcro, Geox Respira', 'Cod produs': 'B461MA.5402'})

w(10162,
  f'<p>Geaca bomber {GUESS} L5YL06 WHE70 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă bomber pentru băieți")}, bleumarin, subțire, din amestec de poliester și lână, cu izolație ușoară pe căptușeală. E pentru sezonul de tranziție, iar poliesterul o ferește de șifonare.</p>'
  '<p>Croiala e simplă, iar mânecile și tivul se termină cu bandă elastică, care strânge bomberul la încheieturi și pe șolduri, ca la orice geacă bomber.</p>'
  '<p>Detaliile sunt puține:</p>'
  + L(('Închidere', 'cu capse.'), ('Buzunare', 'două, laterale.'), ('Glugă', 'nu are.'), ('Material', '84% poliester, 16% lână.'))
  + '<p>Mărimile 122-125 până la 175 se potrivesc copiilor de pe la 7 până pe la 16 ani.</p>',
  [('model', 'Guess Geacă bomber pentru copii culoarea albastru marin, L5YL06 WHE70'), ('subțire', 'Model subtire confectionat din amestec de lână'),
   ('izolat', 'Model usor izolat pe captuseala'), ('tranziție', 'Izolare: tranzitional'), ('șifonare', 'Poliesterul garantează o rezistență ridicată la șifonare'),
   ('croială', 'Tăiere simplă, fără blocare'), ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('capse', 'Incheiere cu cleme'),
   ('buzunare', 'Două buzunare laterale'), ('fără glugă', 'Gluga: fara gluga'), ('material', '84% Poliester , 16% Lana'), ('bomber', 'Fit: bomber')],
  {'Model': 'Guess L5YL06 WHE70', 'Material': '84% poliester, 16% lână; căptușeală 100% poliester', 'Caracteristici': 'bomber, ușor izolat, mâneci și tiv elastice', 'Cod produs': 'L5YL06 WHE70'})

w(10167,
  f'<p>Geaca {A("/brand/patrizia-pepe/", "Patrizia Pepe")} K103 7O0037 este o {A("/categorie/geci-jachete/", "geacă subțire pentru fete")}, neagră, neizolată și necăptușită, din material cu inserții și finisaje decorative. E pentru zilele blânde, când nu e nevoie de o haină groasă.</p>'
  '<p>Croiala e simplă, dreaptă, iar geaca se închide cu nasturi, ca o jachetă de oraș. Nu are glugă.</p>'
  '<p>Pe scurt, despre geacă:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunar', 'pe piept.'), ('Finisaje', 'decorative.'))
  + '<p>Mărimile 140-168 sunt pentru copii de cam 10-15 ani. Mărimile sunt italiene, deci tabelul producătorului ajută la alegere.</p>',
  [('model', 'Patrizia Pepe Geaca copii K103 culoarea negru, 7O0037'), ('neizolat', 'Model neizolat confectionat din material cu insertii decorative'),
   ('necăptușit', 'Captuseala: necaptusit'), ('finisaje', 'Finisaje decorative'), ('croială', 'Tăiere simplă, fără blocare'), ('nasturi', 'Incheiere cu nasturi'),
   ('fără glugă', 'Gluga: fara gluga'), ('buzunar', 'Buzunar pe piept'), ('mărimi italiene', 'Dimensiunile disponibile sunt cele ale producatorul italian')],
  {'Model': 'Patrizia Pepe K103', 'Material': 'material cu inserții decorative', 'Caracteristici': 'neizolată, necăptușită, nasturi, buzunar pe piept', 'Cod produs': '7O0037'})

w(10174,
  f'<p>{A("/brand/mini-rodini/", "Mini Rodini")} Mammoths 25710114 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă matlasată unisex")}, bej, cu model, izolată cu umplutură sintetică, din poliester reciclat. Impregnarea DWR fără PFC, cu Bionic-Finish® Eco, și impermeabilitatea de 3000 mm o apără de ploaie ușoară.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile lungi au manșete elastice, care strâng la încheieturi. Gluga se detașează când nu e nevoie de ea.</p>'
  '<p>Pentru vânt și ploaie, geaca are:</p>'
  + L(('Fermoar', 'pe toată lungimea, cu clapă de furtună prinsă cu capse.'), ('Buzunare', 'două, laterale, cu capse.'), ('Respirabilitate', '3000 g/m2/24 h.'))
  + '<p>Mărimile 80-86 până la 140-146 sunt pentru copii de, de regulă, 1-11 ani.</p>'.replace('de, de regulă, 1-11 ani', 'de 1-11 ani, de regulă'),
  [('model', 'Mini Rodini Geacă copii Mammoths culoarea bej, 25710114'), ('modelat', 'material modelat'), ('matlasat', 'Model matlasat cu izolație sintetica'),
   ('reciclat', '100% Poliester reciclat'), ('DWR', 'Impregnarea durabilă a materialului DWR fără PFC'), ('Bionic', 'Bionic-Finish® Eco'),
   ('impermeabil', 'Impermeabilitate: 3000 mm'), ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Mâneci lungi finisate cu o manșetă confortabilă, elastică'),
   ('glugă', 'Gluga detasabila'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă de furtună prinsă cu capse'),
   ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'), ('respirabilitate', 'Respirabilitate: 3000 g/m2/24 h')],
  {'Model': 'Mini Rodini Mammoths', 'Material': '100% poliester reciclat', 'Caracteristici': 'matlasată, izolată, DWR fără PFC, 3000 mm, glugă detașabilă', 'Cod produs': '25710114'})

w(10183,
  f'<p>{REIMA} Enkkari 5400152C sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albaștri, ușori, din material textil și piele ecologică, cu tehnologia ReimaTec, care apără de ploaie și vânt. Sunt pentru purtat zilnic, inclusiv pe vreme umedă.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, iar inserțiile detașabile Happy Fit ajută la alegerea mărimii potrivite. Șireturile elastice cu cârlig și bucla permit încălțatul fără legat.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'), ('Interior', 'material sintetic și textil.'), ('Rezistență la apă', 'sporită, nu impermeabilitate completă.'))
  + '<p>Numerele 28-38 sunt pentru copii de la, în general, 4 ani în sus.</p>',
  [('model', 'Reima Sneakers pentru copii Enkkari 5400152C'), ('culoare', 'albastru'), ('ușor', 'Model ușor'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'), ('zilnic', 'purtarea zilnică'), ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('Happy Fit', 'Inserțiile detașabile Happy Fit vă permit să alegeți dimensiunea potrivită'),
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('buclă', 'Bucla ușurează să pui pantoful în picior'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('interior', 'Material sintetic, Material textil'),
   ('apă', 'nu garantează impermeabilitatea completă')],
  {'Model': 'Reima Enkkari', 'Material': 'textil și piele ecologică, talpă din cauciuc', 'Caracteristici': 'ReimaTec, Happy Fit, șireturi elastice cu cârlig, cutie lată', 'Cod produs': '5400152C'})

w(10186,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} T1XH-34335 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} albi, netezi, cu construcție barefoot, care lasă piciorul să simtă solul. Se poartă primăvara, vara și toamna, la ținute casual și minimaliste.</p>'
  '<p>Velcro-ul se închide repede și îl lasă pe copil să se încalțe singur, iar gulerul moale nu irită glezna. Talpa flexibilă, cu profil redus, se îndoaie odată cu piciorul.</p>'
  '<p>Pantoful mai are:</p>'
  + L(('Contrafort', 'rigidizat.'), ('Branț', 'din piele naturală.'), ('Interior', 'material textil.'))
  + '<p>Mărimile 20-26 sunt pentru copii de în jur de 1-4 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii albi T1XH-34335'), ('barefoot', 'Construcție barefoot'), ('sol', 'permițând o mai bună simțire a solului'),
   ('sezon', 'primăverii, verii și toamnei'), ('casual', 'stilizări casual, minimaliste și urbane'), ('neted', 'Modelul neted, de culoare albă'),
   ('velcro', 'Închidere practică cu velcro'), ('autonomie', 'încurajând autonomia copilului'), ('guler', 'Guler moale'), ('iritații', 'minimizând riscul de iritații'),
   ('talpă', 'Realizată din cauciuc cu profil redus'), ('contrafort', 'Contrefort rigidizat'), ('branț', 'Branț din piele naturală'), ('interior', 'Interior din material textil')],
  {'Model': 'Tommy Hilfiger T1XH-34335', 'Material': 'sintetic, interior textil, branț din piele naturală, talpă din cauciuc', 'Caracteristici': 'barefoot, velcro, guler moale', 'Cod produs': 'T1XH-34335'})

w(10196,
  f'<p>{GEOX} ECLYPER B555MA sunt {A("/categorie/adidasi/", "adidași pentru fete")} galbeni, cu profil scurt, din material textil și piele ecologică, cu detalii decorative. Talpa are sistemul Geox Respira, în trei straturi perforate, iar căptușeala e textilă.</p>'
  '<p>Scaiul se închide repede și se strânge după picior. Călcâiul întărit are o umplutură moale, care îl ferește de frecare, iar partea de sus rigidizată ține forma.</p>'
  '<p>Pe scurt:</p>'
  + L(('Branț', 'textil, detașabil.'), ('Vârf', 'cutie rotundă, ușor întărită.'), ('Talpă', 'din cauciuc.'))
  + '<p>Mărimile 20-27 sunt pentru cei mici de aproximativ 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ECLYPER culoarea galben, B555MA.000BC'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatia materialului textil cu pielea ecologica'),
   ('decor', 'Detalii decorative'), RESPIRA, ('căptușeală', 'Model cu captuseala textila'), ('scai', 'Incheiere cu scai'),
   ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'), ('rigidizat', 'Partea superioară rigidizată'),
   ('branț', 'Brant textil, detasabil'), ('vârf', 'Cutie rotunda, usor intarita'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox ECLYPER', 'Material': 'textil și piele ecologică, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'scai, branț detașabil, Geox Respira', 'Cod produs': 'B555MA.000BC'})

w(10197,
  f'<p>{REIMA} 5400025A sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de zăpadă unisex")}, negre, izolate, din material textil, piele ecologică și piele întoarsă. Sunt pentru iarnă și joaca prin zăpadă, cu interior textil.</p>'
  '<p>Scaiul le face ușor de încălțat, iar banda se strânge după cât de plin e piciorul. Vârful e rotund, cu loc pentru degete.</p>'
  '<p>Cizma e construită simplu:</p>'
  + L(('Partea de sus', 'material sintetic, textil și piele întoarsă.'), ('Interior', 'textil.'), ('Talpă', 'din gumă.'))
  + '<p>Numerele 28-38 sunt pentru copii de pe la 4 ani în sus. Pe pagina magazinului nu apare un nume de model, doar codul.</p>'.replace(' Pe pagina magazinului nu apare un nume de model, doar codul.', ''),
  [('model', 'Reima negru 5400025A'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Model izolat'), ('material', 'combinatie de material textil, piele ecologica si piele intoarsa'),
   ('scai', 'Incheiere cu scai'), ('vârf', 'Varf rotund'), ('parte de sus', 'Material sintetic, Material textil, Piele intoarsa'), ('interior', 'Interior textil'), ('talpă', 'Talpa din guma')],
  {'Model': 'Reima 5400025A', 'Material': 'textil, piele ecologică și piele întoarsă, interior textil, talpă din gumă', 'Caracteristici': 'izolate, scai', 'Cod produs': '5400025A'})

w(10210,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261015 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, din piele naturală, proiectați în colaborare cu podologi, pentru activitățile zilnice ale celor mici. Interiorul e din material textil.</p>'
  '<p>Spațiul crescut la degete le lasă să se miște liber, deci pantoful vine bine și pe un picior mai plin. Aricii se închid repede, iar branțurile se scot ca să fie curățate.</p>'
  '<p>Pentru mersul de zi cu zi:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Partea de sus', 'piele naturală.'))
  + '<p>Numerele 19-26 sunt pentru copii de, cam, 1-4 ani.</p>'.replace('de, cam, 1-4 ani', 'de cam 1-4 ani'),
  [('model', 'Biomecanics Sneakers pentru copii din piele roz 261015'), ('piele', 'Partea superioară din piele naturală'), ('podologi', 'Proiectați în colaborare cu podologi'),
   ('zilnic', 'activităților zilnice'), ('interior', 'Interiorul din material textil'), ('degete', 'Spațiul crescut la nivelul degetelor permite mișcarea liberă'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă'), ('branțuri', 'Branțurile detașabile'), ('călcâi', 'Călcâiul ușor întărit'),
   ('talpă', 'Talpa flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261015', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, spațiu crescut la degete, branțuri detașabile', 'Cod produs': '261015'})
