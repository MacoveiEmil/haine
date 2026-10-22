import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(12886,
  f'<p>Adidașii {TH} T3A9-34249 albi sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din material sintetic, parțial din poliester reciclat. Inserția elastică ajută pantoful să stea bine pe fiecare picior, iar cutia rotundă, ușor întărită, apără degetele.</p>'
  '<p>Contrafortul rigid ține călcâiul în pantof, ca să nu alunece la mers.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'din cauciuc, durabilă.'), ('Partea de sus', 'imitație de piele.'))
  + '<p>Numerele 35-40 sunt pentru fete de la aproximativ 10 ani în sus; la 40 branțul are 25,5 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea alb, T3A9-34249'), ('profil', 'Înălțime: mic de statură'), ('sintetic', 'Gamba: Material sintetic'),
   ('reciclat', 'Acest produs este realizat partial din poliester reciclat'), ('elastic', 'Inserția elastică asigură o potrivire individuală'), ('vârf', 'Cutie rotunda, usor intarita'),
   ('călcâi', 'Contorul de călcâi rigid stabilizează călcâiul'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'talpă din cauciuc care este durabilă'), ('lungime', 'Lungimea brantului pentru marimea este de: 25,5 cm')],
  {'Model': 'Tommy Hilfiger T3A9-34249', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'inserție elastică, vârf întărit', 'Cod produs': 'T3A9-34249'},
  notes=['Descrierea spune piele întoarsă, compoziția și atributele dau material sintetic (imitație de piele); am scris sintetic.'])

