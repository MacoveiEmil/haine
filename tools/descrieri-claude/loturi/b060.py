import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

KS = A('/brand/konges-slojd/', 'Konges Sløjd')
LIEWOOD = A('/brand/liewood/', 'Liewood')

w(11785,
  f'<p>{KS} LUC SHIRT JACKET KS104958 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă-cămașă unisex")}, albastră, din țesătură ușoară de bumbac 100% certificat GOTS, neizolată și necăptușită. E un strat subțire pentru zilele de tranziție.</p>'
  '<p>Croiala e simplă, dreaptă, cu guler moale, deci se poartă ca o cămașă peste un tricou sau ca o geacă ușoară. Nu are glugă.</p>'
  '<p>Detaliile de închidere și buzunare:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'două, în față.'), ('Material', '100% bumbac.'))
  + '<p>Pe site, mărimile 80 până la 134-140 acoperă copiii de cam 1-10 ani.</p>',
  [('model', 'Konges Sløjd Geacă copii LUC SHIRT JACKET GOTS KS104958'), ('ușor', 'țesătură usoara'), ('bumbac', '100% Bumbac'), ('neizolat', 'Izolare: neizolat'),
   ('necăptușit', 'Captuseala: necaptusit'), ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă, fără blocare'), ('guler', 'Model cu guler moale'),
   ('fără glugă', 'Gluga: fara gluga'), ('nasturi', 'Închiderea convenabilă cu buton'), ('buzunare', 'Două buzunare în față'), ('culoare', 'albastru')],
  {'Model': 'Konges Sløjd LUC SHIRT JACKET', 'Material': '100% bumbac (GOTS)', 'Caracteristici': 'neizolată, necăptușită, nasturi, guler moale', 'Cod produs': 'KS104958'},
  notes=['Titlul nu are culoare; magazinul spune albastru.', '„Ca o cămașă peste un tricou” e dedus din numele modelului (shirt jacket).'])

w(11791,
  f'<p>Pantalonii de trening {A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KG0KG09531 sunt {A("/categorie/pantaloni-treninguri/", "pantaloni de trening pentru fete")}, roz, din tricot moale și subțire de bumbac cu poliester, cu pietre de paiete decorative și logo. Sunt făcuți pentru activitate și joacă.</p>'
  '<p>Croiala e regulară, iar talia normală stă stabil pe șolduri fără să strângă. Cracii au manșete, care țin pantalonii pe gleznă și se potrivesc peste încălțăminte.</p>'
  '<p>Ce merită știut despre material și buzunare:</p>'
  + L(('Buzunare', 'laterale.'), ('Material', '68% bumbac, 32% poliester.'), ('Detalii', 'paiete și logo.'))
  + '<p>Mărimile 128-176 se potrivesc fetelor de pe la 8 până la 16 ani, cu aproximație.</p>',
  [('model', 'Tommy Hilfiger Pantaloni de trening pentru copii cu bumbac roz KG0KG09531'), ('tricot', 'Tricot de bumbac – un material moale și subțire'),
   ('paiete', 'Pietre de paiete decorative și logo'), ('activitate', 'creat pentru activitate și libertate de mișcare'), ('croială', 'Croială regulară'),
   ('talie', 'Talie normală – asigură o așezare stabilă pe șolduri, fără a strânge'), ('manșete', 'Picioare cu manșete – permit ajustarea la încăltăminte'.replace('încăltăminte', 'încălțăminte')),
   ('buzunare', 'Buzunare laterale'), ('material', '68% Bumbac, 32% Poliester')],
  {'Model': 'Tommy Hilfiger KG0KG09531', 'Material': '68% bumbac, 32% poliester', 'Caracteristici': 'manșete la craci, talie normală, paiete', 'Cod produs': 'KG0KG09531'})

