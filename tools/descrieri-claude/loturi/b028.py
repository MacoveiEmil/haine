import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIMIGI = A('/brand/primigi/', 'Primigi')
REIMA = A('/brand/reima/', 'Reima')
GTX = ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant')

w(9684,
  f'<p>Geaca {A("/brand/calvin-klein-jeans/", "Calvin Klein Jeans")} IB0IB02628 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, bej, ușor izolată, din poliester reciclat cu suprafață netedă. Fermoarul pe toată lungimea are o clapă interioară împotriva furtunii, care oprește vântul să treacă printre dinți.</p>'
  '<p>Croiala e lejeră, oversize, cu umerii coborâți pe mânecă, deci geaca lasă loc unui hanorac dedesubt și vine comod și unui copil mai plinuț.</p>'
  '<p>Fără glugă, geaca se bazează pe câteva detalii simple:</p>'
  + L(('Guler', 'moale.'), ('Buzunare', 'două, în față.'), ('Căptușeală', 'cu izolație ușoară.'), ('Material', '100% poliester reciclat.'))
  + '<p>Mărimile 128-176 se potrivesc, în general, copiilor de 8-16 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă copii culoarea bej, IB0IB02628'), ('tranziție', 'Izolare: tranzitional'), ('izolat', 'Model usor izolat pe captuseala'),
   ('neted', 'Model ușor confecționat din material neted'), ('fermoar', 'Închidere cu fermoar pe toată lungimea cu clapă interioară împotriva furtunii'),
   ('croială', 'Tăiere lejeră, fără blocare'), ('oversize', 'Fit: oversize'), ('umeri', 'Croiala la mânecă cu o linie coborâtă a umerilor'), ('fără glugă', 'Gluga: fara gluga'),
   ('guler', 'Model cu guler moale'), ('buzunare', 'Două buzunare în față'), ('material', '100% Poliester reciclat')],
  {'Model': 'Calvin Klein Jeans IB0IB02628', 'Material': '100% poliester reciclat', 'Caracteristici': 'ușor izolată, oversize, clapă împotriva furtunii, fără glugă', 'Cod produs': 'IB0IB02628'})

w(9685,
  f'<p>{A("/brand/mayoral/", "Mayoral")} 2437 este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă reversibilă pentru bebeluși")}, maro, matlasată, cu o față cu model floral, deci se poartă în două feluri. Umplutura ușoară din puf sintetic o face potrivită pentru zilele de tranziție, când e răcoare.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar tivul și manșetele cu bordură elastică se strâng pe corp, ca vântul să nu intre pe sub geacă la un copil mic.</p>'
  '<p>Pentru plimbări pe vânt și burniță, geaca are:</p>'
  + L(('Glugă', 'integrată, apără capul de vânt și ploaie ușoară.'), ('Buzunare', 'laterale, cu închidere.'), ('Închidere', 'fermoar.'), ('Material', '56% poliester, 44% poliamidă.'))
  + '<p>Mărimile 74-104 sunt pentru cei mici de pe la 9 luni până pe la 4 ani.</p>',
  [('model', 'Mayoral Jachetă reversibilă pentru copii maro 2437'), ('reversibil', 'Construcția reversibilă permite o schimbare rapidă a stilului'), ('floral', 'Modelul floral'),
   ('matlasat', 'matlasarea'), ('puf sintetic', 'Umplutura ușoară din puf sintetic'), ('tranziție', 'zilele de tranziție'), ('croială', 'Croiala regulară'),
   ('lungime', 'Lungimea până la șolduri'), ('elastic', 'Tivul și manșetele cu bordură elastică'), ('glugă', 'Gluga integrată constituie o protecție suplimentară pentru cap împotriva vântului și a ploilor ușoare'),
   ('buzunare', 'Buzunarele laterale cu închidere'), ('fermoar', 'Sistemul de închidere cu fermoar'), ('material', '56% Poliester, 44% Poliamidă')],
  {'Model': 'Mayoral 2437', 'Material': '56% poliester, 44% poliamidă, umplutură și căptușeală poliester', 'Caracteristici': 'reversibilă, matlasată, glugă integrată, tiv și manșete elastice', 'Cod produs': '2437'})

