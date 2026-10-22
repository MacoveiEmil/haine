import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
PRIMIGI = A('/brand/primigi/', 'Primigi')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(10585,
  f'<p>{BIO} 221002 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} bleumarin, ușori, din piele naturală și piele întoarsă, pentru purtat zilnic. Au fost creați împreună cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia.</p>'
  '<p>Velcro-ul îi face ușor de încălțat și îi strânge bine pe picior. Vârful rotund, ușor rigid, lasă degetele să se așeze liber, iar călcâiul întărit are o umplutură moale.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'), ('Partea de sus', 'piele naturală și piele întoarsă.'))
  + '<p>Numerele 18-25 sunt pentru copii de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics bleumarin 221002'), ('material', 'combinatia pielii naturale cu pielea intoarsa'), ('ușor', 'Model ușor'), ('zilnic', 'purtarea zilnică'),
   ('Valencia', 'Acestea au fost create in cooperare cu medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'),
   ('velcro', 'Usor de imbracat si se potriveste bine datorita fixarii cu velcro'), ('vârf', 'Degetul rotund, ușor rigid'), ('degete', 'degetele se pot aranja liber în pantof'),
   ('călcâi', 'Călcâiul întărit cu umplutură moale'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Biomecanics 221002', 'Material': 'piele naturală și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, călcâi întărit', 'Cod produs': '221002'})

w(10588,
  f'<p>Pantofii {BIO} 261127 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} verzi, de tip sneakers, din piele naturală netedă, ușor de întreținut, în stil casual și streetwear. Branțul detașabil e textil și antibacterian.</p>'
  '<p>Cureaua reglabilă cu arici strânge pantoful pe picior și permite încălțatul rapid. Vârful rotund și cauciucat lasă degetele să se miște și le apără de abraziuni.</p>'
  '<p>Ce ține piciorul la mers:</p>'
  + L(('Stabilizatori', 'laterali, cu călcâi întărit.'), ('Talpă', 'din cauciuc, cu bandă de rulare.'), ('Interior', 'material textil.'))
  + '<p>Numerele 18-25 sunt, de obicei, pentru copii de 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele verde 261127'), ('sneakers', 'Pantofi pentru copii de tip sneakerși'), ('piele', 'Partea superioară din piele naturală'),
   ('neted', 'Textura netedă a materialului'), ('întreținere', 'ușor de întreținut'), ('casual', 'Stil casual și streetwear'),
   ('branț', 'Branț detașabil din material textil , respirabil și antibacterian'), ('arici', 'Sistem de închidere cu o curea reglabilă cu arici'),
   ('vârf', 'Vârf rotund, cauciucat permite mișcarea liberă a degetelor și protejează suplimentar împotriva abraziunilor'),
   ('stabilizatori', 'Stabilizatori laterali și călcâi întărit'), ('talpă', 'Talpă de cauciuc cu bandă de rulare'), ('interior', 'Interior din material textil')],
  {'Model': 'Biomecanics 261127', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'curea cu arici, branț antibacterian, vârf cauciucat', 'Cod produs': '261127'})

w(10597,
  f'<p>{BIO} 261133 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete de iarnă pentru bebeluși")}, bleumarin, înalte, din piele naturală și imitație, cu interior din lână și membrana impermeabilă BioTEX, care păstrează picioarele uscate. Sunt pentru joaca de iarnă, pe frig și umezeală.</p>'
  '<p>Aricii cu curea reglabilă se strâng după piciorul copilului și permit încălțatul ușor. Gulerul moale nu irită glezna.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Călcâi', 'întărit.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Parteneriat', 'Biomecanics Podology, proiectat cu podologi.'))
  + '<p>Numerele 18-25 se potrivesc copiilor de cam 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii bleumarin 261133'), ('înalt', 'Partea superioară înaltă din piele naturală și imitație'), ('lână', 'Lână'),
   ('BioTEX', 'Membrana impermeabilă BioTEX ajută la menținerea picioarelor uscate'), ('iarnă', 'aventurilor de iarnă'),
   ('arici', 'Sistemul de închidere cu arici și curea reglabilă'), ('guler', 'Gulerul superior moale contribuie la confortul la purtare, fără a provoca iritații'),
   ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa flexibilă din cauciuc'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261133', 'Material': 'piele naturală și imitație, interior din lână, talpă din cauciuc', 'Caracteristici': 'membrană BioTEX, arici cu curea, guler moale', 'Cod produs': '261133'})

