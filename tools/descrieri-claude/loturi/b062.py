import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

NIKE = A('/brand/nike/', 'Nike')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
GEOX = A('/brand/geox/', 'Geox')
NOTE = 'Pagina magazinului (Fashion Days) nu are descriere detaliată; am folosit doar faptele din titlu.'
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(12112,
  f'<p>Vesta {A("/brand/4f/", "4F")} 302874682 este o {A("/categorie/geci-jachete/", "vestă pentru fete")}, verde, din poliamidă, un strat fără mâneci care lasă brațele libere la joacă și se poartă peste un hanorac sau un pulover.</p>'
  '<p>Mărimile 122-158 de pe site merg, în general, la fete de 7-13 ani.</p>',
  [('model', 'Vesta Fete, 302874682, Poliamida, Verde')],
  {'Model': '4F 302874682', 'Material': 'poliamidă', 'Caracteristici': 'vestă', 'Cod produs': '302874682'},
  insuf=True, notes=[NOTE])

w(12126,
  f'<p>Geaca {A("/brand/puma/", "Puma")} 78645 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} în culoarea albastru, singura variantă de culoare din pagina produsului. Pagina nu dă detalii despre material sau izolație, deci e bine de verificat eticheta înainte de sezonul rece.</p>'
  + '<p>Pe site sunt mărimile 128-140, adică, aproximativ, copii de 8-10 ani.</p>',
  [('model', 'copii, - 78645'), ('culoare', 'Albastru')],
  {'Model': 'Puma 78645', 'Material': '', 'Caracteristici': '', 'Cod produs': '78645'},
  insuf=True, notes=[NOTE, 'Titlul paginii e doar „copii, - 78645”; culoarea apare la varianta de mărime 140 CM.'])

w(12193,
  f'<p>{NIKE} G NSW FLC JKT DANCE IF1712-010 este o {A("/categorie/geci-jachete/", "geacă bomber pentru fete")}, neagră, din bumbac, cu croială clasică și aspect ușor scurt, pentru purtare casual primăvara și vara. Logo-ul Swoosh e brodat pe piept.</p>'
  '<p>Gulerul înalt, manșetele și tivul sunt reiate și strâng jacheta pe corp, ca la orice bomber, deci stă aproape și de un copil mai slab.</p>'
  '<p>Pentru zilele blânde, jacheta are:</p>'
  + L(('Închidere', 'fermoar, în față.'), ('Buzunare', 'două, frontale, cu deschidere dreaptă.'), ('Guler', 'reiat, înalt, cu branding Nike.'))
  + '<p>Pe site sunt mărimile M, L și XL, care după tabelul Nike al magazinului acoperă în mare vârsta de 10-15 ani.</p>',
  [('model', 'Jacheta Nike G NSW FLC JKT DANCE neagră'), ('bomber', 'Jachetă Nike în stil bomber'), ('bumbac', 'Material: bumbac'),
   ('croială', 'cu croială clasică și aspect ușor scurt'), ('casual', 'Potrivită pentru purtare casual'), ('sezon', 'în sezonul primăvară-vară'),
   ('logo', 'logo Nike Swoosh brodat pe piept'), ('reiat', 'Are guler tip guler reiat, manșete reiate și tiv reiat'), ('guler', 'guler reiat tip guler înalt, cu branding „Nike”'),
   ('fermoar', 'Închiderea este frontală, cu fermoar'), ('buzunare', 'două buzunare frontale tip buzunar cu deschidere dreaptă')],
  {'Model': 'Nike G NSW FLC JKT DANCE', 'Material': 'bumbac', 'Caracteristici': 'bomber, guler, manșete și tiv reiate', 'Cod produs': 'IF1712-010'},
  varsta_txt='10-15 ani', notes=['Vârsta pentru M-XL: tabelul de mărimi Nike al magazinului (pagina produsului 4949).', 'Magazinul trece la gen „Baieti”; pe site e la fete.'])

w(12255,
  f'<p>{NIKE} Y NK Thermal RPL Park20 Fall Jacket CW6159-010 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de toamnă unisex")}, neagră, din poliester cu suprafață netedă, țesută, cu glugă. Magazinul o indică pentru sport și baschet, toamna.</p>'
  '<p>Croiala e clasică, iar manșetele și tivul elasticizate strâng geaca la încheieturi și jos, ca vântul să nu intre pe dedesubt.</p>'
  '<p>Detaliile de închidere și buzunare:</p>'
  + L(('Închidere', 'fermoar, în față.'), ('Buzunare', 'laterale, diagonale, cu detalii cu capse.'), ('Logo', 'Swoosh, pe piept.'))
  + '<p>Pe site e doar mărimea XL, care după tabelul Nike al magazinului se potrivește cam la 13-15 ani.</p>',
  [('model', 'Geaca Nike Y NK Thermal RPL Park20 Fall Jacket'), ('poliester', 'realizată din poliester, cu suprafață netedă, țesută'), ('glugă', 'Are glugă'),
   ('sport', 'Este potrivită pentru sport și baschet și este indicată pentru toamnă'), ('croială', 'croială clasică'), ('elastic', 'manșetele și tivul sunt elasticizate'),
   ('fermoar', 'închidere frontală cu fermoar'), ('buzunare', 'buzunare laterale diagonale cu detalii cu capse'), ('logo', 'Logo-ul Nike Swoosh este poziționat pe piept')],
  {'Model': 'Nike Y NK Thermal RPL Park20 Fall Jacket', 'Material': 'poliester', 'Caracteristici': 'glugă, manșete și tiv elasticizate', 'Cod produs': 'CW6159-010'},
  varsta_txt='13-15 ani', notes=['Vârsta pentru XL: tabelul de mărimi Nike al magazinului (pagina produsului 4949).'])