w(12891,
  f'<p>Modelul {GEOX} PERTH J367RF există și în maro: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} înalți, casual-streetwear, din imitație de piele și textil, cu logo Geox. Apa nu trece de membrana din talpă, iar umezeala din pantof iese prin GEOX Respira.</p>'
  '<p>Șireturile și aricii se folosesc împreună, pentru reglaj rapid. Profilul înalt, cu guler ușor întărit, sprijină glezna.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Căptușeală', 'textilă, aerisită.'), ('Branțuri', 'textile, se scot.'), ('Talpă', 'din cauciuc, plată.'))
  + '<p>Numerele 28-35 se potrivesc băieților de cam 4-11 ani.</p>',
  [('model', 'Geox PERTH sneakers pentru copii maro J367RF.0MEMS'), ('înalt', 'o încălțăminte înaltă pentru copii'), ('stil', 'Caracterul lor casual și streetwear'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('logo', 'Modelul cu logo-ul mărcii Geox'),
   ('membrană', 'Membrana microporoasă din talpă protejează împotriva pătrunderii apei din exterior'), ('Respira', 'Tehnologia GEOX Respira™ favorizează eliminarea umezelii'),
   ('închidere', 'Combinația de șireturi și arici facilitează ajustarea'), ('guler', 'Profilul înalt al părții superioare cu un guler ușor întărit susține glezna'),
   ('căptușeală', 'Căptușeala interioară textilă favorizează o circulație adecvată a aerului'), ('branț', 'Branțurile textile detașabile'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, membrană în talpă, șireturi și arici', 'Cod produs': 'J367RF.0MEMS'})

w(12893,
  f'<p>{GEOX} GISLI B561MG sunt {A("/categorie/adidasi/", "adidași pentru fete")} aurii, înalți, din imitație de piele și material textil, pentru fetițele mici. Membrana microporoasă din talpă ține apa afară, iar GEOX Respira scoate umezeala.</p>'
  '<p>Aricii fac încălțatul și descălțatul rapid, iar profilul înalt, cu guler ușor întărit, susține glezna. Nuanța aurie dă strălucire ținutei, iar talpa plată din cauciuc lasă piciorul să se miște liber.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Căptușeală', 'textilă.'), ('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-23 merg la fetițe de în jur de 1-3 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii aurii B561MG.0AUAJ'), ('culoare', 'Culoare aur'), ('înalt', 'Profilul înalt al părții superioare împreună cu gulerul ușor întărit susține glezna'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('membrană', 'Membrana microporoasă din talpă protejează împotriva pătrunderii apei'),
   ('Respira', 'Tehnologia GEOX Respira™ favorizează eliminarea umezelii'), ('arici', 'Sistemul practic de închidere cu arici'),
   ('căptușeală', 'Interiorul căptușit cu material textil'), ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa plată din cauciuc permite o mișcare liberă'), ('auriu', 'adăugând strălucire oricărei ținute')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici, profil înalt', 'Cod produs': 'B561MG.0AUAJ'})

w(12894,
  f'<p>{GEOX} KALISPERA sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, înalți, cu imprimeu decorativ, din imitație de piele și material textil, pentru ținute casual și streetwear. Membrana microporoasă din talpă oprește apa, iar GEOX Respira scoate umezeala spre exterior.</p>'
  '<p>Combinația de șireturi și arici permite o reglare precisă, iar gulerul ușor întărit nu încurcă glezna.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'din piele naturală, fără crom.'), ('Interior', 'material textil.'), ('Călcâi', 'ușor întărit.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 28-35 sunt pentru fete de aproximativ 4-11 ani.</p>',
  [('model', 'Geox KALISPERA sneakers pentru copii roz J744GI.0AU54'), ('înalt', 'sneakerși înalți pentru copii'), ('imprimeu', 'Imprimeul decorativ pe fața superioară'),
   ('material', 'Fața superioară din imitație de piele și material textil'), ('stil', 'ținute casual și streetwear'),
   ('membrană', 'O specială membrană microporoasă în talpă protejează interiorul încălțămintei de apă'), ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală a piciorului, eliminând umezeala spre exterior'),
   ('închidere', 'Combinația de șireturi și arici permite ajustarea precisă'), ('guler', 'Gulerul superior ușor întărit susține confortul în jurul gleznei, fără a îngrădi mișcările'),
   ('branț', 'Branțul din piele naturală , fără crom'), ('interior', 'Interiorul din material textil'), ('călcâi', 'Călcâiul ușor întărit'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox KALISPERA', 'Material': 'imitație de piele și textil, branț din piele, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, șireturi și arici', 'Cod produs': 'J744GI.0AU54'})

w(12896,
  f'<p>Adidașii {A("/brand/liewood/", "Liewood")} Denisa sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} bleumarin, cu design simplu, neted, din material textil care lasă aerul să circule, pentru joaca afară și grădiniță. Aricii permit încălțatul și descălțatul rapid, chiar de către copil.</p>'
  '<p>Călcâiul întărit ține piciorul drept, iar gulerul întărit susține glezna. Talpa din cauciuc ține bine pe sol la joacă, iar culoarea bleumarin merge cu multe haine.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Talpă', 'din cauciuc.'), ('Partea de sus', 'material textil.'))
  + '<p>Gama 22-35 acoperă copii de cam 1-11 ani.</p>',
  [('model', 'Liewood Denisa Sneakers pentru copii bleumarin LW20059'), ('neted', 'design simplu, neted'), ('textil', 'Fața din material textil favorizează respirabilitatea'),
   ('preșcolar', 'jocurilor în aer liber și al activităților preșcolare'), ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă de către copii'),
   ('călcâi', 'Călcâi întărit'), ('guler', 'Gulerul superior întărit susține delicat glezna'), ('căptușeală', 'Căptușeală moale din material textil'), ('talpă', 'Talpa de cauciuc oferă o bună aderență la sol'), ('bleumarin', 'Designul neted în culoarea bleumarin permite o asortare ușoară')],
  {'Model': 'Liewood Denisa', 'Material': 'textil, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, călcâi întărit', 'Cod produs': 'LW20059'})

w(12897,
  f'<p>Adidașii {TH} T3A9-35074 bej sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu motiv animalier, profil scurt și guler ușor întărit, din imitație de piele care se curăță ușor. Se leagă cu șireturi clasice, pentru o strângere precisă.</p>'
  '<p>Talpa plată din cauciuc are 2-4 cm grosime și izolează de sol, iar călcâiul întărit ține piciorul pe loc. Talpa e durabilă și merge pe diverse suprafețe.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textilă.'), ('Partea de sus', 'material sintetic.'), ('Închidere', 'șireturi.'))
  + '<p>Numerele 35-40 se potrivesc copiilor de la aproximativ 10 ani în sus.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bej T3A9-35074'), ('animal', 'Motivul animalier adorabil'), ('profil', 'Profilul scurt al încălțămintei'),
   ('guler', 'Gulerul superior ușor întărit'), ('imitație', 'Partea superioară din imitație de piele oferă pantofilor un aspect estetic și facilitează menținerea curățeniei'),
   ('șireturi', 'Sistemul clasic de înșiretare permite ajustarea precisă'), ('talpă', 'Talpa plată asigură un suport stabil'), ('cauciuc', 'Talpa din cauciuc este durabilă și potrivită pentru diverse suprafețe'),
   ('grosime', 'Grosimea tălpii în intervalul 2-4 cm contribuie la confort și la izolarea de sol'), ('călcâi', 'Călcâiul întărit'), ('căptușeală', 'Interiorul căptușit cu material textil')],
  {'Model': 'Tommy Hilfiger T3A9-35074', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi, motiv animalier, profil scurt', 'Cod produs': 'T3A9-35074'})

w(12898,
  f'<p>Pentru fetele mai mari, {GEOX} WASHIBA J36HXA vin în roz și în numerele 36-39: {A("/categorie/adidasi/", "adidași pentru fete")} înalți, din imitație de piele și textil, care se închid cu arici. Membrana microporoasă din talpă blochează apa, iar GEOX Respira elimină umiditatea.</p>'
  '<p>Profilul înalt ține glezna stabilă, iar căptușeala textilă e confortabilă la purtare îndelungată.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Talpă', 'plată, din cauciuc, ține bine pe sol.'), ('Închidere', 'arici, pentru încălțat singur.'), ('Partea de sus', 'imitație de piele și material textil.'))
  + '<p>Se potrivesc fetelor de pe la 12 ani în sus.</p>',
  [('model', 'Geox WASHIBA sneakers pentru copii roz J36HXA.05415'), ('înalt', 'încălțăminte înaltă pentru fetițe'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă, susținând autonomia'), ('membrană', 'blocând pătrunderea apei din exterior'),
   ('Respira', 'Tehnologia GEOX Respira™ favorizează termoreglarea naturală a piciorului, eliminând umiditatea'), ('profil', 'Profilul înalt al părții superioare stabilizează glezna'),
   ('căptușeală', 'Interiorul căptușit cu material textil contribuie la confort în timpul utilizării îndelungate'), ('talpă', 'Talpa plată din cauciuc asigură aderență la sol')],
  {'Model': 'Geox WASHIBA', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici, profil înalt', 'Cod produs': 'J36HXA.05415'})

w(12901,
  f'<p>Geaca {A("/brand/new-balance/", "New Balance")} YJ62H2WF violet este o {A("/categorie/geci-jachete/", "geacă pentru fete")} matlasată, cu umplutură din puf sintetic și izolație medie, pentru tranziție și ierni blânde. Croiala lejeră lasă loc pentru straturi pe dedesubt, iar gluga integrată și gulerul ridicat apără de vânt.</p>'
  '<p>Se închide cu fermoar, iar manșetele cu nervuri țin aerul rece afară.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'sintetică, completă.'), ('Buzunare', 'laterale, slip-on.'), ('Material', '56% nailon, 44% bumbac.'))
  + '<p>Mărimile 122-128 până la 166-168 sunt pentru fete de cam 7-15 ani.</p>',
  [('model', 'New Balance Geacă petrecută pentru copii violet YJ62H2WF'), ('matlasat', 'Finisaj matlasat al materialului'), ('umplutură', 'Umplutură din puf sintetic'),
   ('izolație', 'Izolație termică medie'), ('iarnă', 'sezonul de tranziție și iarna blândă'), ('croială', 'Croială lejeră – favorizează libertatea de mișcare, permițând purtarea unor straturi suplimentare'),
   ('glugă', 'Glugă integrată'), ('guler', 'Guler ridicat'), ('fermoar', 'Sistem de închidere cu fermoar'), ('manșete', 'Manșete cu nervuri'),
   ('căptușeală', 'Căptușeală sintetică completă'), ('buzunare', 'Buzunare laterale, tip slip-on'), ('material', '44% Bumbac, 56% Nailon')],
  {'Model': 'New Balance YJ62H2WF', 'Material': '56% nailon, 44% bumbac, umplutură din puf sintetic', 'Caracteristici': 'matlasată, glugă integrată, guler ridicat', 'Cod produs': 'YJ62H2WF'})

w(12903,
  f'<p>Pantofii {BIO} 261126 bleumarin sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} uni, din piele naturală și materiale sintetice, făcuți împreună cu podologi, în stil casual, clasic și streetwear. Talpa flexibilă de cauciuc are 1 cm și lasă piciorul să se miște liber.</p>'
  '<p>Aricii cu curea reglabilă se strâng repede, iar gulerul moale nu irită. Vârful cauciucat apără degetele.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Branț', 'detașabil, antibacterian.'), ('Stabilizatori', 'laterali, cu călcâi întărit.'), ('Interior', 'textil moale.'))
  + '<p>Numerele 18-25 se poartă cam între 1 și 3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele bleumarin 261126'), ('uni', 'Culoarea bleumarin și modelul uni'), ('material', 'Partea superioară dintr-o combinație de piele naturală și materiale sintetice'),
   ('podologi', 'creată în colaborare cu podologi'), ('stil', 'Stil universal casual, clasic și streetwear'), ('talpă', 'Talpă flexibilă de cauciuc cu o grosime de 1 cm'),
   ('arici', 'Închidere cu arici și curea reglabilă'), ('guler', 'Guler moale al părții superioare minimizează riscul de iritații'), ('vârf', 'Vârf rotund, cauciucat'),
   ('branț', 'Branț detașabil, respirabil, cu proprietăți antibacteriene'), ('stabilizatori', 'Stabilizatori laterali și călcâi întărit'), ('interior', 'Interior din material textil moale')],
  {'Model': 'Biomecanics 261126', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, vârf cauciucat, branț antibacterian', 'Cod produs': '261126'})

w(12906,
  f'<p>Ghetele de trekking {A("/brand/primigi/", "Primigi")} 23918 bleumarin sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} cu profil înalt și membrană GORE-TEX, care ține umezeala afară. Sistemul Shock Absorber din talpă reduce șocurile, iar construcția Primigi × SIPeP e făcută cu podologi.</p>'
  '<p>Închiderea dublă, cu șireturi și arici, fixează bine piciorul, iar călcâiul întărit dă siguranță pe teren accidentat.</p>'
  '<p>Din ce sunt făcute:</p>'
  + L(('Partea de sus', 'piele întoarsă și sintetic.'), ('Interior', 'material textil.'), ('Talpă', 'cu bandă de rulare, pentru suprafețe variate.'))
  + '<p>Numerele 31-35 sunt pentru copii de în jur de 6-11 ani.</p>',
  [('model', 'Primigi Încălțăminte de trekking pentru copii bleumarin PPTGT 23918'), ('înalt', 'cu profil înalt'), ('GORE-TEX', 'Membrana GORE-TEX® protejează împotriva umezelii'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă reduce șocurile'), ('SIPeP', 'Sistemul Primigi × SIPeP , creat în colaborare cu podologi'),
   ('închidere', 'Sistemul dublu de închidere cu șireturi și arici'), ('călcâi', 'Călcâiul întărit stabilizează călcâiul, ceea ce sporește siguranța pe teren accidentat'),
   ('material', 'Partea superioară din piele întoarsă și material sintetic'), ('interior', 'Material textil'), ('talpă', 'Talpa cu bandă de rulare mărește aderența pe suprafețe variate')],
  {'Model': 'Primigi 23918', 'Material': 'piele întoarsă și sintetic, interior textil', 'Caracteristici': 'GORE-TEX, Shock Absorber, șireturi și arici', 'Cod produs': 'PPTGT 23918'})
