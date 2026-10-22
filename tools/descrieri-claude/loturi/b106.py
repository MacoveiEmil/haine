import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

REIMA = A('/brand/reima/', 'Reima')
APRO = A('/brand/alpine-pro/', 'ALPINE PRO')
GECI = '/categorie/unisex-imbracaminte-geci-jachete/'
PANT = '/categorie/unisex-imbracaminte-pantaloni-treninguri/'
ACC = '/categorie/unisex-accesorii-caciuli-manusi-accesorii/'

w(14867,
  f'<p>Pantalonii {REIMA} PUNKITON albastru închis sunt {A(PANT, "pantaloni unisex")} pentru joaca în natură. Partea exterioară are tratament REIMA Bugproof, care apără de înțepăturile insectelor, iar elementele reflectorizante îl fac pe copil mai vizibil.</p>'
  '<p>Talia e elastică, iar cracul lung se termină cu manșetă elastică. Cele două buzunare laterale au loc pentru lucrurile mici luate la plimbare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '65% poliester reciclat, 35% poliester.'), ('Membrană', 'nu are.'), ('Greutate', '200 g.'))
  + '<p>Mărimile 104-140 se potrivesc orientativ copiilor de 4-10 ani.</p>',
  [('model', 'REIMA PUNKITON'), ('culoare', 'Albastru închis'), ('natură', 'în timpul jocurilor în natură'), ('Bugproof', 'Tratamentul de pe partea exterioară REIMA Bugproof protejează împotriva înțepăturilor de insecte'),
   ('reflectorizant', 'elemente reflectorizante'), ('talie', 'talie elastică'), ('manșetă', 'crac finisat cu manșetă elastică'), ('buzunare', 'două buzunare laterale'),
   ('material', '65 % poliester reciclat, 35 % poliester'), ('greutate', '200 g'), ('crac', 'lung, finisat cu elastic')],
  {'Model': 'Reima PUNKITON', 'Material': '65% poliester reciclat, 35% poliester', 'Caracteristici': 'Bugproof, talie elastică, reflectorizante', 'Cod produs': '239984'})

w(14875,
  f'<p>Sandalele barefoot {REIMA} RANTAAN J 2.0 mov sunt listate la {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} și sunt gândite pentru un mers natural. Fața din textil e flexibilă și respirabilă, talpa din cauciuc e flexibilă și ține bine, iar drop-ul e zero.</p>'
  '<p>Vârful e lat, deci degetele au loc, iar benzile velcro le fac ușor de pus și de scos. Branțul detașabil Happy Fit ajută la alegerea numărului, iar perechea se spală în mașină la 30°C.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', '100% poliester.'), ('Talpă', '100% cauciuc.'), ('Greutate', '200 g.'))
  + '<p>Numerele 22-32 sunt pentru copii de aproximativ 1-9 ani.</p>',
  [('model', 'REIMA RANTAAN J 2.0'), ('culoare', 'Mov (mov / alb)'), ('barefoot', 'Sandalele tip barefoot pentru copii Reima RANTAAN J 2.0 asigură un mers sănătos și natural'),
   ('textil', 'Au o parte superioară textilă flexibilă și respirabilă'), ('talpă', 'talpă din cauciuc pentru o aderență mai bună'), ('drop', 'drop zero pentru o poziție naturală'),
   ('lat', 'pantofi mai lați - spațiu suplimentar pentru degete'), ('velcro', 'benzi velcro pentru încălțarea și descălțarea ușoară'),
   ('Happy Fit', 'branț detașabil cu imprimeu Happy Fit'), ('spălare', 'a se spăla în mașina de spălat la 30°C'), ('față', '100 % poliester'), ('cauciuc', '100 % cauciuc'), ('greutate', '200 g')],
  {'Model': 'Reima RANTAAN J 2.0', 'Talpă': '100% cauciuc, drop zero', 'Caracteristici': 'barefoot, velcro, branț Happy Fit', 'Cod produs': '240077'},
  notes=['Magazinul le descrie ca sandale barefoot; pe site sunt la Pantofi.'])