w(12315,
  f'<p>{TH} Low CUT Lace UP SNEAKER T3A9-33212 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, sub gleznă, din material sintetic neted, cu logo proeminent pe lateral, dungă roșu-alb-albastru și accente metalice la călcâi. Se poartă casual, la ținute lifestyle.</p>'
  '<p>Șireturile se reglează după forma piciorului, iar vârful e rotund. La gleznă au căptușeală cu padding, iar pe mijloc perforații mici.</p>'
  '<p>Construcția, în câteva puncte:</p>'
  + L(('Talpă', 'plată, mată, cu textură vizibilă.'), ('Cusături', 'duble la panouri.'), ('Material', 'sintetic.'))
  + '<p>Numerele 38-40 sunt pentru adolescenți de la 12 ani în sus, în general.</p>',
  [('model', 'Pantofi sport Tommy Hilfiger Low CUT Lace UP SNEAKER albi'), ('sub gleznă', 'Model sub gleznă'), ('sintetic', 'Partea superioară este din material sintetic, cu suprafață netedă'),
   ('logo', 'logo proeminent pe lateral'), ('dungă', 'dungă roșu-alb-albastru'), ('metal', 'accente metalice în zona călcâiului'), ('casual', 'potrivit pentru lifestyle și ținute casual'),
   ('șireturi', 'închidere cu șireturi'), ('vârf', 'vârf rotund'), ('padding', 'În zona gleznei se observă căptușeală/padding'), ('perforații', 'perforații mici'),
   ('talpă', 'Talpa este plată, cu finisaj mat și textură vizibilă'), ('cusături', 'cusături duble la panouri')],
  {'Model': 'Tommy Hilfiger Low CUT Lace UP SNEAKER', 'Material': 'sintetic', 'Caracteristici': 'sub gleznă, șireturi, perforații, accente metalice', 'Cod produs': 'T3A9-33212-1355X025'})

w(12316,
  f'<p>{TH} logo Low CUT Lace UP T3X9-33360 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} albi, sub gleznă, din material sintetic, cu talpă groasă, mată, și logo proeminent pe călcâi. Sunt pentru stil lifestyle, la purtat zilnic.</p>'
  '<p>Șireturile strâng pantoful după picior, iar vârful e rotund, fără toc. Zona călcâiului e întărită și ține piciorul în pantof.</p>'
  '<p>Pe dinafară, pantoful are:</p>'
  + L(('Perforații', 'mici, pe lateral.'), ('Webbing', 'lateral, în culorile mărcii.'), ('Cusături', 'decorative.'))
  + '<p>Numerele 40-41 se potrivesc adolescenților de pe la 12 ani în sus.</p>',
  [('model', 'Pantofi sport Tommy Hilfiger logo Low CUT Lace UP, albi'), ('sintetic', 'Pantofi sport Tommy Hilfiger din material sintetic'), ('sub gleznă', 'Modelul este sub gleznă'),
   ('talpă', 'talpă groasă, cu finisaj mat'), ('logo', 'logo vizibil pe călcâi'), ('lifestyle', 'pentru stil lifestyle'), ('șireturi', 'Închiderea cu șireturi'),
   ('vârf', 'cu vârf rotund și fără toc'), ('călcâi', 'în zona călcâiului există o zonă întărită'), ('perforații', 'perforații mici pe lateral'),
   ('webbing', 'webbing lateral în culori semnătură'), ('cusături', 'cusături decorative')],
  {'Model': 'Tommy Hilfiger logo Low CUT Lace UP', 'Material': 'sintetic', 'Caracteristici': 'sub gleznă, talpă groasă, perforații', 'Cod produs': 'T3X9-33360-1355X336'})

