import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(10036,
  f'<p>{GEOX} INEK J56ASA sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, joși, ușori, din material textil și sintetic, pentru purtat zilnic. Șireturile sunt plate, ca să nu apese pe arcada piciorului, iar velcro-ul închide pantoful repede.</p>'
  '<p>Bucla de la spate ajută la tras pantoful pe picior, iar contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece la mers.</p>'
  '<p>Restul construcției:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 32-35 sunt, cam, pentru 8-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii INEK culoarea roz, J56ASA.0BCKC'), ('profil', 'Înălțime: jos'), ('ușor', 'Model ușor'), ('material', 'combinația materialului textil cu cel sintetic'),
   ('zilnic', 'purtarea zilnică'), ('șireturi plate', 'Sireturile plate elimina punctele de presiune de pe arcada piciorului'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('călcâi', 'Contorul de călcâi rigid'), ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('vârf', 'Cutie rotunda, intarita'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox INEK', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi plate cu velcro, buclă la spate', 'Cod produs': 'J56ASA.0BCKC'})

w(10053,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} JW1104 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} roz, ușor izolată cu umplutură sintetică, din material neted, căptușită, pentru temperaturile mai reci. Gulerul ridicat și gluga detașabilă apără gâtul și capul de frig.</p>'
  '<p>Mânecile și tivul au bordură care strânge geaca la încheieturi și jos, deci vântul nu intră pe dedesubt. Un material are elastan, care îi dă puțină elasticitate.</p>'
  '<p>Se îmbracă repede:</p>'
  + L(('Închidere', 'fermoar și capse.'), ('Buzunare', 'cu închidere.'), ('Material', '100% poliester; inserții 94% poliester, 6% elastan.'))
  + '<p>Mărimile 110-176 sunt pentru copii de, în mare, 5-16 ani.</p>'.replace('de, în mare, 5-16 ani', 'de 5-16 ani, în mare'),
  [('model', 'adidas Originals Geacă copii culoarea roz, JW1104'), ('izolat', 'Model usor izolat'), ('neted', 'material neted cu izolatie sintetica'), ('reci', 'temperaturi mai reci'),
   ('căptușeală', 'Captuseala: cu captuseala'), ('guler, glugă', 'Gulerul ridicat și gluga detașabilă oferă protecție suplimentară împotriva frigului'),
   ('bordură', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('elastan', '94% Poliester , 6% Elastan'), ('închidere', 'Fixare cu fermoar si snap'),
   ('buzunare', 'Buzunare incheiate'), ('material', 'Material 1: 100% Poliester')],
  {'Model': 'adidas Originals JW1104', 'Material': '100% poliester; 94% poliester, 6% elastan', 'Caracteristici': 'ușor izolată, glugă detașabilă, guler ridicat, fermoar și capse', 'Cod produs': 'JW1104'})

