import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
GEOX = A('/brand/geox/', 'Geox')

w(9098,
  f'<p>{REIMA} Intona sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni de drumeție unisex")}, negri, de tip jogger, cu membrană impermeabilă de 10000 mm și rezistență la vânt. Sunt gândiți pentru drumeții, trekking și joaca afară pe vreme schimbătoare.</p>'
  '<p>Croiala e relaxed fit, deci vin largi și lasă loc de mișcare, iar talia elastică are reglaj interior, ca să se strângă și pe un copil slab. Crăcii sunt largi, cu șnur de strâns jos.</p>'
  '<p>Pentru teren și pentru seară, pantalonii au:</p>'
  + L(('Întărituri', 'la genunchi și la fese, cu cusături lipite.'), ('Elemente reflectorizante', 'pe picioare.'), ('Respirabilitate', '7000 g/m²/24h.'), ('Căptușeală', 'tip plasă, din material rezistent la murdărie.'))
  + '<p>Mărimile 104-164 sunt pentru copii de pe la 4 până pe la 14 ani.</p>',
  [('model', 'Pantaloni pentru copii Intona negri 5100431A'), ('jogger', 'Joggere de exterior pentru copii'), ('membrană', 'Membrană impermeabilă 10000 mm H2O'),
   ('vânt', 'rezistență la vânt'), ('drumeții', 'Concepuți pentru drumeții și trekking'), ('relaxed', 'croială lejeră relaxed fit'),
   ('talie', 'Talie elastică cu ajustare internă'), ('picior', 'Picior de pantaloni larg cu șnur de strângere'), ('întărituri', 'Întărituri la genunchi și fese și cusături lipite'),
   ('reflectorizante', 'elemente reflectorizante'), ('respirabilitate', 'Respirabilitate 7000 g/m²/24h'), ('căptușeală', 'Căptușeală sintetică tip plasă din material rezistent la murdărie')],
  {'Model': 'Reima Intona', 'Material': '100% poliester acoperit cu TPU', 'Caracteristici': 'membrană 10000 mm, relaxed fit, talie elastică reglabilă, întărituri, reflectorizante', 'Cod produs': '5100431A'})

w(9100,
  f'<p>{A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IG0IG03084 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, bej, ușor izolată, din poliester reciclat. E o geacă de tranziție, pentru toamnă și primăvară, purtată peste un pulover.</p>'
  '<p>Croiala e simplă, iar mânecile au bordură elastică, deci geaca stă mai bine pe corp și se îmbracă ușor. Fără glugă, capul se acoperă cu o piesă din {A("/categorie/caciuli-manusi-accesorii/", "căciulile și mănușile pentru fete")}.</p>'
  '<p>Detaliile:</p>'
  + L(('Închidere', 'capse.'), ('Căptușeală', 'are, cu izolație ușoară.'), ('Glugă', 'nu are.'), ('Material', '100% poliester reciclat.'))
  + '<p>Geaca vine în mărimile 128-176, potrivite de regulă pentru 8-16 ani.</p>',
  [('cod', 'IG0IG03084'), ('culoare', 'culoarea bej'), ('ușor izolat', 'Model ușor izolat'), ('matlasat', 'material matlasat'), ('reciclat', '100% Poliester reciclat'),
   ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă'), ('bordură', 'Mânecile sunt finisate cu o bordură elastică'),
   ('potrivire', 'haina se potrivește mai bine pe corp și este ușor de îmbrăcat'), ('fără glugă', 'Gluga: fara gluga'), ('capse', 'Închiderea convenabilă cu capsă'),
   ('căptușeală', 'Model usor izolat pe captuseala')],
  {'Model': 'Calvin Klein Jeans IG0IG03084', 'Material': '100% poliester reciclat', 'Caracteristici': 'ușor izolată, matlasată, capse, bordură elastică la mâneci', 'Cod produs': 'IG0IG03084'},
  comp={'slug': '/categorie/caciuli-manusi-accesorii/', 'motiv': 'geacă fără glugă'})

