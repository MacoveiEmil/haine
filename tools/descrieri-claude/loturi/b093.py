import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

BIO = A('/brand/biomecanics/', 'Biomecanics')
REIMA = A('/brand/reima/', 'Reima')
PODO = ('Podology', 'Tehnologia Biomecanics Podology Partnership susține dezvoltarea corectă a piciorului copilului')

w(13460,
  f'<p>Geaca de blugi {A("/brand/patrizia-pepe/", "Patrizia Pepe")} CA52 7O0038 este o {A("/categorie/geci-jachete/", "geacă pentru fete")} în culoarea albastru, din denim cu efect prespălat, neizolată și fără căptușeală, cu un detaliu decorativ. Se închide cu nasturi, are buzunar pe piept și nu are glugă.</p>'
  '<p>Atenție la mărime: magazinul folosește mărimile producătorului italian, care pot diferi de cele de pe etichetă, așa că merită verificat tabelul de mărimi.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', 'denim prespălat.'), ('Închidere', 'nasturi.'), ('Croială', 'simplă, dreaptă.'))
  + '<p>Mărimile 118-168 sunt pentru fete de aproximativ 6-15 ani.</p>',
  [('model', 'Patrizia Pepe Geaca de blugi pentru copii CA52 7O0038'), ('culoare', 'Culoare albastru'), ('denim', 'denim cu efect prespălat'), ('neizolat', 'Model neizolat'),
   ('necăptușit', 'Captuseala: necaptusit'), ('decor', 'Detaliu decorativ'), ('nasturi', 'Incheiere cu nasturi'), ('piept', 'Buzunar pe piept'), ('glugă', 'Gluga: fara gluga'),
   ('mărimi', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('etichetă', 'Marimea comandata poate diferi fata de cea inscriptionata pe eticheta'),
   ('croială', 'Tăiere simplă, fără blocare')],
  {'Model': 'Patrizia Pepe CA52 7O0038', 'Material': 'denim prespălat', 'Caracteristici': 'nasturi, buzunar pe piept, neizolată', 'Cod produs': 'CA52 7O0038'},
  notes=['Pagina nu dă compoziția; am scris doar „denim”.'])

w(13465,
  f'<p>Geaca de puf reversibilă {A("/brand/colmar/", "Colmar")} EXUBERANCE gri este o {A("/categorie/geci-jachete/", "geacă pentru fete")} izolată cu puf de rață și pene, din colecția Colmar Green Path, parțial din materiale reciclate. Fibra REPREVE e făcută din sticle de plastic reciclate, iar tratamentul fără PFC o face rezistentă la apă.</p>'
  '<p>Gluga e fixă, iar fermoarul urcă într-un guler înalt, cu protecție pentru bărbie.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Umplutură', '90% puf de rață, 10% pene.'), ('Material 1', '100% poliester.'), ('Material 2', '100% nailon.'))
  + '<p>Numerele 106-142 sunt pentru fete de cam 4-10 ani.</p>',
  [('model', 'Colmar Geaca de puf reversibila pentru copii EXUBERANCE culoarea gri, 3442E.2Y'), ('puf', 'Umplutura din puf si pene'), ('izolat', 'Model izolat cu captuseala'),
   ('Green Path', 'Colmar Green Path'), ('reciclat', 'realizate partial din materiale reciclate'), ('REPREVE', 'Fibra REPREVE este fabricata din sticle de plastic reciclate'),
   ('PFC', 'Modelul cu acoperire ecologica PFC Repellent cu apa libera, care asigura rezistenta la apa'), ('glugă', 'Gluga nedetasabila'),
   ('guler', 'Are inchidere cu fermoar si guler ridicat cu barbie'), ('umplutură', '90% Puf de rata, 10% Pene'), ('material 1', '100% Poliester'), ('material 2', '100% Nailon')],
  {'Model': 'Colmar EXUBERANCE', 'Material': 'poliester și nailon, umplutură 90% puf de rață', 'Caracteristici': 'reversibilă, glugă fixă, fără PFC, REPREVE', 'Cod produs': '3442E.2Y'},
  notes=['„Reversibilă” apare doar în titlu, descrierea magazinului nu o explică.'])