w(12359,
  f'<p>Bocancii {GEOX} în culoarea bleumarin sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} neizolați, din material sintetic neporos, care se curăță cu o cârpă umedă. Se poartă în sezonul de tranziție, nu pe ger.</p>'
  '<p>Au șiret și fermoar lateral: șiretul se reglează o dată după picior, iar fermoarul ajută la încălțat. Bucla de la spate ajută la tras bocancul.</p>'
  '<p>Restul construcției arată așa:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Călcâi', 'contrafort rigid.'), ('Geox Respira', 'talpă în trei straturi, perforată.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Numerele 36-39 se poartă, de obicei, de la 12 ani în sus.</p>',
  [('model', 'Geox Bocanci copii culoarea albastru marin'), ('sintetic', 'confecționat din material sintetic'), ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'),
   ('neizolat', 'Izolare: neizolat'), ('șiret, fermoar', 'Model cu siret cu fermoar lateral'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid'), RESPIRA, ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox (bocanci)', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'neizolați, șiret și fermoar lateral, Geox Respira', 'Cod produs': ''})

w(12363,
  f'<p>Geaca {A("/brand/guess/", "Guess")} H4BT03 WCFM0 este o {A("/categorie/geci-jachete/", "geacă matlasată pentru fete")}, roz, din material neted, ușor izolată pe căptușeală, pentru temperaturile mai reci. Gluga apără capul de vânt.</p>'
  '<p>Croiala e simplă, dreaptă, iar mânecile și tivul au bordură, care strânge la încheieturi și jos. Fermoarul se trage ușor și de un copil mic.</p>'
  '<p>Ce mai are, pe lângă glugă:</p>'
  + L(('Buzunare', 'două, laterale, cu fermoar.'), ('Material', '100% poliester.'), ('Izolație', 'ușoară, pe căptușeală.'))
  + '<p>Mărimile 88-96 până la 122-125 corespund, cu aproximație, vârstei de 1-7 ani.</p>',
  [('model', 'Guess Geaca copii culoarea roz, H4BT03 WCFM0'), ('matlasat', 'Model matlasat cu izolație sintetica'), ('neted', 'material neted'),
   ('izolat', 'Model usor izolat pe captuseala'), ('reci', 'temperaturi mai reci'), ('glugă', 'Model cu gluga'), ('croială', 'Tăiere simplă, fără blocare'),
   ('bordură', 'Mânecile și marginea inferioară sunt finisate cu bătături'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'Guess H4BT03 WCFM0', 'Material': '100% poliester', 'Caracteristici': 'matlasată, ușor izolată, glugă', 'Cod produs': 'H4BT03 WCFM0'})

w(12372,
  f'<p>Bocancii {GEOX} bordo sunt {A("/categorie/ghete-cizme/", "bocanci neizolați pentru fete")}, din material sintetic neporos, ușor de curățat cu o cârpă umedă, pentru zilele de tranziție. Interiorul e textil și se ține ușor curat.</p>'
  '<p>Șiretul se reglează după lățimea piciorului, iar fermoarul lateral face încălțatul rapid. Contrafortul rigid ține călcâiul pe loc.</p>'
  '<p>Pe dinăuntru și pe dinafară:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Buclă', 'la spate, pentru tras pe picior.'), ('Talpă', 'din cauciuc, cu sistemul Geox Respira.'))
  + '<p>Pe site, numerele 36-39 merg la adolescente, cam de la 12 ani în sus.</p>',
  [('model', 'Geox Bocanci copii culoarea bordo'), ('sintetic', 'confecționat din material sintetic'), ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'),
   ('neizolat', 'Izolare: neizolat'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('șiret, fermoar', 'Model cu siret cu fermoar lateral'), ('călcâi', 'Contorul de călcâi rigid'), ('vârf', 'Cutie rotunda, intarita'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('talpă', 'Talpa exterioară din cauciuc'), RESPIRA],
  {'Model': 'Geox (bocanci)', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'neizolați, șiret și fermoar lateral, Geox Respira', 'Cod produs': ''})

w(12375,
  f'<p>Bocancii {GEOX} gri sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} izolați, cu aspect de piele întoarsă, pentru zilele reci. Interiorul e textil, iar talpa are sistemul Geox Respira, în trei straturi cu perforări.</p>'
  '<p>Se închid cu fermoar, deci copilul îi încalță repede, fără șireturi de legat. Vârful e rotund și lasă loc degetelor, deci bocancul merge și la un picior mai plin.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'material sintetic.'), ('Interior', 'textil.'), ('Talpă', 'din gumă.'))
  + '<p>Numerele 26-35 se potrivesc copiilor de 3-11 ani, aproximativ.</p>',
  [('model', 'Geox Bocanci copii culoarea gri'), ('izolat', 'Model izolat'), ('piele întoarsă', 'Model confectionat din piele intoarsa'), ('interior', 'Interior textil'), RESPIRA,
   ('fermoar', 'Incheiere cu fermoar'), ('vârf', 'Varf rotund'), ('parte de sus', 'Gamba: Material sintetic'), ('talpă', 'Talpa din guma')],
  {'Model': 'Geox (bocanci)', 'Material': 'sintetic, interior textil, talpă din gumă', 'Caracteristici': 'izolați, fermoar, Geox Respira', 'Cod produs': ''},
  notes=['Magazinul spune „piele întoarsă” în descriere, dar compoziția dă material sintetic (imitație de piele); am scris „aspect de piele întoarsă”.'])
