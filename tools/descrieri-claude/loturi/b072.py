import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(12670,
  f'<p>Pentru copiii mai mici, modelul {TH} T1X9-35219 vine și în numerele 24-29: {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} bleumarin, cu profil jos, din imitație de piele rezistentă, care se șterge ușor. Aricii permit încălțatul rapid, fără ajutor.</p>'
  '<p>Profilul jos lasă glezna liberă, iar călcâiul întărit ține piciorul drept la joacă. Culoarea bleumarin se poartă ușor cu multe haine.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil moale.'), ('Branț', 'textil.'), ('Talpă', 'plată, din cauciuc, ține bine pe sol.'))
  + '<p>Numerele acestea se potrivesc copiilor de aproximativ 2-5 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bleumarin T1X9-35219'), ('profil', 'Profil jos al feței superioare permite libertatea de mișcare a gleznei'),
   ('imitație', 'Imitație de piele rezistentă la nivelul feței superioare facilitează menținerea curățeniei'), ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă'),
   ('călcâi', 'Călcâi întărit contribuie la stabilizarea piciorului'), ('interior', 'Material textil moale în interiorul pantofului'), ('branț', 'Branț textil'), ('culoare', 'Cromatică universală bleumarin face ca încălțămintea să fie ușor de asortat'),
   ('talpă', 'Talpă de cauciuc, plată oferă o bună aderență la sol')],
  {'Model': 'Tommy Hilfiger T1X9-35219', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, profil jos', 'Cod produs': 'T1X9-35219'})

w(12673,
  f'<p>{GEOX} GISLI B461ME sunt {A("/categorie/adidasi/", "adidași pentru fete")} bej, înalți, cu gulerul ușor întărit care susține glezna, din imitație de piele și material textil. Branțul din lână ține piciorul la o temperatură potrivită, iar tehnologia Geox Respira scoate umezeala.</p>'
  '<p>Aricii fac încălțatul și descălțatul rapid, iar călcâiul întărit ține piciorul pe loc la mers.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Interior', 'textil și lână.'), ('Talpă exterioară', 'din cauciuc, cu profil plat.'), ('Închidere', 'arici.'))
  + '<p>Mărimile 24-27 sunt pentru fete de în jur de 2-4 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii bej B461ME.0AUAJ'), ('înalt', 'Profilul înalt al carâmbului cu gulerul ușor întărit susține glezna copilului'),
   ('material', 'Combinația de imitație de piele și material textil'), ('lână', 'Branțul din lână ajută la menținerea temperaturii optime'),
   ('Respira', 'Tehnologia Geox Respira™ favorizează eliminarea umidității'), ('arici', 'Sistemul practic de închidere cu arici'), ('călcâi', 'Călcâiul întărit'),
   ('interior', 'Material textil, Lână'), ('talpă', 'Talpa exterioară din cauciuc se caracterizează printr-un profil plat')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior textil cu lână, talpă din cauciuc', 'Caracteristici': 'Geox Respira, branț din lână, arici, profil înalt', 'Cod produs': 'B461ME.0AUAJ'})

w(12675,
  f'<p>{REIMA} Enkkari violet sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} sport-casual, cu tehnologia ReimaTec: membrană PU și cusături lipite, care țin umezeala afară. Vârful lat lasă degetele să se așeze liber, iar fața e din materiale textile și sintetice.</p>'
  '<p>Aricii cu inserție elastică și buclele permit încălțatul rapid, chiar de către copil.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Branțuri Happy Fit', 'detașabile, pentru verificarea mărimii.'), ('Interior', 'textil și sintetic.'), ('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'ușor întărit.'))
  + '<p>Numerele 28-38 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'Reima Enkkari sneakers pentru copii violet 5400152C'), ('stil', 'stilul casual și sport'), ('ReimaTec', 'Tehnologia ReimaTec – membrana PU și cusăturile lipite contribuie la protecția împotriva umezelii'),
   ('vârf', 'Vârf lat – permite așezarea liberă a degetelor'), ('față', 'elemente textile și sintetice creează o construcție durabilă'),
   ('arici', 'Închidere cu arici și inserție elastică'), ('bucle', 'Bucle practice – facilitează încălțarea și descălțarea autonomă'),
   ('Happy Fit', 'Branțuri detașabile Happy Fit – facilitează verificarea mărimii'), ('interior', 'Interior din materiale sintetice și textile'),
   ('talpă', 'Talpă plată din cauciuc'), ('călcâi', 'Călcâi ușor întărit')],
  {'Model': 'Reima Enkkari', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'ReimaTec, cusături lipite, arici, branțuri Happy Fit', 'Cod produs': '5400152C'})

