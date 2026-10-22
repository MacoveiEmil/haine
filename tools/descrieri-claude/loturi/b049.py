import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
KS = A('/brand/konges-slojd/', 'Konges Sløjd')

w(10903,
  f'<p>{GEOX} MACCHIA B164PC sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} roz, din piele întoarsă, cu interior și branț din piele naturală. Talpa patentată Geox Respira™ scoate umezeala, iar sistemele Softly Cushioned și Flexy fac talpa moale și flexibilă.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, chiar de către copil, iar banda se strânge după piciorul lui.</p>'
  '<p>Pe scurt:</p>'
  + L(('Partea de sus', 'piele întoarsă.'), ('Interior și branț', 'piele naturală.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 18-26 se potrivesc copiilor de 1-4 ani, de obicei.</p>',
  [('model', 'Geox Încălțăminte pentru copii din piele întoarsă MACCHIA roz B164PC.0BSNF'), ('piele întoarsă', 'Partea superioară din piele întoarsă'),
   ('interior', 'Interior din piele naturală'), ('branț', 'Branț din piele naturală'), ('Respira', 'Tehnologia GEOX Respira™ cu talpă patentată favorizează eliminarea umezelii'),
   ('Softly', 'Sistemul soflty cushioned'), ('Flexy', 'Flexy system susține flexibilitatea tălpii'),
   ('arici', 'Închidere cu arici facilitează încălțarea și descălțarea rapidă a încălțămintei de către copil'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox MACCHIA', 'Material': 'piele întoarsă, interior și branț din piele naturală, talpă din cauciuc', 'Caracteristici': 'arici, Geox Respira™, Softly Cushioned, Flexy', 'Cod produs': 'B164PC.0BSNF'})

w(10905,
  f'<p>{KS} JAZZ TEDDY JACKET KS104861 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă din fleece unisex")}, bej, neizolată și necăptușită, cu broderie decorativă. E un strat moale, de purtat pe vreme blândă sau sub o geacă mai groasă.</p>'.replace(' sau sub o geacă mai groasă', '')
  + '<p>Croiala e simplă, dreaptă, iar mânecile raglan lasă brațele să se miște liber. Se închide cu fermoar și nu are glugă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', 'fleece, 100% poliester.'), ('Închidere', 'fermoar.'), ('Detalii', 'broderie decorativă.'))
  + '<p>Mărimile 74 până la 134-140 sunt pentru copii de la aproximativ 9 luni la 10 ani.</p>',
  [('model', 'Konges Sløjd Geacă copii JAZZ TEDDY JACKET GRS culoarea bej, KS104861'), ('fleece', 'Model neizolat confecționat din material fleece'), ('necăptușit', 'Captuseala: necaptusit'),
   ('broderie', 'Broderie decorativă'), ('croială', 'Tăiere simplă, fără blocare'), ('raglan', 'Mânecile raglan'), ('fermoar', 'Incheiere cu fermoar'), ('fără glugă', 'Gluga: fara gluga'),
   ('material', '100% Poliester')],
  {'Model': 'Konges Sløjd JAZZ TEDDY JACKET', 'Material': '100% poliester (fleece)', 'Caracteristici': 'neizolată, necăptușită, mâneci raglan, fermoar', 'Cod produs': 'KS104861'})

w(10913,
  f'<p>Ghetele de iarnă {A("/brand/primigi/", "Primigi")} PSNGT 23500 sunt {A("/categorie/ghete-cizme/", "ghete înalte pentru fete")}, roz, din piele întoarsă și material textil, cu membrana GORE-TEX® contra umezelii și vântului. Partea de sus înaltă ține frigul afară la jocurile de iarnă.</p>'
  '<p>Aricii permit încălțatul și descălțatul ușor, iar călcâiul întărit ține piciorul stabil pe zăpadă.</p>'
  '<p>Talpa și tehnologiile:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Shock Absorber', 'tehnologie care preia șocurile.'), ('Primigi × SIPeP', 'ține cont de anatomia piciorului.'))
  + '<p>Numerele 25-29 sunt pentru copii de 2-5 ani, cu aproximație.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii roz PSNGT 23500'), ('înalt', 'încălțăminte înaltă pentru copii'), ('material', 'Piele întoarsă, Material textil'),
   ('GORE-TEX', 'Membrana GORE-TEX® oferă protecție împotriva umezelii și vântului'), ('frig', 'contribuie la protecția împotriva frigului'), ('iarnă', 'jocurilor de iarnă'),
   ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea ușoară'), ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpă plată din cauciuc'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă ajută la absorbția șocurilor'), ('SIPeP', 'Construcția Primigi × SIPeP ține cont de anatomia piciorului copilului')],
  {'Model': 'Primigi PSNGT 23500', 'Material': 'piele întoarsă și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber', 'Cod produs': 'PSNGT 23500'})

