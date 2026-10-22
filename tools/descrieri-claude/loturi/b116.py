import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
NOAPA = 'Magazinul descrie membrana ca 100% impermeabilă, dar are și formula că nu garantează impermeabilitatea completă; nu am scris „impermeabile”.'

w(9989,
  f'<p>Adidașii {A("/brand/biomecanics/", "Biomecanics")} 262251 bleumarin sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt, făcuți împreună cu podologi pentru dezvoltarea sănătoasă a piciorului. Talpa Cone Tech din cauciuc e flexibilă și lasă piciorul să se miște natural.</p>'
  '<p>Branțurile Always Dry, detașabile, țin interiorul uscat, iar materialele au protecție antibacteriană. Contrafortul e rigidizat, căptușeala textilă e moale, iar cureaua cu scai se reglează ușor. Sunt gândiți pentru primăvară și vară.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Talpă', 'cauciuc, profilată.'))
  + '<p>Numerele 28-34 se potrivesc orientativ copiilor de 4-11 ani.</p>',
  [('cod', '262251'), ('culoare', 'Culoare bleumarin'), ('podologi', 'Dezvoltați în colaborare cu podologi'), ('profil', 'Profilul lor redus'),
   ('Cone Tech', 'Tehnologia Cone Tech'), ('mișcare', 'favorizează mișcarea naturală a piciorului'), ('Always Dry', 'Branțuri Always Dry'),
   ('antibacterian', 'Protecție antibacteriană'), ('contrafort', 'Contrefort rigidizat'), ('interior', 'Căptușeala din material textil'),
   ('scai', 'Cureaua reglabilă cu scai'), ('detașabile', 'Branțuri detașabile'), ('sezon', 'activitățile de primăvară și vară'), ('talpă', 'Fabricată din cauciuc'),
   ('față', 'Partea superioară:Material sintetic, Material textil'), ('profilată', 'profilată')],
  {'Model': 'Biomecanics 262251', 'Talpă': 'cauciuc, Cone Tech', 'Caracteristici': 'Always Dry, antibacterian, curea cu scai', 'Cod produs': '262251'})

