import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
BIO = A('/brand/biomecanics/', 'Biomecanics')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(8573,
  f'<p>{GEOX} GISLI sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} verzi, din imitație de piele și material textil, cu tehnologia Geox Respira™. Magazinul îi descrie ca model pentru joaca de zi cu zi și pentru ținute de oraș.</p>'
  '<p>Au șireturi elastice și arici, deci pantoful se strânge pe picior fără nod, iar gulerul rigidizat stă fix în jurul gleznei.</p>'
  '<p>Pentru picioarele mici, construcția e solidă:</p>'
  + L(('Talpă', 'din cauciuc.'), ('Contrefort', 'rigidizat.'), ('Branț', 'detașabil.'), ('Interior', 'căptușit cu material sintetic și textil.'))
  + '<p>Pe site sunt numerele 24-27, pentru copii în jur de 2-4 ani.</p>',
  [('model', 'Geox GISLI sneakers copii verde B551NA.05410'), ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia Geox Respira'),
   ('utilizare', 'pentru ținutele urbane și pentru joaca de zi cu zi'), ('șireturi', 'Șireturile elastice'), ('arici', 'Închiderea cu velcro'), ('guler', 'Gulerul rigidizat'),
   ('talpă', 'Talpa de cauciuc'), ('contrefort', 'Contrefortul rigidizat'), ('branț', 'Branțurile detașabile'), ('interior', 'Interiorul căptușit cu material sintetic și textil')],
  {'Model': 'Geox GISLI', 'Material': 'imitație de piele și textil, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira™, șireturi elastice și arici, branț detașabil', 'Cod produs': 'B551NA.05410'})

w(8578,
  f'<p>{GEOX} propune pentru copiii mari acești {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi pentru băieți")} bej, din material sintetic, textil și piele întoarsă, cu membrana Amphibiox®, care protejează atât talpa, cât și partea de sus. Sunt pantofi pentru zilele cu ploaie de toamnă și de primăvară.</p>'
  '<p>Vârful e rotund, iar interiorul textil. Numerele mari, de la 36 la 39, îi fac potriviți, de obicei, copiilor de la 12 ani în sus.</p>'
  '<p>Tehnologiile Geox din model:</p>'
  + L(('Amphibiox®', 'membrană respirabilă și impermeabilă.'), ('Geox Respira', 'talpă în trei straturi, cu perforații.'), ('Talpă', 'din gumă.')),
  [('model', 'Pantofi copii culoarea bej'), ('material', 'combinatia materialului sintetic, textil cu pielea naturala'), ('piele întoarsă', 'Piele intoarsa'),
   ('Amphibiox', 'Tehnologia Amphibiox'), ('membrană', 'protejeaza atat talpa exterioara, cat si cea superioara'), ('nepermeabil', 'Membrana special respirabila si nepermeabila'),
   ('Respira', 'talpei in trei straturi cu sistemul de perforari'), ('vârf', 'Varf rotund'), ('interior', 'Interior textil'), ('talpă', 'Talpa din guma')],
  {'Model': 'Geox, pantofi', 'Material': 'sintetic, textil și piele întoarsă, interior textil, talpă din gumă', 'Caracteristici': 'membrană Amphibiox®, Geox Respira', 'Cod produs': ''})

