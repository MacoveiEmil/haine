import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

PRIMIGI = A('/brand/primigi/', 'Primigi')
BIO = A('/brand/biomecanics/', 'Biomecanics')
CKJ = A('/brand/calvin-klein-jeans/', 'Calvin Klein Jeans')

w(9825,
  f'<p>{PRIMIGI} PNOGT 88883 sunt {A("/categorie/baieti-incaltaminte-ghete-cizme/", "cizme de zăpadă pentru băieți")}, bleumarin, izolate, din piele întoarsă, material textil și sintetic. Membrana GORE-TEX® e foarte subțire, impermeabilă și oprește vântul, așa că piciorul rămâne uscat și pe zăpadă udă.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, deci cizma vine comod și pe un picior lat. Velcro-ul și bucla de la spate îl ajută pe copil să se încalțe repede, singur.</p>'
  '<p>Cizma mai are:</p>'
  + L(('Căptușeală', 'textilă.'), ('Talpă', 'exterioară, din cauciuc, cu absorbția șocului.'), ('Partea de sus', 'rigidizată.'))
  + '<p>Numerele 27-30 sunt pentru copii de în jur de 3-7 ani.</p>',
  [('model', 'Primigi Cizme de iarna copii culoarea albastru marin, PNOGT 88883'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Model Izolat'),
   ('material', 'combinație de piele întoarsă, material textil și material sintetic'),
   ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'), ('căptușeală', 'Model cu captuseala textila'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare'), ('șoc', 'Absorbtia socului'), ('rigidizat', 'Partea superioară rigidizată')],
  {'Model': 'Primigi PNOGT 88883', 'Material': 'piele întoarsă, textil și sintetic, căptușeală textilă', 'Caracteristici': 'GORE-TEX®, izolate, velcro, cutie lată', 'Cod produs': 'PNOGT 88883'})

