import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
PRIM = A('/brand/primigi/', 'Primigi')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')

w(12932,
  f'<p>{GEOX} IUPIDOO B3555D bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} pentru cei mai mici, cu profil jos, din piele naturală, piele întoarsă și material textil, cu interior și branț din piele. Talpa moale și flexibilă lasă piciorul să se miște liber.</p>'
  '<p>Velcro-ul și bucla de pe limbă fac încălțatul ușor, iar contrafortul rigid ține călcâiul pe loc.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Light Flexy', 'sistem de branț care lasă piciorul să se miște.'), ('Geox Respira', 'talpă în trei straturi, perforată.'), ('Vârf', 'rotund, ușor rigid.'))
  + '<p>Numerele 18-26 se potrivesc băieților de aproximativ 1-4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii IUPIDOO culoarea bleumarin, B3555D.05422'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinație de piele naturală, piele întoarsă și material textil'),
   ('interior', 'Un model cu interior din piele'), ('branț', 'Brantul din piele este confortabil pentru picior'), ('talpă', 'Talpa moale și flexibilă oferă libertate deplină de mișcare'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('buclă', 'O buclă pe limbă facilitează alunecarea pantofului pe picior'),
   ('călcâi', 'Contorul de călcâi rigid'), ('Light Flexy', 'Light Flexy Sistem de brant pentru libertatea de miscare'), RESPIRA, ('vârf', 'Degetul rotund, ușor rigid')],
  {'Model': 'Geox IUPIDOO', 'Material': 'piele naturală, piele întoarsă și textil, interior din piele', 'Caracteristici': 'velcro, Light Flexy, Geox Respira, talpă flexibilă', 'Cod produs': 'B3555D.05422'})

