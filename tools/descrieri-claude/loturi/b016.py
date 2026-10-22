import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9153,
  f'<p>{GEOX} WASHIBA J66LQJ sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași înalți pentru băieți")}, bleumarin, din imitație de piele și material textil, cu tehnologia GEOX Respira™, care elimină umezeala și ține interiorul uscat. Se poartă la ținute casual și streetwear.</p>'
  '<p>Aricii se combină cu o inserție elastică, care adaptează pantoful la forma piciorului, iar profilul înalt ține glezna la joacă.</p>'
  '<p>Pe dinăuntru și pe dedesubt:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'ușor întărit.'), ('Branț', 'detașabil, textil.'), ('Căptușeală', 'textilă.'))
  + '<p>Numerele de pe site, 28-35, sunt pentru copii de cam 4-11 ani.</p>',
  [('model', 'Geox WASHIBA sneakers pentru copii bleumarin J66LQJ.0BC15'), ('material', 'Combinația de imitație de piele și material textil'), ('Respira', 'Tehnologia GEOX Respira'),
   ('casual', 'stilul casual și streetwear'), ('arici', 'Sistem de închidere cu arici'), ('elastic', 'Inserție elastică contribuie la adaptarea încălțămintei la forma piciorului'),
   ('profil', 'Profil înalt al părții superioare'), ('talpă', 'Talpă plată din cauciuc'), ('călcâi', 'Călcâi ușor întărit'), ('branț', 'Branțuri detașabile din material textil'),
   ('căptușeală', 'Interiorul căptușit cu material textil')],
  {'Model': 'Geox WASHIBA J66LQJ', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici cu inserție elastică, GEOX Respira™', 'Cod produs': 'J66LQJ.0BC15'})

w(9154,
  f'<p>{A("/brand/guess/", "GUESS")} L6YL09 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")} cu monogramă Guess, bej pe site și neagră la magazin, cu umplutură sintetică și căptușeală completă. E pentru zilele mai reci ale sezonului de tranziție.</p>'
  '<p>Croiala e regulară și lasă loc de straturi dedesubt, iar baza și manșetele se reglează, ca geaca să nu lase aerul rece să intre. Lungimea ajunge până la șolduri.</p>'
  '<p>Mai are:</p>'
  + L(('Glugă', 'integrată.'), ('Buzunare', 'laterale.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester, țesătură rezistentă.'))
  + '<p>Mărimile încep la 122-125 și urcă până la 175, adică pentru copii de pe la 7 până pe la 16 ani.</p>',
  [('cod', 'Geacă petrecută pentru copii neagră L6YL09 W2670'), ('monogramă', 'Model cu monogramă Guess'), ('umplutură', 'Umplutură sintetică'), ('căptușeală', 'Căptușeală completă'),
   ('tranziție', 'sezonul de tranziție'), ('croială', 'Croială regulară'), ('straturi', 'purtarea confortabilă peste alte straturi'), ('reglabil', 'Bază și manșete reglabile'),
   ('lungime', 'Lungime până la șolduri'), ('glugă', 'Glugă integrată'), ('buzunare', 'Buzunare laterale practice'), ('fermoar', 'Închidere cu fermoar'),
   ('material', '100% Poliester'), ('țesătură', 'Confecționată din țesătură rezistentă')],
  {'Model': 'GUESS L6YL09', 'Material': '100% poliester, umplutură sintetică', 'Caracteristici': 'matlasată, monogramă, glugă, bază și manșete reglabile', 'Cod produs': 'L6YL09.W2670'},
  notes=['Titlul de pe site spune bej; magazinul o descrie ca neagră.'])

w(9159,
  f'<p>{A("/brand/columbia/", "Columbia")} Pike Lake este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, violet, matlasată și izolată cu umplutură din poliester reciclat, cu glugă și tehnologia Omni-Heat, care reglează temperatura corpului la efort.</p>'
  '<p>Are sistemul OUTGROWN de la Columbia, care permite prelungirea mânecilor pe măsură ce copilul crește, deci geaca ține mai multe sezoane. Marginile mânecilor se reglează cu arici.</p>'
  '<p>Buzunarele și închiderea:</p>'
  + L(('Buzunare', 'două, laterale, cu fermoar.'), ('Buzunar interior', 'pentru lucruri mici.'), ('Închidere', 'fermoar.'), ('Căptușeală', 'poliester; mânecile, poliamidă.'))
  + '<p>Pe site sunt mărimi de la 104 până la XS, potrivite cam pentru 4-14 ani.</p>',
  [('model', 'Geacă copii Pike Lake culoarea violet, 2133871'), ('matlasat', 'material matlasat'), ('izolat', 'Model izolat'), ('umplutură', 'Umplutura: 100% Poliester reciclat'),
   ('glugă', 'Gluga: cu gluga'), ('Omni-Heat', 'Tehnologia Omni-Heat'), ('OUTGROWN', 'Sistemul OUTGROWN Grow de la Columbia'), ('sezoane', 'astfel incat sa reziste mai multe sezoane'),
   ('arici', 'Marginile inferioare ale mânecilor sunt reglabile cu Velcro'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('buzunar interior', 'Un buzunar interior suplimentar'), ('fermoar', 'Incheiere cu fermoar'), ('căptușeală', 'Căptușeala principală: 100% Poliester'),
   ('mâneci', 'Captuseala minecilor: 100% Poliamida')],
  {'Model': 'Columbia Pike Lake', 'Material': 'poliester reciclat, umplutură poliester reciclat', 'Caracteristici': 'Omni-Heat, OUTGROWN, glugă, manșete cu arici', 'Cod produs': '2133871'})

w(9165,
  f'<p>{GEOX} INEK J659CC sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași cu branț luminos pentru băieți")}, bleumarin, din material textil și piele ecologică, ușori și făcuți pentru purtat zilnic. Au sistemul Geox Respira în talpă, cu perforații.</p>'
  '<p>Șireturile elastice și închiderea cu cârlig se strâng fără nod, iar bucla de la spate ajută la încălțat, deci copilul se descurcă singur dimineața.</p>'
  '<p>Detaliul care se vede seara și restul construcției:</p>'
  + L(('Branț', 'luminos.'), ('Interior', 'textil.'), ('Profil', 'scurt.'), ('Material', 'textil și piele ecologică.'))
  + '<p>Numerele 24-35 se potrivesc în general copiilor de 2-11 ani.</p>',
  [('model', 'Sneakers pentru copii INEK culoarea bleumarin, J659CC.01454'), ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'ideal pentru purtarea zilnică'),
   RESPIRA, ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('buclă', 'Bucla de la spate'), ('branț luminos', 'Pantofi cu branturi luminoase'),
   ('interior', 'Interiorul textil'), ('profil', 'Înălțime: mic de statură')],
  {'Model': 'Geox INEK J659CC', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'branț luminos, șireturi elastice, Geox Respira', 'Cod produs': 'J659CC.01454'})

w(9168,
  f'<p>{GEOX} PERTH J367RE sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} gri, din material textil și piele ecologică, ușori și făcuți pentru purtat zilnic, cu sistemul Geox Respira în talpă.</p>'
  '<p>Se închid cu șireturi elastice și cârlig, deci se pun și se scot fără legat; profilul e scurt, sub gleznă, iar interiorul textil e ușor de ținut curat.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Interior', 'textil.'), ('Material', 'textil și piele ecologică.'), ('Profil', 'scurt.'))
  + '<p>Numerele 28-41 se potrivesc copiilor de la aproximativ 4 ani până la adolescenți.</p>',
  [('model', 'Sneakers pentru copii PERTH culoarea gri, J367RE.054FU'), ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'ideal pentru purtarea zilnică'),
   RESPIRA, ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('profil', 'Înălțime: mic de statură'), ('interior', 'Interiorul textil'), ('talpă', 'Talpa exterioară din cauciuc')],
  {'Model': 'Geox PERTH J367RE', 'Material': 'textil și piele ecologică, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice cu cârlig', 'Cod produs': 'J367RE.054FU'})

