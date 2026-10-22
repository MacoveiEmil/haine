import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(10428,
  f'<p>{GEOX} BIGLIA B554DA sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} bej, din piele naturală și piele întoarsă, cu interior și branț tot din piele. Tehnologia Geox Respira™ scoate umiditatea, iar sistemul Flexy din talpă lasă piciorul să se îndoaie natural.</p>'
  '<p>Aricii se închid repede și se reglează precis pe picior, iar finisajul interior moale cuprinde piciorul fără să strângă.</p>'
  '<p>Pe scurt, din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'piele naturală și piele întoarsă.'), ('Interior și branț', 'piele naturală.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 18-26 se poartă, în general, între 1 și 4 ani.</p>',
  [('model', 'Geox Pantofi pentru copii din piele BIGLIA bej B554DA.08520'), ('material', 'Partea superioară din piele naturală și piele întoarsă'),
   ('interior', 'Interiorul căptușit cu piele naturală'), ('branț', 'Branțul din piele naturală'), ('Respira', 'Tehnologia Geox Respira™'), ('umiditate', 'eliminând umiditatea spre exterior'),
   ('Flexy', 'Sistemul Flexy în talpă susține mișcarea naturală a piciorului'), ('arici', 'Închidere practică cu arici facilitează încălțarea rapidă și o ajustare precisă'),
   ('finisaj', 'Finisajul interior moale'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox BIGLIA', 'Material': 'piele naturală și piele întoarsă, interior din piele, talpă din cauciuc', 'Caracteristici': 'arici, Geox Respira™, sistem Flexy', 'Cod produs': 'B554DA.08520'})

w(10433,
  f'<p>Geaca {TH} KB0KB10587 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, bleumarin, de tip windbreaker, din nailon 100%, care oprește rafalele de vânt. Are modele cu logo și inscripție și e ușoară, pentru ieșirile de primăvară și toamnă.</p>'
  '<p>Croiala e relaxed fit, cu lungimea până la șolduri, iar tivul și manșetele cu bordură elastică strâng geaca pe corp, ca să nu fluture în vânt.</p>'
  '<p>Pentru zilele cu vreme schimbătoare:</p>'
  + L(('Glugă', 'integrată.'), ('Căptușeală', 'parțială, din plasă.'), ('Buzunare', 'laterale, tip slip-on.'), ('Închidere', 'fermoar pe toată lungimea.'))
  + '<p>Mărimile 104-122 sunt pentru copii de cam 4-7 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă de tranziție pentru copii bleumarin KB0KB10587'), ('windbreaker', 'Construcția gecii windbreaker protejează împotriva rafalelor de vânt'),
   ('material', '100% Nailon'), ('logo', 'Decorată cu modele cu logo și inscripție'), ('sezon', 'activitățile în aer liber de primăvară și toamnă'), ('ușoară', 'geacă ușoară de tranziție'),
   ('croială', 'Croiala relaxed fit'), ('lungime', 'Lungimea până la șolduri'), ('elastic', 'Tivul și manșetele cu bordură elastică'), ('glugă', 'Gluga integrată'),
   ('plasă', 'Căptușeala parțială din plasă'), ('buzunare', 'Buzunarele practice laterale slip-on'), ('fermoar', 'Închiderea cu fermoar pe toată lungimea')],
  {'Model': 'Tommy Hilfiger KB0KB10587', 'Material': '100% nailon', 'Caracteristici': 'windbreaker, glugă integrată, căptușeală din plasă, tiv și manșete elastice', 'Cod produs': 'KB0KB10587'})

w(10434,
  f'<p>Botinele {BIO} 261161 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete pentru bebeluși")} gri, din piele întoarsă, cu motiv animal, pentru perioada de tranziție. Sunt făcute în parteneriatul Biomecanics Podology, cu podologi, și urcă deasupra gleznei.</p>'
  '<p>Închiderea dublă, cu arici și fermoar, deschide botina larg la încălțat și o strânge apoi după picior. Gulerul moale nu irită glezna, iar vârful rotund lasă loc degetelor.</p>'
  '<p>Pentru joacă, botina are:</p>'
  + L(('Vârf', 'rotund, întărit, apără de lovituri.'), ('Călcâi', 'întărit.'), ('Căptușeală și branț', 'textile.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 19-26 sunt, de obicei, pentru copii de 1-4 ani.</p>',
  [('model', 'Biomecanics Botine pentru copii din piele întoarsă gri 261161'), ('piele întoarsă', 'Partea superioară din piele întoarsă'), ('motiv', 'Motivul animal adorabil'),
   ('tranziție', 'perioada de tranziție'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership , dezvoltată în colaborare cu podologi'),
   ('gleznă', 'Construcția deasupra gleznei'), ('închidere', 'Închiderea dublă cu arici și fermoar'), ('guler', 'Gulerul moale al părții superioare minimizează riscul de iritații'),
   ('vârf', 'Vârful rotund, întărit oferă spațiu pentru degete și protecție suplimentară împotriva loviturilor'), ('călcâi', 'Călcâiul întărit'),
   ('căptușeală', 'Căptușeala și branțul textil'), ('talpă', 'Talpa din cauciuc')],
  {'Model': 'Biomecanics 261161', 'Material': 'piele întoarsă, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'arici și fermoar, vârf întărit, motiv animal', 'Cod produs': '261161'})

w(10440,
  f'<p>{A("/brand/ugg/", "UGG")} LO LOWMEL 1166490K sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} negri, ușori, cu profil scurt, din material textil și piele întoarsă, pentru purtat zilnic. Talpa e din spumă, iar interiorul textil se ține ușor curat.</p>'
  '<p>Vârful rotund, ușor rigid, lasă degetele să se așeze liber. Șireturile plate nu apasă pe arcada piciorului, iar bucla de la spate ajută la tras pantoful pe picior.</p>'
  '<p>Pe scurt:</p>'
  + L(('Călcâi', 'contrafort rigidizat.'), ('Talpă', 'din spumă.'), ('Partea de sus', 'material textil și piele întoarsă.'))
  + '<p>Numerele 31-36 sunt pentru copii de la, aproximativ, 6 ani în sus.</p>',
  [('model', 'UGG Sneakers pentru copii LO LOWMEL culoarea negru, 1166490K'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea întoarsă'), ('zilnic', 'purtarea zilnică'), ('talpă', 'Talpa din spumă'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('degete', 'degetele se pot aranja liber în pantof'), ('șireturi', 'Sireturile plate elimina punctele de presiune de pe arcada piciorului'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('călcâi', 'Contorul de călcâi rigidizat')],
  {'Model': 'UGG LO LOWMEL', 'Material': 'textil și piele întoarsă, interior textil, talpă din spumă', 'Caracteristici': 'șireturi plate, buclă la spate', 'Cod produs': '1166490K'},
  notes=['Titlul și h1 spun negru; atributul de culoare al magazinului spune roz.'])

w(10441,
  f'<p>Pantofii clasici {A("/brand/primigi/", "Primigi")} PTR 24112 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} maro, din piele nubuc cu textură netedă, cu interior și branț din piele naturală. Stilul e casual, pentru activitățile zilnice ale copiilor mici.</p>'
  '<p>Vârful e lat, de tip barefoot, deci degetele stau natural și încape și un picior mai lat. Aricii permit încălțatul fără ajutor, iar călcâiul moale și gulerul nu fac bătături.</p>'
  '<p>Mai sunt de știut:</p>'
  + L(('Vârf', 'cauciucat, apără degetele la joacă.'), ('Talpă', 'din cauciuc, flexibilă.'), ('Interior', 'piele naturală.'))
  + '<p>Mărimile 20-29 sunt potrivite, cu aproximație, pentru 1-5 ani.</p>',
  [('model', 'Primigi Pantofi pentru copii din nubuck maro PTR 24112'), ('nubuc', 'Fața superioară din piele nubuc'), ('neted', 'Textura netedă'),
   ('interior', 'Interiorul din piele naturală'), ('branț', 'Branțul din piele naturală'), ('casual', 'Stilul casual'), ('zilnic', 'activitățile zilnice'),
   ('vârf lat', 'Vârful lat tip barefoot permite o poziționare naturală a degetelor'), ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă de către copii'),
   ('călcâi', 'Călcâiul moale și gulerul feței superioare minimizează riscul de iritații și bătături'), ('vârf cauciucat', 'Vârful cauciucat protejează degetele'),
   ('talpă', 'Talpa din cauciuc'), ('flexibil', 'contribuie la flexibilitate')],
  {'Model': 'Primigi PTR 24112', 'Material': 'piele nubuc, interior și branț din piele naturală, talpă din cauciuc', 'Caracteristici': 'vârf lat barefoot, arici, vârf cauciucat', 'Cod produs': 'PTR 24112'})

w(10455,
  f'<p>Geaca bomber {TH} KG0KG08316 este o {A("/categorie/geci-jachete/", "geacă bomber pentru fete")}, roz, din bumbac 100% cu aplicație, ușor izolată pe căptușeală, pentru sezonul de tranziție. Nu are glugă.</p>'
  '<p>Croiala e lejeră, deci încape un hanorac dedesubt și vine comod și unui copil mai plinuț. Mânecile se termină cu manșetă, care strânge bomberul la încheieturi.</p>'
  '<p>Pe scurt, despre bomber:</p>'
  + L(('Închidere', 'capse.'), ('Buzunare', 'în față.'), ('Material', '100% bumbac.'))
  + '<p>Mărimile 128-176 sunt pentru copii de în jur de 8-16 ani.</p>',
  [('model', 'Tommy Hilfiger Geacă bomber pentru copii culoarea roz, KG0KG08316'), ('aplicație', 'material textil cu aplicatie'), ('material', '100% Bumbac'),
   ('izolat', 'Model usor izolat pe captuseala'), ('tranziție', 'Izolare: tranzitional'), ('fără glugă', 'Gluga: fara gluga'), ('croială', 'Croială lejeră'),
   ('manșetă', 'Finisaj din manseta'), ('capse', 'Incheiere cu cleme'), ('buzunare', 'In fata buzunare'), ('bomber', 'Fit: bomber')],
  {'Model': 'Tommy Hilfiger KG0KG08316', 'Material': '100% bumbac', 'Caracteristici': 'bomber, ușor izolat, capse, croială lejeră', 'Cod produs': 'KG0KG08316'})

w(10460,
  f'<p>{A("/brand/reima/", "Reima")} Puruton BugProof 5100376A este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de tranziție unisex")}, verde, neizolată și fără căptușeală, din țesătură rezistentă care apără de vânt și precipitații ușoare. Finisajul Reima BugProof, cu geraniol, ajută la respingerea țânțarilor și căpușelor.</p>'
  '<p>Croiala e dreaptă, cu lungimea până la șolduri, iar tivul se strânge cu șnur cu opritor, deci geaca se ajustează pe un copil mai slab și nu lasă vântul să intre.</p>'
  '<p>Pentru plimbările din natură:</p>'
  + L(('Glugă', 'detașabilă.'), ('Elemente reflectorizante', 'copilul se vede după lăsarea întunericului.'), ('Buzunare', 'laterale, cu fermoar.'), ('Închidere', 'fermoar pe toată lungimea.'))
  + '<p>Mărimile 110-164 sunt pentru copii de, în general, 5-14 ani.</p>'.replace('de, în general, 5-14 ani', 'de 5-14 ani, în general'),
  [('model', 'Reima Jachetă pentru copii Puruton BugProof verde 5100376A'), ('neizolat', 'Lipsa izolației termice'), ('necăptușit', 'Construcția fără căptușeală'),
   ('țesătură', 'Realizată dintr-o țesătură rezistentă , care oferă protecție împotriva vântului și a precipitațiilor ușoare'),
   ('BugProof', 'Finisaj Reima BugProof , care conține geraniol, ajută la respingerea țânțarilor și a căpușelor'), ('croială', 'Croiala dreaptă'),
   ('lungime', 'Lungimea până la șolduri'), ('tiv', 'Posibilitatea de ajustare a tivului inferior cu șnururi cu opritor'), ('glugă', 'Gluga detașabilă'),
   ('reflectorizant', 'Elementele reflectorizante integrate sporesc vizibilitatea copilului după lăsarea întunericului'),
   ('buzunare', 'Buzunarele laterale practice cu fermoar'), ('fermoar', 'Închidere cu fermoar pe toată lungimea')],
  {'Model': 'Reima Puruton BugProof', 'Material': '100% poliester', 'Caracteristici': 'BugProof, neizolată, glugă detașabilă, tiv cu șnur, reflectorizante', 'Cod produs': '5100376A'})

w(10461,
  f'<p>Pantofii {BIO} 262100 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} albi, din piele naturală netedă, în stil casual, pentru primăvară și vară. Tehnologia ANTI-ODOR limitează formarea mirosurilor, iar modelul e făcut în parteneriatul Biomecanics Podology.</p>'
  '<p>Scaiul se închide repede și se strânge după piciorul copilului. Branțurile se scot, deci se curăță ușor și se poate măsura piciorul pe ele.</p>'
  '<p>Pe scurt:</p>'
  + L(('Vârf', 'cauciucat, apără degetele.'), ('Interior', 'material textil.'), ('Talpă', 'din cauciuc, flexibilă.'))
  + '<p>Numerele 19-25 sunt pentru cei mici de cam 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele albi 262100'), ('piele', 'Partea superioară din piele naturală netedă'), ('casual', 'caracter casual'),
   ('sezon', 'potriviți pentru primăvară și vară'), ('ANTI-ODOR', 'Tehnologia ANTI-ODOR limitează dezvoltarea microorganismelor și formarea mirosurilor neplăcute'),
   ('parteneriat', 'Biomecanics Podology Partnership'), ('scai', 'Închiderea cu scai facilitează încălțarea rapidă și ajustarea pe piciorul copilului'),
   ('branțuri', 'Branțurile detașabile permit o curățare ușoară'), ('vârf', 'Vârful cauciucat ajută la protejarea degetelor'), ('interior', 'Interiorul din material textil'),
   ('talpă', 'Talpa din cauciuc susține flexibilitatea')],
  {'Model': 'Biomecanics 262100', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'scai, ANTI-ODOR, branțuri detașabile', 'Cod produs': '262100'})

w(10466,
  f'<p>Ghetele de iarnă {BIO} 261102 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "încălțăminte de iarnă pentru bebeluși")}, bleumarin, din piele naturală cu guler moale, cu interior izolat cu lână, care ține de cald. Sunt făcute în parteneriatul Biomecanics Podology, cu podologi.</p>'
  '<p>Aricii cu curea reglabilă permit încălțatul ușor și strâng gheata exact pe picior. Stabilizatorii laterali și contrafortul rigidizat țin piciorul în poziție.</p>'
  '<p>Talpa și vârful:</p>'
  + L(('Vârf', 'rotund, cauciucat, închis.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Branț', 'detașabil.'))
  + '<p>Numerele 18-25 sunt pentru copii de în jur de 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte pentru copii din piele bleumarin 261102'), ('iarnă', 'Ghetele de iarnă Biomecanics 261102'),
   ('piele', 'Partea superioară din piele naturală cu un guler moale'), ('lână', 'Interior izolat cu lână'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership , dezvoltată împreună cu podologi'),
   ('arici', 'Închidere practică cu arici și o curea reglabilă'), ('stabilizatori', 'Stabilizatori laterali și contrafort rigidizat'),
   ('vârf', 'Vârf rotund, cauciucat cu vârf închis'), ('talpă', 'Talpă flexibilă din cauciuc'), ('branț', 'branț detașabil')],
  {'Model': 'Biomecanics 261102', 'Material': 'piele naturală, interior din lână, talpă din cauciuc', 'Caracteristici': 'ghete de iarnă, arici cu curea, branț detașabil', 'Cod produs': '261102'},
  notes=['Sunt ghete de iarnă, listate la Pantofi.'])

w(10467,
  f'<p>{GEOX} RANN-E J56NEA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} albaștri, în stil casual, din imitație de piele și material textil, rezistenți la purtat zilnic. Membrana microporoasă Geox Respira™ scoate umezeala și ține picioarele uscate.</p>'
  '<p>Aricii permit încălțatul și descălțatul rapid, deci copilul se descurcă singur, iar gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Înăuntru și dedesubt:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'căptușit cu material textil.'), ('Branț', 'textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 28-39 sunt pentru copii de la 4 ani în sus, de obicei.</p>',
  [('model', 'Geox RANN-E sneakers pentru copii albaștri J56NEA.09FFU'), ('casual', 'stilul casual'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('zilnic', 'rezistentă la utilizarea zilnică'), ('Respira', 'Tehnologia Geox Respira™ cu membrană microporoasă favorizează eliminarea umezelii, menținând picioarele uscate'),
   ('arici', 'Închidere practică cu arici facilitează încălțarea și descălțarea rapidă'), ('guler', 'Gulerul superior ușor întărit'), ('călcâi', 'Călcâi întărit'),
   ('interior', 'Interior căptușit cu material textil'), ('branț', 'Branț din material textil'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox RANN-E', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, Geox Respira™', 'Cod produs': 'J56NEA.09FFU'})
