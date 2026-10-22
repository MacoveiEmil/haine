import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(12737,
  f'<p>Și în verde, {REIMA} Vaellus sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} de trekking tip Barefoot, adică lasă piciorul să lucreze natural și întăresc mușchii la fiecare pas. Partea de sus, din textil și material sintetic, urcă până la gleznă.</p>'
  '<p>Talpa flexibilă din cauciuc ține bine pe multe suprafețe, iar zona cauciucată din jurul degetelor rezistă pe teren mai greu. Înșiretarea rapidă se strânge dintr-o mișcare.</p>'
  '<p>Branțul și interiorul:</p>'
  + L(('Branțuri EVA', 'profilate, detașabile, cu imprimeu de verificat mărimea.'), ('Interior', 'material textil.'), ('Branț moale', 'reduce sarcina pe articulații la mers.'))
  + '<p>Mărimile 28-38 se potrivesc copiilor de la aproximativ 4 ani în sus.</p>',
  [('model', 'Reima Pantofi pentru copii Vaellus verde 5400173A'), ('trekking', 'Ghetele de trekking Reima pentru copii Barefoot'),
   ('Barefoot', 'Construcția Barefoot favorizează dezvoltarea naturală a piciorului, permițând mișcarea liberă și întărirea mușchilor'),
   ('gleznă', 'Partea superioară până la gleznă, din material textil și sintetic'), ('talpă', 'Talpa flexibilă din cauciuc permite mișcarea liberă a piciorului și o bună aderență pe multiple suprafețe'),
   ('degete', 'Zona cauciucată din jurul degetelor ajută la protejarea împotriva abraziunilor și deteriorărilor pe teren mai dificil'),
   ('înșiretare', 'Sistemul de înșiretare rapidă'), ('branț', 'Branțurile EVA profilate și detașabile cu imprimeu pentru verificarea mărimii'), ('interior', 'Material textil'), ('amortizare', 'Branțul cu amortizare sporește confortul în timpul mersului, reducând sarcina asupra articulațiilor')],
  {'Model': 'Reima Vaellus', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Barefoot, înșiretare rapidă, branț EVA detașabil', 'Cod produs': '5400173A'},
  notes=['Magazinul îi numește „ghete de trekking”, pe site sunt la Pantofi; profil până la gleznă.'])

w(12738,
  f'<p>{REIMA} Hiivin verzi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} vegani, fără PVC, din material textil și piele ecologică, ușori, pentru purtarea zilnică. Membrana din partea de sus apără de umezeală și lasă aerul să circule, deși impermeabilitatea completă nu e garantată.</p>'
  '<p>Velcro-ul și bucla de la spate fac încălțatul ușor, iar elementele reflectorizante îl arată pe copil seara.</p>'
  '<p>Câteva detalii de construcție:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Călcâi', 'contrafort rigid.'), ('Talpă', 'spumă EVA ușoară și cauciuc.'), ('Inserții Happy Fit', 'detașabile, pentru mărime.'))
  + '<p>Numerele 24-36 se poartă de pe la 2 ani în sus.</p>',
  [('model', 'Reima Sneakers pentru copii Hiivin culoarea verde, 5400145A'), ('vegan', 'Potrivit pentru vegani'), ('PVC', 'Acest produs nu conține PVC'),
   ('material', 'combinatia materialului textil cu pielea ecologica'), ('ușor', 'Model ușor și confortabil'), ('membrană', 'Membrana conținută în partea superioară'),
   ('apă', 'nu garantează impermeabilitatea completă'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid'), ('EVA', 'Talpa exterioară este realizată din spumă EVA ușoară'),
   ('cauciuc', 'Talpa exterioară din cauciuc este durabilă'), ('Happy Fit', 'Inserțiile detașabile Happy Fit vă permit să alegeți dimensiunea potrivită')],
  {'Model': 'Reima Hiivin', 'Material': 'textil și piele ecologică, interior textil, talpă EVA și cauciuc', 'Caracteristici': 'membrană, velcro, reflectorizante, vegan, fără PVC', 'Cod produs': '5400145A'},
  notes=['Magazinul dă „Înălțime: jos”, dar și o parte superioară ridicată care rigidizează glezna; n-am precizat profilul.'])

