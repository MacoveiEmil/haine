import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')
AMPHIBIOX = ('Amphibiox', 'Tehnologia Amphibiox®. Membrana special respirabila si nepermeabila protejeaza atat talpa exterioara, cat si cea superioara')

w(12985,
  f'<p>Varianta neagră a modelului {A("/brand/reima/", "Reima")} Tallustelu: {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} ușori, joși, din textil și piele ecologică, cu fața tratată hidrofob, ca umezeala să rămână afară. Rezistă bine la vreme urâtă, dar fără garanția impermeabilității complete.</p>'
  '<p>Se încalță repede, datorită șireturilor cu opritor și buclei. În vârf e loc destul, așa că degetele nu sunt strânse.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Happy Fit', 'inserții detașabile pentru verificarea mărimii.'), ('Căptușeală', 'sintetic și textil.'), ('Talpă', 'cauciuc rezistent.'))
  + '<p>Mărimile 28-40 sunt pentru copii de pe la 4 ani în sus.</p>',
  [('model', 'Reima Sneakers pentru copii Tallustelu culoarea negru, 5400137C'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('ușor', 'Model ușor și confortabil'), ('hidrofob', 'Finisajul hidrofob al feței superioare nu permite umezelii să pătrundă în interior'), ('apă', 'nu garantează impermeabilitatea completă'),
   ('șireturi', 'Sistemul rapid de șireturi cu opritoare'), ('buclă', 'Bucla ușurează să pui pantoful în picior'), ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'),
   ('Happy Fit', 'Inserțiile detașabile Happy Fit vă permit să alegeți dimensiunea potrivită'), ('interior', 'Material sintetic, Material textil'), TALPA],
  {'Model': 'Reima Tallustelu', 'Material': 'textil și piele ecologică, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'finisaj hidrofob, șireturi rapide, Happy Fit', 'Cod produs': '5400137C'})

w(12986,
  f'<p>{GEOX} GISLI J465CC verzi, în numerele 36-39, sunt {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi pentru băieți")} descriși de magazin ca ghete de iarnă, din imitație de piele și material textil. Membrana microporoasă din talpă ține apa afară, iar GEOX Respira scoate umezeala.</p>'
  '<p>Șireturile și scaiul permit o reglare precisă și încălțat rapid, iar călcâiul întărit dă siguranță la fiecare pas.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branțuri', 'textile, detașabile.'), ('Interior', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Se potrivesc băieților de la aproximativ 12 ani în sus.</p>',
  [('model', 'Geox Încălțăminte pentru copii GISLI verde J465CC.0MEFU'), ('iarnă', 'Ghetele de iarnă Geox GISLI'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('membrană', 'Membrana microporoasă din talpă protejează interiorul încălțămintei împotriva pătrunderii apei din exterior'), ('Respira', 'Tehnologia GEOX Respira™ favorizează eliminarea umezelii'),
   ('închidere', 'Sistem de închidere cu șireturi și scai permite o ajustare precisă'), ('călcâi', 'Călcâiul întărit susține stabilizarea piciorului, contribuind la siguranța fiecărui pas'),
   ('branț', 'Branțuri detașabile din material textil'), ('interior', 'Material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, șireturi și scai', 'Cod produs': 'J465CC.0MEFU'},
  notes=['Magazinul îi descrie drept ghete de iarnă; pe site sunt la Pantofi.'])

w(12987,
  f'<p>Adidașii {TH} T1A9-35062 bej sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu profil scurt, din imitație de piele ușor de întreținut, pentru cei mici. Aricii fac încălțatul și descălțatul rapid, iar profilul scurt lasă piciorul să se miște natural.</p>'
  '<p>Călcâiul întărit ține piciorul drept la joacă, iar talpa plată din cauciuc merge pe diverse suprafețe. Interiorul textil rămâne confortabil și după multe ore de purtare.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Interior', 'material textil.'), ('Branț', 'textil.'), ('Partea de sus', 'material sintetic.'))
  + '<p>Numerele 20-29 se potrivesc copiilor de cam 1-5 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bej T1A9-35062'), ('profil', 'Profilul scurt al încălțămintei favorizează mișcarea naturală a piciorului'),
   ('imitație', 'Partea superioară din imitație de piele are un aspect estetic și este ușor de întreținut'), ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă'),
   ('călcâi', 'Călcâi întărit susține stabilitatea piciorului copilului'), ('talpă', 'Talpă plată din cauciuc permite mișcarea liberă pe diverse suprafețe'),
   ('interior', 'Interiorul din material textil asigură confort la purtare pentru o perioadă mai lungă de timp'), ('branț', 'Branț din material textil')],
  {'Model': 'Tommy Hilfiger T1A9-35062', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, profil scurt', 'Cod produs': 'T1A9-35062'})

w(12990,
  f'<p>{GEOX} FLEXYPER bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu profil jos și detalii decorative, din material textil și piele ecologică, cu tehnologia Amphibiox, care ține apa afară și lasă aerul să treacă. Indicele de izolare termică dat de Geox e mediu.</p>'
  '<p>Șireturile elastice și urechile de tragere de la călcâi fac încălțatul ușor, iar partea de sus rigidizată ține forma.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Căptușeală', 'textil moale, nu irită.'), ('Vârf', 'rotund.'), ('Buclă', 'pentru tras pantoful.'))
  + '<p>Numerele 36-39 se potrivesc băieților de la vreo 12 ani în sus, orientativ.</p>',
  [('model', 'Geox FLEXYPER bleumarin J56LCA.0MEFU'), ('profil', 'Înălțime: mic de statură'), ('decor', 'Detalii decorative'), ('material', 'combinatia materialului textil cu pielea ecologica'),
   AMPHIBIOX, ('izolare', 'Indicele de izolare termică'), ('mediu', 'MEDIU'), ('închidere', 'Șireturile elastice și urechile de tragere la călcâi îl fac ușor de pus și scos'),
   ('rigid', 'Partea superioară rigidizată'), ('căptușeală', 'Căptușeala moale din material textil previne iritația'), ('vârf', 'Varf rotund'), ('buclă', 'Bucla ușurează să pui pantoful în picior')],
  {'Model': 'Geox FLEXYPER', 'Material': 'textil și piele ecologică, căptușeală textilă', 'Caracteristici': 'Amphibiox, izolare medie, șireturi elastice', 'Cod produs': 'J56LCA.0MEFU'})