w(9687,
  f'<p>{GEOX} KALISPERA J744GI sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, cu profil înalt și imprimeu decorativ, în stil casual. Partea de sus e din imitație de piele și material textil, iar membrana microporoasă Geox Respira™ scoate umiditatea din pantof.</p>'
  '<p>Șireturile și aricii lucrează împreună, deci pantoful se strânge exact pe picior, mai îngust sau mai lat. Branțurile din piele naturală se scot, iar pe ele se poate măsura piciorul.</p>'
  '<p>Profilul înalt e completat de:</p>'
  + L(('Călcâi', 'ușor întărit.'), ('Interior', 'căptușit cu material textil.'), ('Talpă', 'plată, din cauciuc.'))
  + '<p>Numerele 24-35 sunt, cu aproximație, pentru 2-11 ani.</p>',
  [('model', 'Geox KALISPERA sneakers pentru copii roz J744GI.0AU54'), ('profil', 'Profilul înalt al părții superioare'), ('imprimeu', 'Imprimeul decorativ'), ('casual', 'Stilul lor casual'),
   ('material', 'Partea superioară din imitație de piele și material textil'), ('Respira', 'Tehnologia Geox Respira™ cu membrană microporoasă favorizează eliminarea umidității'),
   ('închidere', 'Combinația dintre șireturi și închidere cu arici permite o ajustare precisă a încălțămintei pe picior'), ('branț', 'Branțurile detașabile din piele naturală'),
   ('călcâi', 'Călcâiul ușor întărit'), ('interior', 'Interiorul căptușit cu material textil'), ('talpă', 'Talpa plată din cauciuc')],
  {'Model': 'Geox KALISPERA', 'Material': 'imitație de piele și textil, branț din piele naturală, talpă din cauciuc', 'Caracteristici': 'profil înalt, șireturi și arici, branțuri detașabile, Geox Respira™', 'Cod produs': 'J744GI.0AU54'})