w(10608,
  f'<p>{A("/brand/colmar/", "Colmar")} DELUXE 3452A.2YO este o {A("/categorie/geci-jachete/", "geacă de puf pentru fete")}, roz, matlasată, umplută cu puf natural de rață și pene (90/10), cu rezistență sporită la apă. E pentru frigul de iarnă.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri pe corp, deci încape un pulover gros dedesubt. Gulerul ridicat și gluga detașabilă apără gâtul și capul de frig și de vânt.</p>'
  '<p>Geaca mai are:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 154-172 sunt pentru adolescenți de aproximativ 12-15 ani.</p>',
  [('model', 'Colmar Geaca de puf pentru copii DELUXE culoarea roz, 3452A.2YO'), ('matlasat', 'Matlasat'), ('puf', '90% Puf de rata, 10% Pene de rață'),
   ('apă', 'Model cu rezistenta sporita la apa'), ('frig', 'izolare impotriva frigului'), ('croială', 'Tăiere simplă, fără blocare'),
   ('guler, glugă', 'Gulerul ridicat și gluga detașabilă oferă protecție suplimentară împotriva frigului'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('material', '100% Poliamida')],
  {'Model': 'Colmar DELUXE', 'Material': '100% poliamidă; umplutură 90% puf de rață, 10% pene', 'Caracteristici': 'puf natural, matlasată, glugă detașabilă, rezistentă la apă', 'Cod produs': '3452A.2YO'})

w(10616,
  f'<p>Pantofii {PRIMIGI} PDE 24031 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} bej, din piele nubuc netedă, cu interior și branț detașabil din piele naturală. Stilul e casual, pentru jocurile zilnice.</p>'
  '<p>Vârful lat, de tip barefoot, dă degetelor spațiu, deci pantoful merge și pe un picior mai lat. Aricii se ajustează repede, iar călcâiul moale nu irită.</p>'
  '<p>Înăuntru și dedesubt, contează:</p>'
  + L(('Talpă', 'din cauciuc, joasă, flexibilă.'), ('Interior', 'piele naturală.'), ('Branț', 'detașabil, din piele naturală.'))
  + '<p>Numerele 19-26 se potrivesc la 1-4 ani, în general.</p>',
  [('model', 'Primigi Pantofi pentru copii din nubuck bej PDE 24031'), ('nubuc', 'Partea superioară din piele nubuc'), ('neted', 'Textura netedă de nubuc'),
   ('interior', 'Interiorul din piele naturală'), ('branț', 'Branțul detașabil din piele naturală'), ('casual', 'Stilul casual'),
   ('vârf', 'Vârful lat de tip barefoot oferă spațiu degetelor'), ('arici', 'Închiderea cu arici facilitează încălțarea rapidă și ajustarea'),
   ('călcâi', 'Călcâiul moale minimizează riscul de iritații'), ('talpă', 'Talpă din cauciuc'), ('joasă', 'Talpa joasă'), ('flexibil', 'susține flexibilitatea')],
  {'Model': 'Primigi PDE 24031', 'Material': 'piele nubuc, interior din piele, talpă din cauciuc', 'Caracteristici': 'vârf lat barefoot, arici, branț detașabil', 'Cod produs': 'PDE 24031'})

w(10617,
  f'<p>{PRIMIGI} PWIGT 23791 sunt {A("/categorie/ghete-cizme/", "ghete de iarnă pentru fete")}, roz, din piele întoarsă și material textil izolat termic, cu membrana GORE-TEX®, care apără de umezeală și vânt. Sunt pentru jocurile de iarnă și zilele reci.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid și se ajustează pe picior, iar călcâiul întărit ține piciorul în gheată.</p>'
  '<p>Talpa e partea care contează pe zăpadă:</p>'
  + L(('Talpă', 'din cauciuc, cu profil plat.'), ('Shock Absorber', 'limitează transferul șocurilor.'), ('Primigi × SIPeP', 'dezvoltată cu podologii.'))
  + '<p>Numerele 31-35 sunt pentru copii de 6-11 ani, cu aproximație.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii roz PWIGT 23791'), ('material', 'Partea superioară din piele întoarsă și material textil este izolată termic'),
   ('GORE-TEX', 'Membrana GORE-TEX® asigură protecție împotriva umezelii și vântului'), ('iarnă', 'jocurilor de iarnă'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă, precum și ajustarea pe picior'), ('călcâi', 'Călcâiul întărit stabilizează piciorul'),
   ('talpă', 'Talpa din cauciuc cu profil plat'), ('Shock Absorber', 'Sistemul Shock Absorber din talpă'), ('șocuri', 'limitând transferul șocurilor'),
   ('SIPeP', 'Tehnologia Primigi × SIPeP , dezvoltată în colaborare cu podologii')],
  {'Model': 'Primigi PWIGT 23791', 'Material': 'piele întoarsă și textil izolat, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber', 'Cod produs': 'PWIGT 23791'})

