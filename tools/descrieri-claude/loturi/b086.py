import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')
TALPA = ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')
AMPHIBIOX = ('Amphibiox', 'Tehnologia Amphibiox®. Membrana special respirabila si nepermeabila protejeaza atat talpa exterioara, cat si cea superioara')

w(13105,
  f'<p>Geaca {A("/brand/columbia/", "Columbia")} Powder Lite albastră este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} matlasată, ușoară, cu izolație sintetică medie, pentru sezonul de tranziție. Căptușeala Omni-Heat Thermal Reflective, cu imprimeu metalic, păstrează căldura, iar Omni-Shield ține umezeala și murdăria afară.</p>'
  '<p>Gluga fixă are șnur și apără de vânt și de ploaia ușoară, iar fermoarul merge pe toată lungimea. Croiala regulară lasă loc de mișcare la joacă.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Buzunare', 'laterale, slip-on.'), ('Manșete', 'cu bordură elastică.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-164 sunt pentru copii de aproximativ 4-14 ani.</p>',
  [('model', 'Columbia Geacă petrecută pentru copii Powder Lite albastră 2090023'), ('matlasat', 'Țesătură exterioară matlasată'), ('ușor', 'o propunere ușoară pentru copii'),
   ('izolație', 'Izolație sintetică medie'), ('tranziție', 'sezonul de tranziție'), ('Omni-Heat', 'Omni-Heat™ Thermal Reflective – imprimeul metalic pe căptușeală ajută la reținerea căldurii'),
   ('Omni-Shield', 'Tehnologia Omni-Shield™ – învelișul hidrofob îngreunează pătrunderea umidității și a murdăriei'), ('glugă', 'Glugă fixă cu șnur – oferă protecție pentru cap împotriva vântului și a ploii ușoare'), ('croială', 'Croială regulară – asigură libertatea de mișcare'),
   ('fermoar', 'Fermoar cu un singur sens pe toată lungimea'), ('buzunare', 'Buzunare laterale tip slip-on'), ('manșete', 'Manșete cu bordură elastică'), ('material', '100% Poliester')],
  {'Model': 'Columbia Powder Lite', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'Omni-Heat, Omni-Shield, glugă fixă cu șnur', 'Cod produs': '2090023'})

w(13107,
  f'<p>{GEOX} IUPIDOO B3555D bej sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} înalți, din piele întoarsă, imitație de piele și material textil, cu interior din piele naturală. Branțul detașabil are imprimeu pentru verificarea mărimii, iar sistemul Flexy din talpă urmează îndoirea piciorului.</p>'
  '<p>Aricii fac încălțatul rapid, iar gulerul întărit cuprinde glezna. Talpa moale reduce șocurile la mers și la alergat.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Geox Respira', 'scoate umiditatea spre exterior.'), ('Călcâi', 'întărit.'), ('Talpă', 'din cauciuc, cu profil plat.'))
  + '<p>Numerele 18-26 se potrivesc băieților de cam 1-4 ani.</p>',
  [('model', 'Geox IUPIDOO sneakers pentru copii bej B3555D.05422'), ('înalt', 'sneakerși înalți pentru copii'), ('material', 'Partea superioară din piele întoarsă, imitație de piele și material textil'),
   ('interior', 'Interior căptușit cu piele naturală'), ('branț', 'Branț detașabil cu imprimeu, permite verificarea ușoară a mărimii'),
   ('Flexy', 'Sistemul Flexy în talpă susține flexarea naturală a piciorului'), ('arici', 'Închidere cu arici'), ('guler', 'Gulerul superior întărit îmbracă delicat glezna'),
   ('șocuri', 'favorizează reducerea șocurilor în timpul mersului și al alergării'), ('Respira', 'Tehnologia Geox Respira™ favorizează termoreglarea naturală a piciorului, eliminând umiditatea la exterior'),
   ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpa de cauciuc cu profil plat')],
  {'Model': 'Geox IUPIDOO', 'Material': 'piele întoarsă, imitație de piele și textil, interior din piele', 'Caracteristici': 'Geox Respira, sistem Flexy, arici, branț cu verificare de mărime', 'Cod produs': 'B3555D.05422'})

