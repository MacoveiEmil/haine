import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GUESS = A('/brand/guess/', 'GUESS')
ADI = A('/brand/adidas/', 'adidas')
ACC = '/categorie/unisex-accesorii-caciuli-manusi-accesorii/'
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
BEBE = '/categorie/bebe-imbracaminte-geci-jachete/'

w(14987,
  f'<p>Șosetele de schi {A("/brand/columbia/", "Columbia")} SKI SOCKS KIDS albastre sunt un {A(ACC, "accesoriu unisex")} pentru pârtie și sporturi de iarnă. Fibra Thermolite ține de cald chiar și după multe ore pe zăpadă, iar grosimea medie păstrează un echilibru între căldură și respirabilitate.</p>'
  '<p>Tibia și talpa au o căptușeală moale, glezna are formă anatomică, iar bolta plantară e susținută. Zonele din plasă lasă piciorul să se aerisească, iar lycra ajută șoseta să stea pe loc.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Pachet', 'o pereche.'), ('Material', '78% poliester (fibră thermolite), 15% poliester, 5% nailon, 2% elastan.'), ('Cod produs', '253384.'))
  + '<p>Mărimile 31-34 până la 39-42 se potrivesc orientativ copiilor de la 6 ani în sus.</p>',
  [('model', 'Columbia SKI SOCKS KIDS'), ('culoare', 'Albastru (albastru / mix / alb)'), ('schi', 'sunt potrivite pentru schi și sporturi de iarnă'),
   ('Thermolite', 'Datorită tehnologiei Thermolite®, oferă o izolare termică avansată'), ('pârtie', 'chiar și în cazul unei șederi îndelungate pe pârtie'),
   ('medie', 'Greutatea medie asigură un echilibru optim între căldură și respirabilitate'), ('tibie', 'Umplutura moale la nivelul tibiei și al tălpii'),
   ('gleznă', 'Forma anatomică a gleznei și susținerea bolții plantare'), ('plasă', 'zonele din plasă respirabilă'), ('lycra', 'elastan lycra pentru o mai bună aderență'),
   ('pereche', 'set cu 1 pereche'), ('material', '78 % poliester (fibră thermolite), 15 % poliester, 5 % nailon, 2 % elastan')],
  {'Model': 'Columbia SKI SOCKS KIDS', 'Material': 'poliester Thermolite, nailon, elastan', 'Caracteristici': 'Thermolite, căptușeală la tibie și talpă', 'Cod produs': '253384'},
  notes=['Titlul site-ului nu are numele modelului (SKI SOCKS KIDS).'])

w(14992,
  f'<p>Șosetele {A("/brand/reima/", "Reima")} NILKAT roz sunt un {A(ACC, "accesoriu unisex")} practic pentru zilele obișnuite și pentru sport. Pachetul are două perechi din tricot elastic, care stau bine pe picior.</p>'
  '<p>Materialul e rezistent, deci șosetele țin și la purtare frecventă, bune pentru copiii care se mișcă mult toată ziua. Compoziția e aproape în întregime din poliamidă reciclată.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Pachet', 'două perechi.'), ('Material', '97% poliamidă reciclată, 3% elastan.'), ('Cod produs', '240015.'))
  + '<p>Mărimile 22/25 până la 38-41 se potrivesc orientativ copiilor de la 1 an în sus.</p>',
  [('model', 'REIMA NILKAT'), ('culoare', 'Roz (roz / alb / negru)'), ('zilnic', 'un accesoriu practic pentru activități zilnice și sportive'),
   ('perechi', 'Pachetul conține două perechi de șosete confecționate din tricot elastic'), ('picior', 'se așază excelent pe picior'),
   ('rezistă', 'șosetele rezistă chiar și la utilizare frecventă'), ('activi', 'Sunt ideale pentru copiii activi'), ('material', '97 % poliamidă reciclată, 3 % elastan')],
  {'Model': 'Reima NILKAT', 'Material': '97% poliamidă reciclată, 3% elastan', 'Caracteristici': '2 perechi, tricot elastic', 'Cod produs': '240015'})

