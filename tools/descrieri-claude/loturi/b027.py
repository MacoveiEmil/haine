import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9652,
  f'<p>{PRIMIGI} PPE GTX 89344 sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme de zăpadă pentru băieți")}, verzi, izolate, din material textil și piele ecologică. Membrana GORE-TEX® e foarte subțire, impermeabilă și rezistentă la vânt, deci piciorul rămâne uscat prin zăpadă și pe lapoviță.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, așa că cizma vine bine și pe un picior mai lat, iar velcro-ul se desface și se închide repede, fără ajutor.</p>'
  '<p>Înăuntru e cald, iar dedesubt talpa e făcută pentru iarnă:</p>'
  + L(('Interior', 'fleece, cu căptușeală textilă.'), ('Talpă', 'din cauciuc, rezistentă la uzură, cu absorbția șocului.'), ('Partea de sus', 'rigidizată.'))
  + '<p>Numerele 24-38 se poartă, de obicei, de la 2 ani în sus.</p>',
  [('model', 'Primigi Cizme de iarna copii culoarea verde, PPE GTX 89344'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinatia materialului textil cu pielea ecologica'), ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('fleece', 'Interior fleece'), ('căptușeală', 'Model cu captuseala textila'), ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'),
   ('șoc', 'Absorbtia socului'), ('rigidizat', 'Partea superioară rigidizată')],
  {'Model': 'Primigi PPE GTX 89344', 'Material': 'textil și piele ecologică, interior fleece, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, izolate, velcro, cutie lată a degetelor', 'Cod produs': 'PPE GTX 89344'})

w(9653,
  f'<p>{A("/brand/donsje/", "Donsje")} 4119500 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă matlasată unisex")}, roz, uni, ușoară, cu umplutură sintetică și izolație termică ușoară, pentru zilele mai reci din sezonul de tranziție. Se închide cu nasturi, ca o haină clasică.</p>'
  '<p>Croiala e regulară, iar lungimea ajunge până la șolduri, deci acoperă trunchiul fără să încurce la joacă. Nu are glugă, așa că se poartă ușor peste un hanorac sau sub o căciulă.</p>'
  '<p>Materialele sunt alese pentru purtat des:</p>'
  + L(('Căptușeală', 'completă, din bumbac.'), ('Țesătură', 'netedă, 100% poliester, ușor de îngrijit.'), ('Buzunare', 'în față.'))
  + '<p>Mărimile 98-140 sunt pentru copii de cam 3-10 ani.</p>',
  [('model', 'Donsje Geacă petrecută pentru copii roz 4119500'), ('matlasat', 'Construcție matlasată'), ('ușor', 'propunere ușoară pentru sezonul de tranziție'),
   ('umplutură', 'Umplutură sintetică'), ('izolație', 'Izolație termică ușoară'), ('zile reci', 'zilele mai reci'), ('uni', 'modelul uni'), ('nasturi', 'Închidere cu nasturi'),
   ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'), ('fără glugă', 'Fără glugă'), ('căptușeală', 'căptușeala completă din bumbac natural'),
   ('țesătură', 'structura netedă a materialului favorizează îngrijirea ușoară'), ('poliester', '100% Poliester'), ('buzunare', 'poziționate în față')],
  {'Model': 'Donsje 4119500', 'Material': '100% poliester, căptușeală 100% bumbac', 'Caracteristici': 'matlasată, izolație ușoară, nasturi, fără glugă', 'Cod produs': '4119500'})

