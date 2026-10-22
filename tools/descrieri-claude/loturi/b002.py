import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(5386,
  f'<p>Ghetele {A("/brand/ugg/", "UGG")} Classic Ultra Mini sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete scurte unisex")} maro, cu aspect de piele întoarsă (suede-like) și căptușeală moale. Magazinul le recomandă pentru ținute de zi cu zi.</p>'
  '<p>Sunt slip-on, fără șiret sau arici, cu acoperire joasă la gleznă: se trag în picior de bucla de la călcâi. Pentru că nu se pot strânge, numărul trebuie ales exact după lungimea piciorului.</p>'
  '<p>Restul construcției e simplu:</p>'
  + L(('Vârf', 'rotund.'), ('Talpă', 'plată, cu striații.'), ('Material', 'sintetic.'), ('Logo', 'UGG, pe călcâi.'))
  + '<p>Pe site sunt doar numerele 31 și 32.5, pentru copii de cam 6-9 ani.</p>',
  [('model', 'Ghete UGG Classic Ultra Mini maro'), ('slip-on, gleznă', 'design slip-on și acoperire joasă la gleznă'), ('vârf, talpă', 'vârf rotund, talpă plată cu striații'),
   ('suede-like', 'aspect suede-like'), ('logo, pull tab', 'logo UGG pe călcâi și un pull tab pentru încălțare'), ('căptușeală', 'căptușeală moale vizibilă'),
   ('utilizare', 'în ținute de zi cu zi'), ('material', 'Sintetic')],
  {'Model': 'UGG Classic Ultra Mini', 'Material': 'sintetic, cu aspect suede', 'Caracteristici': 'slip-on, căptușeală moale, talpă plată cu striații, pull tab', 'Cod produs': '1130750K-CHE'})

w(5453,
  f'<p>{TH} T3X9-33362 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, înalți peste gleznă, din material sintetic cu accente bleumarin și roșii. Sunt făcuți pentru purtat zilnic, în ținute casual.</p>'
  '<p>Profilul înalt acoperă glezna, iar șireturile strâng pantoful pe picior, așa că stă bine și pe un picior mai subțire. Talpa e groasă, albă, cu striații.</p>'
  '<p>De aproape, modelul are:</p>'
  + L(('Vârf', 'rotund.'), ('Lateral', 'perforații mici și branding mare.'), ('Gleznă', 'căptușeală vizibilă.'), ('Detalii', 'logo și steagul Tommy Hilfiger.'))
  + '<p>Pe site e disponibil doar numărul 40, deci se potrivește copiilor mari, de obicei de la 12 ani în sus.</p>',
  [('model', 'Pantofi sport Tommy Hilfiger logo, model peste gleznă, cu șireturi, albi'), ('cod', 'T3X9-33362'), ('material', 'realizat din material sintetic'),
   ('culori', 'alb cu accente bleumarin și roșu'), ('utilizare', 'Potriviți pentru purtare de zi cu zi, în ținute casual'), ('vârf, talpă', 'vârf rotund, talpă groasă albă'),
   ('striații', 'profil texturat cu striații'), ('perforații', 'perforații mici pe lateral'), ('căptușeală', 'căptușeală vizibilă în zona gleznei'),
   ('logo', 'detalii cu logo și steagul Tommy Hilfiger'), ('branding', 'branding mare pe lateral')],
  {'Model': 'Tommy Hilfiger T3X9-33362', 'Material': 'sintetic', 'Caracteristici': 'peste gleznă, șireturi, talpă groasă, perforații laterale', 'Cod produs': 'T3X9-33362'})