w(10915,
  f'<p>Geaca de blugi {A("/brand/hugo/", "HUGO")} G01053 este o {A("/categorie/geci-jachete/", "geacă de blugi pentru fete")}, albastră, din denim de bumbac 100%, neizolată și fără căptușeală. Se poartă în sezonul de tranziție, când e nevoie doar de un strat subțire.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile au manșete care se încheie, deci se strâng pe încheietura unui copil mai slab. Nu are glugă.</p>'
  '<p>Pe scurt, despre geacă:</p>'
  + L(('Închidere', 'nasturi.'), ('Material', '100% bumbac (denim).'), ('Căptușeală', 'nu are.'))
  + '<p>Mărimile 114-150 sunt pentru copii de în jur de 6-12 ani.</p>',
  [('model', 'HUGO Geacă de blugi pentru copii G01053'), ('denim', 'Model neizolat confecționat din denim'), ('material', '100% Bumbac'),
   ('necăptușit', 'Model neizolat fara captuseala'), ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Maneci cu mansete incheiate'),
   ('fără glugă', 'Gluga: fara gluga'), ('nasturi', 'Închiderea convenabilă cu buton'), ('culoare', 'albastru')],
  {'Model': 'HUGO G01053', 'Material': '100% bumbac (denim)', 'Caracteristici': 'neizolată, necăptușită, nasturi', 'Cod produs': 'G01053'})

w(10940,
  f'<p>Blugii {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} BARREL KB0KB10461 sunt {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "blugi barrel pentru băieți")}, negri, cu efect prespălat, din bumbac și lyocell, neelastici. Croiala barrel leg e lejeră, rotunjită pe picior, cu aspect modern.</p>'
  '<p>Talia e înaltă și stă stabil la joacă, iar fermoarul cu nasture se închide ușor, chiar și de către copil.</p>'
  '<p>Pe scurt:</p>'
  + L(('Buzunare', 'oblice, în față și în spate.'), ('Material', '75% bumbac, 25% lyocell.'), ('Finisaj', 'prespălat.'))
  + '<p>Mărimile 128-176 sunt pentru copii de 8-16 ani, de regulă.</p>',
  [('model', 'Tommy Hilfiger Blugi barrel pentru copii BARREL negri KB0KB10461'), ('barrel', 'Croiala lejeră barrel leg'), ('prespălat', 'Finisaj cu efect prespălat'),
   ('material', '75% Bumbac, 25% Lyocell'), ('neelastic', 'materialul neelastic'), ('talie', 'Talie înaltă asigură o poziție stabilă'),
   ('închidere', 'Închidere cu fermoar și nasture facilitează îmbrăcarea independentă'), ('buzunare', 'Buzunare oblice în față și în spate')],
  {'Model': 'Tommy Hilfiger BARREL', 'Material': '75% bumbac, 25% lyocell', 'Caracteristici': 'barrel leg, talie înaltă, prespălați', 'Cod produs': 'KB0KB10461'})