w(9656,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261128 sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} gri, din piele naturală, cu profil jos, căptușiți cu lână, deci țin piciorul cald în zilele mai reci. Sunt făcuți în parteneriatul Biomecanics Podology.</p>'
  '<p>Aricii și cureaua reglabilă strâng pantoful după piciorul copilului, mai lat sau mai îngust, iar branțul din lână se scoate, deci se poate usca separat sau folosi la măsurat piciorul.</p>'
  '<p>Ce ține piciorul drept la primii pași:</p>'
  + L(('Stabilizatori', 'laterali.'), ('Călcâi', 'întărit.'), ('Talpă', 'flexibilă, din cauciuc, se îndoaie odată cu piciorul.'))
  + '<p>Mărimile 18-25 sunt, în general, pentru 1-3 ani.</p>',
  [('model', 'Biomecanics Încălțăminte pentru copii din piele gri 261128'), ('piele', 'Partea superioară din piele naturală'), ('profil', 'profil jos'),
   ('lână', 'Căptușeală interioară din lână ajută la menținerea căldurii'), ('zile reci', 'zilele mai reci'), ('parteneriat', 'Parteneriatul Biomecanics Podology'),
   ('arici', 'Închidere cu arici și curea reglabilă facilitează încălțarea rapidă și ajustarea la picior'), ('branț', 'Branț detașabil și respirabil, din lână'),
   ('stabilizatori', 'Stabilizatori laterali și călcâi întărit'), ('talpă', 'Talpă flexibilă din cauciuc permite flexarea liberă a piciorului')],
  {'Model': 'Biomecanics 261128', 'Material': 'piele naturală, căptușeală din lână, talpă din cauciuc', 'Caracteristici': 'arici și curea reglabilă, branț detașabil din lână, stabilizatori laterali', 'Cod produs': '261128'})

