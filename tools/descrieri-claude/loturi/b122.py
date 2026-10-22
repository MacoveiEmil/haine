import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

F4 = A('/brand/4f/', '4F')
GF = '/categorie/geci-jachete/'
GB = '/categorie/baieti-imbracaminte-geci-jachete/'
GU = '/categorie/unisex-imbracaminte-geci-jachete/'
NOTE = 'Pagina magazinului (Fashion Days) nu are descriere detaliată; am folosit doar faptele din titlu.'

w(12027,
  f'<p>Geaca {F4} bleumarin este o {A(GB, "geacă pentru băieți")} din poliester, cu guler înalt care ține gâtul la adăpost de vânt, într-o culoare închisă, practică pentru zilele de școală și pentru plimbări.</p>'
  '<p>Mărimile 122-164 de pe site se potrivesc, orientativ, la 7-14 ani. Pagina magazinului nu spune dacă e izolată sau dacă are glugă, așa că e bine de verificat pozele înainte de comandă.</p>',
  [('model', 'Geaca pentru baieti bleumarin, poliester, guler inalt')],
  {'Model': '4F (geacă cu guler înalt)', 'Material': 'poliester', 'Caracteristici': 'guler înalt', 'Cod produs': ''},
  insuf=True, notes=[NOTE])

w(12037,
  f'<p>Geaca din puf sintetic {F4} violet este o {A(GF, "geacă ușoară pentru fete")}, din poliester, cu guler ridicat. Umplutura sintetică ține de cald fără să îngreuneze geaca, bună pentru zilele reci de toamnă sau de iarnă.</p>'
  '<p>Pe site sunt mărimile 122-164, potrivite cam pentru 7-14 ani. Alte detalii despre glugă sau buzunare nu apar pe pagina magazinului.</p>',
  [('model', 'Geaca din puf sintetic pentru fete violet, usoara, cu guler ridicat, poliester')],
  {'Model': '4F (geacă din puf sintetic)', 'Material': 'poliester, puf sintetic', 'Caracteristici': 'ușoară, guler ridicat', 'Cod produs': ''},
  insuf=True, notes=[NOTE, '„Toamnă sau iarnă” e dedus din tipul de umplutură.'])

w(12039,
  f'<p>Jacheta {F4} roz este o {A(GU, "geacă unisex")} din poliester, cu tehnologia 4FWarm, adică un material gândit să păstreze căldura corpului în zilele mai reci, la școală sau afară.</p>'
  '<p>Mărimile 122-164 merg, în jur de 7-14 ani. Magazinul nu precizează alte detalii, cum ar fi gluga sau tipul de închidere, deci pozele de pe pagina lui sunt cea mai bună referință.</p>',
  [('model', 'Jacheta copii Tehnologia 4FWarm, Poliester, Roz')],
  {'Model': '4F (jachetă 4FWarm)', 'Material': 'poliester', 'Caracteristici': '4FWarm', 'Cod produs': ''},
  insuf=True, notes=[NOTE, 'Explicația pentru 4FWarm e dedusă din numele tehnologiei.'])

w(12063,
  f'<p>Pantofii sport {A("/brand/geox/", "Geox")} 303950194 bej sunt {A("/categorie/adidasi/", "adidași pentru fete")} din piele ecologică, într-o nuanță deschisă, ușor de purtat cu blugi, colanți sau rochițe, zi de zi.</p>'
  '<p>Pe site e disponibil doar numărul 24, care se potrivește de obicei pe la 2-3 ani. Pagina magazinului nu dă tipul de închidere sau de talpă.</p>',
  [('model', 'Pantofi sport fete 303950194, Piele ecologica, Bej, Bej')],
  {'Model': 'Geox 303950194', 'Material': 'piele ecologică', 'Caracteristici': '', 'Cod produs': '303950194'},
  insuf=True, notes=[NOTE])

w(12075,
  f'<p>Jacheta softshell {F4} roz este o {A(GF, "geacă softshell pentru fete")}, din poliester hidrofob, rezistentă la vânt, cu glugă. E genul de jachetă bună pentru primăvară și toamnă, când bate vântul și cade câte o ploaie scurtă.</p>'
  '<p>Mărimile 128-164 de pe site corespund cu aproximație vârstei de 8-14 ani. Magazinul nu dă alte detalii despre buzunare sau manșete.</p>',
  [('model', 'Jacheta softshell pentru fete, rezistenta la vant, gluga, poliester, roz, hidrofob')],
  {'Model': '4F (jachetă softshell)', 'Material': 'poliester', 'Caracteristici': 'softshell, rezistentă la vânt, hidrofobă, glugă', 'Cod produs': ''},
  insuf=True, notes=[NOTE, '„Primăvară și toamnă” e dedus din tipul de jachetă (softshell).'])

