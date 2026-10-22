import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(8665,
  f'<p>{REIMA} Tromssa este o {A("/categorie/bebe-imbracaminte-salopete-compleuri/", "salopetă de iarnă pentru bebeluși")} și copii mici, verde, izolată și căptușită, cu glugă. Materialul are acoperire din poliuretan și tratamentul BIONIC-FINISH® ECO, o alternativă ecologică la DWR, care respinge apa, deci e bună pentru zăpadă și joaca afară pe frig.</p>'
  '<p>Fiind dintr-o bucată, salopeta nu lasă zăpada să intre pe la mijloc când copilul stă jos sau se rostogolește, iar croiala simplă lasă loc pentru hainele de dedesubt.</p>'
  '<p>Se îmbracă și se dezbracă repede:</p>'
  + L(('Închidere', 'fermoar.'), ('Glugă', 'are.'), ('Mâneci', 'lungi.'), ('Material', '100% poliester, acoperire 100% poliuretan.'))
  + '<p>Salopeta are mărimile 92-140, potrivite pentru copii între aproximativ 2 și 10 ani.</p>',
  [('model', 'Salopeta copii Tromssa culoarea verde, 5100043A'), ('mânecă', 'Model cu maneca lunga'), ('BIONIC', 'BIONIC-FINISH® ECO'),
   ('DWR', 'o alternativa ecologica la acoperirea traditionala, hidrofoba DWR'), ('izolat', 'Model izolat cu captuseala'), ('croială', 'Tăiere simplă'),
   ('fermoar', 'Incheiere cu fermoar'), ('glugă', 'Model cu gluga'), ('material', 'Materialul de baza: 100% Poliester'), ('acoperire', 'Acoperire: 100% Poliuretan')],
  {'Model': 'Reima Tromssa', 'Material': '100% poliester, acoperire 100% poliuretan', 'Caracteristici': 'izolată, căptușită, BIONIC-FINISH® ECO, glugă, fermoar', 'Cod produs': '5100043A'})

