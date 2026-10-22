import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

ADI = A('/brand/adidas/', 'adidas')
WHEAT = A('/brand/wheat/', 'Wheat')

w(8791,
  f'<p>{A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IB0IB02168 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")}, neagră, matlasată și izolată cu umplutură sintetică, pentru temperaturile mai reci. Fibra REPREVE din material e făcută din sticle de plastic reciclate.</p>'
  '<p>Fasonul e drept, iar geaca e lungă, cu mâneci terminate cu manșetă; gulerul ridicat și gluga detașabilă acoperă gâtul și capul când e frig.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', 'poliester, cu căptușeală și umplutură din poliester.'), ('Bandă elastică', '97% poliester, 3% elastan.'))
  + '<p>Geaca se găsește în mărimile 128-176, de obicei pentru copii de 8-16 ani.</p>',
  [('cod', 'IB0IB02168'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat'), ('izolație', 'izolație sintetica'), ('matlasat', 'Matlasat'),
   ('temperaturi', 'temperaturi mai reci'), ('REPREVE', 'Fibra REPREVE este fabricata din sticle de plastic reciclate'), ('fason', 'Fason drept'),
   ('manșetă', 'Manecile finisate cu manseta'), ('glugă, guler', 'Gulerul ridicat și gluga detașabilă'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('material', 'Materialul de baza: 100% Poliester'), ('bandă', 'Banda elastica: 97% Poliester , 3% Elastan')],
  {'Model': 'Calvin Klein Jeans IB0IB02168', 'Material': '100% poliester, izolație sintetică, fibră REPREVE', 'Caracteristici': 'matlasată, glugă detașabilă, guler ridicat, fason drept', 'Cod produs': 'IB0IB02168'})

w(8800,
  f'<p>{A("/brand/primigi/", "Primigi")} PTIGT 23548 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi cu GORE-TEX pentru bebeluși")} și copii mici, roz, din piele întoarsă și material sintetic. Membrana GORE-TEX® oprește apa și vântul, deci pantofii merg de primăvara până toamna, inclusiv pe vreme umedă.</p>'
  '<p>Se închid cu arici și șireturi elastice, care se ajustează repede pe picior, iar vârful e rotund și întărit, ca să protejeze degetele la joacă.</p>'
  '<p>Ce mai are pantoful:</p>'
  + L(('Shock Absorber', 'sistem în talpă.'), ('Talpă', 'din cauciuc, flexibilă.'), ('Branț', 'detașabil, din material textil.'), ('Contrafort', 'rigidizat.'))
  + '<p>Numerele 20-29 se potrivesc în general copiilor de 1-5 ani.</p>',
  [('cod', 'PTIGT 23548'), ('culoare', 'Pantofi pentru copii roz'), ('material', 'Fața superioară, din piele întoarsă și material sintetic'),
   ('GORE-TEX', 'Membrana GORE-TEX® creează o barieră împotriva apei și vântului'), ('sezon', 'de la primăvară până toamna'),
   ('închidere', 'Închiderea cu arici , în combinație cu șireturile elastice'), ('vârf', 'Vârful rotund, întărit'), ('Shock Absorber', 'Sistemul Shock Absorber din talpă'),
   ('talpă', 'Talpă de cauciuc'), ('branț', 'Branțul detașabil din material textil'), ('contrafort', 'Contrafortul rigidizat')],
  {'Model': 'Primigi PTIGT 23548', 'Material': 'piele întoarsă și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, Shock Absorber, arici și șireturi elastice', 'Cod produs': '23548'})

w(8801,
  f'<p>{WHEAT} WF641-01 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")} bej, ușori, din piele întoarsă și material textil cu plasă, cu talpă din spumă EVA și cauciuc. Sunt adidași sport pentru joaca de zi cu zi și ținutele casual.</p>'
  '<p>Șireturile elastice au opritor, deci se strâng dintr-o tragere, fără nod; croiala urcă până la gleznă, iar contrefortul e ușor rigidizat.</p>'
  '<p>La interior, modelul e lucrat atent:</p>'
  + L(('Căptușeală', 'din bumbac organic.'), ('Branț', 'din piele naturală.'), ('Piele', 'cu certificat LWG.'), ('Exterior', 'piele întoarsă, textil și plasă.'))
  + '<p>Pe site sunt numerele 24-35, adică, cu aproximație, 2-11 ani.</p>',
  [('cod', 'Sneakers pentru copii bej WF641-01'), ('material', 'Partea superioară dintr-o combinație de piele întoarsă și material textil'), ('plasă', 'Plasa respirabilă'),
   ('talpă', 'Talpa exterioară din spumă EVA și cauciuc'), ('ușor', 'încălțăminte sport ușoară'), ('casual', 'ținutele casual și sportive'),
   ('șireturi', 'Șireturile elastice cu opritor'), ('gleznă', 'Croiala până la gleznă'), ('contrefort', 'Contrefortul ușor rigidizat'),
   ('bumbac organic', 'Căptușeala din bumbac organic'), ('branț', 'Piele naturală'), ('LWG', 'Pielea cu certificat LWG')],
  {'Model': 'Wheat WF641-01', 'Material': 'piele întoarsă și textil, căptușeală din bumbac organic, branț din piele', 'Caracteristici': 'șireturi elastice cu opritor, talpă EVA și cauciuc', 'Cod produs': 'WF641-01'})

w(8802,
  f'<p>{A("/brand/pinko/", "Pinko")} KFGB013 este o {A("/categorie/geci-jachete/", "geacă de iarnă pentru fete")}, neagră, izolată și căptușită, din poliamidă cu model, fără glugă. E pentru zilele reci, iar poliamida face materialul mai rezistent la purtare.</p>'
  '<p>Croiala e simplă, cu mâneci și margine finisate cu tăietură curată. Magazinul atrage atenția că mărimile sunt italiene, convertite la cele europene, deci merită verificat tabelul de mărimi înainte.</p>'
  '<p>Detaliile gecii:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Glugă', 'nu are.'), ('Material', '100% poliamidă și 100% poliester.'))
  + f'<p>Fără glugă, pe ger capul se acoperă separat, cu o piesă din {A("/categorie/caciuli-manusi-accesorii/", "căciulile și mănușile pentru fete")}. Mărimile de pe site, 128-164, sunt pentru copii de pe la 8 până pe la 14 ani.</p>',
  [('cod', 'KFGB013.C.NY023'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat cu captuseala'), ('material modelat', 'material modelat'),
   ('poliamidă', 'Poliamida asigură o durabilitate mai mare a produsului'), ('fără glugă', 'Gluga: fara gluga'), ('croială', 'Tăiere simplă'),
   ('mâneci', 'Mâneci și marginea inferioară finisate cu tăiere'), ('mărimi italiene', 'Dimensiunile disponibile sunt cele ale producatorul italian'),
   ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('material 1', 'Material 1: 100% Poliamida'), ('material 2', 'Material 2: 100% Poliester')],
  {'Model': 'Pinko KFGB013', 'Material': '100% poliamidă, 100% poliester', 'Caracteristici': 'izolată, căptușită, fără glugă, fermoar, buzunare cu fermoar', 'Cod produs': 'KFGB013.C.NY023'},
  comp={'slug': '/categorie/caciuli-manusi-accesorii/', 'motiv': 'geacă fără glugă'}, notes=['Mărimi italiene convertite la europene (după magazin).'])

