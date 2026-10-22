import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
REIMA = A('/brand/reima/', 'Reima')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9440,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261107 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} roz, cu fața din piele naturală și material sintetic, creați împreună cu podologi, în programul Biomecanics Podology Partnership. Talpa din cauciuc e flexibilă, pentru mersul de zi cu zi.</p>'
  '<p>Închiderea cu arici are curea reglabilă, ca pantoful să stea exact pe picior, iar branțul textil se scoate, pentru curățat și pentru verificat lungimea piciorului.</p>'
  '<p>Mai au:</p>'
  + L(('Branț', 'antibacterian și anti-miros.'), ('Vârf', 'rotund, cauciucat, protejează degetele.'), ('Călcâi', 'întărit, cu stabilizatori laterali.'), ('Interior', 'textil.'))
  + '<p>Numerele 19-25 se potrivesc în mare copiilor de 1-3 ani.</p>',
  [('cod', 'Pantofi pentru copii roz 261107'), ('material', 'Față din combinație de piele naturală și material sintetic'), ('podologi', 'dezvoltat în colaborare cu podologi'),
   ('Podology', 'Tehnologia Biomecanics Podology Partnership'), ('talpă', 'Talpă flexibilă din cauciuc'), ('arici', 'Închidere cu arici cu curea reglabilă'),
   ('branț detașabil', 'Branț detașabil din material textil'), ('antibacterian', 'Branț antibacterian și anti-miros'), ('vârf', 'Vârf rotund, cauciucat'),
   ('călcâi', 'Călcâi întărit și stabilizatori laterali'), ('interior', 'Interior din material textil')],
  {'Model': 'Biomecanics 261107', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, branț antibacterian detașabil, vârf cauciucat', 'Cod produs': '261107'})

w(9448,
  f'<p>{GEOX} CIUFCIUF B455QB sunt {A("/categorie/adidasi/", "adidași pentru fete")} bej, cu profil scurt, făcuți dintr-un amestec de piele întoarsă, material textil și sintetic. Au tehnologia GEOX Respira™ cu membrană, care elimină umezeala, și sunt gândiți pentru activitățile de zi cu zi.</p>'
  '<p>Aricii îi lasă pe copii să se încalțe singuri, iar profilul scurt lasă glezna liberă la joacă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Branț', 'din material textil.'), ('Căptușeală', 'textilă.'))
  + '<p>Numerele 20-27 sunt pentru copii de aproximativ 1-4 ani.</p>',
  [('model', 'Geox CIUFCIUF sneakers pentru copii bej B455QB.0FU22'), ('material', 'Partea superioară dintr-un amestec de materiale , inclusiv piele întoarsă și material textil'),
   ('profil', 'Profilul scurt al încălțămintei'), ('Respira', 'Tehnologia GEOX Respira™ cu membrană'), ('zilnic', 'aventurile de zi cu zi'), ('arici', 'Sistemul practic de închidere cu arici'),
   ('talpă', 'Talpa plată din cauciuc'), ('branț', 'Branțul din material textil'), ('căptușeală', 'Interiorul căptușit cu material textil')],
  {'Model': 'Geox CIUFCIUF B455QB', 'Material': 'piele întoarsă, textil și sintetic, talpă din cauciuc', 'Caracteristici': 'GEOX Respira™, arici, profil scurt', 'Cod produs': 'B455QB.0FU22'})

w(9449,
  f'<p>{GEOX} ECLYPER J66LSG sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, cu profil jos, din imitație de piele și textil, cu logo Geox discret. Talpa patentată Geox Respira™ are membrană microporoasă, care elimină umezeala. Se poartă la ținute casual și streetwear.</p>'
  '<p>Aricii se prind repede, iar profilul jos lasă glezna să se miște liber; căptușeala textilă e moale.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Închidere', 'arici.'))
  + '<p>Numerele 28-35 sunt pentru copii de pe la 4 până pe la 11 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii bleumarin J66LSG.054FU'), ('profil', 'Profil jos al părții superioare'), ('material', 'Combinația de imitație de piele și material textil'),
   ('logo', 'Logo subtil al mărcii'), ('Respira', 'Talpă patentată cu membrană microporoasă care elimină umiditatea'), ('casual', 'stilul casual cu cel streetwear'),
   ('arici', 'Închidere practică cu arici'), ('căptușeală', 'Căptușeala din material textil'), ('talpă', 'Talpă plată din cauciuc'), ('călcâi', 'Călcâi întărit')],
  {'Model': 'Geox ECLYPER J66LSG', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'profil jos, arici, Geox Respira™', 'Cod produs': 'J66LSG.054FU'})

