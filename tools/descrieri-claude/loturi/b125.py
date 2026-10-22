import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
PRIMIGI = A('/brand/primigi/', 'Primigi')
BIO = A('/brand/biomecanics/', 'Biomecanics')
PIELE = 'Descrierea spune „piele întoarsă”, iar compoziția indică material sintetic, imitație de piele; am scris doar compoziția.'

w(12695,
  f'<p>În mărimile mari, de la 128 în sus, geaca {TH} KB0KB09852 neagră e listată la {A("/categorie/baieti-imbracaminte-geci-jachete/", "geci pentru băieți")}: un model de tranziție din poliamidă parțial reciclată, netedă, fără izolație, dar cu căptușeală completă.</p>'
  '<p>Are guler ridicat, mâneci terminate cu manșetă și fermoar pe față. Glugă nu are, iar tăietura rămâne simplă, fără blocare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliamidă reciclată.'), ('Căptușeală', '100% poliamidă.'), ('Umplutură', 'nu are.'))
  + '<p>Între 128 și 176, mărimile se potrivesc pe la 8-16 ani.</p>',
  [('cod', 'KB0KB09852'), ('culoare', 'culoarea negru'), ('neizolat', 'Model neizolat cu captuseala'), ('reciclat', 'realizat partial din poliamida reciclata'),
   ('neted', 'confecționat din material neted'), ('căptușeală', 'cu căptușeală completă, sintetică'), ('guler', 'Guler ridicat'), ('manșetă', 'Finisaj din manseta'),
   ('fermoar', 'Incheiere cu fermoar'), ('glugă', 'fără glugă'), ('tăiere', 'Tăiere simplă, fără blocare'), ('material', '100% Poliamida reciclata'),
   ('poliamidă', '100% Poliamida'), ('umplutură', 'fără umplutură')],
  {'Model': 'Tommy Hilfiger KB0KB09852', 'Material': '100% poliamidă reciclată', 'Caracteristici': 'neizolată, guler ridicat, fermoar', 'Cod produs': 'KB0KB09852'})

w(12722,
  f'<p>Adidașii {TH} T3X9-34364 albi sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} cu gambă ridicată și talpă plată, ușori și confortabili pentru purtat zilnic. Se închid cu șiret, fermoar lateral și velcro, deci se pun repede.</p>'
  '<p>Vârful rotund e întărit, contrafortul rigidizat sprijină glezna și călcâiul, iar interiorul textil e plăcut pe picior și se păstrează ușor curat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic.'), ('Interior', 'material textil.'), ('Lungime branț', '22 cm la numărul 34.'))
  + '<p>Numerele 30-34 merg cam la 6-11 ani.</p>',
  [('cod', 'T3X9-34364'), ('culoare', 'culoarea alb'), ('gambă', 'Gamba ridicata'), ('plată', 'plată'), ('ușor', 'Model ușor și confortabil, ideal pentru purtarea zilnică'),
   ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'), ('vârf', 'Cutie rotunda, intarita'),
   ('contrafort', 'Contorul de călcâi rigidizat oferă un sprijin excelent pentru gleznă și călcâi'), ('interior', 'Interiorul textil este confortabil'),
   ('material', 'Material sintetic'), ('lungime', 'Lungimea brantului pentru marimea este de: 22 cm'), ('mărime', 'Dimensiunile date pentru marimea: 34')],
  {'Model': 'Tommy Hilfiger T3X9-34364', 'Material': 'material sintetic', 'Caracteristici': 'gambă ridicată, șiret, fermoar, velcro', 'Cod produs': 'T3X9.34364'},
  notes=[PIELE, 'Caracteristicile spun profil „înalt”, atributele „jos”; am scris doar „gambă ridicată”, din descriere.'])

