import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

BIO = A('/brand/biomecanics/', 'Biomecanics')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
PODO = ('Podology', 'Biomecanics Podology Partnership')

w(13184,
  f'<p>Pentru copiii puțin mai mari, pantofii {BIO} 261152 maro vin în numerele 24-26: {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} din piele naturală și material sintetic, ușor de îngrijit, în stil casual și clasic. Talpa joasă, de 1,5 cm, ține piciorul așezat natural.</p>'
  '<p>Vârful lat și rotund, cu întăritură, dă degetelor spațiu. Aricii reglabili fac încălțatul ușor, iar stabilizatorii laterali și călcâiul întărit țin piciorul corect.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Branț', 'BioTEX, detașabil, antibacterian și anti-miros.'), ('Căptușeală', 'textilă, moale.'), ('Talpă', 'flexibilă, din cauciuc.'))
  + '<p>Se potrivesc copiilor de aproximativ 2-4 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele maro 261152'), ('material', 'Partea superioară dintr-o combinație de piele naturală și materiale sintetice contribuie la durabilitate și ușurință în îngrijire'),
   ('stil', 'Stil universal casual și clasic'), ('talpă joasă', 'Talpă joasă cu grosimea de 1,5 cm'), ('vârf', 'Vârf lat, rotund cu întăritură'),
   ('arici', 'Închidere cu arici reglabil'), ('stabilizatori', 'Călcâi întărit și stabilizatori laterali'), ('branț', 'Branț detașabil BioTEX cu proprietăți antibacteriene și anti-miros'),
   ('căptușeală', 'Interior căptușit cu material textil'), ('talpă', 'Talpă flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261152', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici reglabil, branț BioTEX antibacterian, vârf lat', 'Cod produs': '261152'})

w(13195,
  f'<p>Geaca bomber {A("/brand/ea7-emporio-armani/", "EA7 Emporio Armani")} 7B000033 neagră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} ușoară, fără izolație, pentru anotimpurile de tranziție, în stil casual și streetwear. Nu are glugă, iar tivul și manșetele cu nervuri se așază bine.</p>'
  '<p>Se închide cu fermoar, iar croiala regulară și lungimea până la șolduri lasă loc de mișcare. Mânecile au croială clasică.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Exterior', '100% poliamidă.'), ('Căptușeală', '100% bumbac.'), ('Tiv elastic', '97% poliester, 3% elastan.'))
  + '<p>Mărimile 140-176 sunt pentru băieți de aproximativ 10-16 ani.</p>',
  [('model', 'EA7 Emporio Armani Geacă bomber pentru copii neagră 7B000033 AF12873'), ('ușor', 'Confecționată din țesătură ușoară'), ('izolație', 'Design fără izolație termică'),
   ('tranziție', 'anotimpurile de tranziție'), ('stil', 'Design în stil casual și streetwear'), ('glugă', 'Absența glugii'), ('nervuri', 'Tivul și manșetele cu nervuri'),
   ('fermoar', 'Închidere cu fermoar'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'), ('exterior', '100% Poliamidă'),
   ('căptușeală', '100% Bumbac'), ('tiv', '97% Poliester, 3% Elastan'), ('mâneci', 'Mâneci cu croială clasică')],
  {'Model': 'EA7 Emporio Armani 7B000033 (bomber)', 'Material': '100% poliamidă, căptușeală din bumbac', 'Caracteristici': 'fără izolație, fermoar, nervuri la tiv și manșete', 'Cod produs': '7B000033 AF12873'})

w(13196,
  f'<p>Ghetele chelsea {BIO} 261161 vin și în gri: {A("/categorie/ghete-cizme/", "ghete pentru fete")} scurte, din piele naturală, cu un motiv animal, pentru primăvară și toamnă. Trec de gleznă și o feresc de frig și de noroi, dar nu sunt căptușite cu izolație.</p>'
  '<p>Scaiul și fermoarul le fac rapide de pus. Vârful și călcâiul au întărituri, iar gulerul e ușor rigid.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'cauciuc plat, 0-2 cm.'), ('Interior', 'textil, cu branțuri care se scot.'), ('Podology', 'colaborare cu podologi.'))
  + '<p>Mărimile 19-23 sunt gândite pentru 1-3 ani, aproximativ.</p>',
  [('model', 'Biomecanics Ghete scurte pentru copii din piele gri 261161'), ('chelsea', 'Model botine chelsea'), ('piele', 'Partea superioară realizată din piele naturală'),
   ('animal', 'Motiv animal'), ('gleznă', 'Înălțime peste gleznă , ce asigură protecție împotriva frigului și murdăriei'), ('izolație', 'Fără izolație interioară'),
   ('închidere', 'Model echipat cu închidere cu scai și fermoar'), ('vârf', 'Vârf întărit și călcâi întărit'), ('guler', 'Construcție cu gulerul superior ușor întărit'),
   ('talpă', 'Talpă plată din cauciuc cu grosimea de 0-2 cm'), ('interior', 'Interior cu căptușeală textilă și branțuri detașabile'), ('Podology', 'Parteneriatul Biomecanics Podology , creat în colaborare cu podologi')],
  {'Model': 'Biomecanics 261161 (chelsea)', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'scai și fermoar, fără izolație, peste gleznă', 'Cod produs': '261161'})