w(13109,
  f'<p>{GEOX} GISLI B561MG violet sunt {A("/categorie/adidasi/", "adidași pentru fete")} înalți, din material textil și sintetic, ușori și ușor de întreținut. Membrana microporoasă GEOX Respira scoate umezeala și ține pantoful uscat pe dinăuntru.</p>'
  '<p>Aricii o lasă pe fetiță să se încalțe singură, iar profilul înalt, cu guler ușor rigidizat, susține glezna. Talpa plată din cauciuc ține bine pe sol și dă pași siguri.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textilă.'), ('Branț', 'textil, moale.'), ('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'))
  + '<p>Numerele 24-27 se potrivesc fetițelor de în jur de 2-4 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii violet B561MG.0AU54'), ('înalt', 'Profil înalt al părții superioare cu guler ușor rigidizat, care susține glezna'),
   ('material', 'Partea superioară din material textil și sintetic , care asigură lejeritatea încălțămintei și ușurința în întreținere'),
   ('Respira', 'Tehnologia GEOX Respira™ cu membrană microporoasă, care elimină umezeala'), ('arici', 'Închidere practică cu arici , care facilitează încălțarea și descălțarea rapidă de către copil'),
   ('căptușeală', 'Interior căptușit cu material textil'), ('branț', 'Branț din material textil'), ('talpă', 'Talpă plată din cauciuc , care asigură o bună aderență la sol, permițând pași stabili'), ('călcâi', 'Călcâi întărit')],
  {'Model': 'Geox GISLI', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici, profil înalt', 'Cod produs': 'B561MG.0AU54'})

w(13110,
  f'<p>{GEOX} PERTH J367RF.054FU bleumarin, în numerele 36-41, sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} înalți, în stil casual, din imitație de piele și material textil. Membrana GEOX Respira scoate umezeala, iar gulerul ușor întărit susține glezna.</p>'
  '<p>Șireturile elastice se reglează pe picior, iar aricii fac încălțatul și descălțatul ușor. Talpa din cauciuc ține bine pe sol, iar căptușeala lasă aerul să circule.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Căptușeală', 'textil și sintetic, aerisită.'), ('Călcâi', 'întărit.'), ('Talpă', 'din cauciuc.'))
  + '<p>Se potrivesc băieților de la aproximativ 12 ani în sus.</p>',
  [('model', 'Geox PERTH sneakers pentru copii bleumarin J367RF.054FU'), ('înalt', 'sneakerși înalți pentru copii'), ('casual', 'Acest model în stil casual'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia GEOX Respira™ contribuie la menținerea picioarelor uscate, grație membranei care elimină umezeala'),
   ('guler', 'Profilul înalt al părții superioare împreună cu gulerul ușor întărit susține glezna'), ('șireturi', 'Șireturi elastice facilitează ajustarea pe picior'),
   ('arici', 'Închiderea practică cu arici'), ('căptușeală', 'Interiorul căptușit cu material textil favorizează circulația aerului'), ('interior', 'Material textil, Material sintetic'),
   ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa din cauciuc asigură o bună aderență la sol')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil și sintetic, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice și arici', 'Cod produs': 'J367RF.054FU'})

