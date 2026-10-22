import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')

w(8451,
  f'<p>{A("/brand/guess/", "GUESS")} L5BL19 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")}, bej și matlasată, cu izolație sintetică, făcută pentru temperaturi mai scăzute. Materialul exterior, din poliester și bumbac, are rezistență sporită la apă și conține plastic reciclat.</p>'
  '<p>Croiala e simplă, iar mărimile sunt duble (de exemplu 158-166), deci fiecare acoperă două înălțimi apropiate și lasă puțin loc de creștere.</p>'
  '<p>Gluga și gulerul țin frigul departe de cap și de gât, iar restul e simplu:</p>'
  + L(('Glugă', 'fixă.'), ('Guler', 'ridicat.'), ('Închidere', 'fermoar.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', '54% poliester și 46% bumbac; umplutură și căptușeală din poliester.'))
  + '<p>Pe site, mărimile încep la 105-112 și se termină la 166-175, cam pentru copii de 4-16 ani.</p>',
  [('cod', 'L5BL19 WFIQ2'), ('culoare', 'culoarea bej'), ('izolat', 'Model izolat'), ('izolație sintetică', 'izolație sintetică'), ('temperaturi', 'temperaturi mai scăzute'),
   ('apă', 'Model cu rezistenta sporita la apa'), ('reciclat', 'Conține plastic reciclat'), ('croială', 'Tăiere simplă'), ('glugă, guler', 'Gulerul ridicat și gluga fixă'),
   ('matlasare', 'Matlasare'), ('fermoar', 'Incheiere cu fermoar'), ('buzunare', 'Buzunare exterioare incheiata'), ('material', '54% Poliester , 46% Bumbac'),
   ('umplutură', 'Umplutura: 100% Poliester'), ('mărime exemplu', '158-166')],
  {'Model': 'GUESS L5BL19', 'Material': '54% poliester, 46% bumbac; căptușeală și umplutură din poliester', 'Caracteristici': 'izolată, matlasată, rezistență sporită la apă, glugă fixă, guler ridicat', 'Cod produs': 'L5BL19.WFIQ2'})

