import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9292,
  f'<p>{GEOX} GISLI J654NB sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, din material textil și piele ecologică, ușori și făcuți pentru purtat zilnic, cu sistemul Geox Respira în talpă și profil scurt.</p>'
  '<p>Au șiret, fermoar lateral și arici: fermoarul deschide pantoful, ca piciorul să intre ușor, iar șiretul rămâne reglat. Vârful rotund, ușor rigid, lasă degetele să stea liber.</p>'
  '<p>Pe dinăuntru și pe dedesubt:</p>'
  + L(('Branț', 'din piele, previne frecarea.'), ('Călcâi', 'contor rigid.'), ('Interior', 'textil, sintetic și piele naturală.'), ('Talpă', 'exterioară, din cauciuc.'))
  + '<p>Numerele 36-39 sunt pentru copii mari, de obicei de la 12 ani în sus.</p>',
  [('model', 'Sneakers pentru copii GISLI culoarea alb, J654NB.0BCEW'), ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'ideal pentru purtarea zilnică'),
   RESPIRA, ('profil', 'Înălțime: mic de statură'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'), ('călcâi', 'Contorul de călcâi rigid'),
   ('interior', 'Interiorul: Material sintetic, Material textil, Piele naturala'), ('talpă', 'Talpa exterioară din cauciuc')],
  {'Model': 'Geox GISLI J654NB', 'Material': 'textil și piele ecologică, interior cu piele naturală, talpă din cauciuc', 'Caracteristici': 'șiret, fermoar lateral și arici, branț din piele, Geox Respira', 'Cod produs': 'J654NB.0BCEW'})