w(9692,
  f'<p>{PRIMIGI} PBZGT 88564 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de zăpadă unisex")}, bleumarin, izolate, din material textil și piele întoarsă. Membrana GORE-TEX® e subțire, impermeabilă și rezistentă la vânt, iar partea de sus rezistă la înmuiere, deci cizma e făcută pentru zăpadă și noroi.</p>'
  '<p>Gura cizmei se strânge cu șnur cu opritor, ca zăpada să nu intre pe sus, iar vârful rotund, ușor rigid, lasă degetele să se așeze liber.</p>'
  '<p>Dedesubt și înăuntru, cizma are:</p>'
  + L(('Talpă', 'exterioară, din cauciuc, cu absorbția șocului.'), ('Interior', 'textil, ușor de ținut curat.'), ('Ochiuri', 'fără nichel.'))
  + '<p>Numerele 25-29 sunt pentru copii de aproximativ 2-5 ani.</p>',
  [('model', 'Primigi Cizme de iarnă copii culoarea bleumarin, PBZGT 88564'), ('zăpadă', 'Cizme de zăpadă pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinația materialului textil cu pielea întoarsă'), GTX, ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'),
   ('șnur', 'Reglarea circumferinței superioare cu șnururi cu opritoare'), ('vârf', 'Degetul rotund, ușor rigid'), ('degete', 'degetele se pot aranja liber în pantof'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('șoc', 'Absorbtia socului'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'), ('nichel', 'Ochiurile din dantelă sunt fără nichel')],
  {'Model': 'Primigi PBZGT 88564', 'Material': 'textil și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, izolate, șnur cu opritor la gură', 'Cod produs': 'PBZGT 88564'})

w(9694,
  f'<p>{GEOX} SPRINTYE J66FWE sunt {A("/categorie/adidasi/", "adidași pentru fete")} roz, ușori, cu profil scurt și față din material textil, întărită cu inserții sintetice în zonele care se uzează. Tehnologia Geox Respira™ scoate umiditatea în afară și ține pantoful uscat pe dinăuntru.</p>'
  '<p>Închiderea cu arici le lasă pe cele mici să se încalțe și să se descalțe repede, singure, iar profilul scurt nu încurcă mișcarea gleznei.</p>'
  '<p>Pantoful rămâne simplu pe dinăuntru și dedesubt:</p>'
  + L(('Branț', 'din material textil.'), ('Interior', 'textil.'), ('Talpă exterioară', 'din cauciuc.'))
  + '<p>Mărimile 24-35 sunt, de obicei, pentru copii între 2 și 11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii SPRINTYE roz J66FWE.0EWNF'), ('ușor', 'combină lejeritatea cu funcționalitatea'), ('profil', 'Profil scurt'),
   ('față', 'Față din material textil'), ('întărituri', 'Întărituri din material sintetic'), ('Respira', 'Tehnologia GEOX Respira™ – susține eliminarea umidității la exterior'),
   ('uscat', 'menținând uscăciunea în interiorul încălțămintei'), ('arici', 'Închidere practică cu arici – facilitează încălțarea și descălțarea rapidă'),
   ('branț', 'Branț din material textil'), ('interior', 'Material textil'), ('talpă', 'Talpă exterioară din cauciuc')],
  {'Model': 'Geox SPRINTYE', 'Material': 'textil cu întărituri sintetice, interior textil, talpă din cauciuc', 'Caracteristici': 'arici, Geox Respira™, profil scurt', 'Cod produs': 'J66FWE.0EWNF'})

w(9699,
  f'<p>{GEOX} SKETLITE J65NWB sunt {A("/categorie/adidasi/", "adidași pentru fete")} albi, ușori, cu profil scurt, din material textil și piele ecologică, pentru purtat zi de zi. Talpa are sistemul Geox Respira, cu trei straturi perforate care ventilează pantoful.</p>'
  '<p>Șireturile elastice cu cârlig se strâng o dată pe picior și apoi pantoful se pune și se scoate fără să mai fie legat.</p>'
  '<p>Restul e ușor de întreținut:</p>'
  + L(('Branț', 'textil, se ține ușor curat.'), ('Interior', 'material textil.'), ('Talpă exterioară', 'din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 32-35 sunt pentru copii de în jur de 8-11 ani.</p>',
  [('model', 'Geox Sneakers pentru copii SKETLITE culoarea alb, J65NWB.0EWBC'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'purtarea zilnică'), ('Respira', 'talpei in trei straturi cu sistemul de perforari'),
   ('ventilare', 'imbunatateste ventilarea'), ('șireturi', 'Șireturile elastice și închiderea cu cârlig fac acești pantofi ușor de pus și de scos'),
   ('branț', 'Brantul textil este confortabil pentru picior si usureaza pastrarea pantofilor curati'), ('interior', 'Interiorul: Material textil'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Geox SKETLITE', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'șireturi elastice cu cârlig, Geox Respira', 'Cod produs': 'J65NWB.0EWBC'})

w(9704,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261163 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} gri, din piele naturală și piele întoarsă, făcuți în parteneriatul Biomecanics Podology. Stilul e casual, pentru joaca de zi cu zi.</p>'
  '<p>În zona degetelor e spațiu extins, deci degetele nu stau înghesuite, iar aricii cu bandă reglabilă se strâng după piciorul copilului. Branțurile textile se scot, așa că pot fi spălate sau folosite la măsurat piciorul.</p>'
  '<p>Pentru primii pași, contează și:</p>'
  + L(('Călcâi', 'întărit.'), ('Guler', 'moale, cu stabilizatori laterali.'), ('Talpă', 'flexibilă, din cauciuc.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Mărimile 20-23 sunt, de regulă, pentru 1-3 ani.</p>',
  [('model', 'Biomecanics Sneakers pentru copii din piele gri 261163'), ('material', 'Partea superioară din piele naturală și piele întoarsă'),
   ('parteneriat', 'Tehnologia Biomecanics Podology Partnership'), ('casual', 'Stilul lor casual'), ('degete', 'Spațiu extins în zona degetelor'),
   ('arici', 'Prindere cu arici cu bandă reglabilă'), ('branțuri', 'Branțuri detașabile, respirabile, din material textil'), ('călcâi', 'Călcâi întărit'),
   ('guler', 'Guler moale și stabilizatori laterali'), ('talpă', 'Talpă flexibilă din cauciuc'), ('interior', 'Interior căptușit cu material textil')],
  {'Model': 'Biomecanics 261163', 'Material': 'piele naturală și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu bandă reglabilă, spațiu extins la degete, branțuri detașabile', 'Cod produs': '261163'})

w(9709,
  f'<p>{REIMA} Aitoo 5100139B este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă softshell unisex")}, bleumarin, cu imprimeu all over, pentru anotimpurile de tranziție. Are impregnare hidrofobă, membrană impermeabilă de 10 000 mm H₂O și construcție rezistentă la vânt, deci ține la ploaie și la rafale.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar elastanul din material o lasă să se miște odată cu copilul. Manșetele cu nervuri strâng mânecile la încheieturi.</p>'
  '<p>Pentru drumurile prin parc și înapoi acasă, pe întuneric:</p>'
  + L(('Elemente reflectorizante', 'copilul se vede după lăsarea serii.'), ('Glugă', 'detașabilă, cu guler ridicat.'), ('Căptușeală', 'parțială, din polar.'),
      ('Buzunare', 'laterale, cu închidere.'), ('Închidere', 'fermoar pe toată lungimea.'))
  + '<p>Mărimile 104-164 merg, cam la 4-14 ani.</p>',
  [('model', 'Reima Geacă softshell pentru copii Aitoo bleumarin 5100139B'), ('imprimeu', 'Model cu imprimeu all over'), ('tranziție', 'anotimpurile de tranziție'),
   ('impermeabil', 'Impregnare hidrofobă și impermeabilitate de 10 000 mm H₂O protejează împotriva ploii'), ('membrană', 'Membrană impermeabilă'),
   ('vânt', 'Construcție rezistentă la vânt'), ('croială', 'Croială regulară'), ('lungime', 'Lungime până la șolduri'), ('elastan', '92% Poliester, 8% Elastan'),
   ('manșete', 'Manșete cu nervuri'), ('reflectorizant', 'Elemente reflectorizante sporesc vizibilitatea copilului după lăsarea întunericului'),
   ('glugă', 'Glugă detașabilă'), ('guler', 'Guler ridicat'), ('polar', 'Căptușeală parțială din polar'), ('buzunare', 'Buzunare laterale cu închidere'),
   ('fermoar', 'Închidere cu fermoar pe toată lungimea')],
  {'Model': 'Reima Aitoo', 'Material': '92% poliester, 8% elastan; inserții poliester acoperit cu TPU', 'Caracteristici': 'softshell, 10 000 mm H₂O, rezistentă la vânt, reflectorizante, glugă detașabilă', 'Cod produs': '5100139B'})

w(9713,
  f'<p>{PRIMIGI} PROGT 88666 sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")}, roz, izolate, din material textil și piele întoarsă. Membrana GORE-TEX® e subțire, impermeabilă și oprește vântul, deci zăpada și băltoacele nu ajung la picior.</p>'
  '<p>Au șiret și fermoar lateral: șiretul se reglează o dată pe picior, iar fermoarul se trage pentru încălțat. Cutia lată a degetelor nu le ciupește, deci cizma merge și la un picior mai lat.</p>'
  '<p>Pe zăpadă și pe teren denivelat, cizma are:</p>'
  + L(('Partea de sus', 'ridicată, rigidizează glezna.'), ('Talpă', 'exterioară, din cauciuc, cu absorbția șocului.'), ('Interior', 'textil, ușor de ținut curat.'))
  + '<p>Numerele 26-40 sunt pentru copii de la, în general, 3 ani în sus.</p>',
  [('model', 'Primigi Cizme de iarnă copii culoarea roz, PROGT 88666'), ('zăpadă', 'Cizme de zăpadă pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinația materialului textil cu pielea întoarsă'), GTX, ('șiret, fermoar', 'Model cu siret cu fermoar lateral'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('gleznă', 'Partea superioară ridicată ajută la rigidizarea gleznei'), ('teren', 'suprafețe neuniforme'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('șoc', 'Absorbtia socului'),
   ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Primigi PROGT 88666', 'Material': 'textil și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'GORE-TEX®, izolate, șiret și fermoar lateral, cutie lată', 'Cod produs': 'PROGT 88666'})

w(9721,
  f'<p>{A("/brand/liewood/", "Liewood")} Noam Pile Jacket LW20017 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă subțire unisex")}, bej, din material texturat, 100% poliester reciclat, certificat GRS. E o geacă de tranziție, căptușită, pentru zilele răcoroase.</p>'
  '<p>Croiala e simplă, dreaptă. Mânecile au finisaj elastic și manșete cu gaură pentru degetul mare, deci nu se ridică pe braț când copilul își trage mâneca peste mână.</p>'
  '<p>Se îmbracă repede și are loc pentru mâini:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'oblice.'), ('Căptușeală', 'da.'))
  + '<p>Mărimile 80-140 se potrivesc copiilor de aproximativ 1-10 ani.</p>',
  [('model', 'Liewood Geaca copii Noam Pile Jacket culoarea bej, LW20017'), ('subțire', 'Model subtire'), ('modelat', 'material modelat'), ('material', '100% Poliester reciclat'),
   ('GRS', 'GRS (Global Recycle Standard)'), ('tranziție', 'Izolare: tranzitional'), ('căptușeală', 'Captuseala: cu captuseala'), ('croială', 'Tăiere simplă, fără blocare'),
   ('elastic', 'Mâneci și glugă finisate cu tundere elastică'), ('deget', 'Manson cu gaura pentru degetul mare'),
   ('fermoar', 'Închiderea convenabilă cu fermoar'), ('buzunare', 'Buzunare oblice')],
  {'Model': 'Liewood Noam Pile Jacket', 'Material': '100% poliester reciclat (GRS)', 'Caracteristici': 'subțire, căptușită, manșete cu gaură pentru deget, fermoar', 'Cod produs': 'LW20017'},
  notes=['Magazinul se contrazice despre glugă („fara gluga” la atribute, „glugă finisată” în listă); nu am pomenit gluga.'])
