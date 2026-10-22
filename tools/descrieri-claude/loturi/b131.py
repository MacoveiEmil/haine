import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GU = '/categorie/unisex-imbracaminte-geci-jachete/'
VANDUT = 'Pagina magazinului arată produsul ca VÂNDUT și nu dă culoarea; culoarea e cea din titlul site-ului.'

w(14726,
  f'<p>Adidașii pe gleznă {A("/brand/geox/", "Geox")} J WASHIBA A negri sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} cu design Disney, cu Minnie Mouse. Tehnologia Respira ajută la respirabilitate și la eliminarea umezelii, iar detaliile perforate din față lasă aerul să intre.</p>'
  '<p>Se închid cu scai, care ține piciorul fix și face încălțatul ușor, iar gulerul e căptușit și confortabil. Sunt pentru purtat zi de zi. Magazinul precizează că nu sunt rezistenți la apă.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'poliuretan, plasă.'), ('Talpă', 'cauciuc.'), ('Cod produs', '253669.'))
  + '<p>Pe site a rămas doar numărul 29, potrivit cam pentru 4-5 ani.</p>',
  [('model', 'Geox J WASHIBA A'), ('Minnie', 'design Disney simpatic cu Minnie Mouse'), ('Respira', 'Tehnologia Respira™ asigură o respirabilitate optimă și eliminarea umezelii'),
   ('perforate', 'Detaliile perforate din partea frontală'), ('scai', 'închidere cu scai'), ('velcro', 'asigură o fixare fermă pe picior'), ('guler', 'guler căptușit confortabil'),
   ('zilnic', 'Sunt ideali pentru activități cotidiene'), ('față', 'poliuretan, plasă'), ('talpă', 'cauciuc')],
  {'Model': 'Geox J WASHIBA A', 'Talpă': 'cauciuc', 'Caracteristici': 'Respira, scai, Minnie Mouse', 'Cod produs': '253669'},
  notes=[VANDUT, 'Magazinul îi descrie ca adidași pentru fete; pe site sunt unisex, la Pantofi.'])

w(14776,
  f'<p>Geaca {A("/brand/didriksons/", "Didriksons")} BRISKA albastru închis este o {A(GU, "geacă unisex")} moale și confortabilă, pentru joaca afară, din țesătură elastică în 4 direcții, cu croială dreaptă. Finisajul hidrofug e fără PFC.</p>'
  '<p>Gluga se detașează, manșetele sunt elastice, iar fermoarul din față are protecție la bărbie. Are buzunare cu fermoar, cusături decorative, elemente reflectorizante și o etichetă cu loc pentru mai multe nume.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Glugă', 'detașabilă.'), ('Buzunare', 'cu fermoar, două în față.'))
  + '<p>Mărimile 90-140 corespund orientativ vârstei de 2-10 ani.</p>',
  [('model', 'DIDRIKSONS BRISKA'), ('moale', 'este moale și confortabilă, ideală pentru activitățile în aer liber'), ('elastic', 'țesătură elastică în 4 direcții'),
   ('dreaptă', 'croială dreaptă'), ('PFC', 'finisaj hidrofug fără PFC'), ('glugă', 'Gluga detașabilă și manșetele elastice'), ('bărbie', 'Fermoarul frontal este dotat cu protecție pentru bărbie'),
   ('buzunare', '3 buzunare practice cu fermoar'), ('decorative', 'cusături decorative'), ('reflectorizant', 'elemente reflectorizante'),
   ('etichetă', 'o etichetă cu spațiu pentru mai multe nume'), ('material', '100 % poliester'), ('față', '2 în față')],
  {'Model': 'Didriksons BRISKA', 'Material': '100% poliester, elastic în 4 direcții', 'Caracteristici': 'hidrofugă fără PFC, glugă detașabilă, reflectorizante', 'Cod produs': '237071'},
  notes=[VANDUT, 'Descrierea spune 3 buzunare cu fermoar, specificațiile 2 în față; am scris „două în față”.'])