w(12784,
  f'<p>Botinele {TH} T3A5-34017 negre sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} din textil și piele ecologică, cu toc gros și talpă groasă, plată, din cauciuc durabil. Conțin materiale din fibre reciclate și au detalii decorative.</p>'
  '<p>Vârful și spatele călcâiului sunt puternic rigidizate, iar partea înaltă ține glezna. Se închid cu fermoar lateral și au o inserție elastică, iar branțul textil e confortabil. Nu sunt izolate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material sintetic, material textil.'), ('Lungime branț', '24 cm la numărul 38.'))
  + '<p>Numerele 35-40 se poartă de pe la 10 ani în sus.</p>',
  [('cod', 'T3A5-34017'), ('culoare', 'culoarea negru'), ('piele', 'combinația materialului textil cu pielea ecologică'), ('toc', 'toc gros'), ('groasă', 'groasă, plată'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('reciclat', 'Produsul contine materiale realizate din fibre reciclate'),
   ('decorativ', 'Detalii decorative'), ('vârf', 'Varful puternic rigidizat'), ('călcâi', 'Spatele calcaiului peternic rigidizat'), ('gleznă', 'rigidizarea piciorului la gleznă'),
   ('fermoar', 'Închiderea laterală convenabilă cu fermoar'), ('elastic', 'Model cu insetie elastica'), ('branț', 'Brantul textil este confortabil'),
   ('neizolat', 'Izolare: neizolat'), ('gambă', 'Material sintetic, Material textil'), ('lungime', 'Lungimea brantului pentru marimea este de: 24 cm'),
   ('mărime', 'Dimensiunile date pentru marimea: 38')],
  {'Model': 'Tommy Hilfiger T3A5-34017', 'Talpă': 'cauciuc, toc gros', 'Caracteristici': 'fermoar lateral, inserție elastică, vârf rigidizat', 'Cod produs': 'T3A5.34017'})

w(12799,
  f'<p>Cizmele de zăpadă {PRIMIGI} 8934644 bleumarin sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme unisex")} izolate, din textil și piele ecologică, cu membrană GORE-TEX respirabilă și rezistentă la vânt. Branțul e din lână, care ține de cald la frig.</p>'
  '<p>Se leagă cu șiret, iar partea de sus se strânge cu șnururi cu opritor. Vârful e lat și rigidizat, iar talpa groasă din cauciuc, cu bandă de rulare antiderapantă, preia șocurile.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Branț', 'lână.'), ('Profil', 'înalt.'))
  + '<p>Numerele 30-35 corespund orientativ vârstei de 6-11 ani.</p>',
  [('cod', '8934644'), ('culoare', 'culoarea bleumarin'), ('izolat', 'Model Izolat din combinația materialului textil cu pielea ecologică'), ('GORE-TEX', 'Model cu membrana GORE-TEX®'),
   ('vânt', 'rezistenta la vant si respirabila'), ('lână', 'Un model cu interior din lână'), ('cald', 'vă ajută să vă mențineți cald când este frig'),
   ('șnur', 'Reglarea circumferinței superioare cu șnururi cu opritoare'), ('vârf', 'Cutia lată a degetelor'), ('rigidizat', 'rigidizat'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă'), ('antiderapantă', 'absorbție a șocurilor, cu bandă de rulare, antiderapantă'), ('groasă', 'groasă, profilată'),
   ('gambă', 'Material sintetic, Material textil'), ('profil', 'înalt')],
  {'Model': 'Primigi 8934644', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, branț din lână, șiret și șnur', 'Cod produs': '8934644'},
  notes=['Magazinul descrie membrana ca 100% impermeabilă; nu am scris „impermeabile”.'])

w(12830,
  f'<p>Adidașii din piele {BIO} 261015 roz sunt {A("/categorie/adidasi/", "adidași pentru fete")} cu profil scurt, făcuți cu sprijinul podologilor (Biomecanics Podology Partnership), pentru dezvoltarea sănătoasă a piciorului. Fața e din piele naturală, iar interiorul din textil.</p>'
  '<p>Talpa din cauciuc e flexibilă și plată, vârful are loc în plus pentru degete, iar călcâiul e ușor întărit. Se închid cu arici, iar branțurile respirabile se scot.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'piele naturală.'), ('Interior', 'material textil.'), ('Lungime branț', '17 cm.'))
  + '<p>Numerele 24-26 se potrivesc pe la 2-4 ani.</p>',
  [('cod', '261015'), ('culoare', 'Culoare roz'), ('podologi', 'Tehnologia Biomecanics Podology Partnership'), ('dezvoltare', 'susține dezvoltarea sănătoasă a picioarelor copiilor'),
   ('piele', 'Partea superioară din piele naturală'), ('interior', 'Interiorul din material textil'), ('profil', 'Profilul scurt'), ('talpă', 'Talpa flexibilă din cauciuc'),
   ('vârf', 'Spațiul mărit în vârful pantofului'), ('călcâi', 'Călcâiul ușor întărit'), ('arici', 'Închiderea practică cu arici'), ('branț', 'Branțuri detașabile'),
   ('respirabil', 'respirabil'), ('lungime', 'Lungimea branțului este: 17 cm')],
  {'Model': 'Biomecanics 261015', 'Material': 'piele naturală', 'Caracteristici': 'arici, talpă flexibilă, branț detașabil', 'Cod produs': '261015'})

w(12845,
  f'<p>Codul {PRIMIGI} 8883533, de data asta în numerele mici, 25-30, aduce aceleași {A("/categorie/ghete-cizme/", "cizme de iarnă pentru fete")} roz: izolate, din textil și piele întoarsă, cu membrană GORE-TEX și branț din lână, cu contur, care se scoate.</p>'
  '<p>Talpa groasă are bandă de rulare antiderapantă și preia șocurile, carâmbul înalt ține glezna, iar vârful e moale și lat. Velcro-ul ajută la încălțat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material textil, piele întoarsă.'), ('Interior', 'material textil.'), ('Profil', 'înalt.'))
  + '<p>Pentru 25-30, vârsta e în jur de 2-7 ani.</p>',
  [('cod', '8883533'), ('culoare', 'culoarea roz'), ('izolat', 'Izolare: izolat'), ('GORE-TEX', 'Model cu membrana GORE-TEX®'), ('lână', 'lână, cu absorbție a șocurilor'),
   ('contur', 'Brant confortabil, cu contur'), ('detașabil', 'Branțuri detașabile'), ('antiderapantă', 'absorbție a șocurilor, cu bandă de rulare, antiderapantă'),
   ('groasă', 'groasă, profilată'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('vârf', 'moale'), ('lat', 'Cutia lată a degetelor'),
   ('velcro', 'Închiderea cu velcro'), ('gambă', 'Material textil, Piele intoarsa'), ('profil', 'înalt')],
  {'Model': 'Primigi 8883533', 'Membrană': 'GORE-TEX', 'Caracteristici': 'izolate, branț din lână, velcro', 'Cod produs': '8883533'},
  notes=['Magazinul descrie membrana ca 100% impermeabilă; nu am scris „impermeabile”.'])