w(9169,
  f'<p>{GEOX} FLEXYPER sunt cizme înalte de iarnă maro, listate pe site la {A("/categorie/baieti-incaltaminte-pantofi/", "încălțămintea de iarnă pentru băieți")}, din piele naturală și material textil, cu membrana microporoasă GEOX Respira™, care elimină umezeala și ține apa afară.</p>'
  '<p>Închiderea e dublă, cu șireturi și scai, deci cizma se strânge exact pe picior; vârful rotund lasă loc degetelor, iar gulerul ușor întărit ține glezna.</p>'
  '<p>Pentru iarnă, cizmele mai au:</p>'
  + L(('Talpă', 'din cauciuc, rezistentă la abraziune.'), ('Călcâi', 'întărit.'), ('Interior', 'textil.'))
  + '<p>Numerele 36-41 sunt pentru copii mari, de obicei de la 12 ani în sus.</p>',
  [('model', 'Geox Încălțăminte pentru copii FLEXYPER maro J369BA.032ME'), ('iarnă', 'Cizmele de iarnă pentru băieți Geox FLEXYPER sunt cizme înalte'),
   ('material', 'Partea superioară din combinație de piele naturală și material textil'), ('Respira', 'Tehnologia GEOX Respira™ cu o membrană microporoasă'),
   ('apă', 'protejând interiorul cizmei de pătrunderea apei'), ('închidere', 'Închiderea dublă cu șireturi și scai'), ('vârf', 'Vârful rotund oferă spațiu pentru degete'),
   ('guler', 'Gulerul superior ușor întărit'), ('talpă', 'Talpa din cauciuc este durabilă și rezistentă la abraziune'), ('călcâi', 'Călcâiul întărit')],
  {'Model': 'Geox FLEXYPER', 'Material': 'piele naturală și textil, talpă din cauciuc', 'Caracteristici': 'cizme de iarnă, membrană GEOX Respira™, șireturi și scai', 'Cod produs': 'J369BA.032ME'},
  notes=['Pe site e la Pantofi; produsul e cizmă de iarnă.'])

