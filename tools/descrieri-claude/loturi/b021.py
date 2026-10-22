import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9374,
  f'<p>{BIO} 261242 sunt ghete înalte de iarnă, violet, izolate termic, listate pe site la {A("/categorie/unisex-incaltaminte-pantofi/", "încălțămintea de iarnă unisex")}. Membrana BioTEX ține piciorul uscat, iar impregnarea hidrofobă a exteriorului respinge apa, deci merg prin zăpadă și pe vreme umedă.</p>'
  '<p>Șireturile elastice și aricii se ajustează repede pe picior, iar talpa plată din spumă, cu sistemul Flexi Lite, e ușoară și flexibilă.</p>'
  '<p>Mai au:</p>'
  + L(('Vârf și călcâi', 'vârf rigidizat, călcâi întărit.'), ('Tehnologie', 'Biomecanics Podology Partnership, cu podologi.'), ('Exterior', 'material sintetic și textil.'))
  + '<p>Numerele 25-34 se potrivesc copiilor de cam 2-11 ani.</p>',
  [('cod', 'Încălțăminte pentru copii violet 261242'), ('iarnă', 'Ghetele înalte pentru copii Biomecanics sunt încălțăminte de iarnă izolată termic'),
   ('BioTEX', 'Membrana BioTEX'), ('hidrofob', 'Impregnarea hidrofobă a materialului exterior ajută la respingerea apei'), ('închidere', 'Șireturi elastice și închidere cu arici'),
   ('Flexi Lite', 'Sistemul Flexi Lite'), ('talpă', 'Talpa plată din spumă'), ('vârf, călcâi', 'Vârful rigidizat și călcâiul întărit'),
   ('Podology', 'Tehnologia Biomecanics Podology Partnership'), ('exterior', 'Material sintetic, Material textil')],
  {'Model': 'Biomecanics 261242', 'Material': 'sintetic și textil, talpă din spumă', 'Caracteristici': 'ghete de iarnă izolate, BioTEX, impregnare hidrofobă, Flexi Lite', 'Cod produs': '261242'},
  notes=['Pe site e la Pantofi; produsul e ghetă înaltă de iarnă.'])

w(9381,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KG0KG08911 sunt {A("/categorie/pantaloni-treninguri/", "pantaloni din tricot pentru fete")}, roșii, uni, din tricot fin cu bumbac, poliester, poliamidă și elastan. Sunt pantaloni simpli, de purtat zilnic, acasă sau la școală.</p>'
  '<p>Talia e regulată, cu bandă elastică și șnururi, deci se strânge și pe un copil slab, iar crăcii sunt drepți, nici largi, nici mulați. Cei 2% elastan îi fac să se întindă la mișcare.</p>'
  '<p>Pe scurt:</p>'
  + L(('Buzunare', 'două, laterale.'), ('Compoziție', '46% bumbac, 40% poliester, 12% poliamidă, 2% elastan.'), ('Model', 'uni.'))
  + '<p>Mărimile 128-176 se potrivesc copiilor de pe la 8 până pe la 16 ani.</p>',
  [('cod', 'Pantaloni copii culoarea rosu, uni, KG0KG08911'), ('tricot', 'Model confectionat din tricot fin'), ('talie', 'Talie regulata'), ('elastic', 'Banda elastica in talie'),
   ('șnururi', 'In talie snururi'), ('picior', 'Picior drept'), ('buzunare', 'Două buzunare laterale'), ('compoziție', '46% Bumbac, 40% Poliester , 12% Poliamida, 2% Elastan'),
   ('uni', 'Model: uni')],
  {'Model': 'Tommy Hilfiger KG0KG08911', 'Material': '46% bumbac, 40% poliester, 12% poliamidă, 2% elastan', 'Caracteristici': 'tricot fin, talie elastică cu șnur, picior drept', 'Cod produs': 'KG0KG08911'})

