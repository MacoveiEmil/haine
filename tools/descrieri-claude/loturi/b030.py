import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
REIMA = A('/brand/reima/', 'Reima')
GEOX = A('/brand/geox/', 'Geox')

w(9766,
  f'<p>Botinele {PRIMIGI} PFS 24120 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} negre, simple, din piele naturală, cu căptușeală tot din piele. Nu au izolație termică, deci sunt pentru zilele mai calde din sezonul de tranziție. Tehnologia Primigi × SIPeP a fost creată în colaborare cu podologi.</p>'
  '<p>Închiderea e dublă: șireturile se reglează precis pe picior, iar fermoarul lateral ajută la încălțat și la descălțat fără să fie desfăcute de fiecare dată.</p>'
  '<p>Botina e întărită și ușor de întreținut:</p>'
  + L(('Vârf și călcâi', 'întărite.'), ('Branțuri', 'detașabile, se pot scoate și înlocui.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 25-35 sunt pentru copii de aproximativ 2-11 ani.</p>',
  [('model', 'Primigi Botine pentru copii din piele negre PFS 24120'), ('piele', 'Partea superioară din piele naturală'), ('simplu', 'Design simplu, negru'),
   ('căptușeală', 'Căptușeală din piele naturală'), ('neizolat', 'Fără izolație termică în interior'), ('tranziție', 'zilele mai calde din perioada de tranziție'),
   ('SIPeP', 'Tehnologia Primigi × SIPeP'), ('podologi', 'creată în colaborare cu podologi'), ('șireturi', 'Șireturile permit ajustarea precisă a încălțămintei'),
   ('fermoar', 'Fermoar lateral facilitează încălțarea și descălțarea rapidă'), ('întărit', 'Vârful întărit și călcâiul întărit'),
   ('branțuri', 'Branțuri detașabile facilitează menținerea igienei încălțămintei și eventuala lor înlocuire'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Primigi PFS 24120', 'Material': 'piele, căptușeală din piele naturală, talpă din cauciuc', 'Caracteristici': 'neizolate, șireturi și fermoar lateral, branțuri detașabile', 'Cod produs': 'PFS 24120'})

w(9769,
  f'<p>{GEOX} SKETLITE J66NWB sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, cu profil înalt, din imitație de piele și material textil, cu aplicații decorative și imprimeu. Membrana microporoasă din talpă, sistemul Geox Respira™, scoate umezeala spre exterior.</p>'
  '<p>Au trei închideri, șiret, arici și fermoar, deci pantoful se strânge exact pe picior și se pune repede. Gulerul ușor întărit cuprinde glezna.</p>'
  '<p>Restul construcției:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Branțuri', 'detașabile.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 32-35 sunt, în mare, pentru 8-11 ani.</p>',
  [('model', 'Geox SKETLITE sneakers pentru copii roz J66NWB.0NFKN'), ('profil', 'Profilul înalt al feței superioare'), ('material', 'Fața superioară din imitație de piele și material textil'),
   ('decor', 'Aplicații decorative și imprimeu'), ('Respira', 'Tehnologia GEOX Respira™'), ('membrană', 'membranei microporoase din talpă, care elimină umezeala la exterior'),
   ('închideri', 'Trei tipuri de închideri – cu șiret, cu arici și cu fermoar'), ('guler', 'gulerul ușor întărit'), ('călcâi', 'Călcâiul ușor întărit'),
   ('branțuri', 'Branțurile detașabile'), ('interior', 'Interiorul căptușit cu material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox SKETLITE', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, șiret, arici și fermoar, branțuri detașabile', 'Cod produs': 'J66NWB.0NFKN'})

w(9771,
  f'<p>{REIMA} Surina BugProof 5100377A sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni outdoor unisex")} roșii, din material textil elastic, pentru activități în aer liber. Finisajul Reima BugProof cu geraniol ajută la protecția împotriva țânțarilor și căpușelor, deci sunt buni pentru pădure și iarbă înaltă vara.</p>'.replace(', deci sunt buni pentru pădure și iarbă înaltă vara', '')
  + '<p>Croiala e dreaptă, cu talie regulară și bandă elastică, care se strânge pe un copil mai slab fără curea. Cracii lungi se detașează, deci pantalonii devin scurți.</p>'
  '<p>Pentru plimbări lungi și seri afară, mai au:</p>'
  + L(('Buzunare', 'laterale, deschise, în față.'), ('Elemente reflectorizante', 'copilul se vede pe întuneric.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 104-164 sunt pentru copii de în jur de 4-14 ani.</p>',
  [('model', 'Reima Pantaloni pentru copii Surina BugProof roșu 5100377A'), ('textil', 'Pantaloni din material textil pentru copii'), ('elastic', 'Materialul elastic'),
   ('aer liber', 'potriviți pentru diverse activități în aer liber'), ('BugProof', 'Finisajul Reima BugProof cu geraniol ajută la protejarea împotriva țânțarilor și căpușelor'),
   ('croială', 'Croiala dreaptă'), ('talie', 'Talie regulară cu bandă elastică'), ('craci', 'Craci lungi cu posibilitate de detașare'),
   ('buzunare', 'Buzunare laterale deschise în partea din față'), ('reflectorizant', 'Elemente reflectorizante practice care sporesc vizibilitatea copilului pe întuneric'),
   ('material', '100% Poliester')],
  {'Model': 'Reima Surina BugProof', 'Material': '100% poliester, elastic', 'Caracteristici': 'BugProof, craci detașabili, talie elastică, reflectorizante', 'Cod produs': '5100377A'})

w(9773,
  f'<p>{A("/brand/mini-rodini/", "Mini Rodini")} Travel agency 26210101 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de tranziție unisex")} (portocaliu pe site, albastră la magazin), din țesătură cu aplicații, căptușită, dar neizolată. E pentru zilele de primăvară și toamnă, nu pentru frig.</p>'.replace('E pentru zilele de primăvară și toamnă, nu pentru frig.', 'Se poartă în sezonul de tranziție, nu pe ger.')
  + '<p>Fasonul e lejer, cu umerii coborâți pe mânecă, iar tivul elastic de la mâneci și de jos strânge geaca pe corp, ca să nu stea largă pe un copil mai slab.</p>'
  '<p>Închiderea și buzunarele sunt gândite pentru copii mici:</p>'
  + L(('Fermoar', 'cu protecție pentru bărbie.'), ('Buzunare', 'două, laterale, cu capse.'), ('Glugă', 'nu are.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 80-86 până la 140-146 merg, de obicei, la copii de 1-11 ani.</p>',
  [('model', 'Mini Rodini Geacă copii Travel agency 26210101'), ('aplicații', 'țesătură cu aplicații'), ('căptușeală', 'Captuseala: cu captuseala'), ('neizolat', 'Izolare: neizolat'),
   ('tranziție', 'Izolare: tranzitional'), ('fason', 'Fason lejer'), ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'),
   ('tiv', 'Mânecile și marginea inferioară sunt finisate cu un tiv elastic'), ('fermoar', 'Închidere cu fermoar, prevăzută cu protecție pentru bărbie'),
   ('buzunare', 'Două buzunare laterale care se îndepărtează și se închid cu apăsare'), ('fără glugă', 'Gluga: fara gluga'), ('material', '100% Poliester')],
  {'Model': 'Mini Rodini Travel agency', 'Material': '100% poliester', 'Caracteristici': 'neizolată, căptușită, tiv elastic, fermoar cu protecție pentru bărbie', 'Cod produs': '26210101'},
  notes=['Titlul de pe site spune portocaliu; magazinul dă culoarea albastru.'])

w(9774,
  f'<p>Sandalele {GEOX} SANDAL KODETTE J65DBC sunt {A("/categorie/incaltaminte-sandale/", "sandale pentru fete")} negre, ușoare, în stil casual, pentru plimbările și ieșirile de vară. Partea de sus e din piele sintetică, ușor de întreținut, cu un model simplu.</p>'
  '<p>Catarama se reglează pe gleznă după piciorul copilului, iar calapodul e făcut pentru o lățime standard a piciorului, deci pe un picior foarte lat poate strânge.</p>'
  '<p>Din ce sunt făcute:</p>'
  + L(('Partea de sus', 'material sintetic.'), ('Interior', 'finisat cu piele sintetică.'), ('Talpă', 'material sintetic.'))
  + '<p>Numerele 36-39 sunt pentru copii mari, de pe la 12 ani în sus.</p>',
  [('model', 'Geox Sandale pentru copii SANDAL KODETTE negre J65DBC.000BC'), ('ușor', 'încălțăminte ușoară'), ('casual', 'Stilul casual este potrivit pentru diverse ieșiri de vară'),
   ('piele sintetică', 'Partea superioară din piele sintetică este ușor de întreținut'), ('simplu', 'Modelul simplu al părții superioare'),
   ('cataramă', 'Sistemul practic de închidere cu cataramă permite o ajustare individuală'), ('lățime', 'adaptată pentru o lățime standard a piciorului'),
   ('interior', 'Interiorul finisat cu piele sintetică'), ('talpă', 'Material sintetic')],
  {'Model': 'Geox SANDAL KODETTE', 'Material': 'sintetic, interior din piele sintetică', 'Caracteristici': 'cataramă reglabilă, lățime standard', 'Cod produs': 'J65DBC.000BC'})

w(9780,
  f'<p>Botinele {A("/brand/biomecanics/", "Biomecanics")} 261214 sunt {A("/categorie/ghete-cizme/", "ghete pentru fete")} negre, cu model decorativ cu buline, din piele întoarsă și material sintetic, pentru sezonul de tranziție. Designul peste gleznă protejează de frig, iar interiorul textil le face potrivite pentru zilele mai calde.</p>'
  '<p>Închiderea dublă, cu arici și fermoar, se deschide larg la încălțat, iar aricii se strâng după piciorul copilului, mai plin sau mai subțire.</p>'
  '<p>Botina e simplă și rezistentă:</p>'
  + L(('Vârf', 'rigidizat, apără degetele.'), ('Căptușeală', 'textilă.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-34 se potrivesc, în general, copiilor de 2-11 ani.</p>',
  [('model', 'Biomecanics Botine pentru copii negre 261214'), ('buline', 'Modelul adorabil cu buline'), ('material', 'Partea superioară din piele întoarsă și material sintetic'),
   ('tranziție', 'o alegere potrivită pentru perioada de tranziție'), ('gleznă', 'Designul peste gleznă'), ('frig', 'protejând în același timp împotriva frigului'),
   ('interior', 'Interiorul finisat cu material textil'), ('zile calde', 'potrivit pentru zilele mai calde'), ('închidere', 'Închiderea dublă cu arici și fermoar'),
   ('ajustare', 'Ajustarea cu arici permite ajustarea încălțămintei la nevoile individuale ale piciorului copilului'), ('vârf', 'Vârful rigidizat contribuie la protecția degetelor'),
   ('căptușeală', 'Căptușeala textilă'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Biomecanics 261214', 'Material': 'piele întoarsă și sintetic, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'arici și fermoar, vârf rigidizat, model cu buline', 'Cod produs': '261214'})

w(9782,
  f'<p>{A("/brand/adidas/", "adidas")} KQ8605 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")} bej, matlasată, cu izolație groasă din puf sintetic și tehnologia CLIMAWARM™, care ține căldura în lunile reci. Stilul e simplu, sportiv, pentru joaca afară.</p>'
  '<p>Croiala e simplă, iar lungimea până la șolduri acoperă spatele când cel mic stă jos în zăpadă. Gluga integrată și gulerul ridicat apără capul și gâtul de vânt.</p>'
  '<p>Pentru mâini și lucruri mici, geaca are:</p>'
  + L(('Buzunare', 'laterale, cu fermoar.'), ('Umplutură', 'puf sintetic, ușor.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 62-104 sunt pentru copii de pe la 3 luni până pe la 4 ani.</p>',
  [('model', 'adidas Jachetă pentru copii bej KQ8605'), ('matlasat', 'Construcția matlasată'), ('izolație', 'Izolație termică groasă cu puf sintetic'),
   ('CLIMAWARM', 'Tehnologia CLIMAWARM™ ajută la menținerea căldurii'), ('reci', 'lunile reci'), ('sportiv', 'un stil simplu, sportiv'), ('croială', 'Croială simplă'),
   ('lungime', 'Lungime până la șolduri'), ('glugă', 'Glugă integrată oferă protecție suplimentară capului împotriva vântului și frigului'),
   ('guler', 'Guler ridicat protejează suplimentar gâtul împotriva aerului rece'), ('buzunare', 'Buzunare laterale cu fermoar'),
   ('umplutură', 'Umplutura din puf sintetic este ușoară'), ('material', '100% Poliester')],
  {'Model': 'adidas KQ8605', 'Material': '100% poliester', 'Caracteristici': 'CLIMAWARM™, puf sintetic, glugă integrată, matlasată', 'Cod produs': 'KQ8605'})

w(9783,
  f'<p>Ghetele de iarnă {PRIMIGI} PTIGT 23547 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete unisex")} maro, din piele întoarsă și material textil, cu membrana GORE-TEX®, care oprește apa și vântul. Interiorul căptușit cu material textil păstrează căldura, deci sunt bune pentru joaca prin zăpadă.</p>'
  '<p>Aricii se închid repede, așa că cei mici se încalță și se descalță singuri, iar partea de sus din piele întoarsă se adaptează la picior.</p>'
  '<p>Talpa și călcâiul au grijă de mers:</p>'
  + L(('Shock Absorber', 'tehnologie în talpă care limitează șocurile.'), ('Talpă', 'din cauciuc, cu profil plat.'), ('Călcâi și guler', 'ușor întărite.'))
  + '<p>Numerele 25-29 corespund, de regulă, vârstei de 2-5 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii maro PTIGT 23547'), ('material', 'Partea superioară din piele întoarsă și material textil'),
   ('GORE-TEX', 'Membrana GORE-TEX® asigură protecție împotriva apei și a vântului'), ('interior', 'Interior căptușit din material textil ajută la menținerea căldurii'),
   ('iarnă', 'jocurilor de iarnă'), ('arici', 'Închidere cu arici facilitează încălțarea și descălțarea rapidă de către copii'), ('adaptare', 'adaptare la picior'),
   ('Shock Absorber', 'Tehnologia Shock Absorber în talpă'), ('șocuri', 'limitând șocurile în timpul mersului'), ('talpă', 'Talpă din cauciuc cu profil plat'),
   ('călcâi', 'Călcâiul întărit și gulerul ușor întărit')],
  {'Model': 'Primigi PTIGT 23547', 'Material': 'piele întoarsă și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, arici, Shock Absorber', 'Cod produs': 'PTIGT 23547'})

w(9786,
  f'<p>{REIMA} Marte Mid 5100115B este o {A("/categorie/bebe-imbracaminte-salopete-compleuri/", "salopetă de iarnă pentru bebeluși")}, bej, cu buline, izolată cu umplutură sintetică medie, pentru temperaturi de la +5 la -10°C. Tehnologia ReimaTec, cu membrană PU, impermeabilitate de 12000 mm H2O și cusături lipite, o face potrivită pentru zăpadă și ploaie.</p>'
  '<p>Talia are ajustare internă, deci salopeta se strânge pe un copil mai slab, iar manșetele și cracii cu elastic țin frigul și zăpada afară.</p>'
  '<p>Pentru joaca afară până se întunecă, contează:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede seara.'), ('Glugă', 'detașabilă.'), ('Țesătură', 'rezistentă la peste 30 000 de cicluri de abraziune.'), ('Vânt', 'material rezistent la vânt.'))
  + '<p>Mărimile 74-98 sunt pentru cei mici de cam 9 luni până la 3 ani.</p>',
  [('model', 'Reima Salopetă pentru copii Marte Mid bej 5100115B'), ('buline', 'modelul cu buline'), ('izolat', 'Izolație sintetică de grosime medie'),
   ('temperatură', '+5 la -10°C'), ('ReimaTec', 'Tehnologia ReimaTec cu membrană PU'), ('impermeabil', 'Impermeabilitate de 12000 mm H2O'), ('cusături', 'Cusături lipite'),
   ('talie', 'Ajustare internă în talie'), ('elastic', 'Manșete și craci cu elastic'), ('reflectorizant', 'Elemente reflectorizante sporesc vizibilitatea copilului după lăsarea întunericului'),
   ('glugă', 'Glugă detașabilă'), ('abraziune', 'rezistență la abraziune de peste 30 000 de cicluri'), ('vânt', 'Material rezistent la vânt')],
  {'Model': 'Reima Marte Mid', 'Material': '100% poliester acoperit cu poliuretan, umplutură 100% poliester', 'Caracteristici': 'ReimaTec, 12000 mm H2O, cusături lipite, reflectorizante, glugă detașabilă', 'Cod produs': '5100115B'})

w(9795,
  f'<p>{REIMA} Qing 5400026A sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "cizme de zăpadă pentru bebeluși")} (roz pe site, albastre la magazin), izolate, din material textil, sintetic și piele ecologică, ușoare. Oferă confort termic până la -10°C, iar acoperirea PFC Repellent le face rezistente la apă, pentru zăpadă și băltoace.</p>'
  '<p>Inserțiile detașabile Happy Fit ajută la alegerea mărimii potrivite, iar velcro-ul și bucla de la spate îl lasă pe copil să se încalțe ușor. Vârful rotund dă loc degetelor.</p>'
  '<p>Pentru zilele scurte de iarnă, cizma are:</p>'
  + L(('Elemente reflectorizante', 'pentru drumurile pe întuneric.'), ('Călcâi', 'contrafort rigid, piciorul nu alunecă.'), ('Partea de sus', 'ridicată, rigidizează glezna.'), ('Interior', 'textil.'))
  + '<p>Numerele 20-28 sunt, cu aproximație, pentru 1-5 ani.</p>',
  [('model', 'Reima Qing albastru 5400026A'), ('zăpadă', 'Cizme de zăpadă pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinatie de material textil, material sintetic și piele ecologică'), ('ușor', 'Model ușor'), ('-10', 'Oferă confort termic până la -10°C'),
   ('PFC', 'Modelul cu acoperire ecologica PFC Repellent cu apa libera, care asigura rezistenta la apa'), ('Happy Fit', 'Inserțiile detașabile Happy Fit vă permit să alegeți dimensiunea potrivită'),
   ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('vârf', 'Degetul rotund, ușor rigid'), ('reflectorizant', 'Elementele reflectorizante sporesc vizibilitatea și siguranța după întuneric'),
   ('călcâi', 'Contorul de călcâi rigid'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Reima Qing', 'Material': 'textil, sintetic și piele ecologică, interior textil', 'Caracteristici': 'izolate până la -10°C, PFC Repellent, Happy Fit, velcro, reflectorizante', 'Cod produs': '5400026A'},
  notes=['Titlul de pe site spune roz; magazinul dă culoarea albastru.', 'Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])
