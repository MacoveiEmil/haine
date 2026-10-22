import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')
COL = A('/brand/columbia/', 'Columbia')
F4 = A('/brand/4f/', '4F')
NOTE = 'Pagina magazinului (Fashion Days) nu are descriere detaliată; am folosit doar faptele din titlu.'

w(11878,
  f'<p>Ghetele de iarnă {A("/brand/froddo/", "Froddo")} BASCO TEX G2110144 sunt {A("/categorie/bebe-incaltaminte-ghete-cizme/", "ghete pentru bebeluși")}, argintii, izolate, din piele naturală, pentru zilele reci. Interiorul e textil, iar talpa exterioară din cauciuc rezistă la uzură.</p>'
  '<p>Șireturile elastice cu cârlig, plus scaiul, fac ghetele ușor de pus și de scos, fără nod. Vârful rotund, ușor rigid, lasă degetele să se așeze liber, deci gheata merge și la un picior mai plin.</p>'
  '<p>Ce ține piciorul în gheată:</p>'
  + L(('Călcâi', 'contrafort rigid, piciorul nu alunecă.'), ('Partea de sus', 'piele naturală.'), ('Interior', 'material textil.'))
  + '<p>Numerele 21-24 sunt pentru cei mici de 1-3 ani, aproximativ.</p>',
  [('model', 'Froddo Ghete de iarna pentru copii din piele BASCO TEX culoarea argintiu, G2110144'), ('izolat', 'Model izolat confecționat din piele naturala'),
   ('interior', 'Interiorul: Material textil'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'),
   ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'), ('scai', 'Fixare: cu scai'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('degete', 'degetele se pot aranja liber în pantof'), ('călcâi', 'Contorul de călcâi rigid'), ('nu alunecă', 'astfel încât să nu alunece în timpul mișcării')],
  {'Model': 'Froddo BASCO TEX', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'izolate, șireturi elastice cu cârlig, scai', 'Cod produs': 'G2110144'})

w(11912,
  f'<p>Pantofii {TH} 305127815 sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} albi, din piele ecologică, un model simplu, de purtat la ținute îngrijite sau de zi cu zi. </p>'
  '<p>Pe site sunt numerele 30-31, care se potrivesc copiilor de cam 6-7 ani, la începutul școlii.</p>',
  [('model', 'Pantofi fete 305127815, Piele ecologica, Alb')],
  {'Model': 'Tommy Hilfiger 305127815', 'Material': 'piele ecologică', 'Caracteristici': '', 'Cod produs': '305127815'},
  insuf=True, notes=[NOTE])

w(11913,
  f'<p>Pantofii {TH} 305127815 în varianta aurie sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} din piele naturală, într-o culoare aurie strălucitoare, care merge la rochițe și la ținutele de ocazie, dar și la blugi sau colanți, în zilele obișnuite.</p>'
  '<p>Numerele 19-23 de pe site merg, în general, la copii între 1 și 3 ani.</p>',
  [('model', 'Pantofi pentru fete 305127815, Piele naturala, Auriu')],
  {'Model': 'Tommy Hilfiger 305127815', 'Material': 'piele naturală', 'Caracteristici': '', 'Cod produs': '305127815'},
  insuf=True, notes=[NOTE])

w(11929,
  f'<p>{COL} Youth Snowtrot Mid sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme pentru băieți")}, negre, din material textil, un model de zăpadă cu profil mediu, după numele modelului, pentru iarnă și joaca afară pe zăpadă.</p>'
  '<p>Pe site e disponibil doar numărul 37, potrivit, de obicei, copiilor de la 12 ani în sus.</p>',
  [('model', 'Cizme Youth Snowtrot Mid, negru, material textil, pentru baieti')],
  {'Model': 'Columbia Youth Snowtrot Mid', 'Material': 'material textil', 'Caracteristici': '', 'Cod produs': ''},
  insuf=True, notes=[NOTE, '„Model de zăpadă” și „iarnă” sunt deduse din numele Snowtrot.'])

w(11944,
  f'<p>{COL} 305283887 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete de trekking unisex")}, în culoarea albastru, din material textil, gândite pentru drumeții, plimbări pe trasee de munte și ieșiri în natură, în weekend sau în vacanțe.</p>'
  '<p>Mărimile de pe site, 32-39, acoperă copiii de pe la 8 ani în sus.</p>',
  [('model', 'Ghete de trekking copii, 305283887, textil, albastru')],
  {'Model': 'Columbia 305283887', 'Material': 'material textil', 'Caracteristici': 'ghete de trekking', 'Cod produs': '305283887'},
  insuf=True, notes=[NOTE])

w(12019,
  f'<p>{F4} propune o {A("/categorie/geci-jachete/", "geacă bomber pentru fete")}, bej, de tranziție, din material sintetic, cu croială supradimensionată și fără glugă, deci încape lejer un hanorac dedesubt.</p>'
  '<p>Mărimile 122-164 sunt pentru copii de aproximativ 7-14 ani. Croiala largă lasă loc și pentru un pulover în zilele mai răcoroase.</p>',
  [('model', 'Jacheta bomber de tranzitie fete bej, croiala supradimensionata, sintetic, fara gluga')],
  {'Model': '4F (bomber de tranziție)', 'Material': 'sintetic', 'Caracteristici': 'bomber, supradimensionată, fără glugă', 'Cod produs': ''},
  insuf=True, notes=[NOTE])

w(12020,
  f'<p>Bomberul {F4} în varianta neagră este o {A("/categorie/geci-jachete/", "geacă bomber pentru fete")} din material sintetic, cu croială oversize și fără glugă. Fiind larg, se poartă comod peste o bluză groasă. Pe site, mărimile 122-164 merg la copii de 7-14 ani, în mare.</p>',
  [('model', 'Jacheta bomber pentru fete neagra, sintetic, croiala oversize, fara gluga')],
  {'Model': '4F (bomber)', 'Material': 'sintetic', 'Caracteristici': 'bomber, oversize, fără glugă', 'Cod produs': ''},
  insuf=True, notes=[NOTE])

w(12066,
  f'<p>Geaca {A("/brand/blue-seven/", "Blue Seven")} 895553X este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă pentru băieți")}, bleumarin, o culoare închisă, practică pentru zilele obișnuite, care merge ușor la blugi și la pantaloni de trening.</p>'
  '<p>Mărimile 110-128 de pe site sunt, de regulă, pentru copii de 5-8 ani.</p>',
  [('model', 'Geaca Baieti, 895553X, Bleumarin')],
  {'Model': 'Blue Seven 895553X', 'Material': '', 'Caracteristici': '', 'Cod produs': '895553X'},
  insuf=True, notes=[NOTE])

w(12087,
  f'<p>Ghetele {COL} de zăpadă sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "ghete de zăpadă unisex")}, în culoarea albastru, din material textil, pentru iarnă, plimbările pe zăpadă și joaca afară în zilele reci, cu prietenii.</p>'
  '<p>Pe site sunt numerele 32-37, pentru copii de la, cu aproximație, 8 ani în sus.</p>',
  [('model', 'Ghete de zapada copii, albastru, material textil')],
  {'Model': 'Columbia (ghete de zăpadă)', 'Material': 'material textil', 'Caracteristici': 'ghete de zăpadă', 'Cod produs': ''},
  insuf=True, notes=[NOTE])

w(12110,
  f'<p>{F4} 302874538 este o {A("/categorie/geci-jachete/", "geacă pentru fete")}, roz, din poliamidă, o fibră sintetică, într-o culoare veselă, potrivită pentru zilele obișnuite de școală, plimbare și joacă în parc.</p>'
  '<p>Mărimile de pe site, 122-164, se potrivesc fetelor de în jur de 7-14 ani.</p>',
  [('model', 'Geaca Fete, 302874538, Poliamida, Roz')],
  {'Model': '4F 302874538', 'Material': 'poliamidă', 'Caracteristici': '', 'Cod produs': '302874538'},
  insuf=True, notes=[NOTE])
