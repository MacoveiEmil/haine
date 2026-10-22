import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

BIO = A('/brand/biomecanics/', 'Biomecanics')

w(8515,
  f'<p>{BIO} 261213 sunt {A("/categorie/adidasi/", "adidași înalți pentru fete")}, multicolori, din material sintetic strălucitor, cu profil înalt peste gleznă. Sunt făcuți pentru activitățile de zi cu zi, iar modelul vine din programul Biomecanics Podology Partnership.</p>'
  '<p>Închiderea cu arici se reglează pe orice lățime de picior, iar branțul textil se scoate: îl poți pune lângă piciorul copilului ca să verifici dacă mai e loc.</p>'
  '<p>Pentru încălțat zilnic, construcția e simplă:</p>'
  + L(('Călcâi', 'întărit.'), ('Talpă', 'plată, din cauciuc.'), ('Interior', 'căptușit cu material textil.'), ('Profil', 'înalt, acoperă glezna.'))
  + '<p>Numerele 28-34 se potrivesc în general copiilor de 4-11 ani.</p>',
  [('cod', '261213'), ('culoare', 'multicolor'), ('material', 'Partea superioară din material sintetic strălucitor'), ('profil', 'Profilul înalt'),
   ('zilnic', 'potriviți pentru numeroase activități zilnice'), ('Podology', 'Tehnologia Biomecanics Podology Partnership'), ('arici', 'Închiderea practică cu arici'),
   ('branț', 'Branțurile textile detașabile'), ('călcâi', 'Călcâiul întărit'), ('talpă', 'Talpa plată din cauciuc'), ('interior', 'Interiorul căptușit cu material textil')],
  {'Model': 'Biomecanics 261213', 'Material': 'sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, arici, branț textil detașabil, călcâi întărit', 'Cod produs': '261213'})

w(8521,
  f'<p>{A("/brand/emporio-armani/", "Emporio Armani")} are aici o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, bleumarin, din poliamidă rezistentă, cu căptușeală, dar fără izolație. E pentru primăvară și toamnă, cu o glugă care se detașează când vremea e bună.</p>'
  '<p>Mânecile și marginea de jos sunt finisate cu bătături, care strâng geaca la încheieturi și jos. Magazinul precizează că mărimile sunt italiene, convertite la cele europene, deci merită verificat tabelul de mărimi.</p>'
  '<p>Detaliile gecii:</p>'
  + L(('Glugă', 'detașabilă.'), ('Închidere', 'cleme.'), ('Buzunare', 'exterioare, cu închidere.'), ('Material', '100% poliamidă, cu căptușeală.'))
  + '<p>Mărimile de pe site, 130-175, acoperă cam vârsta de 8-16 ani.</p>',
  [('culoare', 'culoarea albastru marin'), ('material', 'material rezistent'), ('neizolat', 'Izolare: neizolat'), ('căptușeală', 'Model cu captuseala'),
   ('bătături', 'Mânecile și marginea inferioară finisate cu bătături'), ('mărimi italiene', 'Dimensiunile disponibile sunt cele ale producatorul italian'),
   ('glugă', 'Gluga detasabila'), ('cleme', 'Incheiere cu cleme'), ('buzunare', 'Buzunare exterioare incheiata'), ('poliamidă', '100% Poliamida')],
  {'Model': 'Emporio Armani, geacă', 'Material': '100% poliamidă, cu căptușeală', 'Caracteristici': 'fără izolație, glugă detașabilă, cleme, bătături la mâneci și bază', 'Cod produs': ''},
  notes=['Mărimi italiene convertite la europene (după magazin).'])