w(14880,
  f'<p>Pantalonii de iarnă {REIMA} KOMEIN negri sunt {A(PANT, "pantaloni unisex")} impermeabili, cu cusături etanșe și tehnologie REIMATEC, rezistenți la vânt și cu izolație termică. Materialul e respirabil și rezistent la murdărie, iar finisajul hidrofug este fără PFAS. Produsul are certificare bluesign.</p>'
  '<p>Croiala e lejeră, cu cusătură în cruce care nu încurcă la mers. Au bretele elastice reglabile și detașabile, talie elastică ajustabilă, manșete de zăpadă și crac întărit jos.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'unul lateral, cu fermoar.'), ('Căptușeală', '55% poliester reciclat, 45% elastan.'), ('Respirabilitate', '5 000 g/m²/24h.'), ('Greutate', '500 g.'))
  + '<p>Mărimile 104-164 sunt pentru copii de cam 4-14 ani.</p>',
  [('model', 'REIMA KOMEIN'), ('culoare', 'Negru'), ('etanșe', 'toate cusăturile sunt etanșe, impermeabile'), ('vânt', 'material impermeabil, rezistent la vânt'),
   ('izolație', 'Materialul rezistent și izolația termică combat frigul'), ('murdărie', 'material respirabil și rezistent la murdărie'), ('PFAS', 'finisaj hidrofug și anti-murdărie fără PFAS'),
   ('bluesign', 'Acesta este un produs bluesign®'), ('lejeră', 'lejeră'), ('cruce', 'cusătura în cruce'), ('bretele', 'bretele elastice reglabile și detașabile'),
   ('talie', 'talie elastică care se poate ajusta'), ('manșete', 'manșete de zăpadă'), ('întărituri', 'crac finisat cu întărituri în partea inferioară'), ('buzunar', 'buzunar cu fermoar'),
   ('căptușeală', '55 % poliester reciclat, 45 % elastan'), ('respirabilitate', '5 000 g/m²/24h'), ('greutate', '500 g'), ('REIMATEC', 'REIMATEC')],
  {'Model': 'Reima KOMEIN', 'Tehnologie': 'REIMATEC', 'Caracteristici': 'bretele detașabile, manșete de zăpadă, fără PFAS', 'Cod produs': '259999'},
  notes=['În specificații, la „Izolație termică” apare „7.000 mm”, o valoare de coloană de apă; nu am folosit-o.'])

w(14881,
  f'<p>Geaca {APRO} NURGA roz este o {A(GECI, "geacă unisex")} din SOFT-SHELL cu membrană WINDBARRIER și tratament DWR: materialul e elastic, impermeabil, respirabil și rezistent la vânt, cu imprimeu pe toată suprafața. Croiala e ușor strâmtă pe corp.</p>'
  '<p>Gluga e fixă, cu șnur de ajustare, iar protecția de la bărbie e dintr-un material călduros. Se închide cu fermoar pe toată lungimea, cu trăgătoare mai lungi, iar mânecile au tiv tricotat.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'patru, în față cu fermoar și pe interior.'), ('Material', '94% poliester, 6% elastan.'), ('Coloană de apă', '8 000mm.'), ('Respirabilitate', '3.000 g/m2/24h.'))
  + '<p>Mărimile 104-110 până la 152-158 se potrivesc orientativ copiilor de 4-13 ani.</p>',
  [('model', 'ALPINE PRO NURGA'), ('culoare', 'Roz (roz / albastru)'), ('softshell', 'material cu membrană SOFT-SHELL WINDBARRIER DWR'),
   ('elastic', 'Materialul este elastic, impermeabil, respirabil și rezistent la vânt'), ('imprimeu', 'cu imprimeu pe toată suprafața'), ('croială', 'croială ușor strâmtă pe corp'),
   ('glugă', 'Se remarcă prin gluga fixă cu șnur de ajustare'), ('bărbie', 'protecție la bărbie din material călduros'), ('fermoar', 'fixare cu fermoar pe toată lungimea'),
   ('trăgătoare', 'trăgătoare fermoar mai lungi'), ('tiv', 'mâneci cu tiv tricotat'), ('buzunare', '4 buzunare, frontale cu fermoar și pe interior'),
   ('material', '94 % poliester, 6 % elastan'), ('coloană', '8 000mm'), ('respirabilitate', '3.000 g/m2/24h')],
  {'Model': 'ALPINE PRO NURGA', 'Material': '94% poliester, 6% elastan', 'Caracteristici': 'softshell WINDBARRIER, DWR, glugă reglabilă', 'Cod produs': '162723'})