w(9388,
  f'<p>{GEOX} WASHIBA J45HXD sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, din piele întoarsă, ușori și făcuți pentru purtat zilnic, cu profil scurt și sistemul Geox Respira în talpă.</p>'
  '<p>Șireturile elastice îi fac ușor de pus și de scos fără legat, iar vârful rotund, ușor rigid, lasă degetele să stea liber; contorul de călcâi rigid ține piciorul fix. Interiorul textil e ușor de ținut curat.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Interior', 'textil.'), ('Material', 'piele întoarsă.'))
  + '<p>Numerele 28-35 corespund, în mare, vârstei de 4-11 ani.</p>',
  [('model', 'Sneakers pentru copii WASHIBA culoarea alb, J45HXD.000BC'), ('material', 'confecționat din piele întoarsă'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('profil', 'Înălțime: mic de statură'), RESPIRA, ('șireturi', 'Șireturile elastice fac pantofii ușor de pus și de scos'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('degete', 'degetele se pot aranja liber'), ('călcâi', 'Contorul de călcâi rigid'), ('talpă', 'Talpa exterioară din cauciuc'), ('interior', 'Interiorul textil')],
  {'Model': 'Geox WASHIBA J45HXD', 'Material': 'piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice, Geox Respira, profil scurt', 'Cod produs': 'J45HXD.000BC'})

w(9406,
  f'<p>{GEOX} LOFTUS J65M2B sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, lucrați din material sintetic și textil, ușori și făcuți pentru purtat zilnic. Au profil scurt și sistemul Geox Respira în talpă.</p>'
  '<p>Șireturile elastice și închiderea cu cârlig se strâng fără nod, deci copilul se încalță singur; vârful e rotund și ușor întărit, iar contorul rigid de la călcâi ține piciorul în pantof.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Interior', 'textil.'), ('Profil', 'scurt.'))
  + '<p>Pe site sunt numerele 24-35, potrivite cam pentru 2-11 ani.</p>',
  [('model', 'Sneakers pentru copii LOFTUS culoarea roz, J65M2B.0BC14'), ('material', 'combinația materialului sintetic cu cel textil'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('profil', 'Înălțime: mic de statură'), RESPIRA, ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('vârf', 'Cutie rotunda, usor intarita'),
   ('călcâi', 'Contorul de călcâi rigid'), ('talpă', 'Talpa exterioară din cauciuc'), ('interior', 'Interiorul textil')],
  {'Model': 'Geox LOFTUS J65M2B', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice cu cârlig', 'Cod produs': 'J65M2B.0BC14'})

w(9408,
  f'<p>{GEOX} NASHIK sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, din piele naturală, piele întoarsă și textil, cu talpa GEOX Respira™ cu membrană microporoasă patentată, care elimină umezeala. Sunt potriviți pentru joaca afară și pentru grădiniță.</p>'
  '<p>Gulerul ușor întărit se așază pe gleznă, iar branțurile detașabile din piele naturală se scot pentru curățat și pentru verificat lungimea piciorului.</p>'
  '<p>Mai au:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Interior', 'căptușit cu material textil și piele naturală.'))
  + '<p>Numerele 20-23 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'Geox NASHIK sneakers pentru copii roz B663HB.0CL22'), ('material', 'combinație de piele naturală, piele întoarsă și material textil'),
   ('Respira', 'Tehnologia GEOX Respira™ cu membrană microporoasă patentată'), ('grădiniță', 'jocurilor în aer liber și la grădiniță'), ('guler', 'Gulerul superior ușor întărit'),
   ('branț', 'Branțurile detașabile din piele naturală'), ('talpă', 'Talpa plată din cauciuc'), ('călcâi', 'Călcâiul întărit'), ('interior', 'Material textil, Piele naturală')],
  {'Model': 'Geox NASHIK', 'Material': 'piele naturală, piele întoarsă și textil, talpă din cauciuc', 'Caracteristici': 'GEOX Respira™, branț din piele detașabil', 'Cod produs': 'B663HB.0CL22'})

