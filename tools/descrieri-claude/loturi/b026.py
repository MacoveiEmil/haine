import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9613,
  f'<p>{BIO} 261131 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} verzi, din piele naturală și material sintetic, făcuți în parteneriatul Biomecanics Podology, cu podologi. Stilul e casual, pentru zilele în care copilul e mereu în mișcare.</p>'
  '<p>Aricii și cureaua reglabilă se strâng după cât de lat sau de îngust e piciorul, iar gulerul moale de sus nu irită glezna. Branțurile se scot, deci lungimea piciorului se poate verifica direct pe ele.</p>'
  '<p>Pentru mersul de zi cu zi, pantoful are:</p>'
  + L(('Stabilizator lateral', 'ține piciorul drept în mișcare.'), ('Călcâi', 'întărit.'), ('Branț', 'antibacterian și anti-miros, detașabil.'), ('Talpă', 'flexibilă, din cauciuc.'))
  + '<p>Mărimile 18-25 sunt pentru copii de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele verzi 261131'), ('material', 'Partea superioară din piele naturală și sintetică'), ('podologi', 'creat în colaborare cu podologi'),
   ('parteneriat', 'Parteneriatul Biomecanics Podology'), ('casual', 'stilurile casual și streetwear'), ('zile active', 'zilele active'),
   ('arici', 'Închiderea cu arici și curea reglabilă facilitează încălțarea rapidă și ajustarea'), ('guler', 'Gulerul superior moale minimizează riscul de iritații în jurul gleznei'),
   ('branț detașabil', 'Branțurile detașabile permit curățarea și înlocuirea ușoară'), ('stabilizator', 'Stabilizatorul lateral ajută la menținerea piciorului într-o poziție corectă'),
   ('călcâi', 'Călcâiul întărit'), ('branț', 'Branțul antibacterian și anti-miros'), ('talpă', 'Talpa flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261131', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici și curea reglabilă, stabilizator lateral, branț antibacterian detașabil', 'Cod produs': '261131'})

w(9615,
  f'<p>Cizmele de iarnă {GEOX} J169XC sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme pentru băieți")} bleumarin, izolate, din material textil și piele ecologică, pentru zilele reci. Interiorul e textil și se ține ușor curat, iar talpa are sistemul Geox Respira, cu trei straturi perforate.</p>'
  '<p>Velcro-ul se strânge pe picior și se desface repede, iar bucla de la spate ajută copilul să tragă cizma pe picior singur. Contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece înăuntru.</p>'
  '<p>Pe zăpadă bătută și pe trotuar, contează vârful și talpa:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'), ('Interior', 'textil.'))
  + '<p>Numerele 28-35 se poartă, cu aproximație, între 4 și 11 ani.</p>',
  [('model', 'Geox Cizme de iarnă pentru copii culoarea bleumarin, J169XC.0FU50'), ('izolat', 'Model Izolat'), ('material', 'combinatia materialului textil cu pielea ecologica'),
   ('interior', 'Model cu interior textil'), RESPIRA, ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('călcâi', 'Contorul de călcâi rigid'), ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'),
   ('vârf', 'Cutie rotunda, intarita'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('interior textil', 'Interior textil')],
  {'Model': 'Geox J169XC', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'izolate, velcro, buclă la spate, Geox Respira', 'Cod produs': 'J169XC.0FU50'})