w(12111,
  f'<p>Vesta {F4} 302874620 neagră e listată la {A(GF, "geci pentru fete")} și e făcută din poliamidă, o fibră sintetică rezistentă. Fără mâneci, se poartă peste o bluză sau sub o geacă, după cum e vremea.</p>'
  '<p>Pe site sunt mărimile 128-146, potrivite cam pentru 8-11 ani. Pagina magazinului nu spune dacă vesta e izolată sau ce închidere are.</p>',
  [('model', 'Vesta Fete, 302874620, Poliamida, Negru')],
  {'Model': '4F 302874620', 'Material': 'poliamidă', 'Caracteristici': 'vestă', 'Cod produs': '302874620'},
  insuf=True, notes=[NOTE])

w(12339,
  f'<p>Jacheta de tranziție {F4} gri este o {A(GU, "geacă unisex")} de primăvară-vară, din poliester, cu membrană 5000, care ajută la protecția împotriva ploii, potrivită pentru zilele cu vreme schimbătoare.</p>'
  '<p>Mărimile 122-164 merg orientativ la 7-14 ani. Magazinul nu dă alte detalii, așa că gluga, buzunarele și închiderea se văd doar în pozele de pe pagină.</p>',
  [('model', 'Jacheta de tranzitie copii, Poliester, membrana 5000, unisex, gri, primavara-vara')],
  {'Model': '4F (jachetă de tranziție)', 'Material': 'poliester, membrană 5000', 'Caracteristici': 'membrană, primăvară-vară', 'Cod produs': ''},
  insuf=True, notes=[NOTE])

w(12343,
  f'<p>Vesta de puf {F4} verde e listată la {A(GB, "geci pentru băieți")} și are umplutură sintetică și exterior din poliester, pentru primăvară și vară, când dimineața e încă răcoare.</p>'
  '<p>Mărimile 122-164 de pe site acoperă, cu aproximație, 7-14 ani. Pe pagina magazinului nu apar detalii despre buzunare sau închidere.</p>',
  [('model', 'Vesta de puf pentru baieti, umplutura sintetica, poliester, verde, primavara-vara')],
  {'Model': '4F (vestă de puf)', 'Material': 'poliester, umplutură sintetică', 'Caracteristici': 'vestă, primăvară-vară', 'Cod produs': ''},
  insuf=True, notes=[NOTE])

w(12345,
  f'<p>Jacheta de puf {F4} turcoaz este o {A(GF, "geacă de iarnă pentru fete")}, cu umplutură sintetică, guler înalt și un design ușor, din poliester. Gulerul înalt apără gâtul de frig, iar umplutura ține de cald.</p>'
  '<p>Pe site e doar mărimea 128, care se potrivește de obicei pe la 7-8 ani. Magazinul nu precizează dacă are glugă.</p>',
  [('model', 'Jacheta de puf pentru fete, turcoaz, umplutura sintetica, guler inalt, design usor, poliester')],
  {'Model': '4F (jachetă de puf)', 'Material': 'poliester, umplutură sintetică', 'Caracteristici': 'guler înalt, design ușor', 'Cod produs': ''},
  insuf=True, notes=[NOTE], varsta_txt='7-8 ani')

w(12346,
  f'<p>Vesta {F4} neagră e listată la {A(GF, "geci pentru fete")}, din poliester, cu umplutură sintetică și guler înalt. Ține de cald pe trunchi și lasă brațele libere, bună peste un hanorac în zilele răcoroase.</p>'
  '<p>Mărimile 122-164 se potrivesc pe la 7-14 ani. Pagina magazinului nu are alte detalii despre buzunare sau închidere.</p>',
  [('model', 'Vesta pentru fete poliester, neagra, umplutura sintetica, guler inalt')],
  {'Model': '4F (vestă)', 'Material': 'poliester, umplutură sintetică', 'Caracteristici': 'guler înalt', 'Cod produs': ''},
  insuf=True, notes=[NOTE])