w(5454,
  f'<p>{TH} Flag T3X9-33356 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, cu accente roșii și bleumarin, din material sintetic, tăiați sub gleznă. Sunt gândiți pentru purtare casual, de zi cu zi.</p>'
  '<p>Gura pantofului are padding în zona gleznei, iar călcâiul e întărit, deci piciorul stă fix, iar șireturile clasice permit strângerea exact cât trebuie, inclusiv la un picior îngust.</p>'
  '<p>Pe exterior se văd câteva detalii:</p>'
  + L(('Talpă', 'plată, mată, cu striații.'), ('Lateral', 'perforații discrete și branding.'), ('Vârf', 'rotund.'), ('Material', 'sintetic, cu suprafață netedă.'))
  + '<p>Pe site sunt numerele 35-41, potrivite în general copiilor de la 10 ani în sus.</p>',
  [('model', 'Pantofi sport Tommy Hilfiger Flag Low cut Lace up sneaker albi'), ('cod', 'T3X9-33356'), ('sub gleznă', 'design sub gleznă'), ('utilizare', 'lifestyle și purtare casual'),
   ('culori', 'alb cu accente roșii și bleumarin'), ('închidere, vârf', 'închidere cu șireturi, vârf rotund'), ('padding', 'În zona gleznei se observă padding'),
   ('călcâi', 'un călcâi întărit'), ('talpă', 'Talpa este plată'), ('striații', 'model de striații pe exterior'), ('perforații', 'perforații discrete'),
   ('material', 'Partea superioară este din material sintetic')],
  {'Model': 'Tommy Hilfiger Flag Low cut', 'Material': 'sintetic', 'Caracteristici': 'sub gleznă, șireturi, padding la gleznă, călcâi întărit', 'Cod produs': 'T3X9-33356'})

w(5494,
  f'<p>{TH} Lace Up Bootie sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} albe, din piele ecologică cu finisaj neted, înalte peste gleznă și cu șireturi. Sunt ghete de oraș, pentru ținute lifestyle: magazinul nu declară izolație sau protecție la apă, deci nu sunt ghete de iarnă.</p>'
  '<p>Șiretul se strânge pe toată înălțimea, așa că gheata se potrivește și pe o gleznă mai subțire. Talpa masivă are un toc gros integrat.</p>'
  '<p>Detaliile care se văd:</p>'
  + L(('Talpă', 'groasă, cu profil adânc și striații.'), ('Vârf', 'rotund.'), ('Logo', 'discret, pe limbă și pe lateral.'), ('Material', 'piele ecologică.'))
  + '<p>Pe site sunt numerele 35-39, de regulă pentru copii de la 10 ani în sus.</p>',
  [('model', 'Ghete Tommy Hilfiger Lace UP BootIE albe'), ('închidere, gleznă', 'închidere cu șireturi și acoperire înaltă la gleznă'), ('material', 'piele ecologică, cu finisaj neted'),
   ('utilizare', 'lifestyle și ținute moderne'), ('talpă', 'Talpa este groasă, cu profil pronunțat'), ('toc', 'Talpa masivă include un toc gros integrat'),
   ('striații', 'striații vizibile'), ('vârf', 'vârful este rotund'), ('logo', 'logo-ul este prezent discret pe limbă și pe lateral')],
  {'Model': 'Tommy Hilfiger Lace Up Bootie', 'Material': 'piele ecologică', 'Caracteristici': 'înalte peste gleznă, șireturi, talpă groasă cu toc integrat', 'Cod produs': 'T4A5-33030'})