w(14884,
  f'<p>Șapca {REIMA} BIITSI somon este un {A(ACC, "accesoriu unisex")} de vară, prelungit la spate, astfel încât apără de soare nu doar fața, ci și gâtul. Materialul e ușor și elastic, cu factor de protecție UV 50+.</p>'
  '<p>Stilul e simplu, ușor de purtat la plajă sau în parc, iar țesătura este din poliester reciclat. Mărimea se alege după circumferința capului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester reciclat.'), ('Protecție', 'UV 50+.'), ('Cod produs', '198044.'))
  + '<p>Mărimile 48-52 sunt circumferințe ale capului și se potrivesc orientativ copiilor de la 1 an în sus.</p>',
  [('model', 'REIMA BIITSI'), ('culoare', 'Somon'), ('prelungită', 'este prelungită la spate, astfel protejează și gâtul de razele solare, nu numai fața'),
   ('ușor', 'Materialul ușor și elastic dispune de factor de protecție UV'), ('UV', 'factor de protecție UV 50+'), ('stil', 'stil simplu'), ('material', '100 % poliester reciclat')],
  {'Model': 'Reima BIITSI', 'Material': '100% poliester reciclat', 'Caracteristici': 'UV 50+, prelungită la spate', 'Cod produs': '198044'},
  notes=['Vârsta calculată automat era nefolositoare (0-0 luni); mărimile sunt circumferințe ale capului.'], varsta_txt='de la 1 an în sus')

w(14929,
  f'<p>Geaca softshell {A("/brand/head/", "Head")} EKON albastră este o {A(GECI, "geacă unisex")} bună pentru activități în aer liber și pentru oraș, cu glugă fixă care se ajustează. Materialul softshell e plăcut la atingere și apără de vremea urâtă.</p>'
  '<p>Fermoarul principal are clapetă și protecție pentru bărbie, iar manșetele se reglează. Înăuntru e o etichetă pentru numele copilului.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două în față, cu fermoar.'), ('Material', '100% poliester.'), ('Rezistență la apă', '5.000mm.'), ('Respirabilitate', '5.000g/m²/24h.'))
  + '<p>Mărimile 116-122 până la 164-170 sunt pentru copii de aproximativ 6-15 ani.</p>',
  [('model', 'Head EKON'), ('culoare', 'Albastru (albastru / albastru deschis)'), ('outdoor', 'adecvată pentru toate activitățile outdoor și pentru ținuta de oraș'),
   ('glugă', 'glugă fixă ajustabilă'), ('plăcut', 'material softshell plăcut'), ('protecție', 'Materialul funcțional oferă protecție împotriva condițiilor nefavorabile'),
   ('fermoar', 'fermoarul principal prevăzut cu o clapetă este acoperit cu o protecție pentru bărbie'), ('manșete', 'manșete ajustabile'), ('etichetă', 'etichetă pentru nume în interior'),
   ('buzunare', 'două buzunare frontale cu fermoar'), ('material', '100 % poliester'), ('apă', '5.000mm'), ('respirabilitate', '5.000g/m²/24h')],
  {'Model': 'Head EKON', 'Material': '100% poliester softshell', 'Caracteristici': 'glugă ajustabilă, manșete reglabile, 5.000 mm', 'Cod produs': '140975'})

