import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(13223,
  f'<p>Pentru fetele mai mari, bluza {TH} x Peanuts KS0KS00768 roșie vine în numerele 140-176: o {A("/categorie/bluze-tricouri-hanorace/", "bluză pentru fete")} cu mânecă lungă, din bumbac 100% moale și elastic, cu dungi și grafică Peanuts. Umerii coborâți și croiala lejeră o fac comodă la joacă.</p>'
  '<p>Decolteul are guler și închidere, ceea ce o face ușor de îmbrăcat. Stilul casual și streetwear se potrivește la multe ținute.</p>'
  '<p>Detaliile principale:</p>'
  + L(('Material', 'bumbac 100%, elastic.'), ('Croială', 'lejeră, umeri coborâți.'), ('Model', 'dungi, grafică Peanuts.'))
  + '<p>Se potrivește fetelor de aproximativ 10-16 ani.</p>',
  [('model', 'Tommy Hilfiger Longsleeve pentru copii din bumbac x Peanuts roșu KS0KS00768'), ('bumbac', 'Confecționat din bumbac 100% moale'), ('elastic', 'Material elastic'),
   ('dungi', 'Model în dungi și grafica Peanuts®'), ('croială', 'Croială lejeră cu linia umerilor coborâtă'), ('decolteu', 'Decolteu cu guler și închidere'),
   ('stil', 'Design în stil casual și streetwear'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger x Peanuts KS0KS00768', 'Material': '100% bumbac', 'Caracteristici': 'dungi, grafică Peanuts, guler cu închidere', 'Cod produs': 'KS0KS00768'})

w(13224,
  f'<p>În roz, hanoracul {TH} KG0KG09604 e același {A("/categorie/bluze-tricouri-hanorace/", "hanorac pentru fete")} tras pe cap, fără închidere, tricotat din bumbac plăcut la atingere. Pe față are un logo mic, iar materialul e uni.</p>'
  '<p>Fiindcă nu are căptușeală, rămâne lejer. Manșetele și baza au borduri elastice, iar decolteul rotund își ține forma.</p>'
  '<p>Ce trebuie știut:</p>'
  + L(('Compoziție', 'bumbac 100%.'), ('Mâneci', 'lungi, cu manșete elastice.'), ('Croială', 'simplă.'))
  + '<p>Numerele 128-176 merg la fete de pe la 8 până pe la 16 ani.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii din bumbac roz KG0KG09604'), ('închidere', 'Fasonul fără închidere cu decolteu rotund facilitează îmbrăcarea și dezbrăcarea rapidă'),
   ('tricot', 'Tricotajul din bumbac este respirabil și plăcut la atingere'), ('logo', 'Materialul uni cu un logo subtil al brandului în față'),
   ('căptușeală', 'Lipsa căptușelii contribuie la lejeritatea construcției'), ('borduri', 'Bordurile elastice de la bază și de la manșete ajută la menținerea formei'),
   ('decolteu', 'Decolteul rotund finisat cu bordură elastică ajută la menținerea formei'), ('mâneci', 'Mânecile lungi clasice finisate cu manșete elastice'),
   ('croială', 'Croiala simplă a modelului'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG09604', 'Material': '100% bumbac', 'Caracteristici': 'fără închidere, decolteu rotund, logo', 'Cod produs': 'KG0KG09604'})

w(13235,
  f'<p>Modelul {BIO} 261163 în gri: {A("/categorie/adidasi/", "adidași pentru fete")} din piele naturală combinată cu imitație de piele, făcuți împreună cu podologi pentru joaca de fiecare zi. Vârful e mai larg, ca degetele să stea liber, iar talpa de cauciuc se îndoaie după picior.</p>'
  '<p>Închiderea e cu arici pe o curea reglabilă. Un stabilizator lateral și călcâiul întărit țin piciorul drept, iar gulerul moale nu roade.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Branț', 'antibacterian.'), ('Căptușeală', 'textilă, moale.'), ('Podology', 'tehnologie Biomecanics.'))
  + '<p>Au rămas numerele 24-26, pentru 2-4 ani, cu aproximație.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele gri 261163'), ('material', 'Partea superioară dintr-o combinație de piele naturală și imitație de piele'),
   ('podologi', 'creată în colaborare cu podologi'), ('zilnic', 'activitățile și jocurile de zi cu zi'), ('vârf', 'Spațiu mărit în vârful pantofului'),
   ('talpă', 'Talpă flexibilă din cauciuc'), ('arici', 'Închidere practică cu arici , cu o curea reglabilă'), ('stabilizator', 'Stabilizator lateral în încălțăminte'),
   ('călcâi', 'Călcâi întărit'), ('guler', 'Gulerul superior moale , minimizează riscul de iritații'), ('branț', 'Branț antibacterian'),
   ('căptușeală', 'Căptușeală moale din material textil'), ('Podology', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261163', 'Material': 'piele naturală și imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, stabilizator lateral, branț antibacterian', 'Cod produs': '261163'})

w(13236,
  f'<p>{BIO} 261123 bleumarin sunt {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi pentru băieți")} din piele naturală, căptușiți cu lână, inclusiv branțurile detașabile, pentru zilele mai reci. Aricii fac încălțatul și descălțatul rapid, chiar de către copil.</p>'
  '<p>Talpa flexibilă din cauciuc lasă piciorul să se miște natural, iar stabilizatorul lateral și călcâiul întărit îl țin corect. Pielea se adaptează la forma piciorului.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Exterior', 'piele naturală.'), ('Interior', 'lână.'), ('Vârf', 'întărit și cauciucat.'))
  + '<p>Numerele 18-25 sunt pentru băieți de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte pentru copii din piele bleumarin 261123'), ('piele', 'Partea superioară din piele naturală contribuie la durabilitatea și estetica încălțămintei, adaptându-se formei piciorului'),
   ('lână', 'Căptușeală din lână în interiorul pantofului și în branțurile detașabile'), ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă'),
   ('talpă', 'Talpă flexibilă din cauciuc permite mișcarea naturală a piciorului'), ('stabilizator', 'Stabilizator lateral și călcâi întărit'),
   ('vârf', 'Vârf întărit și cauciucat protejează degetele'), ('interior', 'Lână')],
  {'Model': 'Biomecanics 261123', 'Material': 'piele naturală, căptușeală din lână, talpă din cauciuc', 'Caracteristici': 'căptușiți cu lână, arici, vârf cauciucat', 'Cod produs': '261123'})

