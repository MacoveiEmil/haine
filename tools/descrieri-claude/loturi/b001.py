import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

NIKE = A('/brand/nike/', 'Nike')

w(4877,
  f'<p>{NIKE} JDB ESS DRAFT JACKET este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă ușoară pentru băieți")}, albastră cu negru, din nailon cu suprafață țesută netedă. Magazinul o recomandă pentru activități în aer liber, precum drumețiile, în sezonul primăvară-vară.</p>'
  '<p>Croiala e clasică, iar manșetele și betelia elastică strâng geaca la încheieturi și în talie, așa că stă aproape de corp și pe un copil mai slab.</p>'
  '<p>Pentru o geacă de purtat la drum, detaliile sunt practice:</p>'
  + L(('Glugă', 'atașată, nu se scoate.'), ('Închidere', 'fermoar pe toată lungimea.'), ('Buzunare', 'laterale, cu fermoare ascunse.'), ('Design', 'panouri în contrast pe mâneci și logo pe piept.'))
  + '<p>Pe site se găsește în mărimile S, M, L și XL, care după tabelul magazinului acoperă cam vârsta de 8-15 ani.</p>',
  [('model', 'Jacheta Nike JDB ESS DRAFT JACKET albastru-negru'), ('nailon', 'realizată din nailon'), ('suprafață', 'suprafață țesută netedă'),
   ('drumeție', 'drumețiile'), ('sezon', 'sezonul primăvară-vară'), ('croială', 'croială clasică'), ('elastic', 'manșete și betelie elastică'),
   ('glugă', 'glugă atașată'), ('fermoar', 'fermoar pe toată lungimea'), ('buzunare', 'buzunare laterale cu fermoare ascunse'),
   ('panouri', 'panouri de culoare contrastantă pe mâneci'), ('logo', 'logo vizibil pe piept')],
  {'Model': 'Nike JDB ESS DRAFT JACKET', 'Material': 'nailon', 'Caracteristici': 'glugă atașată, manșete și betelie elastice, buzunare cu fermoare ascunse', 'Cod produs': '95D689-GAG'},
  varsta_txt='8-15 ani', notes=['Vârsta pentru S-XL: tabelul de mărimi Nike al magazinului (pagina produsului 4949); pe pagina acestui produs tabelul e trunchiat.'])

w(4944,
  f'<p>{NIKE} NKG CLUB HBR WOVEN este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă ușoară unisex")}, neagră, din poliester, cu imprimeu floral pe toată suprafața și un logo swoosh mare în față. Magazinul o indică pentru purtare casual sau sport, în sezonul primăvară-vară.</p>'
  '<p>Croiala e lejeră, deci lasă loc de un hanorac dedesubt, iar manșetele și tivul elastic o strâng la încheieturi și jos, ca să nu stea largă.</p>'
  '<p>Se îmbracă repede și se închide până sus:</p>'
  + L(('Închidere', 'fermoar pe toată lungimea.'), ('Guler', 'înalt.'), ('Material', 'poliester, cu suprafață netedă.'), ('Logo', 'swoosh mare în față și unul mic pe mânecă.'))
  + '<p>Mărimile de pe site sunt 4, 5 și 6, adică, după tabelul magazinului, cam 3-6 ani.</p>',
  [('model', 'Jacheta Nike NKG CLUB HBR WOVEN JACKET neagră'), ('material, croială, guler', 'Jachetă Nike din poliester, cu croială lejeră și guler înalt'),
   ('floral', 'motiv floral'), ('logo mare', 'logo Nike swoosh mare pe partea din față'), ('logo mic', 'un swoosh mai mic pe mânecă'),
   ('utilizare', 'purtare casual sau sport'), ('sezon', 'sezonul primăvară-vară'), ('elastic', 'manșete elastice și tiv elastic'),
   ('fermoar', 'fermoar pe toată lungimea'), ('suprafață', 'suprafață netedă')],
  {'Model': 'Nike NKG CLUB HBR WOVEN', 'Material': 'poliester', 'Caracteristici': 'croială lejeră, guler înalt, manșete și tiv elastice, imprimeu floral', 'Cod produs': '36N593-023'},
  varsta_txt='3-6 ani', notes=['Vârsta pentru mărimile 4-6: tabelul de mărimi Nike al magazinului (pagina produsului 4949).'])

