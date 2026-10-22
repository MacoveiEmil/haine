import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(13302,
  f'<p>Bluza cu mânecă lungă {TH} KB0KB09664 bleumarin este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză pentru băieți")} clasică, din bumbac 100% moale și elastic, cu logo discret, pentru zilele mai răcoroase. Decolteul are guler și închidere, ceea ce o face ușor de îmbrăcat.</p>'
  '<p>Croiala regulară nu strânge corpul la mișcare, iar modelul uni se poartă cu multe ținute.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'cu guler și închidere.'), ('Model', 'uni, cu logo.'))
  + '<p>Mărimile 128-176 sunt pentru băieți de aproximativ 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Longsleeve pentru copii, din bumbac bleumarin KB0KB09664'), ('bumbac', 'Bumbacul moale 100% este plăcut la atingere'), ('elastic', 'Materialul elastic ajută la adaptarea la siluetă'),
   ('logo', 'Modelul uni cu logo-ul mărcii'), ('răcoros', 'ideal pentru zilele mai răcoroase'), ('decolteu', 'Decolteu cu guler și închidere adaugă eleganță, facilitând îmbrăcarea'),
   ('croială', 'Croiala regulară favorizează libertatea de mișcare'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KB0KB09664', 'Material': '100% bumbac', 'Caracteristici': 'mânecă lungă, guler cu închidere, logo', 'Cod produs': 'KB0KB09664'})

w(13306,
  f'<p>{BIO} 261165 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, din piele naturală, cu profil scurt și guler întărit, făcuți cu podologi, în stil casual și streetwear. Baretele cu arici fac încălțatul și descălțatul rapid, chiar de către copil.</p>'
  '<p>Talpa plată din cauciuc lasă piciorul să ruleze natural, iar călcâiul întărit îl ține în poziție corectă. Pielea naturală e rezistentă și arată bine mult timp.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textilă, moale.'), ('Branț', 'detașabil, aerisit.'), ('Închidere', 'barete cu arici.'))
  + '<p>Numerele 20-23 se potrivesc băieților de cam 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele bleumarin 261165'), ('piele', 'Materialul exterior contribuie la durabilitate'), ('profil', 'Permite libertatea de mișcare, iar gulerul întărit susține glezna'),
   ('podologi', 'Dezvoltat cu podologi'), ('stil', 'stilurile casual și streetwear'), ('arici', 'Facilitează încălțarea și descălțarea rapidă, susținând autonomia'),
   ('talpă', 'Construcția plată favorizează stabilitatea și rularea naturală a piciorului'), ('călcâi', 'susținând menținerea unei posturi corecte'),
   ('căptușeală', 'Materialul textil din interior'), ('branț', 'Construcția detașabilă favorizează igiena și ventilația')],
  {'Model': 'Biomecanics 261165', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'barete cu arici, profil scurt, branț detașabil', 'Cod produs': '261165'})

