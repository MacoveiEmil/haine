import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(10961,
  f'<p>{GEOX} ASSISTER x Superman J65DZA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} în culoarea albastru, cu motiv Superman și lumini LED cu buton de pornire și oprire. Partea de sus e din material textil și sintetic, ușoară, iar tehnologia Geox Respira™ ajută la termoreglarea piciorului.</p>'
  '<p>Croiala ajunge până la gleznă, iar șireturile elastice cu scai se strâng repede, deci copilul se încalță singur, fără nod.</p>'
  '<p>Pe scurt:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Căptușeală', 'textilă, moale.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-31 sunt pentru copii de 2-7 ani, de regulă.</p>',
  [('model', 'Geox ASSISTER x Superman sneakers pentru copii albastru J65DZA.02ABC'), ('LED', 'Luminile LED integrate, cu buton de pornire/oprire'),
   ('material', 'Partea superioară din material textil și sintetic favorizează lejeritatea'), ('Respira', 'Tehnologia Geox Respira™ susține termoreglarea naturală a piciorului'),
   ('gleznă', 'Croiala până la gleznă'), ('închidere', 'Șireturile elastice și închiderea cu scai facilitează încălțarea rapidă'), ('călcâi', 'Zona călcâiului, ușor întărită'),
   ('căptușeală', 'Căptușeala textilă moale'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox ASSISTER x Superman', 'Material': 'textil și sintetic, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'lumini LED cu buton, șireturi elastice cu scai, Geox Respira™', 'Cod produs': 'J65DZA.02ABC'})

w(10965,
  f'<p>{A("/brand/colmar/", "Colmar")} WEIGHTLESS 3462.6ZN este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de puf pentru băieți")}, bleumarin, izolată cu puf de rață și pene (90/10), cu rezistență sporită la apă. E pentru frigul de iarnă, iar gulerul ridicat și gluga fixă apără gâtul și capul.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri pe corp, deci încape un pulover gros dedesubt.</p>'
  '<p>Pe scurt, despre geacă:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere.'), ('Căptușeală', '100% poliamidă.'))
  + '<p>Mărimile 130-172 sunt pentru copii de 8-15 ani, în mare.</p>',
  [('model', 'Colmar Geaca de puf pentru copii WEIGHTLESS culoarea albastru marin, 3462.6ZN'), ('puf', '90% Puf de rata, 10% Pene de rață'), ('apă', 'Model cu rezistenta sporita la apa'),
   ('frig', 'izolare impotriva frigului'), ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('croială', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('căptușeală', 'Captuseala: 100% Poliamida')],
  {'Model': 'Colmar WEIGHTLESS', 'Material': 'poliamidă și poliester; umplutură 90% puf, 10% pene', 'Caracteristici': 'puf, glugă fixă, rezistentă la apă', 'Cod produs': '3462.6ZN'})