w(12740,
  f'<p>Geaca {A("/brand/mini-rodini/", "Mini Rodini")} Ritzratz neagră este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} izolată, matlasată, oversize, din poliester reciclat, tratată cu BIONIC-FINISH ECO, fără PFC, pentru rezistență la apă. Gulerul ridicat și gluga detașabilă apără de frig.</p>'
  '<p>Fermoarul merge pe toată lungimea și are clapă prinsă cu capse, iar umerii coborâți nu încurcă mișcarea.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Margini', 'mâneci și tiv elastice.'), ('Buzunare', 'două, laterale.'), ('Material', '100% poliester reciclat.'))
  + '<p>Mărimile 80-86 până la 140-146 acoperă copii de aproximativ 1-11 ani. Rezistă la apă, fără garanția impermeabilității complete.</p>',
  [('model', 'Mini Rodini Geacă copii Ritzratz culoarea negru, 25710104'), ('izolat', 'Model izolat confecționat din material matlasat'), ('oversize', 'Fit: oversize'),
   ('reciclat', 'Acest produs este fabricat din poliester reciclat'), ('BIONIC', 'BIONIC-FINISH® ECO - o alternativa ecologica la acoperirea traditionala, hidrofoba DWR'),
   ('PFC', 'Modelul cu acoperire ecologica PFC Repellent cu apa libera'), ('glugă', 'Gulerul ridicat și gluga detașabilă'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă de furtună prinsă cu capse'), ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor nu limitează mobilitatea'),
   ('margini', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('buzunare', 'Două buzunare laterale'), ('material', '100% Poliester reciclat'),
   ('apă', 'nu garantează impermeabilitatea completă')],
  {'Model': 'Mini Rodini Ritzratz', 'Material': '100% poliester reciclat, izolată', 'Caracteristici': 'BIONIC-FINISH ECO, glugă detașabilă, clapă cu capse', 'Cod produs': '25710104'})

w(12741,
  f'<p>{GEOX} ECLYPER J45LRA sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, ușori, cu croială până la gleznă, din material textil și sintetic ușor de întreținut, pentru primăvară, vară și toamnă. Tehnologia Geox Respira ține piciorul uscat.</p>'
  '<p>Velcro-ul face încălțatul și descălțatul rapid, iar gulerul ușor rigidizat nu încurcă mișcarea gleznei. Culoarea roz merge cu multe ținute casual și sport.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textil moale.'), ('Contrafort', 'ușor rigidizat.'), ('Talpă', 'din cauciuc, ține bine pe diverse suprafețe.'))
  + '<p>Numerele 28-35 sunt pentru fete de cam 4-11 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii roz J45LRA.0QDBC'), ('ușor', 'o încălțăminte ușoară și confortabilă'), ('gleznă', 'Croiala până la gleznă'),
   ('material', 'Partea superioară din material textil și sintetic este ușoară și ușor de întreținut'), ('sezon', 'primăvară, vară și toamnă'),
   ('Respira', 'Tehnologia Geox Respira favorizează termoreglarea naturală a piciorului, menținându-l uscat'), ('velcro', 'Închiderea practică cu velcro'),
   ('guler', 'Gulerul pantofului ușor rigidizat adaugă confort și nu restricționează mișcarea'), ('căptușeală', 'Căptușeala moale din material textil'),
   ('contrafort', 'Contrafortul ușor rigidizat'), ('talpă', 'Talpa din cauciuc se caracterizează printr-o bună aderență pe diverse suprafețe'), ('ținute', 'se va potrivi perfect în ținutele casual și sportive')],
  {'Model': 'Geox ECLYPER', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, velcro, croială până la gleznă', 'Cod produs': 'J45LRA.0QDBC'})

w(12744,
  f'<p>{REIMA} Sankari violeți sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} de trekking tip barefoot, neizolați, cu membrană impermeabilă ReimaTec, pentru vreme schimbătoare și ieșiri în natură. Construcția barefoot lasă degetele să se miște liber.</p>'
  '<p>Talpa flexibilă din cauciuc ține bine pe diferite suprafețe, iar călcâiul întărit sprijină piciorul. Detaliile reflectorizante îl fac pe copil vizibil seara.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Branțuri Happy Fit', 'detașabile, pentru verificarea mărimii.'), ('Interior', 'textil și sintetic.'), ('Partea de sus', 'sintetic și textil.'))
  + '<p>Numerele 32-40 se potrivesc copiilor de la aproximativ 8 ani în sus.</p>',
  [('model', 'Reima Pantofi pentru copii Sankari violeți 5400160B'), ('trekking', 'Pantofii de trekking pentru copii Reima Sankari sunt încălțăminte de tip barefoot'),
   ('neizolat', 'Izolare: neizolat'), ('ReimaTec', 'Tehnologia ReimaTec asigură protecție împotriva umidității'), ('membrană', 'Membrana impermeabilă este eficientă în condiții meteorologice variabile'),
   ('barefoot', 'Construcția de tip barefoot permite poziționarea naturală a picioarelor și libertatea de mișcare a degetelor'),
   ('talpă', 'Talpă flexibilă din cauciuc'), ('călcâi', 'Călcâiul întărit'), ('reflectorizant', 'Detalii reflectorizante sporesc vizibilitatea copilului'),
   ('Happy Fit', 'Branțuri detașabile Happy Fit facilitează ajustarea mărimii'), ('interior', 'Material textil, Material sintetic'), ('material', 'Material sintetic, Material textil')],
  {'Model': 'Reima Sankari', 'Material': 'sintetic și textil, interior textil și sintetic, talpă din cauciuc', 'Caracteristici': 'barefoot, ReimaTec, membrană impermeabilă, Happy Fit', 'Cod produs': '5400160B'})