w(10943,
  f'<p>{A("/brand/reima/", "Reima")} Proxima 5100099B sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni de schi unisex")}, roz, pentru sporturi de iarnă, cu impermeabilitate de 10 000 mm și cusături sudate care opresc vântul și umezeala. Materialul rezistă și la murdărie.</p>'
  '<p>Bretelele se detașează și sunt reglabile, deci pantalonii se potrivesc pe un copil slab și stau sus în zăpadă. Croiala e simplă, dreaptă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Respirabilitate', '7 000 g/m2/24h.'), ('Material', '100% poliester reciclat, Bluesign®.'), ('Finisaj', 'BIONIC-FINISH® ECO.'))
  + '<p>Mărimile 92-164 se potrivesc copiilor de 2-14 ani, în general.</p>',
  [('model', 'Reima Proxima roz 5100099B'), ('schi', 'Pantaloni de schi copii'), ('iarnă', 'Tip de activitate: Sporturi de iarnă'), ('impermeabil', 'Impermeabilitate: 10 000 mm/m2/24h'),
   ('cusături', 'Cusăturile sudate etanșează și împiedică pătrunderea vântului și a umezelii'), ('murdărie', 'rezistent la umezeala si murdarie'),
   ('bretele', 'Model cu bretele detasabile'), ('reglabil', 'Caracter: reglabil'), ('croială', 'Tăiere simplă, fără blocare'), ('fermoar', 'Inchidere si fixare cu fermoar'),
   ('respirabilitate', 'Respirabilitate: 7 000 g/m2/24h'), ('reciclat', '100% Poliester reciclat'), ('Bluesign', 'Model certificat Bluesign® Standard'), ('BIONIC', 'BIONIC-FINISH® ECO')],
  {'Model': 'Reima Proxima', 'Material': '100% poliester reciclat; căptușeală poliester', 'Caracteristici': '10 000 mm, cusături sudate, bretele detașabile, Bluesign®', 'Cod produs': '5100099B'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(10947,
  f'<p>{GEOX} CIUFCIUF Looney Tunes B665QA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, cu logo și licență, din piele întoarsă, material textil și sintetic. Membrana microporoasă Geox Respira™ din talpă scoate umezeala și ține apa afară.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, de către copil, iar branțurile textile se scot, pentru curățat sau verificat mărimea.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'plată, din spumă, ușoară.'), ('Călcâi', 'ușor întărit.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Numerele 20-27 sunt pentru cei mici de aproximativ 1-4 ani.</p>',
  [('model', 'Geox CIUFCIUF Looney Tunes sneakers pentru copii roz B665QA.05422'), ('logo', 'Model cu logo și licență'), ('material', 'Piele întoarsă, Material textil, Material sintetic'),
   ('Respira', 'Tehnologia GEOX Respira™'), ('membrană', 'Membrana microporoasă din talpă protejează interiorul pantofului împotriva pătrunderii apei'),
   ('umezeală', 'membranei din talpă, care elimină umezeala'), ('arici', 'Închidere practică cu arici permite încălțarea și descălțarea rapidă și ușoară de către copil'),
   ('branțuri', 'Branțuri detașabile din material textil'), ('talpă', 'Talpă plată din spumă asigură lejeritate'), ('călcâi', 'Călcâi ușor întărit'),
   ('interior', 'Interior căptușit cu material textil')],
  {'Model': 'Geox CIUFCIUF Looney Tunes', 'Material': 'piele întoarsă, textil și sintetic, interior textil, talpă din spumă', 'Caracteristici': 'arici, branțuri detașabile, Geox Respira™', 'Cod produs': 'B665QA.05422'},
  notes=['Magazinul scrie „licență Disney” la un model Looney Tunes; am scris doar „licență”.'])

w(10955,
  f'<p>{A("/brand/ea7-emporio-armani/", "EA7 Emporio Armani")} 7B000113 AF14794 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de schi pentru băieți")}, albastră, izolată, impermeabilă (15000 mm), rezistentă la vânt, pentru sporturi de iarnă. Materialul se întinde în patru direcții, deci nu încurcă mișcarea pe pârtie.</p>'
  '<p>Spatele e mai lung și acoperă când copilul se apleacă, iar centura de zăpadă din interior oprește zăpada să intre sub geacă, chiar și la căzătură. Marginile mânecilor se reglează cu Velcro.</p>'
  '<p>Pentru pârtie, geaca are:</p>'
  + L(('Buzunar ski-pass', 'pe mânecă.'), ('Buzunar interior', 'din plasă, pentru ochelari.'), ('Guler și glugă', 'guler ridicat, glugă fixă.'), ('Fermoare', 'impermeabile.'))
  + '<p>Mărimile 142-176 sunt pentru copii de în jur de 10-16 ani.</p>',
  [('model', 'EA7 Emporio Armani Geacă de schi pentru copii 7B000113 AF14794'), ('izolat', 'Model izolat'), ('impermeabil', 'Impermeabilitate: 15000 mm/m2/24h'),
   ('vânt', 'Model respirabil, rezistent la vant si impermeabil'), ('iarnă', 'Tip de activitate: Sporturi de iarnă'), ('4 direcții', 'Utilizarea soluției de întindere în 4 direcții'),
   ('spate', 'Spatele mai lung oferă acoperire atunci când vă mișcați'), ('centură', 'o centură de zăpadă încorporată'), ('cădere', 'chiar și în caz de cădere'),
   ('velcro', 'Marginile inferioare ale mânecilor sunt reglabile cu Velcro'), ('ski-pass', 'Buzunar ski-pass pe maneca'),
   ('ochelari', 'Buzunar interior din plasă pentru ochelari de protecție'), ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('fermoare', 'Fermoare impermeabile'), ('culoare', 'albastru')],
  {'Model': 'EA7 Emporio Armani 7B000113', 'Material': 'poliester, poliuretan, poliamidă cu elastan', 'Caracteristici': 'geacă de schi, 15000 mm, centură de zăpadă, buzunar ski-pass', 'Cod produs': '7B000113 AF14794'},
  notes=['Magazinul precizează că „impermeabil” nu garantează impermeabilitatea completă.'])

w(10958,
  f'<p>{KS} LUC OVERALLS GOTS KS104956 este o {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopetă cu bretele unisex")}, albastră, cu imprimeu, din bumbac organic certificat GOTS, în stil casual. Se poartă peste un body sau un tricou.</p>'
  '<p>Croiala e simplă, dreaptă, iar bretelele țin salopeta pe umeri. Se închide cu nasturi, care se desfac ușor când copilul trebuie schimbat.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunar', 'în față.'), ('Material', '100% bumbac organic.'))
  + '<p>Mărimile 74-116 sunt pentru copii mici, de cam 9 luni până la 6 ani.</p>',
  [('model', 'Konges Sløjd Salopetă copii LUC OVERALLS GOTS cu imprimeu, KS104956'), ('organic', 'bumbac organic certificat'), ('material', '100% Bumbac organic'),
   ('casual', 'Ocazie: casual'), ('croială', 'Tăiere simplă, fără blocare'), ('bretele', 'Model cu bretele'), ('nasturi', 'Incheiere cu nasturi'), ('buzunar', 'Buzunar alunecat în față'),
   ('culoare', 'albastru')],
  {'Model': 'Konges Sløjd LUC OVERALLS', 'Material': '100% bumbac organic (GOTS)', 'Caracteristici': 'bretele, nasturi, imprimeu', 'Cod produs': 'KS104956'},
  notes=['„Peste un body sau un tricou” e dedus din faptul că e salopetă cu bretele.'])

