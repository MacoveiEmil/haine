import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

KONGES = A('/brand/konges-slojd/', 'Konges Sløjd')
REIMA = A('/brand/reima/', 'Reima')
LIEWOOD = A('/brand/liewood/', 'Liewood')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(13584,
  f'<p>Blugii {KONGES} MAGOT FRILL PANTS sunt {A("/categorie/pantaloni-treninguri/", "pantaloni pentru fete")} în culoarea alb, cu model, din denim confortabil de bumbac organic certificat, cu fason baggy și talie înaltă. Bumbacul organic e cultivat fără îngrășăminte și pesticide.</p>'
  '<p>Talia are bandă elastică, deci se trag ușor pe corp, iar fasonul lejer lasă loc de mișcare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac organic.'), ('Talie', 'înaltă, cu elastic.'), ('Buzunare', 'oblice.'))
  + '<p>Mărimile 86 până la 134-140 se potrivesc fetelor de aproximativ 1-10 ani.</p>',
  [('model', 'Konges Sløjd Jeans copii MAGOT FRILL PANTS GOTS KS104970'), ('culoare', 'Culoare alb'), ('model print', 'Model: cu modele'), ('denim', 'Model confecționat din denim confortabil'),
   ('organic', 'bumbac organic certificat'), ('pesticide', 'fara utilizarea ingrasamintelor sau pesticidelor'), ('baggy', 'fason baggy cu talia înaltă'),
   ('elastic', 'Banda elastica in talie'), ('lejer', 'Fason lejer'), ('buzunare', 'Buzunare oblice'), ('material', '100% Bumbac organic')],
  {'Model': 'Konges Sløjd MAGOT FRILL PANTS', 'Material': '100% bumbac organic', 'Caracteristici': 'talie înaltă elastică, fason baggy', 'Cod produs': 'KS104970'})

w(13585,
  f'<p>Cizmele de zăpadă {LIEWOOD} Albi Pile Boot bleumarin sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} de iarnă, cu interior căptușit care ține de cald, din material textil, cu un motiv animal print. Sunt gândite pentru joaca de iarnă și ieșirile afară.</p>'
  '<p>Talpa din cauciuc ține bine pe suprafețe alunecoase, iar călcâiul întărit sprijină piciorul. Gulerul moale nu irită glezna.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Vârf', 'rotund, lasă degetele libere.'), ('Interior', 'textil, căptușit.'), ('Partea de sus', 'material textil.'))
  + '<p>Gama 22-35 acoperă copii de aproximativ 1-11 ani.</p>',
  [('model', 'Liewood Cizme de zăpadă pentru copii Albi Pile Boot bleumarin LW20855'), ('căptușit', 'Interior căptușit ajută la menținerea căldurii'),
   ('textil', 'Partea superioară din material textil'), ('animal', 'Motiv cu animal print'), ('iarnă', 'jocurile de iarnă și activitățile cotidiene în aer liber'),
   ('talpă', 'Talpă din cauciuc asigură o aderență bună pe suprafețe alunecoase și de iarnă'), ('călcâi', 'Călcâi întărit contribuie la stabilizarea piciorului'),
   ('guler', 'Gulerul moale al părții superioare asigură confort în jurul gleznei, fără a provoca iritații'), ('vârf', 'Vârf rotund permite libertatea de mișcare a degetelor')],
  {'Model': 'Liewood Albi Pile Boot', 'Material': 'textil, interior căptușit, talpă din cauciuc', 'Caracteristici': 'cizme de zăpadă, guler moale, animal print', 'Cod produs': 'LW20855'})