w(8424,
  f'<p>Geaca {ADI} JL7390 roz este o {A(BEBE, "geacă pentru bebeluși")} ușor izolată, din material matlasat, cu tehnologia climawarm, respirabilă, care ține de cald pe vreme rece. Gulerul ridicat și gluga detașabilă apără suplimentar de frig.</p>'
  '<p>Se închide cu fermoar, are buzunare oblice, iar mânecile și marginea de jos sunt finisate simplu. Căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Umplutură', 'sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 62-104 sunt pentru copii de aproximativ 3 luni - 4 ani.</p>',
  [('cod', 'JL7390'), ('culoare', 'culoarea roz'), ('izolat', 'Model ușor izolat confecționat din material matlasat'), ('climawarm', 'Tehnologia climawarm ™ respirabila asigura caldura si confort in conditii de vreme rece'),
   ('glugă', 'Gulerul ridicat și gluga detașabilă oferă protecție suplimentară împotriva frigului'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare oblice'),
   ('mâneci', 'Mâneci și marginea inferioară finisate cu tăiere'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('material', '100% Poliester'), ('umplutură', 'sintetică'),
   ('croială', 'Croială: regular fit')],
  {'Model': 'adidas JL7390', 'Material': '100% poliester', 'Caracteristici': 'climawarm, glugă detașabilă, matlasată', 'Cod produs': 'JL7390'})

w(8427,
  f'<p>Geaca {GUESS} J5YQ30 neagră este o {A(GF, "geacă de tranziție pentru fete")} neizolată, dintr-un material ușor, cu căptușeală. Poliamida din compoziție o face mai rezistentă, iar materialul conține plastic reciclat.</p>'
  '<p>Croiala e supradimensionată, cu umerii coborâți, deci mișcarea nu e limitată. Gulerul ridicat apără de frig, iar fermoarul pe toată lungimea are clapă rezistentă la vânt, cu capse. Mânecile se termină cu elastic.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '58% poliamidă, 42% poliester.'), ('Căptușeală', '100% poliester.'), ('Glugă', 'nu are.'), ('Lungime', '45 cm la mărimea 158-166.'))
  + '<p>Mărimile încep la 118-122 și ajung la 167, pentru copii de aproximativ 6-14 ani.</p>',
  [('cod', 'J5YQ30 WHCH2'), ('culoare', 'culoarea negru'), ('neizolat', 'Model neizolat confecționat din dintr-un material ușor'),
   ('poliamidă', 'Conținutul de poliamidă crește durabilitatea produsului'), ('reciclat', 'Conține plastic reciclat'), ('supradimensionat', 'Croială: supradimensionat'),
   ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor nu limitează mobilitatea'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea, cu clapă rezistentă la vânt, cu capse'), ('mâneci', 'Mâneci finisate cu o coadă elastică'),
   ('material', '58% Poliamida, 42% Poliester'), ('căptușeală', '100% Poliester'), ('glugă', 'fără glugă'), ('lungime', 'Lungimea: 45 cm'), ('mărime', '158 - 166 cm')],
  {'Model': 'GUESS J5YQ30', 'Material': '58% poliamidă, 42% poliester', 'Caracteristici': 'neizolată, oversize, guler ridicat', 'Cod produs': 'J5YQ30.WHCH2'})

w(8431,
  f'<p>Geaca {GUESS} J5BL22 roz este o {A(GF, "geacă de iarnă pentru fete")} izolată, din țesătură ornamentată, cu izolație sintetică medie spre groasă, care ține de cald la temperaturi mai scăzute. Are glugă integrată și căptușeală completă.</p>'
  '<p>Se închide cu fermoar, iar mânecile se termină cu elastic. Cele două buzunare laterale au fermoar, ca lucrurile mici să rămână la locul lor.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Croială', 'regular fit.'), ('Lungime', '51 cm la mărimea 136-146.'))
  + '<p>Pe site sunt mărimile de la 122-125 la 167, pentru copii de cam 7-14 ani.</p>',
  [('cod', 'J5BL22 WI140'), ('culoare', 'culoarea roz'), ('izolat', 'Model izolat confecționat din material modelat'),
   ('izolație', 'Un model cu izolație sintetică care va oferi un confort suplimentar la temperaturi mai scăzute'), ('groasă', 'medie, groasă'), ('ornament', 'Tesatura ornamentata'),
   ('glugă', 'integrată'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('fermoar', 'Incheiere cu fermoar'), ('mâneci', 'Mâneci finisate cu o coadă elastică'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material', '100% Poliester'), ('croială', 'Croială: regular fit'), ('lungime', 'Lungimea: 51 cm'), ('mărime', '136-146 cm')],
  {'Model': 'GUESS J5BL22', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'izolată, glugă integrată, buzunare cu fermoar', 'Cod produs': 'J5BL22.WI140'})

w(8448,
  f'<p>Geaca {GUESS} J5BL07 maro este o {A(GF, "geacă de tranziție pentru fete")} din imitație de piele întoarsă, ușor izolată, cu umplutură sintetică și căptușeală completă. Poliesterul o face rezistentă la îndoire.</p>'
  '<p>Croiala e simplă, fără glugă, iar fermoarul o face ușor de pus și de scos. Buzunarele exterioare se închid, iar partea de mijloc e căptușită moale. Magazinul precizează că nu este impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '60 cm la mărimea 167.'), ('Lățime la umeri', '40 cm.'))
  + '<p>Mărimile merg între 122-125 și 167, potrivite orientativ copiilor de 7-14 ani.</p>',
  [('cod', 'J5BL07 WCFX0'), ('culoare', 'culoarea maro'), ('piele', 'Model ușor izolat confecționat din imitație de piele întoarsă'),
   ('îndoire', 'Poliesterul oferă o rezistență mai mare la îndoire'), ('umplutură', 'sintetică'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('glugă', 'fără glugă'), ('fermoar', 'Închiderea convenabilă cu fermoar îl face ușor de pus și scos'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('centru', 'Centrul moale căptușit crește confortul utilizării'), ('impermeabil', 'fără impermeabilitate'),
   ('material', '100% Poliester'), ('lungime', 'Lungimea: 60 cm'), ('umeri', 'Latimea in umeri: 40 cm'), ('mărime', 'Dimensiunile date pentru marimea: 167 cm')],
  {'Model': 'GUESS J5BL07', 'Material': '100% poliester, imitație de piele întoarsă', 'Caracteristici': 'ușor izolată, fermoar, buzunare închise', 'Cod produs': 'J5BL07.WCFX0'})

w(8481,
  f'<p>Geaca {ADI} JL7392 bleumarin este o {A(BEBE, "geacă pentru bebeluși")} matlasată, ușor izolată, cu glugă integrată și finisaj hidrofob pe exterior, care oprește umezeala să intre. Elementele reflectorizante o fac vizibilă după lăsarea întunericului.</p>'
  '<p>Fasonul e drept, se închide cu fermoar și are două buzunare laterale, plus buzunare interioare pentru lucrurile mici. Căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '39,5 cm la mărimea 86.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 62-104 se potrivesc orientativ copiilor de 3 luni - 4 ani.</p>',
  [('cod', 'JL7392'), ('culoare', 'culoarea albastru marin'), ('matlasat', 'Model usor izolat confecționat din din material matlasat'),
   ('hidrofob', 'Finisajul hidrofob al materialului exterior previne pătrunderea umezelii în interior'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('glugă', 'integrată'), ('fason', 'Fason drept'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare laterale'),
   ('interior', 'Buzunarele interioare suplimentare permit depozitarea în siguranță a obiectelor mici'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('material', '100% Poliester'), ('lungime', 'Lungimea: 39,5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 86 cm'), ('croială', 'Croială: regular fit')],
  {'Model': 'adidas JL7392', 'Material': '100% poliester', 'Caracteristici': 'ușor izolată, hidrofobă, reflectorizante', 'Cod produs': 'JL7392'})

w(8487,
  f'<p>Geaca {GUESS} K5YL04 bej este o {A(GF, "geacă de tranziție pentru fete")} neizolată, din material neted rezistent la apă, cu glugă integrată și o vestă izolată în interior. Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.</p>'
  '<p>Se închide cu cleme, are două buzunare laterale, iar mânecile se termină cu elastic. Talia se reglează cu șnur, pentru o potrivire pe siluetă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Căptușeală', 'completă, sintetică.'), ('Croială', 'regular fit.'))
  + '<p>Mărimile 88-96 până la 122-125 sunt pentru copii de aproximativ 1-7 ani.</p>',
  [('cod', 'K5YL04 WFVK0'), ('culoare', 'culoarea bej'), ('neizolat', 'Model neizolat confecționat din din material neted'), ('apă', 'Rezistent la apa'),
   ('impermeabil', 'nu garantează impermeabilitatea completă'), ('vestă', 'Are vesta izolata'), ('glugă', 'integrată'), ('cleme', 'Incheiere cu cleme'),
   ('buzunare', 'Două buzunare laterale'), ('mâneci', 'Mâneci finisate cu o coadă elastică'), ('talie', 'Talia este reglabila cu snur'),
   ('material', '100% Poliester'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('croială', 'Croială: regular fit')],
  {'Model': 'GUESS K5YL04', 'Material': '100% poliester', 'Caracteristici': 'rezistentă la apă, vestă izolată, talie cu șnur', 'Cod produs': 'K5YL04.WFVK0'},
  notes=['Magazinul o marchează și „produs pentru bebe”; pe site e la geci pentru fete.'])

w(8517,
  f'<p>Geaca {GUESS} L5BL16 neagră este o {A(GB, "geacă de iarnă pentru băieți")} matlasată, izolată, din material neted, cu izolație sintetică medie spre groasă pentru zilele reci. Gulerul ridicat și gluga fixă apără capul și gâtul.</p>'
  '<p>Croiala e simplă, buzunarele exterioare sunt oblice, iar căptușeala e completă, sintetică.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Lungime', '62 cm la mărimea 166-175.'), ('Lungimea mânecii', '58 cm.'), ('Lățime la umeri', '40 cm.'))
  + '<p>Mărimile de la 122-125 până la 175 se potrivesc orientativ copiilor de 7-16 ani.</p>',
  [('cod', 'L5BL16 W3090'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat confecționat din material neted'),
   ('izolație', 'Un model cu izolație sintetică care va oferi un confort suplimentar la temperaturi mai scăzute'), ('groasă', 'medie, groasă'), ('matlasat', 'Matlasat'),
   ('guler', 'Gulerul ridicat și gluga fixă'), ('tăiere', 'Tăiere simplă, fără blocare'), ('buzunare', 'Buzunare oblice exterioare'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 62 cm'), ('mânecă', '58 cm'), ('umeri', 'Latimea in umeri: 40 cm'),
   ('mărime', '166-175 cm')],
  {'Model': 'GUESS L5BL16', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, glugă fixă, guler ridicat', 'Cod produs': 'L5BL16.W3090'})

w(8528,
  f'<p>Geaca {A("/brand/boss/", "BOSS")} J52392 maro este o {A(GB, "geacă de tranziție pentru băieți")} subțire, din material matlasat cu izolație sintetică ușoară, care ține de cald când se răcește afară. Nu are glugă, iar căptușeala e completă.</p>'
  '<p>Croiala e simplă, se închide cu cleme și are două buzunare laterale plus unul pe piept. Bordurile au un material cu puțin elastan.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Borduri', '98% poliester, 2% elastan.'), ('Căptușeală', '100% poliester.'))
  + '<p>Mărimile 114-150 sunt pentru copii de cam 6-12 ani.</p>',
  [('cod', 'J52392'), ('culoare', 'culoarea maro'), ('subțire', 'Model subțire confecționat din material matlasat cu izolație sintetică'),
   ('reci', 'confort suplimentar la temperaturi mai reci'), ('ușoară', 'ușoară'), ('glugă', 'fără glugă'), ('căptușeală', 'cu căptușeală completă, sintetică'),
   ('tăiere', 'Tăiere simplă, fără blocare'), ('cleme', 'Incheiere cu cleme'), ('buzunare', 'Două buzunare laterale'), ('piept', 'Buzunar pe piept'),
   ('material', '100% Poliester'), ('conducte', '98% Poliester , 2% Elastan')],
  {'Model': 'BOSS J52392', 'Material': '100% poliester', 'Caracteristici': 'matlasată, ușor izolată, cleme', 'Cod produs': 'J52392'})
