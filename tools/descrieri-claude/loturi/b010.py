import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

BIO = A('/brand/biomecanics/', 'Biomecanics')
PRIM = A('/brand/primigi/', 'Primigi')

w(8845,
  f'<p>{A("/brand/columbia/", "Columbia")} Hikebound este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")}, portocalie, izolată cu umplutură sintetică și cu două tehnologii Columbia: Omni-Heat, care reglează temperatura corpului la efort, și Omni-tech®, cu membrană microporoasă și cusături sudate. E făcută pentru frig și pentru vremea care se schimbă brusc.</p>'
  '<p>Croiala e simplă și lungă, iar mânecile se termină cu bandă elastică, deci geaca stă strânsă la încheieturi.</p>'
  '<p>Pentru ieșirile pe frig:</p>'
  + L(('Închidere', 'fermoar și arici.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Glugă', 'are.'), ('Căptușeală', 'poliester și poliamidă.'))
  + '<p>Geaca vine în mărimile 104-164, potrivite copiilor de cam 4-14 ani.</p>',
  [('model', 'Geacă copii Hikebound culoarea portocaliu, 2089961'), ('izolat', 'Model izolat'), ('izolație', 'izolație sintetică'), ('Omni-Heat', 'Tehnologia Omni-Heat'),
   ('temperatură', 'regleaza temperatura corpului in timpul exercitiilor'), ('Omni-tech', 'Tehnologia Omni-tech'),
   ('membrană', 'membranei microporoase, respirabile si a cusaturilor sudate'), ('vreme', 'schimbarilor bruste ale vremii'), ('croială', 'Tăiere simplă'),
   ('elastic', 'Mâneci finisate cu o coadă elastică'), ('închidere', 'Fixarea cu fermoar si velcro'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('glugă', 'Gluga: cu gluga'), ('căptușeală 2', 'Captuseala 2: 100% Poliamida')],
  {'Model': 'Columbia Hikebound', 'Material': '100% poliester, căptușeală poliester și poliamidă', 'Caracteristici': 'Omni-Heat, Omni-tech®, izolată, glugă, fermoar și arici', 'Cod produs': '2089961'})

w(8856,
  f'<p>{BIO} 251135 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} violet, din material textil și piele ecologică, cu profil scurt și vârf din gumă. Au fost creați împreună cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia.</p>'
  '<p>Închiderea cu arici permite o potrivire individuală la picior, iar cutia lată a degetelor lasă loc degetelor să stea drept.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Inserție', 'Plantilla, cu perforații.'), ('Talpă', 'exterioară, din cauciuc.'), ('Vârf', 'rigidizat, cu protecție din gumă.'), ('Călcâi', 'ușor rigidizat.'))
  + '<p>Numerele de pe site, 19-25, sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('cod', '251135'), ('culoare', 'culoarea violet'), ('material', 'combinația materialului textil cu pielea ecologică'), ('profil', 'Înălțime: mic de statură'),
   ('vârf gumă', 'Varf din guma'), ('Valencia', 'medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'),
   ('arici', 'Modelul cu închidere velcro permite o potrivire individuală la picior'), ('cutie lată', 'Cutia lată a degetelor'), ('inserție', 'Inserția Plantilla cu perforații'),
   ('talpă', 'Talpa exterioară din cauciuc'), ('vârf', 'Varf rigidizat'), ('călcâi', 'Spatele calcaiului usor rigidizat')],
  {'Model': 'Biomecanics 251135', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, cutie lată a degetelor, inserție Plantilla, vârf din gumă', 'Cod produs': '251135'})

w(8866,
  f'<p>{A("/brand/guess/", "GUESS")} are aici o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă matlasată pentru bebeluși")} și copii mici, bleumarin, ușor izolată și căptușită, cu glugă. E o geacă pentru toamnă și zilele mai reci, din țesătură ornamentată de poliester.</p>'
  '<p>Fasonul e drept, iar gulerul ridicat are o bandă pe fermoar, ca acesta să nu atingă bărbia copilului.</p>'
  '<p>Se îmbracă repede, chiar și pe un copil foarte mic:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'oblice, cu închidere.'), ('Glugă', 'are.'), ('Material', '100% poliester, inclusiv căptușeala și umplutura.'))
  + '<p>Pe site sunt mărimile de la 55-62 până la 122, adică de la nou-născut până pe la 7 ani.</p>',
  [('culoare', 'culoarea albastru marin'), ('ușor izolat', 'Model usor izolat'), ('matlasat', 'Matlasat'), ('căptușeală', 'Model izolat cu captuseala'), ('glugă', 'Model cu gluga'),
   ('ornamentat', 'Tesatura ornamentata'), ('fason', 'Fason drept'), ('guler', 'Guler ridicat cu membrana pe fermoar'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare oblice incheiate'), ('material', 'Materialul de baza: 100% Poliester'), ('umplutură', 'Umplutura: 100% Poliester')],
  {'Model': 'GUESS, geacă bebe', 'Material': '100% poliester', 'Caracteristici': 'ușor izolată, matlasată, glugă, guler ridicat, buzunare închise', 'Cod produs': ''},
  varsta_txt='0-7 ani')

w(8881,
  f'<p>{A("/brand/burton/", "Burton")} OUTBM este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de schi unisex")}, verde, izolată, cu căptușeală fleece care se poate purta și separat, ca strat de mijloc. Cusăturile principale sunt etanșate cu bandă, deci geaca ține vântul și umezeala afară pe pârtie.</p>'
  '<p>Spatele e mai lung și acoperă bine când copilul se apleacă, iar mânecile se reglează cu arici la încheietură. În interior are o centură elastică, cauciucată, care oprește zăpada.</p>'
  '<p>Detaliile de pârtie:</p>'
  + L(('Ventilație', 'deschideri cu fermoar sub axile.'), ('Buzunare', 'mai multe, plus buzunar de ski-pass pe mânecă.'), ('Glugă', 'fixă, cu guler ridicat.'), ('Certificare', 'Burton e companie B Corporation.'))
  + '<p>Mărimile de pe site, de la 116-122 la 152, sunt pentru copii de pe la 6 până pe la 12 ani.</p>',
  [('model', 'Geaca copii OUTBM culoarea verde, 243141'), ('izolat', 'Model izolat'), ('fleece', 'căptușeală fleece care poate fi purtată separat'),
   ('cusături', 'Cusăturile principale cu bandă etanșează și împiedică vântul și umezeala'), ('spate', 'Spatele mai lung oferă acoperire'),
   ('arici', 'Marginile inferioare ale mânecilor sunt reglabile cu Velcro'), ('centură', 'centura flexibila, cauciucata'),
   ('ventilație', 'Deschideri de ventilatie cu fermoar sub axile'), ('buzunare', 'Sistemul extins de buzunare'), ('ski-pass', 'Buzunar ski-pass pe maneca'),
   ('glugă, guler', 'Gulerul ridicat și gluga fixă'), ('B Corp', 'B Corporation')],
  {'Model': 'Burton OUTBM', 'Material': 'nailon cu spandex și poliester, umplutură parțial reciclată', 'Caracteristici': 'geacă de schi, căptușeală fleece detașabilă, cusături etanșate, ventilație sub axile', 'Cod produs': '243141'})

w(8886,
  f'<p>{PRIM} PTIGT 23548 în varianta maro sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi impermeabili pentru bebeluși")} și copii mici, din piele naturală și material sintetic, cu membrana GORE-TEX® (ePTFE), care oprește apa și vântul. Au stil casual, pentru ținutele de zi cu zi.</p>'
  '<p>Aricii fac încălțatul rapid, chiar și de unul singur, iar vârful rotund, rigidizat, lasă loc degetelor și le protejează la joacă.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Shock Absorber', 'sistem în talpă.'), ('Talpă', 'din cauciuc, flexibilă.'), ('Branț', 'detașabil, din material textil.'), ('Călcâi', 'întărit, cu guler.'))
  + '<p>Numerele 20-29 corespund aproximativ vârstei de 1-5 ani.</p>',
  [('cod', 'Pantofi pentru copii maro PTIGT 23548'), ('material', 'Partea superioară din piele naturală și imitație'), ('GORE-TEX', 'Tehnologia GORE-TEX® cu membrană ePTFE'),
   ('apă, vânt', 'protecție împotriva apei și vântului'), ('casual', 'Stilul casual face ca încălțămintea să se potrivească ținutelor zilnice'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă'), ('vârf', 'Vârful rotund, rigidizat'), ('Shock Absorber', 'Sistemul Shock Absorber în talpă'),
   ('talpă', 'Talpa din cauciuc'), ('branț', 'Branțul detașabil din material textil'), ('călcâi', 'Călcâiul întărit')],
  {'Model': 'Primigi PTIGT 23548', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, Shock Absorber, arici, branț detașabil', 'Cod produs': '23548'})

w(8905,
  f'<p>{PRIM} PYR GTX 14200 sunt {A("/categorie/adidasi/", "adidași impermeabili pentru fete")} albi, din piele întoarsă și material textil, cu membrana GORE-TEX® și talpă Vibram®. Sunt pentru primăvară, vară și toamnă, inclusiv pe iarbă udă sau prin bălți.</p>'
  '<p>Partea de sus urcă până la gleznă, cu guler ușor întărit, iar șireturile elastice și aricii se ajustează repede; gaica de la spate îl ajută pe copil să se încalțe singur.</p>'
  '<p>Pe dedesubt și înăuntru:</p>'
  + L(('Talpă', 'Vibram®, din cauciuc cu striații.'), ('Contrefort', 'rigidizat.'), ('Interior', 'material textil.'))
  + '<p>Numerele 26-29 sunt, de obicei, pentru copii de 3-5 ani.</p>',
  [('cod', 'PYR GTX 14200'), ('culoare', 'Sneakers pentru copii alb'), ('material', 'Fața din piele întoarsă și material textil'), ('GORE-TEX', 'Membrana GORE-TEX® asigură picioare uscate'),
   ('Vibram', 'Talpa Vibram'), ('sezon', 'aventurile de primăvară, vară și toamnă'), ('gleznă', 'Fața până la gleznă'), ('guler', 'guler ușor întărit'),
   ('închidere', 'Șireturile elastice și închiderea cu velcro'), ('gaică', 'Gaica practică din spate facilitează încălțarea autonomă'),
   ('striații', 'Talpa de cauciuc cu striații'), ('contrefort', 'Contrefortul rigidizat'), ('interior', 'Interiorul din material textil')],
  {'Model': 'Primigi PYR GTX 14200', 'Material': 'piele întoarsă și textil, interior textil, talpă Vibram®', 'Caracteristici': 'GORE-TEX®, Vibram®, șireturi elastice și arici, gaică', 'Cod produs': '14200'})

w(8908,
  f'<p>{BIO} 261151 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} multicolori, din piele naturală și material sintetic, cu profil scurt și talpă plată din cauciuc. Sunt pentru joaca și activitățile de zi cu zi ale copiilor mici, iar talpa plată merge pe diverse suprafețe, la mers și la joacă.</p>'
  '<p>Aricii îi permit copilului să se încalțe și să se descalțe singur, iar profilul scurt lasă glezna liberă.</p>'
  '<p>Construcția, pe scurt:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'material textil.'), ('Branț', 'textil.'))
  + '<p>Mărimile 19-26 se potrivesc, în general, copiilor de 1-4 ani.</p>',
  [('cod', '261151'), ('culoare', 'design multicolor'), ('material', 'Partea superioară din piele naturală în combinație cu material sintetic'),
   ('profil', 'Profil scurt'), ('talpă', 'Talpă plată din cauciuc oferă stabilitate în timpul mersului și al jocurilor pe diverse suprafețe'), ('zilnic', 'jocurilor și activităților zilnice'), ('arici', 'Închidere practică cu arici'),
   ('călcâi', 'Călcâi întărit'), ('interior', 'Interior din material textil'), ('branț', 'Branț din material textil')],
  {'Model': 'Biomecanics 261151', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, profil scurt, talpă plată', 'Cod produs': '261151'})

w(8909,
  f'<p>{BIO} 261156 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, uni, din piele naturală, cu profil scurt și talpă din cauciuc. Pielea se adaptează în timp la forma piciorului, iar culoarea bleumarin, uni, merge cu multe haine.</p>'
  '<p>Căptușeala textilă e moale, iar închiderea cu arici se prinde repede pe picior; profilul scurt nu restricționează glezna la joacă. Branțul textil ajută la păstrarea prospețimii în pantof.</p>'
  '<p>Ce mai are:</p>'
  + L(('Călcâi', 'întărit.'), ('Branț', 'din material textil.'), ('Material', 'piele naturală și material sintetic.'))
  + '<p>Pe site sunt numerele 21-26, cam pentru 1-4 ani.</p>',
  [('cod', 'Sneakers pentru copii bleumarin 261156'), ('piele', 'Partea superioară din piele naturală'), ('adaptare', 'adaptarea la forma piciorului'), ('uni', 'Modelul uni'),
   ('profil', 'Profilul scurt al părții superioare'), ('talpă', 'Talpa din cauciuc'), ('căptușeală', 'Căptușeala textilă moale'),
   ('arici', 'Sistemul practic de închidere cu arici'), ('călcâi', 'Călcâiul întărit'), ('branț', 'Branțul din material textil asigură ventilația și menținerea prospețimii'), ('material', 'Piele naturală, Material sintetic'), ('culoare', 'Culoarea bleumarin')],
  {'Model': 'Biomecanics 261156', 'Material': 'piele naturală și sintetic, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'arici, profil scurt, călcâi întărit', 'Cod produs': '261156'})

w(8919,
  f'<p>{A("/brand/reima/", "Reima")} Telmin Junior sunt {A("/categorie/unisex-incaltaminte-adidasi/", "teniși unisex")} negri, ușori și flexibili, din material sintetic și textil, cu talpă din cauciuc reciclat. Magazinul îi recomandă pentru sezoanele de tranziție.</p>'
  '<p>Branțurile Happy Fit au imprimat un ghid de mărime, așa că verifici direct pe ele cât loc mai are piciorul. Închiderea cu scai și benzile elastice se ajustează repede.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Contrefort', 'ușor întărit.'), ('Compoziție', 'fără fluorocarburi și PVC, formulă vegană.'), ('Talpă', 'flexibilă, din cauciuc reciclat.'))
  + '<p>Numerele 28-40 îi fac potriviți pentru copii de la 4 ani în sus, aproximativ.</p>',
  [('model', 'Reima Telmin Junior sneakers copii negru 5400176A'), ('ușor, flexibil', 'Construcția lor ușoară și flexibilă'), ('tranziție', 'sezoanele de tranziție'),
   ('material', '50% Material sintetic, 50% Material textil'), ('talpă', 'Talpa flexibilă din cauciuc reciclat'),
   ('Happy Fit', 'Branțurile Happy Fit cu imprimeu facilitează alegerea precisă a mărimii corecte'), ('închidere', 'Închiderea ușoară cu scai și benzile elastice'),
   ('contrefort', 'Contrefortul ușor întărit'), ('fără PVC', 'Fără fluorocarburi și PVC'), ('vegan', 'Formula vegană')],
  {'Model': 'Reima Telmin Junior', 'Material': 'sintetic și textil, talpă din cauciuc reciclat', 'Caracteristici': 'scai și benzi elastice, branț Happy Fit cu ghid de mărime, vegan', 'Cod produs': '5400176A'})

w(8921,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KB0KB10532 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "vestă ușor izolată pentru băieți")}, bleumarin, din țesătură rezistentă de poliester, cu umplutură sintetică ușoară și căptușeală completă. E pentru zilele mai reci, purtată peste un hanorac sau sub o geacă.</p>'
  '<p>Croiala e regulară, cu lungime până la șolduri, iar gulerul ridicat acoperă gâtul.</p>'
  '<p>Detaliile vestei:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale.'), ('Logo', 'al mărcii, la vedere.'), ('Material', '100% poliester.'))
  + '<p>Mărimile de pe site, 128-176, sunt pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'Vestă pentru copii albastră KB0KB10532'), ('ușor izolat', 'propunere ușor izolată termic'), ('umplutură', 'Umplutura sintetică ușoară'),
   ('rezistent', 'Confecționată din țesătură rezistentă'), ('căptușeală', 'Căptușeala completă'), ('zile reci', 'zilele mai reci'), ('croială', 'Croiala regulară'),
   ('lungime', 'Lungimea până la șolduri'), ('guler', 'Gulerul ridicat'), ('fermoar', 'Închiderea cu fermoar pe toată lungimea'), ('buzunare', 'Buzunarele laterale practice'),
   ('logo', 'logo-ul distinctiv al mărcii'), ('material', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KB0KB10532', 'Material': '100% poliester, umplutură sintetică', 'Caracteristici': 'vestă ușor izolată, căptușeală completă, guler ridicat, fermoar', 'Cod produs': 'KB0KB10532'})
print('lot 10 scris')