w(9409,
  f'<p>{A("/brand/guess/", "GUESS")} K6YL03 este o {A("/categorie/geci-jachete/", "geacă bomber pentru fete")}, roșie, cu ecusoane decorative, ușor izolată cu umplutură sintetică și căptușeală integrală. E pentru zilele răcoroase de tranziție, la ținute casual.</p>'
  '<p>Croiala e regulară, lungă până la șolduri, iar marginea de jos elastică și manșetele cu nervuri strâng geaca, ca să nu intre vântul. Se închide cu capse, mai ușor de prins pentru un copil mic.</p>'
  '<p>Din ce e făcută:</p>'
  + L(('Exterior', 'poliamidă cu acoperire din poliuretan și poliester cu bumbac.'), ('Căptușeală', '100% poliester.'), ('Umplutură', '100% poliester.'))
  + '<p>Mărimile duble, de la 88-96 până la 122-125, sunt pentru copii de pe la 1 până pe la 7 ani.</p>',
  [('cod', 'Geacă bomber pentru copii roșie K6YL03 W2586'), ('ecusoane', 'Ecusoane decorative'), ('izolație', 'Izolație sintetică ușoară'), ('căptușeală', 'Căptușeală integrală'),
   ('tranziție', 'sezonului de tranziție'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'), ('margine', 'Margine inferioară elastică'),
   ('manșete', 'Manșete cu nervuri'), ('capse', 'Închidere cu capse'), ('material 1', '100% Poliamidă acoperită cu poliuretan'), ('material 2', '90% Poliester, 10% Bumbac')],
  {'Model': 'GUESS K6YL03', 'Material': 'poliamidă cu poliuretan, poliester cu bumbac', 'Caracteristici': 'bomber, ușor izolată, capse, margine elastică, ecusoane', 'Cod produs': 'K6YL03.W2586'},
  notes=['Titlul de pe site nu are culoare; magazinul o descrie ca roșie.'])

w(9411,
  f'<p>{A("/brand/reima/", "Reima")} Vaeltaa sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni jogger outdoor unisex")}, roz, din poliester cu tehnologie de rezistență la umezeală, gândiți pentru drumeții și pentru joaca zilnică afară, pe orice vreme.</p>'
  '<p>Croiala e relaxată, iar talia elastică are șnururi, deci pantalonii se strâng pe un copil slab. Manșetele elastice de la glezne țin crăcii pe loc și nu lasă murdăria să intre.</p>'
  '<p>Pentru joacă și teren:</p>'
  + L(('Întărituri', 'la genunchi și la șezut.'), ('Buzunare', 'laterale.'), ('Material', 'poliester, cu inserții acoperite cu TPU.'))
  + '<p>Mărimile 104-164 sunt pentru copii de aproximativ 4-14 ani.</p>',
  [('model', 'Reima Pantaloni pentru copii Vaeltaa roz 5100260A'), ('jogger', 'Pantaloni jogger – model creat pentru activități în aer liber'),
   ('umezeală', 'Tehnologie de rezistență la umezeală'), ('drumeții', 'drumeții și jocuri zilnice în aer liber'), ('croială', 'Croială relaxată'),
   ('talie', 'Talie elastică cu șnururi'), ('manșete', 'Manșete elastice la glezne'), ('întărituri', 'Întărituri la genunchi și șezut'), ('buzunare', 'Buzunare laterale practice'),
   ('material', '100% Poliester'), ('TPU', '100% Poliester acoperit cu TPU')],
  {'Model': 'Reima Vaeltaa', 'Material': 'poliester, inserții cu TPU', 'Caracteristici': 'jogger outdoor, croială relaxată, talie elastică cu șnur, întărituri', 'Cod produs': '5100260A'})

w(9412,
  f'<p>{GEOX} THELEVEN J56HTA sunt {A("/categorie/adidasi/", "adidași pentru fete")} bleumarin, cu fața din piele naturală și piele ecologică, ușori și făcuți pentru purtat zilnic. Au profil jos și talpă exterioară din cauciuc.</p>'
  '<p>Șireturile elastice și închiderea cu cârlig se strâng fără nod, iar contorul de călcâi rigid ține piciorul în pantof; vârful rotund e întărit și protejează degetele.</p>'
  '<p>Pe scurt:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'din cauciuc.'), ('Profil', 'jos.'))
  + '<p>Numerele 28-35 sunt pentru copii de pe la 4 până pe la 11 ani.</p>',
  [('model', 'Sneakers pentru copii THELEVEN culoarea bleumarin, J56HTA.077BC'), ('material', 'combinația pielii naturale cu cea ecologică'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('profil', 'Înălțime: jos'), ('talpă', 'Talpa exterioară din cauciuc'), ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('călcâi', 'Contorul de călcâi rigid'),
   ('vârf', 'Cutie rotunda, intarita'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Geox THELEVEN J56HTA', 'Material': 'piele naturală și piele ecologică, interior textil', 'Caracteristici': 'șireturi elastice cu cârlig, profil jos', 'Cod produs': 'J56HTA.077BC'})

w(9425,
  f'<p>{BIO} 261129 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi îmblăniți pentru bebeluși")}, bleumarin, din piele naturală, cu branț și interior din lână, deci țin de cald în zilele reci. Au fost proiectați împreună cu podologi, în programul Biomecanics Podology.</p>'
  '<p>Închiderea cu arici are o curea reglabilă, ca pantoful să stea exact pe picior, iar călcâiul și gulerul moi nu irită pielea. Talpa din cauciuc e flexibilă.</p>'
  '<p>Mai au:</p>'
  + L(('Vârf', 'rotund, cauciucat, protejează degetele.'), ('Interior', 'lână.'), ('Material', 'piele naturală.'))
  + '<p>Numerele de pe site, 18-25, sunt pentru copii de cam 1-3 ani.</p>',
  [('model', 'Încălțăminte pentru copii din piele bleumarin 261129'), ('piele', 'Partea superioară din piele naturală'), ('lână', 'Branț și interior din lână'),
   ('izolat', 'propunere izolată termic'), ('Podology', 'Biomecanics Podology'), ('podologi', 'Proiectați în colaborare cu podologi'),
   ('arici', 'Închidere cu arici cu curea reglabilă'), ('moale', 'Călcâi moale și gulerul părții superioare'), ('talpă', 'Talpă flexibilă din cauciuc'),
   ('vârf', 'Vârf cauciucat și rotund')],
  {'Model': 'Biomecanics 261129', 'Material': 'piele naturală, interior din lână', 'Caracteristici': 'izolați, interior din lână, arici cu curea reglabilă, vârf cauciucat', 'Cod produs': '261129'})

w(9438,
  f'<p>{GEOX} BISLI sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi de iarnă pentru bebeluși")}, bleumarin, ușor izolați, cu partea de sus din textil și imitație de piele. Sunt pentru toamnă și iernile blânde, cu sistemul Geox Respira în talpă.</p>'
  '<p>Șireturile elastice și închiderea cu cârlig se strâng fără nod, iar bucla de la spate ajută la încălțat; vârful e rotund și întărit.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Interior', 'textil.'), ('Izolație', 'ușoară.'))
  + '<p>Numerele 20-27 se potrivesc în general copiilor de 1-4 ani.</p>',
  [('model', 'Pantofi copii BISLI culoarea albastru marin, B461NC.0MEFU'), ('iarnă', 'Pantofi de iarna pentru copii'), ('izolat', 'Model Izolare usoara'),
   ('material', 'combinatia materialului textil cu pielea ecologica'), RESPIRA, ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('buclă', 'Bucla de la spate'),
   ('vârf', 'Cutie rotunda, intarita'), ('talpă', 'Talpa exterioară din cauciuc'), ('interior', 'Interiorul textil')],
  {'Model': 'Geox BISLI', 'Material': 'textil și imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'ușor izolați, Geox Respira, șireturi elastice cu cârlig', 'Cod produs': 'B461NC.0MEFU'})
print('lot 21 scris')