w(13478,
  f'<p>Geaca de tranziție {A("/brand/guess/", "GUESS")} J6YL19 albastră este o {A("/categorie/geci-jachete/", "geacă pentru fete")} din denim de bumbac, fără căptușeală, cu efect prespălat, ușor vintage, și guler clasic. Croiala relaxed fit și umerii coborâți o fac lejeră și comodă la joacă.</p>'
  '<p>Se închide cu nasturi, iar lungimea până la șolduri nu încurcă mișcarea. Denimul își păstrează forma la purtarea de zi cu zi.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '100% bumbac.'), ('Închidere', 'nasturi.'), ('Guler', 'clasic.'))
  + '<p>Mărimile 122-125 până la 167 sunt pentru fete de aproximativ 7-14 ani.</p>',
  [('model', 'Guess Geacă de tranziție pentru copii din denim albastră J6YL19 D1171'), ('bumbac', 'Confecționată din bumbac'), ('căptușeală', 'Fără căptușeală'),
   ('prespălat', 'Efectul prespălat conferă gecii un aspect la modă, ușor vintage'), ('guler', 'Gulerul clasic'), ('croială', 'Croiala lejeră tip relaxed fit'),
   ('umeri', 'Linia umerilor coborâtă'), ('nasturi', 'Sistemul de închidere cu nasturi'), ('lungime', 'Lungimea până la șolduri'),
   ('denim', 'Utilizarea denimului o face rezistentă și durabilă la uzura zilnică, menținându-și forma'), ('material', '100% Bumbac')],
  {'Model': 'GUESS J6YL19', 'Material': '100% bumbac (denim)', 'Caracteristici': 'efect prespălat, guler clasic, nasturi', 'Cod produs': 'J6YL19 D1171'})

w(13483,
  f'<p>Încălțămintea de iarnă {BIO} 261133 roz e una dintre {A("/categorie/ghete-cizme/", "ghete pentru fete")} din piele nubuc și imitație de piele, căptușite cu lână, pentru cele mai mici. Membrana impermeabilă BioTEX ține picioarele uscate și calde.</p>'
  '<p>Aricii cu curea reglabilă fac încălțatul rapid, iar vârful rotund, cauciucat, apără degetele de lovituri.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Călcâi', 'întărit, cu stabilizatori laterali.'), ('Interior', 'lână.'), ('Podology Partnership', 'colaborare cu podologi.'))
  + '<p>Numerele 18-25 se potrivesc fetițelor de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii din piele roz 261133'), ('material', 'Partea superioară din piele nubuc și imitație de piele'), ('lână', 'Lână'),
   ('BioTEX', 'Membrana impermeabilă BioTEX asigură protecție împotriva umidității, menținând picioarele uscate și calde'), ('arici', 'Închidere cu arici și curea reglabilă'),
   ('vârf', 'Vârf rotund, cauciucat asigură protecția degetelor'), ('talpă', 'Talpă flexibilă din cauciuc'), ('călcâi', 'Călcâi întărit și stabilizatori laterali'), PODO],
  {'Model': 'Biomecanics 261133', 'Material': 'piele nubuc și imitație de piele, căptușeală din lână', 'Caracteristici': 'BioTEX, arici cu curea reglabilă, vârf cauciucat', 'Cod produs': '261133'})

w(13484,
  f'<p>Ghetele de iarnă {BIO} 261134 bleumarin sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} din piele naturală, cu guler moale și interior din lână, pentru plimbări de iarnă și joacă afară. Membrana BioTEX integrată ajută la păstrarea picioarelor uscate.</p>'
  '<p>Scaiul cu curea reglabilă face încălțatul rapid, iar vârful rotund, cauciucat, apără degetele de lovituri. Talpa flexibilă lasă piciorul să se miște natural la mers.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Călcâi', 'întărit, cu stabilizatoare laterale.'), ('Podology Partnership', 'lucrat cu podologi.'))
  + '<p>Numerele 18-25 sunt pentru copii de cam 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii din piele bleumarin 261134'), ('piele', 'Partea superioară din piele naturală cu guler moale'), ('lână', 'Lână'),
   ('plimbări', 'Ideale pentru plimbările de iarnă și joaca în aer liber'), ('BioTEX', 'Membrana impermeabilă integrată BioTEX ajută la menținerea picioarelor uscate'),
   ('scai', 'Sistem practic de închidere cu scai cu o curea reglabilă'), ('vârf', 'Vârful rotund, cauciucat oferă protecție degetelor împotriva loviturilor'),
   ('talpă', 'Talpa flexibilă din cauciuc permite mișcarea naturală a piciorului'), ('călcâi', 'Călcâiul întărit și stabilizatoarele laterale'), PODO],
  {'Model': 'Biomecanics 261134', 'Material': 'piele naturală, interior din lână, talpă din cauciuc', 'Caracteristici': 'BioTEX, scai cu curea reglabilă, vârf cauciucat', 'Cod produs': '261134'})