w(12992,
  f'<p>{GEOX} GISLI Batman sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, cu licență DC Comics, din imitație de piele și material textil, în stil casual și streetwear. Tehnologia Geox Respira scoate umiditatea, iar gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Aricii combinați cu șireturi elastice fac încălțatul ușor. Branțul detașabil din piele are imprimeu cu care verificați mărimea, iar talpa din cauciuc ține bine pe diverse suprafețe.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'piele naturală și textil.'), ('Călcâi', 'întărit.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 20-27 sunt pentru băieți de aproximativ 1-4 ani.</p>',
  [('model', 'Geox GISLI Batman sneakers pentru copii negri B661NA.05402'), ('DC', 'Licența DC Comics'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('stil', 'stilul casual cu elemente de streetwear'), ('Respira', 'Tehnologia Geox Respira™ susține termoreglarea naturală a piciorului, eliminând umiditatea'),
   ('guler', 'Gulerul superior ușor întărit'), ('închidere', 'Închiderea practică cu arici în combinație cu șireturile elastice'),
   ('branț', 'Branțul detașabil din piele naturală cu imprimeu permite verificarea ușoară a mărimii'), ('interior', 'Interiorul din piele naturală și material textil'),
   ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa din cauciuc asigură o bună aderență pe diverse suprafețe')],
  {'Model': 'Geox GISLI Batman', 'Material': 'imitație de piele și textil, interior din piele și textil, talpă din cauciuc', 'Caracteristici': 'licență DC Comics, Geox Respira, arici și șireturi elastice', 'Cod produs': 'B661NA.05402'})

w(12998,
  f'<p>Pantofii {GEOX} negri sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} din piele naturală, cu interior tot din piele, care se închid cu cataramă cu ac. Cutia rotundă e întărită și apără degetele, iar spatele călcâiului e rigidizat.</p>'
  '<p>Talpa Geox Respira are trei straturi și perforări pentru aerisirea piciorului, iar interiorul din piele e plăcut la purtare. Atât exteriorul, cât și căptușeala sunt din piele naturală.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Exterior', 'piele naturală.'), ('Interior', 'piele naturală.'), ('Talpă', 'material sintetic, cu Geox Respira.'))
  + '<p>Numerele 36-41 se potrivesc fetelor de la aproximativ 12 ani în sus.</p>',
  [('model', 'Geox Incaltaminte din piele pentru copii culoarea negru'), ('piele', 'Model confectionat din piele naturala'), ('interior', 'Interiorul: Piele naturala'),
   ('cataramă', 'Incheiere cu catarama cu ac'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Spatele calcaiului rigidizat'), RESPIRA],
  {'Model': 'Geox (pantofi din piele)', 'Material': 'piele naturală, interior din piele', 'Caracteristici': 'cataramă cu ac, Geox Respira', 'Cod produs': ''})

w(13002,
  f'<p>Ghetele de iarnă {A("/brand/primigi/", "Primigi")} 23547 roz sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} înalte, din piele întoarsă și textil cu finisaj lucios și fir metalizat, cu membrană GORE-TEX contra apei și vântului. Sunt gândite pentru plimbări de iarnă și joacă în zăpadă.</p>'
  '<p>Aricii cu baretă reglabilă fac încălțatul ușor, iar vârful și călcâiul întărite țin piciorul corect.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'cauciuc cu bandă de rulare, groasă de 1,5 cm.'), ('Shock Absorber și Sky Effect', 'limitează șocurile la mers.'), ('Primigi × SIPeP', 'lucrat cu podologi.'))
  + '<p>Numerele 20-24 se potrivesc fetițelor de cam 1-3 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii roz PTIGT 23547'), ('înalt', 'încălțăminte înaltă pentru copii'), ('material', 'Față superioară din piele întoarsă și material textil cu finisaj lucios și fir metalizat'),
   ('GORE-TEX', 'Membrana GORE-TEX® oferă protecție împotriva apei și vântului'), ('zăpadă', 'plimbările de iarnă și joaca în zăpadă'),
   ('arici', 'Închidere cu arici și baretă reglabilă'), ('vârf', 'Vârf și călcâi întărite'), ('talpă', 'Talpă de cauciuc cu bandă de rulare cu o grosime de 1,5 cm'),
   ('Shock Absorber', 'Tehnologiile Shock Absorber și Sky Effect System în talpă'), ('șocuri', 'limitând transferul șocurilor în timpul mersului'),
   ('SIPeP', 'Linia Primigi × SIPeP reprezintă încălțăminte creată în colaborare cu podologii')],
  {'Model': 'Primigi 23547', 'Material': 'piele întoarsă și textil, interior textil', 'Caracteristici': 'GORE-TEX, Shock Absorber, arici cu baretă', 'Cod produs': 'PTIGT 23547'})

