import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')

w(13368,
  f'<p>Geaca {A("/brand/tinycottons/", "Tinycottons")} COLOR BLOCK POLAR SHERPA HOODIE bleumarin este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} subțire, din fleece, cu croială lejeră, oversize, pentru sezonul de tranziție. Are glugă și căptușeală și se închide cu cleme.</p>'
  '<p>Buzunarele sunt oblice, iar mânecile se termină cu manșetă. Fleece-ul e subțire, iar croiala oversize lasă loc de mișcare la joacă.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '100% poliester (fleece).'), ('Căptușeală', '100% poliester.'), ('Închidere', 'cleme.'), ('Glugă', 'da.'))
  + '<p>Mărimile 92-152 acoperă copii de aproximativ 2-12 ani.</p>',
  [('model', 'Tinycottons Geacă copii COLOR BLOCK POLAR SHERPA HOODIE culoarea bleumarin, AW25-362'), ('fleece', 'Model subțire confecționat din material fleece'),
   ('oversize', 'Fit: oversize'), ('lejer', 'Tăiere lejeră, fără blocare'), ('tranziție', 'Izolare: tranzitional'), ('glugă', 'Model cu gluga'),
   ('căptușeală', 'Captuseala: cu captuseala'), ('cleme', 'Incheiere cu cleme'), ('buzunare', 'Buzunare oblice'), ('manșetă', 'Finisaj din manseta'),
   ('material', 'Material de bază: 100% Poliester')],
  {'Model': 'Tinycottons COLOR BLOCK POLAR SHERPA HOODIE', 'Material': '100% poliester (fleece)', 'Caracteristici': 'glugă, cleme, oversize', 'Cod produs': 'AW25-362'})

w(13373,
  f'<p>Ghetele chelsea {A("/brand/primigi/", "Primigi")} PNDGT 23771 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} multicolore, cu model leopard, din piele întoarsă moale, cu membrană GORE-TEX care ține picioarele uscate și le lasă să respire. Urcă peste gleznă și apără de frig în sezoanele de tranziție.</p>'
  '<p>Se închid cu fermoar, iar talpa groasă din cauciuc izolează de sol și ține bine.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textilă, ține de cald.'), ('Branțuri', 'textile, detașabile.'), ('Primigi × SIPeP', 'susține anatomia piciorului.'))
  + '<p>Numerele 31-35 se potrivesc fetelor de cam 6-11 ani.</p>',
  [('model', 'Primigi Ghete scurte pentru copii din piele întoarsă multicolor PNDGT 23771'), ('chelsea', 'Modelul de botine chelsea'), ('leopard', 'Modelul leopard în culori multiple'),
   ('piele', 'Partea superioară din piele întoarsă oferă încălțămintei un aspect elegant și o senzație moale la atingere'), ('GORE-TEX', 'Membrană GORE-TEX® ajută la menținerea picioarelor uscate'),
   ('gleznă', 'Înălțimea deasupra gleznei ajută la stabilizarea piciorului și protejează împotriva frigului'), ('fermoar', 'Închiderea cu fermoar'),
   ('talpă', 'Talpa groasă din cauciuc ajută la izolarea de sol și la aderență'), ('căptușeală', 'Interiorul căptușit ajută la menținerea căldurii'),
   ('branț', 'Branțurile textile detașabile'), ('SIPeP', 'Tehnologia Primigi × SIPeP susține dezvoltarea corectă și anatomia piciorului copilului')],
  {'Model': 'Primigi PNDGT 23771 (chelsea)', 'Material': 'piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX, fermoar, model leopard', 'Cod produs': 'PNDGT 23771'})