w(13111,
  f'<p>Același cod {GEOX} PERTH J367RF.054FU, bleumarin, în mărimile 28-35: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} pentru joacă afară și ținute de oraș. Membrana microporoasă din talpă nu lasă apa să intre și scoate umezeala.</p>'
  '<p>Arici pentru încălțat rapid, șireturi elastice care se mulează pe picior și un guler ușor întărit în jurul gleznei.</p>'
  '<p>Construcția, pe rând:</p>'
  + L(('Exterior', 'imitație de piele și textil, se întreține ușor.'), ('Interior', 'textil și sintetic.'), ('Talpă', 'cauciuc plat.'), ('Călcâi', 'întărit.'))
  + '<p>Mărimile se potrivesc băieților de pe la 4 până pe la 11 ani.</p>',
  [('model', 'Geox PERTH sneakers pentru copii bleumarin J367RF.054FU'), ('joacă', 'jocurilor în aer liber și în ținutele urbane'),
   ('membrană', 'Talpă respirabilă cu membrană microporoasă protejează interiorul pantofului de apă'), ('Respira', 'Tehnologia GEOX Respira™ susține termoreglarea naturală a piciorului, eliminând umezeala spre exterior'),
   ('arici', 'Prindere practică cu arici'), ('șireturi', 'Șireturi elastice facilitează încălțarea, adaptându-se formei piciorului'), ('guler', 'Gulerul superior ușor întărit'),
   ('material', 'Partea superioară din imitație de piele și material textil constituie o construcție durabilă, ușor de întreținut'), ('interior', 'Interior căptușit cu material textil și sintetic'),
   ('talpă', 'Talpă plată din cauciuc'), ('călcâi', 'Călcâi întărit')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele și textil, interior textil și sintetic, talpă din cauciuc', 'Caracteristici': 'Geox Respira cu membrană, arici și șireturi elastice', 'Cod produs': 'J367RF.054FU'})

w(13112,
  f'<p>{GEOX} FLEXYPER B656GC sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} în culoarea albastru, pentru cei mai mici, cu profil jos, din piele întoarsă, piele naturală și material textil. Velcro-ul face încălțatul și descălțatul rapid.</p>'
  '<p>Branțul din piele previne frecarea și mirosul, iar finisajul antibacterian din interior oprește înmulțirea bacteriilor și formarea mirosurilor. Talpa din cauciuc rezistă bine la purtare.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Geox Respira', 'trei straturi, cu perforări.'), ('Interior', 'textil și piele naturală.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 20-23 sunt pentru băieți de aproximativ 1-3 ani.</p>',
  [('model', 'Geox Sneakers pentru copii FLEXYPER B656GC.01422'), ('culoare', 'Culoare albastru'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinație de piele întoarsă, piele naturală și material textil'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea, abraziunile si aparitia unui miros neplacut'),
   ('antibacterian', 'Finisajul antibacterian din interiorul încălțămintei reduce creșterea bacteriilor nedorite'), RESPIRA,
   ('interior', 'Material textil, Piele naturala'), TALPA],
  {'Model': 'Geox FLEXYPER', 'Material': 'piele întoarsă, piele naturală și textil, interior textil și piele', 'Caracteristici': 'velcro, finisaj antibacterian, Geox Respira', 'Cod produs': 'B656GC.01422'})

w(13113,
  f'<p>Și în maro, {GEOX} FLEXYPER J56LCA vin în numerele 36-39: {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} joși, din textil și piele ecologică, cu Amphibiox, membrana care oprește apa în talpă și în partea de sus fără să sufoce piciorul. Pentru căptușeală, Geox dă un indice de izolare medie.</p>'
  '<p>Încălțatul e simplu, cu șireturi elastice și urechi de tras la călcâi. Fața rigidizată nu se deformează.</p>'
  '<p>Detalii utile:</p>'
  + L(('Căptușeală', 'textilă, moale.'), ('Vârf', 'rotunjit.'), ('Decor', 'detalii decorative.'))
  + '<p>Se potrivesc băieților de pe la 12 ani în sus.</p>',
  [('model', 'Geox FLEXYPER maro J56LCA.0MEFU'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinatia materialului textil cu pielea ecologica'), AMPHIBIOX,
   ('izolare', 'Indicele de izolare termică'), ('mediu', 'MEDIU'), ('închidere', 'Șireturile elastice și urechile de tragere la călcâi îl fac ușor de pus și scos'),
   ('rigid', 'Partea superioară rigidizată'), ('căptușeală', 'Căptușeala moale din material textil'), ('vârf', 'Varf rotund'), ('decor', 'Detalii decorative')],
  {'Model': 'Geox FLEXYPER', 'Material': 'textil și piele ecologică, căptușeală textilă', 'Caracteristici': 'Amphibiox, izolare medie, șireturi elastice', 'Cod produs': 'J56LCA.0MEFU'})

w(13116,
  f'<p>Ghetele de iarnă {A("/brand/biomecanics/", "Biomecanics")} 261152 bleumarin sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} înalte, din piele naturală și material sintetic, cu interior și branț din lână, pentru zilele de iarnă. Membrana BioTEX ține umezeala afară și scoate transpirația.</p>'
  '<p>Vârful lat, tip barefoot, lasă degetele libere, iar carâmbul înalt și călcâiul moale țin piciorul stabil. Talpa elastică permite mișcarea naturală a piciorului.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Talpă', 'cauciuc elastic, cu profil plat.'), ('Căptușeală', 'lână.'), ('Podology Partnership', 'colaborare cu podologi.'))
  + '<p>Numerele 19-23 se potrivesc copiilor de cam 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte de iarnă pentru copii bleumarin 261152'), ('înalt', 'Profilul înalt al carâmbului'), ('material', 'Piele naturală, Material sintetic'),
   ('lână', 'Interior căptușit cu lână și un branț din lână protejează împotriva frigului'), ('BioTEX', 'Membrana BioTEX blochează umezeala din exterior, în același timp eliminând transpirația'),
   ('vârf', 'Vârful lat tip barefoot oferă degetelor libertate'), ('călcâi', 'împreună cu un călcâi moale'), ('talpă', 'Talpă din cauciuc elastic , cu profil plat, permite mișcarea naturală a piciorului'),
   ('Podology', 'Colaborarea cu podologi în cadrul tehnologiei Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261152', 'Material': 'piele naturală și sintetic, căptușeală din lână', 'Caracteristici': 'BioTEX, vârf barefoot, branț din lână', 'Cod produs': '261152'})

