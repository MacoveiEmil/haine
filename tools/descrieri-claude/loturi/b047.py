import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(10777,
  f'<p>{PRIMIGI} PSNGT 23500 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "cizme de zăpadă pentru bebeluși")}, bej, cu motiv animal, din piele întoarsă și material textil. Membrana GORE-TEX® ține picioarele uscate, deci sunt pentru jocurile de iarnă în zăpadă.</p>'
  '<p>Aricii permit încălțatul și descălțatul ușor, iar partea de sus se potrivește flexibil pe picior. Vârful rigidizat apără degetele, iar călcâiul întărit ține piciorul stabil.</p>'
  '<p>Mai sunt câteva lucruri de știut:</p>'
  + L(('Shock Absorber', 'tehnologie în talpă care reduce șocurile.'), ('Primigi × SIPeP', 'pentru dezvoltarea corectă a piciorului.'), ('Interior', 'material textil.'))
  + '<p>Numerele 19-24 sunt pentru cei mici de 1-3 ani, de regulă.</p>',
  [('model', 'Primigi Cizme de zăpadă pentru copii bej PSNGT 23500'), ('motiv', 'Modelul cu motiv animal'), ('material', 'Partea superioară din piele întoarsă și material textil'),
   ('GORE-TEX', 'Membrana GORE-TEX® menține picioarele uscate'), ('iarnă', 'jocurilor de iarnă'), ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea ușoară'),
   ('potrivire', 'o potrivire flexibilă'), ('întărit', 'Călcâiul întărit și vârful rigidizat asigură stabilizarea piciorului și protecția degetelor'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă ajută la reducerea șocurilor'), ('SIPeP', 'Colaborarea Primigi × SIPeP susține dezvoltarea corectă a piciorului copilului'),
   ('interior', 'Material textil')],
  {'Model': 'Primigi PSNGT 23500', 'Material': 'piele întoarsă și textil, interior textil', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber', 'Cod produs': 'PSNGT 23500'})

w(10783,
  f'<p>{A("/brand/guess/", "Guess")} J6YL18 D1169 este o {A("/categorie/geci-jachete/", "geacă de blugi pentru fete")}, albastră, din denim de bumbac 100% cu efect prespălat, decorată cu pietre de paiete. Fără căptușeală, e ușoară, pentru zilele mai calde de tranziție.</p>'
  '<p>Croiala e relaxed fit, cu umerii coborâți pe mânecă, deci stă lejer și încape o bluză dedesubt. Gulerul e clasic.</p>'
  '<p>La purtat, contează și:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'în față, tip slip-on.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 122-125 până la 167 sunt pentru copii de 7-14 ani, în general.</p>',
  [('model', 'Guess Jachetă pentru copii din denim albastră J6YL18 D1169'), ('bumbac', 'Confecționată din bumbac 100%'), ('prespălat', 'Efectul prespălat al materialului'),
   ('paiete', 'Pietre de paiete decorative'), ('necăptușit', 'Lipsa căptușelii contribuie la lejeritate și respirabilitate, ideală pentru zilele mai calde'),
   ('croială', 'Croiala relaxed fit'), ('umeri', 'Mâneci cu linia umerilor coborâtă'), ('guler', 'Gulerul clasic'), ('nasturi', 'Închiderea cu nasturi'),
   ('buzunare', 'Buzunare practice tip slip-on în față')],
  {'Model': 'Guess J6YL18 D1169', 'Material': '100% bumbac (denim)', 'Caracteristici': 'prespălată, paiete, necăptușită, relaxed fit', 'Cod produs': 'J6YL18 D1169'})

w(10790,
  f'<p>{A("/brand/ea7-emporio-armani/", "EA7 Emporio Armani")} 7B000033 AF12873 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă bomber pentru băieți")}, bej, din țesătură ușoară de poliamidă, fără izolație termică, pentru anotimpurile de tranziție. Căptușeala e din bumbac.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar baza și manșetele cu nervuri elastice strâng bomberul pe corp, ca să stea aproape de corp și pe un copil mai slab.</p>'
  '<p>Pentru zi de zi, are:</p>'
  + L(('Închidere', 'fermoar.'), ('Glugă', 'nu are.'), ('Material', '100% poliamidă, căptușeală 100% bumbac.'))
  + '<p>Mărimile 110-176 sunt pentru copii de 5-16 ani, cu aproximație.</p>',
  [('model', 'EA7 Emporio Armani Geacă bomber pentru copii bej 7B000033 AF12873'), ('ușor', 'Confecționată din țesătură ușoară'), ('neizolat', 'Designul fără izolație termică'),
   ('tranziție', 'anotimpurile de tranziție'), ('căptușeală', '100% Bumbac'), ('croială', 'Croiala de tip regulară'), ('lungime', 'Lungimea până la șolduri'),
   ('nervuri', 'Baza și manșetele cu nervuri elastice'), ('fermoar', 'Închiderea cu fermoar'), ('fără glugă', 'Absența glugii'), ('material', '100% Poliamidă')],
  {'Model': 'EA7 Emporio Armani 7B000033', 'Material': '100% poliamidă; căptușeală 100% bumbac', 'Caracteristici': 'bomber, neizolată, bază și manșete cu nervuri', 'Cod produs': '7B000033 AF12873'})

w(10795,
  f'<p>{TH} KB0KB10509 este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")} albastru, uni, din bumbac pur, fără glugă și fără fermoar, cu logo brodat discret. Se îmbracă peste cap și merge la ieșirile de zi cu zi.</p>'
  '<p>Croiala e relaxed fit, cu umerii coborâți pe mânecă, deci stă lejer. Bordurile elastice de la bază, manșete și decolteu țin hanoracul în formă.</p>'
  '<p>Mai sunt câteva detalii:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'rotund, cu bordură elastică.'), ('Model', 'uni, cu logo brodat.'))
  + '<p>Mărimile 128-176 se potrivesc copiilor de 8-16 ani, de obicei.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac albastru KB0KB10509'), ('uni', 'Model uni cu logo brodat'), ('bumbac', 'Materialul din bumbac pur'),
   ('fără glugă', 'Hanoracul fără fermoar și fără glugă este un model clasic care se îmbracă peste cap'), ('urban', 'activitățile urbane și întâlnirile relaxate'),
   ('croială', 'Croiala relaxed fit'), ('umeri', 'Mâneci cu linia umerilor coborâtă'), ('borduri', 'Borduri elastice la bază și la manșete'),
   ('decolteu', 'Decolteu rotund cu bordură elastică'), ('compoziție', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB10509', 'Material': '100% bumbac', 'Caracteristici': 'fără glugă și fermoar, relaxed fit, logo brodat', 'Cod produs': 'KB0KB10509'})

w(10805,
  f'<p>{A("/brand/colmar/", "Colmar")} CAPTION 3472.2XX este o {A("/categorie/geci-jachete/", "geacă de puf pentru fete")}, bej, matlasată, umplută cu puf de rață și pene (90/10), cu rezistență sporită la apă. E pentru iarnă și frig.</p>'
  '<p>Croiala e simplă, dreaptă, deci încape un pulover dedesubt, iar mânecile se termină cu bandă elastică, care strânge la încheieturi. Nu are glugă, deci merge cu o căciulă.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Închidere', 'fermoar și capse.'), ('Căptușeală', '100% poliester.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 130-172 sunt pentru copii de 8-15 ani, aproximativ.</p>',
  [('model', 'Colmar Geacă de puf pentru copii CAPTION culoarea bej, 3472.2XX'), ('matlasat', 'Matlasare'), ('puf', '90% Puf de rata, 10% Pene de rață'),
   ('apă', 'Model cu rezistenta sporita la apa'), ('frig', 'izolare impotriva frigului'), ('croială', 'Tăiere simplă, fără blocare'),
   ('elastic', 'Mâneci finisate cu o coadă elastică'), ('fără glugă', 'Gluga: fara gluga'), ('închidere', 'Fixare cu fermoar si snap'),
   ('căptușeală', 'Captuseala: 100% Poliester'), ('material', 'Materialul de baza: 100% Poliester')],
  {'Model': 'Colmar CAPTION', 'Material': '100% poliester; umplutură 90% puf, 10% pene', 'Caracteristici': 'puf, matlasată, rezistentă la apă, fără glugă', 'Cod produs': '3472.2XX'})

w(10807,
  f'<p>{GEOX} MACCHIA B664NA sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} maro, din piele naturală și piele întoarsă, cu interior și branț detașabil din piele. Tehnologia Geox Respira™ scoate umezeala, iar sistemul Softly Cushioned preia șocurile.</p>'
  '<p>Branțul are imprimeu pentru verificarea mărimii. Vârful rotund, rigidizat, lasă degetele să se miște, iar aricii permit încălțatul fără ajutor.</p>'
  '<p>Talpa e lucrată pentru mers:</p>'
  + L(('Flexy System', 'incizii în talpă, care o lasă să se îndoaie.'), ('Talpă', 'din cauciuc.'), ('Stil', 'casual, pentru ținutele de zi cu zi.'))
  + '<p>Numerele 18-26 sunt pentru copii de 1-4 ani, cam.</p>'.replace('copii de 1-4 ani, cam.', 'copii de cam 1-4 ani.'),
  [('model', 'Geox Pantofi pentru copii din piele MACCHIA maro B664NA.03322'), ('material', 'Partea superioară din combinația de piele naturală și piele întoarsă'),
   ('interior', 'Interiorul din piele naturală'), ('branț', 'Branțul detașabil din piele naturală cu imprimeu'), ('Respira', 'Tehnologia GEOX Respira™ elimină umezeala'),
   ('Softly', 'Sistemul Softly Cushioned'), ('vârf', 'Vârful rotund, rigidizat permite libertatea de mișcare a degetelor'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă'), ('Flexy', 'Flexy System cu incizii în talpă'), ('talpă', 'Talpa din cauciuc'),
   ('casual', 'Stilul casual')],
  {'Model': 'Geox MACCHIA', 'Material': 'piele naturală și piele întoarsă, interior din piele, talpă din cauciuc', 'Caracteristici': 'arici, branț detașabil cu imprimeu, Geox Respira™, Flexy System', 'Cod produs': 'B664NA.03322'})

w(10808,
  f'<p>{TH} x Peanuts KS0KS00768 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză cu mânecă lungă pentru băieți")}, bleumarin, cu dungi și imprimeu Peanuts®, din bumbac subțire, elastic. Mâneca lungă o face potrivită pentru zilele mai reci.</p>'
  '<p>Croiala e regulară, nici mulată, nici largă, iar materialul elastic se adaptează la corp și nu încurcă la joacă. Se poartă singură sau sub un pulover.</p>'
  '<p>Pe scurt, despre bluză:</p>'
  + L(('Material', '100% bumbac, subțire.'), ('Model', 'dungi și imprimeu Peanuts®.'), ('Mâneci', 'lungi.'))
  + '<p>Mărimile 98-176 acoperă copii de 3-16 ani, în mare.</p>',
  [('model', 'Tommy Hilfiger Longsleeve pentru copii din bumbac x Peanuts bleumarin KS0KS00768'), ('Peanuts', 'Imprimeul Peanuts® și dungile'), ('subțire', 'Bumbacul subțire'),
   ('elastic', 'Materialul elastic facilitează ajustarea la siluetă'), ('reci', 'potrivit pentru zilele mai reci'), ('croială', 'Croială regulară'), ('bumbac', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger x Peanuts', 'Material': '100% bumbac', 'Caracteristici': 'mânecă lungă, dungi, imprimeu Peanuts®', 'Cod produs': 'KS0KS00768'})

w(10812,
  f'<p>{PRIMIGI} PBZGT 23527 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete de iarnă pentru bebeluși")}, bleumarin, înalte, din piele întoarsă și material textil, cu membrana GORE-TEX®, impermeabilă. Sunt pentru jocurile de iarnă și plimbările zilnice afară.</p>'
  '<p>Aricii permit încălțatul rapid și se ajustează pe picior, iar partea de sus înaltă cuprinde glezna. Călcâiul întărit ține piciorul stabil.</p>'
  '<p>Talpa și tehnologiile:</p>'
  + L(('Talpă', 'din cauciuc, cu profil plat.'), ('Shock Absorber', 'reduce șocurile la mers.'), ('Primigi × SIPeP', 'ține cont de anatomia piciorului.'))
  + '<p>Numerele 21-24 sunt pentru copii de 1-3 ani, de obicei.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii bleumarin PBZGT 23527'), ('înalt', 'Partea superioară înaltă , din piele întoarsă și material textil'),
   ('GORE-TEX', 'Membrană GORE-TEX® asigură impermeabilitatea'), ('iarnă', 'jocurilor de iarnă și al activităților zilnice în aer liber'),
   ('arici', 'Închidere cu arici facilitează încălțarea rapidă și ușoară, precum și ajustarea'), ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpă din cauciuc cu profil plat'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă ajută la reducerea șocurilor'), ('SIPeP', 'Construcția Primigi × SIPeP ține cont de anatomia piciorului copilului')],
  {'Model': 'Primigi PBZGT 23527', 'Material': 'piele întoarsă și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber', 'Cod produs': 'PBZGT 23527'})

w(10813,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261252 sunt {A("/categorie/ghete-cizme/", "ghete de iarnă pentru fete")}, violet, înalte, cu carâmb din piele întoarsă și materiale sintetice. Nu sunt impermeabile, deci sunt pentru zilele de iarnă uscate, nu pentru zăpadă udă.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, de către copil, iar vârful rigidizat și călcâiul întărit țin piciorul în poziție și apără degetele.</p>'
  '<p>Talpa e partea cea mai lucrată:</p>'
  + L(('Talpă', 'groasă, din spumă, izolează de sol.'), ('Flexi Lite', 'sistem în talpă pentru mișcare ușoară.'), ('Parteneriat', 'Biomecanics Podology.'))
  + '<p>Numerele 28-34 sunt pentru copii de 4-11 ani, aproximativ.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii violet 261252'), ('înalt', 'încălțăminte înaltă pentru copii'), ('carâmb', 'Carâmb înalt confecționat din piele întoarsă și materiale sintetice'),
   ('neimpermeabil', 'Fără impermeabilitate favorizează respirabilitatea încălțămintei în condiții uscate'), ('arici', 'Închidere cu arici facilitează încălțarea și descălțarea rapidă de către copii'),
   ('întărit', 'Vârf rigidizat și călcâi întărit contribuie la stabilizarea piciorului și la protecția degetelor'), ('talpă', 'Talpă groasă din spumă contribuie la izolarea de sol'),
   ('Flexi Lite', 'Sistemul Flexi Lite în talpă'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261252', 'Material': 'piele întoarsă și sintetic, interior textil, talpă din spumă', 'Caracteristici': 'neimpermeabile, arici, Flexi Lite', 'Cod produs': '261252'})
