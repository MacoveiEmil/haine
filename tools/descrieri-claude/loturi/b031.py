import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
BIO = A('/brand/biomecanics/', 'Biomecanics')

w(9796,
  f'<p>Pantofii {BIO} 261120 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} bleumarin, din piele naturală, cu talpă flexibilă din cauciuc și design simplu, care merge la ținute casual și la cele mai clasice. Sunt făcuți pentru copiii activi.</p>'
  '<p>Vârful rotund lasă loc degetelor, iar aricii se strâng după piciorul copilului și se desfac repede. Branțul textil se scoate, deci piciorul se poate măsura pe el când crește.</p>'
  '<p>Ce ține piciorul în poziție:</p>'
  + L(('Stabilizatori', 'laterali.'), ('Călcâi', 'întărit.'), ('Guler', 'moale, nu irită glezna.'), ('Talpă', 'subțire, flexibilă.'))
  + '<p>Numerele 19-25 se potrivesc copiilor de pe la 1 până pe la 3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele bleumarin 261120'), ('piele', 'Partea superioară din piele naturală'), ('talpă', 'Talpă flexibilă din cauciuc'),
   ('design', 'Designul lor universal'), ('casual', 'de la cele casual la cele mai clasice'), ('activi', 'proiectată pentru copiii activi'),
   ('vârf', 'Vârf rotund, întărit oferă spațiu pentru degete'), ('arici', 'Închidere cu arici facilitează încălțarea și descălțarea rapidă'),
   ('branț', 'Branț textil detașabil'), ('stabilizatori', 'Stabilizatori laterali'), ('călcâi', 'Călcâi întărit'), ('guler', 'Guler moale al părții superioare minimizează riscul de iritații'),
   ('subțire', 'Grosime mică a tălpii')],
  {'Model': 'Biomecanics 261120', 'Material': 'piele naturală, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, branț detașabil, stabilizatori laterali', 'Cod produs': '261120'})