w(13121,
  f'<p>Încălțămintea de trekking {A("/brand/primigi/", "Primigi")} 23918, în gri și în numerele 26-30, e una dintre {A("/categorie/baieti-incaltaminte-ghete-cizme/", "ghete pentru băieți")} bune pentru drumeții și joacă pe teren greu. GORE-TEX ține umiditatea afară, iar Shock Absorber protejează articulațiile.</p>'
  '<p>Înșiretarea rapidă se strânge ușor, iar călcâiul întărit dă siguranță. Talpa cu bandă de rulare se prinde de diverse suprafețe.</p>'
  '<p>Materialele și construcția:</p>'
  + L(('Exterior', 'piele întoarsă și sintetic.'), ('Interior', 'textil.'), ('Primigi × SIPeP', 'ține cont de anatomia piciorului.'))
  + '<p>Se potrivesc băieților de aproximativ 3-7 ani.</p>',
  [('model', 'Primigi Încălțăminte de trekking pentru copii gri PPTGT 23918'), ('drumeții', 'potrivit pentru drumeții și joacă pe teren dificil'),
   ('GORE-TEX', 'Membrana GORE-TEX® asigură protecție împotriva umidității'), ('Shock Absorber', 'Tehnologia Shock Absorber în talpă contribuie la reducerea șocurilor, protejând articulațiile copilului'),
   ('înșiretare', 'Sistem de înșiretare rapidă'), ('călcâi', 'Călcâi întărit'), ('talpă', 'Talpă de cauciuc cu bandă de rulare asigură aderență pe diverse suprafețe'),
   ('material', 'Partea superioară din piele întoarsă și material sintetic'), ('interior', 'Material textil'), ('SIPeP', 'Colaborarea Primigi × SIPeP favorizează dezvoltarea sănătoasă a piciorului, ținând cont de anatomia acestuia')],
  {'Model': 'Primigi 23918', 'Material': 'piele întoarsă și sintetic, interior textil', 'Caracteristici': 'GORE-TEX, Shock Absorber, înșiretare rapidă', 'Cod produs': 'PPTGT 23918'})

w(13128,
  f'<p>{GEOX} WASHIBA J56HXE roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} din material sintetic și textil, ușori, pentru purtarea zilnică. Șireturile elastice și cârligul fac pantoful ușor de pus și de scos, fără legat.</p>'
  '<p>Vârful rotund, ușor rigid, lasă loc degetelor, iar contrafortul rigid ține călcâiul pe loc, ca piciorul să nu alunece în pantof la mișcare.</p>'
  '<p>Pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'textil, se păstrează curat ușor.'), ('Interior', 'sintetic și textil.'), ('Talpă exterioară', 'din cauciuc, durabilă.'))
  + '<p>Numerele 28-31 sunt pentru fete de cam 4-7 ani.</p>',
  [('model', 'Geox Sneakers pentru copii WASHIBA culoarea roz, J56HXE.0BCKN'), ('material', 'combinația materialului sintetic cu cel textil'), ('ușor', 'Model ușor și confortabil'),
   ('închidere', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('călcâi', 'Contorul de călcâi rigid'), ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'),
   ('interior', 'Material sintetic, Material textil'), TALPA],
  {'Model': 'Geox WASHIBA', 'Material': 'sintetic și textil, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig', 'Cod produs': 'J56HXE.0BCKN'},
  notes=['Magazinul dă „Înălțime: jos”, dar și o parte superioară ridicată care rigidizează glezna; n-am precizat profilul.'])