w(4949,
  f'<p>{NIKE} K NSW RPL WR HD este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă ușoară unisex")} neagră, din poliester, cu glugă și închidere cu fermoar pe toată lungimea. Magazinul o recomandă pentru purtare casual și pentru drumeție.</p>'
  '<p>Manșetele și betelia sunt elastice, așa că geaca se strânge la încheieturi și în talie și nu se umflă pe un copil mai slab. La spate are un clin (yoke), o bucată de material cusută peste umeri.</p>'
  '<p>Pe drum, contează unde ții lucrurile și cum se închide:</p>'
  + L(('Buzunare', 'laterale, cu fermoar.'), ('Glugă', 'da, fixă.'), ('Material', 'poliester, țesătură netedă.'), ('Logo', 'Nike, pe piept.'))
  + '<p>Pe site sunt mărimile M, L și XL, care corespund, în general, vârstei de 10-15 ani.</p>',
  [('model', 'Jacheta Nike K NSW RPL WR HD JKT neagră'), ('ușoară, glugă', 'Jachetă ușoară Nike, cu glugă'), ('fermoar', 'fermoar pe toată lungimea'),
   ('utilizare', 'purtare casual și pentru drumeție'), ('elastic', 'manșete elastice și betelie elastică'), ('clin', 'La spate are un clin (yoke)'),
   ('buzunare', 'buzunare laterale cu fermoar'), ('logo', 'logo Nike pe piept'), ('material', 'realizată din poliester'), ('vârstă M', '10-12 ani'), ('vârstă XL', '13-15 ani')],
  {'Model': 'Nike K NSW RPL WR HD JKT', 'Material': 'poliester', 'Caracteristici': 'glugă, manșete și betelie elastice, buzunare cu fermoar', 'Cod produs': 'IF2821-010'},
  varsta_txt='10-15 ani')

w(8523,
  f'<p>{A("/brand/columbia/", "Columbia")} Puffect este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, matlasată, care pe site apare în negru și în violet. Izolația medie și groasă o face bună pentru zilele reci, iar tehnologia OMNI-SHIELD™, un strat hidrofob, limitează absorbția umezelii și a murdăriei.</p>'
  '<p>Croiala e regulară, cu loc pentru straturi suplimentare dedesubt, iar lungimea ajunge până la șolduri. Manșetele elastice strâng geaca la încheieturi, deci căldura nu iese pe la mâneci.</p>'
  '<p>Pentru iarnă, geaca mai are:</p>'
  + L(('Guler', 'înalt, acoperă gâtul.'), ('Buzunare', 'laterale, cu fermoar.'), ('Căptușeală', 'sintetică, netedă și completă.'), ('Material', '100% poliester, căptușeală 100% nailon.'))
  + '<p>Pe site sunt mărimile 104-164, pentru copii de aproximativ 4-14 ani.</p>',
  [('model', 'Puffect'), ('culoare la magazin', 'violet 2089992'), ('izolație', 'izolației medii și groase'), ('OMNI-SHIELD', 'OMNI-SHIELD'),
   ('hidrofob', 'limitează absorbția umezelii'), ('murdărie', 'protecția împotriva umezelii și a murdăriei'), ('zile reci', 'în zilele reci'),
   ('croială', 'Croială regulară'), ('straturi', 'permite purtarea unor straturi suplimentare'), ('lungime', 'o croială până la șolduri'),
   ('manșete', 'Manșete elastice'), ('guler', 'Guler înalt'), ('buzunare', 'închise cu fermoar'), ('căptușeală', 'o căptușeală netedă și completă'),
   ('material', '100% Poliester'), ('căptușeală nailon', '100% Nailon')],
  {'Model': 'Columbia Puffect', 'Material': '100% poliester, căptușeală 100% nailon, umplutură 100% poliester', 'Caracteristici': 'OMNI-SHIELD™, izolație medie și groasă, matlasată, guler înalt, manșete elastice', 'Cod produs': '2089992'},
  notes=['Titlul de pe site spune negru; pagina magazinului din link arată varianta violet. Textul le pomenește pe amândouă.'])