w(12745,
  f'<p>A treia culoare a jachetei {REIMA} Vantti e violetul: o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} subțire de softshell, care taie vântul și ține ploaia la 10 000 mm H2O, cu imprimeu vegetal peste tot. Nu are vată, așa că primăvara și toamna se poartă peste un strat mai gros.</p>'
  '<p>Picăturile alunecă pe suprafața impregnată, iar murdăria nu se prinde ușor. Polarul din interior acoperă doar o parte.</p>'
  '<p>Detaliile utile:</p>'
  + L(('Glugă', 'se detașează.'), ('Buzunar', 'pe piept, cu închidere.'), ('Manșete', 'cu nervuri.'), ('Reflectorizante', 'pentru seară.'))
  + '<p>Mărimile 86-140 merg cam la 1-10 ani.</p>',
  [('model', 'Reima Jachetă pentru copii Vantti violet 5100009D'), ('softshell', 'Material rezistent la vânt softshell'), ('H2O', 'Impermeabilitate 10 000 mm H2O'),
   ('imprimeu', 'Imprimeu vegetal pe toată suprafața'), ('izolație', 'Fără izolație termică'), ('straturi', 'permite o stratificare ușoară'),
   ('impregnare', 'Impregnare hidrofobă a suprafeței materialului'), ('murdărie', 'Rezistență la murdărie'), ('polar', 'Căptușeală parțială din polar'),
   ('glugă', 'Glugă detașabilă'), ('buzunar', 'Buzunar pe piept , cu închidere'), ('manșete', 'Manșete cu nervuri'), ('reflectorizant', 'Elemente reflectorizante')],
  {'Model': 'Reima Vantti', 'Material': '92% poliester, 8% elastan, căptușeală parțială din polar', 'Caracteristici': 'softshell, 10000 mm H2O, glugă detașabilă', 'Cod produs': '5100009D'})

w(12746,
  f'<p>Modelul {TH} T1X9-35226, în numerele 30-34, e pentru copiii de școală: {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} bleumarin, uni, cu exterior sintetic care se curăță repede. Profilul scurt lasă glezna liberă la joacă.</p>'
  '<p>Talpa plată ține piciorul în poziție naturală, iar aricii fac încălțatul rapid, comod și pentru copii, și pentru părinți. Modelul uni are un aspect clasic, ușor de purtat cu multe haine.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Călcâi', 'întărit.'), ('Căptușeală', 'textilă, aerisită.'), ('Branțuri', 'textile, detașabile.'))
  + '<p>Se potrivesc copiilor de în jur de 6-11 ani.</p>',
  [('model', 'Tommy Hilfiger Sneakers pentru copii bleumarin T1X9-35226'), ('uni', 'Modelul uni al părții superioare'), ('sintetic', 'Material sintetic pe partea superioară facilitează menținerea curățeniei'),
   ('profil', 'Profilul scurt al părții superioare permite libertatea de mișcare a gleznei'), ('talpă', 'Talpa plată favorizează poziția naturală a piciorului'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea rapidă, ceea ce este comod pentru copii și părinți'), ('călcâi', 'Călcâi întărit'),
   ('căptușeală', 'Căptușeală textilă în interiorul pantofului favorizează ventilația'), ('branț', 'Branțurile detașabile din material textil'), ('clasic', 'oferă încălțămintei un aspect clasic, potrivindu-se multor ținute')],
  {'Model': 'Tommy Hilfiger T1X9-35226', 'Material': 'sintetic, interior textil', 'Caracteristici': 'arici, profil scurt, branț detașabil', 'Cod produs': 'T1X9-35226'})