w(8671,
  f'<p>{REIMA} Loikkii sunt {A("/categorie/incaltaminte-pantofi/", "pantofi de exterior pentru fete")}, bordo, din material sintetic și textil cu acoperire Vegan PU și tratament rezistent la apă, fără PFC. Nu sunt izolați, deci sunt pentru toamnă și primăvară, pe vreme umedă.</p>'
  '<p>Au șireturi rapide cu opritor: se strâng dintr-o tragere, fără nod, și se potrivesc pe orice lățime de picior. Partea de sus urcă pe gleznă și o ține fixă.</p>'
  '<p>Pentru drumuri pe teren denivelat sau pe întuneric:</p>'
  + L(('Talpă', 'din cauciuc, cu caneluri.'), ('Elemente reflectorizante', 'se văd după lăsarea întunericului.'), ('Călcâi', 'contor rigid.'), ('Buclă la spate', 'pentru încălțat.'))
  + '<p>Numerele 32-40 se potrivesc copiilor de la aproximativ 8 ani în sus.</p>',
  [('model', 'Pantofi copii Loikkii culoarea bordo, 5400143A'), ('Vegan PU', 'Vegan PU este o alternativă ecologică la PVC'), ('PFC', 'PFC Repellent'),
   ('rezistență la apă', 'rezistenta la apa'), ('neizolat', 'Izolare: neizolat'), ('material', 'Gamba: Material sintetic, Material textil'),
   ('șireturi', 'Sistemul rapid de șireturi cu comutatoare'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('talpă', 'Talpa exterioară din cauciuc cu caneluri'), ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'),
   ('călcâi', 'Contorul de călcâi rigid'), ('buclă', 'Bucla de la spate')],
  {'Model': 'Reima Loikkii', 'Material': 'sintetic și textil, Vegan PU, talpă din cauciuc', 'Caracteristici': 'rezistenți la apă, șireturi rapide, reflectorizante, neizolați', 'Cod produs': '5400143A'})

w(8674,
  f'<p>{A("/brand/mayoral/", "Mayoral")} 7401 este o {A("/categorie/geci-jachete/", "jachetă din blăniță artificială pentru fete")}, neagră, din 100% poliester, făcută pentru zilele mai răcoroase ale sezonului de tranziție. Se poartă zilnic sau la ocazii.</p>'
  '<p>Croiala e regulară, cu lungime până la șolduri și mâneci clasice, așa că jacheta stă drept pe corp, fără să fie strâmtă.</p>'
  '<p>Fără glugă, jacheta are un aspect clasic:</p>'
  + L(('Guler', 'clasic.'), ('Buzunare', 'laterale.'), ('Închidere', 'fermoar.'), ('Material', 'imitație de blană, uni.'))
  + f'<p>Pentru vânt, gâtul se acoperă cu o eșarfă din {A("/categorie/caciuli-manusi-accesorii/", "căciulile, mănușile și accesoriile pentru fete")}. Jacheta vine în mărimile 128-167, pentru copii de aproximativ 8-14 ani.</p>',
  [('cod', 'Jachetă pentru copii neagră 7401'), ('blană', 'Confecționată din imitație de blană'), ('tranziție', 'zilele mai răcoroase ale sezonului de tranziție'),
   ('ocazii', 'purtată zilnic și la ocazii speciale'), ('material', '100% Poliester'), ('croială', 'Croiala regulară'), ('lungime', 'Lungimea până la șolduri'),
   ('mâneci', 'Tipul de mânecă clasic'), ('fără glugă', 'Lipsa glugii'), ('eșarfe', 'stilizarea cu eșarfe'), ('guler', 'Gulerul clasic'), ('buzunare', 'Buzunare laterale practice'),
   ('fermoar', 'Sistemul de închidere cu fermoar'), ('uni', 'model uni')],
  {'Model': 'Mayoral 7401', 'Material': '100% poliester, imitație de blană', 'Caracteristici': 'croială regulară, lungă până la șolduri, fără glugă, guler clasic, fermoar', 'Cod produs': '7401'},
  comp={'slug': '/categorie/caciuli-manusi-accesorii/', 'motiv': 'jachetă fără glugă, se poartă cu eșarfă'},
  notes=['Titlul de pe site nu are culoare; magazinul dă negru.'])

w(8683,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 262230 sunt sandale maro, listate pe site la {A("/categorie/baieti-incaltaminte-pantofi/", "încălțămintea de vară pentru băieți")}, din piele naturală și material sintetic, pentru vară și activitățile zilnice. Stilul e casual, ușor de purtat cu haine lejere.</p>'
  '<p>Construcția deschisă ține piciorul aerisit în zilele calde, iar închiderea cu arici se ajustează repede pe picior.</p>'
  '<p>Ce mai are sandaua:</p>'
  + L(('Talpă', 'din cauciuc.'), ('Interior', 'căptușit cu material textil.'), ('Tehnologie', 'Biomecanics Podology Partnership.'))
  + '<p>Numerele de pe site sunt 28-34, cam pentru copii de 4-11 ani.</p>',
  [('cod', '262230'), ('culoare', 'Acest model de culoare maro'), ('sandale', 'Sandale pentru băieți'), ('vară', 'potrivite pentru activitățile de vară'),
   ('material', 'Partea superioară din piele naturală și material sintetic'), ('casual', 'Stil casual'), ('deschis', 'Construcția deschisă'),
   ('arici', 'Închiderea cu velcro'), ('talpă', 'Talpa din cauciuc'), ('interior', 'Interiorul căptușit cu material textil'), ('Podology', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 262230', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'sandale, arici, Podology Partnership', 'Cod produs': '262230'},
  notes=['Pe site e în categoria Pantofi; produsul e sanda.'])

w(8702,
  f'<p>{TH} KS0KS00657 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă reversibilă unisex")}, bej, subțire, din poliester reciclat moale. Se poartă pe ambele fețe și e făcută pentru zilele de tranziție.</p>'
  f'<p>Croiala e simplă și geaca nu are glugă, deci se poartă ușor peste un hanorac sau o bluză; pentru vânt, capul se acoperă cu ceva din {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "căciulile și accesoriile unisex")}.</p>'
  '<p>Detaliile, pe scurt:</p>'
  + L(('Fețe', 'două, geaca se poate întoarce.'), ('Buzunare', 'oblice, exterioare.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester reciclat.'))
  + '<p>Mărimile 128-176 sunt pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'KS0KS00657'), ('culoare', 'culoarea bej'), ('subțire', 'Model subțire'), ('moale', 'material moale'), ('două fețe', 'Model cu doua fete'),
   ('tranziție', 'Izolare: tranzitional'), ('reciclat', '100% Poliester reciclat'), ('croială', 'Tăiere simplă'), ('fără glugă', 'Gluga: fara gluga'),
   ('buzunare', 'Buzunare oblice exterioare'), ('fermoar', 'Incheiere cu fermoar')],
  {'Model': 'Tommy Hilfiger KS0KS00657', 'Material': '100% poliester reciclat', 'Caracteristici': 'reversibilă, subțire, fără glugă, buzunare oblice', 'Cod produs': 'KS0KS00657'},
  comp={'slug': '/categorie/unisex-accesorii-caciuli-manusi-accesorii/', 'motiv': 'geacă fără glugă'})

w(8704,
  f'<p>{REIMA} Mutka este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă de iarnă pentru bebeluși")} și copii mici, bleumarin, izolată cu Fellex® din poliester reciclat. E rezistentă la apă, iar cusăturile principale sunt etanșate cu bandă, ca să nu treacă vântul și umezeala.</p>'
  '<p>Croiala e simplă, cu loc pentru un strat cald dedesubt, iar gluga cu blăniță artificială se detașează când nu e nevoie de ea.</p>'
  '<p>Pentru plimbările de iarnă:</p>'
  + L(('Buzunare', 'cu închidere.'), ('Tratament', 'BIONIC-FINISH® ECO, hidrofob.'), ('Certificări', 'Bluesign® și GRS (materiale reciclate).'), ('Apă', 'rezistență sporită, fără impermeabilitate completă.'))
  + '<p>Mărimile 74-110 sunt pentru copii între aproximativ 9 luni și 5 ani.</p>',
  [('model', 'Reima Mutka bleumarin 5100037B'), ('izolat', 'Model izolat cu captuseala'), ('Fellex', 'Izolație Fellex® din poliester reciclat 100%'), ('apă', 'Rezistent la apa'),
   ('cusături', 'Cusăturile principale cu bandă etanșează și împiedică vântul și umezeala'), ('croială', 'Tăiere simplă'),
   ('glugă', 'Gluga cu blanita artificiala, detasabila'), ('buzunare', 'Buzunare incheiate'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('Bluesign', 'Model certificat Bluesign'),
   ('GRS', 'GRS (Global Recycle Standard)'), ('nu complet', 'nu garantează impermeabilitatea completă')],
  {'Model': 'Reima Mutka', 'Material': 'poliester reciclat, izolație Fellex®', 'Caracteristici': 'izolată, rezistentă la apă, cusături cu bandă, glugă detașabilă cu blăniță', 'Cod produs': '5100037B'})

w(8706,
  f'<p>{GEOX} are în acest model {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, din material textil și piele ecologică, cu membrana impermeabilă Geox Respira. Rezistă la umezeală în zilele de toamnă, cu mențiunea magazinului că nu garantează impermeabilitate completă.</p>'
  '<p>Se închid cu scai, deci se prind repede pe orice lățime de picior; vârful e rotund și moale, iar gulerul ușor rigidizat.</p>'
  '<p>Pe dedesubt și în interior:</p>'
  + L(('Talpă', 'sculptată.'), ('Călcâi', 'ușor rigidizat la spate.'), ('Interior', 'textil.'), ('Profil', 'scurt.'))
  + '<p>Pe site sunt numerele 28-35, în general pentru copii de 4-11 ani.</p>',
  [('model', 'Sneakers pentru copii culoarea alb'), ('material', 'combinatia materialului textil cu pielea ecologica'), ('membrană', 'Membrana unica si impermeabila a tehnologiei Geox Respira'),
   ('nu complet', 'nu garantează impermeabilitatea completă'), ('scai', 'Incheiere cu scai'), ('vârf', 'Cutie rotunda si moale'), ('guler', 'Gulerul gambei usor rigidizat'),
   ('talpă', 'Talpa sculptata'), ('călcâi', 'Spatele calcaiului usor rigidizat'), ('interior', 'Interior textil'), ('profil', 'Înălțime: mic de statură')],
  {'Model': 'Geox, adidași', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'membrană Geox Respira, scai, talpă sculptată', 'Cod produs': ''})

w(8707,
  f'<p>Adidașii {GEOX} violet de aici sunt {A("/categorie/adidasi/", "adidași pentru fete")} din textil și piele ecologică, cu exterior neporos, care se curăță ușor cu o cârpă umedă. Au sistemul Geox Respira, cu talpă în trei straturi.</p>'
  '<p>Se leagă cu șiret clasic, care se strânge exact pe picior, iar călcâiul e întărit și căptușit moale, ca să nu roadă.</p>'
  '<p>Partea solidă a pantofului:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Vârf', 'rotund, întărit.'), ('Interior', 'textil.'), ('Profil', 'scurt.'))
  + '<p>Modelul vine în numerele 28-35, adică pentru copii de cam 4-11 ani.</p>',
  [('model', 'Sneakers pentru copii culoarea violet'), ('material', 'combinatia materialului textil cu pielea ecologica'), ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'),
   ('Respira', 'talpei in trei straturi cu sistemul de perforari'), ('șiret', 'Șiretul clasic permite ajustarea individuală'),
   ('călcâi', 'Călcâiul întărit cu umplutură moale protejează călcâiul împotriva abraziunii'), ('talpă', 'Talpa exterioară din cauciuc'), ('vârf', 'Cutie rotunda, intarita'),
   ('interior', 'Interiorul textil'), ('profil', 'Înălțime: mic de statură')],
  {'Model': 'Geox, adidași', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șiret, călcâi căptușit', 'Cod produs': ''})

w(8721,
  f'<p>{TH} KB0KB09311 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză pentru băieți")}, albastră, din material cu mult bumbac, fără glugă. E o bluză simplă, cu decolteu rotund în coaste.</p>'
  '<p>Mânecile și marginea de jos sunt finisate cu bandă elastică, deci bluza stă strânsă la încheieturi și pe șolduri, chiar dacă croiala e simplă și dreaptă.</p>'
  '<p>Din ce e făcută:</p>'
  + L(('Material', '60% bumbac, 40% poliester.'), ('Bandă elastică', '95% bumbac, 5% elastan.'), ('Decolteu', 'rotund, în coaste.'))
  + '<p>Mărimile 128-176 se potrivesc copiilor de pe la 8 până pe la 16 ani.</p>',
  [('cod', 'KB0KB09311'), ('culoare', 'albastru'), ('bumbac', 'continut ridicat de bumbac'), ('fără glugă', 'Gluga: fara gluga'), ('decolteu', 'Decolteu rotund, în coaste'),
   ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('croială', 'Tăiere simplă'), ('material', 'Materialul de baza: 60% Bumbac, 40% Poliester'),
   ('bandă', 'Banda elastica: 95% Bumbac, 5% Elastan')],
  {'Model': 'Tommy Hilfiger KB0KB09311', 'Material': '60% bumbac, 40% poliester', 'Caracteristici': 'decolteu rotund în coaste, bandă elastică la mâneci și bază', 'Cod produs': 'KB0KB09311'},
  notes=['Titlul de pe site nu are culoare; magazinul dă albastru.'])
print('lot 6 scris')