w(13262,
  f'<p>Ghetele de iarnă {A("/brand/primigi/", "Primigi")} 23526 maro sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} înalte, pentru cei mici, din piele nubuc, cu membrană GORE-TEX care ține apa și vântul afară. Interiorul izolat termic ține de cald în zilele reci.</p>'
  '<p>Aricii fac încălțatul rapid, iar călcâiul întărit și vârful rigidizat țin piciorul în siguranță. Talpa plată din cauciuc ține bine pe diverse suprafețe.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Primigi × SIPeP', 'gândită după anatomia piciorului.'), ('Interior', 'textil, izolat.'))
  + '<p>Numerele 19-24 se potrivesc copiilor de cam 1-3 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii maro PBZGT 23526'), ('înalt', 'un model înalt de încălțăminte'), ('nubuc', 'Partea superioară din piele nubuc'),
   ('GORE-TEX', 'Membrană GORE-TEX® ajută la menținerea picioarelor uscate, blocând apa și vântul'), ('izolat', 'Interior izolat termic din material textil'),
   ('arici', 'Sistem de închidere cu arici'), ('călcâi', 'Călcâi întărit și vârf rigidizat'), ('talpă', 'Talpă plată din cauciuc oferă aderență pe diverse suprafețe'),
   ('SIPeP', 'Tehnologia Primigi × SIPeP ține cont de dezvoltarea piciorului copilului')],
  {'Model': 'Primigi 23526', 'Material': 'piele nubuc și sintetic, interior izolat, talpă din cauciuc', 'Caracteristici': 'GORE-TEX, arici, izolate termic', 'Cod produs': 'PBZGT 23526'})