w(9619,
  f'<p>{GEOX} FADINLIGHT J55M4A sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil scurt, din material sintetic și textil, cu detalii decorative. Se pun fără legat: șireturile sunt elastice și se prind cu un cârlig, deci copilul se încalță repede, înainte de joacă.</p>'
  '<p>Călcâiul e întărit și căptușit cu o umplutură moale, care îl ferește de frecare, iar partea de sus rigidizată păstrează forma pantofului pe picior.</p>'
  '<p>Dedesubt și înăuntru, pantoful are:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, perforată, care ventilează.'), ('Inserție', 'detașabilă, se scoate la curățat.'), ('Vârf', 'cutie rotundă, întărită.'), ('Talpă', 'din cauciuc.'))
  + '<p>Pe site, numerele 24-35 acoperă, de regulă, vârsta de 2-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii FADINLIGHT culoarea roz, J55M4A.0KNGN'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatia materialului sintetic cu cel textil'),
   ('decor', 'Detalii decorative'), ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'), ('rigidizat', 'Partea superioară rigidizată'), RESPIRA,
   ('ventilare', 'imbunatateste ventilarea'), ('inserție', 'Inserție detașabilă, ușor de curățat'), ('vârf', 'Cutie rotunda, intarita'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox FADINLIGHT', 'Material': 'sintetic și textil, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, inserție detașabilă, Geox Respira', 'Cod produs': 'J55M4A.0KNGN'})

w(9620,
  f'<p>{GEOX} SPRINTYE J66FWB sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, ușori, în stil sportiv și casual, buni pentru școală și pentru ieșirile de după-amiază. În talpă au membrana microporoasă Geox Respira™, care scoate umezeala și păstrează piciorul uscat.</p>'
  '<p>Închiderea combină șiretul cu scaiul, deci pantoful se potrivește exact pe piciorul copilului. Branțurile se scot, așa că piciorul se poate măsura pe ele când e vremea unei mărimi noi.</p>'
  '<p>Ce ține piciorul în pantof la alergat:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Guler', 'ușor întărit, în jurul gleznei.'), ('Talpă exterioară', 'din spumă.'), ('Partea de sus', 'material textil și sintetic.'))
  + '<p>Mărimile 28-35 sunt potrivite, în general, pentru 4-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii SPRINTYE roz J66FWB.0119J'), ('stil', 'Stilul lor sportiv, dar și casual'), ('școală', 'atât pentru școală, cât și pentru ieșirile de după-amiază'),
   ('Respira', 'Tehnologia GEOX Respira™ cu membrană microporoasă'), ('uscat', 'menținând picioarele uscate'), ('închidere', 'Închidere cu șireturi și scai permite o ajustare precisă pe piciorul copilului'),
   ('branțuri', 'Branțuri detașabile'), ('călcâi', 'Călcâi ușor întărit'), ('guler', 'Gulerul superior ușor întărit'), ('talpă', 'Talpă exterioară din spumă'),
   ('material', 'Partea superioară din material textil și sintetic')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil și sintetic, interior textil, talpă din spumă', 'Caracteristici': 'Geox Respira™, șireturi și scai, branțuri detașabile', 'Cod produs': 'J66FWB.0119J'})