w(8545,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} KB0KB09664 este o {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "bluză cu mânecă lungă pentru băieți")}, albă și uni, din țesătură subțire și ușor elastică. Are guler și o închidere scurtă cu nasturi la gât, deci se poartă ca un polo cu mânecă lungă.</p>'
  '<p>Croiala e simplă, iar elastanul o face să se muleze ușor pe corp, așa că pe un copil slab nu atârnă.</p>'
  '<p>Se îngrijește și se poartă ușor:</p>'
  + L(('Material', '95% bumbac și 5% elastan.'), ('Mâneci', 'lungi.'), ('Logo', 'brodat pe față.'))
  + '<p>Pe site sunt mărimile 128-176, de regulă pentru copii de 8-16 ani.</p>',
  [('cod', 'KB0KB09664'), ('țesătură', 'țesătură subțire, ușor elastică'), ('guler', 'Model cu guler'), ('nasturi', 'Incheiere scurta cu nasturi'),
   ('croială', 'Tăiere simplă'), ('compoziție', '95% Bumbac, 5% Elastan'), ('mâneci', 'Maneca lunga'), ('logo', 'Logo-ul mărcii brodat pe față'), ('uni', 'Model: uni')],
  {'Model': 'Tommy Hilfiger KB0KB09664', 'Material': '95% bumbac, 5% elastan', 'Caracteristici': 'guler, închidere scurtă cu nasturi, mânecă lungă, logo brodat', 'Cod produs': 'KB0KB09664'})

up(8566, [
    ('Numerele 28-35 acoperă, orientativ, copiii între 4 și 11 ani.</p>',
     'Numerele 28-35 se potrivesc de obicei copiilor între 4 și 11 ani; vârful rotund lasă degetele să stea liber, iar profilul e scurt, sub gleznă.</p>'),
], surse=[('vârf', 'Degetul rotund, ușor rigid'), ('profil', 'Înălțime: mic de statură')])

w(8609,
  f'<p>{A("/brand/tommy-hilfiger/", "Tommy Hilfiger")} T4A5-34028 sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} negri, ușor izolați, din imitație de piele cu inserție din piele. Sunt pentru toamnă și zilele reci de iarnă, iar interiorul combină textilul cu pielea naturală.</p>'
  '<p>Se închid cu șiret, fermoar lateral și arici: bocancul se deschide larg la încălțat, iar șiretul se reglează pe un picior mai îngust sau mai lat.</p>'
  '<p>De jos în sus, bocancii au:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Vârf și călcâi', 'vârful e rigidizat, contorul de călcâi la fel.'), ('Branț', 'din piele.'), ('Izolație', 'ușoară.'))
  + '<p>Pe site sunt numerele 30-34, potrivite în general copiilor de 6-11 ani.</p>',
  [('cod', 'T4A5-34028'), ('culoare', 'culoarea negru'), ('izolație', 'Model usor cu izolatie'), ('izolat', 'Izolare: usor izolat'), ('material', 'Material: imitatie de piele'),
   ('inserție', 'inserție din piele'), ('interior', 'Interiorul: Material textil, Piele naturala'), ('închidere', 'Model cu siret cu fermoar lateral si inchidere cu Velcro'),
   ('talpă', 'Talpa exterioară din cauciuc'), ('vârf', 'Varf rigidizat'), ('călcâi', 'Contorul de călcâi rigidizat'), ('branț', 'Brantul din piele')],
  {'Model': 'Tommy Hilfiger T4A5-34028', 'Material': 'imitație de piele cu inserție din piele, interior textil și piele naturală, talpă din cauciuc', 'Caracteristici': 'ușor izolați, șiret, fermoar lateral și arici, branț din piele', 'Cod produs': 'T4A5-34028'})

