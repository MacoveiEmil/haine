import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(10471,
  f'<p>{A("/brand/reima/", "Reima")} Koivula 5100290B este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă softshell unisex")}, verde, ușoară, neizolată, pentru sezoanele de tranziție. Membrana impermeabilă de 10 000 mm H₂O, materialul rezistent la vânt și impregnarea hidrofobă o fac bună pentru ploaie și vânt.</p>'
  '<p>Croiala e regulară, cu loc pentru straturi dedesubt, iar lungimea ajunge la șolduri. Manșetele cu bordură elastică strâng la încheieturi, iar elastanul din material lasă geaca să se miște cu copilul.</p>'
  '<p>Pentru zilele ude și scurte:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede pe întuneric.'), ('Căptușeală', 'parțială, din polar.'), ('Buzunare', 'laterale, cu fermoar.'), ('Murdărie', 'materialul se curăță ușor.'))
  + '<p>Mărimile 104-164 sunt potrivite, în mare, pentru 4-14 ani.</p>',
  [('model', 'Reima Geacă softshell pentru copii Koivula verde 5100290B'), ('neizolat', 'Lipsa izolației face ca modelul să fie ușor, potrivit pentru sezoanele de tranziție'),
   ('membrană', 'Membrană impermeabilă'), ('impermeabil', 'Impermeabilitate 10 000 mm H₂O'), ('vânt', 'Material rezistent la vânt'), ('hidrofob', 'Impregnare hidrofobă a materialului'),
   ('croială', 'Croială regulară favorizează libertatea de mișcare, permițând purtarea de straturi suplimentare'), ('lungime', 'Lungimea până la șolduri'),
   ('manșete', 'Manșete cu bordură elastică'), ('elastan', '92% Poliester, 8% Elastan'), ('reflectorizant', 'Elemente reflectorizante sporesc vizibilitatea copilului după lăsarea întunericului'),
   ('polar', 'Căptușeală parțială din polar'), ('buzunare', 'Buzunare laterale cu fermoar'), ('murdărie', 'Rezistența la murdărie facilitează menținerea curățeniei')],
  {'Model': 'Reima Koivula', 'Material': '92% poliester, 8% elastan; inserții poliester acoperit cu TPU', 'Caracteristici': 'softshell, 10 000 mm H₂O, rezistentă la vânt, reflectorizante', 'Cod produs': '5100290B'})

w(10476,
  f'<p>{TH} KG0KG09439 este un {A("/categorie/bluze-tricouri-hanorace/", "hanorac pentru fete")}, alb, tip pulover, din tricot moale cu bumbac, poliester și elastan, cu logo Tommy Hilfiger și decolteu rotund. Stilul e casual, pentru purtat zi de zi.</p>'
  '<p>Croiala e lejeră, cu umerii coborâți pe mânecă, deci hanoracul stă larg. Benzile elastice de la bază și manșete îl țin în formă și strâng ușor la încheieturi.</p>'
  '<p>Alte detalii utile:</p>'
  + L(('Material', '78% bumbac, 18% poliester, 4% elastan.'), ('Căptușeală', 'nu are.'), ('Decolteu', 'rotund.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Hanorac pentru copii cu bumbac alb KG0KG09439'), ('pulover', 'Hanoracul tip pulover'), ('tricot', 'Tricot moale'), ('material', '78% Bumbac, 18% Poliester, 4% Elastan'),
   ('logo', 'Model cu logo Tommy Hilfiger'), ('decolteu', 'Decolteu rotund'), ('casual', 'Stilul casual'), ('cotidian', 'ținute cotidiene'), ('croială', 'Croiala lejeră'),
   ('umeri', 'Mânecile cu linia umerilor coborâtă'), ('benzi', 'Benzile elastice de la bază și de la manșete'), ('necăptușit', 'Fără căptușeală')],
  {'Model': 'Tommy Hilfiger KG0KG09439', 'Material': '78% bumbac, 18% poliester, 4% elastan', 'Caracteristici': 'tip pulover, croială lejeră, benzi elastice', 'Cod produs': 'KG0KG09439'})

