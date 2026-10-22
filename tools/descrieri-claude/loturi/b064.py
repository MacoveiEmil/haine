import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
COL = A('/brand/columbia/', 'Columbia')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
PODO = ('Podology', 'Tehnologia Biomecanics Podology Partnership')

w(12423,
  f'<p>Adidașii {GEOX} J36FWB roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} din plasă ușoară, gândiți pentru purtarea de zi cu zi, cu profil jos. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos, fără legat la fiecare plecare din casă.</p>'
  '<p>Vârful rotund, ușor rigid, lasă loc degetelor, iar călcâiul rigid ține piciorul în pantof la alergat. Bucla de la spate ajută la încălțat.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Interior', 'textil, cu branț detașabil.'), ('Talpă', 'din spumă, moale la pas.'))
  + '<p>Mărimile încep la 28 și urcă până la 35, pentru fete de cam 4-11 ani; la 35 branțul are 22 cm.</p>',
  [('model', 'Geox Sneakers pentru copii culoarea roz, J36FWB.01454'), ('plasă', 'confecționat din plasă ușoară'), ('zi cu zi', 'purtarea de zi cu zi'),
   ('profil', 'Înălțime: mic de statură'), ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('călcâi', 'Călcâiul puternic rigid stabilizează călcâiul'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   RESPIRA, ('interior', 'Interiorul textil este confortabil pentru picior'), ('branț', 'Brant textil, detasabil'), ('talpă', 'Talpa din spumă oferă o senzație mai moale'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 22 cm')],
  {'Model': 'Geox J36FWB', 'Material': 'plasă textilă și material sintetic, interior textil', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira, branț detașabil', 'Cod produs': 'J36FWB.01454'},
  notes=['Titlul și pagina spun roz, dar atributul de culoare al magazinului e alb; am păstrat roz.'])

w(12426,
  f'<p>{BIO} 261108 sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, plați, cu partea de sus din material textil cu finisaj strălucitor și un motiv animal, în stil casual. Talpa flexibilă din cauciuc are 1 cm grosime, așa că piciorul stă așezat natural la joacă și la plimbare.</p>'
  '<p>Închiderea cu arici și curea reglabilă permite o ajustare precisă, iar călcâiul moale și gulerul nu irită pielea.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Vârf', 'rotund, cauciucat, apără degetele.'), ('Interior', 'din imitație de piele, moale.'), ('Branț', 'textil, detașabil, ușor de curățat.'), ('Podology Partnership', 'tehnologia Biomecanics pentru piciorul în creștere.'))
  + '<p>Numerele 19-25 se potrivesc, orientativ, copiilor de 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii roz 261108'), ('plat', 'Sneakerși flat pentru copii'), ('strălucitor', 'Partea superioară din material textil cu finisaj strălucitor'),
   ('animal', 'Stilul casual cu motiv animal'), ('talpă', 'Talpa flexibilă din cauciuc'), ('grosime', 'Talpa cu grosimea de 1 cm permite o poziționare naturală a piciorului'),
   ('arici', 'Închiderea cu arici și curea reglabilă permite o încălțare ușoară și o ajustare precisă'), ('călcâi', 'Călcâiul moale și gulerul superior minimizează riscul de iritații'),
   ('vârf', 'Vârful rotund, cauciucat protejează degetele'), ('interior', 'Interiorul din imitație de piele favorizează moliciunea'),
   ('branț', 'Branțul detașabil din material textil sprijină igiena și permite o curățare ușoară'), PODO],
  {'Model': 'Biomecanics 261108', 'Material': 'textil strălucitor, interior din imitație de piele, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, branț detașabil, vârf cauciucat', 'Cod produs': '261108'})

