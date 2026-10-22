import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
GEOX = A('/brand/geox/', 'Geox')
LIEWOOD = A('/brand/liewood/', 'Liewood')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(11631,
  f'<p>{TH} KB0KB10603 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză polo pentru băieți")}, albă, din tricot moale de bumbac cu puțin elastan, cu design clasic polo, potrivit pentru zilele calde, de la ieșiri cu prietenii la mese în familie.</p>'
  '<p>Croiala e regulară și se adaptează corpului, iar materialul elastic nu încurcă la joacă. Decolteul are guler și închidere, care se poate desface când e cald.</p>'
  '<p>Pentru zi de zi, are:</p>'
  + L(('Material', '96% bumbac, 4% elastan.'), ('Decolteu', 'cu guler și închidere.'), ('Stil', 'casual, universal.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Polo pentru copii, cu bumbac alb KB0KB10603'), ('tricot', 'Tricot moale din bumbac'), ('cald', 'ideal pentru zilele calde'), ('polo', 'Design clasic polo'),
   ('ocazii', 'de la întâlniri cu prietenii la ieșiri în familie'), ('croială', 'Croială regulară'), ('elastic', 'Material elastic'),
   ('decolteu', 'Decolteu cu închidere și guler'), ('material', '96% Bumbac, 4% Elastan'), ('casual', 'Stil casual universal')],
  {'Model': 'Tommy Hilfiger KB0KB10603', 'Material': '96% bumbac, 4% elastan', 'Caracteristici': 'polo, guler cu închidere', 'Cod produs': 'KB0KB10603'})

w(11634,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} KT4366 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de blugi unisex")}, albastră, din bumbac pur, cu efect prespălat și logo discret, pentru sezonul de tranziție. Gulerul ridicat apără gâtul de vânt.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar tivul are șnur, care strânge geaca jos. Manșetele cu nervuri se potrivesc pe încheietura unui copil mic.</p>'
  '<p>Mai sunt câteva detalii:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 62-104 sunt pentru cei mici, de cam 3 luni până la 4 ani.</p>',
  [('model', 'adidas Originals Geacă de blugi pentru copii albastră KT4366'), ('bumbac', 'Realizată din bumbac pur'), ('prespălat', 'Efectul prespălat'), ('logo', 'Logo-ul subtil adidas Originals'),
   ('tranziție', 'sezonul de tranziție'), ('guler', 'Gulerul ridicat favorizează protecția suplimentară a gâtului împotriva vântului'), ('croială', 'Croiala regulară'),
   ('lungime', 'Lungimea până la șolduri'), ('tiv', 'Tivul cu șnur'), ('manșete', 'Manșetele cu nervuri'), ('fermoar', 'Închiderea cu fermoar'),
   ('buzunare', 'Buzunarele laterale tip slip-on'), ('material', '100% Bumbac')],
  {'Model': 'adidas Originals KT4366', 'Material': '100% bumbac (denim)', 'Caracteristici': 'prespălată, fermoar, tiv cu șnur', 'Cod produs': 'KT4366'})

w(11637,
  f'<p>{GEOX} FLEXYPER FAST x Superman J65N1D sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, ușori, cu profil scurt, din material sintetic și textil, cu motiv Superman, pentru purtat zilnic. Talpa are sistemul Geox Respira, perforat în trei straturi.</p>'
  '<p>Bucla de la spate ajută copilul să tragă pantoful pe picior și să-l scoată singur. Vârful e rotund, cu loc pentru degete.</p>'
  '<p>Înăuntru și dedesubt, contează:</p>'
  + L(('Talpă exterioară', 'din cauciuc, cu caneluri.'), ('Interior', 'material textil.'), ('Partea de sus', 'material sintetic și textil.'))
  + '<p>Numerele 28-35 sunt pentru copii de în jur de 4-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii FLEXYPER FAST x Superman culoarea bleumarin, J65N1D.02ABC'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului sintetic cu cel textil'), ('zilnic', 'purtarea zilnică'), RESPIRA,
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior și ajută la scoaterea acestuia'), ('vârf', 'Varf rotund'),
   ('caneluri', 'Talpa exterioară din cauciuc cu caneluri'), ('interior', 'Interiorul: Material textil')],
  {'Model': 'Geox FLEXYPER FAST x Superman', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'buclă la spate, Geox Respira', 'Cod produs': 'J65N1D.02ABC'})