w(13197,
  f'<p>Mănușile de schi {A("/brand/reima/", "Reima")} Snoukka negre sunt {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "mănuși unisex")} din material textil cu elemente reflectorizante, cu umplutură PrimaLoft din fibre reciclate și tratament BIONIC-FINISH ECO. Au și un buzunar cu fermoar pentru permisul de schi.</p>'
  '<p>Palma are întărituri din PU, iar interiorul e căptușit cu material moale, care ține de cald.</p>'
  '<p>Materialele și certificările:</p>'
  + L(('Exterior', 'poliamidă, parțial reciclată, cu strat de poliuretan.'), ('Umplutură', '100% poliester reciclat.'), ('Certificare', 'Bluesign.'))
  + '<p>Mărimile de pe site, între 2-4ani și 12-14 ani, acoperă cam 2-14 ani.</p>',
  [('model', 'Reima Mănuși de schi pentru copii Snoukka 5300055B'), ('culoare', 'Culoare negru'), ('reflectorizant', 'material textil cu elemente reflectorizante'),
   ('PrimaLoft', 'Umplutura PrimaLoft® realizata din fibre reciclate'), ('BIONIC', 'BIONIC-FINISH® ECO - o alternativa ecologica la acoperirea traditionala, hidrofoba DWR'),
   ('buzunar', 'Buzunar funcțional pentru permis de schi, cu fermoar'), ('PU', 'Întăriri suplimentare pe interiorul mâinii din PU'),
   ('căptușeală', 'Interiorul este căptușit cu un material moale care este plăcut pielii și mărește protecția împotriva frigului'),
   ('exterior', '59% Poliamida reciclata, 41% Poliamidă cu strat de poliuretan'), ('umplutură', 'Umplutura: 100% Poliester reciclat'), ('Bluesign', 'Model certificat Bluesign® Standard')],
  {'Model': 'Reima Snoukka', 'Material': 'poliamidă parțial reciclată, umplutură PrimaLoft', 'Caracteristici': 'buzunar pentru ski-pass, reflectorizante, Bluesign', 'Cod produs': '5300055B'},
  varsta_txt='2-14 ani', notes=['Mărimile sunt date în ani (2-4 ani … 12-14 ani); vârsta e luată direct din ele.'])