w(8618,
  f'<p>{A("/brand/guess/", "GUESS")} H4BJ10 este o {A("/categorie/geci-jachete/", "geacă de iarnă pentru fete")}, roz și matlasată, cu izolație sintetică și căptușeală, din 100% poliester. E făcută pentru temperaturile mai reci, iar croiala e simplă, ușor de purtat peste un pulover.</p>'
  '<p>La frig contează ce acoperă capul și gâtul:</p>'
  + L(('Glugă', 'fixă.'), ('Guler', 'ridicat.'), ('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere, ca mănușile sau cheile să nu cadă din ele.'))
  + '<p>Mărimile de pe site încep la 122-125 și ajung la 167, pentru copii de aproximativ 7-14 ani.</p>',
  [('cod', 'H4BJ10 WCFM0'), ('culoare', 'culoarea roz'), ('izolat', 'Model izolat'), ('izolație sintetică', 'izolație sintetica'), ('matlasat', 'Matlasat'),
   ('temperaturi reci', 'temperaturi mai reci'), ('glugă și guler', 'Gulerul ridicat și gluga fixă'), ('fermoar', 'Incheiere cu fermoar'),
   ('buzunare', 'Buzunare exterioare incheiata'), ('material', '100% Poliester'), ('căptușeală', 'Captuseala: cu captuseala'), ('croială', 'Tăiere simplă')],
  {'Model': 'GUESS H4BJ10', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, glugă fixă, guler ridicat, fermoar, buzunare închise', 'Cod produs': 'H4BJ10.WCFM0'})

w(8619,
  f'<p>{A("/brand/hugo/", "HUGO")} G00490 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de blugi pentru băieți")}, bej, subțire, din denim cu 99% bumbac și 1% elastan. Nu are izolație și nici căptușeală, deci e o geacă de tranziție, pentru primăvară și toamnă.</p>'
  '<p>Croiala e simplă, iar procentul de elastan dă denimului puțină elasticitate. Pe dedesubt încape un hanorac din {A("/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/", "hanoracele și bluzele pentru băieți")}.</p>'
  '<p>E o geacă simplă, cu puține detalii:</p>'
  + L(('Închidere', 'nasturi.'), ('Guler', 'clasic, de geacă de blugi.'), ('Material', '99% bumbac, 1% elastan.'), ('Planet friendly', 'marcată așa de magazin.'))
  + '<p>Pe site sunt mărimile 114-150, pentru copii de pe la 6 până pe la 12 ani.</p>',
  [('cod', 'G00490'), ('culoare', 'culoarea bej'), ('denim', 'Jachetă din denim pentru copii'), ('subțire', 'Model subțire'), ('neizolat', 'Model neizolat fara captuseala'),
   ('tranziție', 'Izolare: tranzitional'), ('compoziție', '99% Bumbac, 1% Elastan'), ('croială', 'Tăiere simplă'), ('guler', 'Model cu guler'), ('nasturi', 'Incheiere cu nasturi'),
   ('planet friendly', 'Planet friendly')],
  {'Model': 'HUGO G00490', 'Material': 'denim, 99% bumbac, 1% elastan', 'Caracteristici': 'subțire, fără izolație și căptușeală, guler, nasturi', 'Cod produs': 'G00490'},
  comp={'slug': '/categorie/baieti-imbracaminte-bluze-tricouri-hanorace/', 'motiv': 'geacă subțire, se poartă cu un hanorac dedesubt'})

w(8628,
  f'<p>{A("/brand/guess/", "GUESS")} H4BT03 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")}, neagră și matlasată, cu izolație sintetică și căptușeală, din țesătură netedă de poliester. Gluga fixă și gulerul ridicat o fac bună pentru temperaturile mai reci.</p>'
  '<p>Croiala e simplă, iar mărimile duble, de la 88-96 până la 122-125, cuprind fiecare câte două înălțimi, deci lasă puțin loc de creștere. Se potrivesc cam copiilor de 1-7 ani.</p>'
  '<p>Se îmbracă repede, chiar și pe un copil mic:</p>'
  + L(('Închidere', 'fermoar.'), ('Glugă', 'fixă, nu se pierde.'), ('Buzunare', 'cu închidere.'), ('Material', '100% poliester.')),
  [('cod', 'H4BT03 WCFM0'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat'), ('țesătură', 'tesatura neteda'), ('matlasat', 'Matlasat'),
   ('izolație sintetică', 'izolație sintetica'), ('temperaturi reci', 'temperaturi mai reci'), ('glugă și guler', 'Gulerul ridicat și gluga fixă'),
   ('croială', 'Tăiere simplă'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('buzunare', 'Buzunare incheiate'), ('material', '100% Poliester'), ('căptușeală', 'Captuseala: cu captuseala')],
  {'Model': 'GUESS H4BT03', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, glugă fixă, guler ridicat, fermoar', 'Cod produs': 'H4BT03.WCFM0'})
print('lot 1 scris')
