import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
NIKE = A('/brand/nike/', 'Nike')

# 4877: descrierea din b001 lipsea din content/descrieri (reluată identic)
w(4877,
  f'<p>{NIKE} JDB ESS DRAFT JACKET este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă ușoară pentru băieți")}, albastră cu negru, din nailon cu suprafață țesută netedă. Magazinul o recomandă pentru activități în aer liber, precum drumețiile, în sezonul primăvară-vară.</p>'
  '<p>Croiala e clasică, iar manșetele și betelia elastică strâng geaca la încheieturi și în talie, așa că stă aproape de corp și pe un copil mai slab.</p>'
  '<p>Pentru o geacă de purtat la drum, detaliile sunt practice:</p>'
  + L(('Glugă', 'atașată, nu se scoate.'), ('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, cu fermoare ascunse.'), ('Design', 'panouri în contrast pe mâneci și logo pe piept.'))
  + '<p>Pe site se găsește în mărimile S, M, L și XL, care după tabelul magazinului acoperă cam vârsta de 8-15 ani.</p>',
  [('model', 'Jacheta Nike JDB ESS DRAFT JACKET albastru-negru'), ('nailon', 'realizată din nailon'), ('suprafață', 'suprafață țesută netedă'),
   ('drumeție', 'drumețiile'), ('sezon', 'sezonul primăvară-vară'), ('croială', 'croială clasică'), ('elastic', 'manșete și betelie elastică'),
   ('glugă', 'glugă atașată'), ('fermoar', 'fermoar pe toată lungimea'), ('buzunare', 'buzunare laterale cu fermoare ascunse'),
   ('panouri', 'panouri de culoare contrastantă pe mâneci'), ('logo', 'logo vizibil pe piept')],
  {'Model': 'Nike JDB ESS DRAFT JACKET', 'Material': 'nailon', 'Caracteristici': 'glugă atașată, manșete și betelie elastice, buzunare cu fermoare ascunse', 'Cod produs': '95D689-GAG'},
  varsta_txt='8-15 ani', notes=['Vârsta pentru S-XL: tabelul de mărimi Nike al magazinului (pagina produsului 4949); pe pagina acestui produs tabelul e trunchiat.'])