w(12680,
  f'<p>Vesta {A("/brand/columbia/", "Columbia")} Puffect roz este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "vestă unisex")} matlasată, cu umplutură sintetică medie, pentru zilele de tranziție. Tratamentul Omni-Shield și impregnarea hidrofobă țin la distanță ploaia ușoară și murdăria, iar țesătura Ripstop oprește întinderea rupturilor.</p>'
  '<p>Se închide cu fermoar pe toată lungimea și ajunge până la șolduri. Croiala e regulară.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'laterale, cu fermoar.'), ('Căptușeală', 'completă, din nailon.'), ('Material', '100% poliester, umplutură din poliester.'))
  + '<p>Mărimile 116-164 sunt pentru copii de cam 6-14 ani.</p>',
  [('model', 'Columbia Vestă pentru copii Puffect roz 2090602'), ('matlasat', 'Țesătură matlasată durabilă'), ('umplutură', 'Umplutură sintetică medie'),
   ('tranziție', 'zilele de tranziție'), ('Omni-Shield', 'Tehnologia Omni-Shield™ – un strat hidrofob special pe țesătură ajută la protejarea împotriva umezelii și a murdăriei'),
   ('ploaie', 'un strat suplimentar contribuie la protecția împotriva ploilor ușoare'), ('Ripstop', 'Construcția Ripstop'), ('rupturi', 'limitează răspândirea rupturilor'),
   ('fermoar', 'fermoarul pe toată lungimea'), ('lungime', 'Lungime până la șolduri'), ('croială', 'Croială regulară'), ('buzunare', 'buzunarele cu fermoar'),
   ('căptușeală', '100% Nailon'), ('material', '100% Poliester')],
  {'Model': 'Columbia Puffect', 'Material': '100% poliester, căptușeală din nailon, umplutură din poliester', 'Caracteristici': 'Omni-Shield, Ripstop, fermoar, buzunare cu fermoar', 'Cod produs': '2090602'})

w(12682,
  f'<p>{GEOX} LOFTUS sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, din imitație de piele și material textil, în stil casual. Membrana microporoasă patentată ține apa afară, iar GEOX Respira scoate umezeala spre exterior.</p>'
  '<p>Șireturile elastice cu arici fac încălțatul rapid și îl lasă pe copil să se descurce singur. Talpa din spumă e ușoară și moale la pas.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Călcâi', 'întărit.'), ('Partea de sus', 'imitație de piele și textil.'))
  + '<p>Numerele 24-27 sunt gândite pentru băieți de aproximativ 2-4 ani.</p>',
  [('model', 'Geox LOFTUS sneakers pentru copii bleumarin J66MQA.0FU54'), ('material', 'Partea superioară din imitație de piele și material textil'), ('stil', 'stilul casual'),
   ('membrană', 'Membrană microporoasă patentată, care protejează interiorul pantofului de apă'), ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală a piciorului, eliminând umezeala la exterior'),
   ('închidere', 'Șireturi elastice cu arici , care facilitează încălțarea și descălțarea rapidă, încurajând autonomia'), ('talpă', 'Talpă din spumă , care contribuie la lejeritatea încălțămintei'),
   ('căptușeală', 'Căptușeală moale din material textil'), ('călcâi', 'Călcâi întărit')],
  {'Model': 'Geox LOFTUS', 'Material': 'imitație de piele și textil, interior textil, talpă din spumă', 'Caracteristici': 'Geox Respira cu membrană, șireturi elastice cu arici', 'Cod produs': 'J66MQA.0FU54'})