w(12864,
  f'<p>Adidașii din piele {PRIMIGI} 1409044 roz sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} pentru primăvară și vară, cu fața din piele naturală și piele întoarsă. Interiorul e din textil și piele, iar branțul din piele naturală preia șocurile.</p>'
  '<p>Urcă până la gleznă, cu guler ușor rigidizat, iar contrafortul e întărit. Talpa plată e din cauciuc, iar șireturile elastice și velcro-ul fac încălțatul rapid.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'piele întoarsă, piele naturală.'), ('Interior', 'material textil, piele naturală.'), ('Profil', 'scurt.'))
  + '<p>Numerele 25-29 corespund cam vârstei de 2-5 ani.</p>',
  [('cod', '1409044'), ('culoare', 'Culoare roz'), ('sezon', 'zilele de primăvară și vară'), ('față', 'Partea superioară din piele naturală și piele întoarsă'),
   ('interior', 'Interior:Material textil, Piele naturală'), ('branț', 'Branțul cu amortizare din piele naturală'), ('gleznă', 'Partea superioară care ajunge până la gleznă'),
   ('guler', 'guler ușor rigidizat'), ('contrafort', 'Contrefortul întărit'), ('talpă', 'Talpa plată din cauciuc'), ('velcro', 'Șireturile elastice și închiderea cu velcro'),
   ('profil', 'scurt')],
  {'Model': 'Primigi 1409044', 'Material': 'piele naturală, piele întoarsă', 'Caracteristici': 'branț din piele, velcro și șireturi elastice', 'Cod produs': '1409044'})