w(10101,
  f'<p>{GEOX} IUPIDOO B3558C sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} violet, din piele întoarsă și imitație de piele, cu interior și branț din piele naturală. Tehnologia Geox Respira™ scoate umezeala spre exterior, iar sistemul Softly Cushioned preia vibrațiile la călcâi.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, deci cei mici sunt gata de joacă în câteva secunde, iar banda se strânge după cât de lat e piciorul.</p>'
  '<p>Pe scurt, din ce e făcut pantoful:</p>'
  + L(('Partea de sus', 'piele întoarsă și material sintetic.'), ('Interior', 'piele naturală.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 18-26 se potrivesc copiilor de aproximativ 1-4 ani.</p>',
  [('model', 'Geox IUPIDOO sneakers pentru copii violet B3558C.05422'), ('material', 'Partea superioară din piele întoarsă și imitație de piele'),
   ('interior', 'Interiorul căptușit cu piele naturală'), ('branț', 'Branțul din piele naturală'), ('Respira', 'Tehnologia GEOX Respira™'), ('umezeală', 'eliminând umezeala spre exterior'),
   ('Softly Cushioned', 'Amortizarea Softly Cushioned absoarbe vibrațiile'), ('călcâi', 'protecția călcâiului'),
   ('arici', 'Sistemul de închidere practic cu arici facilitează încălțarea și descălțarea rapidă'), ('parte de sus', 'Piele întoarsă, Material sintetic'),
   ('talpă', 'Talpa de cauciuc, plată')],
  {'Model': 'Geox IUPIDOO', 'Material': 'piele întoarsă și imitație de piele, interior și branț din piele naturală', 'Caracteristici': 'arici, Geox Respira™, Softly Cushioned', 'Cod produs': 'B3558C.05422'})

w(10105,
  f'<p>Vesta {A("/brand/columbia/", "Columbia")} Puffect 2090602 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "vestă matlasată unisex")}, neagră, cu izolație sintetică medie, pentru zilele de tranziție. Țesătura Ripstop limitează extinderea rupturilor, iar stratul Omni-Shield™ și impregnarea hidrofobă o apără de ploaie ușoară și murdărie.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, deci acoperă trunchiul, iar fără mâneci lasă brațele libere. Se poartă peste un hanorac sau sub o geacă de ploaie.</p>'.replace('Se poartă peste un hanorac sau sub o geacă de ploaie.', '')
  + '<p>Vesta mai are:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, cu fermoar.'), ('Căptușeală', 'sintetică, completă, din nailon.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 116-164 sunt pentru copii de în jur de 6-14 ani.</p>',
  [('model', 'Columbia Vestă pentru copii Puffect neagră 2090602'), ('matlasat', 'Țesătură matlasată durabilă'), ('izolație', 'Izolație sintetică medie'),
   ('tranziție', 'zilele de tranziție'), ('Ripstop', 'Construcția Ripstop'), ('rupturi', 'limitează extinderea rupturilor'),
   ('Omni-Shield', 'Tehnologia Omni-Shield™ – un strat hidrofob special pe țesătură ajută la protecția împotriva umezelii și a murdăriei'),
   ('ploaie', 'Impregnare hidrofobă – un strat suplimentar contribuie la protecția împotriva ploilor ușoare'), ('croială', 'Croială regulară'),
   ('lungime', 'Lungime până la șolduri'), ('fermoar', 'fermoarul simplu pe toată lungimea'), ('buzunare', 'buzunarele cu fermoar'),
   ('căptușeală', 'Căptușeală sintetică completă'), ('nailon', '100% Nailon'), ('material', '100% Poliester')],
  {'Model': 'Columbia Puffect', 'Material': '100% poliester, căptușeală 100% nailon', 'Caracteristici': 'vestă matlasată, izolație medie, Omni-Shield™, Ripstop', 'Cod produs': '2090602'})

w(10116,
  f'<p>Geaca de blugi {A("/brand/guess/", "Guess")} N6RL02 D4MS0 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de blugi pentru băieți")}, albastră, din denim cu 99% bumbac și 1% elastan, neizolată și necăptușită. E pentru zilele blânde din sezonul de tranziție.</p>'
  '<p>Croiala e simplă, dreaptă, iar manșetele se încheie, deci se strâng pe încheietura unui copil mic. Elastanul îi dă puțină elasticitate la mișcare.</p>'
  '<p>Ca o geacă de blugi clasică, are:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare la piept', 'două, cu nasturi.'), ('Buzunare laterale', 'două.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 88-96 până la 122-125 sunt pentru copii de pe la 1 până pe la 7 ani.</p>',
  [('model', 'Guess Geacă de blugi pentru copii N6RL02 D4MS0'), ('denim', 'Model neizolat confecționat din denim'), ('material', '99% Bumbac, 1% Elastan'),
   ('necăptușit', 'Captuseala: necaptusit'), ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Mansete incheiate'),
   ('nasturi', 'Incheiere cu nasturi'), ('buzunare piept', 'Două buzunare la piept cu nasturi'), ('buzunare laterale', 'Două buzunare laterale'), ('fără glugă', 'Gluga: fara gluga')],
  {'Model': 'Guess N6RL02 D4MS0', 'Material': '99% bumbac, 1% elastan (denim)', 'Caracteristici': 'neizolată, necăptușită, nasturi, patru buzunare', 'Cod produs': 'N6RL02 D4MS0'})

w(10118,
  f'<p>Pantofii {PRIMIGI} PTR 24112 sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} bleumarin, din piele nubuc, cu interior și branț din piele naturală, în stil casual, pentru purtat zi de zi. Tehnologia Primigi × SIPeP a fost creată împreună cu podologi italieni.</p>'
  '<p>Vârful e lat și moale, de tip barefoot, și lasă degetele să se miște liber, deci pantoful vine bine și pe un picior mai lat. Aricii permit încălțatul fără ajutor, iar călcâiul moale nu strânge.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Partea de sus', 'piele nubuc.'), ('Interior și branț', 'piele naturală.'), ('Talpă', 'din cauciuc, flexibilă.'))
  + '<p>Numerele 20-29 sunt, în general, pentru copii de 1-5 ani.</p>',
  [('model', 'Primigi Pantofi pentru copii din nubuck bleumarin PTR 24112'), ('nubuc', 'Partea superioară din piele nubuc'), ('interior', 'Interior din piele naturală'),
   ('branț', 'Branț din piele naturală'), ('casual', 'Stilul casual'), ('zilnic', 'utilizarea zilnică'), ('SIPeP', 'Tehnologia Primigi × SIPeP'),
   ('podologi', 'creată împreună cu podologi italieni'), ('vârf', 'Vârf lat, moale , de tip barefoot, permite mișcarea liberă a degetelor'),
   ('arici', 'Sistemul practic de închidere cu arici facilitează încălțarea și descălțarea independentă'), ('călcâi', 'Călcâiul moale'), ('talpă', 'Talpă din cauciuc oferă flexibilitate')],
  {'Model': 'Primigi PTR 24112', 'Material': 'piele nubuc, interior și branț din piele naturală, talpă din cauciuc', 'Caracteristici': 'vârf lat barefoot, arici, Primigi × SIPeP', 'Cod produs': 'PTR 24112'})