w(12934,
  f'<p>Adidașii {TH} T3A9-34242 albi sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil jos, din piele ecologică și imitație de piele întoarsă, ușori, pentru purtarea zilnică. Se leagă cu șiret clasic, care se reglează după picior.</p>'
  '<p>Cutia rotundă e întărită, iar călcâiul întărit are umplutură moale care îl apără de frecare.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'material textil.'), ('Talpă exterioară', 'din cauciuc, durabilă.'), ('Partea de sus', 'material sintetic.'))
  + '<p>Numerele 35-40 se potrivesc fetelor de la vreo 10 ani în sus, orientativ; la 39 branțul are 25,5 cm.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii culoarea alb, T3A9-34242'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația de piele ecologică cu imitatia de piele întoarsă'),
   ('ușor', 'Model ușor și confortabil'), ('șiret', 'Șiretul clasic permite ajustarea individuală a piciorului'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'), ('interior', 'Interiorul: Material textil'), TALPA,
   ('lungime', 'Lungimea brantului pentru marimea este de: 25,5 cm')],
  {'Model': 'Tommy Hilfiger T3A9-34242', 'Material': 'piele ecologică și imitație de piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'șiret, călcâi căptușit', 'Cod produs': 'T3A9-34242'})

w(12935,
  f'<p>{GEOX} CIUFCIUF B455RB maro sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} din piele întoarsă și material textil, plăcute la atingere, cu talpa GEOX Respira cu membrană microporoasă. Sistemul Original Breathing scoate umezeala și ține apa afară.</p>'
  '<p>Aricii și inserția elastică fac încălțatul rapid, iar gulerul ușor rigidizat stă bine în jurul gleznei. Talpa din spumă preia șocurile la fiecare pas.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'plată, din spumă, ușoară și flexibilă.'), ('Căptușeală', 'textilă.'), ('Călcâi', 'ușor întărit.'))
  + '<p>Numerele 24-27 se potrivesc băieților de cam 2-4 ani.</p>',
  [('model', 'Geox CIUFCIUF sneakers pentru copii maro B455RB.0FU22'), ('material', 'Partea superioară din piele întoarsă și material textil creează o construcție durabilă, care este plăcută la atingere'),
   ('Respira', 'Tehnologia GEOX Respira™ favorizează menținerea picioarelor uscate datorită membranei microporoase'), ('Breathing', 'Original Breathing System susține ventilația, eliminând umezeala și protejând împotriva apei'),
   ('arici', 'Sistemul de închidere cu arici'), ('elastic', 'Inserția elastică în partea superioară'), ('guler', 'Guler ușor rigidizat în jurul gleznei'),
   ('talpă', 'Talpă plată din spumă oferă lejeritate și flexibilitate'), ('căptușeală', 'Interior căptușit cu material textil'), ('călcâi', 'Călcâi ușor întărit'), ('șocuri', 'Talpa din spumă susține absorbția șocurilor')],
  {'Model': 'Geox CIUFCIUF', 'Material': 'piele întoarsă, textil și sintetic, interior textil, talpă din spumă', 'Caracteristici': 'Geox Respira cu membrană, arici cu inserție elastică', 'Cod produs': 'B455RB.0FU22'})

w(12936,
  f'<p>Cizmele de zăpadă {PRIM} 88840 negre sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} ușor izolate, din material textil, piele naturală și piele întoarsă, cu membrană GORE-TEX subțire, rezistentă la vânt. Rezistă la apă, deși magazinul nu garantează impermeabilitatea completă.</p>'
  '<p>Partea de sus ridicată sprijină glezna pe teren denivelat, iar velcro-ul face încălțatul rapid.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Vârf', 'cutie rotundă, ușor întărită.'), ('Călcâi', 'contrafort rigid.'), ('Interior', 'textil.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 36-40 sunt pentru copii de la aproximativ 12 ani în sus.</p>',
  [('model', 'Primigi Cizme de iarnă copii culoarea negru, PFZGT 88840'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Izolare: usor izolat'),
   ('material', 'combinație de material textil, piele naturală și piele întoarsă'), ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire'),
   ('vânt', 'rezistenta la vant'), ('apă', 'nu garantează impermeabilitatea completă'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('vârf', 'Cutie rotunda, usor intarita'), ('călcâi', 'Contorul de călcâi rigid'),
   ('interior', 'Interiorul textil este confortabil pentru picior'), TALPA],
  {'Model': 'Primigi 88840', 'Material': 'textil, piele naturală și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX, ușor izolate, velcro', 'Cod produs': 'PFZGT 88840'},
  notes=['Magazinul scrie că membrana e 100% impermeabilă, dar și că produsul nu garantează impermeabilitatea completă; am scris varianta prudentă.'])

w(12938,
  f'<p>Încă o pereche {GEOX} WASHIBA J55LQD în numerele 31-35: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} în culoarea verde pe site (albastru la magazin), joși, cu detalii decorative, din piele naturală, piele ecologică și textil. Se strâng cu șiret clasic.</p>'
  '<p>Fața e rigidizată, iar umplutura moale de la călcâi previne frecarea. Inserția din interior se scoate și se spală ușor.</p>'
  '<p>Talpa și căptușeala:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Căptușeală', 'textilă.'), ('Talpă', 'din cauciuc.'), ('Vârf', 'cutie rotundă, întărită.'))
  + '<p>Se potrivesc băieților de în jur de 6-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii WASHIBA culoarea verde, J55LQD.05422'), ('culoare', 'Culoare albastru'), ('profil', 'Înălțime: mic de statură'), ('decor', 'Detalii decorative'),
   ('material', 'combinatie de piele naturală, piele ecologică și material textil'), ('șiret', 'Șiretul clasic permite ajustarea individuală a piciorului'), ('rigid', 'Partea superioară rigidizată'),
   ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'), ('inserție', 'Inserție detașabilă, ușor de curățat'), RESPIRA,
   ('căptușeală', 'Model cu captuseala textila'), ('talpă', 'Talpă din cauciuc'), ('vârf', 'Cutie rotunda, intarita')],
  {'Model': 'Geox WASHIBA', 'Material': 'piele naturală, piele ecologică și textil, talpă din cauciuc', 'Caracteristici': 'șiret, Geox Respira, inserție detașabilă', 'Cod produs': 'J55LQD.05422'},
  notes=['Titlul spune verde, magazinul dă culoarea albastru; am scris ambele.'])

