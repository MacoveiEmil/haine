import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

FRODDO = A('/brand/froddo/', 'Froddo')
F4 = A('/brand/4f/', '4F')
KS = A('/brand/konges-slojd/', 'Konges Sløjd')
NOTE = 'Pagina magazinului (Fashion Days) nu are descriere detaliată; am folosit doar faptele din titlu.'

w(11633,
  f'<p>Blugii {A("/brand/liewood/", "Liewood")} Borris Printed Denim Pants albaștri sunt {A("/categorie/pantaloni-treninguri/", "pantaloni pentru fete")} din denim de bumbac 100%, cu imprimeu și talie înaltă. Talia are bandă elastică și se poate regla pe dinăuntru, așa că pantalonii pot fi strânși pe măsura copilului.</p>'
  '<p>Pe laterale au două buzunare. Sunt un model simplu de purtat zi de zi, la grădiniță sau la joacă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Talie', 'înaltă, elastică, reglabilă.'), ('Buzunare', 'două laterale.'))
  + '<p>Mărimile 92-140 se potrivesc, cu aproximație, între 2 și 10 ani.</p>',
  [('model', 'Borris Printed Denim Pants'), ('culoare', 'Culoare albastru'), ('denim', 'Model confecționat din denim de bumbac'), ('talie', 'Talie inalta cu banda elastica in talie'),
   ('reglare', 'In talie reglare a latimii interioare'), ('buzunare', 'Două buzunare laterale'), ('material', '100% Bumbac'), ('modele', 'Model: cu modele')],
  {'Model': 'Liewood Borris Printed Denim Pants', 'Material': '100% bumbac', 'Caracteristici': 'talie înaltă, elastică, reglabilă', 'Cod produs': ''},
  notes=['Titlul site-ului are „Borris” în locul culorii; culoarea e cea de la magazin (albastru).', '„La grădiniță sau la joacă” e o sugestie de purtare. Produsul e marcat și „pentru bebe”.'])

w(11658,
  f'<p>Cizmele de iarnă {FRODDO} MINNI SUEDE albastre sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete pentru bebeluși")} izolate, din piele întoarsă, cu interior și branț din lână. Talpa exterioară din cauciuc e plată, antiderapantă, durabilă și rezistentă la deteriorare.</p>'
  '<p>Vârful e rigidizat, iar contrafortul rigidizat sprijină glezna și călcâiul. Se închid cu velcro, deci se pun și se scot repede.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'piele întoarsă.'), ('Interior', 'lână.'), ('Lungime branț', '15,5 cm la numărul 24.'), ('Profil', 'înalt.'))
  + '<p>Numerele 20-24 țin cam de 1-3 ani.</p>',
  [('model', 'MINNI SUEDE'), ('culoare', 'Culoare albastru'), ('izolat', 'Model izolat confecționat din piele intoarsa'), ('lână', 'Interiorul din lana'), ('branț', 'lână'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('antiderapantă', 'antiderapantă'), ('plată', 'plată'), ('vârf', 'Varf rigidizat'),
   ('contrafort', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), ('velcro', 'Închiderea cu velcro'), ('gambă', 'Piele intoarsa'),
   ('lungime', 'Lungimea brantului pentru marimea este de: 15,5 cm'), ('mărime', 'Dimensiunile date pentru marimea: 24'), ('profil', 'înalt')],
  {'Model': 'Froddo MINNI SUEDE', 'Material': 'piele întoarsă, interior din lână', 'Caracteristici': 'izolate, velcro, talpă antiderapantă', 'Cod produs': 'G2110141'})

w(11694,
  f'<p>Geaca bomber {A("/brand/vans/", "Vans")} Denim Baseball Jacket albastră este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de blugi pentru băieți")}, neizolată, din denim de bumbac cu efect prespălat. Materialul e rigid și își păstrează forma, iar căptușeala e din poliester și bumbac.</p>'
  '<p>Se închide cu capse, iar mânecile și marginea de jos au bandă elastică, ca la o geacă de baseball. Tăietura e simplă, fără glugă, și nu e impermeabilă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac.'), ('Căptușeală', '65% poliester, 35% bumbac.'), ('Lungime', '56 cm la mărimea 151-165.'))
  + '<p>Mărimile 129-139.5 până la 165-173 corespund aproximativ vârstei de 8-15 ani.</p>',
  [('model', 'Denim Baseball Jacket'), ('culoare', 'Culoare albastru'), ('bomber', 'Geaca bomber pentru copii din colecția Vans'), ('prespălat', 'denim cu efect prespălat'),
   ('rigid', 'material rigid, care păstrează forma'), ('neizolat', 'Model neizolat cu captuseala'), ('căptușeală', '65% Poliester , 35% Bumbac'),
   ('capse', 'Închiderea convenabilă cu capsă'), ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('glugă', 'fără glugă'), ('impermeabil', 'fără impermeabilitate'), ('material', '100% Bumbac'), ('lungime', 'Lungimea: 56 cm'), ('mărime', '151-165 cm')],
  {'Model': 'Vans Denim Baseball Jacket', 'Material': '100% bumbac (denim)', 'Caracteristici': 'bomber, denim prespălat, capse', 'Cod produs': 'VN000PXMCDX1'})