w(10125,
  f'<p>Botinele {PRIMIGI} PND 23772 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} roz, cu partea de sus sintetică, care rezistă la umezeală și se curăță ușor. Interiorul nu e izolat, deci sunt pentru zilele mai calde din perioada de tranziție.</p>'
  '<p>Construcția peste gleznă ține piciorul și apără de frig, iar fermoarul îi lasă pe copii să le încalțe și să le scoată singuri.</p>'
  '<p>Înăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textilă.'), ('Branțuri', 'detașabile.'), ('Talpă', 'plată, din cauciuc.'), ('Primigi × SIPeP', 'ține cont de anatomia piciorului copilului.'))
  + '<p>Numerele 27-30 sunt pentru copii de pe la 3 până pe la 7 ani.</p>',
  [('model', 'Primigi Botine pentru copii roz PND 23772'), ('sintetic', 'Partea superioară sintetică'), ('umezeală', 'Materialul exterior ajută la protejarea împotriva umezelii'),
   ('curat', 'facilitează menținerea acesteia curată'), ('neizolat', 'Interiorul neizolat face ca încălțămintea să fie potrivită pentru zilele mai calde din perioada de tranziție'),
   ('gleznă', 'Construcția peste gleznă'), ('frig', 'oferă protecție împotriva frigului'), ('fermoar', 'Închiderea cu fermoar facilitează încălțarea și descălțarea rapidă și independentă'),
   ('căptușeală', 'Căptușeala textilă'), ('branțuri', 'branțurile detașabile'), ('talpă', 'Talpa plată din cauciuc'), ('SIPeP', 'Tehnologia Primigi × SIPeP'),
   ('anatomie', 'ținând cont de anatomia acestuia')],
  {'Model': 'Primigi PND 23772', 'Material': 'sintetic, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'neizolate, fermoar, branțuri detașabile', 'Cod produs': 'PND 23772'})

w(10126,
  f'<p>{A("/brand/reima/", "Reima")} Hyppii 5400144B sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} maro, ușori, din material textil și sintetic, cu partea de sus rezistentă la înmuiere, pentru purtat zi de zi. Elementele reflectorizante îl fac pe copil mai vizibil după lăsarea întunericului.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, deci pantoful merge și la un picior mai lat. Velcro-ul și bucla de la spate îl ajută pe cel mic să se încalțe singur.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Interior', 'material sintetic și textil.'), ('Rezistență la apă', 'sporită, fără impermeabilitate completă.'))
  + '<p>Mărimile 22-31 sunt, cu aproximație, pentru 1-7 ani.</p>',
  [('model', 'Reima Pantofi copii Hyppii culoarea maro, 5400144B'), ('ușor', 'Model ușor'), ('material', 'combinația materialului textil cu cel sintetic'),
   ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'), ('zilnic', 'purtarea zilnică'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea după lăsarea întunericului'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('talpă', 'Talpa flexibilă din cauciuc'), ('interior', 'Material sintetic, Material textil'),
   ('apă', 'nu garantează impermeabilitatea completă')],
  {'Model': 'Reima Hyppii', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'velcro, cutie lată, reflectorizante, rezistent la înmuiere', 'Cod produs': '5400144B'})