w(12941,
  f'<p>{GEOX} ECLYPER B665MB sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, cu profil înalt, din imitație de piele și material textil, ușor de întreținut. Tehnologia GEOX Respira ține piciorul uscat, iar branțul textil lasă aerul să circule.</p>'
  '<p>Șireturile elastice și scaiul fac încălțatul rapid și reglarea simplă, iar călcâiul întărit ține piciorul pe loc.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'material textil.'), ('Talpă', 'din cauciuc, ține bine pe sol.'), ('Închidere', 'șireturi elastice și scai.'))
  + '<p>Numerele 24-27 sunt pentru fetițe de aproximativ 2-4 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi B665MB.0BCQ6'), ('înalt', 'profilul înalt'), ('material', 'Față din imitație de piele și material textil creează o construcție durabilă, ușor de întreținut'),
   ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală a piciorului, menținându-l uscat'), ('branț', 'Branț textil respirabil susține circulația aerului'),
   ('închidere', 'Șireturi elastice și închidere cu scai facilitează încălțarea rapidă'), ('călcâi', 'Călcâi întărit asigură stabilizarea piciorului'),
   ('căptușeală', 'Interior căptușit cu material textil'), ('talpă', 'Talpă din cauciuc oferă o bună aderență la sol')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice și scai, profil înalt', 'Cod produs': 'B665MB.0BCQ6'})

w(12950,
  f'<p>Anoracul {A("/brand/wheat/", "Wheat")} 7270 verde este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} lejeră, din bumbac 100%, cu dungi clasice, pentru aventurile de primăvară și vară. Se închide cu fermoar scurt, iar gulerul înalt apără gâtul de vânt.</p>'
  '<p>Gluga se detașează, iar mânecile raglan și croiala lejeră lasă brațele libere la joacă. Bumbacul e moale și plăcut pe piele.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunar', 'în față.'), ('Manșete', 'cu bandă elastică.'), ('Lungime', 'până la șolduri.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 92-128 sunt pentru copii de cam 2-8 ani.</p>',
  [('model', 'Wheat Anorac pentru copii, din bumbac verde 7270-901'), ('lejer', 'Croiala lejeră favorizează libertatea de mișcare'), ('bumbac', 'Utilizarea de bumbac 100% susține respirabilitatea naturală și delicatețea la contactul cu pielea'),
   ('dungi', 'Modelul clasic în dungi'), ('sezon', 'aventurilor de primăvară-vară'), ('fermoar', 'Închiderea scurtă cu fermoar'), ('guler', 'Gulerul de tip înalt ajută la protejarea gâtului'),
   ('glugă', 'Gluga detașabilă'), ('raglan', 'Croiala raglan a mânecilor'), ('buzunar', 'Un buzunar practic în partea din față'), ('manșete', 'Manșetele finisate cu bandă elastică'),
   ('lungime', 'Lungimea până la șolduri'), ('material', '100% Bumbac')],
  {'Model': 'Wheat 7270 (anorac)', 'Material': '100% bumbac', 'Caracteristici': 'glugă detașabilă, fermoar scurt, dungi', 'Cod produs': '7270-901'})

w(12954,
  f'<p>Ghetele de iarnă {PRIM} 23500 roz sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} înalte, pentru cele mai mici, din piele întoarsă și material textil, cu interior izolat termic. Membrana GORE-TEX blochează apa și scoate umezeala, iar Shock Absorber din talpă reduce șocurile la mers.</p>'
  '<p>Aricii fac încălțatul rapid, chiar de către copil, iar călcâiul întărit ține piciorul drept.</p>'
  '<p>Ce mai au ghetele:</p>'
  + L(('Primigi × SIPeP', 'construcție după anatomia piciorului.'), ('Interior', 'textil, izolat.'), ('Partea de sus', 'piele întoarsă și textil.'))
  + '<p>Numerele 19-24 se potrivesc fetițelor de în jur de 1-3 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii roz PSNGT 23500'), ('înalt', 'Partea superioară înaltă , din combinația de piele întoarsă și material textil'),
   ('izolat', 'Interior izolat termic'), ('GORE-TEX', 'Membrană GORE-TEX® care contribuie la menținerea picioarelor uscate, blocând apa și evacuând umezeala către exterior'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă, reduce șocurile'), ('arici', 'Sistem practic de închidere cu arici care facilitează încălțarea și descălțarea rapidă de către copil'),
   ('călcâi', 'Călcâi întărit'), ('SIPeP', 'Colaborarea Primigi × SIPeP ține cont de anatomia piciorului copilului')],
  {'Model': 'Primigi 23500', 'Material': 'piele întoarsă și textil, interior izolat', 'Caracteristici': 'GORE-TEX, Shock Absorber, arici', 'Cod produs': 'PSNGT 23500'})

