import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9046,
  f'<p>{A("/brand/polo-ralph-lauren/", "Polo Ralph Lauren")} 323P02019001 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de vânt pentru băieți")}, bleumarin, subțire, fără izolație, pentru anotimpurile mai calde și zilele de tranziție. Se pliază și se strânge în plicul atașat, deci încape ușor în ghiozdan.</p>'
  '<p>Are fermoar scurt, ca un anorak, și mâneci raglan, care lasă brațele libere; gulerul ridicat și gluga detașabilă protejează pe vânt.</p>'
  '<p>Ce mai are geaca:</p>'
  + L(('Buzunar', 'tip cangur, în față.'), ('Căptușeală', 'din bumbac; gluga, din poliamidă.'), ('Material', '100% poliester.'), ('Glugă', 'detașabilă.'))
  + '<p>Mărimile de pe site, de la 140-149 la 163-174, sunt pentru copii de aproximativ 10-16 ani.</p>',
  [('cod', '323P02019001'), ('culoare', 'culoarea albastru marin'), ('neizolat', 'Model neizolat'), ('subțire', 'material subtire, perfect pentru anotimpurile mai calde'),
   ('tranziție', 'Izolare: tranzitional'), ('pliabil', 'Modelul este ușor de pliat și de ambalat în plicul atașat'), ('fermoar scurt', 'Închiderea cu fermoar scurt'),
   ('raglan', 'Mânecile raglan'), ('guler', 'Gulerul ridicat'), ('glugă', 'Gluga detasabila'), ('cangur', 'Un buzunar cangur'),
   ('căptușeală', 'Captuseala: 100% Bumbac'), ('căptușeală glugă', 'Captuseala glugii: 100% Poliamida'), ('material', 'Materialul de baza: 100% Poliester')],
  {'Model': 'Polo Ralph Lauren 323P02019001', 'Material': '100% poliester, căptușeală bumbac', 'Caracteristici': 'subțire, pliabilă în plic, fermoar scurt, glugă detașabilă, mâneci raglan', 'Cod produs': '323P02019001'})