w(10139,
  f'<p>Geaca {TH} KB0KB10093 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, verde, din țesătură netedă, izolată cu umplutură sintetică, pentru temperaturile mai reci. Gulerul ridicat și gluga detașabilă apără gâtul și capul de frig.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri pe corp, deci lasă loc unui pulover gros dedesubt. Fermoarul și capsele închid geaca strâns, ca vântul să nu treacă prin față.</p>'
  '<p>Geaca mai are:</p>'
  + L(('Buzunare', 'exterioare, cu închidere.'), ('Căptușeală', '100% poliester.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-176 sunt, de regulă, pentru 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă copii culoarea verde, KB0KB10093'), ('neted', 'Model izolat confecționat din țesătură netedă'), ('matlasat', 'Model matlasat izolat cu umplutura sintetica'),
   ('reci', 'temperaturi mai reci'), ('guler, glugă', 'Gulerul ridicat și gluga detașabilă oferă protecție suplimentară împotriva frigului'),
   ('croială', 'Tăiere simplă, fără blocare'), ('închidere', 'Fixare cu fermoar si snap'), ('buzunare', 'Buzunare exterioare incheiata'),
   ('căptușeală', 'Captuseala: 100% Poliester'), ('material', 'Materialul de baza: 100% Poliester')],
  {'Model': 'Tommy Hilfiger KB0KB10093', 'Material': '100% poliester', 'Caracteristici': 'matlasată, izolată, glugă detașabilă, fermoar și capse', 'Cod produs': 'KB0KB10093'})

w(10141,
  f'<p>Puloverul {TH} KB0KB10071 este un {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "pulover pentru băieți")} bej, cu imprimeu, din tricot elastic de grosime medie, cu bumbac Better Cotton și acril. Decolteul e clasic, rotund.</p>'
  '<p>Croiala e lejeră, cu umerii coborâți pe mânecă, deci puloverul stă larg și încape o cămașă dedesubt. Mânecile și tivul au bordură, care strânge la încheieturi și jos.</p>'
  '<p>Pe scurt, despre pulover:</p>'
  + L(('Material', '60% bumbac, 40% acril.'), ('Tricot', 'grosime medie, elastic.'), ('Decolteu', 'rotund.'))
  + '<p>Mărimile 128-176 sunt pentru copii de cam 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Pulover copii culoarea bej, KB0KB10071'), ('imprimeu', 'Model: imprimeu'), ('elastic', 'tricotaje elastice'), ('grosime', 'Tricot de grosime medie'),
   ('BCI', 'Better Cotton Initiative'), ('material', '60% Bumbac, 40% Acril'), ('decolteu', 'Decolteu clasic, rotund'), ('croială', 'Croială lejeră'),
   ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'), ('bordură', 'Mânecile și marginea inferioară sunt finisate cu bătături')],
  {'Model': 'Tommy Hilfiger KB0KB10071', 'Material': '60% bumbac, 40% acril', 'Caracteristici': 'tricot mediu, croială lejeră, decolteu rotund', 'Cod produs': 'KB0KB10071'})