w(11876,
  f'<p>Cămașa {KS} EMMY SHIRT bleumarin e printre {A("/categorie/bluze-tricouri-hanorace/", "bluzele pentru fete")}, din țesătură ornamentată de bumbac organic certificat GOTS, foarte confortabilă. Are mânecă lungă și broderie decorativă.</p>'
  '<p>Tăietura e simplă, cu guler, și se încheie cu nasturi. Magazinul o încadrează la ocaziile mai elegante, iar bumbacul organic e cultivat fără îngrășăminte sau pesticide, din plante nemodificate genetic.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% bumbac organic.'), ('Mânecă', 'lungă.'), ('Închidere', 'nasturi.'))
  + '<p>Mărimile 92 până la 134-140 acoperă orientativ 2-10 ani.</p>',
  [('model', 'EMMY SHIRT'), ('culoare', 'culoarea bleumarin'), ('ornament', 'confecționat din tesatura ornamentata'), ('organic', 'bumbac organic certificat'), ('pesticide', 'cultivat si recoltat din plante nemodificate genetic, fara utilizarea ingrasamintelor sau pesticidelor'),
   ('confortabil', 'material bumbac extrem de confortabil'), ('mânecă', 'Mânecă: lungă'), ('broderie', 'Broderie decorativa'), ('tăiere', 'Tăiere simplă, fără blocare'),
   ('guler', 'Model cu guler'), ('nasturi', 'Incheiere cu nasturi'), ('elegant', 'Ocazie: elegant'), ('material', '100% Bumbac organic')],
  {'Model': 'Konges Sløjd EMMY SHIRT', 'Material': '100% bumbac organic', 'Caracteristici': 'broderie, guler, nasturi', 'Cod produs': 'KS104294'},
  notes=['Caracteristicile dau „tip de guler: rotund”, descrierea „model cu guler”; nu am detaliat gulerul. Produsul e marcat și „pentru bebe”.'])

w(11892,
  f'<p>Tricoul {A("/brand/united-colors-of-benetton/", "United Colors of Benetton")} 3JERG10J3 roz e printre {A("/categorie/bluze-tricouri-hanorace/", "bluzele pentru fete")} și e făcut din bumbac, un material plăcut pentru zilele obișnuite și pentru vară.</p>'
  '<p>Pe site sunt mărimile 82-116, care merg cam la 1-6 ani. Magazinul nu dă alte detalii despre croială sau finisaje, așa că merită verificat tabelul de mărimi al magazinului înainte de comandă.</p>',
  [('model', 'Tricou pentru fete 3JERG10J3, Bumbac, Roz, Roz')],
  {'Model': 'United Colors of Benetton 3JERG10J3', 'Material': 'bumbac', 'Caracteristici': '', 'Cod produs': '3JERG10J3'},
  insuf=True, notes=[NOTE])