w(10480,
  f'<p>{GEOX} NASHIK B465NA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} bleumarin, cu profil înalt, din piele naturală, piele întoarsă și material textil, în stil casual. Branțul are imprimeu pentru verificarea mărimii, deci se vede ușor când piciorul a crescut.</p>'
  '<p>Aricii îl lasă pe copil să se încalțe și să se descalțe singur, iar gulerul ușor întărit cuprinde glezna fără să o strângă.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'piele naturală și material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-27 sunt pentru copii de, de regulă, 1-4 ani.</p>'.replace('de, de regulă, 1-4 ani', 'de 1-4 ani, de regulă'),
  [('model', 'Geox NASHIK sneakers pentru copii din piele bleumarin B465NA.0CL22'), ('profil', 'profilul înalt'),
   ('material', 'Partea superioară, din combinație de piele naturală, piele întoarsă și material textil'), ('casual', 'stil casual'),
   ('branț', 'Branț cu imprimeu pentru verificarea mărimii'), ('arici', 'Sistem practic de închidere cu arici'), ('independent', 'încălțarea și descălțarea independentă'),
   ('guler', 'Gulerul ușor întărit al părții superioare'), ('călcâi', 'Călcâi întărit'), ('interior', 'Interiorul finisat cu piele naturală și material textil'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox NASHIK', 'Material': 'piele naturală, piele întoarsă și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici, branț cu imprimeu de mărime', 'Cod produs': 'B465NA.0CL22'})

w(10483,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261109 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} bej, din piele naturală combinată cu imitație, în stil casual și streetwear, făcuți în parteneriatul Biomecanics Podology. Interiorul e din material textil.</p>'
  '<p>Aricii se închid repede și se ajustează pe picior. Vârful rotund, rigidizat și cauciucat lasă degetele libere și le apără, iar călcâiul și gulerul ușor întărite țin piciorul.</p>'
  '<p>Pentru purtat toată ziua:</p>'
  + L(('Branț', 'detașabil.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Partea de sus', 'piele naturală și material sintetic.'))
  + '<p>Numerele 18-25 sunt pentru copii de cam 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele bej 261109'), ('material', 'Partea superioară din combinație de piele naturală și imitație'),
   ('casual', 'Stil casual și streetwear'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership'), ('interior', 'Interior din material textil'),
   ('arici', 'Închidere practică cu arici , care facilitează încălțarea rapidă și ajustarea la picior'), ('vârf', 'Vârf rotund, rigidizat și cauciucat'),
   ('călcâi', 'Călcâi ușor întărit și gulerul superior ușor întărit'), ('branț', 'Branț detașabil'), ('talpă', 'Talpă flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261109', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, vârf cauciucat, branț detașabil', 'Cod produs': '261109'})

w(10491,
  f'<p>{GEOX} NEW EMBERLIX J66DKA sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, din imitație de piele și material textil, cu membrana microporoasă Geox Respira™, care ține picioarele uscate. Stilul e casual, urban.</p>'
  '<p>Inserția elastică ajută pantoful să se adapteze la forma piciorului, iar aricii permit încălțatul rapid, fără ajutor. Călcâiul ușor întărit nu lasă piciorul să alunece.</p>'
  '<p>Înăuntru și dedesubt:</p>'
  + L(('Guler', 'ușor întărit, în jurul gleznei.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 28-35 sunt pentru copii de, în general, 4-11 ani.</p>'.replace('de, în general, 4-11 ani', 'de 4-11 ani, în general'),
  [('model', 'Geox NEW EMBERLIX sneakers pentru copii albi J66DKA.054FU'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('Respira', 'Tehnologia GEOX Respira™ cu membrană microporoasă favorizează eliminarea umidității, menținând picioarele uscate'), ('casual', 'ținutele casual, urbane'),
   ('inserție', 'Inserția elastică în construcția pantofului ajută la adaptarea la forma piciorului'), ('arici', 'Sistemul practic de închidere cu arici'),
   ('călcâi', 'Călcâiul ușor întărit'), ('alunecare', 'minimalizând alunecarea acestuia în pantof'), ('guler', 'Gulerul superior ușor întărit'),
   ('interior', 'Interiorul căptușit cu material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox NEW EMBERLIX', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, inserție elastică, Geox Respira™', 'Cod produs': 'J66DKA.054FU'})

w(10494,
  f'<p>Geaca de blugi {TH} KG0KG08752 este o {A("/categorie/geci-jachete/", "geacă de blugi pentru fete")}, bleumarin, din denim rigid de bumbac, care își păstrează forma, cu aspect spălăcit decorativ. E neizolată și necăptușită, deci pentru zilele blânde de tranziție.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile au manșete care se încheie, deci se strâng pe încheietură. Are guler și nu are glugă.</p>'
  '<p>La purtat, contează și:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'în față.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 128-176 sunt pentru copii de, aproximativ, 8-16 ani.</p>'.replace('de, aproximativ, 8-16 ani', 'de aproximativ 8-16 ani'),
  [('model', 'Tommy Hilfiger Geacă de blugi pentru copii culoarea bleumarin, KG0KG08752'), ('denim', 'Model neizolat confecționat din denim'),
   ('rigid', 'Modelul este realizat dintr-un material rigid, care păstrează forma'), ('spălăcit', 'Denim spalacit decorativ'), ('necăptușit', 'Captuseala: necaptusit'),
   ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Maneci cu mansete incheiate'), ('guler', 'Model cu guler'),
   ('fără glugă', 'Gluga: fara gluga'), ('nasturi', 'Închiderea convenabilă cu buton'), ('buzunare', 'In fata buzunare'), ('material', '100% Bumbac')],
  {'Model': 'Tommy Hilfiger KG0KG08752', 'Material': '100% bumbac (denim)', 'Caracteristici': 'neizolată, necăptușită, denim rigid, nasturi', 'Cod produs': 'KG0KG08752'})

w(10507,
  f'<p>{GEOX} FADINLIGHT J65M4A sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, ușori, cu profil scurt, din material textil și sintetic, cu lumini încorporate pe care copilul le aprinde dintr-un buton. Luminile ajută ca cel mic să fie văzut seara.</p>'
  '<p>Contrafortul rigid ține călcâiul în pantof, ca piciorul să nu alunece, iar vârful e o cutie rotundă, ușor întărită.</p>'
  '<p>Pantoful mai are:</p>'
  + L(('Geox Respira', 'talpă în trei straturi, cu perforări.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 28-31 se potrivesc, cu aproximație, la 4-7 ani.</p>',
  [('model', 'Geox Sneakers pentru copii FADINLIGHT culoarea roz, J65M4A.0NFKC'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu cel sintetic'), ('lumini', 'Model cu lumini incorporate, activate de un buton'), ('călcâi', 'Contorul de călcâi rigid'),
   ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('vârf', 'Cutie rotunda, usor intarita'), RESPIRA,
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox FADINLIGHT', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini cu buton, Geox Respira', 'Cod produs': 'J65M4A.0NFKC'})

w(10520,
  f'<p>{A("/brand/konges-slojd/", "Konges Sløjd")} MAGOT OVERALLS KS104361 este o {A("/categorie/unisex-imbracaminte-salopete-compleuri/", "salopetă cu bretele unisex")}, bleumarin, din țesătură de bumbac 100% cu broderie decorativă, certificată GOTS. Se poartă peste un body, un tricou sau o bluză.</p>'
  '<p>Bretelele nu se detașează, dar sunt reglabile, deci salopeta se potrivește pe măsură ce copilul crește. Croiala e simplă, dreaptă.</p>'
  '<p>Detaliile:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'două în față, plus unul mic.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 74-116 sunt pentru copii de pe la 9 luni până pe la 6 ani.</p>'.replace('de pe la 9 luni până pe la 6 ani', 'mici, cam de la 9 luni la 6 ani'),
  [('model', 'Konges Sløjd Salopetă copii MAGOT OVERALLS GOTS KS104361'), ('bretele', 'Salopetă bretele copii'), ('broderie', 'țesături cu broderie decorativă'),
   ('material', '100% Bumbac'), ('GOTS', 'Global Organic Textile Standard (GOTS)'), ('reglabile', 'Model cu bretele nedetasabile, reglabile'),
   ('croială', 'Tăiere simplă, fără blocare'), ('nasturi', 'Incheiere cu nasturi'), ('buzunare', 'Două buzunare în față'), ('buzunar mic', 'Buzunar mic în față'),
   ('culoare', 'bleumarin')],
  {'Model': 'Konges Sløjd MAGOT OVERALLS', 'Material': '100% bumbac (GOTS)', 'Caracteristici': 'bretele reglabile, nasturi, broderie', 'Cod produs': 'KS104361'},
  notes=['„Se poartă peste un body, un tricou sau o bluză” e dedus din faptul că e salopetă cu bretele.'])

w(10522,
  f'<p>Pantofii {GEOX} TUTIM B9440B sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} roz, ușori, din piele năbuc, cu interior din piele naturală, pentru purtat zilnic. Branțul din piele previne frecarea și mirosul neplăcut.</p>'
  '<p>Velcro-ul se închide repede și se strânge după picior, iar contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece în pantof.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Vârf', 'rotund.'), ('Geox Respira', 'talpă în trei straturi, perforată.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 18-23 sunt pentru copii de 1-3 ani, în mare.</p>',
  [('model', 'Geox Pantofi năbuc pentru copii TUTIM culoarea roz, B9440B.007NF'), ('năbuc', 'Model confectionat din piele nabuc'), ('ușor', 'Model ușor'),
   ('interior', 'Interiorul: Piele naturala'), ('zilnic', 'purtarea zilnică'), ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea'),
   ('miros', 'aparitia unui miros neplacut'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('călcâi', 'Contorul de călcâi rigid'),
   ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării'), ('vârf', 'Varf rotund'), RESPIRA,
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox TUTIM', 'Material': 'piele năbuc, interior din piele naturală, talpă din cauciuc', 'Caracteristici': 'velcro, branț din piele, Geox Respira', 'Cod produs': 'B9440B.007NF'})

w(10533,
  f'<p>Geaca de blugi {A("/brand/guess/", "Guess")} L6RL13 D5FM0 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de blugi pentru băieți")}, albastră, din denim ușor elastic, cu aspect spălăcit decorativ. E neizolată și fără căptușeală, pentru sezonul de tranziție.</p>'
  '<p>Croiala e simplă, dreaptă, iar manșetele se încheie, deci se strâng pe încheietură. Elastanul din țesătură îi dă libertate la mișcare. Gulerul e moale.</p>'
  '<p>Buzunarele și închiderea:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare la piept', 'două, cu nasturi.'), ('Buzunare laterale', 'două.'), ('Material', '99% bumbac, 1% elastan.'))
  + '<p>Mărimile 122-125 până la 175 sunt pentru copii de 7-16 ani, de obicei.</p>',
  [('model', 'Guess Geacă de blugi pentru copii L6RL13 D5FM0'), ('denim', 'Model neizolat confecționat din denim'), ('elastic', 'Țesătura ușor elastică'),
   ('spălăcit', 'Denim spalacit decorativ'), ('necăptușit', 'Model neizolat fara captuseala'), ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă, fără blocare'),
   ('manșete', 'Maneci cu mansete incheiate'), ('guler', 'Model cu guler moale'), ('nasturi', 'Închiderea convenabilă cu buton'),
   ('buzunare piept', 'Două buzunare la piept cu nasturi'), ('buzunare laterale', 'Două buzunare laterale'), ('material', '99% Bumbac, 1% Elastan'), ('culoare', 'albastru')],
  {'Model': 'Guess L6RL13 D5FM0', 'Material': '99% bumbac, 1% elastan (denim)', 'Caracteristici': 'neizolată, necăptușită, denim ușor elastic, patru buzunare', 'Cod produs': 'L6RL13 D5FM0'})