w(9052,
  f'<p>{GEOX} MAQUINNENS sunt {A("/categorie/ghete-cizme/", "botine Jodhpur pentru fete")}, negre, cu platformă, din material textil și piele ecologică, fără izolație. Se poartă toamna și primăvara, cu talpă din cauciuc și sistemul Geox Respira.</p>'
  '<p>Nu au șiret sau fermoar: inserția elastică laterală le ține pe gleznă, așa că se trag direct în picior, iar numărul trebuie ales exact.</p>'
  '<p>Construcția:</p>'
  + L(('Partea de sus', 'rigidizată.'), ('Vârf', 'rotund.'), ('Interior', 'textil.'), ('Talpă', 'din cauciuc, cu platformă.'))
  + '<p>Numerele 36-40 sunt pentru copii mari, în general de la 12 ani în sus.</p>',
  [('model', 'Geox Botine copii MAQUINNENS culoarea negru, J56M6D.0CNNH'), ('Jodhpur', 'Ghete Jodhpur copii'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('neizolat', 'Izolare: neizolat'), ('platformă', 'Pantof cu platforma'), RESPIRA, ('talpă', 'Talpa exterioară din cauciuc'), ('elastic', 'Model cu insetie elastica'),
   ('fără fixare', 'Fixare: fara fixare'), ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Varf rotund'), ('interior', 'Interiorul textil')],
  {'Model': 'Geox MAQUINNENS', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'botine Jodhpur, platformă, inserție elastică, neizolate', 'Cod produs': 'J56M6D.0CNNH'})

w(9056,
  f'<p>{TH} T1A5-34006 sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} negri, pentru copiii mici, din material textil și piele ecologică, cu poliester parțial reciclat. Nu sunt izolați, deci se poartă toamna și primăvara, zilnic.</p>'
  '<p>Au șiret, fermoar lateral și arici: fermoarul deschide bocancul ca piciorul să intre ușor, iar șiretul rămâne strâns cât trebuie.</p>'
  '<p>Ce mai au:</p>'
  + L(('Vârf', 'rigidizat.'), ('Călcâi', 'contor rigidizat.'), ('Branț', 'textil.'), ('Talpă', 'exterioară, din cauciuc.'))
  + '<p>Numerele 22-29 sunt pentru copii între aproximativ 1 și 5 ani.</p>',
  [('cod', 'Bocanci copii culoarea negru, T1A5-34006'), ('material', 'combinatia materialului textil cu pielea ecologica'), ('reciclat', 'realizat partial din poliester reciclat'),
   ('neizolat', 'Izolare: neizolat'), ('zilnic', 'ideal pentru purtarea zilnică'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'),
   ('vârf', 'Varf rigidizat'), ('călcâi', 'Contorul de călcâi rigidizat'), ('branț', 'Brantul textil'), ('talpă', 'Talpa exterioară din cauciuc')],
  {'Model': 'Tommy Hilfiger T1A5-34006', 'Material': 'textil și piele ecologică, talpă din cauciuc', 'Caracteristici': 'neizolați, șiret, fermoar lateral și arici', 'Cod produs': 'T1A5-34006'})

w(9057,
  f'<p>{A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IB0IB02639 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, neagră, subțire, din poliester reciclat, fără izolație și fără căptușeală, pentru anotimpurile mai calde.</p>'
  '<p>Croiala e oversize, cu umerii coborâți, deci geaca vine largă și lasă loc de un hanorac dedesubt; mânecile și marginea de jos au bătături care o strâng la încheieturi și în talie.</p>'
  '<p>Pentru vânt și ploaie ușoară:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea, cu clapă interioară.'), ('Glugă', 'fixă, cu guler ridicat.'), ('Buzunare', 'două, laterale.'), ('Material', '100% poliester reciclat.'))
  + '<p>Pe site sunt mărimile 104-176, potrivite cam pentru 4-16 ani.</p>',
  [('cod', 'IB0IB02639'), ('culoare', 'culoarea negru'), ('neizolat', 'Model neizolat'), ('necăptușit', 'Captuseala: necaptusit'), ('subțire', 'material subțire, perfect pentru anotimpurile mai calde'),
   ('reciclat', '100% Poliester reciclat'), ('oversize', 'Fit: oversize'), ('umeri', 'linie coborâtă a umerilor'), ('bătături', 'Mânecile și marginea inferioară sunt finisate cu bătături'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară'), ('glugă, guler', 'Gulerul ridicat și gluga fixă'), ('buzunare', 'Două buzunare laterale')],
  {'Model': 'Calvin Klein Jeans IB0IB02639', 'Material': '100% poliester reciclat', 'Caracteristici': 'oversize, fără căptușeală, glugă fixă, fermoar cu clapă', 'Cod produs': 'IB0IB02639'})

w(9060,
  f'<p>{A("/brand/guess/", "GUESS")} K6YL01 este o {A("/categorie/geci-jachete/", "jachetă matlasată pentru fete")}, roz, cu inscripție, izolată ușor cu umplutură sintetică, pentru zilele mai reci de tranziție. Gluga apără de vânt și de ploaia ușoară.</p>'
  '<p>Croiala e regulară, lungă până la șolduri, iar manșetele cu nervuri strâng mânecile pe încheieturi, ca să nu intre frigul.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Căptușeală', 'integrală, ușurează îmbrăcatul.'), ('Buzunare', 'laterale.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester, țesătură rezistentă.'))
  + '<p>Mărimile duble, de la 88-96 până la 122-125, se potrivesc copiilor de aproximativ 1-7 ani.</p>',
  [('cod', 'Jachetă pentru copii roz K6YL01 W2576'), ('matlasat', 'Jacheta matlasată roz'), ('inscripție', 'Model modern cu inscripție'), ('izolație', 'Izolația sintetică ușoară'),
   ('tranziție', 'sezonul de tranziție'), ('glugă', 'Glugă practică oferă protecție suplimentară împotriva vântului și a ploii ușoare'), ('croială', 'Croiala regulară'),
   ('lungime', 'Lungime până la șolduri'), ('manșete', 'Manșete cu nervuri'), ('căptușeală', 'Căptușeală integrală'), ('buzunare', 'Buzunare laterale'),
   ('fermoar', 'Închidere cu fermoar'), ('material', '100% Poliester'), ('țesătură', 'Țesătură rezistentă')],
  {'Model': 'GUESS K6YL01', 'Material': '100% poliester, izolație sintetică ușoară', 'Caracteristici': 'matlasată, glugă, manșete cu nervuri, căptușeală integrală', 'Cod produs': 'K6YL01.W2576'})

w(9062,
  f'<p>Adidașii {GEOX} negri de aici sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} din material textil, cu partea de sus flexibilă, care se adaptează ușor la picior. Au talpă din spumă și sistemul Geox Respira în trei straturi.</p>'
  '<p>Vârful e rotund și moale, iar contorul călcâiului e tot moale, ca să nu roadă; pantoful e flexibil și se îndoaie odată cu piciorul.</p>'
  '<p>Detaliile:</p>'
  + L(('Buclă la spate', 'pentru încălțat.'), ('Interior', 'textil.'), ('Talpă', 'din spumă.'), ('Material', 'textil.'))
  + '<p>Numerele 28-39 sunt pentru copii de la aproximativ 4 ani până la adolescenți.</p>',
  [('model', 'Sneakers pentru copii culoarea negru'), ('textil', 'confecționat din material textil'), ('flexibil', 'Modelul cu partea superioară flexibilă se adaptează cu ușurință la picior'),
   ('talpă', 'Talpa din spumă'), RESPIRA, ('vârf', 'Cutie rotunda si moale'), ('călcâi', 'Contorul moale pentru călcâi protejează călcâiul de frecare'),
   ('buclă', 'Bucla de la spate'), ('interior', 'Interiorul textil')],
  {'Model': 'Geox, adidași', 'Material': 'textil, talpă din spumă', 'Caracteristici': 'partea de sus flexibilă, Geox Respira, vârf și călcâi moi', 'Cod produs': ''})

w(9065,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261276 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, ușori, din material textil și sintetic, cu profil scurt și talpă plată din spumă și cauciuc. Modelul vine din programul Biomecanics Podology, pentru activitățile zilnice.</p>'
  '<p>Profilul scurt lasă glezna liberă, iar aricii se prind repede; branțurile textile se scot, pentru curățat și pentru verificat lungimea piciorului.</p>'
  '<p>Pe scurt:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'plată, spumă și cauciuc.'))
  + '<p>Numerele 28-38 se potrivesc copiilor de la 4 ani în sus, cu aproximație.</p>',
  [('cod', 'Sneakers pentru copii negri 261276'), ('material', 'Partea superioară din material textil și sintetic'), ('ușor', 'construcție ușoară'),
   ('Podology', 'Parteneriatul Biomecanics Podology'), ('zilnic', 'activităților zilnice'), ('profil', 'Profilul scurt al părții superioare'),
   ('talpă', 'Talpă plată din spumă și cauciuc'), ('arici', 'Închidere practică cu arici'), ('branț', 'Branțuri textile detașabile'), ('călcâi', 'Călcâi ușor întărit'),
   ('interior', 'Interior căptușit cu material textil')],
  {'Model': 'Biomecanics 261276', 'Material': 'textil și sintetic, talpă din spumă și cauciuc', 'Caracteristici': 'profil scurt, arici, branț detașabil', 'Cod produs': '261276'},
  notes=['Titlul de pe site nu are culoare; magazinul arată negru.'])

w(9083,
  f'<p>{A("/brand/reima/", "Reima")} Tepastelu sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași impermeabili unisex")} verzi, din material textil și piele ecologică, cu membrana ReimaTec, care oprește ploaia și vântul. Sunt ușori și făcuți pentru purtat zilnic, inclusiv pe vreme umedă.</p>'
  '<p>Cutia degetelor e lată, cu loc pentru un picior mai plinuț, iar aricii se ajustează repede. Inserțiile detașabile Happy Fit ajută la alegerea mărimii.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Talpă', 'flexibilă.'), ('Profil', 'scurt.'), ('Apă', 'rezistență sporită, fără impermeabilitate completă.'))
  + '<p>Numerele 22-28 sunt pentru copii între aproximativ 1 și 5 ani.</p>',
  [('model', 'Sneakers pentru copii Tepastelu 5400141B'), ('material', 'combinația materialului textil cu pielea ecologică'), ('ReimaTec', 'ReimaTec oferă protecție împotriva ploii și vântului'),
   ('zilnic', 'ideal pentru purtarea zilnică'), ('cutie lată', 'Cutia lată a degetelor'), ('arici', 'Închiderea cu velcro'), ('Happy Fit', 'Inserțiile detașabile Happy Fit'),
   ('talpă', 'Talpa flexibilă'), ('profil', 'Înălțime: mic de statură'), ('nu complet', 'nu garantează impermeabilitatea completă')],
  {'Model': 'Reima Tepastelu', 'Material': 'textil și piele ecologică', 'Caracteristici': 'ReimaTec, arici, cutie lată a degetelor, Happy Fit', 'Cod produs': '5400141B'},
  notes=['Titlul de pe site spune verde; magazinul listează culoarea albastru.'])