w(10960,
  f'<p>{A("/brand/columbia/", "Columbia")} Helvetia 2087831 este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac polar unisex")} albastru, uni, din polar moale de poliester, care ține de cald în zilele mai reci, cu o aplicație decorativă. E făcut pentru joacă și activități în aer liber.</p>'
  '<p>Croiala e regulară, iar materialul neelastic își păstrează forma. Benzile elastice de la manșete și bază strâng hanoracul pe corp, iar decolteul cu închidere se deschide când copilul se încălzește.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', '100% poliester, polar.'), ('Căptușeală', 'nu are.'), ('Decolteu', 'cu închidere.'))
  + '<p>Mărimile 104-164 sunt pentru copii de 4-14 ani, aproximativ.</p>',
  [('model', 'Columbia Hanorac pentru copii din polar Helvetia albastru 2087831'), ('uni', 'Modelul uni'), ('polar', 'Confecționat din polar moale , care ajută la menținerea căldurii în zilele mai reci'),
   ('aplicație', 'Aplicația decorativă'), ('aer liber', 'diverse activități în aer liber'), ('croială', 'Croiala standard, regulară'), ('neelastic', 'Materialul cu o structură neelastică menține croiala'),
   ('benzi', 'Benzile elastice de la manșete și de la bază'), ('decolteu', 'Decolteu cu închidere permite reglarea ventilației'), ('necăptușit', 'Construcția fără căptușeală'),
   ('material', '100% Poliester')],
  {'Model': 'Columbia Helvetia', 'Material': '100% poliester (polar)', 'Caracteristici': 'polar, decolteu cu închidere, benzi elastice', 'Cod produs': '2087831'})