w(13383,
  f'<p>Geaca de blugi {A("/brand/guess/", "GUESS")} J6GL03 albastră este o {A("/categorie/geci-jachete/", "geacă pentru fete")} din bumbac 100%, cu efect prespălat și model floral, fără vatelină și fără căptușeală, pentru zilele mai calde de primăvară, vară și toamnă. Croiala relaxed fit lasă loc de mișcare.</p>'
  '<p>Se închide cu nasturi, iar manșetele au tot nasturi, ca mânecile să se poată regla. Nu are glugă.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Buzunare', 'la piept și laterale.'), ('Lungime', 'până la șolduri.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 122-125 până la 167 sunt pentru fete de aproximativ 7-14 ani.</p>',
  [('model', 'Guess Jachetă pentru copii din denim albastră J6GL03 D4EU0'), ('bumbac', 'Confecționarea din bumbac 100%'), ('prespălat', 'Materialul cu efect prespălat'),
   ('floral', 'Modelul floral'), ('căptușeală', 'Lipsa vatelinii și a căptușelii'), ('sezon', 'ținutele tinerești de primăvară, vară și toamnă'),
   ('croială', 'Croiala lejeră (relaxed fit)'), ('nasturi', 'Închiderea cu nasturi'), ('manșete', 'Manșetele cu nasturi permit ajustarea mânecilor'),
   ('glugă', 'Lipsa glugii'), ('buzunare', 'Buzunarele practice de la piept și buzunarele laterale inserate'), ('lungime', 'Lungimea până la șolduri'), ('material', '100% Bumbac')],
  {'Model': 'GUESS J6GL03', 'Material': '100% bumbac (denim)', 'Caracteristici': 'efect prespălat, model floral, nasturi', 'Cod produs': 'J6GL03 D4EU0'})

w(13384,
  f'<p>Și în roz, cizmele {A("/brand/biomecanics/", "Biomecanics")} 261257 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} de iarnă cu carâmb înalt din imitație de piele și textil, căptușite cu pluș moale. Membrana BioTEX nu lasă apa să treacă și elimină transpirația.</p>'
  '<p>Talpa groasă din cauciuc, cu bandă de rulare, ține bine pe suprafețele de iarnă. Aricii fac încălțatul ușor pentru fetițe.</p>'
  '<p>Construcția, pe puncte:</p>'
  + L(('Vârf', 'rigidizat.'), ('Călcâi și guler', 'întărite.'), ('Podology Partnership', 'lucrat cu podologi.'))
  + '<p>Mărimile 24-34 sunt pentru 2-11 ani, cu aproximație.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii roz 261257'), ('carâmb', 'Carâmbul înalt din imitație de piele și materiale textile'),
   ('pluș', 'Căptușeala interioară din pluș moale'), ('BioTEX', 'Membrana BioTEX formează o barieră împotriva apei din exterior, eliminând în același timp umiditatea din interior'),
   ('talpă', 'Talpa groasă de cauciuc cu bandă de rulare asigură aderență pe suprafețele de iarnă'), ('arici', 'Fixarea cu arici facilitează încălțarea și descălțarea rapidă de către copii'),
   ('întărit', 'Călcâiul întărit, vârful rigidizat și gulerul superior'), ('Podology', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261257', 'Material': 'imitație de piele și textil, căptușeală din pluș, talpă din cauciuc', 'Caracteristici': 'BioTEX, arici, căptușeală de pluș', 'Cod produs': '261257'})

w(13398,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} LVCKTJM01G neagră este o {A("/categorie/geci-jachete/", "geacă pentru fete")} matlasată, cu izolație sintetică medie, pentru zilele reci, cu croială lejeră care lasă loc pentru straturi. Gulerul ridicat apără gâtul de vânt.</p>'
  '<p>Închiderea dublă, cu fermoar și capse, ține aerul rece afară. Nu are glugă, deci se poartă bine cu fular și căciulă.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'completă.'), ('Buzunare', 'laterale.'), ('Mâneci', 'cu umeri coborâți.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-170 sunt pentru fete de cam 8-15 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă petrecută pentru copii neagră LVCKTJM01G'), ('matlasat', 'Geaca matlasată neagră'), ('izolație', 'Izolație sintetică medie'),
   ('croială', 'Croială lejeră – permite libertatea de mișcare, facilitând purtarea straturilor suplimentare'), ('guler', 'Guler ridicat – oferă protecție suplimentară gâtului împotriva vântului'),
   ('închidere', 'Închidere dublă – cu fermoar și capse'), ('glugă', 'Fără glugă – contribuie la un design minimalist, facilitând stilizarea cu eșarfe și căciuli'),
   ('căptușeală', 'Căptușeală completă'), ('buzunare', 'Buzunare laterale practice'), ('mâneci', 'Mâneci cu linia umerilor coborâtă'), ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans LVCKTJM01G', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, fermoar și capse, guler ridicat', 'Cod produs': 'LVCKTJM01G'})