w(9830,
  f'<p>Geaca {A("/brand/guess/", "Guess")} N6YL01 W2656 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, bej, cu izolație sintetică și căptușeală completă, în stil casual, pentru vremea schimbătoare din sezonul de tranziție.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, iar tivul și manșetele elastice strâng geaca pe corp și țin căldura. Gluga integrată și gulerul ridicat apără capul și gâtul de vânt.</p>'
  '<p>La purtat, mai contează:</p>'
  + L(('Închidere', 'fermoar.'), ('Buzunare', 'laterale, tip slip-on.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 68-76 până la 122-125 corespund, în mare, vârstei de 6 luni - 7 ani.</p>',
  [('model', 'Guess Geacă petrecută pentru copii bej N6YL01 W2656'), ('matlasat', 'Construcția matlasată'), ('izolație', 'Izolația sintetică ajută la menținerea căldurii'),
   ('căptușeală', 'Căptușeala completă'), ('casual', 'stil casual'), ('tranziție', 'vremea schimbătoare din sezonul de tranziție'), ('croială', 'Croiala regulară'),
   ('lungime', 'Lungimea până la șolduri'), ('elastic', 'Tivul și manșetele elastice permit o ajustare mai bună și rețin căldura'),
   ('glugă', 'Gluga integrată ajută la protejarea capului împotriva vântului'), ('guler', 'Gulerul ridicat'), ('fermoar', 'Închiderea cu fermoar'),
   ('buzunare', 'Buzunarele laterale tip slip-on'), ('material', '100% Poliester')],
  {'Model': 'Guess N6YL01 W2656', 'Material': '100% poliester', 'Caracteristici': 'matlasată, izolație sintetică, glugă integrată, tiv și manșete elastice', 'Cod produs': 'N6YL01 W2656'})

w(9836,
  f'<p>Paltonul {CKJ} IG0IG03006 este un {A("/categorie/geci-jachete/", "palton subțire pentru fete")}, bej, din material texturat, căptușit, pentru sezonul de tranziție. Are clapete clasice și se închide cu nasture, ca un palton de oraș.</p>'
  '<p>Croiala e simplă, dreaptă, fără strângeri pe corp, deci cade lejer și peste un pulover subțire. Nu are glugă, așa că pe vânt merge bine cu o căciulă.</p>'
  '<p>Pe scurt, despre palton:</p>'
  + L(('Închidere', 'cu nasture.'), ('Căptușeală', 'da.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 128-170 sunt pentru copii de aproximativ 8-15 ani.</p>',
  [('model', 'Calvin Klein Jeans Palton copii culoarea bej, IG0IG03006'), ('subțire', 'Model subțire'), ('modelat', 'material modelat'), ('căptușeală', 'Captuseala: cu captuseala'),
   ('tranziție', 'Izolare: tranzitional'), ('clapete', 'Clapete clasice'), ('nasture', 'Are o inchidere confortabila cu nasture'), ('croială', 'Tăiere simplă, fără blocare'),
   ('fără glugă', 'Gluga: fara gluga'), ('material', '100% Poliester')],
  {'Model': 'Calvin Klein Jeans IG0IG03006', 'Material': '100% poliester', 'Caracteristici': 'subțire, căptușit, nasture, fără glugă', 'Cod produs': 'IG0IG03006'})

w(9839,
  f'<p>Geaca bomber {CKJ} IG0IG03076 este o {A("/categorie/geci-jachete/", "geacă bomber pentru fete")}, bordo, subțire, din bumbac 100%, cu logo-ul mărcii în față. Nu e izolată și nici căptușită, deci e pentru zilele blânde, nu pentru frig.</p>'
  '<p>Croiala e simplă, cu linia umerilor lăsată, iar mânecile se termină cu bandă elastică, care strânge la încheieturi și pe un braț mai subțire.</p>'
  '<p>Bomberul are puține detalii, dar practice:</p>'
  + L(('Închidere', 'fermoar.'), ('Glugă', 'nu are.'), ('Material', 'bumbac 100%.'))
  + '<p>Mărimile 128-170 sunt pentru copii de pe la 8 până pe la 15 ani.</p>',
  [('model', 'Calvin Klein Jeans Geacă bomber pentru copii culoarea bordo, IG0IG03076'), ('subțire', 'Model subtire confectionat din material de bumbac'), ('bumbac', '100% Bumbac'),
   ('logo', 'Logo-ul mărcii pe față'), ('neizolat', 'Izolare: neizolat'), ('necăptușit', 'Captuseala: necaptusit'), ('croială', 'Tăiere simplă, fără blocare'),
   ('umeri', 'Linia umerilor lasata'), ('elastic', 'Mâneci finisate cu o coadă elastică'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('fără glugă', 'Gluga: fara gluga'),
   ('bomber', 'Fit: bomber')],
  {'Model': 'Calvin Klein Jeans IG0IG03076', 'Material': '100% bumbac', 'Caracteristici': 'bomber, subțire, neizolat, mâneci elastice', 'Cod produs': 'IG0IG03076'})

w(9847,
  f'<p>{A("/brand/mayoral/", "Mayoral")} 2439 este o {A("/categorie/bebe-imbracaminte-geci-jachete/", "geacă reversibilă pentru bebeluși")}, roz, cu o față matlasată, în stil sportiv, și una din imitație de blană moale. Izolația sintetică medie o face bună pentru zilele reci de tranziție și iernile blânde.</p>'
  '<p>Croiala e regulară, cu lungimea până la șolduri, deci nu încurcă la joacă. Gluga integrată apără capul de vânt și frig, iar fermoarul se trage repede la îmbrăcat.</p>'
  '<p>Ce mai are, pe lângă croială:</p>'
  + L(('Fețe', 'matlasată și din imitație de blană.'), ('Izolație', 'sintetică, medie.'), ('Material', '100% poliamidă.'))
  + '<p>Mărimile 74-104 sunt pentru cei mici, de la cam 9 luni până la 4 ani.</p>',
  [('model', 'Mayoral Jachetă reversibilă pentru copii roz 2439'), ('reversibil', 'Designul reversibil permite purtarea jachetei în două moduri'),
   ('matlasat', 'Partea matlasată conferă jachetei un aspect clasic, sportiv'), ('blană', 'Imitația de blană pe o parte a modelului adaugă moliciune'),
   ('izolație', 'Izolație termică medie'), ('tranziție', 'zilele mai reci ale sezonului de tranziție și iernile blânde'), ('croială', 'Croiala regulară'),
   ('lungime', 'Lungimea până la șolduri'), ('glugă', 'Gluga integrată oferă o protecție suplimentară a capului împotriva vântului și frigului'),
   ('fermoar', 'Închiderea cu fermoar'), ('material', '100% Poliamidă')],
  {'Model': 'Mayoral 2439', 'Material': '100% poliamidă', 'Caracteristici': 'reversibilă (matlasată / imitație de blană), izolație medie, glugă integrată', 'Cod produs': '2439'})

w(9855,
  f'<p>Pantofii {BIO} 261124 sunt {A("/categorie/bebe-incaltaminte-pantofi/", "pantofi pentru bebeluși")} bleumarin, din piele naturală și piele întoarsă, cu finisaj neted și stil casual universal. Sunt făcuți în parteneriatul Biomecanics Podology, pentru copiii mici și activi.</p>'
  '<p>Aricii și cureaua reglabilă strâng pantoful pe picior, iar bucla de la spate ajută la încălțat. Vârful rotund, cauciucat, lasă degetele libere și le apără la joacă.</p>'
  '<p>Pentru mers sigur, pantoful are:</p>'
  + L(('Călcâi și guler', 'întărite.'), ('Stabilizator', 'lateral.'), ('Branț', 'detașabil, antibacterian.'), ('Talpă', 'flexibilă, din cauciuc.'))
  + '<p>Numerele 19-25 sunt pentru copii de, în general, 1-3 ani.</p>',
  [('model', 'Biomecanics Pantofi pentru copii din piele bleumarin 261124'), ('material', 'Partea superioară din piele naturală și piele întoarsă , cu un finisaj neted'),
   ('casual', 'Stil casual universal'), ('parteneriat', 'Tehnologia Biomecanics Podology Partnership'), ('activi', 'proiectați pentru cei mici activi'),
   ('arici', 'Închidere cu arici și curea reglabilă'), ('buclă', 'Buclă la spate facilitează încălțarea'), ('vârf', 'Vârf rotund, cauciucat , protejează degetele'),
   ('călcâi', 'Călcâi întărit și un guler ușor întărit'), ('stabilizator', 'stabilizatorul lateral'), ('branț', 'Branț detașabil, respirabil , cu proprietăți antibacteriene'),
   ('talpă', 'Talpă flexibilă din cauciuc')],
  {'Model': 'Biomecanics 261124', 'Material': 'piele naturală și piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'arici și curea, branț antibacterian detașabil, vârf cauciucat', 'Cod produs': '261124'})

w(9856,
  f'<p>{BIO} 261152 sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi unisex")} bleumarin, din piele naturală și material sintetic, cu membrana impermeabilă BioTEX, care păstrează picioarele uscate, și interior căptușit cu lână pentru zilele mai reci. Sunt pentru joaca afară, pe vreme rece și umedă.</p>'
  '<p>Vârful e lat și rotund, de tip barefoot, cu loc ca degetele să stea liber, deci merg și la un picior mai lat. Aricii și cureaua reglabilă strâng pantoful după picior.</p>'
  '<p>Talpa și călcâiul:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Călcâi', 'întărit.'), ('Parteneriat', 'Biomecanics Podology, după recomandările podologilor.'))
  + '<p>Mărimile 19-26 sunt, cam, pentru 1-4 ani.</p>',
  [('model', 'Biomecanics Încălțăminte pentru copii din piele bleumarin 261152'), ('material', 'Piele naturală, Material sintetic'),
   ('BioTEX', 'Membrana impermeabilă BioTEX ajută la menținerea picioarelor uscate'), ('lână', 'Interior căptușit cu lână ajută la menținerea căldurii'),
   ('reci', 'zilele mai reci'), ('aer liber', 'joacă în aer liber'), ('vârf', 'Vârf lat, rotund (barefoot) favorizează așezarea liberă a degetelor'),
   ('arici', 'Închidere cu arici și curea reglabilă'), ('talpă', 'Talpă flexibilă de cauciuc'), ('călcâi', 'Călcâi întărit'),
   ('podologi', 'în conformitate cu recomandările podologilor')],
  {'Model': 'Biomecanics 261152', 'Material': 'piele naturală și sintetic, interior din lână, talpă din cauciuc', 'Caracteristici': 'membrană BioTEX, vârf lat barefoot, arici și curea', 'Cod produs': '261152'})

w(9864,
  f'<p>{A("/brand/columbia/", "Columbia")} Boulder Falls 2156421 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de ploaie unisex")}, neagră, neizolată, cu tehnologia Omni-tech®: membrană microporoasă și cusături sudate acoperite cu strat impermeabil. E pentru ploaie și vreme schimbătoare, în sezonul de tranziție.</p>'
  '<p>Fasonul e drept, cu loc pentru un pulover dedesubt, iar marginile mânecilor se reglează cu Velcro, deci se strâng pe încheieturi subțiri.</p>'
  '<p>Când copilul se încălzește la mișcare, ajută:</p>'
  + L(('Ventilație', 'deschideri cu fermoar sub axile.'), ('Căptușeală', 'din plasă.'), ('Glugă', 'da.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Fermoar', 'cu apărătoare pentru bărbie.'))
  + '<p>Mărimile 104-164 sunt pentru copii de pe la 4 până pe la 14 ani.</p>',
  [('model', 'Columbia Geacă copii Boulder Falls culoarea negru, 2156421'), ('neizolat', 'Model neizolat'), ('Omni-tech', 'Tehnologia Omni-tech®'),
   ('membrană', 'membranei microporoase, respirabile si a cusaturilor sudate acoperite cu un strat impermeabil'), ('impermeabil', 'material impermeabil'),
   ('tranziție', 'Izolare: tranzitional'), ('fason', 'Fason drept'), ('manșete', 'Marginile inferioare ale mânecilor sunt reglabile cu Velcro'),
   ('ventilație', 'Deschideri de ventilatie cu fermoar sub axile'), ('plasă', 'Căptușeala este realizată dintr-un material plasă'), ('glugă', 'Model cu gluga'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('bărbie', 'apărătoare pentru bărbie')],
  {'Model': 'Columbia Boulder Falls', 'Material': 'material impermeabil, căptușeală din plasă', 'Caracteristici': 'Omni-tech®, cusături sudate, ventilație sub axile, manșete cu Velcro', 'Cod produs': '2156421'})

w(9871,
  f'<p>{PRIMIGI} PDE 14040 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, cu profil scurt, din material textil și piele întoarsă. Branțul din piele previne frecarea, abraziunile și mirosul neplăcut, iar vârful e rotund.</p>'
  '<p>Au șiret care se închide cu velcro, deci se reglează o dată pe picior și apoi se pun repede. Spatele călcâiului e rigidizat și ține piciorul pe loc.</p>'
  '<p>Din ce sunt făcuți:</p>'
  + L(('Partea de sus', 'piele întoarsă și textil.'), ('Interior', 'piele și material sintetic.'), ('Talpă', 'exterioară, din cauciuc, rezistentă la uzură.'))
  + '<p>Numerele 18-26 sunt pentru copii de aproximativ 1-4 ani.</p>',
  [('model', 'Primigi Sneakers pentru copii culoarea roz, PDE 14040'), ('profil', 'Înălțime: mic de statură'), ('material', 'combinația materialului textil cu pielea întoarsă'),
   ('branț', 'Un model cu branț din piele care este confortabil pentru picior și previne frecarea, abraziunile și apariția unui miros neplăcut'),
   ('vârf', 'Varf rotund'), ('șiret', 'Model cu siret cu inchidere Velcro'), ('călcâi', 'Spatele calcaiului rigidizat'), ('interior', 'Piele, Material sintetic'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Primigi PDE 14040', 'Material': 'textil și piele întoarsă, branț din piele, talpă din cauciuc', 'Caracteristici': 'șiret cu închidere velcro, călcâi rigidizat', 'Cod produs': 'PDE 14040'})

w(9880,
  f'<p>{A("/brand/reima/", "Reima")} Kiirus 5400006A sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, ușori, cu profil scurt, din material textil și piele ecologică, pentru purtat zi de zi. Velcro-ul îi lasă pe cei mici să se încalțe și să se descalțe singuri.</p>'
  '<p>Cutia lată a degetelor nu le ciupește, deci pantoful merge și pe un picior mai plin, iar bucla de la spate ajută la tras pantoful pe picior.</p>'
  '<p>Pentru alergat prin parc, contează:</p>'
  + L(('Călcâi', 'contrafort rigidizat.'), ('Interior', 'textil, ușor de ținut curat.'), ('Talpă', 'exterioară, din cauciuc, rezistentă la uzură.'))
  + '<p>Mărimile 20-28 sunt, de regulă, pentru 1-5 ani.</p>',
  [('model', 'Reima Sneakers pentru copii Kiirus culoarea roz, 5400006A'), ('ușor', 'Model ușor'), ('profil', 'Înălțime: mic de statură'),
   ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'purtarea zilnică'), ('velcro', 'Închiderea cu velcro facilitează încălțarea și scoaterea pantofilor'),
   ('cutie lată', 'Cutia lată a degetelor previne ciupirea degetelor'), ('buclă', 'Bucla de la spate ușurează alunecarea pantofului peste picior'),
   ('călcâi', 'Contorul de călcâi rigidizat'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați'),
   ('talpă', 'Talpa exterioară din cauciuc este durabilă și rezistentă la deteriorare')],
  {'Model': 'Reima Kiirus', 'Material': 'textil și piele ecologică, interior textil, talpă din cauciuc', 'Caracteristici': 'velcro, cutie lată, buclă la spate', 'Cod produs': '5400006A'})