w(14950,
  f'<p>Geaca de schi {APRO} GERGO roz este o {A(GECI, "geacă unisex")} cu membrană PTX SNOW și tratament DWR: materialul e impermeabil, permeabil la vapori, rezistent la vânt și elastic. Umplutura e groasă și călduroasă, cusăturile sunt lipite, iar centura de zăpadă oprește zăpada să intre.</p>'
  '<p>Gluga e fixă, mânecile se ajustează cu velcro și au manșete interioare elastice, iar tivul de jos se strânge cu șnur. Imprimeul reflectorizant e în față și la spate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'trei.'), ('Material', '100% poliester.'), ('Coloană de apă', '8 000mm.'), ('Respirabilitate', '3000 g/m²/24h.'))
  + '<p>Mărimile 104-110 până la 152-158 sunt pentru copii de cam 4-13 ani.</p>',
  [('model', 'ALPINE PRO GERGO'), ('culoare', 'Roz'), ('PTX', 'membrană PTX SNOW, finisaj DWR'), ('material', 'material - impermeabil, permeabil la vapori, rezistent la vânt și elastic'),
   ('umplutură', 'umplutura groasă care va menține căldura'), ('lipite', 'cusături lipite'), ('centură', 'centură de protecție împotriva zăpezii'), ('glugă', 'glugă fixă'),
   ('mâneci', 'mâneci anatomice, ajustabile cu bandă velcro și manșete interioare elastice'), ('tiv', 'tiv inferior ajustabil cu șnur'),
   ('reflectorizant', 'imprimeu reflectorizant pe partea din față și la spate'), ('buzunare', '3 buzunare'), ('poliester', '100 % poliester'), ('coloană', '8 000mm'),
   ('respirabilitate', '3000 g/m²/24h')],
  {'Model': 'ALPINE PRO GERGO', 'Material': '100% poliester', 'Caracteristici': 'membrană PTX SNOW, centură de zăpadă, cusături lipite', 'Cod produs': '175068'},
  notes=['Descrierea vorbește de croială „ușor strâmtă”, lista de caracteristici de „croială lejeră”; nu am scris croiala.'])

w(14967,
  f'<p>Șosetele lungi {REIMA} KARKUUN albe sunt un {A(ACC, "accesoriu unisex")} pentru drumeții, cu finisaj Anti-Bite, un repelent sintetic împotriva țânțarilor și a căpușelor. Substanța activă e biodegradabilă și nu irită pielea.</p>'
  '<p>Tricotul conține bumbac organic certificat, poliamidă, polipropilenă și elastan, așa că șosetele sunt elastice, plăcute pe piele și elimină umezeala.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '76% bumbac organic, 11% poliamidă, 11% polipropilenă, 2% elastan.'), ('Tehnologie', 'ANTI-BITE.'), ('Greutate', '40 g.'))
  + '<p>Mărimile 26-29 până la 38-41 se potrivesc orientativ copiilor de la 3 ani în sus.</p>',
  [('model', 'REIMA KARKUUN'), ('culoare', 'Alb (alb / negru)'), ('lungi', 'Șosete lungi pentru copii REIMA KARKUUN'),
   ('Anti-Bite', 'finisaj Anti-Bite care conține repelent sintetic împotriva țânțarilor și a căpușelor'), ('biodegradabil', 'substanța este biodegradabilă și nu irită pielea'),
   ('organic', 'bumbac organic certificat'), ('elastic', 'De aceea sunt elastice, plăcute în contact cu pielea și elimină fiabil umezeala'),
   ('material', '76 % bumbac organic, 11 % poliamidă, 11 % polipropilenă, 2 % elastan'), ('tehnologie', 'ANTI-BITE'), ('greutate', '40 g')],
  {'Model': 'Reima KARKUUN', 'Material': '76% bumbac organic', 'Caracteristici': 'Anti-Bite, șosete lungi', 'Cod produs': '198051'})