w(9102,
  f'<p>{REIMA} Patter 2.0 sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi rezistenți la apă unisex")}, negri, din material sintetic și textil, cu căptușeală moale din textil. Se poartă pe vreme umedă, deși magazinul precizează că nu garantează impermeabilitate completă.</p>'
  '<p>Se închid cu arici, care se strâng pe orice lățime de picior, iar branțul detașabil se scoate pentru curățat și se poate pune lângă piciorul copilului ca să vezi dacă mai e loc.</p>'
  '<p>Pentru drumurile de seară și la încălțat:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede după lăsarea întunericului.'), ('Buclă la spate', 'ajută la încălțat.'), ('Călcâi', 'contor rigid.'), ('Talpă', 'din cauciuc, cu vârf rotund.'))
  + '<p>Numerele 24-36 sunt pentru copii de la cam 2 ani în sus.</p>',
  [('model', 'Pantofi copii Patter 2.0 culoarea negru, 5400042A'), ('impermeabil', 'material impermeabil'), ('căptușeală', 'căptușeală moale din material textil'),
   ('nu complet', 'nu garantează impermeabilitatea completă'), ('arici', 'Închiderea cu velcro'), ('branț', 'Branțul detașabil este ușor de curățat'),
   ('reflectorizante', 'Elementele reflectorizante'), ('buclă', 'Bucla de la spate'), ('călcâi', 'Contorul de călcâi rigid'), ('talpă', 'Talpa exterioară din cauciuc'), ('vârf', 'Varf rotund')],
  {'Model': 'Reima Patter 2.0', 'Material': 'sintetic și textil, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'rezistenți la apă, arici, branț detașabil, reflectorizante', 'Cod produs': '5400042A'})

w(9103,
  f'<p>{TH} KB0KB09887 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă cu glugă pentru băieți")}, neagră, izolată cu umplutură sintetică și căptușită, pentru temperaturile mai reci. Gluga are blăniță artificială și nu se detașează, iar gulerul ridicat apără gâtul.</p>'
  '<p>Fermoarul pe toată lungimea are clapă prinsă cu capse, care ține vântul afară, iar mânecile se termină cu manșetă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar și clapă cu capse.'), ('Glugă', 'cu blăniță artificială, fixă.'), ('Material', '100% poliester, cu fibre reciclate.'))
  + '<p>Mărimile de pe site, 128-176, se potrivesc copiilor de cam 8-16 ani.</p>',
  [('cod', 'KB0KB09887'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat cu captuseala'), ('izolație', 'izolatie sintetica'), ('temperaturi', 'temperaturi mai reci'),
   ('blăniță', 'Gluga cu blanita artificiala, netdetasabila'), ('guler', 'Gulerul ridicat'), ('clapă', 'Închidere cu fermoar pe toată lungimea cu clapă de furtună prinsă cu capse'),
   ('manșetă', 'Finisaj din manseta'), ('reciclat', 'fibre reciclate'), ('material', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KB0KB09887', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'izolată, glugă cu blăniță, fermoar cu clapă cu capse', 'Cod produs': 'KB0KB09887'})

w(9107,
  f'<p>{GEOX} BISLI sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} negri, din piele ecologică și material textil, cu tehnologia Geox Respira: o membrană respirabilă și impermeabilă, care lasă umezeala să iasă și ține apa afară, fără impermeabilitate completă.</p>'
  '<p>Șireturile elastice și aricii fac încălțatul rapid, iar călcâiul întărit ține piciorul în pantof; vârful e rotund.</p>'
  '<p>Ce mai au:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Căptușeală', 'textilă, ușor de curățat.'), ('Închidere', 'șireturi elastice și arici.'))
  + '<p>Numerele 20-27 sunt pentru copii între aproximativ 1 și 4 ani.</p>',
  [('model', 'Sneakers pentru copii BISLI culoarea negru, B461NA.054FU'), ('material', 'combinație de piele ecologică și material textil'),
   ('Respira', 'Tehnologia Geox Respira, datorită unei membrane speciale respirabile și impermeabile'), ('nu complet', 'nu garantează impermeabilitate completă'),
   ('închidere', 'Șireturile elastice și închiderea cu velcro'), ('călcâi', 'Călcâiul întărit'), ('vârf', 'Vârf rotund'), ('talpă', 'Talpa exterioară din cauciuc'),
   ('căptușeală', 'Căptușeala textilă este confortabilă și facilitează curățarea')],
  {'Model': 'Geox BISLI', 'Material': 'piele ecologică și textil, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'membrană Geox Respira, șireturi elastice și arici', 'Cod produs': 'B461NA.054FU'})

w(9111,
  f'<p>{TH} T3A9-33988 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași cu platformă unisex")}, gri, din piele întoarsă și piele ecologică, cu profil scurt. Sunt ușori și făcuți pentru purtat zilnic.</p>'
  '<p>Șireturile sunt plate, ca să nu apese pe partea de sus a piciorului, iar contorul de călcâi rigid ține piciorul în pantof; vârful e rotund și întărit.</p>'
  '<p>Pe dinăuntru și pe dedesubt:</p>'
  + L(('Platformă', 'talpă înălțată, din cauciuc.'), ('Interior', 'textil.'), ('Material', 'piele întoarsă și piele ecologică.'))
  + '<p>Numerele 35-40 sunt pentru copii mari, de obicei de la 10 ani în sus.</p>',
  [('cod', 'T3A9-33988'), ('culoare', 'culoarea gri'), ('material', 'combinația pielii intoarse cu pielea ecologică'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('profil', 'Înălțime: mic de statură'), ('platformă', 'Pantof cu platforma'), ('șireturi', 'Sireturile plate elimina punctele de presiune de pe arcada piciorului'),
   ('călcâi', 'Contorul de călcâi rigid'), ('vârf', 'Cutie rotunda, intarita'), ('interior', 'Interiorul textil'), ('talpă', 'Talpa exterioară din cauciuc')],
  {'Model': 'Tommy Hilfiger T3A9-33988', 'Material': 'piele întoarsă și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'platformă, șireturi plate, călcâi rigid', 'Cod produs': 'T3A9-33988'})

w(9113,
  f'<p>{TH} T4A9-33933 sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, din piele întoarsă, cu profil scurt și branț din piele, făcuți pentru purtat zilnic. Interiorul combină sinteticul cu pielea naturală.</p>'
  '<p>Au șiret, fermoar lateral și arici: fermoarul deschide pantoful la încălțat, iar șiretul rămâne reglat pe picior. Branțul din piele previne frecarea și mirosul neplăcut.</p>'
  '<p>Construcția:</p>'
  + L(('Vârf', 'rigidizat.'), ('Călcâi', 'contor rigidizat.'), ('Branț', 'din piele.'), ('Talpă', 'exterioară, din cauciuc.'))
  + '<p>Numerele 35-40 se potrivesc copiilor de la 10 ani în sus, în general.</p>',
  [('cod', 'T4A9-33933'), ('culoare', 'culoarea alb'), ('material', 'confecționat din piele intoarsa'), ('zilnic', 'ideal pentru purtarea zilnică'), ('profil', 'Înălțime: mic de statură'),
   ('interior', 'Interiorul: Material sintetic, Piele naturala'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('vârf', 'Varf rigidizat'),
   ('călcâi', 'Contorul de călcâi rigidizat'), ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea, abraziunile si aparitia unui miros neplacut'), ('talpă', 'Talpa exterioară din cauciuc')],
  {'Model': 'Tommy Hilfiger T4A9-33933', 'Material': 'piele întoarsă, interior sintetic și piele naturală, talpă din cauciuc', 'Caracteristici': 'șiret, fermoar lateral și arici, branț din piele', 'Cod produs': 'T4A9-33933'})

w(9114,
  f'<p>{REIMA} Vantti în varianta roz este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă softshell unisex")} cu imprimeu vegetal, fără izolație, pentru sezonul de tranziție. Materialul softshell oprește vântul, are impregnare hidrofobă și impermeabilitate de 10.000 mm, deci ține și la ploaie.</p>'
  '<p>E lungă până la genunchi, deci acoperă o bună parte din corp când copilul stă jos sau se joacă; croiala regulară și căptușeala parțială din polar lasă loc de un strat subțire dedesubt. Manșetele au bordură elastică.</p>'
  '<p>Mai are:</p>'
  + L(('Glugă', 'detașabilă.'), ('Elemente reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Buzunar', 'pe piept, cu închidere.'), ('Material', '92% poliester, 8% elastan.'))
  + '<p>Mărimile 86-140 se potrivesc în mare copiilor de 1-10 ani.</p>',
  [('model', 'Jachetă pentru copii Vantti roz 5100009D'), ('softshell', 'Material softshell rezistent la vânt'), ('imprimeu', 'Imprimeu vegetal pe toată suprafața'),
   ('fără izolație', 'Fără izolație'), ('tranziție', 'sezonul de tranziție'), ('hidrofob', 'Impregnare hidrofobă'), ('impermeabilitate', 'Impermeabilitate de 10.000 mm H2O'),
   ('lungime', 'Lungime până la genunchi'), ('croială', 'Croială regulară'), ('polar', 'Căptușeală parțială din polar'), ('manșete', 'Manșete cu bordură elastică'),
   ('glugă', 'Glugă detașabilă'), ('reflectorizante', 'Elemente reflectorizante'), ('buzunar', 'Buzunar pe piept'), ('material', '92% Poliester, 8% Elastan')],
  {'Model': 'Reima Vantti', 'Material': '92% poliester, 8% elastan, softshell', 'Caracteristici': 'softshell, 10.000 mm, lungă până la genunchi, glugă detașabilă, reflectorizante', 'Cod produs': '5100009D'})

w(9115,
  f'<p>{A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IG0IG02056 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, gri, ușor izolată, din poliester neted, cu glugă și logo brodat pe față. E o geacă pentru toamnă și primăvară.</p>'
  '<p>Fasonul e lejer, deci geaca vine largă și se poartă comod peste un hanorac, iar mânecile se termină cu manșetă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Închidere', 'fermoar.'), ('Glugă', 'are.'), ('Căptușeală', 'are, cu izolație ușoară.'), ('Logo', 'brodat pe față.'))
  + '<p>Pe site sunt mărimile 128-176, pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'IG0IG02056'), ('culoare', 'culoarea gri'), ('ușor izolat', 'Model ușor izolat'), ('matlasat', 'Matlasat'), ('neted', 'Material neted'), ('poliester', 'Poliester'),
   ('glugă', 'Gluga: cu gluga'), ('logo', 'Logo-ul mărcii brodat pe față'), ('fason', 'Fason lejer'), ('manșetă', 'Finisaj din manseta'), ('fermoar', 'Incheiere cu fermoar'),
   ('căptușeală', 'Model usor izolat pe captuseala')],
  {'Model': 'Calvin Klein Jeans IG0IG02056', 'Material': 'poliester', 'Caracteristici': 'ușor izolată, matlasată, fason lejer, glugă, logo brodat', 'Cod produs': 'IG0IG02056'})

w(9116,
  f'<p>{GEOX} INEK în varianta albastră sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași cu lumini pentru băieți")}, înalți, din imitație de piele și material textil. Talpa are membrana microporoasă Geox Respira™, care elimină umezeala și ține apa afară, iar luminile încorporate se văd seara.</p>'
  '<p>Profilul înalt, cu guler ușor întărit, acoperă glezna, iar șireturile elastice și aricii se prind repede, fără nod.</p>'
  '<p>Detaliile:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Interior', 'material sintetic și textil.'))
  + '<p>Numerele 24-35 se potrivesc copiilor de pe la 2 până pe la 11 ani.</p>',
  [('model', 'Geox INEK sneakers pentru copii albaștri J669CD.01454'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('Respira', 'Tehnologia Geox Respira'), ('membrană', 'membranei microporoase, care elimină umiditatea la exterior, protejând în același timp împotriva apei'),
   ('lumini', 'Lumini încorporate'), ('profil', 'Profilul înalt al părții superioare'), ('guler', 'gulerul ușor întărit'), ('închidere', 'Șireturi elastice și închidere cu arici'),
   ('talpă', 'Talpă plată din cauciuc'), ('călcâi', 'Călcâi întărit'), ('interior', 'Interiorul din material sintetic și textil')],
  {'Model': 'Geox INEK', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, lumini, Geox Respira™, șireturi elastice și arici', 'Cod produs': 'J669CD.01454'},
  notes=['Titlul de pe site nu are culoare; magazinul arată albastru.'])
print('lot 14 scris')
