import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
TH = A('/brand/tommy-hilfiger/', 'Tommy Hilfiger')

w(8922,
  f'<p>{GEOX} LOFTUS sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} gri, din imitație de piele și material textil, cu tehnologia GEOX Respira™, care ține interiorul uscat. Se poartă la ținute casual și streetwear, la joacă și la școală.</p>'
  '<p>Combină aricii cu șireturile elastice, deci pantoful se strânge repede și exact pe picior; gulerul e moale și se așază pe gleznă fără să irite, iar profilul e scurt.</p>'
  '<p>Pe dinăuntru și pe dedesubt:</p>'
  + L(('Talpă', 'din spumă, ușoară și flexibilă.'), ('Călcâi', 'întărit.'), ('Căptușeală', 'textilă, moale.'), ('Branț', 'din material textil.'))
  + '<p>Numerele 24-35 corespund, cu aproximație, vârstei de 2-11 ani.</p>',
  [('model', 'Geox LOFTUS sneakers pentru copii gri J66MQA.0FU54'), ('material', 'Partea superioară din imitație de piele și material textil'),
   ('Respira', 'Tehnologia GEOX Respira'), ('casual', 'ținutele casual și streetwear'), ('închidere', 'închiderea practică cu velcro, combinată cu șireturile elastice'),
   ('guler', 'Gulerul moale al părții superioare se adaptează delicat la gleznă'), ('profil', 'Profilul scurt'), ('talpă', 'Talpa din spumă oferă lejeritate și flexibilitate'),
   ('călcâi', 'Călcâiul întărit'), ('căptușeală', 'Căptușeala moale din material textil'), ('branț', 'Branțul din material textil')],
  {'Model': 'Geox LOFTUS', 'Material': 'imitație de piele și textil, căptușeală textilă, talpă din spumă', 'Caracteristici': 'GEOX Respira™, arici și șireturi elastice, guler moale', 'Cod produs': 'J66MQA.0FU54'})

w(8923,
  f'<p>{GEOX} GISLI sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași înalți pentru bebeluși")} roz, cu imprimeu, din piele naturală, material textil și sintetic. Talpa are o membrană microporoasă și tehnologia GEOX Respira™, care elimină umezeala și împiedică apa să pătrundă pe dedesubt.</p>'
  '<p>Profilul e înalt, cu guler ușor întărit în jurul gleznei, iar închiderea cu scai se prinde repede, ca încălțatul copilului mic să dureze puțin.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Talpă', 'plată, din cauciuc.'), ('Călcâi', 'întărit.'), ('Interior', 'căptușit cu material textil.'))
  + '<p>Mărimile de pe site, 20-27, se potrivesc în mare copiilor de 1-4 ani.</p>',
  [('model', 'Geox GISLI sneakers pentru copii roz B661MA.022BC'), ('imprimeu', 'imprimeul drăguț'), ('material', 'Piele naturală, Material textil, Material sintetic'),
   ('Respira', 'Tehnologia GEOX Respira'), ('membrană', 'Membrana microporoasă din talpă susține ventilația, protejând în același timp împotriva pătrunderii apei'),
   ('profil', 'Profilul înalt al părții superioare'), ('guler', 'Gulerul superior ușor întărit'), ('scai', 'Închiderea practică cu scai'),
   ('talpă', 'Talpa plată din cauciuc'), ('călcâi', 'Călcâiul întărit'), ('interior', 'Interiorul căptușit cu material textil')],
  {'Model': 'Geox GISLI', 'Material': 'piele naturală, textil și sintetic, talpă din cauciuc', 'Caracteristici': 'profil înalt, scai, membrană în talpă, GEOX Respira™', 'Cod produs': 'B661MA.022BC'})