w(10041,
  f'<p>Geaca {A("/brand/elisabetta-franchi/", "Elisabetta Franchi")} EFGB129 roz este o {A(GF, "geacă de iarnă pentru fete")} izolată, din material catifelat cu viscoză și poliamidă, cu izolație sintetică medie spre groasă. Gluga se detașează, iar căptușeala e din poliamidă.</p>'
  '<p>Se închide cu fermoar și capsă, mânecile se termină cu elastic, iar jos are șnururi de strângere. Cele două buzunare laterale se închid prin apăsare. Mărimile sunt italienești, raportate la cele europene.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '75% viscoză, 25% poliamidă.'), ('Umplutură', '100% poliester.'), ('Lungime', '52 cm la mărimea 140.'))
  + '<p>Mărimile 140-158 corespund, orientativ, vârstei de 10-13 ani.</p>',
  [('cod', 'EFGB129'), ('culoare', 'culoarea roz'), ('izolat', 'Model izolat confecționat din material catifelat'), ('groasă', 'medie, groasă'),
   ('glugă', 'Gluga detasabila'), ('căptușeală', '100% Poliamida'), ('fermoar', 'Fixare cu fermoar si snap'), ('mâneci', 'Mâneci finisate cu o coadă elastică'),
   ('șnur', 'Jos snururi'), ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'),
   ('italian', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('material', '75% Viscoza, 25% Poliamida'), ('umplutură', '100% Poliester'),
   ('lungime', 'Lungimea: 52 cm'), ('mărime', '140 cm')],
  {'Model': 'Elisabetta Franchi EFGB129', 'Material': '75% viscoză, 25% poliamidă', 'Caracteristici': 'catifelată, glugă detașabilă, șnur jos', 'Cod produs': 'EFGB129.C.NY295'})

w(10042,
  f'<p>Pantofii {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} T3X5-34130 negri sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} din textil și piele ecologică, cu talpă groasă, plată, din cauciuc durabil și rezistent la deteriorare. Conțin materiale din fibre reciclate.</p>'
  '<p>Se închid cu fermoar în lateral și au o inserție elastică, deci se pun și se scot ușor. Vârful e rotund și întărit, spatele călcâiului e puternic rigidizat, iar interiorul e confortabil.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Lungime branț', '20,5 cm la numărul 33.'), ('Izolație', 'nu au.'))
  + '<p>Numerele 30-34 sunt pentru copii de cam 6-11 ani.</p>',
  [('cod', 'T3X5-34130'), ('culoare', 'culoarea negru'), ('piele', 'combinația materialului textil cu pielea ecologică'), ('groasă', 'groasă, plată'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('reciclat', 'Produsul contine materiale realizate din fibre reciclate'),
   ('fermoar', 'Închidere cu fermoar în lateral'), ('elastic', 'Model cu insetie elastica'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Spatele calcaiului peternic rigidizat'),
   ('interior', 'Interior confortabil'), ('gambă', 'Material sintetic, Material textil'), ('lungime', 'Lungimea brantului pentru marimea este de: 20,5 cm'),
   ('mărime', 'Dimensiunile date pentru marimea: 33'), ('neizolat', 'Izolare: neizolat')],
  {'Model': 'Tommy Hilfiger T3X5-34130', 'Talpă': 'cauciuc, groasă', 'Caracteristici': 'fermoar lateral, inserție elastică, vârf întărit', 'Cod produs': 'T3X5.34130'})

w(10052,
  f'<p>Paltonul {A("/brand/michael-kors/", "Michael Kors")} R30454 maro e listat la {A(GF, "geci pentru fete")} și e făcut dintr-un material cu mult conținut de lână, care apără de frig, iar poliesterul adăugat îl face mai rezistent la șifonare. E subțire, neizolat, cu căptușeală completă.</p>'
  '<p>Tăietura e simplă, se închide cu buton, iar pe laterale are două buzunare. Magazinul precizează că nu e impermeabil, deci e mai potrivit pentru zilele uscate de toamnă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '43% poliester, 33% lână, 19% acril, 4% poliamidă, 1% viscoză.'), ('Căptușeală', '100% poliester.'), ('Închidere', 'buton.'))
  + '<p>Mărimile 138-150 se potrivesc orientativ copiilor de 10-12 ani.</p>',
  [('cod', 'R30454'), ('culoare', 'culoarea maro'), ('palton', 'Palton copii din colecția Michael Kors'), ('lână', 'material cu un conținut ridicat de lână, care oferă protecție împotriva frigului'),
   ('șifonare', 'adăugarea de poliester crește rezistența la șifonare'), ('subțire', 'Model subțire'), ('neizolat', 'Model neizolat cu captuseala'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('buton', 'Închiderea convenabilă cu buton'), ('buzunare', 'Două buzunare laterale'), ('impermeabil', 'fără impermeabilitate'),
   ('material', '43% Poliester , 33% Lana, 19% Acril, 4% Poliamida, 1% Viscoza'), ('căptușeală', '100% Poliester')],
  {'Model': 'Michael Kors R30454', 'Material': '43% poliester, 33% lână', 'Caracteristici': 'palton subțire, buton, buzunare laterale', 'Cod produs': 'R30454'},
  notes=['Atributele spun „cu glugă”, caracteristicile „fără glugă”; nu am scris despre glugă. „Toamnă” e dedus din „neizolat”.'])

w(10065,
  f'<p>Codul {PRIMIGI} 8883711 roz, în numerele mai mari, este o pereche de {A("/categorie/ghete-cizme/", "cizme de iarnă pentru fete")} ușor izolate, din textil, piele naturală și piele întoarsă, cu membrană GORE-TEX subțire, rezistentă la vânt și respirabilă. Talpa are punctul Primitor Shock Absorber, care preia șocurile la pas.</p>'
  '<p>Carâmbul înalt ține glezna fermă pe teren denivelat. Vârful e rotund, ușor întărit, contrafortul rigid nu lasă piciorul să alunece, iar velcro-ul ajută la încălțat. Talpa exterioară din cauciuc e antiderapantă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele naturală, piele întoarsă.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 31-35 se potrivesc orientativ copiilor de 6-11 ani.</p>',
  [('cod', '8883711'), ('culoare', 'culoarea roz'), ('izolat', 'Izolare: usor izolat'), ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire'),
   ('vânt', 'rezistenta la vant si respirabila'), ('Shock', 'Primitor Shock Absorber - o talpa cu punct de absorbtie a socurilor'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('vârf', 'Cutie rotunda, usor intarita'), ('călcâi', 'ține piciorul în pantof, astfel încât să nu alunece'),
   ('velcro', 'Închiderea cu velcro'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('antiderapantă', 'antiderapantă'),
   ('gambă', 'Material textil, Piele naturala, Piele intoarsa'), ('profil', 'înalt')],
  {'Model': 'Primigi 8883711', 'Membrană': 'GORE-TEX', 'Caracteristici': 'Primitor Shock Absorber, velcro, profil înalt', 'Cod produs': '8883711'},
  notes=[NOAPA])

w(10067,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IG0IG02976 gri este o {A(GF, "geacă de iarnă pentru fete")} izolată, din material neted cu izolație sintetică medie spre groasă, din fibre reciclate. Croiala e cambrată, pe talie.</p>'
  '<p>Se închide cu fermoar, are guler ridicat și glugă integrată, iar o curea e prinsă de geacă. Pe laterale are două buzunare, iar căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material 1', '100% poliamidă reciclată.'), ('Material 2', '100% poliester reciclat.'), ('Croială', 'cambrată.'))
  + '<p>Pe mărimi, 128-170 acoperă aproximativ intervalul 8-15 ani.</p>',
  [('cod', 'IG0IG02976'), ('culoare', 'culoarea gri'), ('izolat', 'Model izolat confecționat din material neted cu izolație sintetică'), ('groasă', 'medie, groasă'),
   ('reciclat', 'Produsul contine materiale realizate din fibre reciclate'), ('cambrat', 'Croială: cambrat'), ('fermoar', 'Are închidere cu fermoar și guler ridicat'),
   ('glugă', 'integrată'), ('curea', 'Curea atasata'), ('buzunare', 'Două buzunare laterale'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('material1', '100% Poliamida reciclata'), ('material2', '100% Poliester reciclat')],
  {'Model': 'Calvin Klein Jeans IG0IG02976', 'Material': 'poliamidă și poliester reciclate', 'Caracteristici': 'izolată, croială cambrată, curea', 'Cod produs': 'IG0IG02976'})

w(10081,
  f'<p>Același model {A("/brand/mini-rodini/", "Mini Rodini")} Ritzratz, aici în violet, ca {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} matlasată, cu izolație sintetică groasă și croială supradimensionată. E făcută din poliester reciclat, cu BIONIC-FINISH ECO și acoperire PFC Repellent pentru rezistență la apă.</p>'
  '<p>Fermoarul pe toată lungimea are clapă de furtună prinsă cu capse, gluga se detașează, iar umerii sunt coborâți. Mânecile și marginea de jos au bătături contra vremii urâte, iar pe laterale sunt două buzunare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Croială', 'supradimensionată.'), ('Căptușeală', 'completă, sintetică.'))
  + '<p>Mărimile 80-86 până la 140-146 se potrivesc orientativ copiilor de 1-11 ani.</p>',
  [('model', 'Ritzratz'), ('culoare', 'culoarea violet'), ('matlasat', 'Model izolat confecționat din material matlasat'), ('groasă', 'groasă'),
   ('supradimensionat', 'Croială: supradimensionat'), ('reciclat', 'Acest produs este fabricat din poliester reciclat'), ('BIONIC', 'BIONIC-FINISH® ECO'),
   ('PFC', 'acoperire ecologica PFC Repellent'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă de furtună prinsă cu capse'),
   ('glugă', 'gluga detașabilă'), ('umeri', 'linie coborâtă a umerilor'), ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'),
   ('buzunare', 'Două buzunare laterale'), ('material', '100% Poliester reciclat'), ('căptușeală', 'cu căptușeală completă, sintetică')],
  {'Model': 'Mini Rodini Ritzratz', 'Material': '100% poliester reciclat', 'Caracteristici': 'matlasată, oversize, glugă detașabilă', 'Cod produs': '25710104'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă. Produsul e marcat și „pentru bebe”.'])

w(10086,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8858933 roz, pentru cei mici, sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} ușor izolate, din textil și piele naturală. Membrana Gore-Tex are porii mai mici decât picăturile de apă, dar mai mari decât vaporii, așa că le face rezistente la vânt și respirabile.</p>'
  '<p>Talpa Primitor Shock Absorber preia șocurile, iar banda de rulare e antiderapantă. Vârful rotund e moale, partea de sus ridicată ține glezna, iar velcro-ul și bucla de la spate ajută la încălțat. Interiorul textil se curăță ușor.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele naturală.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Numerele 25-29 se poartă cam pe la 2-5 ani.</p>',
  [('cod', '8858933'), ('culoare', 'culoarea roz'), ('izolat', 'Model Izolare ușoară din combinația materialului textil cu pielea naturală'),
   ('Gore-Tex', 'Acoperirea Gore-Tex® are găuri mai mici decât picăturile de apă, dar mai mari decât o moleculă de vapori de apă'),
   ('Shock', 'Primitor Shock Absorber'), ('antiderapantă', 'absorbție a șocurilor, cu bandă de rulare, antiderapantă'), ('vârf', 'Varf rotund'), ('moale', 'moale'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('velcro', 'Închiderea cu velcro'), ('buclă', 'Bucla de la spate'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('gambă', 'Material textil, Piele naturala'), ('profil', 'înalt')],
  {'Model': 'Primigi 8858933', 'Membrană': 'Gore-Tex', 'Caracteristici': 'Primitor Shock Absorber, velcro, vârf moale', 'Cod produs': '8858933'})

w(10100,
  f'<p>Geaca bomber {A("/brand/guess/", "GUESS")} L5YL08 bleumarin este o {A(GB, "geacă de tranziție pentru băieți")} neizolată și fără căptușeală, din material neted. Gulerul ridicat apără de frig, iar mânecile și marginea de jos se termină cu elastic, ca la orice bomber.</p>'
  '<p>Tăietura e simplă, se închide cu fermoar și are două buzunare laterale. E o geacă subțire, pentru zilele mai blânde.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'nu are.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile de la 122-125 la 175 sunt pentru copii de cam 7-16 ani.</p>',
  [('cod', 'L5YL08'), ('culoare', 'culoarea albastru marin'), ('bomber', 'Geaca bomber din colectia Guess'), ('neizolat', 'Model neizolat confectionat din material neted'),
   ('căptușeală', 'fără căptușeală'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare laterale'), ('material', '100% Poliester'),
   ('umplutură', 'fără umplutură'), ('croială', 'Croială: regular fit')],
  {'Model': 'GUESS L5YL08', 'Material': '100% poliester', 'Caracteristici': 'bomber, neizolată, guler ridicat', 'Cod produs': 'L5YL08.WH762'})

w(10131,
  f'<p>Geaca {A("/brand/ea7-emporio-armani/", "EA7 Emporio Armani")} 7B000233 bleumarin este o {A(GB, "geacă de iarnă pentru băieți")} izolată, din poliamidă rezistentă, cu izolație sintetică medie spre groasă. Gulerul ridicat și gluga fixă apără de frig, iar orificiile de aerisire ajută la respirabilitate.</p>'
  '<p>Fermoarul pe toată lungimea are clapă interioară împotriva furtunii, mânecile și marginea de jos au bătături, iar cele două buzunare laterale au fermoar. Magazinul precizează că nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă.'), ('Umplutură', '100% poliester.'), ('Lungime', '64,5 cm la mărimea 164.'))
  + '<p>Mărimile 142-176 se potrivesc orientativ copiilor de 10-16 ani.</p>',
  [('cod', '7B000233'), ('culoare', 'culoarea bleumarin'), ('izolat', 'Model izolat confecționat din material rezistent'), ('groasă', 'medie, groasă'),
   ('guler', 'Gulerul ridicat și gluga fixă'), ('aerisire', 'Modelul are orificii de aerisire care asigură o mai mare respirabilitate'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară împotriva furtunii'), ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('impermeabil', 'fără impermeabilitate'), ('material', '100% Poliamida'), ('umplutură', '100% Poliester'),
   ('lungime', 'Lungimea: 64,5 cm'), ('mărime', '164 cm')],
  {'Model': 'EA7 Emporio Armani 7B000233', 'Material': '100% poliamidă', 'Caracteristici': 'izolată, orificii de aerisire, glugă fixă', 'Cod produs': '7B000233'})
