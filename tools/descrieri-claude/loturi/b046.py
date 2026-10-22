import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
BIO = A('/brand/biomecanics/', 'Biomecanics')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(10724,
  f'<p>{TH} KG0KG09447 este un {A("/categorie/bluze-tricouri-hanorace/", "hanorac pentru fete")}, roz, fără fermoar, din tricot moale și subțire cu bumbac, cu model geometric. E lejer, pentru ținute casual în zilele mai calde.</p>'
  '<p>Croiala e lejeră, cu umerii coborâți pe mânecă, iar bordurile elastice de la bază, manșete și decolteu țin hanoracul în formă. Materialul elastic se îmbracă ușor.</p>'
  '<p>Material și închidere, pe rând:</p>'
  + L(('Decolteu', 'rotund.'), ('Material', '78% bumbac, 18% poliester, 4% elastan.'), ('Model', 'geometric.'))
  + '<p>Mărimile 104-122 sunt pentru copii de 4-7 ani, cu aproximație.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii cu bumbac roz KG0KG09447'), ('fără fermoar', 'Construcție fără fermoar cu decolteu rotund'), ('tricot', 'Tricot moale cu bumbac'),
   ('subțire', 'Material subțire favorizează lejeritatea și confortul în zilele mai calde'), ('geometric', 'Model geometric'), ('casual', 'Stilul casual'),
   ('croială', 'Croială lejeră'), ('umeri', 'Mâneci cu linia umerilor coborâtă'), ('borduri', 'Borduri elastice la bază, manșete și decolteu'), ('elastic', 'Material elastic'),
   ('material', '78% Bumbac, 18% Poliester, 4% Elastan')],
  {'Model': 'Tommy Hilfiger KG0KG09447', 'Material': '78% bumbac, 18% poliester, 4% elastan', 'Caracteristici': 'fără fermoar, croială lejeră, model geometric', 'Cod produs': 'KG0KG09447'})