w(13266,
  f'<p>{GEOX} IUPIDOO Batman sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, cu aplicație Batman, făcuți în colaborare cu Asociația Italiană de Podiatrie, din material textil și sintetic, ușori și rezistenți. Tehnologia patentată GEOX Respira scoate umezeala.</p>'
  '<p>Banda de rulare Flexy System lasă talpa să se îndoaie natural, iar suportul pentru gleznă și vârful și călcâiul întărite apără piciorul. Aricii fac încălțatul rapid.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'piele naturală și textil.'), ('Talpă', 'din cauciuc.'), ('Închidere', 'arici.'))
  + '<p>Numerele 18-26 se potrivesc băieților de aproximativ 1-4 ani.</p>',
  [('model', 'Geox IUPIDOO Batman sneakers pentru copii negri B6655B.000BC'), ('Batman', 'Aplicația cu motivul Batman'), ('podiatrie', 'Asociația Italiană de Podiatrie'),
   ('material', 'Partea superioară din material textil și sintetic contribuie la lejeritate și durabilitate'), ('Respira', 'Tehnologia patentată GEOX Respira™ favorizează eliminarea umezelii'),
   ('Flexy', 'Banda de rulare Flexy System sprijină elasticitatea naturală a tălpii'), ('gleznă', 'Suportul pentru gleznă'), ('întărit', 'Vârfurile și călcâiele întărite'),
   ('arici', 'Închiderea practică cu arici'), ('căptușeală', 'Interiorul căptușit cu piele naturală și material textil'), ('talpă', 'Talpa din cauciuc sprijină aderența')],
  {'Model': 'Geox IUPIDOO Batman', 'Material': 'textil și sintetic, interior din piele și textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, Flexy System, arici, aplicație Batman', 'Cod produs': 'B6655B.000BC'})