w(12958,
  f'<p>{BIO} 261163 sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, din piele naturală și imitație de piele, gândiți cu podologi pentru joaca de zi cu zi. Spațiul mai mare din vârf lasă degetele libere, iar talpa flexibilă din cauciuc urmează mișcarea piciorului.</p>'
  '<p>Aricii cu curea reglabilă se strâng rapid, iar gulerul moale nu irită. Stabilizatorul lateral și călcâiul întărit țin piciorul corect.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Branț', 'antibacterian.'), ('Căptușeală', 'textil moale.'), ('Podology Partnership', 'colaborare cu podologi.'))
  + '<p>Au rămas numerele 24-26, pentru fetițe de cam 2-4 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele roz 261163'), ('material', 'Partea superioară dintr-o combinație de piele naturală și imitație de piele'),
   ('podologi', 'creată în colaborare cu podologi'), ('zilnic', 'activitățile și joaca de zi cu zi'), ('vârf', 'Spațiu sporit în vârful pantofului permite o poziționare liberă a degetelor'),
   ('talpă', 'Talpă flexibilă din cauciuc favorizează mișcarea naturală a piciorului'), ('arici', 'Închidere practică cu arici și curea reglabilă'),
   ('guler', 'Gulerul superior moale minimizează riscul de iritații'), ('stabilizator', 'Stabilizator lateral în încălțăminte'), ('călcâi', 'Călcâi întărit'),
   ('branț', 'Branț antibacterian'), ('căptușeală', 'Căptușeală moale din material textil'), ('Podology', 'Parteneriatul Biomecanics Podology')],
  {'Model': 'Biomecanics 261163', 'Material': 'piele naturală și imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, stabilizator lateral, branț antibacterian', 'Cod produs': '261163'})

w(12959,
  f'<p>{BIO} 261128 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} bleumarin, din piele naturală, cu imprimeu decorativ, în stil casual și streetwear, pentru joaca dinamică. Spațiul extins în zona degetelor ajută piciorul să stea natural.</p>'
  '<p>Aricii permit o reglare rapidă, iar gulerul ușor întărit cuprinde glezna. Talpa de cauciuc, plată, se îndoaie ușor la pas. Pielea naturală ține mult, iar imprimeul dă pantofului un aer copilăresc.</p>'
  '<p>Pe dinăuntru:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Branț', 'aerisit.'), ('Călcâi', 'ușor întărit.'))
  + '<p>Numerele 18-25 merg la copii de aproximativ 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele bleumarin 261128'), ('piele', 'Partea superioară confecționată din piele naturală permite o utilizare de lungă durată'), ('imprimeu', 'Imprimeu decorativ adaugă încălțămintei un caracter și un stil copilăresc'),
   ('stil', 'Caracterul său casual și streetwear'), ('joacă', 'conceput pentru joacă dinamică'), ('degete', 'Spațiu extins în zona degetelor'),
   ('arici', 'Închidere practică cu arici facilitează ajustarea rapidă'), ('guler', 'Gulerul superior ușor întărit îmbrățișează delicat glezna'),
   ('talpă', 'Talpă de cauciuc cu profil plat permite flexarea liberă a piciorului'), ('căptușeală', 'Interior căptușit cu material textil'),
   ('branț', 'Branț respirabil susține circulația aerului'), ('călcâi', 'Călcâi ușor întărit')],
  {'Model': 'Biomecanics 261128', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, spațiu extins la degete', 'Cod produs': '261128'})