w(9293,
  f'<p>{GEOX} CIUFCIUF B655QA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, din material textil și piele ecologică, ușori și făcuți pentru purtat zilnic. Au sistemul Geox Respira în talpă și profil scurt, sub gleznă.</p>'
  '<p>Se închid cu scai, deci încălțatul unui copil mic durează câteva secunde, iar contorul rigidizat de la călcâi ține piciorul fix. Vârful e rotund.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'scai.'), ('Interior', 'textil, ușor de ținut curat.'), ('Material', 'textil și piele ecologică.'))
  + '<p>Numerele 20-23 se potrivesc copiilor de pe la 1 până pe la 3 ani.</p>',
  [('model', 'Sneakers pentru copii CIUFCIUF culoarea roz, B655QA.0BC14'), ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'ideal pentru purtarea zilnică'),
   RESPIRA, ('profil', 'Înălțime: mic de statură'), ('scai', 'Incheiere cu scai'), ('călcâi', 'Contorul de călcâi rigidizat'), ('vârf', 'Varf rotund'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Geox CIUFCIUF B655QA', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'Geox Respira, scai, profil scurt', 'Cod produs': 'B655QA.0BC14'})

w(9294,
  f'<p>{A("/brand/reima/", "Reima")} Mjosa este o {A("/categorie/bebe-imbracaminte-salopete-compleuri/", "salopetă softshell pentru bebeluși")} și copii mici, violet, cu membrană impermeabilă de 10000 mm și construcție rezistentă la vânt. Are umplutură sintetică ușoară și căptușeală din polar, deci e făcută pentru sezoanele de tranziție, cu ploaie și vânt.</p>'
  '<p>E lungă peste genunchi și are chingi din silicon reglabile la picioare, care țin crăcii pe loc peste cizme; gluga se detașează, iar benzile elastice se reglează după copil.</p>'
  '<p>Pentru joaca afară:</p>'
  + L(('Detalii reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Buzunare', 'cu fermoar.'), ('Material', 'rezistent la murdărie, cu acoperire hidrofobă.'))
  + '<p>Mărimile 74-98 sunt pentru copii între aproximativ 9 luni și 3 ani.</p>',
  [('model', 'Reima Salopetă pentru copii Mjosa violet 5100006D'), ('softshell', 'softshell tehnic'), ('membrană', 'Membrană impermeabilă (10000 mm H2O)'),
   ('vânt', 'Construcție softshell rezistentă la vânt'), ('umplutură', 'Umplutură sintetică ușoară și căptușeală din polar'), ('tranziție', 'anotimpurilor de tranziție'),
   ('lungime', 'Lungime peste genunchi și chingi reglabile din silicon pentru picioare'), ('glugă', 'Glugă detașabilă și benzi elastice reglabile'),
   ('reflectorizante', 'Detalii reflectorizante'), ('buzunare', 'Buzunare practice cu fermoar'), ('murdărie', 'Material rezistent la murdărie'), ('hidrofob', 'Acoperire hidrofobă')],
  {'Model': 'Reima Mjosa', 'Material': 'softshell 92% poliester, 8% elastan', 'Caracteristici': 'membrană 10000 mm, căptușeală polar, chingi la picioare, glugă detașabilă', 'Cod produs': '5100006D'},
  varsta_txt='9 luni - 3 ani')

w(9295,
  f'<p>{A("/brand/columbia/", "Columbia")} Arctic Blast este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de schi unisex")}, neagră, cu izolație sintetică groasă și tehnologia OMNI-SHIELD™, un strat hidrofob care respinge umezeala și murdăria. E făcută pentru pârtie și pentru activitățile de iarnă.</p>'
  '<p>Croiala e regular fit, cu lungime până la șolduri, iar fusta de zăpadă integrată și manșetele elastice opresc zăpada să intre pe dedesubt sau pe la mâneci.</p>'
  '<p>Detaliile de pârtie:</p>'
  + L(('Buzunar ski-pass', 'pentru permisul de schi.'), ('Buzunare', 'laterale cu fermoar și interioare.'), ('Glugă', 'fixă.'), ('Material', '100% poliamidă, căptușeală completă din poliamidă.'))
  + '<p>Mărimile 104-164 se potrivesc copiilor de cam 4-14 ani.</p>',
  [('model', 'Geacă de schi pentru copii Arctic Blast neagră 2089721'), ('izolație', 'Izolație sintetică groasă'), ('OMNI-SHIELD', 'Tehnologia OMNI-SHIELD'),
   ('hidrofob', 'favorizând rezistența la umiditate și murdărie'), ('pârtie', 'confort pe pârtie'), ('croială', 'Croială regular fit'), ('lungime', 'Lungime până la șolduri'),
   ('fustă', 'Fustă de zăpadă integrată'), ('manșete', 'Manșete elastice'), ('ski-pass', 'Buzunar pentru permisul de schi'), ('buzunare', 'Buzunare laterale cu fermoar'),
   ('interioare', 'Buzunare interioare'), ('glugă', 'Glugă fixă'), ('material', '100% Poliamidă'), ('căptușeală', 'Căptușeală completă')],
  {'Model': 'Columbia Arctic Blast', 'Material': '100% poliamidă, umplutură poliester', 'Caracteristici': 'geacă de schi, OMNI-SHIELD™, fustă de zăpadă, buzunar ski-pass', 'Cod produs': '2089721'})

w(9300,
  f'<p>{A("/brand/karl-lagerfeld/", "Karl Lagerfeld")} Z30607 este o {A("/categorie/geci-jachete/", "geacă de tranziție pentru fete")}, maro, din poliester neted, cu căptușeală din viscoză, fără izolație și fără glugă. Se poartă primăvara și toamna, ca strat exterior.</p>'
  '<p>Croiala e simplă, cu guler, iar fermoarul o închide până sus. Magazinul precizează că mărimile sunt italiene, convertite la cele europene, deci merită verificat tabelul de mărimi.</p>'
  '<p>Pe scurt:</p>'
  + L(('Buzunare', 'oblice.'), ('Căptușeală', '100% viscoză.'), ('Material', '100% poliester.'), ('Glugă', 'nu are.'))
  + f'<p>Pe vânt, capul se acoperă cu o piesă din {A("/categorie/caciuli-manusi-accesorii/", "căciulile și accesoriile pentru fete")}. Mărimile 114-150 sunt pentru copii de pe la 6 până pe la 12 ani.</p>',
  [('cod', 'Geacă copii culoarea maro, Z30607'), ('neizolat', 'Model neizolat'), ('neted', 'material neted'), ('căptușeală', 'Captuseala: 100% Viscoza'),
   ('tranziție', 'Izolare: tranzitional'), ('fără glugă', 'Gluga: fara gluga'), ('croială', 'Tăiere simplă'), ('guler', 'Model cu guler'), ('fermoar', 'Incheiere cu fermoar'),
   ('mărimi italiene', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('buzunare', 'Buzunare oblice'), ('material', 'Material de bază: 100% Poliester')],
  {'Model': 'Karl Lagerfeld Z30607', 'Material': '100% poliester, căptușeală 100% viscoză', 'Caracteristici': 'de tranziție, căptușită, guler, fermoar, fără glugă', 'Cod produs': 'Z30607'},
  comp={'slug': '/categorie/caciuli-manusi-accesorii/', 'motiv': 'geacă fără glugă'}, notes=['Mărimi italiene convertite la europene (după magazin).'])

w(9303,
  f'<p>{A("/brand/bobo-choses/", "Bobo Choses")} B126AC117 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă ușoară unisex")}, galbenă, din poliamidă colorată, căptușită, dar fără izolație, pentru zilele de tranziție. Poliamida face materialul mai rezistent la purtare.</p>'
  '<p>Croiala e oversize, cu umerii coborâți, deci geaca vine largă și lasă loc de un pulover; mânecile și marginea de jos au tiv elastic, care o strânge pe corp și o face ușor de îmbrăcat.</p>'
  '<p>Pentru vânt, geaca are:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea, cu clapă interioară.'), ('Guler', 'ridicat.'), ('Buzunare', 'două, laterale.'), ('Material', '100% poliamidă, căptușeală 100% poliester.'))
  + '<p>Mărimile duble, de la 89/98 la 149/155, sunt pentru copii de aproximativ 1-12 ani.</p>',
  [('cod', 'Geacă copii culoarea galben, B126AC117'), ('ușor', 'Model ușor'), ('rezistent', 'Poliamida asigură o durabilitate mai mare a produsului'), ('poliamidă', 'Materialul de baza: 100% Poliamida'), ('căptușeală', 'Captuseala: 100% Poliester'),
   ('neizolat', 'Izolare: neizolat'), ('tranziție', 'Izolare: tranzitional'), ('oversize', 'Fit: oversize'), ('umeri', 'linie coborâtă a umerilor'),
   ('tiv', 'Mânecile și marginea inferioară sunt finisate cu un tiv elastic'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară'),
   ('guler', 'Gulerul ridicat'), ('buzunare', 'Două buzunare laterale')],
  {'Model': 'Bobo Choses B126AC117', 'Material': '100% poliamidă, căptușeală poliester', 'Caracteristici': 'oversize, fără izolație, fermoar cu clapă, tiv elastic', 'Cod produs': 'B126AC117'})

w(9310,
  f'<p>{A("/brand/primigi/", "Primigi")} PPE GTX 89346 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de zăpadă unisex")}, bleumarin, izolate, cu interior din lână și membrana GORE-TEX®, impermeabilă și rezistentă la vânt. Sunt pentru ger și zăpadă.</p>'
  '<p>Cutia degetelor e lată, cu loc pentru un picior mai plin, iar circumferința de sus se reglează cu șnururi cu opritor, ca zăpada să rămână afară.</p>'
  '<p>Mai au:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Absorbție', 'talpa absoarbe șocurile.'), ('Partea de sus', 'rigidizată.'), ('Material', 'textil și piele ecologică.'))
  + '<p>Numerele 36-39 sunt pentru copii mari, în general de la 12 ani în sus.</p>',
  [('model', 'Primigi Cizme de iarnă copii culoarea bleumarin, PPE GTX 89346'), ('zăpadă', 'Cizme de zăpadă pentru copii'), ('izolat', 'Model Izolat'),
   ('lână', 'Un model cu interior din lână'), ('GORE-TEX', 'Model cu membrana GORE-TEX'), ('cutie lată', 'Cutia lată a degetelor'),
   ('șnururi', 'Reglarea circumferinței superioare cu șnururi cu opritoare'), ('talpă', 'Talpa exterioară din cauciuc'), ('absorbție', 'Absorbtia socului'),
   ('rigidizat', 'Partea superioară rigidizată'), ('material', 'combinația materialului textil cu pielea ecologică')],
  {'Model': 'Primigi PPE GTX 89346', 'Material': 'textil și piele ecologică, interior din lână', 'Caracteristici': 'izolate, GORE-TEX®, șnur cu opritor, cutie lată a degetelor', 'Cod produs': '89346'})