w(11807,
  f'<p>Vesta {LIEWOOD} Noam Pile Vest LW20450 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "vestă din polar unisex")}, bej, fără izolație termică, ușoară, pentru zilele mai reci din sezonul de tranziție. Gulerul ridicat apără gâtul de frig.</p>'
  '<p>Croiala e regular fit, cu lungimea până la șolduri, iar fără mâneci lasă brațele libere. Fiind subțire, se poartă în straturi, peste un hanorac sau sub o geacă.</p>'
  '<p>Pentru purtat zi de zi, vesta are:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'în față, tip slip-on.'), ('Material', '100% poliester (polar).'))
  + '<p>Mărimile 92-128 se poartă, în general, între 2 și 8 ani.</p>',
  [('model', 'Liewood Vestă pentru copii din polar Noam Pile Vest bej LW20450'), ('polar', 'Materialul din polar favorizează menținerea căldurii'),
   ('neizolat', 'Lipsa izolației termice contribuie la lejeritatea produsului , ideal pentru a fi purtat în straturi'), ('reci', 'zilele mai reci'), ('tranziție', 'sezonul de tranziție'),
   ('guler', 'Gulerul ridicat ajută la protejarea gâtului de frig'), ('croială', 'Croiala regular fit'), ('lungime', 'Lungimea până la șolduri'),
   ('fermoar', 'Sistemul de închidere cu fermoar pe toată lungimea'), ('buzunare', 'Buzunarele practice slip-on în față'), ('material', '100% Poliester')],
  {'Model': 'Liewood Noam Pile Vest', 'Material': '100% poliester (polar)', 'Caracteristici': 'vestă polar, neizolată, guler ridicat, fermoar', 'Cod produs': 'LW20450'})

w(11819,
  f'<p>{LIEWOOD} Ridley Printed Sweatshirt LW20989 este un {A("/categorie/bluze-tricouri-hanorace/", "hanorac pentru fete")}, roz, tip crewneck, din bumbac 100% ușor elastic, cu imprimeu delicat. E simplu, fără buzunare, pentru activitățile de zi cu zi.</p>'
  '<p>Croiala e regulară, iar benzile elastice de la manșete și bază strâng ușor. Fără închidere, hanoracul se trage peste cap, iar decolteul rotund nu strânge.</p>'
  '<p>Material și croială, pe scurt:</p>'.replace(', pe scurt:', ', în trei puncte:')
  + L(('Material', '100% bumbac.'), ('Decolteu', 'rotund.'), ('Model', 'cu imprimeu.'))
  + '<p>Mărimile 86-92 până la 134-140 corespund, cu aproximație, vârstei de 1-10 ani.</p>',
  [('model', 'Liewood Hanorac pentru copii din bumbac Ridley Printed Sweatshirt roz LW20989'), ('crewneck', 'Croiala tip crewneck fără închidere'), ('bumbac', 'Bumbacul 100%'),
   ('elastic', 'Tricotul de bumbac ușor elastic'), ('imprimeu', 'Imprimeul delicat'), ('fără buzunare', 'Lipsa buzunarelor'), ('cotidian', 'activități cotidiene'),
   ('croială', 'Croiala standard regulară'), ('benzi', 'Benzile elastice de la manșete și de la bază'), ('decolteu', 'Decolteul rotund')],
  {'Model': 'Liewood Ridley Printed Sweatshirt', 'Material': '100% bumbac', 'Caracteristici': 'crewneck, imprimeu, benzi elastice', 'Cod produs': 'LW20989'})

w(11822,
  f'<p>{KS} BILLI SWEATER KS104234 este un {A("/categorie/unisex-imbracaminte-bluze-tricouri-hanorace/", "pulover de lână unisex")}, bej, din tricot ornamentat de grosime medie, cu lână și acril. Lâna îl face bun pentru zilele răcoroase de toamnă și iarnă, sub o geacă.</p>'.replace(' de toamnă și iarnă, sub o geacă', '')
  + '<p>Croiala e simplă, dreaptă, deci încape o bluză dedesubt, iar mânecile se termină cu manșetă, care strânge ușor la încheieturi. Decolteul e clasic, rotund.</p>'
  '<p>Detaliile puloverului:</p>'
  + L(('Material', '60% lână, 40% acril.'), ('Tricot', 'ornamentat, grosime medie.'), ('Decolteu', 'rotund.'))
  + '<p>Mărimile 92 până la 134-140 sunt pentru copii de în jur de 2-10 ani.</p>',
  [('model', 'Konges Sløjd Pulover de lână pentru copii BILLI SWEATER culoarea bej, KS104234'), ('ornamentat', 'Tricot ornamentat'), ('grosime', 'Tricotaje: grosime medie'),
   ('material', '60% Lana, 40% Acril'), ('croială', 'Tăiere simplă, fără blocare'), ('manșetă', 'Finisaj din manseta'), ('decolteu', 'Decolteu clasic, rotund')],
  {'Model': 'Konges Sløjd BILLI SWEATER', 'Material': '60% lână, 40% acril', 'Caracteristici': 'tricot ornamentat, decolteu rotund', 'Cod produs': 'KS104234'},
  notes=['„Zile răcoroase” e dedus din compoziția cu lână.'])