w(13399,
  f'<p>Geaca din denim {A("/brand/kenzo-kids/", "Kenzo Kids")} K60631 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} în culoarea albastru, din denim de bumbac 100%, cu material ornamentat, neizolată și fără căptușeală. Are guler, se închide cu nasturi și nu are glugă.</p>'
  '<p>Pe piept sunt două buzunare cu nasturi, iar manșetele se încheie și ele. Croiala e simplă și dreaptă, iar denimul de bumbac are un model ornamentat.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '100% bumbac (denim).'), ('Croială', 'simplă, dreaptă.'), ('Buzunare', 'două, la piept.'))
  + '<p>Mărimile 114-150 sunt pentru copii de aproximativ 6-12 ani.</p>',
  [('model', 'Kenzo Kids Geacă din denim pentru copii K60631'), ('culoare', 'Culoare albastru'), ('denim', 'Model neizolat confecționat din denim de bumbac'),
   ('ornamentat', 'Material ornamentat'), ('necăptușit', 'Captuseala: necaptusit'), ('guler', 'Model cu guler'), ('nasturi', 'Închiderea convenabilă cu buton'),
   ('glugă', 'Gluga: fara gluga'), ('buzunare', 'Două buzunare la piept cu nasturi'), ('manșete', 'Maneci cu mansete incheiate'), ('material', '100% Bumbac'),
   ('croială', 'Tăiere simplă, fără blocare')],
  {'Model': 'Kenzo Kids K60631', 'Material': '100% bumbac (denim)', 'Caracteristici': 'nasturi, guler, buzunare la piept', 'Cod produs': 'K60631'})

w(13400,
  f'<p>{GEOX} IUPIDOO x Looney Tunes roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} pentru cei mai mici, cu personaje Looney Tunes, din material sintetic, ușori și confortabili, pentru purtarea zilnică. Au profil jos și se închid cu scai, deci copilul se încalță repede.</p>'
  '<p>Vârful e rotund, iar interiorul e confortabil. Pagina magazinului dă puține detalii despre construcție.</p>'
  '<p>Ce știm despre pereche:</p>'
  + L(('Exterior', 'material sintetic.'), ('Închidere', 'scai.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 18-26 se potrivesc fetițelor de aproximativ 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii IUPIDOO x Looney Tunes culoarea roz, B6558B.011BC'), ('sintetic', 'confecționat din material sintetic'), ('ușor', 'Model ușor și confortabil'),
   ('zilnic', 'ideal pentru purtarea zilnică'), ('profil', 'Înălțime: mic de statură'), ('scai', 'Fixare: cu scai'), ('vârf', 'Varf rotund'), ('interior', 'Interior confortabil'), TALPA],
  {'Model': 'Geox IUPIDOO x Looney Tunes', 'Material': 'sintetic, talpă din cauciuc', 'Caracteristici': 'scai, licență Looney Tunes', 'Cod produs': 'B6558B.011BC'},
  notes=['Pagina magazinului are puține detalii (fără Geox Respira sau materialul interiorului); am scris doar ce apare.'])

