import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9569,
  f'<p>{GEOX} ILLUMINUS J55HPA sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, cu profil scurt, din material sintetic și textil, cu detalii decorative și lumini încorporate care pornesc dintr-un buton. Pe drumul spre casă, seara, luminile îl fac pe copil mai ușor de observat.</p>'
  '<p>Scaiul se reglează pe picior, iar bucla de la spate ajută la tras pantoful și la scos, deci copilul se descurcă și singur. Partea de sus e rigidizată și își păstrează forma.</p>'
  '<p>În interior și în talpă, Geox a pus următoarele:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări care ventilează.'), ('Căptușeală', 'textilă.'), ('Vârf', 'cutie rotundă, ușor întărită.'), ('Talpă', 'din cauciuc.'))
  + '<p>Mărimile 28-31 se potrivesc, în general, copiilor de 4-7 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ILLUMINUS culoarea alb, J55HPA.014BU'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatia materialului sintetic cu cel textil'),
   ('decor', 'Detalii decorative'), ('lumini', 'Model cu lumini incorporate, activate de un buton'), ('scai', 'Incheiere cu scai'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior și ajută la scoaterea acestuia'), ('rigidizat', 'Partea superioară rigidizată'),
   RESPIRA, ('ventilare', 'imbunatateste ventilarea'), ('căptușeală', 'Model cu captuseala textila'), ('vârf', 'Cutie rotunda, usor intarita'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox ILLUMINUS', 'Material': 'sintetic și textil, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'lumini cu buton, scai, buclă la spate, Geox Respira', 'Cod produs': 'J55HPA.014BU'})

w(9580,
  f'<p>{A("/brand/columbia/", "Columbia")} Arctic Peak 2134921 este o {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "bluză polar cu glugă unisex")}, neagră, uni, din poliester 100%. Se închide cu fermoar, deci se îmbracă și se dă jos fără să fie trasă peste cap, cu glugă cu tot.</p>'
  '<p>Croiala e simplă, dreaptă, fără ajustări pe corp, așa că bluza cade drept și lasă loc unui tricou sau unei bluze subțiri dedesubt.</p>'
  '<p>Pentru o bluză care se poartă des, contează din ce e făcută și ce are în față:</p>'
  + L(('Material', 'polar din poliester, rezistent la îndoire.'), ('Glugă', 'da.'), ('Buzunare', 'două, în față.'))
  + '<p>Pe site sunt mărimile 104-164, adică, cu aproximație, copii de 4-14 ani.</p>',
  [('model', 'Columbia Bluză copii Arctic Peak culoarea negru, cu glugă, uni, 2134921'), ('polar', 'Material: polar'), ('poliester', '100% Poliester'),
   ('fermoar', 'Incheiere cu fermoar'), ('croială', 'Tăiere simplă, fără blocare'), ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'),
   ('glugă', 'Gluga: cu gluga'), ('buzunare', 'Două buzunare în față')],
  {'Model': 'Columbia Arctic Peak', 'Material': '100% poliester (polar)', 'Caracteristici': 'glugă, fermoar, două buzunare în față', 'Cod produs': '2134921'},
  notes=['Magazinul scrie „material de lână” în descriere, dar compoziția e 100% poliester; am folosit compoziția.',
         'Paragraful despre Omni-tech (membrană, cusături sudate) pare text generic pe o bluză polar; omis.'])