w(9095,
  f'<p>{TH} KS0KS00731 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, bej, ușor izolată cu umplutură sintetică, din poliamidă parțial reciclată. E pentru temperaturile mai scăzute de toamnă și primăvară.</p>'
  '<p>Croiala e simplă, fără glugă, iar mânecile lungi se termină cu manșetă elastică, care le strânge pe încheieturi.</p>'
  f'<p>Pe scurt, despre geacă:</p>'
  + L(('Căptușeală', 'are, cu izolație ușoară.'), ('Material', '100% poliamidă reciclată și 100% nailon.'), ('Glugă', 'nu are.'))
  + f'<p>Pentru vânt, capul se acoperă cu ceva din {A("/categorie/baieti-accesorii-caciuli-manusi-accesorii/", "căciulile și accesoriile pentru băieți")}. Geaca vine în mărimile 128-176, pentru copii de aproximativ 8-16 ani.</p>',
  [('cod', 'KS0KS00731'), ('culoare', 'culoarea bej'), ('ușor izolat', 'Model usor izolat'), ('izolație', 'izolație sintetică'), ('matlasat', 'Matlasat'),
   ('reciclat', 'realizat partial din poliamida reciclata'), ('temperaturi', 'temperaturi mai scăzute'), ('croială', 'Tăiere simplă'), ('fără glugă', 'Gluga: fara gluga'),
   ('manșetă', 'Mâneci lungi finisate cu o manșetă confortabilă, elastică'), ('căptușeală', 'Model usor izolat pe captuseala'),
   ('material 1', 'Material 1: 100% Poliamida reciclata'), ('material 2', 'Material 2: 100% Nailon')],
  {'Model': 'Tommy Hilfiger KS0KS00731', 'Material': 'poliamidă reciclată și nailon', 'Caracteristici': 'ușor izolată, matlasată, manșete elastice, fără glugă', 'Cod produs': 'KS0KS00731'},
  comp={'slug': '/categorie/baieti-accesorii-caciuli-manusi-accesorii/', 'motiv': 'geacă fără glugă'})