w(13591,
  f'<p>Hanoracul cu fermoar {REIMA} Turina albastru este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} din polar moale de grosime medie, care se usucă repede, cu model abstract și logo aplicat. Fermoarul merge pe toată lungimea, iar gulerul înalt apără gâtul de frig.</p>'
  '<p>Croiala lejeră și materialul elastic lasă loc de mișcare, iar bordurile elastice de la bază și manșete țin căldura.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'laterale și pe piept, unul cu fermoar.'), ('Față', '100% poliester.'), ('Spate', '92% poliester, 8% elastan.'))
  + '<p>Mărimile 104-164 sunt pentru copii de aproximativ 4-14 ani.</p>',
  [('model', 'Reima Hanorac cu fermoar pentru copii din polar Turina albastru 5200503A'), ('polar', 'Material moale din polar'), ('grosime', 'Grosimea medie a materialului'),
   ('uscare', 'Material cu uscare rapidă'), ('model abstract', 'Model abstract și o aplicație cu logo Reima'), ('fermoar', 'Construcție cu fermoar pe toată lungimea'),
   ('guler', 'Guler înalt , protejează gâtul de frig'), ('croială', 'Croială lejeră , din material elastic'), ('borduri', 'Borduri elastice la bază și manșete'),
   ('buzunare', 'Buzunare practice , laterale și pe piept, inclusiv unul cu fermoar'), ('față', '100% Poliester'), ('spate', '92% Poliester, 8% Elastan')],
  {'Model': 'Reima Turina', 'Material': 'polar din poliester, spate cu elastan', 'Caracteristici': 'fermoar întreg, guler înalt, uscare rapidă', 'Cod produs': '5200503A'})

w(13595,
  f'<p>Cizmele cowboy {TH} T3A6-35194 bej sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} din piele întoarsă, fără izolație, pentru zilele mai calde ale sezonului de tranziție, în stil boho și casual. Se închid cu fermoar, iar gulerul moale nu strânge gamba.</p>'
  '<p>Vârful rigidizat apără degetele și ține forma, iar călcâiul întărit sprijină piciorul. Talpa din cauciuc ține bine pe sol.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'din piele naturală.'), ('Căptușeală', 'textilă.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 30-40 se poartă de pe la 6 ani în sus.</p>',
  [('model', 'Tommy Hilfiger Cizme cowboy pentru copii din piele întoarsă bej T3A6-35194'), ('piele', 'Partea superioară din piele întoarsă'), ('izolație', 'Lipsa izolației termice face modelul potrivit pentru zilele mai calde'),
   ('stil', 'stilul lejer boho și casual'), ('fermoar', 'Închiderea cu fermoar'), ('guler', 'Gulerul moale al părții superioare permite o potrivire confortabilă în jurul gambei, fără a strânge'),
   ('vârf', 'Vârful rigidizat susține protecția degetelor, menținând forma'), ('călcâi', 'Călcâiul întărit'), ('branț', 'Branțul din piele naturală'),
   ('căptușeală', 'Căptușeala textilă'), ('talpă', 'Talpa din cauciuc contribuie la aderența la sol')],
  {'Model': 'Tommy Hilfiger T3A6-35194 (cowboy)', 'Material': 'piele întoarsă, branț din piele, talpă din cauciuc', 'Caracteristici': 'fermoar, fără izolație', 'Cod produs': 'T3A6-35194'})

w(13596,
  f'<p>Pantalonii de trening {TH} KB0KB10654 bleumarin sunt {A("/categorie/baieti-imbracaminte-pantaloni-treninguri/", "pantaloni pentru băieți")} din tricot moale de bumbac 100%, cu imprimeu decorativ, buni pentru sport și pentru acasă. Talia regulară are bandă elastică și șnururi.</p>'
  '<p>Picioarele se termină cu manșete, care țin pantalonii pe loc, iar croiala simplă nu încurcă la joacă. Bumbacul e plăcut la atingere și lasă pielea să respire.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Buzunare', 'laterale.'), ('Talie', 'elastică, cu șnur.'))
  + '<p>Mărimile 128-176 sunt pentru băieți de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Pantaloni de trening pentru copii din bumbac bleumarin regular waist KB0KB10654'), ('tricot', 'Tricot moale din bumbac (100% bumbac), plăcut la atingere și respirabil'),
   ('imprimeu', 'Imprimeu decorativ'), ('sport', 'activități sportive, precum și pentru momentele de relaxare acasă'), ('talie', 'Talie elastică cu bandă elastică și șnururi'),
   ('manșete', 'Picioare cu manșete , ce ajută la menținerea pantalonilor în poziție'), ('croială', 'Croială simplă'), ('buzunare', 'Buzunare laterale practice'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB10654', 'Material': '100% bumbac', 'Caracteristici': 'talie elastică cu șnur, manșete, imprimeu', 'Cod produs': 'KB0KB10654'})

w(13603,
  f'<p>Geaca de blugi {A("/brand/marc-jacobs/", "MARC JACOBS")} W61010 este o {A("/categorie/geci-jachete/", "geacă pentru fete")} în culoarea albastru, din bumbac 100%, cu croială regulară și ecusoane decorative, pentru sezonul de tranziție. Nu are glugă și se închide cu nasturi.</p>'
  '<p>Buzunarele de la piept au clapă, iar lungimea până la șolduri se potrivește cu pantaloni și cu fuste. Croiala lasă loc și pentru un strat pe dedesubt.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Închidere', 'nasturi.'), ('Decor', 'ecusoane.'))
  + '<p>E disponibilă doar mărimea 156, pentru fete de aproximativ 12-13 ani.</p>',
  [('model', 'MARC JACOBS Geacă de blugi pentru copii din bumbac albastră W61010'), ('culoare', 'Culoare albastru'), ('bumbac', 'compoziția naturală a materialului favorizează respirabilitatea'),
   ('croială', 'Croială regulară – favorizează libertatea de mișcare și permite purtarea de straturi suplimentare'), ('ecusoane', 'Ecusoane decorative'),
   ('tranziție', 'sezonul de tranziție'), ('glugă', 'Fără glugă'), ('nasturi', 'Sistem de închidere cu nasturi'), ('buzunare', 'buzunarele practice cu clapă'),
   ('piept', 'Buzunare la piept'), ('lungime', 'se asortează bine cu diferite croieli de pantaloni sau fuste'), ('material', '100% Bumbac')],
  {'Model': 'MARC JACOBS W61010', 'Material': '100% bumbac (denim)', 'Caracteristici': 'nasturi, ecusoane, buzunare la piept', 'Cod produs': 'W61010'},
  varsta_txt='12-13 ani', notes=['Doar mărimea 156 e disponibilă; vârsta e estimată după înălțime.'])

