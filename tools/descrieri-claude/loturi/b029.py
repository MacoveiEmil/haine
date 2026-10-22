import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
BIO = A('/brand/biomecanics/', 'Biomecanics')
GTX = ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant')

w(9722,
  f'<p>Bocancii {PRIMIGI} PND 23772 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} negre, uni, din piele naturală, cu vârf rotund și design peste gleznă. Nu sunt izolați, deci se poartă în zilele mai calde de primăvară și toamnă, nu pe ger.</p>'
  '<p>Combinația de șireturi și fermoar ajută mult: șiretul se reglează o dată după lățimea piciorului, iar fermoarul se trage la încălțat, fără să mai fie desfăcut nodul.</p>'
  '<p>Bocancul e întărit și are talpă de teren:</p>'
  + L(('Vârf și călcâi', 'întărite.'), ('Talpă', 'plată, din cauciuc, cu bandă de rulare.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Numerele 31-35 sunt, cu aproximație, pentru 6-11 ani.</p>',
  [('model', 'Primigi Bocanci pentru copii din piele negri PND 23772'), ('piele', 'Partea superioară confecționată din piele naturală'), ('uni', 'Designul uni, negru'),
   ('vârf', 'cu vârf rotund'), ('gleznă', 'Designul peste gleznă'), ('neizolat', 'Lipsa izolației face ca încălțămintea să fie potrivită pentru zilele mai calde de primăvară și toamnă'),
   ('închidere', 'Combinația de șireturi și fermoar facilitează ajustarea și încălțarea rapidă'), ('întărit', 'Vârful și călcâiul întărite'),
   ('talpă', 'Talpa din cauciuc cu bandă de rulare'), ('plată', 'Talpa plată'), ('interior', 'Interiorul căptușit cu material textil')],
  {'Model': 'Primigi PND 23772', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'neizolați, șireturi și fermoar, vârf și călcâi întărite', 'Cod produs': 'PND 23772'})

w(9724,
  f'<p>{BIO} 261165 sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, din piele naturală, cu interior din material textil, pentru copiii mici care merg mult. Aricii le permit să se încalțe și să se descalțe repede, singuri.</p>'
  '<p>În zona degetelor e mai mult spațiu, iar degetele se mișcă liber, deci pantoful merge și pe un picior mai lat. Călcâiul e moale, iar gulerul ușor întărit ține piciorul în pantof.</p>'
  '<p>Detaliile care contează la purtat:</p>'
  + L(('Branțuri', 'detașabile, se scot la curățat sau la măsurat piciorul.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Partea de sus', 'piele naturală.'))
  + '<p>Mărimile 20-26 sunt pentru copii de în jur de 1-4 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele roz 261165'), ('piele', 'Partea superioară din piele naturală'), ('interior', 'Interiorul din material textil'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă de către copii'), ('degete', 'Spațiul crescut în zona degetelor permite mișcarea liberă'),
   ('călcâi', 'Călcâiul moale'), ('guler', 'Gulerul ușor întărit'), ('branțuri', 'Branțuri detașabile'), ('talpă', 'Talpa flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261165', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, spațiu extins la degete, branțuri detașabile', 'Cod produs': '261165'})

w(9725,
  f'<p>Geaca {A("/brand/maxco/", "Max&amp;Co.")} MAXJ54F JACKET MX0281 este o {A("/categorie/geci-jachete/", "geacă izolată pentru fete")}, bej, din țesătură netedă de poliamidă, căptușită. Gulerul ridicat și gluga încorporată țin frigul departe de gât și de cap.</p>'
  '<p>Croiala e lejeră, oversize, cu umerii coborâți pe mânecă, deci încape un pulover gros dedesubt și vine comod și unui copil mai plinuț.</p>'
  '<p>Se îmbracă repede și are loc pentru mâini:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 156-172 sunt pentru adolescenți de aproximativ 13-15 ani.</p>',
  [('model', 'Max&Co. Geacă copii MAXJ54F JACKET culoarea bej, MX0281'), ('izolat', 'Model izolat confecționat din țesătură netedă'), ('căptușeală', 'Captuseala: cu captuseala'),
   ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('glugă', 'Gluga încorporată'), ('croială', 'Croială lejeră'), ('oversize', 'Fit: oversize'),
   ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('buzunare', 'Două buzunare laterale'), ('material', '100% Poliamida')],
  {'Model': 'Max&Co. MAXJ54F', 'Material': '100% poliamidă', 'Caracteristici': 'izolată, oversize, glugă încorporată, guler ridicat', 'Cod produs': 'MX0281'},
  notes=['Mărimile sunt italiene; magazinul atenționează că pot diferi de cele europene.'])

w(9738,
  f'<p>Pantofii {PRIMIGI} PTR 24113 sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} bordo (burgundy), din piele naturală netedă, cu interior tot din piele, în stil casual, pentru purtat zi de zi. Sunt făcuți cu tehnologia Primigi × SIPeP, dezvoltată împreună cu podologii.</p>'
  '<p>Vârful e lat și cauciucat, cu spațiu pentru degete, deci pantoful merge și la un picior mai lat. Aricii se strâng după picior și îl lasă pe copil să se încalțe singur.</p>'
  '<p>Pentru purtat toată ziua, mai contează:</p>'
  + L(('Branț', 'detașabil, din piele naturală.'), ('Călcâi', 'moale, cu guler ușor întărit.'), ('Talpă', 'flexibilă, din cauciuc.'))
  + '<p>Mărimile 25-29 sunt, în general, pentru copii de 2-5 ani.</p>',
  [('model', 'Primigi Pantofi pentru copii din piele burgundii PTR 24113'), ('piele', 'Partea superioară din piele naturală'), ('netedă', 'Textura netedă a materialului în nuanță burgundy'),
   ('interior', 'Interiorul din piele naturală'), ('casual', 'Stilul casual'), ('zilnic', 'ținutele zilnice'), ('SIPeP', 'Tehnologia Primigi × SIPeP'),
   ('podologi', 'dezvoltată împreună cu podologii'), ('vârf', 'Vârful lat, cauciucat oferă degetelor spațiu'), ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă de către copil'),
   ('branț', 'Branțul detașabil din piele naturală'), ('călcâi', 'Călcâiul moale și gulerul ușor întărit'), ('talpă', 'Talpa flexibilă din cauciuc')],
  {'Model': 'Primigi PTR 24113', 'Material': 'piele naturală, interior din piele, talpă din cauciuc', 'Caracteristici': 'vârf lat cauciucat, arici, branț detașabil, Primigi × SIPeP', 'Cod produs': 'PTR 24113'},
  notes=['Titlul nu are culoare; magazinul spune burgundy.'])

w(9745,
  f'<p>{BIO} 261162 sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, din piele naturală, cu imprimeu decorativ, făcuți în parteneriatul Biomecanics Podology. Sunt gândiți pentru activitățile zilnice și ținutele casual ale copiilor mici.</p>'
  '<p>Spațiul extins din zona degetelor le lasă loc să se miște, iar scaiul se strânge pe picior și se desface repede, fără ajutor.</p>'
  '<p>Înăuntru și dedesubt, pantoful are câteva lucruri simple:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Branțuri', 'detașabile.'), ('Interior', 'material textil.'), ('Talpă', 'flexibilă, din cauciuc.'))
  + '<p>Numerele 24-26 sunt, de regulă, pentru 2-4 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele roz 261162'), ('piele', 'Confecționați din piele naturală'), ('imprimeu', 'Imprimeu decorativ'),
   ('parteneriat', 'Tehnologia Biomecanics Podology Partnership'), ('zilnic', 'activități zilnice și ținute casual'), ('degete', 'Spațiu extins în zona degetelor'),
   ('scai', 'Sistem practic de închidere cu scai facilitează încălțarea și descălțarea rapidă'), ('călcâi', 'Călcâi ușor întărit'), ('branțuri', 'Branțuri detașabile'),
   ('interior', 'Materialul textil la interior'), ('talpă', 'Talpă flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261162', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'scai, spațiu extins la degete, branțuri detașabile', 'Cod produs': '261162'})

w(9747,
  f'<p>{PRIMIGI} PPTGT 23918 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete de trekking unisex")}, bleumarin, cu carâmb înalt din piele întoarsă și material sintetic, pentru drumeții la munte și joacă afară. Membrana GORE-TEX ține umezeala de afară, deci piciorul rămâne uscat pe iarbă udă și prin noroi.</p>'
  '<p>Înșiretarea rapidă strânge gheata exact pe picior, iar profilul înalt și călcâiul întărit țin glezna pe teren dificil.</p>'
  '<p>Pe traseu, contează talpa:</p>'
  + L(('Talpă', 'din cauciuc, groasă.'), ('Shock Absorber', 'sistem în talpă care reduce șocurile.'), ('Branț', 'din material textil.'))
  + '<p>Numerele 26-40 se poartă de la, cu aproximație, 3 ani în sus.</p>',
  [('model', 'Primigi Încălțăminte de trekking pentru copii bleumarin PPTGT 23918'), ('carâmb', 'Carâmbul din combinație de piele întoarsă și material sintetic'),
   ('drumeții', 'drumeții montane'), ('GORE-TEX', 'Membrana GORE-TEX ajută la menținerea picioarelor uscate'), ('umezeală', 'protejând împotriva umezelii din exterior'),
   ('șireturi', 'Sistem de înșiretare rapidă'), ('profil', 'Profilul înalt al carâmbului și călcâiul întărit'), ('teren', 'teren dificil'),
   ('talpă', 'Talpă de cauciuc cu o grosime de 2-4 cm'), ('Shock Absorber', 'Sistemul Shock Absorber în talpă contribuie la reducerea șocurilor'), ('branț', 'Branț din material textil')],
  {'Model': 'Primigi PPTGT 23918', 'Material': 'piele întoarsă și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX, înșiretare rapidă, Shock Absorber', 'Cod produs': 'PPTGT 23918'})

w(9748,
  f'<p>{PRIMIGI} PWIGT 88816 sunt {A("/categorie/ghete-cizme/", "cizme de iarnă pentru fete")}, roz, izolate, din material textil și piele întoarsă, cu interior din lână care ține piciorul cald pe frig. Membrana Gore-Tex® e impermeabilă și rezistentă la vânt, pentru zăpadă și zile ude.</p>'
  '<p>Se închid cu velcro, deci copilul le încalță și le scoate singur, iar banda se strânge după cât de plin e piciorul.</p>'
  '<p>Din ce sunt făcute:</p>'
  + L(('Partea de sus', 'material textil și piele întoarsă.'), ('Interior', 'lână.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 25-30 se potrivesc copiilor de pe la 2 până pe la 7 ani.</p>',
  [('model', 'Primigi Cizme de iarnă pentru copii culoarea roz, PWIGT 88816'), ('izolat', 'Model Izolat'), ('material', 'combinatia materialului textil cu pielea intoarsa'),
   ('lână', 'Un model cu interior din lână'), ('cald', 'vă ajută să vă mențineți cald când este frig'),
   ('Gore-Tex', 'Gore-Tex® - o membrană care combină caracteristicile de impermeabilitate, rezistență la vânt'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Primigi PWIGT 88816', 'Material': 'textil și piele întoarsă, interior din lână, talpă din cauciuc', 'Caracteristici': 'Gore-Tex®, izolate, velcro', 'Cod produs': 'PWIGT 88816'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(9752,
  f'<p>Geaca {A("/brand/united-colors-of-benetton/", "United Colors of Benetton")} 2MDJCN06R este o {A("/categorie/geci-jachete/", "geacă de tranziție pentru fete")}, violet, izolată și căptușită, din țesătură netedă cu bumbac și in. Face parte din linia Dress Safely, produsă fără metale grele sau coloranți nocivi.</p>'.replace('Face parte din linia', 'E din linia')
  + '<p>Nu are glugă, dar gulerul ridicat apără gâtul de frig. Mânecile și tivul sunt simplu tăiate, fără elastic, deci geaca cade drept.</p>'
  '<p>Are buzunare pentru toate mărunțișurile:</p>'
  + L(('Buzunare la piept', 'două, cu capse.'), ('Buzunare laterale', 'două.'), ('Închidere', 'fermoar și capse.'), ('Material', '73% bumbac, 27% in.'))
  + '<p>Mărimile 122-168 sunt, în mare, pentru copii de 7-15 ani.</p>',
  [('model', 'United Colors of Benetton Geacă copii culoarea violet, 2MDJCN06R'), ('tranziție', 'Izolare: tranzitional'), ('izolat', 'Model izolat cu captuseala'),
   ('neted', 'tesatura netedă'), ('Dress Safely', 'Dress Safely este o linie de produse care sunt produse fara utilizarea substantelor chimice, cum ar fi metalele grele sau colorantii nocivi'),
   ('fără glugă', 'Gluga: fara gluga'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'), ('mâneci', 'Mâneci și marginea inferioară finisate cu tăiere'),
   ('buzunare piept', 'Două buzunare la piept cu închidere cu capse'), ('buzunare laterale', 'Două buzunare laterale'), ('închidere', 'Fixare cu fermoar si snap'),
   ('material', '73% Bumbac, 27% In')],
  {'Model': 'United Colors of Benetton 2MDJCN06R', 'Material': '73% bumbac, 27% in; 55% poliester, 45% viscoză; 100% poliester', 'Caracteristici': 'izolată, căptușită, guler ridicat, patru buzunare, Dress Safely', 'Cod produs': '2MDJCN06R'},
  notes=['Mărimile sunt italiene; magazinul atenționează că pot diferi de cele europene.'])

w(9761,
  f'<p>{PRIMIGI} PIKGT 88753 sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")}, negre, izolate, din material sintetic și piele întoarsă, cu interior din lână. Membrana GORE-TEX® e subțire, impermeabilă și rezistentă la vânt, deci picioarele rămân uscate și calde iarna.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, iar șiretul se strânge după picior, deci cizma merge și pe un picior mai lat. Partea de sus ridicată rigidizează glezna pe teren denivelat.</p>'
  '<p>Talpa și branțul sunt făcute pentru mers mult prin zăpadă:</p>'
  + L(('Talpă', 'exterioară, din cauciuc, cu absorbția șocului.'), ('Branț', 'cu contur.'), ('Interior', 'textil, ușor de ținut curat.'))
  + '<p>Numerele 36-40 sunt pentru copii de pe la 12 ani în sus.</p>',
  [('model', 'Primigi Cizme de iarna copii culoarea negru, PIKGT 88753'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinatia materialului sintetic cu pielea intoarsa'), ('lână', 'Un model cu interior din lână'), GTX,
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('șiret', 'Fixare: cu snur'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('teren', 'suprafețe neuniforme'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('șoc', 'Absorbtia socului'),
   ('branț', 'Brant confortabil, cu contur'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Primigi PIKGT 88753', 'Material': 'sintetic și piele întoarsă, interior textil și lână, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, izolate, șiret, cutie lată', 'Cod produs': 'PIKGT 88753'})

w(9762,
  f'<p>{A("/brand/ugg/", "UGG")} LOWMEL 1152410K sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} maro, joși, din piele întoarsă și material textil, cu căptușeala UGGplush din lână și lyocell, care ține căldura înăuntru. Sunt pentru zilele mai reci, pe străzile orașului.</p>'
  '<p>Vârful rotund lasă loc degetelor, iar șiretul se strânge după forma piciorului. Are și șireturi suplimentare, pentru alt aspect al legăturii.</p>'
  '<p>Construcția e solidă:</p>'
  + L(('Contrafort', 'rigidizat, împreună cu gulerul.'), ('Talpă', 'plată, din cauciuc.'), ('Interior', 'material textil.'))
  + '<p>Numerele 31-36 se poartă, cam de la 6 ani în sus.</p>',
  [('model', 'UGG Încălțăminte pentru copii LOWMEL maro 1152410K'), ('joși', 'încălțăminte joasă și căptușită'), ('material', 'Partea superioară din piele întoarsă și material textil'),
   ('UGGplush', 'Căptușeala UGGplush din lână și lyocell asigură menținerea căldurii la interior'), ('reci', 'zilele mai reci'), ('urban', 'condiții meteorologice urbane'),
   ('vârf', 'Vârful rotund oferă degetelor spațiu adecvat'), ('șiret', 'Fixare: cu snur'), ('șireturi extra', 'Șireturile suplimentare facilitează schimbarea aspectului legăturii'),
   ('contrafort', 'Contrefortul rigidizat , împreună cu gulerul'), ('talpă', 'Talpa plată din cauciuc'), ('interior', 'Material textil')],
  {'Model': 'UGG LOWMEL', 'Material': 'piele întoarsă și textil, căptușeală UGGplush (lână și lyocell), talpă din cauciuc', 'Caracteristici': 'căptușiți, șireturi suplimentare, contrafort rigidizat', 'Cod produs': '1152410K'})
