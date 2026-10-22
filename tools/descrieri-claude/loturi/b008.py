import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(8760,
  f'<p>{A("/brand/kenzo-kids/", "Kenzo Kids")} K60721 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă ușor izolată pentru băieți")}, bleumarin, din poliamidă cu aplicație, căptușită cu poliester. E pentru zilele răcoroase de toamnă și primăvară, la copiii mici.</p>'
  '<p>Fasonul e drept, iar manșetele se încheie, deci mânecile se strâng și pe încheieturi subțiri. Geaca se închide cu cleme.</p>'
  '<p>Geaca are puține piese, toate practice:</p>'
  + L(('Închidere', 'cleme.'), ('Guler', 'are.'), ('Buzunare', 'oblice.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 86-108 sunt gândite pentru copii între aproximativ 1 și 5 ani.</p>',
  [('cod', 'K60721'), ('culoare', 'culoarea albastru marin'), ('ușor izolat', 'Model usor izolat'), ('aplicație', 'material textil cu aplicatie'),
   ('poliamidă', 'Materialul de baza: 100% Poliamida'), ('căptușeală', 'Captuseala: 100% Poliester'), ('fason', 'Fason drept'), ('manșete', 'Maneci cu mansete incheiate'),
   ('cleme', 'Incheiere cu cleme'), ('guler', 'Model cu guler'), ('buzunare', 'Buzunare oblice'), ('fără glugă', 'Gluga: fara gluga')],
  {'Model': 'Kenzo Kids K60721', 'Material': '100% poliamidă, căptușeală 100% poliester', 'Caracteristici': 'ușor izolată, fason drept, cleme, manșete încheiate', 'Cod produs': 'K60721'})

w(8765,
  f'<p>{GEOX} MAQUINNENS sunt {A("/categorie/ghete-cizme/", "bocanci cu platformă pentru fete")}, negri, ușor izolați, cu talpă din cauciuc și sistemul Geox Respira. Sunt pentru toamnă și pentru iernile blânde.</p>'
  '<p>Au șiret, fermoar lateral și arici: fermoarul deschide bocancul la încălțat, iar șiretul și aricii îl strâng pe gleznă cât e nevoie.</p>'
  '<p>Și câteva detalii de construcție:</p>'
  + L(('Partea de sus', 'rigidizată.'), ('Vârf', 'rotund.'), ('Interior', 'textil.'), ('Buclă la spate', 'pentru încălțat.'))
  + '<p>Bocancii se găsesc între numerele 31 și 40, deci pentru copii de 6 ani și mai mari, în general.</p>',
  [('model', 'Bocanci copii MAQUINNENS culoarea negru, J56M6E.000CN'), ('platformă', 'Pantof cu platforma'), ('izolat', 'Izolare: usor izolat'),
   ('talpă', 'Talpa exterioară din cauciuc'), RESPIRA, ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'),
   ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Varf rotund'), ('interior', 'Interiorul textil'), ('buclă', 'Bucla de la spate')],
  {'Model': 'Geox MAQUINNENS', 'Material': 'imitație de piele, interior textil, talpă din cauciuc', 'Caracteristici': 'ușor izolați, platformă, șiret, fermoar lateral și arici', 'Cod produs': 'J56M6E.000CN'})

w(8766,
  f'<p>{A("/brand/burton/", "Burton")} CROWN este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă rezistentă la apă unisex")}, neagră, cu glugă, din poliester parțial reciclat, cu tehnologia Dryride pentru rezistență la apă și respirabilitate. Nu are izolație, deci se poartă pe vreme umedă de tranziție sau peste un strat cald.</p>'
  '<p>Croiala e simplă, iar mânecile raglan lasă brațele și umerii liberi la mișcare.</p>'
  '<p>Ce mai declară magazinul:</p>'
  + L(('Tratament', 'PFC Repellent, fără compuși perfluorurați.'), ('Certificare', 'Bluesign®.'), ('Buzunare', 'oblice.'), ('Glugă', 'are.'))
  + '<p>Mărimile de pe site, de la 140 la 164-166, sunt pentru copii de cam 10-14 ani.</p>',
  [('model', 'Geacă copii CROWN culoarea negru, 221221'), ('neizolat', 'Model neizolat'), ('Dryride', 'Tehnologia Dryride ofera rezistenta la apa si respirabilitate'),
   ('reciclat', 'Materialul de baza: 60% Poliester reciclat, 40% Poliester'), ('PFC', 'PFC Repellent'), ('Bluesign', 'Model certificat Bluesign'),
   ('croială', 'Tăiere simplă'), ('raglan', 'Maneca raglan'), ('buzunare', 'Buzunare oblice'), ('glugă', 'Model cu gluga')],
  {'Model': 'Burton CROWN', 'Material': '60% poliester reciclat, 40% poliester', 'Caracteristici': 'Dryride, PFC Repellent, Bluesign®, glugă, mâneci raglan, fără izolație', 'Cod produs': '221221'})

w(8767,
  f'<p>{TH} KS0KS00644 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de tranziție unisex")}, bleumarin, din țesătură netedă de poliester parțial reciclat, cu căptușeală, dar fără izolație. Se poartă primăvara și toamna.</p>'
  '<p>Croiala e simplă, iar manșetele se încheie, ca mânecile să nu atârne pe încheieturi subțiri. Umplutura, din poliester reciclat, e subțire, de geacă de tranziție.</p>'
  '<p>Geaca are mai multe buzunare decât pare:</p>'
  + L(('Buzunare laterale', 'două, cu capse.'), ('Buzunar', 'pe piept.'), ('Închidere', 'capse.'), ('Guler', 'are.'))
  + '<p>Geaca are mărimile 128-176, potrivite cam de la 8 la 16 ani.</p>',
  [('cod', 'KS0KS00644'), ('culoare', 'culoarea bleumarin'), ('neted', 'țesătură netedă'), ('reciclat', 'realizat partial din poliester reciclat'),
   ('neizolat', 'Model neizolat cu captuseala'), ('tranziție', 'Izolare: tranzitional'), ('croială', 'Tăiere simplă'), ('manșete', 'Maneci cu mansete incheiate'),
   ('buzunare', 'Două buzunare laterale'), ('piept', 'Buzunar pe piept'), ('capse', 'Închiderea convenabilă cu capsă'), ('guler', 'Model cu guler'), ('umplutură', 'Umplutura: 100% Poliester reciclat')],
  {'Model': 'Tommy Hilfiger KS0KS00644', 'Material': '100% poliester, parțial reciclat', 'Caracteristici': 'de tranziție, căptușită, capse, trei buzunare, manșete încheiate', 'Cod produs': 'KS0KS00644'})

w(8771,
  f'<p>{A("/brand/reima/", "Reima")} Sujuva sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași impermeabili unisex")}, negri, din textil și material sintetic, cu membrană impermeabilă laminată pe partea de sus. Sunt ușori, pentru activitățile în aer liber, iar membrana ține piciorul uscat pe iarba udă sau prin bălți mici.</p>'
  '<p>Branțul detașabil are imprimat un ghid de mărime, deci verifici direct pe el dacă mai e loc pentru picior. Șireturile elastice și aricii se prind repede.</p>'
  '<p>Pentru drumurile de seară și pentru mediu:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede după lăsarea întunericului.'), ('Talpă', 'spumă și cauciuc, flexibilă.'), ('Contrefort', 'rigidizat.'), ('Compoziție', 'fără fluorocarburi și PVC.'))
  + '<p>Numerele 26-40 acoperă copii de la cam 3 ani până la vârsta de adolescent.</p>',
  [('model', 'Reima Sujuva sneakers pentru copii negri 5400153B'), ('membrană', 'Membrana impermeabilă laminată pe partea superioară'),
   ('uscat', 'menținerea picioarelor uscate'), ('material', 'Partea superioară din material textil și sintetic'), ('aer liber', 'activitățile în aer liber'),
   ('branț', 'Branțul detașabil cu imprimeu pentru verificarea mărimii'), ('închidere', 'Șireturile elastice și închiderea cu velcro'),
   ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'), ('talpă', 'Talpa din spumă și cauciuc'), ('contrefort', 'Contrefortul rigidizat'),
   ('fără PVC', 'Compoziția fără fluorocarburi și PVC')],
  {'Model': 'Reima Sujuva', 'Material': 'textil și sintetic, interior textil, talpă din spumă și cauciuc', 'Caracteristici': 'membrană impermeabilă, branț cu ghid de mărime, reflectorizante', 'Cod produs': '5400153B'})

w(8772,
  f'<p>{TH} T1A9-35107 sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, uni, din imitație de piele și material textil, cu profil scurt. Sunt făcuți pentru activitățile de zi cu zi, de la joaca afară la ținutele de oraș.</p>'
  '<p>Aricii au o curea reglabilă, care se strânge pe un picior îngust sau mai plin, iar gulerul e ușor întărit în jurul gleznei.</p>'
  '<p>Restul pantofului:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare.'), ('Călcâi', 'întărit.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Cu numere de la 20 la 34, modelul se potrivește copiilor între aproximativ 1 și 11 ani.</p>',
  [('model', 'Sneakers pentru copii roz T1A9-35107'), ('uni', 'modelul uni'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('profil', 'Profil scurt'), ('zilnic', 'activitățile zilnice'), ('oraș', 'completare a ținutelor urbane'), ('arici', 'Închidere practică cu arici'),
   ('curea', 'Curea reglabilă'), ('guler', 'Guler ușor întărit în jurul gleznei'), ('talpă', 'Talpă de cauciuc cu bandă de rulare'), ('călcâi', 'Călcâi întărit'),
   ('interior', 'Interior căptușit cu material textil')],
  {'Model': 'Tommy Hilfiger T1A9-35107', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'profil scurt, arici cu curea reglabilă', 'Cod produs': 'T1A9-35107'})

w(8773,
  f'<p>{GEOX} PERTH sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași înalți pentru băieți")}, negri, din imitație de piele, textil și material sintetic, cu tehnologia Geox Respira™ în talpă. Se poartă la ținute casual și streetwear.</p>'
  '<p>Au șireturi plus o bandă cu arici, deci se strâng exact pe picior, iar profilul înalt, cu guler ușor întărit, acoperă glezna.</p>'
  '<p>La interior și dedesubt:</p>'
  + L(('Talpă', 'din cauciuc.'), ('Căptușeală', 'textilă.'), ('Branț', 'detașabil.'), ('Călcâi', 'ușor întărit.'))
  + '<p>Numerele 28-41 sunt pentru copii de la 4 ani în sus, în general.</p>',
  [('model', 'Geox PERTH sneakers pentru copii negri J467RA.0MEFU'), ('material', 'Combinație de imitație de piele, material textil și sintetic'),
   ('Respira', 'Tehnologia GEOX Respira'), ('casual', 'ținute casual și streetwear'), ('închidere', 'Combinația de șireturi cu bandă velcro'),
   ('profil', 'Profil înalt al părții superioare'), ('guler', 'Guler ușor întărit în jurul gleznei'), ('talpă', 'Talpă din cauciuc'), ('căptușeală', 'Căptușeală textilă'),
   ('branț', 'Branțuri detașabile'), ('călcâi', 'Călcâi ușor întărit')],
  {'Model': 'Geox PERTH', 'Material': 'imitație de piele, textil și sintetic, talpă din cauciuc', 'Caracteristici': 'profil înalt, șireturi și arici, Geox Respira™, branț detașabil', 'Cod produs': 'J467RA.0MEFU'},
  notes=['Titlul de pe site nu are culoare; magazinul arată negru.'])

w(8774,
  f'<p>{GEOX} ASSISTER sunt {A("/categorie/adidasi/", "adidași cu lumini pentru fete")}, roz, din material textil și sintetic. Luminile se activează de la un buton, așa că pe drumurile de seară copilul se vede mai bine.</p>'
  '<p>Călcâiul e întărit și căptușit moale, ca să nu roadă, iar inserția detașabilă se scoate pentru curățat și pentru verificat lungimea piciorului.</p>'
  '<p>Restul construcției Geox:</p>'
  + L(('Geox Respira', 'talpă în trei straturi.'), ('Vârf', 'rotund, întărit.'), ('Guler', 'ușor rigidizat.'), ('Buclă la spate', 'pentru încălțat.'))
  + '<p>Pe site sunt numerele 32-35, de regulă pentru copii de 8-11 ani.</p>',
  [('model', 'Sneakers pentru copii ASSISTER culoarea roz, J55E9B.0ASKN'), ('material', 'combinatia materialului textil cu cel sintetic'),
   ('lumini', 'Model cu lumini incorporate, activate de un buton'), ('călcâi', 'Călcâiul întărit cu umplutură moale'), ('inserție', 'Inserție detașabilă, ușor de curățat'),
   RESPIRA, ('vârf', 'Cutie rotunda, intarita'), ('guler', 'Gulerul gambei usor rigidizat'), ('buclă', 'Bucla de la spate'), ('talpă', 'Talpă din cauciuc')],
  {'Model': 'Geox ASSISTER', 'Material': 'textil și sintetic, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'lumini cu buton, Geox Respira, inserție detașabilă', 'Cod produs': 'J55E9B.0ASKN'})

w(8784,
  f'<p>{A("/brand/abellula/", "Abel&amp;Lula")} 5395 este o {A("/categorie/geci-jachete/", "jachetă de tranziție pentru fete")}, albă, din stofă cu aplicații din paiete, fără izolație și fără căptușeală. E o piesă de primăvară și de toamnă.</p>'
  '<p>Fasonul e drept, iar jacheta se încheie cu nasturi; fără glugă și căptușeală, rămâne subțire, ușor de purtat peste o rochie sau un tricou.</p>'
  '<p>De aproape, jacheta are:</p>'
  + L(('Paiete', 'aplicație decorativă.'), ('Buzunare', 'false, decorative.'), ('Material', 'bumbac și poliester, în două țesături (95/5 și 65/35).'), ('Închidere', 'nasturi.'))
  + '<p>Jacheta vine în mărimile 104-162, pentru copii de aproximativ 4-14 ani.</p>',
  [('cod', 'Geacă copii culoarea alb, 5395'), ('paiete', 'stofa cu paiete'), ('neizolat', 'Model neizolat'), ('necăptușit', 'Captuseala: necaptusit'),
   ('tranziție', 'Izolare: tranzitional'), ('fason', 'Fason drept'), ('nasturi', 'Incheiere cu nasturi'), ('fără glugă', 'Gluga: fara gluga'),
   ('aplicație', 'Aplicație decorativă din paiete'), ('buzunar', 'Imitatie de buzunar'), ('material 1', 'Material 1: 95% Bumbac, 5% Poliester'), ('material 2', '65% Poliester , 35% Bumbac')],
  {'Model': 'Abel&Lula 5395', 'Material': 'bumbac și poliester', 'Caracteristici': 'de tranziție, paiete, nasturi, fason drept', 'Cod produs': '5395'})

w(8788,
  f'<p>{GEOX} WASHIBA în bleumarin sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} din material textil, piele naturală și piele ecologică, cu talpă din cauciuc și sistemul Geox Respira în trei straturi.</p>'
  '<p>Se leagă cu șiret clasic, care se strânge exact pe picior, iar inserția detașabilă se scoate la curățat. Călcâiul e întărit și căptușit moale, ca să nu roadă.</p>'
  '<p>Construcția, pe scurt:</p>'
  + L(('Vârf', 'rotund, întărit.'), ('Partea de sus', 'rigidizată.'), ('Profil', 'scurt.'), ('Detalii', 'decorative.'))
  + '<p>Numerele 31-41 sunt pentru copii de pe la 6 ani în sus.</p>',
  [('model', 'Sneakers pentru copii WASHIBA culoarea albastru marin, J55LQD.05422'), ('material', 'combinatie de material textil, piele naturala si piele ecologica'),
   ('talpă', 'Talpă din cauciuc'), RESPIRA, ('șiret', 'Șiretul clasic permite ajustarea individuală'), ('inserție', 'Inserție detașabilă, ușor de curățat'),
   ('călcâi', 'Călcâiul întărit cu umplutură moale'), ('vârf', 'Cutie rotunda, intarita'), ('rigidizat', 'Partea superioară rigidizată'),
   ('profil', 'Înălțime: mic de statură'), ('decorative', 'Detalii decorative')],
  {'Model': 'Geox WASHIBA', 'Material': 'textil, piele naturală și piele ecologică, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șiret, inserție detașabilă', 'Cod produs': 'J55LQD.05422'})
print('lot 8 scris')