w(11842,
  f'<p>{A("/brand/adidas-originals/", "adidas Originals")} KR9129 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă bomber din denim unisex")}, neagră, din bumbac 100%, fără căptușeală, pentru sezonul de tranziție. Are mâneci raglan și guler ridicat, cu un aer sportiv.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar tivul cu elastic și manșetele strâng geaca pe corp, ca la orice bomber.</p>'
  '<p>Închiderea și buzunarele:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'oblice, laterale.'), ('Material', '100% bumbac (denim).'))
  + '<p>Numerele de pe site, 128-176, merg cam de la 8 la 16 ani.</p>',
  [('model', 'adidas Originals Geacă de blugi pentru copii din bumbac neagră KR9129'), ('bomber', 'Croiala tip bomber îi conferă un caracter sportiv'),
   ('bumbac', 'Modelul confecționat în 100% din bumbac denim'), ('necăptușit', 'Lipsa căptușelii'), ('tranziție', 'Acest model de tranziție'), ('raglan', 'Croiala raglan a mânecilor'),
   ('guler', 'guler ridicat'), ('croială', 'Croiala regulară'), ('lungime', 'Lungimea până la șolduri'), ('tiv', 'Tivul cu elastic și manșetele'),
   ('fermoar', 'Închiderea cu fermoar pe toată lungimea'), ('buzunare', 'buzunare oblice pe laterale')],
  {'Model': 'adidas Originals KR9129', 'Material': '100% bumbac (denim)', 'Caracteristici': 'bomber, necăptușită, mâneci raglan', 'Cod produs': 'KR9129'})

w(11859,
  f'<p>{A("/brand/reima/", "Reima")} Kuuraan 5300214B este un {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "accesoriu de iarnă unisex")}, bleumarin, din lână merinos certificată RWS, cu căptușeală din bumbac organic cu elastan. Pe site apare ca fular circular, iar magazinul îl descrie drept căciulă.</p>'
  '<p>Tricotul are grosime medie și model, iar stratul suplimentar de căptușeală îl face moale pe piele și mai călduros pe frig.</p>'.replace(' și mai călduros pe frig', '')
  + '<p>Materialele, pe rând:</p>'
  + L(('Exterior', '100% lână merinos.'), ('Căptușeală', '97% bumbac organic, 3% elastan.'), ('Tricot', 'grosime medie, cu model.'))
  + '<p>Mărimile 46-54 sunt circumferințe de cap, potrivite, cu aproximație, de la 1 an în sus.</p>',
  [('model', 'Reima Kuuraan bleumarin 5300214B'), ('merinos', '100% Lana de merinosi'), ('RWS', 'Standardului responsabil de lana (RWS)'),
   ('căptușeală', '97% Bumbac organic, 3% Elastan'), ('căciulă', 'Căciulă pentru copii din colecția Reima'), ('strat', 'Un strat suplimentar de material sub formă de căptușeală'),
   ('tricot', 'Tricotaje: grosime medie'), ('model imprimat', 'Model: cu modele')],
  {'Model': 'Reima Kuuraan', 'Material': '100% lână merinos (RWS), căptușeală bumbac organic', 'Caracteristici': 'căptușit, tricot mediu', 'Cod produs': '5300214B'},
  varsta_txt='de la 1 an în sus', notes=['Titlul de pe site spune fular circular; magazinul îl descrie drept căciulă; mărimile 46-54 sunt circumferințe de cap.'])