w(12683,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IG0IG02056 verde este o {A("/categorie/geci-jachete/", "geacă pentru fete")} izolată, cu căptușeală, din material neted, făcută integral din poliester reciclat. Izolația sintetică ține de cald la temperaturi mai scăzute.</p>'
  '<p>Gulerul ridicat și gluga fixă apără de frig, iar mânecile și tivul au margine elastică, care ține vântul afară. Se închide cu fermoar, deci se îmbracă repede.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Croială', 'simplă, dreaptă.'), ('Căptușeală', 'da, cu izolație sintetică.'))
  + '<p>Mărimile 128-176 sunt pentru fete de cam 8-16 ani.</p>',
  [('model', 'Calvin Klein Jeans Geaca copii culoarea verde, IG0IG02056'), ('izolat', 'Izolare: izolat'), ('căptușeală', 'Captuseala: cu captuseala'), ('neted', 'material neted'),
   ('reciclat', 'Acest produs este fabricat din poliester reciclat'), ('izolație', 'izolatie sintetica, care va oferi un confort suplimentar la temperaturi mai reci'),
   ('glugă', 'Gulerul ridicat și gluga fixă'), ('margini', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('fermoar', 'Incheiere cu fermoar'),
   ('material', '100% Poliester reciclat'), ('croială', 'Tăiere simplă, fără blocare')],
  {'Model': 'Calvin Klein Jeans IG0IG02056', 'Material': '100% poliester reciclat, izolație sintetică', 'Caracteristici': 'glugă fixă, guler ridicat, fermoar', 'Cod produs': 'IG0IG02056'})

w(12684,
  f'<p>Adidașii {TH} T3X9-35233 albi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt și șiret, din imitație de piele, pentru copiii mai mari. Șiretul permite o strângere precisă pe picior, iar gulerul ușor întărit e confortabil în jurul gleznei.</p>'
  '<p>Talpa din cauciuc, cu profil plat și grosime de 2-4 cm, izolează bine de sol. Călcâiul întărit ține piciorul în pantof.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Interior', 'căptușit cu textil.'), ('Branț', 'material textil.'), ('Partea de sus', 'material sintetic.'))
  + '<p>Numerele 35-41 se potrivesc copiilor de la aproximativ 10 ani în sus.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii albi T3X9-35233'), ('profil', 'Profilul scurt al încălțămintei'), ('imitație', 'Partea superioară din imitație de piele'),
   ('șiret', 'Închiderea cu șiret permite ajustarea precisă'), ('guler', 'Gulerul ușor întărit al părții superioare contribuie la confortul din jurul gleznei'),
   ('talpă', 'Talpa din cauciuc cu profil plat'), ('grosime', 'Grosimea tălpii în intervalul 2-4 cm permite o izolare adecvată față de sol'), ('călcâi', 'Călcâiul întărit'),
   ('interior', 'Interior căptușit cu material textil'), ('branț', 'Branț din material textil')],
  {'Model': 'Tommy Hilfiger T3X9-35233', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'șiret, profil scurt, guler întărit', 'Cod produs': 'T3X9-35233'})