w(13004,
  f'<p>Jacheta din denim {A("/brand/adidas-originals/", "adidas Originals")} KQ8874 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} în culoarea albastru, din bumbac 100%, fără căptușeală și fără glugă, pentru zilele mai răcoroase din sezonul de tranziție. Croiala regulară și stilul casual o fac ușor de purtat cu multe ținute.</p>'
  '<p>Se închide cu fermoar, iar tivul și manșetele au nervuri.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'laterale, slip-on.'), ('Lungime', 'până la șolduri.'), ('Material', '100% bumbac (denim).'))
  + '<p>Mărimile 104-128 sunt pentru copii de în jur de 4-8 ani.</p>',
  [('model', 'adidas Originals Jachetă pentru copii din denim albastră KQ8874'), ('culoare', 'Culoare albastru'), ('bumbac', 'Confecționată 100% din bumbac tip denim'),
   ('căptușeală', 'Lipsa căptușelii'), ('glugă', 'Modelul fără glugă'), ('tranziție', 'sezonul de tranziție'), ('croială', 'Croiala de tip regulară'),
   ('casual', 'Modelul simplu și stilul casual clasic fac ca modelul să fie ușor de asortat cu multe ținute'), ('fermoar', 'Închiderea cu fermoar simplu'),
   ('nervuri', 'Tivul și manșetele cu nervuri'), ('buzunare', 'Buzunarele practice tip slip-on pe laterale'), ('lungime', 'Lungimea până la șolduri')],
  {'Model': 'adidas Originals KQ8874', 'Material': '100% bumbac (denim)', 'Caracteristici': 'fermoar, fără căptușeală, nervuri la tiv și manșete', 'Cod produs': 'KQ8874'})