w(13309,
  f'<p>Pantofii {BIO} 261121 bleumarin sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} din piele naturală, ușori și flexibili, în stil casual, cu tehnologia Podology Partnership. Talpa din cauciuc are 1 cm și lasă piciorul să se miște liber.</p>'
  '<p>Vârful rotund e cauciucat și apără degetele, iar aricii cu curea reglabilă se strâng ușor după picior. Interiorul textil e confortabil și lasă aerul să circule.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Branț', 'textil, detașabil, antimiros și antibacterian.'), ('Interior', 'material textil.'), ('Călcâi', 'întărit.'))
  + '<p>Numerele 19-25 sunt pentru copii de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele bleumarin 261121'), ('piele', 'Partea superioară din piele naturală'), ('ușor', 'Ușori și flexibili'),
   ('casual', 'Stil casual'), ('Podology', 'Tehnologia Biomecanics Podology Partnership'), ('talpă', 'Talpă flexibilă din cauciuc , cu o grosime de 1 cm'),
   ('vârf', 'Vârf rotund, cauciucat , protejează degetele'), ('arici', 'Închidere cu arici , cu o curea reglabilă'),
   ('branț', 'Branț detașabil din material textil , este respirabil, antimiros și antibacterian'), ('interior', 'Interior din material textil asigură confort și respirabilitate'), ('călcâi', 'Călcâi întărit')],
  {'Model': 'Biomecanics 261121', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, vârf cauciucat, branț antibacterian', 'Cod produs': '261121'})

w(13316,
  f'<p>Cizmele {TH} T1X5-34087 maro sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} numite de magazin „de iarnă”, dar neizolate, din imitație de piele nubuc, ușor de curățat. Au șiret, fermoar lateral și Velcro, deci se reglează o dată și se încalță repede.</p>'
  '<p>Partea de sus ridicată sprijină glezna, iar cutia rotundă e întărită. Spatele călcâiului e puternic rigidizat.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'sintetic și textil, confortabil.'), ('Talpă exterioară', 'din cauciuc, durabilă.'), ('Închidere', 'șiret, fermoar și Velcro.'))
  + '<p>Numerele 30-34 se potrivesc copiilor de cam 6-11 ani; la 34 branțul are 22 cm.</p>',
  [('model', 'Tommy Hilfiger Cizme de iarnă pentru copii culoarea maro, T1X5-34087'), ('neizolat', 'Izolare: neizolat'), ('nubuc', 'imitație de piele năbuc'),
   ('întreținere', 'Modelul este ușor de curățat și de întreținut'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Spatele calcaiului peternic rigidizat'),
   ('interior', 'Interior confortabil'), ('textil', 'Material sintetic, Material textil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 22 cm')],
  {'Model': 'Tommy Hilfiger T1X5-34087', 'Material': 'imitație de piele nubuc, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'șiret, fermoar lateral și Velcro, neizolate', 'Cod produs': 'T1X5-34087'},
  notes=['Titlul spune „cizme de iarnă”, dar atributele dau „neizolat”; am scris ambele.'])

w(13317,
  f'<p>Pantofii {GEOX} MACCHIA B664NA bleumarin sunt {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi pentru băieți")} din piele naturală și piele întoarsă, cu interior din piele, în stil casual. Sistemul Softly Cushioned preia impactul pașilor, iar Flexy System, cu incizii în talpă, ajută piciorul să se îndoaie natural.</p>'
  '<p>Aricii fac încălțatul rapid, iar vârful rotund, rigidizat, lasă loc degetelor. Tehnologia GEOX Respira ține piciorul uscat.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'din piele, detașabil, cu imprimeu de mărime.'), ('Talpă', 'din cauciuc.'), ('Interior', 'piele naturală.'))
  + '<p>Numerele 18-26 sunt pentru băieți de aproximativ 1-4 ani.</p>',
  [('model', 'Geox Pantofi pentru copii din piele MACCHIA bleumarin B664NA.03322'), ('material', 'Partea superioară dintr-o combinație de piele naturală și piele întoarsă'),
   ('interior', 'Interiorul din piele naturală'), ('casual', 'Stilul casual'), ('Softly', 'Sistemul Softly Cushioned'), ('Flexy', 'Flexy System cu incizii în talpă favorizează flexarea naturală a piciorului'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă'), ('vârf', 'Vârf rotund, rigidizat'),
   ('Respira', 'Tehnologia GEOX Respira™ favorizează eliminarea umidității, menținând picioarele uscate'), ('branț', 'Branț detașabil din piele naturală cu imprimeu'),
   ('talpă', 'Talpa din cauciuc permite o bună aderență')],
  {'Model': 'Geox MACCHIA', 'Material': 'piele naturală și piele întoarsă, interior din piele, talpă din cauciuc', 'Caracteristici': 'Geox Respira, Softly Cushioned, Flexy System, arici', 'Cod produs': 'B664NA.03322'})

w(13322,
  f'<p>Cardiganul {TH} KG0KG09503 bleumarin este o {A("/categorie/bluze-tricouri-hanorace/", "bluză pentru fete")} subțire, din bumbac 100% tricotat, elastic, cu nasturi, ușoară și potrivită pentru sezoanele de tranziție. Croiala relaxată și umerii coborâți îl fac comod la joacă.</p>'
  '<p>Decolteul rotund clasic și modelul uni îl fac ușor de purtat cu multe haine, inclusiv în ținute boho. Bumbacul e plăcut pe piele.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Închidere', 'nasturi.'), ('Mâneci', 'lungi, cu umeri coborâți.'))
  + '<p>Au rămas mărimile 116-122, pentru fete de aproximativ 6-7 ani.</p>',
  [('model', 'Tommy Hilfiger Cardigan pentru copii din bumbac bleumarin KG0KG09503'), ('subțire', 'Țesătura subțire face ca acest cardigan să fie ușor și ideal pentru sezoanele de tranziție'),
   ('bumbac', 'Confecționat 100% din bumbac , permite un contact plăcut cu pielea'), ('elastic', 'Materialul tricotat elastic'), ('nasturi', 'Sistemul practic de închidere cu nasturi'),
   ('croială', 'Croiala relaxată'), ('umeri', 'Mâneca lungă cu linia umerilor coborâtă'), ('decolteu', 'Decolteul rotund clasic'), ('uni', 'Modelul uni al materialului'),
   ('boho', 'în stil boho'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG09503 (cardigan)', 'Material': '100% bumbac', 'Caracteristici': 'nasturi, croială relaxată, decolteu rotund', 'Cod produs': 'KG0KG09503'})

w(13326,
  f'<p>Modelul {GEOX} MACCHIA în varianta violet B664PD: {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} din piele nubuc și piele întoarsă, moi la atingere, cu căptușeală și branț din piele naturală. Sunt făcuți pentru școală, locul de joacă sau plimbări.</p>'
  '<p>Pernuța softly cushioned din talpă face pasul mai moale, iar sistemul flexy lasă talpa să se îndoaie odată cu piciorul. Aricii se închid repede.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'cu membrană, ține piciorul uscat.'), ('Talpă', 'cauciuc flexibil.'), ('Vârf', 'rotund, lasă degetele libere.'))
  + '<p>Numerele 18-26 merg la fetițe de cam 1-4 ani.</p>',
  [('model', 'Geox Încălțăminte pentru copii din nubuck MACCHIA violet B664PD.03322'), ('material', 'Partea superioară din piele nubuc și piele întoarsă conferă încălțămintei un aspect elegant și o senzație moale la atingere'),
   ('interior', 'Interiorul din piele naturală'), ('branț', 'Branțul din piele naturală'), ('școală', 'potrivită pentru școală, locul de joacă sau plimbări'),
   ('softly', 'Amortizarea moale softly cushioned din talpă'), ('flexy', 'Sistemul flexy din talpă permite îndoirea naturală a piciorului'),
   ('arici', 'Închiderea practică cu arici'), ('Respira', 'Tehnologia GEOX Respira™ cu membrană ajută la eliminarea umidității'),
   ('talpă', 'Talpa din cauciuc asigură o bună aderență la sol și flexibilitate'), ('vârf', 'Vârful rotund permite așezarea liberă a degetelor')],
  {'Model': 'Geox MACCHIA', 'Material': 'piele nubuc și piele întoarsă, interior din piele, talpă din cauciuc', 'Caracteristici': 'Geox Respira, softly cushioned, flexy, arici', 'Cod produs': 'B664PD.03322'})

w(13329,
  f'<p>Geaca {A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 322B15066001 bleumarin este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} matlasată, ușor izolată, pentru sezonul de tranziție, cu croială regular fit, în stil casual și clasic. Se poate împacheta într-un săculeț, ca să o luați ușor la drum.</p>'
  '<p>Nu are glugă, se închide cu fermoar, iar lungimea până la șolduri acoperă bine trunchiul.</p>'
  '<p>Materialele și buzunarele:</p>'
  + L(('Exterior și căptușeală', '100% nailon.'), ('Umplutură', '100% poliester.'), ('Buzunare', 'laterale.'))
  + '<p>Mărimile 88-93 până la 124-134 se potrivesc băieților de aproximativ 1-9 ani.</p>',
  [('model', 'Polo Ralph Lauren Geacă petrecută pentru copii bleumarin 322B15066001'), ('matlasat', 'Geaca matlasată bleumarin Polo Ralph Lauren'), ('izolat', 'Izolație termică ușoară'),
   ('tranziție', 'ideală pentru sezonul de tranziție'), ('croială', 'Croiul regular fit'), ('stil', 'ținutele casual și clasice'),
   ('săculeț', 'Posibilitatea de a fi împachetată într-un săculeț permite depozitarea și transportul facil'), ('glugă', 'Fără glugă'), ('fermoar', 'Sistem de închidere cu fermoar'),
   ('lungime', 'Lungime până la șolduri asigură o acoperire optimă a trunchiului'), ('exterior', '100% Nailon'), ('umplutură', '100% Poliester'),
   ('buzunare', 'Buzunare laterale')],
  {'Model': 'Polo Ralph Lauren 322B15066001', 'Material': '100% nailon, umplutură din poliester', 'Caracteristici': 'matlasată, se împachetează în săculeț, fermoar', 'Cod produs': '322B15066001'})

w(13334,
  f'<p>Bomberul {A("/brand/ea7-emporio-armani/", "EA7 Emporio Armani")} 7B000033 vine și în bleumarin, în numerele 110-170: o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} subțire, neizolată, gândită pentru primăvară și toamnă. Nu are glugă, iar stilul e casual și streetwear.</p>'
  '<p>Pe interior e căptușită cu bumbac. Fermoarul se trage rapid, iar marginile elastice de la bază și manșete o țin bine pe corp.</p>'
  '<p>Compoziția:</p>'
  + L(('Exterior', 'poliamidă 100%.'), ('Căptușeală', 'bumbac 100%.'), ('Bordură elastică', 'poliester cu 3% elastan.'))
  + '<p>Se potrivește băieților de pe la 5 până pe la 15 ani.</p>',
  [('model', 'EA7 Emporio Armani Geacă bomber pentru copii bleumarin 7B000033 AF12873'), ('neizolat', 'Izolare: neizolat'), ('tranziție', 'Construcția fără izolație termică permite purtarea în sezoanele de tranziție'),
   ('ușor', 'Realizată din țesătură ușoară'), ('glugă', 'Lipsa glugii'), ('stil', 'Designul în stil casual și streetwear'), ('căptușeală', '100% Bumbac'),
   ('fermoar', 'Închiderea cu fermoar'), ('borduri', 'Baza și manșetele cu bordură elastică'), ('exterior', '100% Poliamidă'), ('tiv', '97% Poliester, 3% Elastan')],
  {'Model': 'EA7 Emporio Armani 7B000033 (bomber)', 'Material': '100% poliamidă, căptușeală din bumbac', 'Caracteristici': 'neizolată, fermoar, margini elastice', 'Cod produs': '7B000033 AF12873'})

w(13341,
  f'<p>Geaca de blugi {A("/brand/guess/", "GUESS")} J6RL07 bleumarin este o {A("/categorie/geci-jachete/", "geacă pentru fete")} oversize, neizolată și fără căptușeală, din denim strălucitor, cu fibră metalică, pentru sezonul de tranziție. Croiala lejeră și umerii coborâți lasă mișcarea liberă.</p>'
  '<p>Se închide cu nasturi pe două rânduri, are clape clasice și două buzunare laterale. Tivul are bandă elastică, așa că geaca stă bine pe corp.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Material', '85% bumbac, 11% viscoză, 4% fibră metalică.'), ('Închidere', 'nasturi, pe două rânduri.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 122-125 până la 167 sunt pentru fete de aproximativ 7-14 ani.</p>',
  [('model', 'Guess Geacă de blugi pentru copii culoarea bleumarin, J6RL07 D5D90'), ('oversize', 'Fit: oversize'), ('neizolat', 'Model neizolat fara captuseala'),
   ('denim', 'Model neizolat confecționat din denim'), ('strălucitor', 'Model din material eficient, strălucitor'), ('tranziție', 'Izolare: tranzitional'),
   ('croială', 'Croială lejeră pentru libertate totală de mișcare'), ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'), ('nasturi', 'Fixare dubla cu butoane'),
   ('clape', 'Clapete clasice'), ('buzunare', 'Două buzunare laterale'), ('tiv', 'Marginea inferioară este finisată cu o bandă elastică'),
   ('material', '85% Bumbac, 11% Viscoza, 4% Fibra metalica'), ('glugă', 'Gluga: fara gluga')],
  {'Model': 'GUESS J6RL07', 'Material': '85% bumbac, 11% viscoză, 4% fibră metalică', 'Caracteristici': 'oversize, denim strălucitor, nasturi', 'Cod produs': 'J6RL07 D5D90'})