w(9311,
  f'<p>{GEOX} WASHIBA J36HXA sunt {A("/categorie/adidasi/", "adidași înalți pentru fete")}, roz, din imitație de piele și material textil, cu talpa GEOX Respira™ cu membrană microporoasă, care elimină umezeala și ține apa afară.</p>'
  '<p>Profilul înalt ține glezna, iar aricii se prind și se desfac repede, așa că pantoful se pune ușor chiar și cu un picior mai plin.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Interior', 'căptușit cu material textil.'), ('Material', 'imitație de piele și textil.'))
  + '<p>Modelul are numere de la 24 până la 39, deci se găsește de la cam 2 ani până la adolescenți.</p>',
  [('model', 'Geox WASHIBA sneakers pentru copii roz J36HXA.05415'), ('material', 'Față din imitație de piele și material textil'), ('Respira', 'Talpă respirabilă GEOX Respira'),
   ('membrană', 'Membrana GEOX Respira™ protejează interiorul pantofului de pătrunderea apei'), ('profil', 'Profil înalt al încălțămintei'), ('arici', 'Închidere practică cu arici'),
   ('talpă', 'Talpă plată din cauciuc'), ('interior', 'Interior căptușit cu material textil')],
  {'Model': 'Geox WASHIBA J36HXA', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici, GEOX Respira™ cu membrană', 'Cod produs': 'J36HXA.05415'})

w(9317,
  f'<p>{A("/brand/mini-rodini/", "Mini Rodini")} Planet este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă subțire unisex")}, din nailon neted, căptușită cu plasă, fără izolație. Pe site apare roz, iar magazinul o dă albastră. E pentru primăvară și toamnă.</p>'
  '<p>Croiala e oversize, cu umerii coborâți, deci vine largă și lasă loc de straturi dedesubt; mânecile și marginea de jos au bătături, care o strâng la încheieturi și jos.</p>'
  '<p>Detaliile:</p>'
  + L(('Guler', 'moale.'), ('Închidere', 'fermoar.'), ('Căptușeală', 'plasă.'), ('Material', '100% nailon.'))
  + '<p>Mărimile duble, de la 80-86 până la 140-146, sunt pentru copii de pe la 1 până pe la 11 ani.</p>',
  [('model', 'Mini Rodini Geacă copii Planet 26210105'), ('neizolat', 'Model neizolat'), ('neted', 'tesatura neteda'), ('nailon', '100% Nailon'), ('plasă', 'Model captusit cu plasa'),
   ('tranziție', 'Izolare: tranzitional'), ('oversize', 'Fit: oversize'), ('umeri', 'linie coborâtă a umerilor'), ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'),
   ('guler', 'Model cu guler moale'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('culoare magazin', 'albastru')],
  {'Model': 'Mini Rodini Planet', 'Material': '100% nailon, căptușeală plasă', 'Caracteristici': 'oversize, fără izolație, bătături la mâneci și bază', 'Cod produs': '26210105'},
  notes=['Titlul de pe site spune roz; magazinul dă albastru.'])

w(9318,
  f'<p>{GEOX} WASHIBA J66HXA sunt {A("/categorie/adidasi/", "adidași înalți pentru fete")}, albi, din imitație de piele și material textil, cu aplicație decorativă și talpa Geox Respira™, care elimină umezeala. Se poartă la ținute casual.</p>'
  '<p>Închiderea e dublă, cu fermoar și șireturi: fermoarul deschide pantoful la încălțat, iar șireturile rămân reglate. Gulerul ușor întărit ține glezna, iar profilul înalt o acoperă.</p>'
  '<p>Ce mai au:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Interior', 'material sintetic și textil.'))
  + '<p>Numerele 28-35 sunt pentru copii de aproximativ 4-11 ani.</p>',
  [('model', 'Geox WASHIBA sneakers pentru copii albi J66HXA.0NFKN'), ('material', 'Partea superioară din imitație de piele și material textil'), ('aplicație', 'Aplicație decorativă'),
   ('Respira', 'Talpa respirabilă Geox Respira'), ('casual', 'stilul casual'), ('închidere', 'Închiderea dublă cu fermoar și șireturi'), ('guler', 'Gulerul superior ușor întărit'),
   ('talpă', 'Talpa plată din cauciuc'), ('călcâi', 'Călcâi întărit'), ('interior', 'Interiorul din material sintetic și textil'), ('profil', 'Profilul înalt')],
  {'Model': 'Geox WASHIBA J66HXA', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, fermoar și șireturi, Geox Respira™', 'Cod produs': 'J66HXA.0NFKN'},
  notes=['Titlul de pe site nu are culoare; magazinul arată alb.'])
print('lot 19 scris')