w(13016,
  f'<p>Geaca de schi {A("/brand/burton/", "Burton")} SKIMMER este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} în culoarea negru pe site (roz la magazin), cu umplutură ușoară ThermacoreECO, din peste 90% fibre reciclate, care se usucă repede. Sistemul Grow îi prelungește viața pe mai multe sezoane, pe măsură ce copilul crește.</p>'
  '<p>Pe interior are centură de zăpadă, iar geaca se închide cu fermoar și velcro. E certificată Bluesign.</p>'
  '<p>Buzunarele și materialele:</p>'
  + L(('Buzunare', 'două laterale cu fermoar, plus unul pe mânecă.'), ('Exterior', '100% nailon.'), ('Umplutură', '95% poliester reciclat.'))
  + '<p>Mărimile 116-122 până la 164-166 sunt pentru copii de aproximativ 6-14 ani.</p>',
  [('model', 'Burton Geacă de schi pentru copii SKIMMER culoarea negru, 243151'), ('culoare', 'Culoare roz'), ('Thermacore', 'Umplutura usoara, sintetica ThermacoreECO, realizata din peste 90% fibre reciclate'),
   ('uscare', 'proprietățile sale de uscare rapidă'), ('Grow', 'Sistemul Grow va permite sa prelungiti durata de viata a imbracamintei exterioare pentru copii, astfel incat sa dureze mai multe sezoane'),
   ('centură', 'o centură de zăpadă încorporată'), ('închidere', 'Fixarea cu fermoar si velcro'), ('Bluesign', 'Model certificat Bluesign® Standard'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('mânecă', 'Un buzunar suplimentar pe mânecă'), ('exterior', 'Materialul de baza: 100% Nailon'),
   ('umplutură', '95% Poliester reciclat, 5% Elastan')],
  {'Model': 'Burton SKIMMER', 'Material': '100% nailon, umplutură ThermacoreECO din poliester reciclat', 'Caracteristici': 'sistem Grow, centură de zăpadă, Bluesign', 'Cod produs': '243151'},
  notes=['Titlul spune negru, magazinul dă culoarea roz; am scris ambele.', 'Descrierea scurtă spune „neizolat”, dar lista pomenește umplutura ThermacoreECO; am scris umplutură ușoară.'])

w(13018,
  f'<p>Cizmele de iarnă {GEOX} TREKKYUP negre sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme pentru băieți")} izolate, din material textil și piele ecologică, cu tehnologia Amphibiox și membrana Geox Respira, care ține apa afară și scade umezeala din interior. Partea de sus ridicată sprijină glezna pe teren denivelat.</p>'
  '<p>Se închid cu scai, deci se încalță repede. Cutia rotundă e întărită, iar spatele călcâiului e rigidizat.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'confortabil, textil.'), ('Talpă exterioară', 'din cauciuc, durabilă.'), ('Închidere', 'scai.'))
  + '<p>Numerele 20-27 se potrivesc băieților de cam 1-4 ani.</p>',
  [('model', 'Geox Cizme de iarnă pentru copii TREKKYUP culoarea negru, B566LB.0MEFU'), ('izolat', 'Izolare: izolat'), ('material', 'combinația materialului textil cu pielea ecologică'),
   AMPHIBIOX, ('Respira', 'Membrana unica si impermeabila a tehnologiei Geox Respira ajuta la scaderea umezelii excesive'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('scai', 'Incheiere cu scai'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Spatele calcaiului rigidizat'),
   ('interior', 'Interior confortabil'), TALPA],
  {'Model': 'Geox TREKKYUP', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'Amphibiox, Geox Respira, izolate, scai', 'Cod produs': 'B566LB.0MEFU'})