w(13605,
  f'<p>Încălțămintea de iarnă {A("/brand/biomecanics/", "Biomecanics")} 261125 verde e o pereche de {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} înalte, din piele naturală, căptușite cu lână, inclusiv branțul, pentru plimbări de iarnă. Talpa flexibilă din cauciuc, groasă de 1 cm, lasă piciorul să se miște natural.</p>'
  '<p>Aricii cu curea reglabilă fac încălțatul ușor, iar vârful rotund, cauciucat, apără degetele de lovituri. Pielea naturală ține mult.</p>'
  '<p>Construcția, pe puncte:</p>'
  + L(('Stabilizator', 'lateral, cu călcâi moale.'), ('Interior', 'lână.'), ('Podology Partnership', 'tehnologia Biomecanics.'))
  + '<p>Numerele 18-25 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii din piele verde 261125'), ('înalt', 'o încălțăminte înaltă, din piele'), ('piele', 'Partea superioară din piele naturală'),
   ('lână', 'Interiorul căptușit și branțul din lână ajută la menținerea căldurii'), ('plimbări', 'plimbările de iarnă'), ('talpă', 'Talpă flexibilă din cauciuc , cu o grosime de 1 cm'),
   ('arici', 'Închidere cu arici și curea reglabilă'), ('vârf', 'Vârf rotund, cauciucat favorizează protecția degetelor împotriva loviturilor'), ('stabilizator', 'Stabilizator lateral și călcâi moale'), ('durabil', 'Partea superioară din piele naturală contribuie la durabilitate'),
   ('Podology', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261125', 'Material': 'piele naturală, căptușeală și branț din lână', 'Caracteristici': 'arici cu curea reglabilă, vârf cauciucat, lână', 'Cod produs': '261125'})

w(13615,
  f'<p>Setul de ploaie {LIEWOOD} Pedia Rainwear Set bleumarin e o {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopetă unisex")}, de fapt geacă și pantaloni, cu membrană impermeabilă de 20000 mm H2O. Gluga se detașează, iar detaliile reflectorizante îl fac pe copil vizibil seara.</p>'
  '<p>Fermoarul are bandă cu velcro contra vântului, iar sub brațe sunt orificii de aerisire. Pantalonii au talie ajustabilă și bretele din silicon pentru picioare, care țin cracii la locul lor.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Manșete', 'elastice, la geacă și pantaloni.'), ('Buzunare', 'laterale.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-128 sunt pentru copii de cam 4-8 ani.</p>',
  [('model', 'Liewood Pelerină de ploaie pentru copii Pedia Rainwear Set bleumarin LW19909'), ('membrană', 'Membrană impermeabilă cu un parametru de 20000 mm H2O'),
   ('glugă', 'Glugă detașabilă'), ('reflectorizant', 'Detalii reflectorizante pe set sporesc vizibilitatea copilului'), ('fermoar', 'Fermoar cu bandă velcro facilitează îmbrăcarea și protejează împotriva vântului'),
   ('ventilație', 'Orificii de ventilație sub brațe'), ('talie', 'Talie ajustabilă la pantaloni'), ('bretele', 'Bretele detașabile din silicon pentru picioare ajută la menținerea cracilor'),
   ('manșete', 'Manșete elastice la geacă și pantaloni'), ('buzunare', 'Buzunare laterale practice'), ('material', '100% Poliester')],
  {'Model': 'Liewood Pedia Rainwear Set', 'Material': '100% poliester', 'Caracteristici': '20000 mm H2O, glugă detașabilă, reflectorizante, geacă și pantaloni', 'Cod produs': 'LW19909'},
  notes=['Produsul e un set de ploaie (geacă și pantaloni), listat la Salopete.'])

w(13620,
  f'<p>Geaca de tranziție {KONGES} ACTY JACKET verde este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} ușoară, din nailon, pentru primăvară și vară, cu croială lejeră și mâneci raglan, în stil sport și casual. Gluga integrată apără de vânt și de ploaia ușoară.</p>'
  '<p>Se închide cu fermoar, iar tivul are șnur de strângere, care se reglează după copil.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'practice.'), ('Material', '100% nailon.'), ('Glugă', 'integrată.'))
  + '<p>Mărimile 92 până la 134-140 se potrivesc copiilor de aproximativ 2-10 ani.</p>',
  [('model', 'Konges Sløjd Geacă de tranziție pentru copii ACTY JACKET verde KS104624'), ('ușor', 'o opțiune ușoară pentru cei mici'), ('sezon', 'Ideală pentru sezonul de tranziție , primăvară și vară'),
   ('croială', 'Croiala lejeră a gecii'), ('raglan', 'Mânecile raglan'), ('stil', 'Stilul sport și casual'), ('glugă', 'Gluga integrată oferă protecție suplimentară împotriva vântului și a ploii ușoare'),
   ('fermoar', 'Închiderea cu fermoar'), ('tiv', 'Tivul cu șnur de strângere'), ('buzunare', 'Buzunarele practice'), ('material', '100% Nailon')],
  {'Model': 'Konges Sløjd ACTY JACKET', 'Material': '100% nailon', 'Caracteristici': 'glugă integrată, mâneci raglan, tiv cu șnur', 'Cod produs': 'KS104624'})

w(13642,
  f'<p>Hanoracul cu fermoar {REIMA} Tupsis roșu este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} din polar, fără căptușeală, cu model abstract și logo, bun pentru joacă afară și ieșiri în oraș. Gulerul înalt apără gâtul de frig, iar fermoarul ajută la reglarea temperaturii.</p>'
  '<p>Croiala lejeră și materialul elastic lasă loc de mișcare, iar manșetele și baza cu nervuri se așază bine pe corp.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Buzunare', 'laterale, slip-on.'), ('Față', '100% poliester.'), ('Spate', '92% poliester, 8% elastan.'))
  + '<p>Mărimile 92-164 acoperă copii de aproximativ 2-14 ani.</p>',
  [('model', 'Reima Hanorac cu fermoar pentru copii din polar Tupsis roșu 5200476A'), ('polar', 'Țesătura din polar ajută la menținerea căldurii'), ('căptușeală', 'Absența căptușelii'),
   ('model abstract', 'Modelul abstract cu logo-ul brandului Reima'), ('urban', 'de la joacă la ieșiri urbane'), ('guler', 'Gulerul înalt asigură protecția gâtului împotriva frigului'),
   ('fermoar', 'Modelul cu fermoar facilitează îmbrăcarea și dezbrăcarea, precum și reglarea temperaturii'), ('croială', 'Croiala lejeră'), ('elastic', 'Materialul elastic'),
   ('nervuri', 'Manșetele și baza hanoracului cu nervuri'), ('buzunare', 'Buzunarele laterale tip slip-on'), ('față', '100% Poliester'), ('spate', '92% Poliester, 8% Elastan')],
  {'Model': 'Reima Tupsis', 'Material': 'polar din poliester, spate cu elastan', 'Caracteristici': 'fermoar, guler înalt, fără căptușeală', 'Cod produs': '5200476A'})