w(6823,
  f'<p>{A("/brand/reima/", "Reima")} Astelu sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} negri, din material textil, cu profil scurt și talpă flexibilă. Șireturile sunt elastice, deci pantoful se pune și se scoate fără legat, iar copilul se încalță singur.</p>'
  '<p>Vârful e rotund și moale, iar spatele călcâiului e doar ușor rigidizat: pantoful e moale și lasă loc degetelor.</p>'
  '<p>Mai are câteva detalii utile la încălțat:</p>'
  + L(('Buclă la spate', 'de ea se trage când piciorul intră în pantof.'), ('Interior', 'textil.'), ('Talpă', 'din material sintetic, flexibilă.'))
  + '<p>Modelul are o plajă mare de numere, de la 22 la 40, deci se găsește pentru copii de cam 1 an în sus.</p>',
  [('model', 'Sneakers pentru copii Astelu culoarea negru'), ('material', 'Model confecționat material textil'), ('profil', 'Înălțime: mic de statură'), ('talpă flexibilă', 'Talpa flexibilă'),
   ('șireturi', 'Șireturile elastice fac pantofii ușor de pus și de scos'), ('vârf', 'Cutie rotunda si moale'), ('călcâi', 'Spatele calcaiului usor rigidizat'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('interior', 'Interiorul textil'), ('talpă material', 'Talpa: Material sintetic')],
  {'Model': 'Reima Astelu', 'Material': 'material textil, talpă sintetică', 'Caracteristici': 'șireturi elastice, talpă flexibilă, vârf moale, buclă la spate', 'Cod produs': ''})

w(6856,
  f'<p>{A("/brand/reima/", "Reima")} Passo 2.0 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} negre, din imitație de piele și material textil, rezistente la apă, cu căptușeală moale din textil. Merg pe ploaie și prin bălți mici, deși magazinul precizează că nu garantează impermeabilitate completă.</p>'
  '<p>Aricii se prind oricât de strâns e nevoie, la un picior plinuț ca și la unul subțire, iar inserția detașabilă se scoate și se poate pune lângă piciorul copilului, ca să vezi dacă mai e loc.</p>'
  '<p>Pentru drumul de seară și pentru încălțat, ghetele au:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede mai bine pe întuneric.'), ('Buclă la spate', 'ajută la încălțat.'), ('Călcâi', 'contor rigid, care ține piciorul în gheată.'), ('Talpă', 'exterioară, din cauciuc, cu vârf rotund.'))
  + '<p>Pe site sunt numerele 20-28, potrivite cam copiilor de 1-5 ani.</p>',
  [('model', 'Pantofi copii Passo 2.0 culoarea negru, 5400010A'), ('impermeabil', 'material impermeabil'), ('căptușeală', 'căptușeală moale din material textil'),
   ('nu e complet impermeabil', 'nu garantează impermeabilitatea completă'), ('material', 'Material: imitatie de piele'), ('arici', 'Închiderea cu velcro facilitează încălțarea'),
   ('inserție', 'Inserție detașabilă, ușor de curățat'), ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea după lăsarea întunericului'),
   ('buclă', 'Bucla de la spate'), ('călcâi', 'ține piciorul în pantof'), ('talpă', 'Talpa exterioară din cauciuc'), ('vârf', 'Varf rotund')],
  {'Model': 'Reima Passo 2.0', 'Material': 'imitație de piele, material sintetic și textil, talpă din cauciuc', 'Caracteristici': 'rezistente la apă, arici, elemente reflectorizante, inserție detașabilă', 'Cod produs': '5400010A'})