w(13403,
  f'<p>Tricoul polo {TH} KB0KB09103 alb este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "tricou pentru băieți")} uni, cu mânecă scurtă și guler, din bumbac 100%, cu țesătură subțire, ușor elastică. Se închide cu nasturi pe o porțiune scurtă, la gât.</p>'
  '<p>Croiala e simplă și dreaptă, iar bumbacul subțire și ușor elastic se mișcă odată cu corpul. Modelul e uni, cu decolteu cu guler.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Mânecă', 'scurtă.'), ('Guler', 'polo, cu nasturi.'))
  + '<p>Mărimile 128-176 sunt pentru băieți de aproximativ 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger alb KB0KB09103'), ('polo', 'Tricou polo copii'), ('uni', 'Model: uni'), ('mânecă', 'Maneca scurta'), ('guler', 'Model cu guler'),
   ('bumbac', '100% Bumbac'), ('țesătură', 'tesatura subtire, usor elastica'), ('nasturi', 'Incheiere scurta cu nasturi'), ('croială', 'Tăiere simplă, fără blocare')],
  {'Model': 'Tommy Hilfiger KB0KB09103 (polo)', 'Material': '100% bumbac', 'Caracteristici': 'guler polo, nasturi, mânecă scurtă', 'Cod produs': 'KB0KB09103'})

w(13443,
  f'<p>Botinele {TH} T1A5-35191 bej sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} din piele întoarsă naturală, cu finisaj neted, fără izolație, pentru zilele mai calde ale sezonului de tranziție. Acoperă glezna și o țin stabilă la joacă.</p>'
  '<p>Aricii și fermoarul fac încălțatul și descălțatul rapid. Vârful rigidizat apără degetele, iar călcâiul întărit ține piciorul pe loc.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil și piele întoarsă.'), ('Branț', 'textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-29 se potrivesc fetițelor de cam 2-5 ani.</p>',
  [('model', 'Tommy Hilfiger Botine pentru copii din piele întoarsă bej T1A5-35191'), ('piele', 'Confecționarea din piele întoarsă naturală'), ('neted', 'Finisajul neted al pielii întoarse'),
   ('izolație', 'Lipsa izolației interioare face ca botinele să fie potrivite pentru zilele mai calde ale sezonului de tranziție'), ('gleznă', 'Modelul care acoperă glezna susține stabilizarea piciorului'),
   ('închidere', 'Combinația de închidere cu arici și fermoar'), ('vârf', 'Vârful rigidizat contribuie la protecția degetelor'), ('călcâi', 'Călcâiul întărit'),
   ('interior', 'Material textil, Piele întoarsă'), ('branț', 'Branțul textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Tommy Hilfiger T1A5-35191', 'Material': 'piele întoarsă naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici și fermoar, fără izolație', 'Cod produs': 'T1A5-35191'})

w(13453,
  f'<p>Cizmele de iarnă {GEOX} OMAR WPF roz sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} izolate și impermeabile, din material textil, piele întoarsă și piele naturală, pentru cele mai mici. Partea de sus ridicată sprijină glezna pe teren denivelat, iar velcro-ul face încălțatul rapid.</p>'
  '<p>Vârful rotund e întărit, iar contrafortul rigid ține călcâiul. Magazinul precizează că nu garantează impermeabilitatea completă.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 20-23 se potrivesc fetițelor de aproximativ 1-3 ani.</p>',
  [('model', 'Geox Cizme de iarna pentru copii OMAR WPF culoarea roz, B462LC.022FU'), ('izolat', 'Model izolat'), ('impermeabil', 'Model impermeabil'),
   ('material', 'combinație de material textil, piele întoarsă și piele naturală'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('vârf', 'vârf rotund, intarita'), ('călcâi', 'Contorul de călcâi rigid'),
   ('apă', 'nu garantează impermeabilitatea completă'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), TALPA],
  {'Model': 'Geox OMAR WPF', 'Material': 'textil, piele întoarsă și piele naturală, interior textil', 'Caracteristici': 'izolate, impermeabile, velcro, Geox Respira', 'Cod produs': 'B462LC.022FU'})