w(9537,
  f'<p>{GEOX} ECLYPER sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu partea de sus din imitație de piele și material textil, decorată cu detalii cu sclipici. În talpă au tehnologia Geox Respira™, făcută să scoată umezeala din pantof cât timp copilul se joacă.</p>'
  '<p>Aricii se strâng pe lățimea piciorului, deci pantoful se închide bine și pe un picior mai îngust, iar copilul se încalță singur, fără șireturi de legat.</p>'
  '<p>Înăuntru și dedesubt, lucrurile stau așa:</p>'
  + L(('Interior', 'din material textil.'), ('Branț', 'textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-35 se poartă cam între 2 și 11 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii roz J66LRG.0BCKC'), ('parte superioară', 'Partea superioară din imitație de piele și material textil'),
   ('sclipici', 'Detalii cu sclipici'), ('Respira', 'Tehnologia GEOX Respira™'), ('umezeală', 'eliminând umezeala'), ('activitate', 'în timpul activităților'),
   ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă'), ('interior', 'Interior din material textil'),
   ('branț', 'Branț respirabil din material textil'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira™, arici, detalii cu sclipici', 'Cod produs': 'J66LRG.0BCKC'})

w(9539,
  f'<p>{GEOX} WASHIBA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, cu profil înalt și guler ușor întărit în jurul gleznei. Partea de sus e din imitație de piele și material textil, cu logo-ul mărcii pe o suprafață netedă, iar în talpă au membrana microporoasă Geox Respira™.</p>'
  '<p>Închiderea e dublă, cu șireturi și arici: șiretul se strânge după forma piciorului, iar aricii îi lasă pe copii să se încalțe singuri. Branțul textil se scoate, așa că piciorul se poate măsura direct pe el.</p>'
  '<p>Pentru purtat de dimineața până seara, contează și restul construcției:</p>'
  + L(('Călcâi', 'întărit, ține piciorul pe loc.'), ('Interior', 'căptușit cu material textil moale.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 28-35 sunt, de regulă, pentru copii de 4-11 ani.</p>',
  [('model', 'Geox WASHIBA sneakers pentru copii bleumarin J66LQI.0BC15'), ('profil înalt', 'Sneakerșii Geox WASHIBA sunt sneakerși pentru copii cu profil înalt'),
   ('guler', 'Profilul înalt al părții superioare cu guler ușor întărit'), ('material', 'Partea superioară realizată din imitație de piele și material textil'),
   ('logo', 'Model cu logo-ul mărcii pe suprafață netedă'), ('membrană', 'membrană microporoasă în talpă'), ('Respira', 'Tehnologia patentată GEOX Respira™'),
   ('închidere', 'Sistem de închidere dublu cu șireturi și arici'), ('singur', 'încălțarea autonomă'), ('branț', 'Branțuri detașabile din material textil'),
   ('călcâi', 'Călcâiul întărit'), ('interior', 'Interiorul căptușit cu material textil moale'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox WASHIBA', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, șireturi și arici, branț detașabil, Geox Respira™', 'Cod produs': 'J66LQI.0BC15'})

w(9543,
  f'<p>{GEOX} SPRINTYE sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, ușori, cu profil sub gleznă, din material textil combinat cu piele ecologică. Talpa are trei straturi cu perforări, după sistemul Geox Respira, care ventilează pantoful.</p>'
  '<p>Vârful e rotund, ușor rigid, iar degetele se pot așeza liber în pantof. Șireturile elastice cu închidere pe cârlig se reglează fără nod, iar bucla de la spate ajută la tras pantoful pe picior.</p>'
  '<p>Mai sunt câteva lucruri de știut despre construcție:</p>'
  + L(('Călcâi', 'contrafort rigid, piciorul nu alunecă în pantof.'), ('Interior', 'textil, se păstrează ușor curat.'), ('Talpă', 'din spumă.'))
  + '<p>Numerele 20-27 se potrivesc copiilor de în jur de 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii SPRINTYE culoarea roz, B454TD.01454'), ('material', 'combinația materialului textil cu pielea ecologică'), ('ușor', 'Model ușor'),
   ('profil', 'Pantoful de sub gleznă'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'), ('ventilare', 'imbunatateste ventilarea'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('degete', 'degetele se pot aranja liber în pantof'), ('șireturi', 'Șireturile elastice și închiderea cu cârlig'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('călcâi', 'Contorul de călcâi rigid'), ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpa din spumă')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil și piele ecologică, interior textil, talpă din spumă', 'Caracteristici': 'Geox Respira, șireturi elastice cu cârlig, buclă la spate', 'Cod produs': 'B454TD.01454'},
  notes=['Titlul și h1 spun roz; atributul de culoare al magazinului spune alb.'])

w(9545,
  f'<p>Pantofii {PRIMIGI} PTR 24113 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} roz, din piele nubuc, cu motiv animalier și închidere cu arici, pentru zilele de primăvară și toamnă. Sunt făcuți cu tehnologia Primigi × SIPeP, dezvoltată cu podologi.</p>'
  '<p>Vârful lat, de tip barefoot, lasă degetele într-o poziție naturală, deci pantoful merge și la un picior mai lat. Aricii se strâng pe lățimea piciorului, iar gulerul moale reduce frecarea în jurul gleznei.</p>'
  '<p>Ce e înăuntru și dedesubt:</p>'
  + L(('Interior', 'piele naturală.'), ('Branț', 'detașabil, din piele naturală, se scoate la curățat.'), ('Vârf', 'întărit, apără degetele.'), ('Talpă', 'din cauciuc, cu profil redus.'))
  + '<p>Mărimile 20-29 sunt, cu aproximație, pentru copii de 1-5 ani.</p>',
  [('model', 'Primigi Pantofi pentru copii din nubuck roz PTR 24113'), ('nubuc', 'Partea superioară din piele nubuc în nuanță de roz'), ('motiv', 'Stil casual cu motiv animalier'),
   ('arici', 'Închidere cu arici'), ('sezon', 'zilele de primăvară și toamnă'), ('SIPeP', 'Tehnologia Primigi × SIPeP'), ('podologi', 'dezvoltată cu podologi'),
   ('vârf lat', 'Vârf lat tip barefoot oferă degetelor spațiu pentru o poziție naturală'), ('guler', 'Gulerul moale'), ('abraziuni', 'minimizează riscul de abraziuni în jurul gleznei'),
   ('interior', 'Interiorul din piele naturală'), ('branț', 'Branțul detașabil din piele naturală'), ('vârf întărit', 'Vârf întărit'), ('degete', 'protejează degetele copilului'),
   ('talpă', 'Talpă din cauciuc cu profil redus')],
  {'Model': 'Primigi PTR 24113', 'Material': 'piele nubuc, interior din piele naturală, talpă din cauciuc', 'Caracteristici': 'vârf lat barefoot, arici, branț detașabil, Primigi × SIPeP', 'Cod produs': 'PTR 24113'})

w(9546,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261123 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} maro, din piele naturală, izolați termic cu o căptușeală din lână care continuă și în branțurile detașabile. Sunt pentru zilele mai răcoroase, când piciorul trebuie ținut la cald.</p>'
  '<p>Aricii permit încălțatul rapid și se reglează pe picior, iar pielea se adaptează la forma lui, fie că e mai plin, fie mai îngust.</p>'
  '<p>Pantoful e întărit acolo unde se lovește și se uzează mai repede:</p>'
  + L(('Vârf', 'întărit și cauciucat, apără degetele de lovituri.'), ('Contrafort', 'rigidizat, cu stabilizator lateral.'), ('Talpă', 'flexibilă, din cauciuc, lasă piciorul să se miște natural.'))
  + '<p>Numerele 18-25 sunt pentru copiii de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte pentru copii din piele maro 261123'), ('izolat', 'izolată termic'), ('lână', 'Căptușeala din lână în interiorul pantofului și în branțurile detașabile'),
   ('piele', 'Partea superioară din piele naturală'), ('formă', 'adaptându-se la forma piciorului'), ('răcoros', 'zilele mai răcoroase'),
   ('arici', 'Sistemul practic de închidere cu arici facilitează încălțarea și descălțarea rapidă'), ('vârf', 'Vârful întărit și cauciucat protejează degetele de lovituri'),
   ('contrafort', 'Stabilizatorul lateral și contrafortul rigidizat'), ('talpă', 'Talpa flexibilă din cauciuc favorizează mișcarea naturală a piciorului')],
  {'Model': 'Biomecanics 261123', 'Material': 'piele naturală, căptușeală din lână, talpă din cauciuc', 'Caracteristici': 'izolați termic, arici, branțuri detașabile, vârf cauciucat', 'Cod produs': '261123'})

w(9552,
  f'<p>Parka {A("/brand/columbia/", "Columbia")} 2090241 este o {A("/categorie/geci-jachete/", "geacă de iarnă pentru fete")}, neagră, izolată, cu membrana Omni-Tech® și cusături sigilate care o fac impermeabilă, deci ține la ploaie și la zăpadă. Are și tehnologia Omni-Heat Thermal Reflective, pentru frig.</p>'
  '<p>Talia elastică strânge geaca pe mijloc, ca să nu stea largă pe un copil slab, iar sistemul OUTGROWN de la Columbia e făcut ca haina să reziste mai multe sezoane, pe măsură ce copilul crește.</p>'
  '<p>Pentru vânt și frig, partea de sus e bine închisă:</p>'
  + L(('Guler și glugă', 'guler înalt, glugă fixă.'), ('Blană', 'artificială, detașabilă, pe marginea glugii.'), ('Închidere', 'fermoar și velcro.'),
      ('Buzunare', 'exterioare, cu fermoar.'), ('Umplutură', '85% poliester reciclat, 15% poliester.'))
  + '<p>Mărimile 104-164 merg, în mare, la copii de 4-14 ani.</p>',
  [('model', 'Columbia Parka pentru copii culoarea negru, 2090241'), ('izolat', 'Model izolat'), ('membrană', 'Tehnologia Omni-Tech®'), ('cusături', 'cusăturilor sigilate'),
   ('impermeabil', 'un strat durabil și impermeabil'), ('Omni-Heat', 'Tehnologia Omni-Heat Thermal Reflective'), ('talie', 'Talie elastică'),
   ('OUTGROWN', 'Sistemul OUTGROWN Grow de la Columbia'), ('sezoane', 'rezistă mai multe sezoane'), ('guler, glugă', 'Gulerul înalt și gluga fixă'),
   ('blană', 'Glugă cu garnitură detașabilă din blană artificială'), ('închidere', 'Închidere cu fermoar și velcro'), ('buzunare', 'Buzunare exterioare cu fermoar'),
   ('umplutură', '85% Poliester reciclat, 15% Poliester')],
  {'Model': 'Columbia 2090241', 'Material': '72% nailon, 28% poliester; umplutură 85% poliester reciclat, 15% poliester', 'Caracteristici': 'Omni-Tech®, cusături sigilate, Omni-Heat, OUTGROWN, talie elastică, blană detașabilă', 'Cod produs': '2090241'})

w(9556,
  f'<p>Botinele {PRIMIGI} PHR 23729 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} negre, din piele naturală, cu croiala până la gleznă și stil casual. Nu sunt izolate, așa că se poartă în zilele mai calde din sezonul de tranziție, nu iarna.</p>'
  '<p>Fermoarul îi lasă pe copii să le încalțe și să le scoată singuri, repede, iar colaborarea Primigi × SIPeP ține cont de anatomia piciorului copilului.</p>'
  '<p>Talpa și interiorul sunt făcute așa:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Shock Absorber', 'tehnologie în talpă care limitează șocurile transmise piciorului.'), ('Interior', 'căptușeală și branț textile.'))
  + '<p>Numerele 36-40 sunt, de obicei, pentru copii de la 12 ani în sus.</p>',
  [('model', 'Primigi Botine pentru copii din piele negre PHR 23729'), ('piele', 'Partea superioară din piele naturală'), ('croială', 'Croiala până la gleznă'),
   ('casual', 'Botine cu stil casual'), ('neizolat', 'Lipsa izolației face ca modelul să fie potrivit pentru zilele mai calde din sezonul de tranziție'),
   ('fermoar', 'Închidere practică cu fermoar facilitează încălțarea și descălțarea rapidă de către copil'), ('SIPeP', 'Colaborarea Primigi × SIPeP'),
   ('anatomie', 'ține cont de anatomia și dezvoltarea piciorului copilului'), ('talpă', 'Talpa plată din cauciuc'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă'), ('șocuri', 'limitând transferul acestora către picior'), ('interior', 'Căptușeala și branțul textil')],
  {'Model': 'Primigi PHR 23729', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'neizolate, fermoar, Shock Absorber, Primigi × SIPeP', 'Cod produs': 'PHR 23729'})

w(9561,
  f'<p>{GEOX} SPRINTYE J66GBB sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, sport, cu partea de sus din material textil și sintetic. Talpa exterioară e perforată și are o membrană impermeabilă, după sistemul Original Respirabil Geox, deci impermeabilă e doar talpa, nu tot pantoful.</p>'
  '<p>Scaiul cu inserție elastică îi lasă pe copii să se încalțe și să se descalțe repede, singuri, iar gulerul ușor întărit ține piciorul în poziție când aleargă.</p>'
  '<p>De la talpă la călcâi, construcția arată așa:</p>'
  + L(('Talpă', 'exterioară, din spumă.'), ('Călcâi', 'ușor întărit.'), ('Interior', 'din material textil.'))
  + '<p>Mărimile 28-35 sunt pentru copiii de pe la 4 până pe la 11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii SPRINTYE negri J66GBB.0119J'), ('material', 'Partea superioară din material textil și sintetic'),
   ('talpă perforată', 'Talpă exterioară perforată'), ('membrană', 'cu membrană respirabilă și impermeabilă'), ('sistem', 'Sistemul Original Respirabil Geox'),
   ('scai', 'Închidere cu scai și inserție elastică'), ('singur', 'facilitează încălțarea și descălțarea rapidă de către copil'), ('guler', 'Gulerul superior ușor întărit'),
   ('poziție', 'menținerea piciorului într-o poziție adecvată în timpul mișcării'), ('spumă', 'Talpă exterioară din spumă'), ('călcâi', 'Călcâi ușor întărit'),
   ('interior', 'Material textil')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil și sintetic, interior textil, talpă din spumă', 'Caracteristici': 'talpă perforată cu membrană, scai cu inserție elastică', 'Cod produs': 'J66GBB.0119J'})

w(9562,
  f'<p>{GEOX} ASSISTER J65E9A sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil scurt, din material textil și sintetic, cu lumini încorporate care se aprind dintr-un buton. Luminile îi fac pe copii mai ușor de văzut pe drum, seara sau pe înnorat.</p>'
  '<p>Șireturile elastice și cârligul înlocuiesc nodul, așa că pantoful se pune și se scoate ușor, iar cutia de la vârf e rotundă și ușor întărită.</p>'
  '<p>Ce mai are pantoful, de la talpă până la călcâi:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Călcâi', 'contrafort rigidizat.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 32-35 sunt, în general, pentru 8-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ASSISTER culoarea roz, J65E9A.0ASPV'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu cel sintetic'),
   ('lumini', 'Model cu lumini incorporate, activate de un buton'), ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('cutie', 'Cutie rotunda, usor intarita'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'), ('călcâi', 'Contorul de călcâi rigidizat'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox ASSISTER', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini cu buton, șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J65E9A.0ASPV'})