w(12881,
  f'<p>Ghetele de iarnă {BIO} 261242 bleumarin, în numerele 25-27, sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} înalte, făcute împreună cu podologi. Membrana BioTEX ajută la păstrarea piciorului uscat, iar talpa Flexi Lite e ușoară și flexibilă.</p>'
  '<p>Vârful și călcâiul sunt întărite, profilul înalt din textil și material sintetic ține glezna, iar interiorul căptușit cu textil păstrează căldura. Se închid cu arici.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'material sintetic, material textil.'), ('Talpă', 'cauciuc, plată.'), ('Branț', 'material textil.'))
  + '<p>Numerele 25-27 țin cam de vârsta 2-4 ani.</p>',
  [('cod', '261242'), ('culoare', 'Culoare bleumarin'), ('podologi', 'creat în colaborare cu podologi'), ('BioTEX', 'Membrana BioTEX'), ('uscat', 'contribuie la menținerea uscăciunii'),
   ('Flexi Lite', 'Talpa Flexi Lite'), ('ușoară', 'asigură lejeritate și flexibilitate'), ('întărit', 'Vârful întărit și călcâiul întărit'), ('profil', 'Profilul înalt'),
   ('interior', 'Interiorul căptușit'), ('căldură', 'contribuie la menținerea căldurii'), ('arici', 'Închiderea practică cu arici'),
   ('față', 'Partea superioară:Material sintetic, Material textil'), ('cauciuc', 'cauciuc'), ('plată', 'plată')],
  {'Model': 'Biomecanics 261242', 'Membrană': 'BioTEX', 'Caracteristici': 'talpă Flexi Lite, arici, profil înalt', 'Cod produs': '261242'},
  notes=['Caracteristicile spun „fără impermeabilitate”, deși descrierea pomenește membrana BioTEX; nu am scris „impermeabile”.'])

w(12895,
  f'<p>Reversibila {A("/brand/liewood/", "Liewood")} LW17576 portocalie, listată aici ca {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")}, are două fețe în culori diferite și se poartă pe oricare parte. E ușor izolată, din poliester reciclat, cu finisaj BIONIC-FINISH ECO care respinge apa.</p>'
  '<p>Gulerul ridicat ține gâtul la adăpost, gluga e integrată, fermoarul închide geaca pe toată lungimea, iar buzunarele sunt oblice. Căptușeala sintetică acoperă tot interiorul.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Căptușeală', 'completă, sintetică.'), ('Izolație', 'ușoară.'))
  + '<p>Mărimile 80-140 merg orientativ între 1 și 10 ani.</p>',
  [('cod', 'LW17576'), ('culoare', 'culoarea portocaliu'), ('două fețe', 'Model cu două fețe'), ('culori', 'din stofa in diferite culori'), ('izolat', 'Model usor izolat'),
   ('reciclat', 'Acest produs este fabricat din poliester reciclat'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('guler', 'Gulerul ridicat oferă protecție suplimentară împotriva frigului'),
   ('glugă', 'integrată'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare oblice'), ('material', '100% Poliester reciclat'),
   ('căptușeală', 'cu căptușeală completă, sintetică'), ('ușoară', 'ușoară')],
  {'Model': 'Liewood LW17576', 'Material': '100% poliester reciclat', 'Caracteristici': 'reversibilă, BIONIC-FINISH ECO, glugă', 'Cod produs': 'LW17576'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])

w(12928,
  f'<p>Kiritin de la {A("/brand/reima/", "Reima")}, în violet, apare aici la {A("/categorie/adidasi/", "adidași pentru fete")}: o pereche ușoară, din textil și piele ecologică, cu fața rezistentă la înmuiere și la apă, pentru purtat zi de zi.</p>'
  '<p>Șireturile rapide cu opritor se strâng dintr-o mișcare, talpa e flexibilă, iar inserțiile Happy Fit se scot și arată dacă numărul e potrivit. Elementele reflectorizante se văd după lăsarea întunericului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Gambă', 'material sintetic, material textil.'), ('Interior', 'material textil.'), ('Profil', 'scurt.'))
  + '<p>Numerele 28-38 se poartă de pe la 4 ani în sus.</p>',
  [('model', 'Kiritin'), ('culoare', 'culoarea violet'), ('ușor', 'Model ușor și confortabil, ideal pentru purtarea zilnică'), ('piele', 'pielea ecologică'),
   ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'), ('apă', 'Rezistența la apă înseamnă o protecție sporită'), ('șireturi', 'Sistemul rapid de șireturi cu opritoare'),
   ('flexibilă', 'Talpa flexibilă asigură un confort ridicat'), ('Happy Fit', 'Inserțiile detașabile Happy Fit'), ('reflectorizant', 'Elementele reflectorizante'),
   ('gambă', 'Material sintetic, Material textil'), ('interior', 'Material textil'), ('profil', 'scurt')],
  {'Model': 'Reima Kiritin', 'Material': 'textil, piele ecologică', 'Caracteristici': 'șireturi rapide, Happy Fit, reflectorizante', 'Cod produs': '5400134B'},
  notes=['Rezistența la apă e cea declarată de magazin, care precizează că nu garantează impermeabilitatea completă.'])