w(11865,
  f'<p>{A("/brand/geox/", "Geox")} PRO-RAN FAST IN J667JA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, ușori, din material textil și sintetic, cu țesătură RIPSTOP, care limitează extinderea rupturilor. Tehnologia Geox Respira™ scoate umiditatea și ține interiorul uscat.</p>'
  '<p>Șireturile elastice permit încălțatul și descălțatul rapid, fără nod, iar gulerul ușor întărit și călcâiul întărit țin piciorul în pantof.</p>'
  '<p>Sub picior, pantoful are:</p>'
  + L(('Talpă', 'din spumă, preia șocurile.'), ('Talpă exterioară', 'din cauciuc.'), ('Interior', 'material textil.'))
  + '<p>Numerele 28-39 se potrivesc copiilor de pe la 4 ani în sus.</p>',
  [('model', 'Geox Sneakers pentru copii PRO-RAN FAST IN negri J667JA.0FUM8'), ('material', 'Partea superioară din material textil și sintetic asigură lejeritatea'),
   ('RIPSTOP', 'Utilizarea tehnologiei RIPSTOP în construcția materialului reduce riscul de extindere a rupturilor'),
   ('Respira', 'Tehnologia GEOX Respira™ favorizează eliminarea umidității spre exterior, menținând uscăciunea'), ('șireturi', 'Șireturi elastice facilitează încălțarea și descălțarea rapidă'),
   ('guler', 'Gulerul superior ușor întărit'), ('călcâi', 'Călcâiul întărit'), ('spumă', 'Talpa din spumă susține absorbția șocurilor'), ('talpă', 'Talpa exterioară din cauciuc'),
   ('interior', 'Material textil')],
  {'Model': 'Geox PRO-RAN FAST IN', 'Material': 'textil și sintetic, interior textil, talpă din spumă și cauciuc', 'Caracteristici': 'RIPSTOP, șireturi elastice, Geox Respira™', 'Cod produs': 'J667JA.0FUM8'})

w(11869,
  f'<p>{KS} SHEENY SS TOP KS105538 este o {A("/categorie/bluze-tricouri-hanorace/", "bluză cu mânecă scurtă pentru fete")}, bej, cu model floral, în stil casual, pentru zilele calde de primăvară și vară. Se închide cu un nasture la spate.</p>'
  '<p>Croiala e regulară și clasică, iar materialul neelastic își păstrează forma. Decolteul rotund stă comod la gât.</p>'
  '<p>Ce trebuie știut despre material:</p>'
  + L(('Material', '97% poliester, 3% elastan.'), ('Mâneci', 'scurte, clasice.'), ('Închidere', 'nasture la spate.'))
  + '<p>Mărimile 86 până la 134-140 se potrivesc, de obicei, între 1 și 10 ani.</p>',
  [('model', 'Konges Sløjd Bluză pentru copii SHEENY SS TOP bej înflorată KS105538'), ('floral', 'Model floral'), ('casual', 'în stil casual'),
   ('vară', 'zilele de primăvară și vară'), ('nasture', 'închidere cu nasture la spate'), ('croială', 'Croială regulară'), ('neelastic', 'material textil neelastic'),
   ('decolteu', 'Decolteu rotund'), ('material', '97% Poliester, 3% Elastan'), ('mâneci', 'Mânecă scurtă, clasică')],
  {'Model': 'Konges Sløjd SHEENY SS TOP', 'Material': '97% poliester, 3% elastan', 'Caracteristici': 'mânecă scurtă, model floral, nasture la spate', 'Cod produs': 'KS105538'},
  notes=['Compoziția are 3% elastan, deși magazinul spune „material neelastic”.'])

w(11875,
  f'<p>{KS} COCO PADDED JACKET KS103759 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă matlasată unisex")}, bej, din bumbac organic 100%, cu țesătură ornamentată și căptușeală, pentru sezonul de tranziție. Nu are glugă.</p>'
  '<p>Croiala e simplă, dreaptă, deci încape un pulover dedesubt. Se închide cu nasturi, ușor de desfăcut și de copii, iar matlasarea ține căptușeala la locul ei.</p>'
  '<p>Material și închidere, în câteva cuvinte:</p>'
  + L(('Material', '100% bumbac organic.'), ('Închidere', 'nasturi.'), ('Căptușeală', 'da.'))
  + '<p>Pe site, 86 până la 134-140 înseamnă copii de aproximativ 1-10 ani.</p>',
  [('model', 'Konges Sløjd Geacă de bumbac pentru copii COCO PADDED JACKET culoarea bej, KS103759'), ('matlasat', 'Matlasat'), ('bumbac', '100% Bumbac organic'),
   ('ornamentat', 'Tesatura ornamentata'), ('căptușeală', 'Model cu captuseala'), ('tranziție', 'Izolare: tranzitional'), ('fără glugă', 'Gluga: fara gluga'),
   ('croială', 'Tăiere simplă, fără blocare'), ('nasturi', 'Închiderea convenabilă cu buton')],
  {'Model': 'Konges Sløjd COCO PADDED JACKET', 'Material': '100% bumbac organic', 'Caracteristici': 'matlasată, căptușită, nasturi', 'Cod produs': 'KS103759'})