w(8606,
  f'<p>{A("/brand/reima/", "Reima")} Astelu în varianta portocalie sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} ușori, din material textil, cu talpă din cauciuc. Șireturile elastice și gaica de la spate îi ajută pe copii să se încalțe singuri.</p>'
  '<p>Partea de sus ajunge până la gleznă, cu guler ușor întărit, iar contrafortul e doar ușor rigidizat, așa că pantoful rămâne flexibil.</p>'
  '<p>Pe scurt, din ce e făcut:</p>'
  + L(('Exterior', 'material textil.'), ('Căptușeală', 'textilă.'), ('Talpă', 'din cauciuc.'))
  + '<p>Modelul are numere de la 22 până la 40, deci se găsește atât pentru cei mici, de la aproximativ 1 an, cât și pentru copiii mari.</p>',
  [('model', 'Reima Astelu sneakers copii portocalii 5400066B'), ('textil', 'Partea superioară din material textil'), ('talpă', 'Talpa din cauciuc'),
   ('șireturi', 'Șireturile elastice facilitează încălțarea'), ('gaică', 'Gaica practică de la spate facilitează încălțarea autonomă'),
   ('gleznă', 'Construcția părții superioare până la nivelul gleznei'), ('guler', 'Gulerul pantofului este ușor întărit'), ('contrafort', 'Contrafort ușor rigidizat'),
   ('căptușeală', 'Căptușeala textilă')],
  {'Model': 'Reima Astelu', 'Material': 'textil, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'șireturi elastice, gaică la spate, guler ușor întărit', 'Cod produs': '5400066B'})

w(8608,
  f'<p>{BIO} 262165 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} în culoarea albastru, din material textil și sintetic, ușori, pentru primăvară, vară și toamnă. Talpa e din cauciuc, flexibilă și plată.</p>'
  '<p>Branțul detașabil are imprimat un ghid de mărime: îl scoți, pui piciorul copilului pe el și vezi imediat dacă pantoful mai are loc. Contrefortul e moale, iar partea de sus urcă până la gleznă.</p>'
  '<p>Copilul își poate pune singur pantofii:</p>'
  + L(('Închidere', 'arici.'), ('Căptușeală', 'textilă.'), ('Material', 'textil și sintetic.'))
  + '<p>Mărimile 19-23 se potrivesc de obicei copiilor de 1-3 ani.</p>',
  [('cod', '262165'), ('culoare', 'Sneakers pentru copii albastru 262165'), ('material', 'Partea superioară din material textil și sintetic'),
   ('sezon', 'ideal pentru primăvară, vară și toamnă'), ('talpă', 'Talpa flexibilă din cauciuc cu profil plat'),
   ('branț', 'Branțul detașabil cu imprimeu pentru verificarea mărimii'), ('contrefort', 'Contrefortul moale'), ('gleznă', 'Construcția părții superioare până la gleznă'),
   ('arici', 'Închiderea practică cu velcro'), ('autonom', 'încălțarea și descălțarea rapidă și autonomă'), ('căptușeală', 'Interiorul căptușit cu material textil')],
  {'Model': 'Biomecanics 262165', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'branț cu ghid de mărime, arici, talpă flexibilă', 'Cod produs': '262165'})

w(8629,
  f'<p>{A("/brand/wheat/", "Wheat")} 7350-972R este un compleu de ploaie roz, cu o {A("/categorie/geci-jachete/", "geacă de ploaie pentru fete")} și pantaloni cu bretele, din poliester cu poliuretan pe bază de apă și impermeabilitate de 8000 mm. Nu are izolație, deci e pentru ploile de primăvară și toamnă.</p>'
  f'<p>Bretelele pantalonilor se reglează, iar lamelele de la călcâi țin crăcii jos, peste {A("/categorie/ghete-cizme/", "ghetele și cizmele pentru fete")}, ca să nu urce când copilul sare prin bălți.</p>'
  '<p>Geaca are câteva detalii pentru ploaie:</p>'
  + L(('Glugă', 'detașabilă.'), ('Mâneci', 'cu elastic la capăt.'), ('Închidere', 'fermoar.'), ('Margine', 'cu manșetă.'))
  + '<p>Compleul vine în mărimile 98-128, cam pentru 3-8 ani.</p>',
  [('cod', '7350-972R GRS'), ('compleu', 'Compleu pentru copii'), ('culoare', 'culoarea roz'), ('material', '55% Poliester , 45% Poliuretan pe bază de apă'),
   ('impermeabilitate', 'Impermeabilitate: 8000 mm/m2/24h'), ('neizolat', 'Izolare: neizolat'), ('bretele', 'Model cu bretele nedetasabile, reglabile'),
   ('lamele', 'Lamelele pentru călcâi împiedică picioarele să alunece în sus'), ('glugă', 'Gluga detasabila'), ('mâneci', 'Mâneci finisate cu o coadă elastică'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('margine', 'Marginea de jos finisata cu manseta')],
  {'Model': 'Wheat 7350-972R', 'Material': '55% poliester, 45% poliuretan pe bază de apă', 'Caracteristici': 'compleu de ploaie: geacă și pantaloni cu bretele, impermeabilitate 8000 mm, glugă detașabilă', 'Cod produs': '7350-972R'},
  comp={'slug': '/categorie/ghete-cizme/', 'motiv': 'compleu de ploaie, se poartă cu cizme'},
  notes=['Pe site e listat ca geacă; magazinul vinde un compleu de ploaie (geacă + pantaloni cu bretele).'])

w(8632,
  f'<p>{BIO} 261240 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, din imitație de piele și material textil, cu talpă Flexi Lite, ușoară și flexibilă. Modelul vine din programul Biomecanics Podology Partnership, făcut împreună cu podologi, pentru copiii activi.</p>'
  '<p>Închiderea cu arici se ajustează repede, iar gulerul ușor întărit cuprinde glezna fără să o strângă.</p>'
  '<p>Talpa și interiorul:</p>'
  + L(('Talpă', 'din spumă, Flexi Lite.'), ('Călcâi', 'întărit.'), ('Branț', 'detașabil, din material textil.'), ('Interior', 'textil.'))
  + '<p>Numerele de pe site, 28-34, corespund, în mare, vârstei de 4-11 ani.</p>',
  [('cod', '261240'), ('culoare', 'bleumarin 261240'), ('material', 'Partea superioară din imitație de piele și material textil'), ('Flexi Lite', 'Talpa Flexi Lite'),
   ('Podology', 'Tehnologia Biomecanics Podology Partnership'), ('podologi', 'creată în colaborare cu podologi'), ('activi', 'băieții activi'),
   ('arici', 'Sistemul de închidere cu arici'), ('guler', 'Gulerul superior ușor întărit'), ('talpă', 'Talpa din spumă'), ('călcâi', 'Călcâiul întărit'),
   ('branț', 'Branțurile detașabile din material textil'), ('interior', 'Interiorul din material textil')],
  {'Model': 'Biomecanics 261240', 'Material': 'imitație de piele și textil, interior textil, talpă din spumă', 'Caracteristici': 'Flexi Lite, arici, branț detașabil, Podology Partnership', 'Cod produs': '261240'})

w(8638,
  f'<p>{A("/brand/kenzo-kids/", "Kenzo Kids")} K60631 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de blugi unisex")}, albastră, din denim 100% bumbac, fără izolație și fără căptușeală. E o geacă de tranziție pentru copiii mici, de purtat primăvara și toamna.</p>'
  '<p>Croiala e simplă, iar manșetele se încheie, deci mânecile se strâng la încheietură și pe un copil cu brațe subțiri.</p>'
  '<p>Ca orice geacă de blugi, se încheie în față:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'două la piept, cu nasturi.'), ('Guler', 'clasic.'), ('Glugă', 'nu are.'))
  + '<p>Mărimile 86-108 se potrivesc copiilor de aproximativ 1-5 ani.</p>',
  [('cod', 'K60631'), ('culoare', 'albastru'), ('denim', 'denim de bumbac'), ('bumbac', '100% Bumbac'), ('neizolat', 'Model neizolat'), ('necăptușit', 'Captuseala: necaptusit'),
   ('croială', 'Tăiere simplă'), ('manșete', 'Mansete incheiate'), ('buton', 'Închiderea convenabilă cu buton'), ('buzunare', 'Două buzunare la piept cu nasturi'),
   ('guler', 'Model cu guler'), ('fără glugă', 'Gluga: fara gluga')],
  {'Model': 'Kenzo Kids K60631', 'Material': 'denim, 100% bumbac', 'Caracteristici': 'fără izolație și căptușeală, nasturi, două buzunare la piept, manșete încheiate', 'Cod produs': 'K60631'},
  notes=['Titlul de pe site nu are culoare; pagina magazinului dă albastru.'])

w(8641,
  f'<p>{TH} are aici un {A("/categorie/bebe-imbracaminte-pantaloni-treninguri/", "trening pentru bebeluși")} bleumarin, din tricot subțire și flexibil, cu bluză cu mânecă lungă și pantaloni. Bumbacul e cel puțin pe jumătate organic, iar compoziția are 5% elastan.</p>'
  '<p>Fasonul e drept, iar pantalonii au șnururi în talie, deci se strâng pe un bebeluș mai slab; mânecile și picioarele se termină cu manșete.</p>'
  '<p>Pentru îmbrăcat și dezbrăcat des, contează:</p>'
  + L(('Decolteu', 'rotund.'), ('Buzunare', 'oblice.'), ('Material', '95% bumbac, 5% elastan, cu imprimeu.'))
  + '<p>Treningul se găsește în mărimile 56-92, de la aproximativ o lună până la 2 ani.</p>',
  [('tip', 'Compleu de trening pentru copii'), ('culoare', 'culoarea albastru marin'), ('tricot', 'Material tricot flexibil si subtire'),
   ('organic', 'cel putin 50% bumbac organic'), ('compoziție', '95% Bumbac, 5% Elastan'), ('fason', 'Fason drept'), ('mânecă', 'Maneca lunga'),
   ('șnururi', 'In talie snururi'), ('manșetă', 'Finisaj din manseta'), ('decolteu', 'Decolteu rotund'), ('buzunare', 'Buzunare oblice'), ('print', 'Model: print')],
  {'Model': 'Tommy Hilfiger, trening bebe', 'Material': '95% bumbac (cel puțin 50% organic), 5% elastan', 'Caracteristici': 'bluză și pantaloni, șnur în talie, manșete, buzunare oblice', 'Cod produs': ''},
  varsta_txt='1 lună - 2 ani')

w(8658,
  f'<p>{BIO} 261256 sunt ghete înalte de iarnă, verzi, din material sintetic și textil, puse pe site la {A("/categorie/unisex-incaltaminte-pantofi/", "încălțăminte de iarnă unisex")}. Membrana BioTEX ține interiorul uscat, iar căptușeala păstrează căldura în zilele friguroase.</p>'
  '<p>Se închid cu arici, care se strâng ușor pe picior, iar branțul textil se scoate, ca să verifici lungimea piciorului direct pe el.</p>'
  '<p>Pentru zăpadă și frig, ghetele mai au:</p>'
  + L(('Talpă', 'din cauciuc, cu bandă de rulare.'), ('Vârf și călcâi', 'vârf rigidizat, călcâi întărit.'), ('Tehnologie', 'Biomecanics Podology Partnership, dezvoltată cu podiatri.'))
  + '<p>Pe site sunt numerele 24-34, cam pentru 2-11 ani.</p>',
  [('model', 'Ghetele de iarnă pentru copii Biomecanics 261256'), ('culoare', 'verde 261256'), ('înalte', 'încălțăminte înaltă'), ('zile friguroase', 'zilele friguroase'),
   ('BioTEX', 'Membrana BioTEX'), ('uscăciune', 'menținerea uscăciunii'), ('căptușeală', 'Interior căptușit contribuie la menținerea căldurii'),
   ('arici', 'Sistem de închidere cu arici'), ('branț', 'Branț detașabil din material textil'), ('talpă', 'Talpă de cauciuc cu bandă de rulare'),
   ('vârf, călcâi', 'Vârf rigidizat și călcâi întărit'), ('Podology', 'Tehnologia Biomecanics Podology Partnership'), ('podiatri', 'colaborării cu podiatri')],
  {'Model': 'Biomecanics 261256', 'Material': 'sintetic și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'ghete de iarnă, membrană BioTEX, căptușeală caldă, arici', 'Cod produs': '261256'},
  notes=['Pe site e în categoria Pantofi; produsul e ghetă înaltă de iarnă.'])

w(8664,
  f'<p>{TH} T3A5-34016 sunt {A("/categorie/ghete-cizme/", "botine pentru fete")} negre, în stil Jodhpur, fără izolație, deci de purtat toamna și primăvara. Talpa e din cauciuc, cu caneluri.</p>'
  '<p>Au inserție elastică, fermoar lateral și arici: botina se deschide ușor la încălțat, iar elasticul o așază pe gleznă, fie ea mai subțire sau mai plină.</p>'
  '<p>La încălțat și la mers ajută:</p>'
  + L(('Bucle', 'pentru tras botina pe picior.'), ('Branț', 'conturat.'), ('Vârf', 'rotund, întărit.'), ('Călcâi', 'contor rigid.'))
  + '<p>Numerele 35-40 le fac potrivite, de regulă, copiilor de la 10 ani în sus.</p>',
  [('cod', 'T3A5-34016'), ('culoare', 'culoarea negru'), ('Jodhpur', 'Ghete Jodhpur'), ('neizolat', 'Izolare: neizolat'), ('talpă', 'Talpa exterioară din cauciuc cu caneluri'),
   ('elastic', 'Inserția elastică asigură o potrivire individuală'), ('fermoar, arici', 'Fermoarul lateral convenabil și închiderea cu velcro'),
   ('bucle', 'Buclele facilitează glisarea pantofului pe picior'), ('branț', 'Brantul conturat'), ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid')],
  {'Model': 'Tommy Hilfiger T3A5-34016', 'Material': 'imitație de piele, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'stil Jodhpur, inserție elastică, fermoar lateral și arici, neizolate', 'Cod produs': 'T3A5-34016'})
print('lot 5 scris')