w(9657,
  f'<p>{GEOX} FLEXYPER MINI sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} violet, ușori, cu partea de sus din material textil și sintetic, ușor de întreținut. Tehnologia Geox Respira™ scoate umezeala din pantof în timpul joacei.</p>'
  '<p>Profilul scurt lasă glezna liberă, iar aricii permit încălțatul și descălțatul rapid, deci copilul învață să se descurce singur.</p>'
  '<p>Înăuntru și sub picior:</p>'
  + L(('Branț', 'moale, din material textil.'), ('Interior', 'textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-27 sunt pentru cei mici, de pe la 1 până pe la 4 ani.</p>',
  [('model', 'Geox FLEXYPER MINI sneakers pentru copii violet B566NB.0AJAS'), ('ușor', 'combină lejeritatea cu funcționalitatea'), ('material', 'Partea superioară din material textil și sintetic'),
   ('întreținere', 'ușurința în întreținere'), ('Respira', 'Tehnologia GEOX Respira™ favorizează evacuarea umezelii'), ('profil', 'Profilul scurt al încălțămintei'),
   ('arici', 'Sistemul de închidere cu arici facilitează încălțarea și descălțarea rapidă'), ('autonomie', 'susținând autonomia copilului'),
   ('branț', 'Branț moale din material textil'), ('interior', 'Material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox FLEXYPER MINI', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira™, arici, profil scurt', 'Cod produs': 'B566NB.0AJAS'})

w(9659,
  f'<p>{PRIMIGI} PPTGT 23918 sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "ghete de trekking pentru băieți")}, gri, înalte, din piele întoarsă și material sintetic, pentru drumeții la munte și prin pădure. Membrana GORE-TEX® ține apa și vântul afară, iar talpa cu bandă de rulare e făcută pentru teren variat.</p>'
  '<p>Înșiretarea rapidă se strânge și se slăbește ușor, deci gheata se potrivește pe picioare diferite ca lățime. Colaborarea Primigi × SIPeP ține cont de dezvoltarea piciorului copilului.</p>'
  '<p>Pe traseu, contează ce e sub călcâi și în talpă:</p>'
  + L(('Călcâi', 'întărit.'), ('Shock Absorber', 'tehnologie din talpă care reduce șocurile.'), ('Interior', 'material textil.'))
  + '<p>Numerele 26-40 acoperă copiii de la aproximativ 3 ani în sus.</p>',
  [('model', 'Primigi Încălțăminte de trekking pentru copii gri PPTGT 23918'), ('înalt', 'încălțăminte outdoor înaltă'), ('material', 'Partea superioară din piele întoarsă și material sintetic'),
   ('drumeții', 'drumeții montane și aventuri în pădure'), ('GORE-TEX', 'Membrana GORE-TEX® contribuie la protecția împotriva apei și vântului'),
   ('talpă', 'Talpă cu bandă de rulare'), ('teren', 'teren variat'), ('șireturi', 'Sistem de înșiretare rapidă'), ('SIPeP', 'Colaborarea Primigi × SIPeP'),
   ('dezvoltare', 'ia în considerare dezvoltarea piciorului copilului'), ('călcâi', 'Călcâi întărit'), ('Shock Absorber', 'Tehnologia Shock Absorber din talpă contribuie la reducerea șocurilor'),
   ('interior', 'Material textil')],
  {'Model': 'Primigi PPTGT 23918', 'Material': 'piele întoarsă și sintetic, interior textil', 'Caracteristici': 'GORE-TEX®, înșiretare rapidă, Shock Absorber, talpă cu bandă de rulare', 'Cod produs': 'PPTGT 23918'})

w(9666,
  f'<p>{GEOX} CIBERDRON Batman sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} negri, inspirați de Batman, cu lumini încorporate care îl fac pe copil mai vizibil seara. Partea de sus e din imitație de piele și material textil, iar tehnologia Geox Respira™ scoate umiditatea din pantof.</p>'
  '<p>Șireturile elastice și aricii se reglează repede pe picior, deci copilul se încalță singur, iar gulerul întărit cuprinde glezna.</p>'
  '<p>Sub și în jurul piciorului:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 28-35 merg, cam între 4 și 11 ani.</p>',
  [('model', 'Geox CIBERDRON Batman sneakers pentru copii negri J66LBE.0BC14'), ('lumini', 'Lumini încorporate adaugă dinamism și vizibilitate'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia GEOX Respira™ sprijină eliminarea umidității'),
   ('închidere', 'Șireturi elastice și închidere cu arici facilitează încălțarea rapidă și ajustarea'), ('guler', 'Gulerul superior întărit îmbrățișează delicat glezna'),
   ('călcâi', 'Călcâi întărit'), ('interior', 'Interiorul din material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox CIBERDRON Batman', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'lumini încorporate, șireturi elastice și arici, Geox Respira™', 'Cod produs': 'J66LBE.0BC14'})

w(9669,
  f'<p>{A("/brand/napapijri/", "Napapijri")} RAINFOREST WI 2 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă unisex")} bleumarin, ușor izolată cu umplutura Comfortemp®, din poliester 100% reciclat, care își păstrează proprietățile și când aerul e umed. E pentru zilele cu temperaturi mai scăzute.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri, deci geaca stă lejer și peste un pulover. Gulerul ridicat și gluga fixă țin frigul departe de gât și de cap.</p>'
  '<p>Materialele și detaliile:</p>'
  + L(('Material', '100% poliamidă, cu acoperire din poliuretan.'), ('Buzunar', 'pe piept.'), ('Căptușeală', '100% poliester.'))
  + '<p>Mărimile 134-140 până la 168-172 sunt pentru copii de în jur de 9-15 ani.</p>',
  [('model', 'Napapijri Geaca copii RAINFOREST WI 2 culoarea albastru marin, NP0A4HHK1761'), ('izolat', 'Model usor izolat'),
   ('Comfortemp', 'Un model cu umplutură Comfortemp®, care este o izolație inovatoare din poliester reciclat 100%'),
   ('umiditate', 'își păstrează toate proprietățile și în condiții de umiditate ridicată a aerului'), ('frig', 'temperaturi mai scăzute'),
   ('croială', 'Tăiere simplă, fără blocare'), ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('material', '100% Poliamida'), ('acoperire', 'Acoperire: Poliuretan'),
   ('buzunar', 'Buzunar pe piept'), ('căptușeală', 'Captuseala: 100% Poliester')],
  {'Model': 'Napapijri RAINFOREST WI 2', 'Material': '100% poliamidă cu acoperire din poliuretan, căptușeală și umplutură poliester', 'Caracteristici': 'ușor izolată, Comfortemp®, glugă fixă, guler ridicat', 'Cod produs': 'NP0A4HHK1761'},
  notes=['Magazinul scrie „căptușeală din lână”, dar compoziția dă căptușeală 100% poliester; am folosit compoziția.'])

w(9670,
  f'<p>Pantofii {GEOX} CASEY J1620E sunt {A("/categorie/incaltaminte-pantofi/", "pantofi pentru fete")} negri, din imitație de piele lăcuită, cu un detaliu decorativ în față. Talpa e antialunecare și are sistemul Geox Respira, cu trei straturi perforate.</p>'
  '<p>Se închid cu velcro, deci se încalță și se scot repede, iar velcro-ul se strânge după lățimea piciorului. Spatele călcâiului e rigidizat și ține piciorul pe loc.</p>'
  '<p>Pantoful e construit simplu:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Branț', 'din piele naturală.'), ('Talpă', 'din material sintetic, antialunecare.'))
  + '<p>Mărimile 28-35 se potrivesc, de regulă, copiilor de 4-11 ani.</p>',
  [('model', 'Geox Pantofi copii CASEY culoarea negru, J1620E.000HH'), ('lăcuit', 'imitatie de piele lacuita'), ('decor', 'Detaliu decorativ in fata'),
   ('antialunecare', 'Talpa antialunecare'), RESPIRA, ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('călcâi', 'Spatele calcaiului rigidizat'), ('vârf', 'Cutie rotunda, intarita'), ('branț', 'Introduceti: Piele naturala'), ('talpă', 'Talpa: Material sintetic')],
  {'Model': 'Geox CASEY', 'Material': 'imitație de piele lăcuită, branț din piele naturală, talpă sintetică', 'Caracteristici': 'velcro, talpă antialunecare, Geox Respira', 'Cod produs': 'J1620E.000HH'})

w(9681,
  f'<p>Geaca {A("/brand/guess/", "Guess")} K5BL08 WGL60 este o {A("/categorie/geci-jachete/", "geacă reversibilă pentru fete")}, portocalie, ușor izolată, pentru sezonul de tranziție. O față e din imitație de blană, cealaltă din țesătură netedă, iar geaca se poartă pe oricare dintre ele.</p>'
  '<p>Nu are glugă, dar gulerul înalt se închide cu un fermoar scurt și ține gâtul la adăpost de vânt.</p>'
  '<p>Pe ambele fețe, geaca are loc pentru mâini și mărunțișuri:</p>'
  + L(('Buzunare', 'două, laterale.'), ('Buzunare interioare', 'da.'), ('Material', 'poliuretan 100% și poliester 100%.'))
  + '<p>Mărimile 88-96 până la 122-125 corespund, cu aproximație, vârstei de 1-7 ani.</p>',
  [('model', 'Guess Geacă reversibilă pentru copii culoarea portocaliu, K5BL08 WGL60'), ('izolat', 'Model ușor izolat'), ('tranziție', 'Izolare: tranzitional'),
   ('materiale', 'combinație de imitație de blană și țesătură netedă'), ('reversibil', 'Model cu două fețe, asigurând funcționalitate deplină în utilizare pe ambele părți'),
   ('fără glugă', 'Gluga: fara gluga'), ('guler', 'Guler înalt cu fermoar scurt'), ('buzunare', 'Două buzunare laterale'), ('buzunare interioare', 'Buzunare interioare'),
   ('material 1', 'Material 1: 100% Poliuretan'), ('material 2', 'Material 2: 100% Poliester')],
  {'Model': 'Guess K5BL08 WGL60', 'Material': 'imitație de blană (100% poliuretan) și țesătură netedă (100% poliester)', 'Caracteristici': 'reversibilă, ușor izolată, guler înalt cu fermoar, fără glugă', 'Cod produs': 'K5BL08 WGL60'})