w(10621,
  f'<p>{GEOX} ASSISTER J45DZC sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, cu profil scurt, din material textil și sintetic, cu lumini încorporate care se aprind dintr-un buton. Luminile îl fac pe copil mai ușor de văzut când se întunecă.</p>'
  '<p>Scaiul se închide repede și strânge pantoful după picior. Călcâiul întărit are o umplutură moale, care îl ferește de frecare.</p>'
  '<p>Materialele și talpa, pe rând:</p>'
  + L(('Talpă', 'din spumă.'), ('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Vârf', 'cutie rotundă, ușor întărită.'), ('Interior', 'textil.'))
  + '<p>Numerele 32-35 sunt pentru copii de în jur de 8-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ASSISTER culoarea verde, J45DZC.014CE'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu cel sintetic'),
   ('lumini', 'Model cu lumini incorporate, activate de un buton'), ('scai', 'Incheiere cu scai'), ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'),
   ('talpă', 'Talpa din spumă'), RESPIRA, ('vârf', 'Cutie rotunda, usor intarita'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Geox ASSISTER', 'Material': 'textil și sintetic, interior textil, talpă din spumă', 'Caracteristici': 'lumini cu buton, scai, Geox Respira', 'Cod produs': 'J45DZC.014CE'},
  notes=['Titlul și h1 spun verde; atributul de culoare al magazinului spune albastru.'])

w(10623,
  f'<p>Vesta {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KS0KS00755 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "vestă de puf pentru băieți")}, bleumarin, uni, matlasată, umplută cu puf de rață și pene, cu căptușeală completă și un logo discret. E un strat ușor pentru zilele mai reci din sezoanele de tranziție.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri. Gulerul ridicat apără gâtul, iar fără glugă și fără mâneci, vesta se poartă ușor peste un hanorac sau sub o geacă.</p>'
  '<p>Elementele practice:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, tip fentă.'), ('Material', '100% nailon; umplutură 90% puf de rață, 10% pene.'))
  + '<p>Mărimile 104-176 sunt pentru copii de 4-16 ani, aproximativ.</p>',
  [('model', 'Tommy Hilfiger Vestă de puf pentru copii bleumarin KS0KS00755'), ('uni', 'Model uni cu logo subtil al mărcii'), ('matlasat', 'Confecționată din țesătură matlasată'),
   ('puf', '90% Puf de rață, 10% Pene'), ('căptușeală', 'Are căptușeală completă'), ('tranziție', 'sezoanele de tranziție'), ('reci', 'zilele mai reci'),
   ('croială', 'Croiala regulară'), ('lungime', 'Lungime până la șolduri'), ('guler', 'Are guler ridicat'), ('fără glugă', 'Model fără glugă'),
   ('straturi', 'ușurință în asortare cu alte straturi'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'), ('buzunare', 'buzunare laterale tip fentă'), ('nailon', '100% Nailon')],
  {'Model': 'Tommy Hilfiger KS0KS00755', 'Material': '100% nailon; umplutură 90% puf de rață, 10% pene', 'Caracteristici': 'vestă de puf, matlasată, guler ridicat', 'Cod produs': 'KS0KS00755'})

w(10640,
  f'<p>{GEOX} GISLI x Superman B651NA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} bleumarin, ușori, cu profil scurt, din material sintetic și textil, cu motiv Superman, pentru purtat zilnic. Interiorul are și piele naturală.</p>'
  '<p>Branțul din piele previne frecarea, abraziunile și mirosul neplăcut, iar talpa Geox Respira, în trei straturi perforate, ventilează pantoful.</p>'
  '<p>Pe scurt, din ce e făcut:</p>'
  + L(('Partea de sus', 'material sintetic și textil.'), ('Interior', 'textil, sintetic și piele naturală.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 20-27 sunt pentru cei mici de 1-4 ani, de regulă.</p>',
  [('model', 'Geox Sneakers pentru copii GISLI x Superman culoarea bleumarin, B651NA.01054'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinatia materialului sintetic cu cel textil'), ('zilnic', 'purtarea zilnică'), ('interior', 'Material textil, Material sintetic, Piele naturala'),
   ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea, abraziunile si aparitia unui miros neplacut'), RESPIRA, ('ventilare', 'imbunatateste ventilarea'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox GISLI x Superman', 'Material': 'sintetic și textil, interior cu piele naturală, talpă din cauciuc', 'Caracteristici': 'branț din piele, Geox Respira', 'Cod produs': 'B651NA.01054'},
  notes=['Motivul Superman reiese doar din numele modelului.'])