w(12686,
  f'<p>{GEOX} INEK sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albaștri, înalți, cu lumini încorporate, din imitație de piele și material textil, pentru ținute casual. Membrana microporoasă ține apa afară, iar GEOX Respira scoate umezeala prin talpă.</p>'
  '<p>Șireturile elastice și aricii fac încălțatul rapid, iar profilul înalt sprijină glezna la mișcare. Talpa plată din cauciuc ține bine pe diverse suprafețe.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Interior', 'sintetic și textil, moale.'), ('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 28-31 merg la băieți de în jur de 4-7 ani.</p>',
  [('model', 'Geox INEK sneakers pentru copii albaștri J669CD.01454'), ('înalt', 'sneakerși înalți pentru băieți'), ('lumini', 'Lumini încorporate adaugă atractivitate'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('casual', 'stilizări casual'),
   ('membrană', 'O membrană microporoasă specială protejează interiorul pantofului împotriva pătrunderii apei'), ('Respira', 'Tehnologia GEOX Respira™ favorizează respirabilitatea tălpii, eliminând umezeala spre exterior'),
   ('închidere', 'Șireturi elastice și închidere cu arici facilitează încălțarea rapidă'), ('profil', 'Profilul înalt al părții superioare oferă suport suplimentar pentru gleznă'),
   ('interior', 'Interiorul din material sintetic și textil'), ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa plată din cauciuc susține stabilitatea și aderența pe diverse suprafețe')],
  {'Model': 'Geox INEK', 'Material': 'imitație de piele și textil, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'lumini încorporate, Geox Respira cu membrană, șireturi elastice și arici', 'Cod produs': 'J669CD.01454'})

w(12687,
  f'<p>Salopeta {REIMA} Mjosa bleumarin este o {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopetă unisex")} din softshell tehnic, pentru joaca afară în sezonul de tranziție. Membrana are 10000 mm H2O, stratul hidrorepelent face apa să se scurgă, iar softshell-ul oprește vântul.</p>'
  '<p>Umplutura sintetică ușoară și căptușeala din polar țin de cald. Gluga se detașează și are șnururi de reglat.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Benzi', 'reglabile pentru picior, ca să nu urce cracii.'), ('Buzunare', 'cu fermoar.'), ('Reflectorizante', 'pentru întuneric.'), ('Material', 'rezistent la murdărie.'))
  + '<p>Mărimile 74-98 sunt pentru copii de la aproximativ 9 luni până pe la 3 ani.</p>',
  [('model', 'Reima Salopetă pentru copii Mjosa bleumarin 5100006D'), ('softshell', 'confecționat din softshell tehnic'), ('aer liber', 'joaca liberă în aer liber'),
   ('tranziție', 'anotimpurilor de tranziție'), ('membrană', 'Membrană impermeabilă (10000 mm H2O)'), ('hidrorepelent', 'Strat hidrorepelent susține scurgerea apei'),
   ('vânt', 'Construcție softshell rezistentă la vânt'), ('polar', 'Umplutură sintetică ușoară și căptușeală din polar'), ('glugă', 'Glugă detașabilă și șnururi reglabile'),
   ('benzi', 'benzi reglabile pentru picior'), ('buzunare', 'Buzunare practice cu fermoar'), ('reflectorizant', 'Detalii reflectorizante'),
   ('murdărie', 'Material rezistent la murdărie')],
  {'Model': 'Reima Mjosa', 'Material': 'softshell 92% poliester și 8% elastan, căptușeală din polar', 'Caracteristici': '10000 mm H2O, glugă detașabilă, benzi pentru picior', 'Cod produs': '5100006D'},
  varsta_txt='9 luni - 3 ani')

w(12689,
  f'<p>{GEOX} CIUFCIUF B455QB sunt {A("/categorie/adidasi/", "adidași pentru fete")} bej pe site (violet la magazin), cu profil jos, din material textil, piele întoarsă și piele naturală, care se închid cu velcro. Sistemul Check Your Feet ajută la verificarea mărimii.</p>'
  '<p>Vârful rotund, ușor rigid, lasă degetele libere, iar contrafortul rigidizat sprijină călcâiul. Talpa din spumă e moale la pas.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Inserție', 'textilă, detașabilă, ușor de curățat.'), ('Interior', 'material textil.'))
  + '<p>Numerele 20-23 merg la fetițe de cam 1-3 ani; la 23 branțul are 13 cm.</p>',
  [('model', 'Geox Sneakers pentru copii CIUFCIUF culoarea bej, B455QB.0FU22'), ('culoare', 'Culoare violet'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinație de material textil, piele întoarsă și piele naturală'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('Check', 'Check Your Feet ajuta la ajustarea pantofilor'), ('vârf', 'Degetul rotund, ușor rigid'), ('călcâi', 'Contorul de călcâi rigidizat'),
   ('talpă', 'Talpa din spumă oferă o senzație mai moale'), RESPIRA, ('inserție', 'Inserție textilă detașabilă, ușor de curățat'),
   ('interior', 'Un model cu interior textil'), ('lungime', 'Lungimea brantului pentru marimea este de: 13 cm')],
  {'Model': 'Geox CIUFCIUF', 'Material': 'textil, piele întoarsă și piele naturală, interior textil, talpă din spumă', 'Caracteristici': 'velcro, Check Your Feet, Geox Respira', 'Cod produs': 'B455QB.0FU22'},
  notes=['Titlul spune bej, magazinul dă culoarea violet; am scris ambele.'])