w(8525,
  f'<p>{A("/brand/reima/", "Reima")} Vaanila este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă de iarnă unisex")} neagră, matlasată, cu izolație sintetică, pentru temperaturi mai reci. Are impermeabilitate de 10000 mm și tratament Teflon EcoElite, deci ține la zăpadă umedă și la ploaie.</p>'
  '<p>Croiala e simplă, iar fermoarul pe toată lungimea are o clapă cu capse, rezistentă la vânt, care închide geaca bine la piept.</p>'
  '<p>Ce mai are geaca, pe scurt:</p>'
  + L(('Glugă', 'detașabilă, cu guler ridicat.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Respirabilitate', '7000 g/m2/24h.'), ('Material', 'poliester reciclat, certificat Bluesign®.'))
  + '<p>Între mărimile 104 și 164, geaca acoperă de regulă copiii de 4-14 ani.</p>',
  [('model', 'Reima Vaanila negru 5100102B'), ('izolat', 'Model izolat'), ('matlasat', 'material matlasat'), ('izolație sintetică', 'izolatie sintetică'),
   ('temperaturi', 'temperaturi mai reci'), ('impermeabilitate', 'Impermeabilitate: 10000 mm/m2/24h'), ('Teflon', 'Teflon EcoElite'), ('croială', 'Tăiere simplă'),
   ('clapă', 'Închidere cu fermoar pe toată lungimea, cu clapă rezistentă la vânt, cu capse'), ('glugă, guler', 'Gulerul ridicat și gluga detașabilă'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('respirabilitate', 'Respirabilitate: 7000 g/m2/24h'),
   ('reciclat', 'Material de bază: 100% Poliester reciclat'), ('Bluesign', 'Model certificat Bluesign')],
  {'Model': 'Reima Vaanila', 'Material': 'poliester reciclat, izolație sintetică', 'Caracteristici': 'impermeabilitate 10000 mm, respirabilitate 7000 g, Teflon EcoElite, glugă detașabilă, Bluesign®', 'Cod produs': '5100102B'})

w(8526,
  f'<p>{BIO} 261246 sunt {A("/categorie/incaltaminte-pantofi/", "pantofi înalți pentru fete")}, roz, din textil și material sintetic cu finisaj de piele întoarsă. Membrana BioTEX îi protejează de umezeala de afară, deci merg și în zilele umede de toamnă.</p>'
  '<p>Se închid cu înșiretare rapidă, arici și fermoar: se deschid larg la încălțat și se strâng repede pe picior, iar gulerul e ușor întărit în jurul gleznei.</p>'
  '<p>La talpă și la interior, modelul are:</p>'
  + L(('Talpă', 'din spumă, plată, cu structura Flexi Lite.'), ('Călcâi', 'întărit.'), ('Interior', 'căptușeală textilă.'))
  + '<p>Modelul vine în numerele 25-34, aproximativ pentru copii de 2-11 ani.</p>',
  [('cod', '261246'), ('culoare', 'Acest model roz'), ('material', 'partea superioară din material textil și sintetic, cu finisaj de piele întoarsă'),
   ('BioTEX', 'Membrană BioTEX'), ('umezeală', 'protejează împotriva umezelii externe'), ('închidere', 'sistemul de înșiretare rapidă, ariciul și fermoarul'),
   ('guler', 'gulerul ușor întărit'), ('talpă', 'Talpă din spumă'), ('Flexi Lite', 'Lejeritate Flexi Lite'), ('călcâi', 'Călcâi întărit'),
   ('interior', 'căptușeală din material textil'), ('profil', 'Profil înalt al părții superioare')],
  {'Model': 'Biomecanics 261246', 'Material': 'textil și sintetic, interior textil, talpă din spumă', 'Caracteristici': 'membrană BioTEX, Flexi Lite, înșiretare rapidă, arici și fermoar', 'Cod produs': '261246'})

w(8533,
  f'<p>{BIO} 262166 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")}, albi pe site, din piele naturală și piele ecologică, cu profil scurt. Au fost creați împreună cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia.</p>'
  '<p>Deschiderea e largă, iar curelele cu arici se reglează pe piciorul copilului, inclusiv pe unul mai plinuț. Cutia degetelor e lată și lasă loc degetelor.</p>'
  '<p>Pentru primii ani de mers, contează și:</p>'
  + L(('Inserție', 'Plantilla, cu perforații.'), ('Vârf', 'rotund, întărit.'), ('Călcâi', 'contor rigidizat.'))
  + '<p>Numerele de pe site, 19-26, se potrivesc cam copiilor de 1-4 ani.</p>',
  [('cod', '262166'), ('material', 'combinația pielii naturale cu cea ecologică'), ('profil', 'Înălțime: mic de statură'),
   ('Valencia', 'medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'), ('deschidere', 'Deschidere larga'),
   ('curele', 'Curelele cu velcro pentru prindere ușoară'), ('cutie lată', 'Cutia lată a degetelor'), ('inserție', 'Inserția Plantilla cu perforații'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigidizat')],
  {'Model': 'Biomecanics 262166', 'Material': 'piele naturală și piele ecologică, interior textil', 'Caracteristici': 'curele cu arici, deschidere largă, cutie lată a degetelor, inserție Plantilla', 'Cod produs': '262166'},
  notes=['Titlul de pe site spune alb; pagina magazinului din link dă culoarea albastru.'])

w(8534,
  f'<p>{BIO} 262274 sunt {A("/categorie/adidasi/", "adidași cu lumini pentru fete")}, roz, din material textil și piele ecologică, cu profil scurt. Luminile se aprind de la un buton, deci seara copilul se vede mai bine pe drum.</p>'
  '<p>Spatele are o tăietură în formă de U, care lasă glezna liberă și nu apasă pe tendonul lui Ahile, iar șireturile elastice cu închidere cu cârlig se strâng fără nod.</p>'
  '<p>Restul detaliilor vin din lucrul cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia:</p>'
  + L(('Branț', 'detașabil, antibacterian, profilat la mijlocul tălpii.'), ('Vârf', 'protejat, pentru degete.'), ('Talpă', 'în formă de „picior de elefant” la călcâi.'), ('Inserție', 'perforată.'))
  + '<p>Pe site sunt numerele 24-34, care corespund, cu aproximație, vârstei de 2-11 ani.</p>',
  [('cod', '262274'), ('culoare', 'culoarea roz'), ('material', 'combinația materialului textil cu pielea ecologică'), ('lumini', 'Model cu lumini incorporate, activate de un buton'),
   ('profil', 'Înălțime: mic de statură'), ('U', 'taieturi in forma de U care impiedica exercitarea presiunii asupra tendonului lui Ahile'),
   ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('Valencia', 'medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'),
   ('branț', 'Brant detasabil si antibacterian, profilat la mijlocul piciorului'), ('vârf', 'Degetul securizat protejeaza degetele'),
   ('talpă', 'Talpa in forma de „picior de elefant” peste calcaie'), ('inserție', 'insertiei perforate')],
  {'Model': 'Biomecanics 262274', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'lumini cu buton, șireturi elastice, branț antibacterian detașabil, tăietură în U', 'Cod produs': '262274'})

w(8539,
  f'<p>{A("/brand/geox/", "Geox")} PHAOLAE sunt {A("/categorie/ghete-cizme/", "bocanci pentru fete")} negri, din piele întoarsă, ușor izolați, cu talpă din cauciuc ușor flexibilă. Sunt pentru toamnă și pentru zilele reci, nu pentru ger.</p>'
  '<p>Partea de sus urcă peste gleznă și o ține fixă, iar șiretul clasic se strânge exact cât trebuie, la un picior subțire sau la unul mai plin.</p>'
  '<p>La interior și la vârf:</p>'
  + L(('Vârf', 'rotund, întărit.'), ('Călcâi', 'contor rigid.'), ('Branț', 'textil.'), ('Izolație', 'ușoară.'))
  + '<p>Numerele 28-39 îi fac potriviți pentru copii de la 4 ani în sus, în general.</p>',
  [('model', 'Bocanci copii PHAOLAE culoarea negru'), ('material', 'Model confectionat din piele intoarsa'), ('izolat', 'Izolare: usor izolat'),
   ('talpă', 'talpă de cauciuc, ușor flexibilă'), ('gleznă', 'Partea superioară ridicată'), ('șiret', 'Șiretul clasic permite ajustarea individuală'),
   ('vârf', 'Cutie rotunda, intarita'), ('călcâi', 'Contorul de călcâi rigid'), ('branț', 'Brantul textil')],
  {'Model': 'Geox PHAOLAE', 'Material': 'piele întoarsă, interior sintetic și textil, talpă din cauciuc', 'Caracteristici': 'ușor izolați, șiret, gleznă înaltă, vârf întărit', 'Cod produs': 'J46ETD.000BC'})

w(8540,
  f'<p>Adidașii {BIO} din acest model sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} roz, din material textil și piele ecologică, ușori, cu profil scurt și talpă elastică. Sunt potriviți pentru purtat zilnic.</p>'
  '<p>Aricii fac pantoful ușor de pus și îl potrivesc bine pe picior, iar tăietura în formă de U din spate lasă glezna să se miște liber.</p>'
  '<p>Pentru primii pași, detaliile sunt:</p>'
  + L(('Vârf', 'protejat.'), ('Branț', 'detașabil, antibacterian, profilat.'), ('Inserție', 'perforată.'))
  + '<p>Numerele de pe site, de la 18 până la 25, sunt gândite cam pentru 1-3 ani.</p>',
  [('model', 'Sneakers pentru copii culoarea roz'), ('material', 'combinatia materialului textil cu pielea ecologica'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('profil', 'Înălțime: mic de statură'), ('talpă', 'Talpa elastica'), ('arici', 'se potriveste bine datorita fixarii cu velcro'),
   ('U', 'taieturi in forma de U'), ('vârf', 'Degetul securizat'), ('branț', 'Brant detasabil si antibacterian, profilat'), ('inserție', 'insertiei perforate')],
  {'Model': 'Biomecanics, adidași bebe', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'arici, talpă elastică, branț antibacterian detașabil, tăietură în U', 'Cod produs': ''})

w(8548,
  f'<p>{BIO} 261108 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} gri, cu motiv animalier și finisaj strălucitor, din piele naturală și material sintetic. Sunt adidași plați, de purtat la joaca de zi cu zi.</p>'
  '<p>Închiderea cu arici are o curea reglabilă, deci pantoful se strânge exact pe picior, iar călcâiul și gulerul sunt moi, fără margini tari la gleznă.</p>'
  '<p>Pentru picioarele mici, contează și:</p>'
  + L(('Talpă', 'flexibilă, din cauciuc.'), ('Vârf', 'rotund, cauciucat.'), ('Branț', 'detașabil, din material textil.'))
  + '<p>Mărimile 19-25 acoperă, de regulă, vârsta de 1-3 ani.</p>',
  [('cod', '261108'), ('culoare', 'Sneakers pentru copii gri 261108'), ('animalier', 'motiv animalier'), ('strălucitor', 'finisaj strălucitor'),
   ('material', 'Piele naturală, Material sintetic'), ('flat', 'Sneakerși flat'), ('zi cu zi', 'aventurile urbane de zi cu zi'),
   ('arici', 'Închidere cu arici și curea reglabilă'), ('moale', 'Călcâi moale și guler superior moale'), ('talpă', 'Talpă flexibilă din cauciuc'),
   ('vârf', 'Vârf rotund, cauciucat'), ('branț', 'Branț detașabil din material textil')],
  {'Model': 'Biomecanics 261108', 'Material': 'piele naturală și sintetic, interior textil, talpă din cauciuc', 'Caracteristici': 'arici cu curea reglabilă, talpă flexibilă, vârf cauciucat, branț detașabil', 'Cod produs': '261108'})

w(8556,
  f'<p>{A("/brand/columbia/", "Columbia")} Coreshot este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă impermeabilă unisex")}, violet, ușor izolată, cu tehnologia Omni-tech®: membrană microporoasă și cusături sudate, acoperite cu un strat impermeabil. E făcută pentru vremea care se schimbă brusc.</p>'
  '<p>Are fermoar scurt, deci se îmbracă peste cap, ca un anorak, iar mânecile raglan lasă umerii liberi la mișcare. În interior are o centură flexibilă, cauciucată, care ține geaca strânsă pe corp.</p>'
  '<p>Pe exterior, geaca are:</p>'
  + L(('Glugă', 'fixă, cu guler ridicat.'), ('Buzunar', 'în față.'), ('Izolație', 'ușoară, cu umplutură din poliester parțial reciclat.'))
  + '<p>Geaca se găsește în mărimile 104-164, adică, orientativ, pentru copii de 4-14 ani.</p>',
  [('model', 'Geacă copii Coreshot culoarea violet, 2133811'), ('ușor izolat', 'Model ușor izolat'), ('Omni-tech', 'Tehnologia Omni-tech'),
   ('membrană, cusături', 'membranei microporoase, respirabile si a cusaturilor sudate acoperite cu un strat impermeabil'), ('vreme', 'schimbarilor bruste ale vremii'),
   ('fermoar', 'Incheiere scurta cu fermoar'), ('raglan', 'Mânecile raglan'), ('centură', 'centura flexibila, cauciucata'), ('glugă, guler', 'Gulerul ridicat și gluga fixă'),
   ('buzunar', 'In fata buzunar'), ('umplutură', 'Umplutura: 85% Poliester reciclat, 15% Poliester')],
  {'Model': 'Columbia Coreshot', 'Material': 'poliester, umplutură din poliester parțial reciclat', 'Caracteristici': 'Omni-tech®, cusături sudate, fermoar scurt, glugă fixă, mâneci raglan', 'Cod produs': '2133811'})
print('lot 4 scris')