w(12747,
  f'<p>{GEOX} ECLYPER J66LRG sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, din imitație de piele și material textil, în stil casual. Tehnologia patentată GEOX Respira scoate umezeala din pantof, iar gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Aricii fac încălțatul și descălțatul rapid, iar călcâiul întărit dă pași mai siguri la joacă. Căptușeala textilă lasă aerul să circule în jurul piciorului.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Interior', 'căptușit cu textil și sintetic.'), ('Talpă', 'plată, din cauciuc, rezistentă la abraziune.'), ('Închidere', 'arici.'))
  + '<p>Numerele 32-35 sunt pentru fete de aproximativ 8-11 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi J66LRG.0BCKC'), ('material', 'Partea superioară din imitație de piele și material textil'), ('casual', 'Stilul lor casual'),
   ('Respira', 'Tehnologia patentată GEOX Respira™ favorizează termoreglarea naturală, eliminând umezeala'), ('guler', 'Gulerul ușor întărit al părții superioare îmbracă delicat glezna'),
   ('arici', 'Închiderea practică cu arici'), ('călcâi', 'Călcâiul întărit stabilizează piciorul, ceea ce permite pași mai siguri'),
   ('interior', 'Material textil, Material sintetic'), ('aer', 'Interiorul căptușit cu material textil favorizează circulația aerului'), ('talpă', 'Talpa plată din cauciuc oferă o bună aderență la sol și este rezistentă la abraziune')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele și textil, interior textil și sintetic, talpă din cauciuc', 'Caracteristici': 'Geox Respira, arici', 'Cod produs': 'J66LRG.0BCKC'})

w(12748,
  f'<p>{GEOX} ECLYPER J36LRA albi sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil scurt, care lasă glezna să se miște liber, din imitație de piele și material textil. Membrana microporoasă GEOX Respira scoate umezeala spre exterior.</p>'
  '<p>Prinderea cu arici face încălțatul rapid, iar talpa plată din cauciuc ține bine pe sol. Modelul alb se poartă ușor cu multe ținute, iar construcția e gândită pentru joaca de fiecare zi.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Căptușeală', 'textilă, aerisită.'), ('Branț', 'material textil.'), ('Partea de sus', 'imitație de piele și textil.'))
  + '<p>Mărimile 28-35 se potrivesc fetelor de cam 4-11 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi J36LRA.0BCKC'), ('profil', 'Profilul scurt al părții superioare favorizează libertatea de mișcare a gleznei'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia GEOX Respira™ cu membrană microporoasă'),
   ('arici', 'Prinderea practică cu arici facilitează încălțarea și descălțarea rapidă'), ('talpă', 'Talpa plată din cauciuc favorizează stabilitatea și aderența'),
   ('căptușeală', 'Interiorul căptușit cu material textil sprijină circulația aerului'), ('branț', 'Branțul din material textil')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici, profil scurt', 'Cod produs': 'J36LRA.0BCKC'})

w(12753,
  f'<p>{GEOX} WASHIBA J65LQA albi sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} cu profil jos, din material sintetic, ușori și confortabili pentru purtarea zilnică. Vârful e rotund, iar interiorul e confortabil.</p>'
  '<p>Talpa exterioară din cauciuc are caneluri, deci e durabilă și ține bine pe sol, iar talpa Geox Respira are trei straturi cu perforări pentru aerisire.</p>'
  '<p>Din ce e făcută încălțămintea:</p>'
  + L(('Partea de sus', 'material sintetic.'), ('Interior', 'material textil.'), ('Talpă exterioară', 'cauciuc cu caneluri.'))
  + '<p>Numerele 28-35 sunt pentru băieți de în jur de 4-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii WASHIBA culoarea alb, J65LQA.054FU'), ('profil', 'Înălțime: mic de statură'), ('sintetic', 'confecționat din material sintetic'),
   ('ușor', 'Model ușor și confortabil'), ('vârf', 'Varf rotund'), ('interior', 'Interior confortabil'),
   ('talpă', 'Talpa exterioară din cauciuc cu caneluri este durabilă și oferă o tracțiune bună'), RESPIRA, ('textil', 'Material textil')],
  {'Model': 'Geox WASHIBA', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, talpă cu caneluri', 'Cod produs': 'J65LQA.054FU'})