w(11650,
  f'<p>Vesta {LIEWOOD} Vada Pile Vest LW14942 este o {A("/categorie/geci-jachete/", "vestă din polar pentru fete")}, roz, cu imprimeu vegetal, din polar moale, căptușită complet, pentru zilele mai reci din sezoanele de tranziție. Gulerul ridicat apără gâtul de frig și vânt.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, deci acoperă trunchiul și lasă brațele libere. Se poartă peste un tricou sau un hanorac.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, plus unul la piept, cu fermoar.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 92-128 sunt pentru copii de în jur de 2-8 ani.</p>',
  [('model', 'Liewood Vestă pentru copii din polar Vada Pile Vest roz LW14942'), ('vegetal', 'Imprimeul vegetal'), ('polar', 'Confecționat din polar moale'),
   ('căptușeală', 'Căptușeala completă'), ('reci', 'zilele mai reci'), ('tranziție', 'sezoanele de tranziție'), ('guler', 'Gulerul ridicat oferă protecție suplimentară gâtului împotriva frigului și vântului'),
   ('croială', 'Croiala regulară'), ('lungime', 'Lungimea până la șolduri'), ('fermoar', 'Închiderea cu fermoar pe toată lungimea'), ('buzunare', 'Buzunare laterale practice'),
   ('buzunar piept', 'Un buzunar la piept suplimentar, cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'Liewood Vada Pile Vest', 'Material': '100% poliester (polar)', 'Caracteristici': 'vestă polar, căptușită, guler ridicat', 'Cod produs': 'LW14942'},
  notes=['„Peste un tricou sau un hanorac” e dedus din faptul că e vestă.'])

w(11651,
  f'<p>{TH} KB0KB10634 este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac cu fermoar pentru băieți")}, roz, din polar cu uscare rapidă, care ține căldura în zilele mai reci, cu steagul Tommy Hilfiger pe spate și broderie pe piept.</p>'
  '<p>Croiala e relaxed fit, cu umerii coborâți, iar materialul elastic se adaptează la corp. Tivul și manșetele cu nervuri strâng ușor, iar gulerul înalt cu fermoar apără gâtul.</p>'
  '<p>Elementele practice:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '100% poliester (polar).'))
  + '<p>Mărimile 104-176 sunt pentru copii de 4-16 ani, de regulă.</p>',
  [('model', 'Tommy Hilfiger Hanorac cu fermoar pentru copii din polar roz KB0KB10634'), ('uscare', 'Țesătură cu uscare rapidă'), ('polar', 'Confecția din polar asigură menținerea căldurii, fiind potrivită pentru zilele mai reci'),
   ('steag', 'Steagul Tommy Hilfiger pe spate și broderia pe piept'), ('croială', 'Croiala relaxed fit'), ('umeri', 'Linia umerilor coborâtă'), ('elastic', 'Material elastic'),
   ('nervuri', 'Tivul și manșetele cu nervuri'), ('guler', 'Gulerul înalt cu fermoar protejează gâtul de frig'), ('fermoar', 'Sistemul de închidere cu fermoar pe toată lungimea'),
   ('buzunare', 'Buzunarele laterale, tip slip-on'), ('material', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KB0KB10634', 'Material': '100% poliester (polar)', 'Caracteristici': 'polar, fermoar, guler înalt, relaxed fit', 'Cod produs': 'KB0KB10634'})

w(11661,
  f'<p>{A("/brand/konges-slojd/", "Konges Sløjd")} FRANKIE OVERALL KS105393 este o {A("/categorie/bebe-imbracaminte-salopete-compleuri/", "salopetă cu bretele pentru bebeluși")}, multicoloră, cu dungi, din bumbac 100% certificat GOTS, cu broderie decorativă pe piept. Se poartă peste un body sau un tricou.</p>'
  '<p>Bretelele nu se scot, dar se reglează după înălțimea copilului, deci salopeta crește puțin cu el. Materialul neelastic își păstrează forma și după multe spălări și zile de joacă.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Închidere', 'nasturi.'), ('Material', '100% bumbac.'), ('Detalii', 'broderie pe piept.'))
  + '<p>Mărimile 80-116 sunt pentru copii de aproximativ 1-6 ani.</p>',
  [('model', 'Konges Sløjd Salopetă pentru copii FRANKIE OVERALL GOTS multicolor KS105393'), ('dungi', 'Acest model cu dungi'), ('bumbac', 'Confecționată din bumbac 100%'),
   ('broderie', 'Broderie decorativă – pe piept'), ('bretele', 'Bretele reglabile – neamovibile, permit ajustarea la înălțimea copilului'),
   ('neelastic', 'Material neelastic – își menține forma'), ('nasturi', 'Închidere cu nasturi')],
  {'Model': 'Konges Sløjd FRANKIE OVERALL', 'Material': '100% bumbac (GOTS)', 'Caracteristici': 'bretele reglabile, nasturi, broderie', 'Cod produs': 'KS105393'},
  notes=['„Peste un body sau un tricou” e dedus din faptul că e salopetă cu bretele.'])

w(11663,
  f'<p>{GEOX} WASHIBA x Disney Princess J65HXC sunt {A("/categorie/adidasi/", "adidași pentru fete")} turcoaz, cu profil scurt, din material textil și piele ecologică, cu prințese Disney. Talpa are sistemul Geox Respira, în trei straturi perforate.</p>'
  '<p>Șireturile elastice cu cârlig permit încălțatul fără nod, iar contrafortul rigidizat ține călcâiul în pantof. Vârful e rotund.</p>'
  '<p>Materialele și talpa, pe rând:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'din cauciuc, rezistentă la uzură.'), ('Partea de sus', 'material textil și piele ecologică.'))
  + '<p>Numerele 28-35 sunt pentru copii de 4-11 ani, în general.</p>',
  [('model', 'Geox Sneakers pentru copii WASHIBA x Disney Princess culoarea turcoaz, J65HXC.054AJ'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea ecologică'), RESPIRA, ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('călcâi', 'Contorul de călcâi rigidizat'), ('vârf', 'Varf rotund'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'talpă din cauciuc care este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox WASHIBA x Disney Princess', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J65HXC.054AJ'})

w(11672,
  f'<p>Geaca de blugi {TH} KB0KB10397 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de blugi pentru băieți")}, albastră, cu croială trucker, din denim rezistent de bumbac și lyocell, cu broderia wavy flag pe toată suprafața. Fără căptușeală, e pentru sezonul de tranziție.</p>'
  '<p>Croiala e regulară, iar lungimea e scurtă. Manșetele se închid cu un nasture și se strâng pe încheietură.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Închidere', 'nasturi pe toată lungimea.'), ('Buzunare', 'două aplicate la piept, două laterale.'), ('Material', '61% bumbac, 39% lyocell.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă de blugi pentru copii, din bumbac albastră KB0KB10397'), ('trucker', 'Croiala de tip trucker'), ('denim', 'Confecționată din denim rezistent din bumbac'),
   ('broderie', 'Broderia wavy flag Tommy Hilfiger pe toată suprafața'), ('necăptușit', 'Lipsa căptușelii'), ('tranziție', 'sezonul de tranziție'), ('croială', 'Croiala regulară'),
   ('scurt', 'Lungimea scurtă a modelului'), ('manșete', 'Manșetele cu închidere cu un singur nasture'), ('nasturi', 'Închiderea cu nasturi pe toată lungimea'),
   ('buzunare piept', 'Două buzunare aplicate la piept'), ('buzunare laterale', 'Două buzunare laterale tip slip-on'), ('material', '61% Bumbac, 39% Lyocell')],
  {'Model': 'Tommy Hilfiger KB0KB10397', 'Material': '61% bumbac, 39% lyocell (denim)', 'Caracteristici': 'trucker, broderie wavy flag, necăptușită', 'Cod produs': 'KB0KB10397'})

w(11673,
  f'<p>Paltonul {A("/brand/maxco/", "Max&amp;Co.")} MAXJ35F JACKET MX0229 este un {A("/categorie/geci-jachete/", "palton de lână pentru fete")}, negru, din lână 100%, moale, neizolat, pentru sezonul de tranziție. Are revere clasice și se închide cu nasturi pe două rânduri.</p>'
  '<p>Croiala e lejeră, deci paltonul stă larg și se poartă comod peste un pulover. Nu are glugă.</p>'
  '<p>Câteva detalii practice:</p>'
  + L(('Închidere', 'nasturi pe două rânduri.'), ('Buzunare', 'două, în față.'), ('Material', '100% lână.'))
  + '<p>Mărimile 156-175 sunt pentru adolescente de 13-16 ani, aproximativ. Mărimile sunt italiene, deci ajută tabelul producătorului.</p>',
  [('model', 'Max&Co. Palton de lână pentru copii MAXJ35F JACKET culoare neagră MX0229'), ('lână', '100% Lână'), ('moale', 'confecționată dintr-un material moale'),
   ('neizolat', 'Izolare: neizolat'), ('tranziție', 'Izolare: tranzitional'), ('revere', 'Revere clasice'), ('nasturi', 'Închidere cu nasturi la două rânduri'),
   ('croială', 'Croială lejeră pentru libertate completă de mișcare'), ('fără glugă', 'Gluga: fara gluga'), ('buzunare', 'Două buzunare frontale'),
   ('mărimi', 'Mărimile disponibile sunt convertite din sistemul italian')],
  {'Model': 'Max&Co. MAXJ35F', 'Material': '100% lână', 'Caracteristici': 'palton, revere, nasturi pe două rânduri, croială lejeră', 'Cod produs': 'MX0229'},
  notes=['Magazinul se contrazice despre căptușeală („fără căptușeală” în text, „cu captuseala” la atribute); nu am pomenit-o.'])

w(11714,
  f'<p>{LIEWOOD} Orson Sweatshirt LW20900 este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} verde, clasic, fără fermoar și fără glugă, din bumbac 100% ușor elastic, cu imprimeu jucăuș și broderii. Stilul e casual, fără buzunare.</p>'
  '<p>Croiala e lejeră, cu mâneci raglan, deci brațele se mișcă liber la joacă. Decolteul rotund nu strânge la gât, iar hanoracul se trage repede peste cap.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Mâneci', 'raglan.'), ('Detalii', 'imprimeu și broderii.'))
  + '<p>Mărimile 86-92 până la 134-140 sunt pentru copii de aproximativ 1-10 ani.</p>',
  [('model', 'Liewood Hanorac pentru copii din bumbac Orson Sweatshirt verde LW20900'), ('clasic', 'Un hanorac clasic fără fermoar și fără glugă'),
   ('elastic', 'Materialul tricotat din bumbac este ușor elastic'), ('bumbac', 'Confecționat 100% din bumbac'), ('imprimeu', 'Broderiile și imprimeul'),
   ('casual', 'stilul casual'), ('fără buzunare', 'Absența buzunarelor'), ('croială', 'Croiala lejeră'), ('raglan', 'Mânecile raglan'), ('decolteu', 'Decolteul rotund'),
   ('fără închidere', 'Construcția fără închidere facilitează îmbrăcarea și dezbrăcarea rapidă')],
  {'Model': 'Liewood Orson Sweatshirt', 'Material': '100% bumbac', 'Caracteristici': 'fără fermoar și glugă, mâneci raglan, imprimeu', 'Cod produs': 'LW20900'})