w(8422,
  f'<p>Bocancii {A("/brand/geox/", "Geox")} din acest model sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} negri, din imitație de piele, cu talpă din cauciuc și sistemul Geox Respira în trei straturi. Nu sunt izolați, deci sunt pentru toamnă și primăvară, nu pentru ger.</p>'
  '<p>Se închid cu șiret, fermoar lateral și arici: fermoarul îi deschide larg la încălțat, iar șiretul se reglează pe gleznă.</p>'
  '<p>Construcția e rigidă acolo unde contează:</p>'
  + L(('Vârf', 'rotund, întărit.'), ('Călcâi', 'rigidizat la spate.'), ('Partea de sus', 'rigidizată.'), ('Interior', 'material sintetic și textil.'))
  + '<p>Pe site sunt numerele 26-39, deci bocancii se găsesc pentru copii de la 3 ani în sus, în general.</p>',
  [('model', 'Bocanci copii culoarea negru'), ('material', 'Material: imitatie de piele'), ('talpă', 'talpă din cauciuc'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('neizolat', 'Izolare: neizolat'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('vârf', 'Cutie rotunda, intarita'),
   ('călcâi', 'Spatele calcaiului rigidizat'), ('partea de sus', 'Partea superioară rigidizată'), ('interior', 'Interiorul: Material sintetic, Material textil')],
  {'Model': 'Geox, bocanci', 'Material': 'imitație de piele, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șiret, fermoar lateral și arici, neizolați', 'Cod produs': ''})

w(8437,
  f'<p>{A("/brand/guess/", "GUESS")} L6RL05 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, neagră, din material neted de poliamidă, fără glugă. Nu are izolație, deci e pentru primăvară și toamnă.</p>'
  '<p>Fermoarul e dublat de capse, iar buzunarele sunt oblice. Pentru că nu are glugă, pe vânt capul se acoperă separat, cu o piesă din {A("/categorie/baieti-accesorii-caciuli-manusi-accesorii/", "căciulile și accesoriile pentru băieți")}.</p>'
  '<p>Geaca e simplă, cu puține elemente:</p>'
  + L(('Închidere', 'fermoar și capse.'), ('Buzunare', 'oblice.'), ('Glugă', 'nu are.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile de pe site încep la 122-125 și urcă până la 175, potrivite în mare copiilor de 7-16 ani.</p>',
  [('cod', 'L6RL05 W4210'), ('culoare', 'culoarea negru'), ('material neted', 'material neted'), ('poliamidă', 'Materialul de baza: 100% Poliamida'),
   ('fără glugă', 'Gluga: fara gluga'), ('tranziție', 'Izolare: tranzitional'), ('închidere', 'Fixare cu fermoar si snap'), ('buzunare', 'Buzunare oblice')],
  {'Model': 'GUESS L6RL05', 'Material': '100% poliamidă', 'Caracteristici': 'de tranziție, fermoar și capse, buzunare oblice, fără glugă', 'Cod produs': 'L6RL05.W4210'},
  comp={'slug': '/categorie/baieti-accesorii-caciuli-manusi-accesorii/', 'motiv': 'geacă fără glugă'})

w(8443,
  f'<p>{A("/brand/wheat/", "Wheat")} 7664-927R este o {A("/categorie/geci-jachete/", "geacă pentru fete")} roșie, ușor izolată, cu izolație sintetică și impermeabilitate declarată de 8000 mm. E pentru toamnă și zilele mai reci, inclusiv pe ploaie măruntă, cu precizarea magazinului că nu garantează impermeabilitate completă.</p>'
  '<p>Croiala e simplă, iar gulerul ridicat acoperă gâtul. Se încheie cu nasturi, nu cu fermoar, ceea ce la copiii mici cere puțin ajutor la îmbrăcat. Fără glugă, capul se acoperă cu o piesă din {A("/categorie/caciuli-manusi-accesorii/", "căciulile și mănușile pentru fete")}.</p>'
  '<p>Ce declară magazinul despre material:</p>'
  + L(('Impermeabilitate', '8000 mm/m2/24h.'), ('Respirabilitate', '5000 g/m2/24h.'), ('Material', '100% poliester.'), ('Glugă', 'nu are.'))
  + '<p>Pe site sunt mărimile 92-152, pentru copii de aproximativ 2-12 ani.</p>',
  [('cod', '7664-927R GRS'), ('culoare', 'culoarea roșu'), ('ușor izolat', 'Model ușor izolat'), ('izolație sintetică', 'izolație sintetică'),
   ('temperaturi', 'temperaturi mai scăzute'), ('impermeabilitate', 'Impermeabilitate: 8000 mm/m2/24h'), ('respirabilitate', 'Respirabilitate: 5000 g/m2/24h'),
   ('nu e complet impermeabil', 'nu garantează impermeabilitatea completă'), ('croială', 'Tăiere simplă'), ('nasturi', 'Incheiere cu nasturi'),
   ('guler', 'Gulerul ridicat'), ('fără glugă', 'Gluga: fara gluga'), ('material', '100% Poliester')],
  {'Model': 'Wheat 7664-927R', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'ușor izolată, impermeabilitate 8000 mm, respirabilitate 5000 g, nasturi, guler ridicat', 'Cod produs': '7664-927R'},
  comp={'slug': '/categorie/caciuli-manusi-accesorii/', 'motiv': 'geacă fără glugă'})
print('lot 2 scris')