w(9581,
  f'<p>{GEOX} GISLI B461ME sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} bej, din imitație de piele și material textil, ușor de întreținut. Interiorul e din material textil și lână, iar membrana microporoasă din talpă ține apa de afară, deci doar partea de jos a pantofului e protejată la umezeală.</p>'
  '<p>Aricii îl lasă pe copil să se încalțe și să se descalțe singur, iar gulerul ușor întărit înconjoară glezna fără să fie înalt.</p>'
  '<p>Ce ține piciorul în pantof la mers:</p>'
  + L(('Călcâi', 'întărit.'), ('Geox Respira™', 'scoate umezeala spre exterior.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 20-27 sunt, de obicei, pentru copii de 1-4 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii bej B461ME.0AUAJ'), ('material', 'Partea superioară din imitație de piele și material textil'), ('întreținere', 'este ușor de întreținut'),
   ('lână', 'Material textil, Lână'), ('membrană', 'Membrana microporoasă din talpă'), ('apă', 'protejând interiorul de pătrunderea apei din exterior'),
   ('arici', 'Sistemul de închidere cu arici permite încălțarea și descălțarea rapidă și ușoară a pantofilor de către copil'), ('guler', 'Gulerul superior ușor întărit'),
   ('călcâi', 'Călcâiul întărit'), ('Respira', 'Tehnologia GEOX Respira™'), ('umezeală', 'eliminând umezeala spre exterior'), ('talpă', 'Talpa din cauciuc')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior textil și lână, talpă din cauciuc', 'Caracteristici': 'membrană în talpă, arici, Geox Respira™', 'Cod produs': 'B461ME.0AUAJ'})

w(9582,
  f'<p>Geaca {A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 323P02021001 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, bleumarin, ușor izolată cu umplutură sintetică, pentru sezonul de tranziție și zilele mai reci. Gulerul ridicat ține frigul departe de gât, iar gluga lipsește.</p>'
  '<p>Croiala e simplă, dreaptă, iar marginile mânecilor se reglează în lățime, deci se strâng pe încheietura unui copil mai slab sau se lărgesc peste o bluză groasă.</p>'
  '<p>Se îmbracă repede și are loc pentru mâini:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale, cu capse.'), ('Material', '100% poliester, căptușeală din nailon.'))
  + '<p>Mărimile 136-138 până la 163-174 merg, în jur de, la copii de 9-16 ani.</p>',
  [('model', 'Polo Ralph Lauren Geacă copii culoarea bleumarin, 323P02021001'), ('matlasat', 'material matlasat'), ('izolat', 'Model usor izolat'),
   ('izolație sintetică', 'izolație sintetică'), ('tranziție', 'Izolare: tranzitional'), ('frig', 'temperaturi mai scăzute'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('fără glugă', 'Gluga: fara gluga'), ('croială', 'Tăiere simplă, fără blocare'), ('mâneci', 'Marginile inferioare ale mânecilor sunt reglabile în lățime'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'),
   ('material', '100% Poliester'), ('căptușeală', 'Captuseala: 100% Nailon')],
  {'Model': 'Polo Ralph Lauren 323P02021001', 'Material': '100% poliester, căptușeală 100% nailon, umplutură 100% poliester', 'Caracteristici': 'matlasată, ușor izolată, guler ridicat, mâneci reglabile', 'Cod produs': '323P02021001'})

w(9586,
  f'<p>{GEOX} LESTRELLA J56NLC sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, ușori, cu profil scurt, din material sintetic și textil, pentru purtat zi de zi. Se leagă cu șiret clasic, care se strânge după forma piciorului, fie el mai îngust sau mai plin.</p>'
  '<p>Vârful e rotund și ușor rigid, iar degetele se așază liber în pantof, fără să fie strânse. Contrafortul rigid de la călcâi ține piciorul pe loc, ca să nu alunece la mers.</p>'
  '<p>Interiorul are și piele naturală, iar asta se vede în detalii:</p>'
  + L(('Branț', 'din piele, previne frecarea și mirosul neplăcut.'), ('Interior', 'sintetic, textil și piele naturală.'), ('Talpă', 'exterioară, din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 36-39 sunt pentru copii mari, cam de la 12 ani în sus.</p>',
  [('model', 'Geox Sneakers pentru copii LESTRELLA culoarea alb, J56NLC.000BC'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului sintetic cu cel textil'), ('zilnic', 'purtarea zilnică'), ('șiret', 'Șiretul clasic permite ajustarea individuală a piciorului'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('degete', 'degetele se pot aranja liber în pantof'), ('călcâi', 'Contorul de călcâi rigid'),
   ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'),
   ('miros', 'aparitia unui miros neplacut'), ('interior', 'Material sintetic, Material textil, Piele naturala'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox LESTRELLA', 'Material': 'sintetic și textil, interior cu piele naturală, talpă din cauciuc', 'Caracteristici': 'șiret clasic, branț din piele, contrafort rigid', 'Cod produs': 'J56NLC.000BC'},
  notes=['Titlul și h1 spun alb; atributul de culoare al magazinului spune bej.'])

w(9592,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 251133 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} maro, din piele naturală, căptușiți cu lână, care ține căldura pe vreme rece. Au fost dezvoltați împreună cu pediatri și ingineri de la Institutul de Biomecanică din Valencia.</p>'
  '<p>Se fixează cu curele Velcro, deci se strâng exact pe piciorul copilului, mai lat sau mai îngust, iar stabilizatorul lateral controlează mișcarea piciorului spre lateral.</p>'
  '<p>Pentru primii ani de mers, construcția e simplă:</p>'
  + L(('Călcâi', 'întărit.'), ('Talpă', 'flexibilă, din cauciuc, rezistentă la uzură.'), ('Căptușeală', 'lână.'))
  + '<p>Mărimile 21-25 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Incaltaminte din piele pentru copii culoarea maro, 251133'), ('piele', 'confecționat din piele naturală'), ('lână', 'căptușeală din lână'),
   ('căldură', 'ajută la menținerea căldurii pe vreme rece'), ('dezvoltați', 'Dezvoltați în colaborare cu pediatri și ingineri de la Institutul de Biomecanică din Valencia'),
   ('velcro', 'Curelele Velcro pentru fixare ușoară permit o potrivire personalizată'), ('stabilizator', 'stabilizator lateral pentru a controla mișcarea laterală a piciorului'),
   ('călcâi', 'Un fulger întărit pentru călcâi'), ('talpă flexibilă', 'O talpă flexibilă din cauciuc'), ('rezistentă', 'talpă din cauciuc care este durabilă și rezistentă la deteriorare')],
  {'Model': 'Biomecanics 251133', 'Material': 'piele naturală, căptușeală din lână, talpă din cauciuc', 'Caracteristici': 'curele Velcro, stabilizator lateral, călcâi întărit', 'Cod produs': '251133'},
  notes=['Titlul și h1 spun maro; atributul de culoare al magazinului spune bleumarin.'])

w(9598,
  f'<p>{GEOX} SPRINTYE B664TA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, ușori, cu partea de sus din materiale textile și sintetice. Talpa patentată Geox Respira™ are o membrană microporoasă care scoate umezeala și păstrează piciorul uscat la joacă.</p>'
  '<p>Profilul e scurt și lasă glezna liberă când copilul aleargă și sare, iar închiderea cu arici îl ajută să se încalțe fără ajutorul unui adult.</p>'
  '<p>Talpa și branțul sunt simple:</p>'
  + L(('Talpă exterioară', 'din cauciuc.'), ('Branț', 'din material textil, moale sub picior.'), ('Interior', 'textil.'))
  + '<p>Numerele 20-27 se poartă, pe la 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii SPRINTYE roz B664TA.0119J'), ('ușor', 'model ușor de încălțăminte pentru copii'), ('material', 'Partea superioară din materiale textile și sintetice'),
   ('Respira', 'Tehnologia GEOX Respira™'), ('membrană', 'talpă patentată respirabilă cu membrană microporoasă'), ('uscat', 'contribuind la menținerea picioarelor uscate'),
   ('profil', 'Profil scurt al părții superioare'), ('alergare', 'în timpul alergării și săriturilor'), ('arici', 'Sistem practic de închidere cu arici'),
   ('independent', 'facilitează încălțarea și descălțarea independentă a încălțămintei'), ('talpă', 'Talpă exterioară din cauciuc'),
   ('branț', 'Branț din material textil'), ('moale', 'asigură o așezare moale a piciorului în interiorul pantofului'), ('interior', 'Material textil')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira™, arici, profil scurt', 'Cod produs': 'B664TA.0119J'})

w(9599,
  f'<p>{GEOX} ECLYPER B655MB sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, ușori, din material textil și piele ecologică, cu profil scurt, gândiți pentru purtat zilnic. Talpa în trei straturi, cu perforări, are sistemul Geox Respira, care ventilează pantoful.</p>'
  '<p>Velcro-ul se închide repede și se reglează pe piciorul copilului, iar branțul textil se păstrează ușor curat.</p>'
  '<p>Pe scurt, din ce e făcut pantoful:</p>'
  + L(('Partea de sus', 'material sintetic și textil.'), ('Interior', 'material textil.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Mărimile 24-27 sunt pentru copii mici, undeva între 2 și 4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ECLYPER culoarea alb, B655MB.000BC'), ('material', 'combinația materialului textil cu pielea ecologică'), ('ușor', 'Model ușor'),
   ('profil', 'Înălțime: mic de statură'), ('zilnic', 'purtarea zilnică'), RESPIRA, ('ventilare', 'imbunatateste ventilarea'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'),
   ('parte de sus', 'Gamba: Material sintetic, Material textil'), ('interior', 'Interiorul: Material textil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox ECLYPER', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira', 'Cod produs': 'B655MB.000BC'})

w(9603,
  f'<p>{A("/brand/reima/", "Reima")} Telmin Kids 5400175A sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} în culoarea albastru, ușori, cu partea de sus jumătate textil, jumătate material sintetic. Sunt făcuți și cu materiale reciclate, după o formulă fără fluorocarburi.</p>'
  '<p>Croiala ajunge până la gleznă, iar șireturile elastice cu velcro se strâng după piciorul copilului și îi lasă să se încalțe repede, fără nod.</p>'
  '<p>Pentru mersul de zi cu zi, construcția e simplă:</p>'
  + L(('Contrafort', 'ușor rigidizat, la călcâi.'), ('Interior', '100% material textil.'), ('Talpă', 'plată, din cauciuc rezistent.'))
  + '<p>Numerele 22-27 corespund, de regulă, vârstei de 1-4 ani.</p>',
  [('model', 'Reima Telmin Kids sneakers copii albastru 5400175A'), ('ușor', 'contribuie la greutatea redusă a încălțămintei'), ('material', '50% Material sintetic, 50% Material textil'),
   ('reciclat', 'Utilizarea materialelor reciclate'), ('fluorocarburi', 'Formula fără fluorocarburi'), ('croială', 'Croiala până la gleznă'),
   ('închidere', 'Sistemul de închidere cu șireturi elastice și velcro facilitează încălțarea rapidă și ajustarea'), ('contrafort', 'contrafort ușor rigidizat'),
   ('interior', '100% Material textil'), ('talpă', 'Talpa plată, realizată din cauciuc rezistent')],
  {'Model': 'Reima Telmin Kids', 'Material': '50% sintetic, 50% textil, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice și velcro, fără fluorocarburi, materiale reciclate', 'Cod produs': '5400175A'})

w(9611,
  f'<p>{GEOX} PRO-RAN J65P7F sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albi, cu profil scurt, din material textil și piele ecologică, cu detalii decorative. Interiorul e textil și se păstrează ușor curat, iar talpa are sistemul Geox Respira, în trei straturi cu perforări.</p>'
  '<p>Șireturile elastice cu cârlig țin pantoful strâns fără nod, iar bucla de la spate ajută la tras pe picior, așa că un copil îl pune și îl scoate singur.</p>'
  '<p>Forma pantofului vine din câteva elemente:</p>'
  + L(('Vârf', 'rotund.'), ('Partea de sus', 'rigidizată, își ține forma.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 28-39 acoperă, în mare, copiii de la 4 ani în sus.</p>',
  [('model', 'Geox Sneakers pentru copii PRO-RAN culoarea alb, J65P7F.01454'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('decor', 'Detalii decorative'), ('interior', 'interior textil care este confortabil pentru picior și facilitează păstrarea pantofilor curați'), RESPIRA,
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior și ajută la scoaterea acestuia'), ('vârf', 'Varf rotund'),
   ('rigidizat', 'Partea superioară rigidizată'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox PRO-RAN', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, buclă la spate, Geox Respira', 'Cod produs': 'J65P7F.01454'})