w(14979,
  f'<p>Geaca de iarnă {A("/brand/loap/", "LOAP")} INVOLFA roz este o {A(GECI, "geacă unisex")} cu fața STORMEX și membrană DryTech, care rezistă la vânt, ploaie și joacă. Izolația din fibre tubulare POLYTHERM încălzește repede și își păstrează forma.</p>'
  '<p>Tivul de jos și mânecile sunt finisate cu elastic, deci geaca stă bine pe corp. Fermoarul are capac la capăt, ca să nu ciupească bărbia, iar gluga fixă are blăniță. Elementele reflectorizante ajută la vizibilitate.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două.'), ('Material', '100% poliester (Stormex).'), ('Căptușeală', 'tafta din poliester.'))
  + '<p>Mărimile 112-116 până la 158-164 sunt pentru copii de aproximativ 5-14 ani.</p>',
  [('model', 'LOAP INVOLFA'), ('culoare', 'Roz (roz / maro)'), ('STORMEX', 'Partea superioară STORMEX durabilă'), ('DryTech', 'DryTech'),
   ('vânt', 'pot rezista vântului, ploii și jocului cu prietenii'), ('POLYTHERM', 'izolația din fibre tubulare POLYTHERM asigură încălzirea rapidă'),
   ('formă', 'are o memorie excelentă a formei'), ('elastic', 'tiv inferior și mâneci elastice'), ('fermoar', 'Fermoarul cu capac la capăt previne ciupirea nedorită a pielii de pe bărbie'),
   ('blăniță', 'glugă fixă cu blăniță'), ('reflectorizant', 'elemente reflectorizante'), ('buzunare', '2 buzunare'), ('material', '100 % poliester (Stormex)'), ('tafta', '100 % poliester (tafta)')],
  {'Model': 'LOAP INVOLFA', 'Material': '100% poliester (Stormex)', 'Caracteristici': 'DryTech, umplutură Polytherm, glugă cu blăniță', 'Cod produs': '194515'},
  notes=['Magazinul spune o dată „blană nedetașabilă” și o dată „blăniță detașabilă”; nu am precizat dacă blănița se scoate.'])

w(14982,
  f'<p>Geaca softshell {APRO} FERLO mix este o {A(GECI, "geacă unisex")} fără umplutură, cu imprimeu colorat pe toată suprafața. Materialul are tratament DWR, e hidrofug, rezistent la vânt, flexibil și permeabil la vapori, iar căptușeala e contrastantă.</p>'
  '<p>Croiala e ușor strâmtă, cu spatele extins. Mânecile sunt finisate cu elastic, are protecție la bărbie, trăgătoare lungi la fermoar și imprimeu cu elemente reflectorizante în față.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Buzunare', 'două laterale, cu fermoar.'), ('Material', '96% poliester, 4% elastan.'), ('Tehnologie', 'DWR, Softshell.'))
  + '<p>Mărimile 104-110 până la 152-158 se potrivesc orientativ copiilor de 4-13 ani.</p>',
  [('model', 'ALPINE PRO FERLO'), ('culoare', 'Mix'), ('imprimeu', 'Geaca cu imprimeu pe toată suprafața pentru copii ALPINE PRO FERLO'), ('umplutură', 'fără umplutură'),
   ('hidrofug', 'material hidrofug, rezistent la vânt și respirabil, cu tratament DWR'), ('flexibil', 'material hidrofug, permeabil la vapori, flexibil'),
   ('căptușeală', 'căptușeală contrastantă'), ('croială', 'croială ușor strâmtă'), ('spate', 'spate extins'), ('mâneci', 'mâneci finisate cu elastic'),
   ('bărbie', 'protecție la bărbie'), ('trăgătoare', 'trăgătoare lungi pentru fermoar'), ('reflectorizant', 'imprimeul modern cu elemente reflectorizante în partea frontală'),
   ('buzunare', '2 laterale cu fermoar'), ('material', '96 % poliester , 4 % elastan'), ('tehnologie', 'DWR , Softshell')],
  {'Model': 'ALPINE PRO FERLO', 'Material': '96% poliester, 4% elastan', 'Caracteristici': 'softshell DWR, fără umplutură, reflectorizante', 'Cod produs': '171252'},
  notes=['Magazinul spune o dată „gluga detașabilă” și o dată „glugă fixă”; nu am scris despre glugă.'])