w(8805,
  f'<p>{A("/brand/geox/", "Geox")} B842HA sunt {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi de iarnă pentru băieți")}, bleumarin, izolați, din material sintetic și piele naturală, cu sistemul Geox Tex Waterproof, care îi face rezistenți la apă. Sunt pentru copiii mici, pe zăpadă și pe vreme umedă.</p>'
  '<p>Se închid cu scai, deci se prind repede pe orice picior, iar interiorul combină textilul cu pielea naturală. Magazinul precizează că mărimile sunt italiene, convertite la cele europene.</p>'
  '<p>Talpa și construcția:</p>'
  + L(('Geox Respira', 'talpă în trei straturi.'), ('Vârf', 'rigidizat.'), ('Călcâi', 'rigidizat la spate.'), ('Talpă', 'stabilă.'))
  + '<p>Pe site sunt numerele 24-27, cam pentru 2-4 ani.</p>',
  [('cod', 'Geox bleumarin B842HA00032'), ('iarnă', 'Pantofi de iarna pentru copii'), ('izolat', 'Model Izolat'), ('material', 'combinatia materialului sintetic cu pielea naturala'),
   ('Geox Tex', 'Geox Tex Waterproof'), ('scai', 'Incheiere cu scai'), ('interior', 'Interiorul: Material textil, Piele naturala'),
   ('mărimi italiene', 'Dimensiunile disponibile sunt cele ale producatorul italian'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('vârf', 'Varf rigidizat'), ('călcâi', 'Spatele calcaiului rigidizat'), ('talpă', 'Talpa stabila')],
  {'Model': 'Geox B842HA', 'Material': 'sintetic și piele naturală, interior textil și piele naturală', 'Caracteristici': 'izolați, Geox Tex Waterproof, Geox Respira, scai', 'Cod produs': 'B842HA00032'},
  notes=['Titlul de pe site nu are culoare; magazinul dă bleumarin.'])

w(8807,
  f'<p>{A("/brand/lego/", "LEGO")} 22881 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de schi unisex")}, matlasată, cu dungi (verde pe site, albastră la magazin), făcută pentru pârtie și pentru iarna de zi cu zi. Izolația sintetică medie ține de cald, iar finisajul DWR și impregnarea apără de umezeală și de ninsoarea ușoară.</p>'
  '<p>Croiala e regular fit, cu loc pentru un strat gros dedesubt fără ca geaca să stea strâmtă.</p>'
  '<p>Pentru zăpadă și vânt, geaca are:</p>'
  + L(('Glugă', 'integrată.'), ('Guler', 'înalt.'), ('Buzunare', 'exterioare.'), ('Material', '100% poliester, umplutură sintetică ușoară.'))
  + '<p>Mărimile 104-164 sunt pentru copii între cam 4 și 14 ani.</p>',
  [('model', 'Geacă de schi pentru copii albastră 22881'), ('matlasat', 'Construcția matlasată'), ('dungi', 'Modelul cu dungi'), ('pârtie', 'funcționalitatea necesară pe pârtie'),
   ('izolație', 'Izolația sintetică medie'), ('DWR', 'Finisajul hidrofob DWR'), ('impregnare', 'Impregnarea impermeabilă ajută la protecția împotriva umezelii și a precipitațiilor ușoare de zăpadă'),
   ('croială', 'Croiala regular fit'), ('glugă', 'Gluga integrată'), ('guler', 'Gulerul înalt'), ('buzunare', 'Buzunarele exterioare'), ('material', '100% Poliester'),
   ('umplutură', 'Umplutura sintetică asigură izolație termică fără a adăuga greutate inutilă')],
  {'Model': 'LEGO 22881', 'Material': '100% poliester, izolație sintetică medie', 'Caracteristici': 'geacă de schi, DWR, glugă integrată, guler înalt, matlasată', 'Cod produs': '22881'},
  notes=['Titlul de pe site spune verde; magazinul o descrie ca albastră.'])

w(8820,
  f'<p>{ADI} JW2444 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, roz, izolată cu umplutură sintetică și tehnologia CLIMAWARM, din poliester 100% reciclat. E făcută pentru temperaturile mai reci, inclusiv pentru mișcare intensă afară.</p>'
  '<p>Mânecile și marginea de jos se termină cu bandă elastică, așa că geaca stă strânsă la încheieturi și jos; fermoarul are clapă interioară contra vântului.</p>'
  '<p>Pentru frig și pentru drumurile de seară:</p>'
  + L(('Glugă', 'fixă, cu guler ridicat.'), ('Elemente reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Căptușeală', 'are.'), ('Material', '100% poliester reciclat.'))
  + '<p>Pe site sunt mărimile 140-176, adică pentru copii de pe la 10 până pe la 16 ani.</p>',
  [('cod', 'JW2444'), ('culoare', 'culoarea roz'), ('izolat', 'Model izolat'), ('izolație', 'izolație sintetică'), ('CLIMAWARM', 'Tehnologia CLIMAWARM'),
   ('reciclat', 'Poliesterul folosit la realizarea acestui model este reciclat în întregime'), ('temperaturi', 'temperaturi mai reci'), ('efort', 'efortului intens'),
   ('elastic', 'Mâneci și marginea inferioară finisate cu o coadă elastică'), ('clapă', 'clapă interioară împotriva furtunii'),
   ('glugă, guler', 'Gulerul ridicat și gluga fixă'), ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'), ('căptușeală', 'Model cu captuseala')],
  {'Model': 'adidas JW2444', 'Material': '100% poliester reciclat, izolație sintetică', 'Caracteristici': 'CLIMAWARM, glugă fixă, clapă la fermoar, reflectorizante', 'Cod produs': 'JW2444'})

w(8821,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 262121 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")}, albi pe site, din material textil și piele naturală, fabricați fără nichel și crom. Sunt ușori și făcuți pentru purtat zilnic.</p>'
  '<p>Deschiderea e largă, iar aricii fixează pantoful pe picior; cutia lată a degetelor lasă loc degetelor, iar tăietura în U de la spate nu apasă pe tendonul lui Ahile.</p>'
  '<p>Din colaborarea cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia au rămas:</p>'
  + L(('Branț', 'detașabil, antibacterian, profilat.'), ('Talpă', 'în formă de „picior de elefant” la călcâi.'), ('Vârf', 'protejat.'), ('Inserție', 'perforată.'))
  + '<p>Numerele 19-25 corespund, de regulă, vârstei de 1-3 ani.</p>',
  [('cod', 'Pantofi copii 262121'), ('material', 'combinația materialului textil cu pielea naturală'), ('nichel', 'fara nichel si crom'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('deschidere', 'Deschidere larga'), ('arici', 'fixarii cu velcro'), ('cutie lată', 'Cutia lată a degetelor'), ('U', 'tendonului lui Ahile'),
   ('Valencia', 'medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'), ('branț', 'Brant detasabil si antibacterian, profilat'),
   ('talpă', 'Talpa in forma de „picior de elefant” peste calcaie'), ('vârf', 'Degetul securizat'), ('inserție', 'insertiei perforate')],
  {'Model': 'Biomecanics 262121', 'Material': 'textil și piele naturală, fără nichel și crom', 'Caracteristici': 'deschidere largă, arici, cutie lată a degetelor, branț antibacterian', 'Cod produs': '262121'},
  notes=['Titlul de pe site spune alb; magazinul arată albastru.'])

w(8833,
  f'<p>{ADI} JW2443 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă cu glugă unisex")}, neagră, ușor izolată, din poliester cu aplicații și finisaj hidrofob, care oprește umezeala. E potrivită pentru toamnă și pentru zilele reci cu ploaie, la copiii mai mici.</p>'
  '<p>Fasonul e drept, iar tivul elastic de la mâneci și de jos o face să stea mai bine pe corp și să se îmbrace ușor.</p>'
  '<p>Mai are:</p>'
  + L(('Elemente reflectorizante', 'pentru drumurile pe întuneric.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester.'))
  + '<p>Mărimile de pe site, 110-128, sunt pentru copii de aproximativ 5-8 ani.</p>',
  [('cod', 'JW2443'), ('culoare', 'culoarea negru'), ('ușor izolat', 'Model usor izolat'), ('aplicații', 'țesătură cu aplicații'),
   ('hidrofob', 'Finisajul hidrofob al materialului exterior previne pătrunderea umezelii'), ('fason', 'Fason drept'), ('glugă', 'Model cu gluga'),
   ('tiv', 'Mânecile și marginea inferioară sunt finisate cu un tiv elastic'), ('potrivire', 'haina se potrivește mai bine pe corp și este ușor de îmbrăcat'),
   ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('fermoar', 'Incheiere cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'adidas JW2443', 'Material': '100% poliester', 'Caracteristici': 'ușor izolată, finisaj hidrofob, glugă, reflectorizante, tiv elastic', 'Cod produs': 'JW2443'})

w(8844,
  f'<p>{WHEAT} 7558-941R sunt {A("/categorie/pantaloni-treninguri/", "pantaloni de ploaie pentru fete")}, roz, din poliester reciclat impermeabil, cu tratamentul BIONIC-FINISH® ECO. Impermeabilitatea e de 10 000 mm, deci sunt pentru ploaie, bălți și noroi.</p>'
  '<p>Bretelele sunt reglabile, iar talia se strâmtează cu capse, deci pantalonii se potrivesc și pe un copil slab; picioarele se termină cu manșete elastice, care stau strânse peste cizme.</p>'
  '<p>Ce declară magazinul:</p>'
  + L(('Impermeabilitate', '10 000 mm.'), ('Respirabilitate', '8 000 g/m2/24h.'), ('Material', '100% poliester reciclat, certificat GRS.'), ('Bretele', 'nedetașabile, reglabile.'))
  + '<p>Mărimile 80-128 merg pentru copii de cam 1-8 ani.</p>',
  [('cod', '7558-941R GRS'), ('culoare', 'culoarea roz'), ('impermeabil', 'Model confecționat din material impermeabil'), ('BIONIC', 'BIONIC-FINISH® ECO'),
   ('impermeabilitate', 'Impermeabilitate: 10 000 mm'), ('bretele', 'Model cu bretele nedetasabile, reglabile'), ('talie', 'Talia este ajustabilă cu capse'),
   ('manșete', 'Picioarele sunt finisate cu manșete confortabile, elastice'), ('respirabilitate', 'Respirabilitate: 8 000 g/m2/24h'),
   ('material', '100% Poliester reciclat'), ('GRS', 'GRS (Global Recycle Standard)')],
  {'Model': 'Wheat 7558-941R', 'Material': '100% poliester reciclat', 'Caracteristici': 'impermeabilitate 10 000 mm, bretele reglabile, talie cu capse, manșete elastice', 'Cod produs': '7558-941R'})
print('lot 9 scris')