w(9171,
  f'<p>{A("/brand/colmar/", "Colmar")} GLOWER este o {A("/categorie/geci-jachete/", "geacă de puf pentru fete")}, cu umplutură naturală din 90% puf de rață și 10% pene, izolată și căptușită, pentru frig și iarnă. Pe site apare ca neagră, iar magazinul o dă albastră.</p>'
  '<p>Croiala e simplă, cu loc pentru un pulover dedesubt, iar fermoarul urcă până la gulerul ridicat. Gluga apără capul pe ger.</p>'
  '<p>Detaliile:</p>'
  + L(('Buzunare', 'două, laterale, cu fermoar.'), ('Glugă', 'are.'), ('Material', '100% poliamidă, căptușeală 100% poliamidă.'), ('Umplutură', '90% puf de rață, 10% pene de rață.'))
  + '<p>Mărimile de pe site, 106-172, sunt pentru copii de aproximativ 4-15 ani.</p>',
  [('model', 'Colmar Geacă copii GLOWER 3475.8XV'), ('puf', 'Umplutura din puf si pene'), ('umplutură', '90% Duck Down, 10% Pene de rață'), ('izolat', 'Model izolat cu captuseala'),
   ('frig', 'nivel ridicat de izolare împotriva frigului'), ('croială', 'Tăiere simplă'), ('fermoar, guler', 'Are inchidere cu fermoar si guler ridicat'),
   ('glugă', 'Model cu gluga'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material', 'Material de bază: 100% Poliamida'), ('culoare magazin', 'albastru')],
  {'Model': 'Colmar GLOWER', 'Material': '100% poliamidă, umplutură puf de rață și pene', 'Caracteristici': 'geacă de puf, glugă, guler ridicat, buzunare cu fermoar', 'Cod produs': '3475.8XV'},
  notes=['Titlul de pe site spune negru; magazinul dă albastru.'])

w(9178,
  f'<p>{GEOX} ASSISTER sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași cu lumini pentru băieți")}, negri, din material textil și sintetic, cu talpă ușoară din spumă și tehnologia Geox Respira™, cu membrană în talpă. Luminile încorporate se văd după lăsarea întunericului.</p>'
  '<p>Închiderea e dublă, cu șireturi și scai, deci se strâng exact pe picior; profilul scurt nu limitează glezna la joacă.</p>'
  '<p>Ce mai au:</p>'
  + L(('Branț', 'detașabil, textil.'), ('Călcâi', 'ușor întărit.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Numerele 24-35 sunt pentru copii de cam 2-11 ani.</p>',
  [('model', 'Geox ASSISTER sneakers pentru copii negri J66DZB.02A9J'), ('material', 'Partea superioară, din material textil și sintetic'), ('talpă', 'Talpa din spumă oferă lejeritate'),
   ('Respira', 'Tehnologia Geox Respira'), ('membrană', 'Membrana microporoasă din talpă'), ('lumini', 'Luminile încorporate adaugă încălțămintei atractivitate și vizibilitate după lăsarea întunericului'),
   ('închidere', 'Închiderea dublă cu șireturi și scai'), ('profil', 'Profilul scurt'), ('branț', 'Branțurile detașabile din material textil'), ('călcâi', 'Călcâiul ușor întărit'),
   ('interior', 'Interiorul căptușit cu material textil')],
  {'Model': 'Geox ASSISTER', 'Material': 'textil și sintetic, talpă din spumă', 'Caracteristici': 'lumini, șireturi și scai, Geox Respira™', 'Cod produs': 'J66DZB.02A9J'},
  notes=['Titlul de pe site nu are culoare; magazinul arată negru.'])

w(9180,
  f'<p>{A("/brand/lego/", "LEGO")} LWJIPE 704 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, bleumarin, izolată și căptușită, cu tratamentul BIONIC-FINISH® ECO, care respinge apa. Gulerul ridicat și gluga detașabilă apără de frig.</p>'
  '<p>Mânecile raglan lasă brațele libere la joacă, iar mânecile se termină cu elastic, care le strânge pe încheieturi; croiala e simplă.</p>'
  '<p>Pentru drumurile de seară și pentru mărunțișuri:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede după lăsarea întunericului.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester.'))
  + '<p>Plaja mare de mărimi, 80-164, acoperă copii de cam 1-14 ani.</p>',
  [('model', 'Lego Geacă copii LWJIPE 704 22898'), ('izolat', 'Izolare: izolat'), ('căptușeală', 'Captuseala: cu captuseala'), ('BIONIC', 'BIONIC-FINISH® ECO'),
   ('glugă, guler', 'Gulerul ridicat și gluga detașabilă'), ('raglan', 'Maneca raglan'), ('elastic', 'Mâneci finisate cu o coadă elastică'), ('croială', 'Tăiere simplă'),
   ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'LEGO LWJIPE 704', 'Material': '100% poliester', 'Caracteristici': 'izolată, BIONIC-FINISH® ECO, glugă detașabilă, mâneci raglan, reflectorizante', 'Cod produs': '22898'})

w(9184,
  f'<p>{GEOX} BRIEZEE sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași impermeabili pentru băieți")}, bleumarin, din material sintetic, piele întoarsă și textil, cu membrana impermeabilă Geox Respira, care ține umezeala sub control. Sunt buni și pentru zilele umede.</p>'
  '<p>Șireturile elastice și închiderea cu cârlig se strâng fără nod, iar branțul detașabil din piele, făcut fără crom, se scoate pentru aerisit și pentru verificat lungimea piciorului.</p>'
  '<p>Construcția:</p>'
  + L(('Vârf', 'rotund, întărit.'), ('Partea de sus', 'rigidizată.'), ('Talpă', 'din cauciuc.'), ('Căptușeală', 'textilă, cu interior din piele naturală.'))
  + '<p>Numerele 24-35 corespund, aproximativ, vârstei de 2-11 ani.</p>',
  [('model', 'Sneakers pentru copii BRIEZEE culoarea albastru marin, J36GMA.01454'), ('material', 'mix de material sintetic, piele întoarsă și material textil'),
   ('membrană', 'Membrana unica si impermeabila a tehnologiei Geox Respira'), ('închidere', 'Șireturile elastice și închiderea cu cârlig'),
   ('branț', 'Branțul detașabil din piele a fost realizat fără utilizarea cromului'), ('vârf', 'Cutie rotunda, intarita'), ('rigidizat', 'Partea superioară rigidizată'),
   ('talpă', 'Talpă din cauciuc'), ('căptușeală', 'Model cu captuseala textila'), ('interior', 'Interiorul: Material textil, Piele naturala')],
  {'Model': 'Geox BRIEZEE', 'Material': 'sintetic, piele întoarsă și textil, talpă din cauciuc', 'Caracteristici': 'membrană Geox Respira, branț din piele fără crom, șireturi elastice', 'Cod produs': 'J36GMA.01454'})
print('lot 16 scris')