w(9453,
  f'<p>{GEOX} GISLI B561MG sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași înalți pentru bebeluși")} violet, cu fața din imitație de piele și textil și tehnologia GEOX Respira™, care elimină umezeala. Sunt pentru zilele active ale copiilor mici.</p>'
  '<p>Profilul înalt ține glezna, iar gulerul ușor întărit se așază fără să irite; scaiul îl lasă pe copil să se încalțe singur și se reglează mai larg sau mai strâns, după cât de plin e piciorul.</p>'
  '<p>Mai au:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Căptușeală', 'textilă.'))
  + '<p>Mărimile 20-27 corespund, de regulă, vârstei de 1-4 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii violet B561MG.0AU54'), ('material', 'Fața superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia GEOX Respira'),
   ('profil', 'Profilul înalt al feței superioare'), ('guler', 'Gulerul ușor întărit în jurul gleznei favorizează ajustarea și previne iritațiile'),
   ('scai', 'Închiderea practică cu scai'), ('talpă', 'Talpa plată din cauciuc'), ('călcâi', 'Călcâiul întărit'), ('căptușeală', 'Căptușeala din material textil')],
  {'Model': 'Geox GISLI B561MG', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, scai, GEOX Respira™', 'Cod produs': 'B561MG.0AU54'})

w(9457,
  f'<p>{A("/brand/levis/", "Levi\'s")} LIGHT WEIGHT WINDBREAKER este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de vânt unisex")}, bleumarin, din nailon, ușoară și fără izolație, pentru zilele de tranziție. Oprește vântul și se poartă la joaca afară, pe vreme schimbătoare.</p>'
  '<p>Croiala e regulară, lungă până la șolduri, iar tivul cu șnur elastic și manșetele elastice o strâng pe corp, după copil. Căptușeala completă o face ușor de îmbrăcat peste haine.</p>'
  '<p>Detaliile:</p>'
  + L(('Glugă', 'integrată, cu guler ridicat.'), ('Buzunare', 'laterale, tip slip-on.'), ('Închidere', 'fermoar.'), ('Material', '100% nailon.'))
  + '<p>Geaca vine în mărimile 92-176, deci pentru copii de cam 2 până la 16 ani.</p>',
  [('model', 'Levi\'s Geacă de tranziție pentru copii LIGHT WEIGHT WINDBREAKER bleumarin 8EP678'), ('neizolat', 'Construcție ușoară fără izolație'), ('vânt', 'protejează eficient împotriva vântului'),
   ('tranziție', 'Izolare: tranzitional'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'), ('tiv', 'Tiv cu șnur elastic și manșete elastice'),
   ('căptușeală', 'Căptușeală completă'), ('glugă', 'Glugă integrată'), ('guler', 'Guler ridicat'), ('buzunare', 'Buzunare laterale tip slip-on'), ('fermoar', 'Închidere cu fermoar'),
   ('material', '100% Nailon')],
  {'Model': "Levi's LIGHT WEIGHT WINDBREAKER", 'Material': '100% nailon', 'Caracteristici': 'windbreaker, fără izolație, glugă, tiv cu șnur elastic', 'Cod produs': '8EP678'})

w(9460,
  f'<p>{GEOX} FOOT-RUN sunt {A("/categorie/adidasi/", "adidași de tip barefoot pentru fete")}, violet, din material textil, cu formă anatomică și cutia degetelor lată. Au sistemul Geox Respira în talpă și profil scurt.</p>'
  '<p>Cutia lată lasă degetele să stea liber, potrivită și pentru un picior mai plin, iar șireturile elastice cu închidere cu cârlig se strâng fără nod.</p>'
  '<p>Mai au:</p>'
  + L(('Talpă', 'exterioară, din cauciuc, absoarbe șocurile.'), ('Partea de sus', 'rigidizată.'), ('Interior', 'textil.'))
  + '<p>Numerele 24-35 sunt pentru copii de aproximativ 2-11 ani.</p>',
  [('model', 'Sneakers pentru copii FOOT-RUN culoarea violet, J65PCA.06K9J'), ('textil', 'confecționat din material textil'), ('barefoot', 'Barefoot - oferă o formă anatomică'),
   ('cutie lată', 'Cutia lată a degetelor'), RESPIRA, ('profil', 'Înălțime: mic de statură'), ('închidere', 'Șireturile elastice și închiderea cu cârlig'),
   ('talpă', 'Talpa exterioară din cauciuc'), ('absorbție', 'Absorbtia socului'), ('rigidizat', 'Partea superioară rigidizată'), ('interior', 'Interiorul textil')],
  {'Model': 'Geox FOOT-RUN', 'Material': 'textil, talpă din cauciuc', 'Caracteristici': 'barefoot, cutie lată a degetelor, Geox Respira, șireturi elastice', 'Cod produs': 'J65PCA.06K9J'})

w(9473,
  f'<p>{REIMA} Vaellus sunt ghete ușoare de trekking, negre, de tip barefoot, listate pe site la {A("/categorie/unisex-incaltaminte-pantofi/", "încălțăminte unisex")}. Construcția barefoot lasă piciorul să se miște liber, iar zona cauciucată din jurul degetelor îl protejează pe teren dificil.</p>'
  '<p>Branțurile detașabile din EVA au imprimat un ghid de mărime, deci verifici direct pe ele dacă mai e loc. Înșiretarea rapidă se reglează repede pe picior.</p>'
  '<p>Pe scurt:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Partea de sus', 'până la gleznă, textil și sintetic.'), ('Interior', 'textil.'))
  + '<p>Numerele 28-38 sunt pentru copii de la 4 ani în sus, în general.</p>',
  [('model', 'Reima Pantofi pentru copii Vaellus negri 5400173A'), ('trekking', 'Ghetele de trekking Reima Barefoot'), ('barefoot', 'Construcția Barefoot'),
   ('degete', 'Zona cauciucată în jurul degetelor'), ('branț', 'Branțurile detașabile și profilate din EVA cu imprimeu pentru verificarea mărimii'),
   ('înșiretare', 'Sistemul de înșiretare rapidă'), ('talpă', 'Talpa flexibilă din cauciuc'), ('gleznă', 'Partea superioară până la gleznă din material textil și sintetic'),
   ('interior', 'Interior:Material textil')],
  {'Model': 'Reima Vaellus', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'barefoot, branț EVA cu ghid de mărime, înșiretare rapidă', 'Cod produs': '5400173A'},
  notes=['Pe site e la Pantofi; produsul e ghetă de trekking.'])