w(12429,
  f'<p>{BIO} 261151 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} bleumarin, uni, cu partea de sus din piele naturală și material sintetic, buni pentru joaca în parc și ieșirile în familie. Au fost creați cu podiatri și specialiști în biomecanica mișcării, după etapele de dezvoltare ale piciorului.</p>'
  '<p>Aricii îl lasă pe copil să se încalțe singur, iar călcâiul întărit ține piciorul în poziție corectă la mers.</p>'
  '<p>Materialele, pe scurt:</p>'
  + L(('Interior', 'căptușeală textilă, delicată.'), ('Talpă', 'din cauciuc, plată.'), ('Închidere', 'arici.'))
  + '<p>Există numerele 24-26, pentru copii de aproximativ 2-4 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii bleumarin 261151'), ('uni', 'Culoare bleumarin și model uni'), ('material', 'Partea superioară din piele naturală și material sintetic'),
   ('ocazii', 'de la joaca în parc la ieșirile în familie'), ('podiatri', 'Produse create în colaborare cu podiatri și specialiști în biomecanica mișcării'),
   ('arici', 'Facilitează încălțarea și descălțarea autonomă de către copii'), ('călcâi', 'Stabilizează călcâiul, favorizând menținerea piciorului într-o poziție corectă'),
   ('interior', 'Căptușeala delicată favorizează confortul'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Biomecanics 261151', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, călcâi întărit', 'Cod produs': '261151'})

w(12432,
  f'<p>{BIO} 262165 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, cu partea de sus până la gleznă, din material textil și sintetic, pentru primăvară, vară și toamnă. Branțul detașabil are imprimeu pentru verificarea mărimii, deci vedeți repede dacă piciorul a crescut.</p>'
  '<p>Gulerul moale înconjoară călcâiul, iar scaiul îl lasă pe copil să se încalțe și să se descalțe singur.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Interior', 'căptușit cu material textil.'), ('Talpă', 'din cauciuc, flexibilă, cu profil plat.'), ('Închidere', 'scai.'))
  + '<p>Numerele 19-23 merg, cu aproximație, la copii de 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii albi 262165'), ('gleznă', 'Construcția părții superioare până la gleznă'), ('material', 'Partea superioară din material textil și sintetic'),
   ('sezon', 'Ideal pentru primăvară, vară și toamnă'), ('branț', 'Branțul detașabil cu imprimeu pentru verificarea mărimii'), ('guler', 'Gulerul moale înconjoară delicat călcâiul'),
   ('scai', 'Închiderea practică cu scai permite încălțarea și descălțarea rapidă și independentă'), ('interior', 'Interiorul căptușit cu material textil'),
   ('talpă', 'Talpa flexibilă din cauciuc cu profil plat')],
  {'Model': 'Biomecanics 262165', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'scai, branț cu verificare de mărime, înălțime până la gleznă', 'Cod produs': '262165'})

w(12436,
  f'<p>Geaca {COL} Hikebound neagră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} izolată, cu umplutură sintetică, pentru zilele reci. Membrana Omni-Tech, cu cusături sudate, oprește ploaia, iar Omni-Heat ajută la păstrarea căldurii corpului.</p>'
  '<p>Are glugă și căptușeală, se închide cu fermoar și velcro, iar mânecile se termină cu manșetă elastică.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Material', '100% poliester, căptușeală din poliester și poliamidă.'), ('Croială', 'simplă, dreaptă.'))
  + '<p>Mărimile 128-164 vin cam la 8-14 ani; la 164 cm geaca are 74 cm lungime.</p>',
  [('model', 'Columbia Geacă copii Hikebound culoarea negru, 2089961'), ('izolat', 'Model izolat confecționat din material neted'), ('umplutură', 'izolație sintetică'),
   ('frig', 'temperaturi mai scăzute'), ('Omni-Tech', 'Tehnologia Omni-tech® ofera protectie completa impotriva schimbarilor bruste ale vremii'), ('sudate', 'cusaturilor sudate'),
   ('Omni-Heat', 'Tehnologia Omni-Heat regleaza temperatura corpului'), ('glugă', 'Gluga: cu gluga'), ('căptușeală', 'Captuseala: cu captuseala'),
   ('închidere', 'Fixarea cu fermoar si velcro'), ('mâneci', 'Mâneci finisate cu o coadă elastică confortabilă'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('material', '100% Poliester'), ('căptușeala 2', '100% Poliamida'), ('croială', 'Tăiere simplă, fără blocare'), ('lungime', 'Lungimea: 74 cm')],
  {'Model': 'Columbia Hikebound', 'Material': '100% poliester, umplutură din poliester', 'Caracteristici': 'Omni-Tech, Omni-Heat, glugă, fermoar și velcro', 'Cod produs': '2089961'})