w(8461,
  f'<p>{A("/brand/adidas/", "adidas")} JL7402 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă ușor izolată unisex")}, neagră, cu dungile laterale ale mărcii și glugă. Materialul exterior are un finisaj hidrofob, care oprește umezeala, deci geaca e bună pentru toamnă și pentru zilele răcoroase cu ploaie.</p>'
  '<p>Fasonul e drept, iar mânecile și marginea de jos au tiv elastic, așa că geaca stă mai bine pe corp, chiar și pe un copil slab.</p>'
  '<p>Pentru drumurile de seară, contează și:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede mai bine după lăsarea întunericului.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester.'))
  + '<p>Pe site sunt mărimile 140-176, potrivite de obicei copiilor de 10-16 ani.</p>',
  [('cod', 'JL7402'), ('culoare', 'culoarea negru'), ('ușor izolat', 'Model usor izolat'), ('dungi', 'Cu dungi laterale'), ('glugă', 'Model cu gluga'),
   ('hidrofob', 'Finisajul hidrofob al materialului exterior previne pătrunderea umezelii'), ('fason', 'Fason drept'),
   ('tiv', 'Mânecile și marginea inferioară sunt finisate cu un tiv elastic'), ('potrivire', 'haina se potrivește mai bine pe corp'),
   ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'), ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'),
   ('fermoar', 'Incheiere cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'adidas JL7402', 'Material': '100% poliester', 'Caracteristici': 'ușor izolată, finisaj hidrofob, glugă, elemente reflectorizante, tiv elastic', 'Cod produs': 'JL7402'})

w(8465,
  f'<p>{PRIMIGI} PBYGT 88909 sunt {A("/categorie/baieti-incaltaminte-pantofi/", "pantofi pentru băieți")} bleumarin, din material textil și piele întoarsă, cu membrană GORE-TEX®. Membrana e impermeabilă și rezistentă la vânt, deci pantofii merg și pe ploaie sau prin bălți, nu doar pe vreme bună.</p>'
  '<p>Cutia degetelor e lată, cu loc pentru un picior mai plinuț, iar închiderea cu arici se strânge exact cât e nevoie.</p>'
  '<p>Pe lângă membrană, mai contează:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Branț', 'UltraCush.'), ('Partea de sus', 'rigidizată, cu vârf rotund.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Pe site sunt numerele 25-30, pentru copii între 2 și 7 ani, aproximativ.</p>',
  [('cod', 'PBYGT 88909'), ('culoare', 'culoarea bleumarin'), ('material', 'combinația materialului textil cu pielea întoarsă'), ('GORE-TEX', 'membrana GORE-TEX'),
   ('impermeabil, vânt', '100% impermeabila, rezistenta la vant'), ('cutie lată', 'Cutia lată a degetelor'), ('arici', 'Închiderea cu velcro facilitează încălțarea'),
   ('talpă', 'Talpa exterioară din cauciuc'), ('branț', 'Brantul UltraCush'), ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Varf rotund'), ('căptușeală', 'Model cu captuseala textila')],
  {'Model': 'Primigi PBYGT 88909', 'Material': 'textil și piele întoarsă, talpă din cauciuc', 'Caracteristici': 'membrană GORE-TEX®, arici, cutie lată a degetelor, branț UltraCush', 'Cod produs': '88909'})

w(8478,
  f'<p>Bocancii {GEOX} de aici sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} negri, din material sintetic neporos, care se curăță ușor cu o cârpă umedă. Nu au izolație, deci sunt bocanci de toamnă și primăvară, cu talpă din cauciuc și sistemul Geox Respira.</p>'
  '<p>Se închid cu șiret și fermoar lateral: fermoarul deschide gheata la încălțat, iar șiretul o strânge pe gleznă după nevoie.</p>'
  '<p>Restul detaliilor țin piciorul fix:</p>'
  + L(('Călcâi', 'contor rigid.'), ('Vârf', 'rotund, întărit.'), ('Buclă la spate', 'ajută la încălțat.'), ('Interior', 'textil.'))
  + '<p>Pe site sunt numerele 36-39, pentru copii mari, în general de la 12 ani în sus.</p>',
  [('model', 'Bocanci copii culoarea negru'), ('sintetic', 'confecționat din material sintetic'), ('neporos', 'Partea superioară neporoasă, ușor de curățat cu o cârpă umedă'),
   ('neizolat', 'Izolare: neizolat'), ('talpă', 'Talpa exterioară din cauciuc'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('închidere', 'Model cu siret cu fermoar lateral'), ('călcâi', 'Contorul de călcâi rigid'), ('vârf', 'Cutie rotunda, intarita'), ('buclă', 'Bucla de la spate'), ('interior', 'Interiorul textil')],
  {'Model': 'Geox, bocanci', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'neizolați, șiret și fermoar lateral, Geox Respira', 'Cod produs': ''})

w(8482,
  f'<p>{GEOX} are aici niște {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} roz, din material textil, foarte ușori, cu talpă din gumă și sistemul Geox Respira în trei straturi, cu perforații.</p>'
  '<p>Vârful și spatele călcâiului sunt moi, nu rigidizate, deci pantoful e flexibil pe picior și se îndoaie ușor la mers.</p>'
  '<p>E un model simplu, făcut să fie ușor:</p>'
  + L(('Material', 'textil, la exterior și la interior.'), ('Branț', 'textil.'), ('Talpă', 'din gumă.'), ('Greutate', 'model ultra ușor.'))
  + '<p>Numerele de pe site încep la 28 și urcă până la 39, deci modelul se găsește pentru copii de cam 4 ani în sus.</p>',
  [('model', 'Pantofi copii culoarea roz'), ('material', 'Model confectionat din material textil'), ('ultra ușor', 'Model ultra usor'), ('vârf', 'Cutie rotunda si moale'),
   ('călcâi', 'Spatele calcaiului moale'), ('branț', 'Brant textil'), ('talpă', 'Talpa din guma'), ('Respira', 'talpei in trei straturi cu sistemul de perforari')],
  {'Model': 'Geox, pantofi', 'Material': 'textil, talpă din gumă', 'Caracteristici': 'ultra ușori, vârf și călcâi moi, Geox Respira', 'Cod produs': ''})

w(8483,
  f'<p>{A("/brand/desigual/", "Desigual")} 25WGED01 este o {A("/categorie/geci-jachete/", "geacă de blugi pentru fete")}, albastră, cu motive cu personaje de basm, fără izolație și fără căptușeală. E o geacă de tranziție, pentru primăvară și toamnă.</p>'
  '<p>Croiala e simplă, iar materialul e mai ales bumbac (86%), cu puțin lyocell, poliester și viscoză, așa că se poartă ușor peste un tricou sau un hanorac subțire.</p>'
  '<p>Se încheie și se folosește ca o geacă de blugi clasică:</p>'
  + L(('Închidere', 'nasturi.'), ('Buzunare', 'două laterale și două la piept.'), ('Glugă', 'are.'), ('Bumbac', 'Better Cotton, cel puțin 50% din bumbac vine de la producători din această inițiativă.'))
  + '<p>Geaca vine în mărimile 104-164, potrivite copiilor de pe la 4 până pe la 14 ani.</p>',
  [('cod', '25WGED01'), ('culoare', 'albastru'), ('personaje', 'Personaje de basm'), ('neizolat', 'Model neizolat'), ('necăptușit', 'Captuseala: necaptusit'),
   ('tranziție', 'Izolare: tranzitional'), ('jeans', 'Material: jeans'), ('croială', 'Tăiere simplă'), ('compoziție', '86% Bumbac, 7% Lyocell, 5% Poliester , 2% Viscoza'),
   ('nasturi', 'Incheiere cu nasturi'), ('buzunare', 'Două buzunare laterale și două buzunare la piept'), ('glugă', 'Gluga: cu gluga'),
   ('Better Cotton', 'contin cel putin 50% bumbac de la un vanzator sau o marca apartinand initiativei Better Cotton')],
  {'Model': 'Desigual 25WGED01', 'Material': '86% bumbac, 7% lyocell, 5% poliester, 2% viscoză', 'Caracteristici': 'de tranziție, fără căptușeală, nasturi, patru buzunare, glugă', 'Cod produs': '25WGED01'},
  notes=['Titlul de pe site nu are culoare; pagina magazinului dă albastru.'])

w(8488,
  f'<p>{GEOX} J944GD sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} negri, din material sintetic, cu interior din textil și piele naturală. Au sistemul Anti Shock în talpă și tehnologia Geox Respira, cu talpă în trei straturi.</p>'
  '<p>Se leagă cu șireturi, dar au și fermoar, așa că se pot încălța fără să desfaci șiretul de fiecare dată: el rămâne reglat pe piciorul copilului.</p>'
  '<p>În rest, pantofii au:</p>'
  + L(('Vârf', 'ușor rigidizat.'), ('Călcâi', 'rigidizat la spate.'), ('Talpă', 'din gumă.'))
  + '<p>Pe site sunt numerele 24-35, pentru copii de aproximativ 2-11 ani.</p>',
  [('cod', 'J944GD.000HH'), ('culoare', 'Geox negru J944GD'), ('material', 'Model confectionat din material sintetic'), ('interior', 'Interiorul: Material textil, Piele naturala'),
   ('Anti Shock', 'Anti Shock este un sistem de absorbtie a socurilor'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('șireturi', 'Model legat cu sireturi'), ('fermoar', 'Incheiere cu fermoar'), ('vârf', 'Varful usor rigidizat'), ('călcâi', 'Spatele calcaiului rigidizat'), ('talpă', 'Talpa din guma')],
  {'Model': 'Geox J944GD', 'Material': 'sintetic, interior textil și piele naturală, talpă din gumă', 'Caracteristici': 'Anti Shock, Geox Respira, șireturi și fermoar', 'Cod produs': 'J944GD.000HH'},
  notes=['Titlul de pe site nu are culoare; pagina magazinului arată negru.'])

w(8490,
  f'<p>{PRIMIGI} PYR 14214 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași sport unisex")} bleumarin, din imitație de piele, cu talpă Vibram. Sunt gândiți pentru copiii foarte activi, care aleargă și se joacă afară.</p>'
  '<p>Vârful e lat și lasă loc degetelor, iar închiderea cu scai și șireturi elastice se ajustează repede, inclusiv pe un picior mai lat. Profilul e jos, sub gleznă.</p>'
  '<p>Talpa și interiorul sunt partea tehnică a modelului:</p>'
  + L(('Talpă', 'Vibram, profilată.'), ('Branț', 'cu formă anatomică.'), ('Interior', 'căptușit cu material textil.'), ('Contrefort', 'ușor rigidizat.'))
  + '<p>Pe site sunt numerele 30-33, de obicei pentru copii de 6-9 ani.</p>',
  [('cod', 'PYR 14214'), ('culoare', 'bleumarin'), ('material', 'confecționată din imitație de piele'), ('Vibram', 'Talpa Vibram'), ('activi', 'conceput pentru cei mai activi prichindei'),
   ('vârf', 'Vârful lat oferă spațiu pentru degete'), ('închidere', 'Sistemul de închidere cu scai și șireturile elastice'), ('profil', 'Profilul jos'),
   ('talpă profilată', 'Talpa profilată'), ('branț', 'Branțul amortizant cu formă anatomică'), ('interior', 'Interiorul căptușit cu material textil'), ('contrefort', 'Contrefortul ușor rigidizat')],
  {'Model': 'Primigi PYR 14214', 'Material': 'imitație de piele, interior textil, talpă sintetică Vibram', 'Caracteristici': 'scai și șireturi elastice, vârf lat, branț anatomic, profil jos', 'Cod produs': '14214'})

w(8498,
  f'<p>{A("/brand/wheat/", "Wheat")} 7378-927R este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă subțire unisex")}, roșie, din poliester, fără izolație și fără căptușeală, făcută pentru zilele mai blânde de primăvară și de toamnă.</p>'
  '<p>Fasonul e oversize: geaca vine largă și lasă loc de un pulover sau un hanorac dedesubt, iar mânecile se termină cu manșetă.</p>'
  '<p>Fermoarul e scurt, deci geaca se îmbracă pe jumătate peste cap:</p>'
  + L(('Închidere', 'fermoar scurt.'), ('Glugă', 'fixă.'), ('Guler', 'ridicat.'), ('Material', '100% poliester.'))
  + '<p>Între 98 și 140, mărimile acoperă cam vârsta de 3-10 ani.</p>',
  [('cod', '7378-927R GRS'), ('culoare', 'culoarea roșu'), ('neizolat', 'Model neizolat'), ('necăptușit', 'Captuseala: necaptusit'), ('oversize', 'Fason oversize'),
   ('fermoar', 'Închiderea cu fermoar scurt'), ('glugă, guler', 'Gulerul ridicat și gluga fixă'), ('manșetă', 'Finisaj din manseta'), ('material', '100% Poliester')],
  {'Model': 'Wheat 7378-927R', 'Material': '100% poliester', 'Caracteristici': 'fără izolație și căptușeală, oversize, fermoar scurt, glugă fixă', 'Cod produs': '7378-927R'})
print('lot 3 scris')