w(9475,
  f'<p>{A("/brand/donsje/", "Donsje")} Ceasie Jacket este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă ușor izolată unisex")}, bleumarin, din material rezistent de poliester, fără glugă, cu izolație sintetică, pentru temperaturile mai scăzute din perioada de tranziție.</p>'
  '<p>Fermoarul pe toată lungimea are clapă interioară și exterioară, care țin vântul afară, iar mânecile se termină cu bandă elastică. Croiala e simplă.</p>'
  '<p>Pe scurt:</p>'
  + L(('Căptușeală', 'are, cu izolație ușoară.'), ('Glugă', 'nu are.'), ('Material', '100% poliester.'))
  + f'<p>Pentru vânt, capul se acoperă cu ceva din {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "căciulile și accesoriile unisex")}. Mărimile 86-140 sunt pentru copii de pe la 1 până pe la 10 ani.</p>',
  [('model', 'Donsje Geacă copii Ceasie Jacket culoarea bleumarin, 4110400'), ('ușor izolat', 'Model usor izolat'), ('rezistent', 'material rezistent'),
   ('izolație', 'izolație sintetică'), ('temperaturi', 'temperaturi mai scăzute'), ('tranziție', 'Izolare: tranzitional'), ('fără glugă', 'Gluga: fara gluga'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea, cu clapă interioară și exterioară'), ('elastic', 'Mâneci finisate cu o coadă elastică'), ('croială', 'Tăiere simplă'),
   ('material', '100% Poliester')],
  {'Model': 'Donsje Ceasie Jacket', 'Material': '100% poliester', 'Caracteristici': 'ușor izolată, fermoar cu dublă clapă, fără glugă', 'Cod produs': '4110400'},
  comp={'slug': '/categorie/unisex-accesorii-caciuli-manusi-accesorii/', 'motiv': 'geacă fără glugă'})

w(9476,
  f'<p>{REIMA} Kulkuri Low sunt pantofi negri cu membrana ReimaTec, care oprește ploaia și vântul, listați pe site la {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")}. Nu au izolație, deci sunt pentru toamnă și primăvară, pe vreme umedă.</p>'
  '<p>Se leagă cu șiret clasic, care se reglează exact pe picior, iar inserțiile detașabile Happy Fit ajută la alegerea mărimii. Bucla de la spate ajută la încălțat.</p>'
  '<p>Pentru seară și pentru teren:</p>'
  + L(('Elemente reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Talpă', 'exterioară, din cauciuc.'), ('Material', 'sintetic și textil.'))
  + '<p>Numerele 28-38 îi fac potriviți pentru copii de la cam 4 ani în sus.</p>',
  [('model', 'Reima Pantofi copii Kulkuri Low culoarea negru, 5400179A'), ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'), ('neizolat', 'Izolare: neizolat'),
   ('nu complet', 'nu garantează impermeabilitatea completă'), ('șiret', 'Șiretul clasic permite ajustarea individuală'), ('Happy Fit', 'Inserțiile detașabile Happy Fit'),
   ('buclă', 'Bucla de la spate'), ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'), ('talpă', 'Talpa exterioară din cauciuc')],
  {'Model': 'Reima Kulkuri Low', 'Material': 'sintetic și textil, talpă din cauciuc', 'Caracteristici': 'ReimaTec, neizolați, Happy Fit, reflectorizante', 'Cod produs': '5400179A'})
print('lot 22 scris')