w(13199,
  f'<p>Hanoracul {TH} KG0KG09604 bleumarin este un {A("/categorie/bluze-tricouri-hanorace/", "hanorac pentru fete")} fără fermoar, din tricot de bumbac 100%, moale și plăcut pe piele, cu logo pe față. Croiala simplă și decolteul rotund îl fac ușor de tras pe cap.</p>'
  '<p>Mânecile lungi se termină cu manșete, iar baza are bandă elastică. Nu are căptușeală, deci e lejer.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% bumbac.'), ('Decolteu', 'rotund, cu bordură elastică.'), ('Decor', 'logo Tommy Hilfiger.'))
  + '<p>Mărimile 128-176 sunt pentru fete de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac bleumarin KG0KG09604'), ('fermoar', 'Croiala fără fermoar cu decolteu rotund facilitează îmbrăcarea și dezbrăcarea rapidă'),
   ('tricot', 'Tricotul din bumbac este respirabil și plăcut la atingere'), ('logo', 'Materialul neted cu logo-ul subtil al mărcii pe partea din față'),
   ('croială', 'Croiala simplă a modelului'), ('mâneci', 'Mâneci lungi clasice terminate cu manșete'), ('benzi', 'Benzile elastice de la bază și de la manșete'),
   ('căptușeală', 'Absența căptușelii contribuie la lejeritatea construcției'), ('decolteu', 'Decolteu rotund finisat cu bordură elastică'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG09604', 'Material': '100% bumbac', 'Caracteristici': 'fără fermoar, decolteu rotund, logo', 'Cod produs': 'KG0KG09604'})

w(13201,
  f'<p>Pantofii {BIO} 262100 roz sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} din piele naturală netedă, în stil casual, pentru primăvară și vară, făcuți cu podologi. Vârful cauciucat apără degetele, iar velcro-ul face încălțatul rapid și reglarea după picior.</p>'
  '<p>Tehnologia ANTI-ODOR limitează mirosurile neplăcute, iar talpa din cauciuc e flexibilă și ține bine pe sol. Pielea dă pantofului un aspect clasic.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Interior', 'material textil.'), ('Branțuri', 'detașabile, se curăță ușor.'), ('Podology Partnership', 'sprijin pentru dezvoltarea piciorului.'))
  + '<p>Numerele 19-25 se potrivesc fetițelor de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele roz 262100'), ('piele', 'Partea superioară din piele naturală'), ('neted', 'Textura netedă a materialului conferă încălțămintei un aspect clasic'),
   ('casual', 'Pantofi pentru copii cu un caracter casual, potriviți pentru primăvară și vară'), ('podologi', 'conceput în colaborare cu podologi'),
   ('vârf', 'Vârful cauciucat ajută la protejarea degetelor'), ('velcro', 'Închiderea cu velcro facilitează încălțarea rapidă și ajustarea'),
   ('ANTI-ODOR', 'Tehnologia ANTI-ODOR limitează dezvoltarea microorganismelor și formarea mirosurilor neplăcute'), ('talpă', 'Talpa din cauciuc asigură flexibilitate și o bună aderență la sol'),
   ('interior', 'Interiorul din material textil'), ('branț', 'Branțurile detașabile permit curățarea ușoară'), PODO],
  {'Model': 'Biomecanics 262100', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, vârf cauciucat, ANTI-ODOR', 'Cod produs': '262100'})

w(13203,
  f'<p>Cizmele de iarnă {A("/brand/geox/", "Geox")} ADELHIDE argintii sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} ușor izolate, din material textil, cu tehnologia Amphibiox, care ține apa afară și lasă aerul să circule. Rezistă la apă, dar magazinul nu garantează impermeabilitatea completă.</p>'
  '<p>Partea de sus ridicată sprijină glezna pe teren denivelat, iar velcro-ul face încălțatul rapid.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Interior', 'sintetic și textil, confortabil.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 28-35 sunt pentru fete de în jur de 4-11 ani.</p>',
  [('model', 'Geox Cizme de iarnă pentru copii ADELHIDE culoarea argintiu, J56EWA.0LVNF'), ('izolat', 'Izolare: usor izolat'), ('textil', 'confectionat din material textil'),
   ('Amphibiox', 'Tehnologia Amphibiox®. Membrana special respirabila si nepermeabila protejeaza atat talpa exterioara, cat si cea superioara'),
   ('apă', 'nu garantează impermeabilitatea completă'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('interior', 'Material sintetic, Material textil'), ('confort', 'Interior confortabil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox ADELHIDE', 'Material': 'textil, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'Amphibiox, Geox Respira, ușor izolate, velcro', 'Cod produs': 'J56EWA.0LVNF'})

w(13210,
  f'<p>Pantofii {A("/brand/primigi/", "Primigi")} PTR 24112 bleumarin sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} uni, din piele naturală, cu interior și branț tot din piele, pentru cei mici. Vârful lat și rigidizat, tip barefoot, lasă degetele libere și le apără.</p>'
  '<p>Talpa flexibilă din cauciuc urmează mișcarea piciorului, iar aricii fac încălțatul și reglarea rapide. Călcâiul întărit și gulerul ușor întărit țin piciorul în pantof.</p>'
  '<p>Din ce e făcut pantoful:</p>'
  + L(('Exterior', 'piele naturală.'), ('Interior', 'piele naturală, aerisit.'), ('Branț', 'piele naturală.'))
  + '<p>Numerele 20-24 se potrivesc copiilor de aproximativ 1-3 ani.</p>',
  [('model', 'Primigi Pantofi pentru copii din piele bleumarin PTR 24112'), ('uni', 'Modelul uni'), ('piele', 'Partea superioară din piele naturală'),
   ('interior', 'Interiorul din piele naturală permite o circulație adecvată a aerului'), ('branț', 'Branțul din piele naturală'),
   ('vârf', 'Vârful lat și rigidizat tip barefoot oferă degetelor libertate și protecție'), ('talpă', 'Talpa flexibilă din cauciuc susține mișcarea naturală a piciorului'),
   ('arici', 'Închiderea cu arici permite o încălțare și o ajustare ușoară și rapidă'), ('călcâi', 'Călcâiul întărit stabilizează piciorul copilului în pantof'),
   ('guler', 'Gulerul superior ușor întărit')],
  {'Model': 'Primigi PTR 24112', 'Material': 'piele naturală, interior și branț din piele', 'Caracteristici': 'vârf barefoot, arici', 'Cod produs': 'PTR 24112'})

w(13212,
  f'<p>Vesta de puf {TH} KS0KS00755 în bleumarin este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "vestă pentru băieți")} matlasată din țesătură durabilă, umplută cu puf de rață și pene, care încălzește fără să îngreuneze. Are logo discret și guler ridicat, bun în zilele cu vânt.</p>'
  '<p>Fermoarul de pe toată lungimea o face rapid de pus, iar lipsa glugii o lasă să încapă sub alte haine.</p>'
  '<p>Detaliile vestei:</p>'
  + L(('Căptușeală', 'integrală.'), ('Buzunare', 'slip-on, pe laterale.'), ('Lungime', 'până la șolduri.'), ('Compoziție', 'nailon, umplutură 90% puf de rață.'))
  + '<p>Între 104 și 122, mărimile acoperă băieți de pe la 4 până pe la 7 ani.</p>',
  [('model', 'Tommy Hilfiger Vestă de puf pentru copii bleumarin KS0KS00755'), ('matlasat', 'Confecționată din țesătură durabilă cu o structură matlasată'),
   ('puf', 'Umplutura ușoară din puf natural'), ('logo', 'Modelul uni cu logo subtil'), ('guler', 'Gulerul ridicat susține protecția gâtului împotriva frigului, adăugând confort în zilele vântoase'),
   ('fermoar', 'Sistemul de închidere cu fermoar pe toată lungimea'), ('glugă', 'Lipsa glugii favorizează un aspect minimalist și facilitează purtarea sub alte articole de îmbrăcăminte'),
   ('căptușeală', 'Căptușeala integrală'), ('buzunare', 'Buzunare laterale slip-on'), ('lungime', 'Lungimea până la șolduri'), ('umplutură', '90% Puf de rață, 10% Pene de rață')],
  {'Model': 'Tommy Hilfiger KS0KS00755', 'Material': '100% nailon, umplutură 90% puf de rață', 'Caracteristici': 'vestă de puf, guler ridicat, fermoar', 'Cod produs': 'KS0KS00755'})

w(13216,
  f'<p>{BIO} 261131 sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil scurt, din piele naturală și imitație de piele, rezistenți la purtarea zilnică, în stil casual și streetwear. Cureaua reglabilă cu arici face încălțatul rapid.</p>'
  '<p>Stabilizatorul lateral și călcâiul întărit țin piciorul corect, iar gulerul moale cuprinde glezna. Branțurile se scot ușor pentru curățat.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'anti-miros și antibacterian, detașabil.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Podology Partnership', 'sprijin podologic.'))
  + '<p>Numerele 18-25 se potrivesc fetițelor de cam 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele roz 261131'), ('profil', 'cu profil scurt'), ('material', 'Combinația de piele naturală și imitație de piele asigură rezistență pentru utilizarea zilnică'),
   ('stil', 'ținutele casual și streetwear'), ('arici', 'Cureaua reglabilă cu arici facilitează încălțarea rapidă'), ('stabilizator', 'Stabilizatorul lateral susține poziționarea corectă'),
   ('călcâi', 'Asigură o menținere stabilă a călcâiului'), ('guler', 'Asigură o înfășurare delicată în jurul gleznei'), ('branț', 'Branțul anti-miros și antibacterian'),
   ('detașabil', 'Branțuri detașabile: Permit o curățare ușoară'), ('talpă', 'Confecționată din cauciuc, favorizează flexarea naturală a piciorului'), ('Podology', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261131', 'Material': 'piele naturală și imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, stabilizator lateral, branț antibacterian', 'Cod produs': '261131'})