w(14813,
  f'<p>Geaca {A("/brand/nax/", "NAX")} COMO roz este o {A(GU, "geacă unisex")} din material impermeabil, permeabil la vapori și rezistent la vânt, cu membrană PTX și tratament DWR, bună pentru vremea capricioasă. Croiala e lejeră, cu mâneci elastice.</p>'
  '<p>Lățimea se reglează cu un șnur, deci geaca se poate strânge pe corp, pe spate are un imprimeu, iar pe mânecă o emblemă decorativă. Croiala e elegantă, dar comodă la mișcare.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Material', '100% poliester.'), ('Membrană', 'PTX.'), ('Croială', 'lejeră.'))
  + '<p>Mărimile 104-110 până la 164-170 merg pe la 4-15 ani.</p>',
  [('model', 'NAX COMO'), ('impermeabil', 'material impermeabil, permeabil la vapori și rezistent la vânt'), ('PTX', 'membrană PTX, DWR'), ('capricioasă', 'vremea capricioasă'),
   ('lejeră', 'croială lejeră'), ('mâneci', 'mâneci elastice'), ('șnur', 'Datorită șnurului, este posibilă reglarea lățimii acesteia'), ('imprimeu', 'imprimeu pe partea din spate'),
   ('emblemă', 'element decorativ pe mânecă'), ('elegantă', 'Are o croială elegantă, dar confortabilă'), ('material', '100 % poliester')],
  {'Model': 'NAX COMO', 'Material': '100% poliester, membrană PTX', 'Caracteristici': 'impermeabilă, DWR, croială lejeră', 'Cod produs': '146028'},
  notes=[VANDUT])

w(14854,
  f'<p>Ghetele de iarnă {A("/brand/reima/", "Reima")} HALLAVA QUICKLOCK maro sunt listate la {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} și sunt testate pentru izolare termică până la -20 °C. Modelul e vegan, cu membrană Reimatec și inserție impermeabilă cu cusături etanșe, iar căptușeala din fleece ține de cald.</p>'
  '<p>Sistemul Freelock strânge sau slăbește șireturile prin rotire. Talpa din EVA și cauciuc reciclat e ușoară și flexibilă, branțurile detașabile au imprimeu Happy Fit, iar detaliile reflectorizante se văd seara.</p>'
  '<p>Detaliile de bază:</p>'
  + L(('Față', 'materiale sintetice, textile.'), ('Talpă', 'cauciuc.'), ('Tehnologie', 'EVA, REIMATEC.'))
  + '<p>Pe site a rămas doar numărul 37, potrivit orientativ de la 12 ani în sus.</p>',
  [('model', 'REIMA HALLAVA QUICKLOCK'), ('-20', 'au fost testate pentru izolare termică până la -20 °C'), ('vegan', 'vegane'), ('Reimatec', 'membrană rezistentă la apă Reimatec'),
   ('etanșe', 'inserție impermeabilă cu cusături etanșe'), ('fleece', 'căptușeala din fleece păstrează căldura'), ('Freelock', 'sistem de șireturi Freelock – se strâng și se desfac prin rotire'),
   ('talpă', 'Talpa flexibilă și ușoară din EVA/cauciuc conține cauciuc reciclat'), ('Happy Fit', 'branțuri detașabile cu imprimeu Happy Fit'),
   ('reflectorizant', 'elemente reflectorizante'), ('față', 'materiale sintetice, textile'), ('cauciuc', 'cauciuc'), ('tehnologie', 'EVA , REIMATEC')],
  {'Model': 'Reima HALLAVA QUICKLOCK', 'Membrană': 'Reimatec', 'Caracteristici': '-20 °C, Freelock, vegane', 'Cod produs': '259939'},
  notes=[VANDUT, 'Pe site sunt la Pantofi; magazinul le descrie ca ghete de iarnă.'])