w(10973,
  f'<p>Geaca {TH} KB0KB09815 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de puf pentru băieți")}, bej, matlasată, izolată cu puf de rață și pene (70/30), din material neted, cu sigla brandului. E pentru zilele reci de iarnă, iar gluga apără capul.</p>'
  '<p>Croiala e lejeră, deci încape un pulover gros dedesubt, iar mânecile se termină cu bandă elastică, care strânge la încheieturi.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'oblice.'), ('Material', '100% poliester; umplutură 70% puf, 30% pene.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, cu aproximație.</p>',
  [('model', 'Tommy Hilfiger Geacă de puf pentru copii culoarea bej, KB0KB09815'), ('matlasat', 'Matlasat'), ('puf', '70% Duck Down, 30% Pene'), ('neted', 'Material neted'),
   ('siglă', 'Model cu sigla brandului'), ('izolat', 'Model izolat cu captuseala'), ('glugă', 'Model cu gluga'), ('croială', 'Tăiere lejeră, fără blocare'),
   ('elastic', 'Mâneci finisate cu o coadă elastică'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare oblice'), ('material', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KB0KB09815', 'Material': '100% poliester; umplutură 70% puf de rață, 30% pene', 'Caracteristici': 'puf, matlasată, glugă, croială lejeră', 'Cod produs': 'KB0KB09815'},
  notes=['Titlul și h1 spun bej; atributul de culoare al magazinului spune verde.'])

w(10977,
  f'<p>{GEOX} NASHIK B465NC sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} bej, din piele naturală, piele întoarsă și material textil, în stil casual. Membrana Geox Respira™ din talpă scoate umezeala și protejează în același timp împotriva apei.</p>'
  '<p>Aricii permit încălțatul rapid și o ajustare ușoară. Branțul detașabil din piele are imprimeu pentru verificarea mărimii, deci se vede când piciorul a crescut.</p>'
  '<p>Pe scurt:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'piele naturală și material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-23 sunt pentru cei mici de în jur de 1-3 ani.</p>',
  [('model', 'Geox NASHIK sneakers pentru copii din piele bej B465NC.0CL22'), ('material', 'Partea superioară din combinație de piele naturală, piele întoarsă și material textil'),
   ('casual', 'stilul casual'), ('Respira', 'o membrane speciale în talpă, care elimină umezeala, protejând în același timp împotriva apei'.replace('o membrane', 'unei membrane')),
   ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă'), ('branț', 'Branț detașabil din piele naturală cu imprimeu pentru verificarea mărimii'),
   ('călcâi', 'Călcâi întărit'), ('interior', 'Interior căptușit cu piele naturală și material textil'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox NASHIK', 'Material': 'piele naturală, piele întoarsă și textil, talpă din cauciuc', 'Caracteristici': 'arici, branț cu imprimeu de mărime, Geox Respira™', 'Cod produs': 'B465NC.0CL22'})

w(10994,
  f'<p>{GEOX} LIGHTYLOO x Looney Tunes B655ZB sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} bleumarin, ușori, cu profil scurt, din material textil și sintetic, pentru purtat zilnic. Talpa are sistemul Geox Respira, în trei straturi cu perforări.</p>'
  '<p>Velcro-ul se închide repede și strânge pantoful pe picior, deci încălțatul durează puțin. Branțul textil se ține ușor curat.</p>'
  '<p>Pe scurt:</p>'
  + L(('Partea de sus', 'material textil și sintetic.'), ('Interior', 'material sintetic și textil.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 18-27 se potrivesc celor mici de 1-4 ani, în general.</p>',
  [('model', 'Geox Sneakers pentru copii LIGHTYLOO x Looney Tunes B655ZB.05411'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinatia materialului textil cu cel sintetic'), ('zilnic', 'purtarea zilnică'), RESPIRA,
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'),
   ('interior', 'Interiorul: Material sintetic, Material textil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox LIGHTYLOO x Looney Tunes', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'velcro, Geox Respira', 'Cod produs': 'B655ZB.05411'},
  notes=['Titlul spune bleumarin; magazinul dă culoarea albastru.'])

w(10998,
  f'<p>Cizmele cowboy {TH} T3A6-35193 sunt {A("/categorie/ghete-cizme/", "cizme cowboy pentru fete")}, negre, din piele naturală netedă, cu vârf ascuțit, rigidizat, pentru sezonul de tranziție. Designul trece de gleznă, iar gulerul e ușor întărit.</p>'
  '<p>Fermoarul și velcro-ul se combină: cizma se deschide larg la încălțat și se ajustează apoi pe picior. Călcâiul întărit ține piciorul în cizmă.</p>'
  '<p>Înăuntru și dedesubt:</p>'
  + L(('Branț', 'din piele naturală.'), ('Căptușeală', 'textilă.'), ('Talpă', 'din cauciuc, groasă.'))
  + '<p>Numerele 30-40 sunt pentru copii de la 6 ani în sus, de regulă.</p>',
  [('model', 'Tommy Hilfiger Cizme cowboy pentru copii din piele negre T3A6-35193'), ('piele', 'Partea superioară din piele naturală'), ('cowboy', 'Modelul de cizme cowboy'),
   ('tranziție', 'sezonul de tranziție'), ('vârf', 'Vârful ascuțit, rigidizat'), ('gleznă', 'Designul deasupra gleznei , cu gulerul ușor întărit'),
   ('închidere', 'Combinația de închidere cu fermoar și velcro'), ('călcâi', 'Călcâiul întărit'), ('branț', 'Branțul din piele naturală'), ('căptușeală', 'Căptușeala textilă'),
   ('talpă', 'Talpa din cauciuc cu grosimea de 3,5 cm')],
  {'Model': 'Tommy Hilfiger T3A6-35193', 'Material': 'piele naturală, căptușeală textilă, branț din piele, talpă din cauciuc', 'Caracteristici': 'cizme cowboy, fermoar și velcro, vârf ascuțit', 'Cod produs': 'T3A6-35193'})

w(11009,
  f'<p>Pantofii {A("/brand/wheat/", "Wheat")} WF622-02 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} portocalii, din piele întoarsă cu imprimeu floral, pentru ținutele lejere de vară. Interiorul și branțul sunt din piele tăbăcită fără crom și metale.</p>'
  '<p>Scaiul permite încălțatul și descălțatul rapid, iar contrafortul ușor rigidizat ține piciorul în pantof. Vârful e ranforsat și își păstrează forma.</p>'
  '<p>Pe scurt:</p>'
  + L(('Partea de sus', 'piele întoarsă.'), ('Interior și branț', 'piele naturală fără crom.'), ('Talpă', 'din cauciuc rezistent.'))
  + '<p>Numerele 21-26 sunt pentru copii de 1-4 ani, aproximativ.</p>',
  [('model', 'Wheat Pantofi pentru copii din piele întoarsă portocalii WF622-02'), ('piele întoarsă', 'Partea superioară din piele întoarsă'), ('floral', 'Imprimeu floral fermecător'),
   ('vară', 'creat pentru ținutele lejere de vară'), ('interior', 'Interior finisat cu piele tăbăcită fără crom și metale'),
   ('branț', 'Branț din piele naturală tăbăcită fără crom și metale'), ('scai', 'Închidere practică cu scai'), ('contrafort', 'Contrefort ușor rigidizat'),
   ('vârf', 'Vârf ranforsat , care ajută la menținerea formei pantofului'), ('talpă', 'Talpă realizată din cauciuc rezistent')],
  {'Model': 'Wheat WF622-02', 'Material': 'piele întoarsă, interior și branț din piele fără crom, talpă din cauciuc', 'Caracteristici': 'scai, imprimeu floral, vârf ranforsat', 'Cod produs': 'WF622-02'})

w(11010,
  f'<p>Geaca {A("/brand/ea7-emporio-armani/", "EA7 Emporio Armani")} 8NFB08 FNF8Z este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, neagră, ușor izolată cu umplutură sintetică, din țesătură durabilă, pentru zilele reci de iarnă și de tranziție.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar căptușeala completă o face ușor de purtat peste alte straturi. Gluga se detașează când vremea se încălzește.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 140-170 sunt pentru copii de 10-15 ani, de obicei.</p>',
  [('model', 'EA7 Emporio Armani Geacă petrecută pentru copii neagră 8NFB08 FNF8Z'), ('matlasat', 'structură matlasată'), ('izolat', 'Izolare: usor izolat'),
   ('umplutură', 'Umplutură sintetică ușoară'), ('țesătură', 'Țesătură exterioară durabilă'), ('iarnă', 'condițiile de iarnă și de tranziție'), ('croială', 'Croială regulară'),
   ('lungime', 'Lungime până la șolduri'), ('căptușeală', 'Căptușeală interioară completă sporește confortul la purtare, facilitând îmbrăcarea peste alte straturi'),
   ('glugă', 'Glugă detașabilă'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'), ('buzunare', 'Buzunare laterale practice'), ('material', '100% Poliester')],
  {'Model': 'EA7 Emporio Armani 8NFB08 FNF8Z', 'Material': '100% poliester', 'Caracteristici': 'matlasată, ușor izolată, glugă detașabilă', 'Cod produs': '8NFB08 FNF8Z'})

w(11015,
  f'<p>Pantofii {GEOX} STEPPIEUP Barefoot B4663A sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi barefoot pentru bebeluși")}, maro, din piele naturală, cu interior și branț din piele. Stilul barefoot lasă piciorul să se așeze natural, iar tehnologia Geox Respira™ scoate umiditatea.</p>'
  '<p>Vârful e lat și moale, deci degetele stau liber și pantoful merge și la un picior mai lat. Aricii permit încălțatul rapid și ajustarea pe picior.</p>'
  '<p>Pe scurt:</p>'
  + L(('Partea de sus', 'piele naturală.'), ('Interior și branț', 'piele naturală.'), ('Talpă', 'din cauciuc, flexibilă.'))
  + '<p>Numerele 20-27 sunt pentru copii de în jur de 1-4 ani.</p>',
  [('model', 'Geox Pantofi pentru copii din piele STEPPIEUP Barefoot maro B4663A.000AK'), ('piele', 'Partea superioară din piele naturală'), ('interior', 'Interior din piele naturală'),
   ('branț', 'Branț din piele naturală'), ('barefoot', 'Stilul barefoot susține dezvoltarea liberă a picioarelor'), ('Respira', 'Tehnologia GEOX Respira™ contribuie la evacuarea umidității'),
   ('vârf', 'Vârf lat și moale permite așezarea liberă a degetelor piciorului'), ('arici', 'Sistem de închidere cu arici facilitează încălțarea rapidă și ajustarea'),
   ('talpă', 'Talpă din cauciuc permite o bună aderență și flexibilitate')],
  {'Model': 'Geox STEPPIEUP Barefoot', 'Material': 'piele naturală, interior și branț din piele, talpă din cauciuc', 'Caracteristici': 'barefoot, vârf lat, arici, Geox Respira™', 'Cod produs': 'B4663A.000AK'})

w(11021,
  f'<p>Sacoul {A("/brand/mayoral/", "Mayoral")} 6413 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "jachetă din amestec de in pentru băieți")}, bej, uni, din țesătură netedă și aerisită, cu mult bumbac. Se închide cu nasturi pe un singur rând, ca un sacou clasic, pentru ocazii și zile mai calde.</p>'.replace(', pentru ocazii și zile mai calde', '')
  + '<p>Fasonul e drept, fără strângeri pe corp, iar căptușeala îl face ușor de îmbrăcat și de dat jos peste o cămașă.</p>'
  '<p>Pe scurt, despre sacou:</p>'
  + L(('Închidere', 'nasturi, un singur rând.'), ('Material', '90% bumbac, 10% in.'), ('Căptușeală', 'da.'))
  + '<p>Mărimile 128-172 sunt pentru copii de 8-15 ani, cu aproximație.</p>',
  [('model', 'Mayoral Jachetă din amestec de in pentru copii culoarea bej, 6413'), ('sacou', 'Sacou pentru copii din colecția Mayoral'), ('neted', 'țesătură neteda'),
   ('aerisit', 'material aerisit cu un conținut ridicat de bumbac'), ('uni', 'Model: uni'), ('nasturi', 'Închidere cu nasturi la un singur piept'), ('fason', 'Fason drept'),
   ('căptușeală', 'Model cu captuseala'), ('material', '90% Bumbac, 10% In')],
  {'Model': 'Mayoral 6413', 'Material': '90% bumbac, 10% in', 'Caracteristici': 'sacou, nasturi pe un rând, căptușit', 'Cod produs': '6413'},
  notes=['Magazinul îl descrie ca sacou; e listat la Geci.', '„Peste o cămașă” e dedus din faptul că e sacou căptușit.'])