w(10736,
  f'<p>{GEOX} MACCHIA B164PA sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} bej, ușori, din piele naturală, cu interior din piele, care previne frecarea și mirosul neplăcut. Branțul Geox e din piele perforată, antibacterian și conturat pentru așezarea piciorului.</p>'
  '<p>Velcro-ul se închide repede, iar vârful rotund, ușor rigid, lasă degetele să se așeze liber. Contrafortul rigid ține piciorul în pantof.</p>'
  '<p>Talpa are două sisteme Geox:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Light Flexy', 'branț care lasă piciorul să se miște.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 18-26 sunt pentru copii de 1-4 ani, de regulă.</p>',
  [('model', 'Geox Încălțăminte din piele pentru copii MACCHIA culoarea bej, B164PA.00778'), ('piele', 'confecționat din piele naturală'), ('ușor', 'Model ușor'),
   ('interior', 'Un model cu interior din piele care este confortabil pentru picior și previne frecarea'), ('branț', 'brant din piele cu perforari'),
   ('antibacterian', 'Are proprietati antibacteriene'), ('contur', 'Este conturat corespunzator'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('degete', 'degetele se pot aranja liber în pantof'), ('călcâi', 'Contorul de călcâi rigid'), RESPIRA,
   ('Light Flexy', 'Light Flexy Sistem de brant pentru libertatea de miscare'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox MACCHIA', 'Material': 'piele naturală, interior din piele, talpă din cauciuc', 'Caracteristici': 'velcro, branț Geox antibacterian, Geox Respira, Light Flexy', 'Cod produs': 'B164PA.00778'})

w(10744,
  f'<p>{GEOX} WASHIBA Hello Kitty J66HXH sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil înalt și imprimeu Hello Kitty, din imitație de piele și material textil. Membrana microporoasă Geox Respira™ scoate umiditatea și ține picioarele uscate.</p>'
  '<p>Au șireturi și fermoar: șiretul se reglează o dată după picior, iar fermoarul ajută la încălțat repede. Branțurile textile se scot, pentru curățat sau pentru verificat mărimea.</p>'
  '<p>Pentru purtat zilnic, contează și:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Guler', 'ușor întărit, în jurul gleznei.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-31 sunt pentru copii de în jur de 2-7 ani.</p>',
  [('model', 'Geox WASHIBA Hello Kitty sneakers pentru copii roz J66HXH.054AS'), ('profil', 'Profilul înalt al părții superioare'), ('Hello Kitty', 'Imprimeul adorabil Hello Kitty'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia Geox Respira™ cu membrană microporoasă favorizează evacuarea umidității, menținând picioarele uscate'),
   ('închidere', 'Închiderea cu șireturi și fermoar'), ('branțuri', 'Branțurile detașabile din material textil'), ('călcâi', 'Călcâiul ușor întărit'),
   ('guler', 'Gulerul superior ușor întărit'), ('interior', 'Interiorul căptușit cu material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox WASHIBA Hello Kitty', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, șireturi și fermoar, branțuri detașabile', 'Cod produs': 'J66HXH.054AS'})

w(10749,
  f'<p>{TH} KB0KB10473 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză polo pentru băieți")}, bleumarin, cu dungi și logo brodat, din bumbac 100% cu material elastic. Croiala clasică de polo merge și la ținute casual, și la ocazii mai elegante.</p>'
  '<p>Croiala e regulară și nu strânge pe corp, iar materialul elastic urmează mișcarea. Decolteul are guler și închidere.</p>'
  '<p>Ce merită știut în plus:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'cu guler și închidere.'), ('Detalii', 'dungi și logo brodat.'))
  + '<p>Mărimile 128-176 sunt pentru copii de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Polo pentru copii din bumbac bleumarin KB0KB10473'), ('dungi', 'Modelul cu dungi precum și logo-ul brodat al mărcii'), ('bumbac', '100% Bumbac'),
   ('elastic', 'Materialul elastic'), ('polo', 'Croiala clasică de polo oferă stilizărilor un caracter elegant și, în același timp, casual'), ('croială', 'Croiala regulară'),
   ('decolteu', 'Decolteu cu guler și închidere')],
  {'Model': 'Tommy Hilfiger KB0KB10473', 'Material': '100% bumbac', 'Caracteristici': 'polo, dungi, logo brodat', 'Cod produs': 'KB0KB10473'})

w(10753,
  f'<p>{GEOX} IUPIDOO Hello Kitty B6658A sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, cu motiv Hello Kitty, din imitație de piele ușor de întreținut și cu interior căptușit cu piele naturală. Membrana microporoasă Geox Respira™ scoate umiditatea.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, iar banda se strânge după cât de lat e piciorul. Gulerul ușor întărit cuprinde glezna fără să o strângă.</p>'
  '<p>Alte detalii utile:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Interior', 'piele naturală.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 18-26 sunt pentru cei mici de aproximativ 1-4 ani.</p>',
  [('model', 'Geox IUPIDOO Hello Kitty sneakers pentru copii roz B6658A.05402'), ('material', 'Partea superioară din imitație de piele constituie un strat exterior rezistent, ușor de întreținut'),
   ('interior', 'Interiorul căptușit cu piele naturală'), ('Respira', 'Tehnologia GEOX Respira™ cu membrană microporoasă favorizează eliminarea umidității'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă'), ('guler', 'Gulerul superior ușor întărit'), ('călcâi', 'Călcâiul ușor întărit'),
   ('talpă', 'Talpa plată din cauciuc'), ('Hello Kitty', 'IUPIDOO Hello Kitty')],
  {'Model': 'Geox IUPIDOO Hello Kitty', 'Material': 'imitație de piele, interior din piele naturală, talpă din cauciuc', 'Caracteristici': 'arici, Geox Respira™', 'Cod produs': 'B6658A.05402'})

w(10755,
  f'<p>Geaca {TH} KS0KS00652 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă cu puf pentru băieți")}, bleumarin, matlasată, cu izolație ușoară din puf natural de rață și pene, pentru sezonul de tranziție și zilele mai reci. Gulerul ridicat apără gâtul de frig și vânt.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar manșetele cu bordură elastică strâng la încheieturi. Căptușeala completă o face ușor de purtat peste alte straturi.</p>'
  '<p>Alte detalii utile:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale.'), ('Material', '100% nailon; umplutură 90% puf, 10% pene de rață.'))
  + '<p>Mărimile 104-176 sunt pentru copii de 4-16 ani, în mare.</p>',
  [('model', 'Tommy Hilfiger Geacă cu puf pentru copii bleumarin KS0KS00652'), ('matlasat', 'Construcția matlasată'), ('puf', 'Izolație termică din puf natural'),
   ('compoziție', '90% Puf de rață, 10% Pene de rață'), ('tranziție', 'sezonul de tranziție'), ('guler', 'Gulerul ridicat protejează gâtul de frig și vânt'),
   ('croială', 'Croiala regulară'), ('lungime', 'Lungimea până la șolduri'), ('manșete', 'Manșetele cu bordură elastică'),
   ('căptușeală', 'Căptușeala completă contribuie la purtarea confortabilă peste diverse straturi'), ('fermoar', 'Închiderea cu fermoar'), ('buzunare', 'Buzunarele laterale practice'),
   ('nailon', '100% Nailon')],
  {'Model': 'Tommy Hilfiger KS0KS00652', 'Material': '100% nailon; umplutură 90% puf de rață, 10% pene', 'Caracteristici': 'puf natural, matlasată, guler ridicat', 'Cod produs': 'KS0KS00652'})

w(10761,
  f'<p>{GEOX} SPRINTYE FAST IN J65NQA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, cu profil scurt, din material textil și piele ecologică, cu detalii decorative. Interiorul e textil și se ține ușor curat, iar talpa are sistemul Geox Respira.</p>'
  '<p>Șireturile elastice și bucla de pe limbă permit încălțatul fără legat, deci copilul se descurcă singur dimineața.</p>'
  '<p>Forma pantofului vine din:</p>'
  + L(('Vârf', 'rotund.'), ('Partea de sus', 'rigidizată.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 28-39 sunt pentru copii de la, în mare, 4 ani în sus.</p>',
  [('model', 'Geox Sneakers pentru copii SPRINTYE FAST IN J65NQA.01454'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('decor', 'Detalii decorative'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), RESPIRA,
   ('șireturi', 'Șireturile elastice fac pantofii ușor de pus și de scos'), ('buclă', 'O buclă pe limbă facilitează alunecarea pantofului pe picior'), ('vârf', 'Varf rotund'),
   ('rigidizat', 'Partea superioară rigidizată'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox SPRINTYE FAST IN', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice, buclă pe limbă, Geox Respira', 'Cod produs': 'J65NQA.01454'},
  notes=['Titlul spune bleumarin; magazinul dă culoarea albastru.'])

w(10764,
  f'<p>Cizmele de iarnă {A("/brand/reima/", "Reima")} Talvella Kids 5400150A sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de iarnă unisex")}, maro, izolate, din material textil și piele ecologică, rezistente la apă. Interiorul moale căptușit ține de cald, iar elementele reflectorizante îl fac pe copil vizibil seara.</p>'
  '<p>Șireturile elastice cu cârlig și bucla de la spate permit încălțatul rapid, iar partea de sus ridicată rigidizează glezna pe teren denivelat.</p>'
  '<p>Cizma mai are:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Călcâi', 'contrafort rigid.'), ('Inserție', 'textilă, detașabilă, ușor de curățat.'), ('Talpă', 'exterioară, din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 22-31 se poartă de obicei între 1 și 7 ani.</p>',
  [('model', 'Reima Cizme de iarna pentru copii Talvella Kids culoarea maro, 5400150A'), ('izolat', 'Model izolat'), ('material', 'combinatia materialului textil cu pielea ecologica'),
   ('apă', 'Model rezistent la apa'), ('interior', 'Interiorul moale căptușit asigură un confort ridicat la purtare și un confort termic optim'),
   ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('teren', 'suprafețe neuniforme'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid'),
   ('inserție', 'Inserție textilă detașabilă, ușor de curățat'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Reima Talvella Kids', 'Material': 'textil și piele ecologică, interior textil căptușit, talpă din cauciuc', 'Caracteristici': 'izolate, rezistente la apă, șireturi elastice cu cârlig, reflectorizante', 'Cod produs': '5400150A'})

w(10772,
  f'<p>{BIO} 261255 sunt {A("/categorie/ghete-cizme/", "ghete de iarnă pentru fete")}, multicolore, cu carâmb înalt și interior izolat din pluș moale. Membrana BioTEX, cu structură polimerică microporoasă, ține picioarele uscate și calde în zilele reci.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, deci copilul se descurcă singur, iar profilul înalt cuprinde glezna.</p>'
  '<p>Pentru zăpadă și gheață:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare.'), ('Vârf și călcâi', 'rigidizat, respectiv întărit.'), ('Parteneriat', 'Biomecanics Podology, cu podologii.'))
  + '<p>Numerele 24-34 sunt pentru copii de 2-11 ani, cu aproximație.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii multicolor 261255'), ('carâmb', 'Profil înalt al carâmbului'), ('pluș', 'Interior izolat termic din pluș moale'),
   ('BioTEX', 'Membrana BioTEX cu o structură polimerică microporoasă ajută la menținerea uscăciunii și căldurii'), ('reci', 'zilele reci'),
   ('arici', 'Închidere cu arici facilitează încălțarea și descălțarea rapidă'), ('independență', 'încurajează independența copilului'),
   ('talpă', 'Talpă din cauciuc cu bandă de rulare'), ('întărit', 'Călcâi întărit și vârf rigidizat'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261255', 'Material': 'sintetic și textil, interior din pluș, talpă din cauciuc', 'Caracteristici': 'membrană BioTEX, izolate, arici, profil înalt', 'Cod produs': '261255'})

w(10773,
  f'<p>{BIO} 261153 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași înalți pentru bebeluși")}, bleumarin, din piele naturală, cu interior și branț din lână, moi pentru picioarele copilului. Sunt făcuți în parteneriatul Biomecanics Podology.</p>'
  '<p>Vârful rotund, rigidizat, are spațiu suplimentar pentru degete, deci pantoful merge și la un picior mai plin. Aricii permit încălțatul rapid, fără ajutor, iar pielea se adaptează la forma piciorului.</p>'
  '<p>Pentru zilele reci, contează:</p>'
  + L(('Branțuri', 'detașabile, din lână.'), ('Talpă', 'plată, din cauciuc.'), ('Interior', 'lână.'))
  + '<p>Numerele 24-26 sunt pentru copii de 2-4 ani, de obicei.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele bleumarin 261153'), ('înalt', 'Sneakerși Biomecanics înalți'), ('piele', 'Partea superioară din piele naturală'),
   ('lână', 'Interiorul și branțul din lână'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership'),
   ('vârf', 'Vârf rotund, rigidizat , cu spațiu suplimentar'), ('arici', 'Prindere practică cu arici facilitează încălțarea și descălțarea rapidă'),
   ('adaptare', 'adaptându-se la picior'), ('branțuri', 'Branțuri detașabile'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Biomecanics 261153', 'Material': 'piele naturală, interior și branț din lână, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici, branțuri detașabile', 'Cod produs': '261153'})