w(9624,
  f'<p>Botinele de iarnă {BIO} 261106 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "încălțăminte pentru bebeluși")} bej, din piele naturală și material sintetic cu finisaj lucios, căptușite cu lână care ține căldura în zilele reci. Sunt făcute în parteneriatul Biomecanics Podology.</p>'
  '<p>Aricii și cureaua reglabilă strâng gheata pe picior, fie că e lat, fie că e îngust, și o fac ușor de încălțat. Stabilizatorii laterali țin piciorul într-o poziție corectă.</p>'
  '<p>Pentru primii ani de mers prin frig:</p>'
  + L(('Vârf', 'rotund, cauciucat, apără degetele.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Interior', 'lână.'))
  + '<p>Numerele 18-25 sunt, aproximativ, pentru copii de 1-3 ani.</p>',
  [('model', 'Botinele de iarnă Biomecanics 261106'), ('material', 'Partea superioară din piele naturală și material sintetic cu finisaj lucios'),
   ('lână', 'Căptușeala din lână în interiorul ghetei ajută la menținerea căldurii în zilele reci'), ('parteneriat', 'Parteneriatul Biomecanics Podology'),
   ('arici', 'Închiderea cu arici și cureaua reglabilă facilitează ajustarea și încălțarea rapidă'), ('stabilizatori', 'Stabilizatorii laterali ajută la menținerea piciorului într-o poziție corectă'),
   ('vârf', 'Vârful rotund, cauciucat asigură protecția degetelor'), ('talpă', 'Talpa flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261106', 'Material': 'piele naturală și sintetic, căptușeală din lână, talpă din cauciuc', 'Caracteristici': 'botine de iarnă, arici și curea reglabilă, vârf cauciucat', 'Cod produs': '261106'},
  notes=['Titlul spune bej; h1 și atributul magazinului spun multicolor.', 'Sunt botine de iarnă, listate la Pantofi.'])

w(9626,
  f'<p>{A("/brand/columbia/", "Columbia")} Marquam Peak Fusion 2090211 este o {A("/categorie/geci-jachete/", "geacă de iarnă pentru fete")}, neagră, izolată și căptușită, făcută parțial din poliester reciclat. Are tehnologia Omni-Heat™ Infinity, o membrană aurie care ține de cald, deci e pentru frigul de iarnă.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri pe corp, deci încape un pulover sub ea. Gulerul ridicat și gluga fixă apără gâtul și capul de frig.</p>'
  '<p>La închidere și la glugă, geaca are:</p>'
  + L(('Închidere', 'fermoar și velcro.'), ('Blăniță', 'artificială, detașabilă, pe glugă.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', '85% poliester, 15% bumbac.'))
  + '<p>Mărimile 116-164 sunt pentru copii de pe la 6 până pe la 14 ani.</p>',
  [('model', 'Columbia Geaca copii Marquam Peak Fusion culoarea negru, 2090211'), ('izolat', 'Model izolat cu captuseala'), ('reciclat', 'realizat partial din poliester reciclat'),
   ('Omni-Heat', 'Omni-Heat ™ Infinity este o membrana speciala de aur care va mentine cald'), ('croială', 'Tăiere simplă, fără blocare'),
   ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('închidere', 'Fixarea cu fermoar si velcro'), ('blăniță', 'Gluga cu blanita artificiala, detasabila'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('material', '85% Poliester , 15% Bumbac')],
  {'Model': 'Columbia Marquam Peak Fusion', 'Material': '85% poliester, 15% bumbac; umplutură 100% poliester reciclat', 'Caracteristici': 'izolată, Omni-Heat™ Infinity, glugă fixă cu blăniță detașabilă', 'Cod produs': '2090211'})

w(9627,
  f'<p>{A("/brand/reima/", "Reima")} Uumaja 5100340A este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă matlasată unisex")}, turcoaz, cu izolație sintetică medie, pentru temperaturi între +5 și -10°C. Membrana impermeabilă de 10 000 mm H₂O și țesătura rezistentă la vânt o fac bună pentru ploaie ușoară, vânt rece și sezonul de tranziție.</p>'
  '<p>Croiala e regulară, iar lungimea ajunge până la șolduri, deci acoperă spatele când copilul se apleacă. Manșetele cu bordură elastică strâng la încheieturi și țin frigul afară.</p>'
  '<p>Pentru zilele ude de toamnă, mai contează:</p>'
  + L(('Glugă', 'detașabilă, cu guler ridicat.'), ('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, cu închidere.'),
      ('Material', 'poliester acoperit cu poliuretan, rezistent la murdărie.'), ('Respirabilitate', '7 000 g/m²/24h.'))
  + '<p>Mărimile 104-164 se potrivesc, în mare, copiilor de 4-14 ani.</p>',
  [('model', 'Reima Geacă petrecută pentru copii Uumaja turcoaz 5100340A'), ('matlasat', 'Finisaj matlasat al materialului'), ('izolație', 'Izolație sintetică medie'),
   ('temperatură', '+5 până la -10°C'), ('membrană', 'Membrană impermeabilă cu parametri 10 000 mm H₂O'), ('vânt', 'Structură a țesăturii rezistentă la vânt'),
   ('ploaie', 'protecția împotriva ploilor ușoare'), ('tranziție', 'sezoanele de tranziție'), ('croială', 'Croială regulară cu lungime până la șolduri'),
   ('manșete', 'Manșete cu bordură elastică'), ('glugă', 'Glugă detașabilă și guler ridicat'), ('fermoar', 'Închidere cu fermoar pe toată lungimea'),
   ('buzunare', 'Buzunare laterale cu închidere'), ('material', '100% Poliester acoperit cu strat de poliuretan'), ('murdărie', 'Material rezistent la murdărie'),
   ('respirabilitate', '7 000 g/m²/24h')],
  {'Model': 'Reima Uumaja', 'Material': '100% poliester acoperit cu poliuretan, umplutură 100% poliester', 'Caracteristici': 'membrană 10 000 mm, 7 000 g/m²/24h, izolație medie, glugă detașabilă', 'Cod produs': '5100340A'})

w(9628,
  f'<p>Cizmele de iarnă {A("/brand/primigi/", "Primigi")} PPE GTX 89346 sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme pentru băieți")} verzi, ușor izolate, din material textil și imitație de piele întoarsă, cu membrana GORE-TEX®, impermeabilă și rezistentă la vânt. Interiorul e din material textil și lână, pentru zăpadă și zile ude.</p>'
  '<p>Cutia lată a degetelor nu le strânge, deci încap bine și pe un picior mai lat. Șiretul rapid cu opritor și velcro-ul se reglează repede, iar partea de sus ridicată rigidizează glezna pe teren denivelat.</p>'
  '<p>Talpa și branțul au fiecare rolul lor:</p>'
  + L(('Talpă exterioară', 'din cauciuc, cu caneluri.'), ('Talpă intermediară', 'din spumă EVA ușoară.'), ('Primigi Sky Effect', 'branț căptușit cu piele moale, detașabil.'), ('Călcâi', 'contrafort rigid.'))
  + '<p>Numerele 30-39 sunt pentru copii de pe la 6 ani în sus.</p>',
  [('model', 'Primigi Cizme de iarnă pentru copii culoarea verde, PPE GTX 89346'), ('izolare', 'Izolare usoara'), ('material', 'combinația materialului textil cu pielea întoarsă'),
   ('GORE-TEX', 'Membrana GORE-TEX® utilizată în acest model oferă un nivel ridicat de impermeabilitate și protecție împotriva vântului'), ('lână', 'Material textil, Lana'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('șireturi', 'Sistemul rapid de șireturi cu opritoare și o închidere suplimentară cu velcro'),
   ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('teren', 'suprafețe neuniforme'), ('talpă', 'Talpa exterioară din cauciuc cu caneluri'),
   ('EVA', 'Talpa intermediară este realizată din spumă EVA ușoară'), ('Sky Effect', 'Primigi Sky Effect'), ('branț piele', 'captusit in piele moale'),
   ('inserție', 'Inserție detașabilă, ușor de curățat'), ('călcâi', 'Contorul de călcâi rigid')],
  {'Model': 'Primigi PPE GTX 89346', 'Material': 'textil și imitație de piele întoarsă, interior textil și lână', 'Caracteristici': 'GORE-TEX®, ușor izolate, șiret rapid și velcro, cutie lată a degetelor', 'Cod produs': 'PPE GTX 89346'},
  notes=['Magazinul precizează că „impermeabil” nu garantează impermeabilitatea completă.'])

w(9635,
  f'<p>{GEOX} ASSISTER J45E9B sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, cu profil scurt, din material textil și piele ecologică, cu lumini în talpă care se aprind la fiecare pas. Pe drumurile de seară, copilul se vede de departe.</p>'
  '<p>Șireturile elastice cu cârlig și bucla de la spate îi lasă pe cei mici să se încalțe și să se descalțe fără nod, iar partea de sus rigidizată ține forma pantofului.</p>'
  '<p>Talpa și interiorul sunt simple:</p>'
  + L(('Geox Respira', 'trei straturi perforate în talpă.'), ('Vârf', 'rotund.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'din cauciuc.'))
  + '<p>Mărimile 24-27 se poartă, cam de la 2 până la 4 ani.</p>',
  [('model', 'Geox Sneakers pentru copii ASSISTER culoarea alb, J45E9B.0GFHH'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('lumini', 'Pe talpă, lumini care se aprind în timp ce mergi'), ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('rigidizat', 'Partea superioară rigidizată'), RESPIRA, ('vârf', 'Varf rotund'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox ASSISTER', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini în talpă, șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J45E9B.0GFHH'})

w(9651,
  f'<p>Geaca {A("/brand/adidas/", "adidas")} KQ6169 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, maro, cu imprimeu cu motiv animal, gândită pentru iarnă. Are izolație groasă din puf sintetic și tehnologia CLIMAWARM™, care păstrează căldura corpului în zilele reci.</p>'
  '<p>Croiala e simplă, iar lungimea ajunge până la șolduri, deci spatele rămâne acoperit când copilul stă jos. Tivul are șnur și se strânge, ca aerul rece să nu intre pe dedesubt.</p>'
  '<p>În rest, geaca e închisă bine la frig:</p>'
  + L(('Guler', 'ridicat, apără gâtul.'), ('Buzunare', 'laterale, tip slip-on, pentru mâini reci.'), ('Căptușeală', 'sintetică, completă.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 140-170 merg, aproximativ, de la 10 la 15 ani.</p>',
  [('model', 'adidas Geacă petrecută pentru copii maro KQ6169'), ('matlasat', 'Construcția matlasată'), ('motiv', 'Imprimeu cu motiv animal'), ('iarnă', 'propunere de iarnă'),
   ('izolație', 'Izolație groasă din puf sintetic'), ('CLIMAWARM', 'Tehnologia CLIMAWARM™ ajută la menținerea căldurii corpului'), ('croială', 'Croială simplă'),
   ('lungime', 'lungimea până la șolduri'), ('tiv', 'Tiv cu șnur permite ajustarea și protecția împotriva rafalelor de aer rece'), ('guler', 'Guler ridicat'),
   ('buzunare', 'Buzunare laterale tip slip-on'), ('mâini', 'pentru a încălzi mâinile'), ('căptușeală', 'Căptușeală sintetică completă'), ('material', '100% Poliester')],
  {'Model': 'adidas KQ6169', 'Material': '100% poliester, umplutură și căptușeală din poliester', 'Caracteristici': 'CLIMAWARM™, puf sintetic, tiv cu șnur, guler ridicat', 'Cod produs': 'KQ6169'})