w(8932,
  f'<p>{A("/brand/reima/", "Reima")} 5100053A sunt {A("/categorie/unisex-imbracaminte-pantaloni-treninguri/", "pantaloni de schi unisex")}, albi, cu bretele, din poliamidă cu acoperire din poliuretan și căptușeală din poliester. Magazinul îi trece la sporturi de iarnă, iar tratamentul BIONIC-FINISH® ECO respinge apa.</p>'
  '<p>Fasonul e drept, cu talie regulată, iar bretelele țin pantalonii pe loc și urcă spatele mai sus, ca zăpada să nu intre când copilul se apleacă.</p>'
  '<p>Ce mai are modelul:</p>'
  + L(('Buzunare', 'cu închidere.'), ('Certificare', 'Bluesign®.'), ('Material', '100% poliamidă, acoperire 100% poliuretan.'))
  + '<p>Mărimile 104-164 sunt pentru copii de aproximativ 4-14 ani.</p>',
  [('cod', 'Reima alb 5100053A'), ('bretele', 'Model cu bretele'), ('material', 'Materialul de baza: 100% Poliamida'), ('acoperire', 'Acoperire: 100% Poliuretan'),
   ('căptușeală', 'Captuseala: 100% Poliester'), ('iarnă', 'Sporturi de iarnă'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('fason', 'Fason drept'),
   ('talie', 'Talie regulata'), ('buzunare', 'Buzunare incheiate'), ('Bluesign', 'Model certificat Bluesign')],
  {'Model': 'Reima 5100053A', 'Material': '100% poliamidă, acoperire poliuretan, căptușeală poliester', 'Caracteristici': 'pantaloni de schi cu bretele, BIONIC-FINISH® ECO, Bluesign®', 'Cod produs': '5100053A'})

w(8935,
  f'<p>{TH} KB0KB09882 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de iarnă pentru băieți")}, neagră, izolată, cu interior din fleece și blăniță din poliester și acril. Gulerul ridicat și gluga fixă o fac potrivită pentru zilele geroase.</p>'
  '<p>Croiala e simplă, iar fermoarul pe toată lungimea o face ușor de pus și de scos, chiar și peste un pulover gros.</p>'
  '<p>Pe scurt, din ce e făcută:</p>'
  + L(('Exterior', '100% poliester.'), ('Umplutură', 'poliester.'), ('Blăniță', '86% poliester, 14% acril.'), ('Buzunare', 'oblice, exterioare.'))
  + '<p>Pe site sunt mărimile 128-176, pentru copii de pe la 8 la 16 ani.</p>',
  [('cod', 'KB0KB09882'), ('culoare', 'culoarea negru'), ('izolat', 'Model izolat'), ('fleece', 'material fleece'), ('blană', 'Blana: 86% Poliester , 14% Acril'),
   ('guler, glugă', 'Gulerul ridicat și gluga fixă'), ('croială', 'Tăiere simplă'), ('fermoar', 'Închiderea convenabilă cu fermoar'),
   ('material', 'Materialul de baza: 100% Poliester'), ('umplutură', 'Umplutura: 100% Poliester'), ('buzunare', 'Buzunare oblice exterioare')],
  {'Model': 'Tommy Hilfiger KB0KB09882', 'Material': '100% poliester, blăniță poliester și acril', 'Caracteristici': 'izolată, glugă fixă, guler ridicat, fermoar', 'Cod produs': 'KB0KB09882'})

w(8941,
  f'<p>{TH} KB0KB10114 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă matlasată pentru băieți")}, bej, izolată cu umplutură sintetică, din poliester neted. Finisajul hidrofob lasă apa să se scurgă pe suprafață, deci geaca ține la ploaie ușoară, deși magazinul precizează că nu garantează impermeabilitate completă.</p>'
  '<p>Croiala e simplă, iar fermoarul e dublat de capse, ca geaca să se închidă bine pe vânt.</p>'
  '<p>Detaliile gecii:</p>'
  + L(('Glugă', 'are.'), ('Buzunare', 'două, laterale.'), ('Căptușeală', 'are.'), ('Material', '100% poliester.'))
  + '<p>Geaca vine în mărimile 128-176, potrivite cam pentru 8-16 ani.</p>',
  [('cod', 'KB0KB10114'), ('culoare', 'culoarea bej'), ('izolat', 'Model izolat'), ('matlasat', 'Model matlasat'), ('izolație', 'izolație sintetica'),
   ('hidrofob', 'Finisajul hidrofob al materialului oferă rezistență la apă'), ('scurgere', 'să se scurgă fără a fi absorbită'),
   ('nu complet', 'nu garantează impermeabilitatea completă'), ('croială', 'Tăiere simplă'), ('fermoar, capse', 'Fixare cu fermoar si snap'),
   ('glugă', 'Gluga: cu gluga'), ('buzunare', 'Două buzunare laterale'), ('căptușeală', 'Captuseala: cu captuseala'), ('material', '100% Poliester')],
  {'Model': 'Tommy Hilfiger KB0KB10114', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'matlasată, finisaj hidrofob, glugă, fermoar și capse', 'Cod produs': 'KB0KB10114'})

w(8942,
  f'<p>{A("/brand/reima/", "Reima")} Ilves este o {A("/categorie/unisex-accesorii-caciuli-manusi-accesorii/", "căciulă de iarnă unisex")} neagră, din tricot de grosime medie combinat cu imitație de blană, cu model. Are un profil special în jurul urechilor, care le apără de frig, și tratamentul BIONIC-FINISH® ECO, care respinge apa.</p>'
  '<p>Căptușeala e din poliester parțial reciclat, iar materialul de bază e 100% poliester reciclat. Modelul e certificat Bluesign®.</p>'
  '<p>Cum alegi mărimea:</p>'
  + L(('Mărime', 'numărul (48-56) e circumferința capului în centimetri; măsori capul pe frunte și deasupra urechilor.'), ('Urechi', 'acoperite de profilul special al căciulii.'), ('Material', 'tricot și imitație de blană.'))
  + '<p>Plaja 48-56 acoperă, de obicei, copii de la 1 an în sus.</p>',
  [('model', 'Reima Ilves negru 5300111C'), ('tricot', 'Tricotaje: grosime medie'), ('blană', 'material tricotat cu imitație de blană'), ('model', 'Model: cu modele'),
   ('urechi', 'Un profil special în jurul urechilor le protejează de frig'), ('BIONIC', 'BIONIC-FINISH® ECO'), ('reciclat', 'Material de bază: 100% Poliester reciclat'),
   ('căptușeală', 'Captuseala: 70% Poliester reciclat, 30% Poliester'), ('Bluesign', 'Model certificat Bluesign')],
  {'Model': 'Reima Ilves', 'Material': 'poliester reciclat, tricot și imitație de blană', 'Caracteristici': 'protecție pentru urechi, BIONIC-FINISH® ECO, Bluesign®', 'Cod produs': '5300111C'},
  varsta_txt='de la 1 an în sus', notes=['Mărimile căciulii sunt circumferința capului (cm); vârsta e estimată.'])

w(8957,
  f'<p>{A("/brand/guess/", "GUESS")} L6RN03 este o {A("/categorie/baieti-imbracaminte-geci-jachete/", "geacă de tranziție pentru băieți")}, verde, din material neted cu 98% bumbac și 2% spandex, fără izolație și fără căptușeală. Se poartă primăvara și toamna, peste un tricou sau un hanorac.</p>'
  '<p>Croiala e simplă, iar spandexul dă materialului puțină elasticitate. Se închide cu nasturi.</p>'
  '<p>Buzunarele sunt partea practică a gecii:</p>'
  + L(('Buzunar', 'pe piept.'), ('Buzunare laterale', 'două.'), ('Glugă', 'nu are.'), ('Material', '98% bumbac, 2% spandex.'))
  + '<p>Mărimile de pe site încep la 122-125 și ajung la 175, pentru copii de aproximativ 7-16 ani.</p>',
  [('cod', 'L6RN03 WJ820'), ('culoare', 'culoarea verde'), ('neizolat', 'Model neizolat'), ('necăptușit', 'Captuseala: necaptusit'), ('tranziție', 'Izolare: tranzitional'),
   ('material', '98% Bumbac, 2% Spandex'), ('croială', 'Tăiere simplă'), ('buton', 'Închiderea convenabilă cu buton'), ('piept', 'Buzunar pe piept'),
   ('laterale', 'Două buzunare laterale'), ('fără glugă', 'Gluga: fara gluga')],
  {'Model': 'GUESS L6RN03', 'Material': '98% bumbac, 2% spandex', 'Caracteristici': 'de tranziție, fără căptușeală, nasturi, trei buzunare', 'Cod produs': 'L6RN03.WJ820'})

w(8958,
  f'<p>{A("/brand/adidas/", "adidas")} JW2454 este o {A("/categorie/unisex-imbracaminte-geci-jachete/", "geacă matlasată unisex")}, roz, ușor izolată cu umplutură sintetică și tehnologia CLIMAWARM, care păstrează căldura și la efort. E pentru zilele mai reci, la copiii mai mici.</p>'
  '<p>Gluga, mânecile și marginea de jos au garnitură elastică, deci geaca se potrivește mai bine pe corp și nu lasă frigul pe la margini.</p>'
  '<p>Pentru drumurile de seară și pentru mărunțișuri:</p>'
  + L(('Elemente reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Buzunare', 'două, laterale, cu fermoar.'), ('Închidere', 'fermoar.'), ('Material', '100% poliester.'))
  + '<p>Mărimile 110-128 se potrivesc cam copiilor de 5-8 ani.</p>',
  [('cod', 'JW2454'), ('culoare', 'culoarea roz'), ('ușor izolat', 'Model ușor izolat'), ('matlasat', 'material matlasat'), ('izolație', 'izolatie sintetică'),
   ('CLIMAWARM', 'Tehnologia CLIMAWARM'), ('efort', 'efortului intens'), ('temperaturi', 'temperaturi mai reci'),
   ('elastic', 'Gluga, mânecile și marginea inferioară sunt finisate cu o garnitură elastică'), ('reflectorizante', 'Elementele reflectorizante sporesc vizibilitatea'),
   ('buzunare', 'Două buzunare laterale antiderapante și cu fermoar'), ('fermoar', 'Închiderea convenabilă cu fermoar'), ('material', '100% Poliester')],
  {'Model': 'adidas JW2454', 'Material': '100% poliester, izolație sintetică', 'Caracteristici': 'ușor izolată, CLIMAWARM, glugă, garnituri elastice, reflectorizante', 'Cod produs': 'JW2454'})

w(8968,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 262277 sunt {A("/categorie/unisex-incaltaminte-adidasi/", "adidași unisex")}, albaștri, din imitație de piele întoarsă, piele ecologică și material textil, ușori și făcuți pentru purtat zilnic. Au fost creați cu medici pediatri și ingineri de la Institutul de Biomecanică din Valencia.</p>'
  '<p>Șireturile elastice cu închidere cu cârlig se strâng fără nod, iar tăietura în formă de U de la spate lasă glezna liberă și nu apasă pe tendonul lui Ahile.</p>'
  '<p>Construcția Biomecanics include:</p>'
  + L(('Branț', 'detașabil, antibacterian, profilat la mijloc.'), ('Talpă', 'în formă de „picior de elefant” la călcâi.'), ('Vârf', 'protejat.'), ('Inserție', 'perforată.'))
  + '<p>Numerele 28-38 îi fac potriviți, de obicei, pentru copii de la 4 ani în sus.</p>',
  [('cod', 'Sneakers pentru copii 262277'), ('culoare', 'albastru'), ('material', 'imitatie de piele intoarsa, piele ecologică și material textil'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('Valencia', 'medici pediatri si ingineri de la Institutul de Biomecanica din Valencia'), ('închidere', 'Șireturile elastice și închiderea cu cârlig'),
   ('U', 'tendonului lui Ahile'), ('branț', 'Brant detasabil si antibacterian, profilat la mijlocul piciorului'), ('talpă', 'Talpa in forma de „picior de elefant” peste calcaie'),
   ('vârf', 'Degetul securizat'), ('inserție', 'insertiei perforate')],
  {'Model': 'Biomecanics 262277', 'Material': 'imitație de piele întoarsă, piele ecologică și textil', 'Caracteristici': 'șireturi elastice, tăietură în U, branț antibacterian detașabil', 'Cod produs': '262277'},
  notes=['Titlul de pe site nu are culoare; magazinul arată albastru.'])

w(8972,
  f'<p>{GEOX} are în acest model {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi din piele unisex")}, negri, din piele naturală la exterior și la interior, cu talpă din cauciuc și sistemul Geox Respira. Branțul Geox, din piele cu perforații, are proprietăți antibacteriene și sistem anti-shock.</p>'
  '<p>Se leagă cu șiret clasic, care se strânge exact pe picior; partea de sus e rigidizată, iar vârful rotund și întărit.</p>'
  '<p>Pe scurt:</p>'
  + L(('Material', 'piele naturală.'), ('Branț', 'din piele, perforat, conturat.'), ('Talpă', 'exterioară, din cauciuc.'))
  + '<p>Pe site sunt numerele 35-41, pentru copii mari, în general de la 10 ani în sus.</p>',
  [('model', 'Pantofi copii culoarea negru'), ('piele', 'confecționat din piele naturala'), ('interior', 'Interiorul: Piele naturala'), ('talpă', 'Talpa exterioară din cauciuc'),
   ('Respira', 'talpei in trei straturi cu sistemul de perforari'), ('branț', 'brant din piele cu perforari'), ('antibacterian', 'Are proprietati antibacteriene'),
   ('anti-shock', 'sistemului anti-shockl'), ('conturat', 'Este conturat corespunzator'), ('șiret', 'Șiretul clasic permite ajustarea individuală'),
   ('rigidizat', 'Partea superioară rigidizată'), ('vârf', 'Cutie rotunda, intarita')],
  {'Model': 'Geox, pantofi din piele', 'Material': 'piele naturală, interior din piele, talpă din cauciuc', 'Caracteristici': 'Geox Respira, branț Geox din piele, șiret', 'Cod produs': ''})
print('lot 11 scris')