w(13278,
  f'<p>{GEOX} NASHIK B465NA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albaștri, înalți, din piele naturală, piele întoarsă și material textil, pentru ținute de zi cu zi. Membrana microporoasă din talpă oprește apa, iar GEOX Respira scoate umezeala.</p>'
  '<p>Aricii fac încălțatul rapid, iar profilul înalt sprijină glezna. Branțul detașabil are imprimeu pentru verificarea mărimii, iar căptușeala din piele creează un microclimat bun.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'piele naturală și textil.'), ('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-27 sunt pentru băieți de cam 2-4 ani.</p>',
  [('model', 'Geox NASHIK sneakers pentru copii din piele albastri B465NA.0CL22'), ('culoare', 'Culoare albastru'), ('înalt', 'Profilul înalt al părții superioare oferă suport suplimentar pentru glezna copilului'),
   ('material', 'Partea superioară din piele naturală și piele întoarsă'), ('membrană', 'Membrana microporoasă din talpă protejează interiorul încălțămintei împotriva pătrunderii apei'),
   ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală a piciorului, eliminând umezeala spre exterior'), ('arici', 'Închiderea cu arici'),
   ('branț', 'Branțul detașabil cu imprimeu ajută la verificarea ușoară a mărimii corecte'), ('căptușeală', 'Interiorul căptușit cu piele naturală creează un microclimat adecvat'),
   ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa plată din cauciuc'), ('textil', 'Piele întoarsă, Piele naturală, Material textil')],
  {'Model': 'Geox NASHIK', 'Material': 'piele naturală, piele întoarsă și textil, interior din piele', 'Caracteristici': 'Geox Respira cu membrană, arici, profil înalt', 'Cod produs': 'B465NA.0CL22'})

w(13284,
  f'<p>Geaca bomber {A("/brand/donsje/", "Donsje")} 3048502 bleumarin este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} de tranziție, din tricot moale cu bumbac, cu mâneci raglan din țesătură matlasată și broderie cu aplicații decorative. Croiala regulară lasă copilul să se miște liber.</p>'
  '<p>Se închide cu capse, iar tivul are șnur elastic și manșetele au nervuri, care țin vântul afară.</p>'
  '<p>Materialele, pe rând:</p>'
  + L(('Corp', '57% bumbac, 43% poliester.'), ('Mâneci', '100% poliester, matlasate.'), ('Buzunare', 'laterale.'), ('Lungime', 'până la șolduri.'))
  + '<p>Mărimile 74-92 sunt pentru copii de aproximativ 9 luni - 2 ani.</p>',
  [('model', 'Donsje Geacă bomber pentru copii cu bumbac bleumarin 3048502'), ('tranziție', 'geacă de tranziție pentru copii'), ('tricot', 'Confecționată din tricot moale'),
   ('raglan', 'Mâneci raglan din țesătură matlasată'), ('broderie', 'Decorative aplicații și broderie'), ('croială', 'Croiala regulară permite mișcări libere'),
   ('capse', 'Sistemul de închidere cu capse'), ('tiv', 'Tivul cu șnur elastic'), ('manșete', 'Manșetele cu nervuri ajută la stabilizarea mânecilor și protejează împotriva vântului'),
   ('corp', '57% Bumbac, 43% Poliester'), ('mâneci', '100% Poliester'), ('buzunare', 'Buzunarele practice laterale'), ('lungime', 'Lungimea până la șolduri')],
  {'Model': 'Donsje 3048502 (bomber)', 'Material': '57% bumbac, 43% poliester, mâneci din poliester', 'Caracteristici': 'capse, mâneci raglan matlasate, broderie', 'Cod produs': '3048502'},
  varsta_txt='9 luni - 2 ani')

w(13289,
  f'<p>{GEOX} NASHIK B465NC bej sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} din piele naturală, piele întoarsă și material textil, cu talpa GEOX Respira cu membrană, care scoate umiditatea și ține apa afară. Gulerul ușor întărit cuprinde glezna fără să încurce.</p>'
  '<p>Aricii îl lasă pe copil să se încalțe singur. Branțul detașabil din piele are imprimeu pentru verificarea mărimii.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'piele, sintetic și textil.'), ('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-27 se potrivesc băieților de în jur de 2-4 ani.</p>',
  [('model', 'Geox NASHIK sneakers pentru copii din piele bej B465NC.0CL22'), ('material', 'Piele naturală, piele întoarsă și material textil'),
   ('Respira', 'Talpă cu membrană, care favorizează eliminarea umidității și protejează interiorul de apă'), ('guler', 'Îmbrățișează delicat glezna'),
   ('arici', 'Facilitează încălțarea și descălțarea independentă de către copil'), ('branț', 'Din piele, cu imprimeu pentru verificarea mărimii'),
   ('căptușeală', 'Căptușeală din piele, material sintetic și material textil'), ('călcâi', 'Susține stabilizarea piciorului'), ('talpă', 'Structură plată din cauciuc')],
  {'Model': 'Geox NASHIK', 'Material': 'piele naturală, piele întoarsă și textil, interior din piele', 'Caracteristici': 'Geox Respira cu membrană, arici, branț cu verificare de mărime', 'Cod produs': 'B465NC.0CL22'})

w(13301,
  f'<p>Același cod {GEOX} NASHIK B465NA, de data asta în bleumarin: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu gleznă înaltă, cu fața din piele naturală și piele întoarsă combinate cu textil. Talpa are membrană microporoasă, iar sistemul GEOX Respira elimină umezeala spre exterior.</p>'
  '<p>Încălțatul se face din arici, fără ajutor. Pe dinăuntru e căptușit cu piele naturală.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Branț', 'detașabil, cu imprimeu pentru mărime.'), ('Călcâi', 'întărit, pentru siguranță.'), ('Talpă', 'cauciuc plat.'))
  + '<p>Mărimile 24-27 sunt gândite pentru 2-4 ani, orientativ.</p>',
  [('model', 'Geox NASHIK sneakers pentru copii din piele bleumarin B465NA.0CL22'), ('înalt', 'Profilul înalt al părții superioare oferă suport suplimentar'),
   ('material', 'Partea superioară din piele naturală și piele întoarsă'), ('textil', 'Piele întoarsă, Piele naturală, Material textil'),
   ('membrană', 'Membrana microporoasă din talpă protejează interiorul încălțămintei împotriva pătrunderii apei'), ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală a piciorului, eliminând umezeala către exterior'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă de către copil'), ('căptușeală', 'Interiorul căptușit cu piele naturală'),
   ('branț', 'Branțul detașabil cu imprimeu ajută la verificarea ușoară a mărimii corecte'), ('călcâi', 'Călcâiul întărit stabilizează piciorul, contribuind la siguranță'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox NASHIK', 'Material': 'piele naturală, piele întoarsă și textil, interior din piele', 'Caracteristici': 'Geox Respira cu membrană, arici, profil înalt', 'Cod produs': 'B465NA.0CL22'})