w(11939,
  f'<p>Adidașii {FRODDO} G3130269 bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} din piele naturală, un material care se mulează pe picior, pentru purtat zi de zi, la școală și la plimbare.</p>'
  '<p>Numerele 31-34 de pe site se potrivesc, de obicei, copiilor de 6-11 ani. Magazinul nu dă alte detalii despre croială sau finisaje, așa că merită verificat tabelul de mărimi al magazinului înainte de comandă.</p>',
  [('model', 'Adidasi baieti G3130269, Piele naturala, Bleumarin')],
  {'Model': 'Froddo G3130269', 'Material': 'piele naturală', 'Caracteristici': '', 'Cod produs': 'G3130269'},
  insuf=True, notes=[NOTE])

w(11942,
  f'<p>Cizmele {FRODDO} 301438076 maro sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "ghete pentru băieți")} din piele naturală, într-o nuanță caldă de maro, ușor de asortat cu blugi sau pantaloni de stofă, pentru sezonul rece.</p>'
  '<p>Pe site sunt numerele 25-30, potrivite cu aproximație pentru 2-7 ani. Magazinul nu dă alte detalii despre croială sau finisaje, așa că merită verificat tabelul de mărimi al magazinului înainte de comandă.</p>',
  [('model', 'Cizme baieti 301438076, Piele naturala, Maro, Maro')],
  {'Model': 'Froddo 301438076', 'Material': 'piele naturală', 'Caracteristici': '', 'Cod produs': '301438076'},
  insuf=True, notes=[NOTE, '„Sezonul rece” e dedus din tipul produsului (cizme).'])

w(11957,
  f'<p>Jacheta de trekking {F4} albastră este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} din poliester, cu membrană NeoDry 5000, gândită pentru drumeții și ieșiri în natură pe vreme schimbătoare.</p>'
  '<p>Mărimile 122-164 de pe site merg, în mare, la 7-14 ani. Magazinul nu dă alte detalii despre croială sau finisaje, așa că merită verificat tabelul de mărimi al magazinului înainte de comandă.</p>',
  [('model', 'Jacheta trekking copii Poliester, membrana NeoDry 5000, albastra')],
  {'Model': '4F (jachetă de trekking)', 'Material': 'poliester, membrană NeoDry 5000', 'Caracteristici': 'trekking, membrană', 'Cod produs': ''},
  insuf=True, notes=[NOTE, 'Titlul site-ului are „membrana” în locul culorii; culoarea e cea din titlul magazinului (albastră).'])

w(12023,
  f'<p>Jacheta sport {F4} maro deschis este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă din fleece pentru băieți")}, moale și călduroasă, bună ca strat de mijloc sau singură în zilele răcoroase.</p>'
  '<p>Mărimile 122-164 se potrivesc pe la 7-14 ani. Magazinul nu dă alte detalii despre croială sau finisaje, așa că merită verificat tabelul de mărimi al magazinului înainte de comandă.</p>',
  [('model', 'Jacheta sport baieti, Fleece, Maro deschis')],
  {'Model': '4F (jachetă fleece)', 'Material': 'fleece', 'Caracteristici': 'jachetă sport', 'Cod produs': ''},
  insuf=True, notes=[NOTE, '„Moale și călduroasă” și „strat de mijloc” sunt deduse din material (fleece).'])

w(12025,
  f'<p>Jacheta sport {F4} portocalie este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} din fleece, un material moale și călduros, bun ca strat de mijloc sau de purtat singur în zilele răcoroase.</p>'
  '<p>Pe site sunt mărimile 122-164, care acoperă cu aproximație 7-14 ani. Magazinul nu dă alte detalii despre croială sau finisaje, așa că merită verificat tabelul de mărimi al magazinului înainte de comandă.</p>',
  [('model', 'Jacheta sport copii, Fleece, Portocaliu')],
  {'Model': '4F (jachetă fleece)', 'Material': 'fleece', 'Caracteristici': 'jachetă sport', 'Cod produs': ''},
  insuf=True, notes=[NOTE, '„Moale și călduros” și „strat de mijloc” sunt deduse din material (fleece).'])