w(9806,
  f'<p>{A("/brand/liewood/", "Liewood")} Maddy Snowsuit LW20051 este o {A("/categorie/bebe-imbracaminte-salopete-compleuri/", "salopetă de zăpadă pentru bebeluși")}, bleumarin, din poliester reciclat certificat GRS, ușor izolată cu umplutură Thermolite® Ecomade și căptușită cu fleece moale. Cu impermeabilitate de 12 000 mm, e făcută pentru zăpadă și sporturi de iarnă.</p>'
  '<p>Croiala e simplă, dreaptă, iar manșetele elastice strâng la încheieturi și lasă mănușile să intre pe dedesubt. Cracii au bretele elastice care trec pe sub gheată, deci nu se ridică în zăpadă.</p>'
  '<p>Pentru joaca lungă afară, salopeta mai are:</p>'
  + L(('Glugă', 'detașabilă, cu guler ridicat.'), ('Fermoar', 'frontal, cu protecție pentru bărbie și clapă împotriva vântului.'), ('Ventilație', 'orificii la subraț.'))
  + '<p>Mărimile 80-128 sunt pentru copii de aproximativ 1-8 ani.</p>',
  [('model', 'Liewood Salopetă copii Maddy Snowsuit LW20051'), ('reciclat', '100% Poliester reciclat'), ('GRS', 'GLOBAL RECYCLED STANDARD (GRS)'), ('izolat', 'Model ușor izolat'),
   ('Thermolite', 'Thermolite® Halmingul Ecomade'), ('fleece', 'Interiorul este căptușit cu un fleece moale'), ('impermeabil', 'Impermeabilitate: 12 000 mm'),
   ('iarnă', 'Tip de activitate: Sporturi de iarnă'), ('croială', 'Tăiere simplă, fără blocare'), ('manșete', 'Manșetele elastice se potrivesc perfect la încheieturile tale'),
   ('mănuși', 'îți permit să bagi cu ușurință manșetele mănușilor dedesubt'), ('bretele', 'Picioare finisate cu bretele elastice pentru toc'),
   ('glugă', 'Gluga detasabila'), ('guler', 'Gulerul ridicat'), ('fermoar', 'Fermoar frontal cu barbie și clapă interioară rezistentă la vânt'), ('ventilație', 'La subrat orificii de ventilare')],
  {'Model': 'Liewood Maddy Snowsuit', 'Material': '100% poliester reciclat (GRS), căptușeală fleece', 'Caracteristici': 'Thermolite® Ecomade, 12 000 mm, glugă detașabilă, bretele sub talpă', 'Cod produs': 'LW20051'},
  notes=['Magazinul dă culoarea albastru; titlul spune bleumarin.', 'Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(9808,
  f'<p>{PRIMIGI} PWIGT 88815 sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")}, aurii, ușor izolate, din material textil, piele naturală și piele întoarsă. Au membrana GORE-TEX®, subțire, impermeabilă și rezistentă la vânt, pentru iarnă și zăpadă udă.</p>'
  '<p>Velcro-ul se închide repede, iar cutia lată a degetelor nu le ciupește, deci cizma vine bine și pe un picior mai lat. Partea de sus ridicată rigidizează glezna pe teren denivelat.</p>'
  '<p>Cizma mai are:</p>'
  + L(('Călcâi', 'contrafort rigidizat.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'exterioară, din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 25-30 sunt pentru copii de în jur de 2-7 ani.</p>',
  [('model', 'Primigi Cizme de iarnă copii culoarea auriu, PWIGT 88815'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolare', 'Izolare usoara'),
   ('material', 'combinație de material textil, piele naturală și piele întoarsă'), ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant'),
   ('velcro', 'Fixare: cu scai'), ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'),
   ('teren', 'suprafețe neuniforme'), ('călcâi', 'Contorul de călcâi rigidizat'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Primigi PWIGT 88815', 'Material': 'textil, piele naturală și piele întoarsă, interior textil', 'Caracteristici': 'GORE-TEX®, ușor izolate, velcro, cutie lată', 'Cod produs': 'PWIGT 88815'},
  notes=['Magazinul precizează că rezistența la apă nu garantează impermeabilitatea completă.'])

w(9811,
  f'<p>{GEOX} ECLYPER J66LRA sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, sport, cu partea de sus din imitație de piele și material textil. Membrana Geox Respira™ din talpă scoate umiditatea și, în același timp, ține apa să nu intre prin talpă.</p>'
  '<p>Aricii permit încălțatul rapid, fără șireturi, iar gulerul ușor întărit cuprinde glezna și ajută pantoful să stea bine pe picior.</p>'
  '<p>Restul e gândit pentru mișcare:</p>'
  + L(('Călcâi', 'întărit.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 32-35 sunt, de obicei, pentru 8-11 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi J66LRA.0BCQ6'), ('sport', 'încălțăminte sport pentru copii'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('membrană', 'Membrana GEOX Respira™ elimină activ umiditatea la exterior, protejând în același timp interiorul pantofului de apă'),
   ('arici', 'Închiderea practică cu arici facilitează încălțarea și descălțarea rapidă'), ('guler', 'Gulerul ușor întărit al părții superioare îmbrățișează delicat glezna'),
   ('călcâi', 'Călcâiul întărit'), ('interior', 'Interiorul căptușit cu material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox ECLYPER', 'Material': 'imitație de piele și textil, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira™, arici', 'Cod produs': 'J66LRA.0BCQ6'})

w(9812,
  f'<p>{GEOX} ECLYPER B365MA sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} albi, ușori, din material textil și sintetic, ușor de întreținut. Membrana Geox Respira™ scoate umezeala și păstrează picioarele uscate, pentru activitățile zilnice și joacă.</p>'
  '<p>Închiderea cu arici îl lasă pe cel mic să se încalțe repede, iar călcâiul întărit ține piciorul pe loc când aleargă.</p>'
  '<p>Înăuntru, pantoful e simplu:</p>'
  + L(('Interior', 'căptușit cu material textil.'), ('Branț', 'din material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 20-27 sunt pentru copii de aproximativ 1-4 ani.</p>',
  [('model', 'Geox ECLYPER sneakers pentru copii albi B365MA.0BCKC'), ('ușor', 'încălțăminte ușoară'), ('material', 'Partea superioară din material textil și sintetic , ușoară și ușor de întreținut'),
   ('Respira', 'Tehnologie GEOX Respira™ cu membrană care favorizează eliminarea umezelii, menținând picioarele uscate'), ('zilnic', 'activități zilnice și joacă'),
   ('arici', 'Închidere practică cu arici'), ('călcâi', 'Călcâi întărit'), ('interior', 'Interior căptușit cu material textil'), ('branț', 'Branț din material textil'), ('talpă', 'Talpă plată din cauciuc')],
  {'Model': 'Geox ECLYPER', 'Material': 'textil și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira™, arici', 'Cod produs': 'B365MA.0BCKC'})

w(9813,
  f'<p>{A("/brand/mayoral/", "Mayoral")} 7440 este o {A("/categorie/geci-jachete/", "geacă de iarnă pentru fete")}, maro, uni, matlasată, cu umplutură sintetică groasă și căptușeală completă, pentru zilele reci. Gulerul din blană artificială apără gâtul de frig.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, deci trunchiul rămâne acoperit la joacă. Baza și manșetele cu nervuri strâng geaca pe corp și opresc vântul.</p>'
  '<p>Pentru zilele de iarnă, mai are:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale, tip slip-on, pentru mâini reci.'), ('Material', '99% poliester, 1% elastan.'))
  + '<p>Mărimile 128-167 merg, în general, la copii de 8-14 ani.</p>',
  [('model', 'Mayoral Geacă petrecută pentru copii maro 7440'), ('uni', 'Model uni'), ('matlasat', 'Finisajul matlasat'), ('umplutură', 'Umplutură sintetică groasă'),
   ('căptușeală', 'Căptușeală completă'), ('iarnă', 'zilele de iarnă'), ('blană', 'Guler din blană artificială'), ('gât', 'protejarea gâtului de frig'),
   ('croială', 'Croială regulară'), ('lungime', 'Lungimea până la șolduri'), ('nervuri', 'Bază și manșete cu nervuri'), ('vânt', 'protecție împotriva vântului'),
   ('fermoar', 'Închidere cu fermoar'), ('buzunare', 'Buzunare laterale tip slip-on'), ('mâini', 'încălzirea mâinilor'), ('material', '99% Poliester, 1% Elastan')],
  {'Model': 'Mayoral 7440', 'Material': '99% poliester, 1% elastan', 'Caracteristici': 'matlasată, umplutură groasă, guler din blană artificială, manșete cu nervuri', 'Cod produs': '7440'})

w(9818,
  f'<p>{BIO} 261130 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} bleumarin, din piele naturală și material sintetic, în stil casual, făcuți în parteneriatul Biomecanics Podology, cu podologii. Sunt pentru primii pași ai celor mici.</p>'
  '<p>Profilul gulerului e scurt, iar spațiul mărit din zona degetelor le lasă să stea natural. Aricii se închid repede și strâng pantoful după picior.</p>'
  '<p>Dedesubt și înăuntru:</p>'
  + L(('Călcâi', 'întărit.'), ('Branțuri', 'detașabile, se scot la curățat.'), ('Interior', 'material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Mărimile 18-25 sunt, cu aproximație, pentru 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele bleumarin 261130'), ('material', 'Piele naturală, Material sintetic'), ('casual', 'stilul casual streetwear'),
   ('parteneriat', 'Tehnologia Biomecanics Podology Partnership'), ('podologi', 'creat în colaborare cu podologii'), ('primii pași', 'primii pași'),
   ('profil', 'Profilul scurt al gulerului'), ('degete', 'Spațiul mărit în zona degetelor favorizează poziționarea naturală a degetelor'),
   ('arici', 'Sistemul practic de închidere cu arici facilitează încălțarea și descălțarea rapidă'), ('călcâi', 'Călcâiul întărit'),
   ('branțuri', 'Branțurile detașabile'), ('interior', 'Interiorul din material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Biomecanics 261130', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, branțuri detașabile, spațiu mărit la degete', 'Cod produs': '261130'})

w(9819,
  f'<p>Sandalele {GEOX} SANDAL KARLY J6535F sunt {A("/categorie/incaltaminte-sandale/", "sandale pentru fete")} albe, casual, pentru zilele de vară și joaca în aer liber. Partea de sus e din material sintetic, care se curăță ușor, iar tehnologia Geox Respira ține picioarele uscate.</p>'
  '<p>Catarama permite reglajul precis al sandalei, deci se strânge și pe un picior îngust, și pe unul mai plin.</p>'
  '<p>Din ce sunt făcute:</p>'
  + L(('Branț', 'din piele naturală.'), ('Interior', 'material sintetic.'), ('Talpă', 'din cauciuc, rezistentă la abraziune.'))
  + '<p>Numerele 28-35 sunt, în mare, pentru copii de 4-11 ani.</p>',
  [('model', 'Geox Sandale pentru copii SANDAL KARLY albe J6535F.054AJ'), ('vară', 'ideale pentru zilele de vară și activitățile în aer liber'), ('casual', 'Stilul casual'),
   ('material', 'Partea superioară din material sintetic facilitează curățarea'), ('Respira', 'Tehnologia Geox Respira permite termoreglarea naturală a picioarelor, menținându-le uscate'),
   ('cataramă', 'Închiderea cu cataramă permite ajustarea precisă a sandalelor'), ('branț', 'Branțul din piele naturală'), ('interior', 'Material sintetic'),
   ('talpă', 'Talpa din cauciuc'), ('abraziune', 'este rezistentă la abraziune')],
  {'Model': 'Geox SANDAL KARLY', 'Material': 'sintetic, branț din piele naturală, talpă din cauciuc', 'Caracteristici': 'cataramă, Geox Respira', 'Cod produs': 'J6535F.054AJ'})

w(9821,
  f'<p>Încălțămintea de iarnă {PRIMIGI} PTIGT 23547 în varianta bleumarin intră la {A("/categorie/baieti-incaltaminte-ghete-cizme/", "ghete pentru băieți")}: înalte, din piele întoarsă și material textil, cu membrana GORE-TEX® contra umezelii și vântului. Căptușeala textilă ține de cald la joaca zilnică în zăpadă și la plimbările de iarnă.</p>'
  '<p>Pielea întoarsă se adaptează la forma piciorului, iar aricii permit încălțatul fără ajutor, deci cel mic se pregătește singur de ieșit afară.</p>'
  '<p>Ce mai e de știut:</p>'
  + L(('Primigi × SIPeP', 'tehnologie dezvoltată cu podologi.'), ('Călcâi', 'întărit.'), ('Talpă', 'din cauciuc.'))
  + '<p>Numerele 25-29 se poartă, de obicei, între 2 și 5 ani.</p>',
  [('model', 'Primigi Încălțăminte de iarnă pentru copii bleumarin PTIGT 23547'), ('înalt', 'încălțăminte înaltă pentru copii'), ('material', 'Partea superioară din piele întoarsă și material textil'),
   ('GORE-TEX', 'Membrana GORE-TEX® oferă protecție împotriva umezelii și vântului'), ('căptușeală', 'Căptușeala interioară călduroasă din material textil'),
   ('zăpadă', 'joaca zilnică în zăpadă și plimbările de iarnă'), ('adaptare', 'adaptându-se la forma piciorului'),
   ('arici', 'Închiderea cu arici facilitează încălțarea și descălțarea ușoară'), ('SIPeP', 'Tehnologia Primigi × SIPeP'), ('podologi', 'dezvoltată în colaborare cu podologi'),
   ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa din cauciuc')],
  {'Model': 'Primigi PTIGT 23547', 'Material': 'piele întoarsă și textil, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, arici, Primigi × SIPeP', 'Cod produs': 'PTIGT 23547'})

w(9824,
  f'<p>Cizmele de iarnă {GEOX} de mai jos sunt {A("/categorie/ghete-cizme/", "cizme pentru fete")} negre, izolate, din material textil și sintetic, cu membrana Amphibiox®, care protejează și talpa, și partea de sus. Așa, piciorul rămâne uscat în zăpadă și pe ploaie, nu doar pe dedesubt.</p>'.replace(' de mai jos', '')
  + '<p>Fermoarul face încălțatul ușor, iar spatele călcâiului rigidizat ține piciorul în cizmă. Talpa are și sistemul Geox Respira, în trei straturi cu perforări.</p>'
  '<p>Detaliile de construcție:</p>'
  + L(('Vârf', 'cutie rotundă, întărită.'), ('Talpă', 'din gumă.'), ('Interior', 'textil.'))
  + '<p>Numerele 28-35 sunt, de regulă, pentru copii de 4-11 ani.</p>',
  [('model', 'Geox Cizme de iarnă copii culoarea negru'), ('izolat', 'Model Izolat'), ('material', 'combinatia materialului textil cu cel sintetic'),
   ('Amphibiox', 'Tehnologia Amphibiox®'), ('protecție', 'protejeaza atat talpa exterioara, cat si cea superioara'), ('fermoar', 'Fixare: cu fermoar'),
   ('călcâi', 'Spatele calcaiului rigidizat'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'), ('vârf', 'Cutie rotunda, intarita'),
   ('talpă', 'Talpa din guma'), ('interior', 'Interior textil')],
  {'Model': 'Geox (cizme de iarnă)', 'Material': 'textil și sintetic, interior textil, talpă din gumă', 'Caracteristici': 'Amphibiox®, izolate, fermoar, Geox Respira', 'Cod produs': ''})