w(12442,
  f'<p>Bocancii {TH} roșii sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} din imitație de piele lăcuită, neizolați, cu partea de sus neporoasă, care se curăță cu o cârpă umedă. Au șiret clasic, fermoar lateral și Velcro, deci se reglează o dată și apoi se încalță repede.</p>'
  '<p>Cutia rotundă, întărită, apără degetele, iar contrafortul rigid ține călcâiul pe loc.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'textil și piele naturală.'), ('Branț', 'din piele, previne frecarea.'), ('Talpă', 'din cauciuc, rezistentă.'))
  + '<p>Numerele 35-39 se poartă de pe la 10 ani în sus; la 35 branțul are 22,5 cm.</p>',
  [('model', 'Tommy Hilfiger Bocanci copii culoarea rosu, T4A5-34025'), ('lăcuit', 'imitatie de piele lacuita'), ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'),
   ('neizolat', 'Izolare: neizolat'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('șiret', 'Șiretul clasic permite ajustarea individuală'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid stabilizează călcâiul'), ('interior', 'Material textil, Piele naturala'),
   ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'), ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('lungime', 'Lungimea brantului pentru marimea este de: 22,5 cm')],
  {'Model': 'Tommy Hilfiger T4A5-34025', 'Material': 'imitație de piele lăcuită, interior textil și piele, talpă din cauciuc', 'Caracteristici': 'șiret, fermoar lateral, Velcro, neizolați', 'Cod produs': 'T4A5-34025'})

w(12444,
  f'<p>Bluza {A("/brand/reima/", "Reima")} Meriol albă este o {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "bluză unisex")} din țesătură subțire, ușor elastică, din materialul Seawool Blend, făcut din pulbere de cochilii și poliester reciclat. E moale ca lâna și antistatică, bună ca strat de mijloc pe vreme rece.</p>'
  '<p>Are fermoar scurt la gât, guler ridicat contra frigului și mâneci raglan, care lasă brațele să se miște liber.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Interior', 'moale, căptușit.'), ('Model', 'uni, fără glugă.'), ('Croială', 'simplă, dreaptă.'))
  + '<p>Gama de mărimi merge de la 104 la 164, deci acoperă cam 4-14 ani.</p>',
  [('model', 'Reima Meriol alb 5200441A'), ('țesătură', 'tesatura subtire, usor elastica'), ('Seawool', 'Seawool Blend, realizat dintr-o combinatie de cochilii de pulbere si poliester reciclat'),
   ('lână', 'similar cu lana si are, de asemenea, proprietati antistatice'), ('fermoar', 'Închiderea cu fermoar scurt'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('raglan', 'Maneca raglan'), ('interior', 'Interiorul moale căptușit'), ('glugă', 'Gluga: fara gluga'), ('uni', 'Model: uni'), ('croială', 'Tăiere simplă, fără blocare')],
  {'Model': 'Reima Meriol', 'Material': 'Seawool Blend (poliester reciclat și elastan)', 'Caracteristici': 'fermoar scurt, guler ridicat, mâneci raglan', 'Cod produs': '5200441A'},
  notes=['Compoziția de pe pagină e incompletă (30% poliester reciclat, 10% elastan); nu am dat procente.'])

w(12447,
  f'<p>Geaca {COL} Hikebound turcoaz este o {A("/categorie/geci-jachete/", "geacă pentru fete")} subțire, de tranziție, din material ușor, cu membrana Omni-Tech și cusături sudate, care țin ploaia afară la schimbările bruște de vreme. Gulerul ridicat și gluga fixă apără de vânt.</p>'
  '<p>Căptușeala e din plasă, iar geaca se închide cu fermoar și velcro.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Mâneci', 'cu manșetă elastică.'), ('Buzunare', 'două laterale, cu fermoar.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-164 se potrivesc fetelor de aproximativ 4-14 ani; la 104 cm geaca are 41 cm lungime.</p>',
  [('model', 'Columbia Geacă copii Hikebound culoarea turcoaz, 2115931'), ('subțire', 'Model subțire'), ('ușor', 'material ușor'), ('tranziție', 'Izolare: tranzitional'),
   ('Omni-Tech', 'Tehnologia Omni-tech® ofera protectie completa impotriva schimbarilor bruste ale vremii'), ('sudate', 'cusaturilor sudate'),
   ('glugă', 'Gulerul ridicat și gluga fixă'), ('plasă', 'Căptușeala este realizată dintr-un material plasă'), ('închidere', 'Fixarea cu fermoar si velcro'),
   ('mâneci', 'Mâneci finisate cu o coadă elastică confortabilă'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material', '100% Poliester'), ('lungime', 'Lungimea: 41 cm')],
  {'Model': 'Columbia Hikebound', 'Material': '100% poliester, căptușeală din plasă', 'Caracteristici': 'Omni-Tech, glugă fixă, fermoar și velcro', 'Cod produs': '2115931'})

w(12450,
  f'<p>Geaca {A("/brand/guess/", "GUESS")} L6RL06 bej este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")} ușoară, de tranziție, din material neted, rezistentă la vânt și la apă. Ține la ploaie scurtă, dar magazinul precizează că nu e complet impermeabilă.</p>'
  '<p>Mânecile și tivul au margine elastică, iar fermoarul o face ușor de pus și de scos. Nu are glugă.</p>'
  '<p>Detaliile de închidere și material:</p>'
  + L(('Buzunare', 'exterioare, cu închidere.'), ('Căptușeală', 'din poliester.'), ('Material', '100% poliester.'))
  + '<p>Mărimile pornesc de la 122-125 și ajung la 175, pentru băieți de cam 7-16 ani.</p>',
  [('model', 'Guess Geacă copii culoarea bej, L6RL06 WH762'), ('ușor', 'Model ușor izolat confecționat din material neted'), ('tranziție', 'Izolare: tranzitional'),
   ('vânt', 'Model rezistent la vânt și impermeabil'), ('apă', 'nu garantează impermeabilitatea completă'), ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică confortabilă'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('glugă', 'Gluga: fara gluga'), ('buzunare', 'Buzunare exterioare incheiata'), ('material', '100% Poliester')],
  {'Model': 'GUESS L6RL06', 'Material': '100% poliester, căptușeală din poliester', 'Caracteristici': 'rezistentă la vânt și apă, fermoar, manșete elastice', 'Cod produs': 'L6RL06 WH762'})

w(12456,
  f'<p>Cămașa {TH} KB0KB10192 albă este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "cămașă pentru băieți")} uni, cu mânecă lungă, din țesătură netedă de bumbac organic cu puțin elastan, pentru ținute casual. Gulerul e moale, în stil clasic Kent.</p>'
  '<p>Se închide cu nasturi pe toată lungimea, iar manșetele au și ele nasturi, deci mânecile se pot strânge la încheietură sau sufleca. Conținutul ridicat de bumbac o face confortabilă.</p>'
  '<p>Restul detaliilor:</p>'
  + L(('Material', '98% bumbac organic, 2% elastan.'), ('Croială', 'simplă, dreaptă.'), ('Model', 'uni.'))
  + '<p>Mărimile 128-176 sunt gândite pentru băieți de 8-16 ani, orientativ.</p>',
  [('model', 'Tommy Hilfiger Cămașă copii culoarea alb, KB0KB10192'), ('țesătură', 'țesătură netedă'), ('organic', 'Acest produs este realizat parțial din bumbac organic'),
   ('uni', 'Model: uni'), ('mânecă', 'Maneca: lung'), ('casual', 'Ocazie: casual'), ('guler', 'Guler soft in stil clasic Kent'),
   ('închidere', 'Închiderea convenabilă cu buton'), ('manșete', 'Manșete cu nasturi'), ('material', '98% Bumbac organic, 2% Elastan'), ('croială', 'Tăiere simplă, fără blocare')],
  {'Model': 'Tommy Hilfiger KB0KB10192', 'Material': '98% bumbac organic, 2% elastan', 'Caracteristici': 'guler Kent, manșete cu nasturi, mânecă lungă', 'Cod produs': 'KB0KB10192'})