w(9096,
  f'<p>{GEOX} SKETLITE sunt {A("/categorie/adidasi/", "adidași cu luminițe pentru fete")}, albi, din imitație de piele și material textil, pentru primăvară, vară și toamnă. Luminițele se aprind de la un buton de pe capută, așa că seara copilul se vede mai bine.</p>'
  '<p>Caputa urcă până la gleznă, cu guler ușor rigidizat, iar șireturile elastice și aricii îi lasă pe copii să se încalțe singuri și să ajusteze pantoful.</p>'
  '<p>Restul pantofului:</p>'
  + L(('Geox Respira™', 'ține piciorul uscat.'), ('Talpă', 'plată, din cauciuc.'), ('Contrafort', 'rigidizat.'), ('Interior', 'material textil.'))
  + '<p>Numerele 24-27 sunt pentru copii de cam 2-4 ani.</p>',
  [('model', 'Geox SKETLITE sneakers copii albi J65NWA.054AJ'), ('material', 'Caputa din imitație de piele'), ('sezon', 'zilele de primăvară, vară și toamnă'),
   ('luminițe', 'Luminițele încorporate , activate printr-un buton de pe capută'), ('gleznă', 'Caputa până la gleznă , cu un guler ușor rigidizat'),
   ('închidere', 'Șireturile elastice și închiderea cu scai'), ('Respira', 'Tehnologia Geox Respira'), ('talpă', 'Talpa plată din cauciuc'),
   ('contrafort', 'Contrabrațul rigidizat'), ('interior', 'Interiorul din material textil')],
  {'Model': 'Geox SKETLITE', 'Material': 'imitație de piele și textil, talpă din cauciuc', 'Caracteristici': 'luminițe cu buton, șireturi elastice și arici, Geox Respira™', 'Cod produs': 'J65NWA.054AJ'})
print('lot 13 scris')