w(13508,
  f'<p>Cizmele de iarnă {REIMA} Hiipien maro sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} ușor izolate, vegane, fără PVC, din material textil și piele ecologică, confortabile până la -10°C. Membrana din partea de sus apără de umezeală și lasă aerul să circule, fără garanția impermeabilității complete.</p>'
  '<p>Șireturile elastice cu cârlig, scaiul și bucla de la spate fac încălțatul rapid. Partea de sus ridicată sprijină glezna.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'spumă moale și cauciuc durabil.'), ('Inserții Happy Fit', 'detașabile, pentru mărime.'), ('Interior', 'textil.'), ('Reflectorizante', 'pentru seară.'))
  + '<p>Numerele 28-38 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'Reima Cizme de iarna pentru copii Hiipien culoarea maro, 5400018B'), ('izolat', 'Izolare: usor izolat'), ('vegan', 'Potrivit pentru vegani'), ('PVC', 'Acest produs nu conține PVC'),
   ('material', 'combinatia materialului textil cu pielea ecologica'), ('temperatură', 'Modelul asigură confort de utilizare la temperaturi de până la -10°C'),
   ('membrană', 'Membrana conținută în partea superioară'), ('apă', 'nu garantează impermeabilitatea completă'), ('închidere', 'Șireturile elastice și închiderea cu cârlig'),
   ('scai', 'Fixare: cu scai'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('spumă', 'Talpa intermediară din spumă oferă o senzație mai moale'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'),
   ('Happy Fit', 'Inserțiile detașabile Happy Fit vă permit să alegeți dimensiunea potrivită'), ('interior', 'Interiorul textil este confortabil'), ('reflectorizant', 'Elementele reflectorizante')],
  {'Model': 'Reima Hiipien', 'Material': 'textil și piele ecologică, interior textil, talpă din spumă și cauciuc', 'Caracteristici': 'ușor izolate, -10°C, membrană, Happy Fit, vegane', 'Cod produs': '5400018B'})

w(13509,
  f'<p>Hanoracul {REIMA} Muhku violet este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "hanorac unisex")} din polar moale, pufos, cu uscare rapidă, cu croială relaxed fit, bun pentru oraș și pentru ieșiri în aer liber. Gulerul înalt apără gâtul de frig.</p>'
  '<p>Se închide scurt, cu capse, iar buzunarele laterale au tot capse. Manșetele cu bandă elastică țin căldura, iar materialul elastic nu încurcă mișcările.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Polar', '100% poliester.'), ('Inserții', '92% poliester, 8% elastan.'), ('Stil', 'casual, lejer.'))
  + '<p>Mărimile 104-164 sunt pentru copii de aproximativ 4-14 ani.</p>',
  [('model', 'Reima Hanorac pentru copii din polar Muhku violet 5200504B'), ('polar', 'Polar moale din fleece pufos'), ('uscare', 'Tricot cu uscare rapidă'),
   ('croială', 'Croială lejeră relaxed fit'), ('aer liber', 'Caracter universal face ca modelul să fie potrivit pentru activități în aer liber'), ('guler', 'Guler înalt practic protejează gâtul de frig'),
   ('capse', 'Închidere scurtă cu capse'), ('buzunare', 'Buzunare laterale cu capse'), ('manșete', 'Manșete cu bandă elastică'), ('material', '100% Poliester'),
   ('suplimentar', '92% Poliester, 8% Elastan'), ('casual', 'Stil casual'), ('elastic', 'Material elastic permite adaptarea la siluetă și nu restricționează mișcările')],
  {'Model': 'Reima Muhku', 'Material': 'polar 100% poliester, inserții cu elastan', 'Caracteristici': 'uscare rapidă, guler înalt, capse', 'Cod produs': '5200504B'})

w(13517,
  f'<p>Pantofii {A("/brand/geox/", "Geox")} BIGLIA argintii sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} din piele, cu interior tot din piele, ușori, pentru cele mai mici. Velcro-ul face încălțatul rapid, iar vârful e rotund.</p>'
  '<p>Membrana Geox Respira scade umezeala din interior, iar sistemul Light Flexy din branț lasă piciorul să se miște liber. O tehnologie moale din talpă preia șocurile, iar branțul din piele previne mirosul neplăcut.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Branț', 'din piele, previne frecarea.'), ('Interior', 'piele.'), ('Talpă', 'material sintetic.'))
  + '<p>Numerele 18-26 se potrivesc fetițelor de aproximativ 1-4 ani.</p>',
  [('model', 'Geox Încălțăminte din piele pentru copii BIGLIA culoarea argintiu, B044CC.007BC'), ('piele', 'Gamba: Piele'), ('interior', 'Interiorul: Piele'), ('ușor', 'Model ușor și confortabil'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('vârf', 'Varf rotund'),
   ('Respira', 'Membrana unica si impermeabila a tehnologiei Geox Respira ajuta la scaderea umezelii excesive'), ('Light Flexy', 'Light Flexy Sistem de brant pentru libertatea de miscare'),
   ('moale', 'Tehnologie moale pentru amortizare'), ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea, abraziunile si aparitia unui miros neplacut')],
  {'Model': 'Geox BIGLIA', 'Material': 'piele, interior din piele', 'Caracteristici': 'velcro, Geox Respira, Light Flexy', 'Cod produs': 'B044CC.007BC'})

w(13518,
  f'<p>Botinele {BIO} 261214 negre sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} din piele întoarsă, cu buline delicate, fără izolație, pentru zilele mai calde ale sezonului de tranziție. Închiderea dublă, cu arici și fermoar, face încălțatul rapid.</p>'
  '<p>Vârful și călcâiul sunt întărite, iar talpa plată din cauciuc dă un pas stabil pe diverse suprafețe. Negrul se poartă ușor cu multe ținute.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Interior', 'material textil.'), ('Exterior', 'piele întoarsă.'), ('Model', 'cu buline.'))
  + '<p>Numerele 28-34 sunt pentru fete de cam 4-11 ani.</p>',
  [('model', 'Biomecanics Botine pentru copii din piele întoarsă negre 261214'), ('piele', 'Partea superioară din piele întoarsă'), ('buline', 'Modelul cu buline'),
   ('izolație', 'Lipsa izolației termice face ca modelul să fie potrivit pentru zilele mai calde din perioada de tranziție'), ('închidere', 'Închiderea dublă cu arici și fermoar'),
   ('vârf', 'Vârful întărit'), ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa plată din cauciuc susține stabilitatea pasului pe diverse suprafețe'),
   ('negru', 'Culoarea neagră facilitează asortarea cu multe ținute'), ('interior', 'Interiorul din material textil')],
  {'Model': 'Biomecanics 261214 (botine)', 'Material': 'piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'arici și fermoar, fără izolație, buline', 'Cod produs': '261214'})

w(13519,
  f'<p>Pentru băieții mai mari, hanoracul {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KB0KB10766 roșu vine în numerele 128-176: un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanorac pentru băieți")} din tricot de bumbac 100%, fără fermoar și fără glugă, uni. Decolteul rotund are bordură elastică.</p>'
  '<p>Benzile elastice de la bază și manșete țin forma, iar lipsa căptușelii îl face ușor. Croiala e simplă și lasă loc de mișcare.</p>'
  '<p>Detaliile principale:</p>'
  + L(('Material', 'tricot de bumbac, plăcut la atingere.'), ('Stil', 'casual și streetwear.'), ('Model', 'uni.'))
  + '<p>Se potrivește băieților de pe la 8 până pe la 16 ani.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac roșu KB0KB10766'), ('tricot', 'Materialul din tricot de bumbac este plăcut la atingere'), ('bumbac', '100% bumbac în compoziție'),
   ('fermoar', 'Modelul fără fermoar și fără glugă'), ('uni', 'Modelul uni'), ('decolteu', 'Decolteul rotund cu bordură elastică'), ('benzi', 'Benzile elastice de la bază și manșete'),
   ('căptușeală', 'Fără căptușeală permite o construcție ușoară'), ('croială', 'Croiala simplă a hanoracului permite libertate de mișcare'), ('stil', 'Stilul casual și streetwear')],
  {'Model': 'Tommy Hilfiger KB0KB10766', 'Material': '100% bumbac', 'Caracteristici': 'fără fermoar și glugă, decolteu rotund', 'Cod produs': 'KB0KB10766'})
