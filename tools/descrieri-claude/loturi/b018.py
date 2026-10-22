import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from desc_tools import w, up, L, A

GEOX = A('/brand/geox/', 'Geox')
PRIM = A('/brand/primigi/', 'Primigi')
RESPIRA = ('Respira', 'talpei in trei straturi cu sistemul de perforari')

w(9251,
  f'<p>{A("/brand/reima/", "Reima")} Viikari sunt {A("/categorie/unisex-incaltaminte-pantofi/", "pantofi impermeabili unisex")}, ușori, din material textil și sintetic, cu talpă din cauciuc. Pe site apar ca gri, iar magazinul îi arată violeți. Sunt pentru joaca afară, inclusiv pe vreme umedă.</p>'
  '<p>Vârful e lat și rotund, de tip barefoot, deci degetele stau în poziție naturală și au loc chiar și la un picior mai lat. Gulerul și călcâiul sunt moi, iar aricii se prind repede.</p>'
  '<p>Mai trebuie știut:</p>'
  + L(('Elemente reflectorizante', 'pentru vizibilitate după lăsarea întunericului.'), ('Interior', 'material textil.'), ('Izolație', 'nu au, sunt pantofi de sezon blând.'))
  + '<p>Numerele 22-31 sunt pentru copii de aproximativ 1-7 ani.</p>',
  [('model', 'Reima Pantofi pentru copii Viikari violeți 5400159B'), ('material', 'combinație de material textil și sintetic'), ('impermeabil', 'Model impermeabil'),
   ('talpă', 'Talpa din cauciuc'), ('aer liber', 'jocurilor în aer liber'), ('barefoot', 'Vârf lat și rotund de tip barefoot'), ('degete', 'poziția naturală a degetelor'),
   ('guler', 'Gulerul moale al părții superioare și călcâiul'), ('arici', 'Închidere cu arici'), ('reflectorizante', 'Elemente reflectorizante'),
   ('interior', 'Interior din material textil'), ('neizolat', 'Izolare: neizolat')],
  {'Model': 'Reima Viikari', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'impermeabili, vârf lat barefoot, arici, reflectorizante', 'Cod produs': '5400159B'},
  notes=['Titlul de pe site spune gri; magazinul îi arată violeți.'])

w(9257,
  f'<p>{PRIM} PBZ 23532 sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași înalți pentru băieți")}, albaștri, din piele întoarsă și material textil, cu interior căptușit cu piele naturală și textil. Sunt pentru copiii mici, activi, la jocurile zilnice.</p>'
  '<p>Profilul înalt are guler moale, iar călcâiul e tot moale, deci gheata se așază pe gleznă fără să roadă; aricii se prind repede. Talpa e plată și subțire, pentru o poziție naturală a piciorului.</p>'
  '<p>Pe dedesubt și înăuntru:</p>'
  + L(('Talpă', 'din cauciuc, plată.'), ('Branț', 'detașabil, din piele naturală.'), ('Interior', 'piele naturală și material textil.'))
  + '<p>Numerele 19-29 se potrivesc copiilor de cam 1-5 ani.</p>',
  [('model', 'Primigi Sneakers pentru copii albastri PBZ 23532'), ('material', 'Partea superioară din piele întoarsă și material textil'), ('interior', 'Interior căptușit cu piele naturală și material textil'),
   ('activi', 'conceput pentru copiii activi'), ('profil', 'Profil înalt al părții superioare cu guler moale'), ('călcâi', 'Călcâi moale'), ('arici', 'Închidere practică cu arici'),
   ('talpă', 'Talpă din cauciuc'), ('talpă plată', 'Talpă plată'), ('branț', 'Branțuri detașabile din piele naturală')],
  {'Model': 'Primigi PBZ 23532', 'Material': 'piele întoarsă și textil, interior piele naturală și textil, talpă din cauciuc', 'Caracteristici': 'profil înalt, guler moale, arici, branț din piele detașabil', 'Cod produs': '23532'},
  notes=['Titlul de pe site nu are culoare; magazinul arată albastru.'])

w(9262,
  f'<p>{A("/brand/biomecanics/", "Biomecanics")} 261167 sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași de iarnă pentru bebeluși")}, roz, căptușiți, din piele naturală și material sintetic, cu membrana BioTEX, care blochează umezeala de afară. Sunt pentru plimbările de iarnă și joaca afară pe frig.</p>'
  '<p>Structura multistrat BioTEX lasă vaporii să iasă, iar aricii fac încălțatul rapid, ceea ce contează la un copil mic, îmbrăcat gros.</p>'
  '<p>Mai au:</p>'
  + L(('Vârf', 'rotund, întărit, protejează degetele.'), ('Călcâi', 'întărit.'), ('Tehnologie', 'Biomecanics Podology Partnership, cu podologi.'))
  + '<p>Numerele de pe site, 19-26, sunt pentru copii de aproximativ 1-4 ani.</p>',
  [('cod', 'Sneakers pentru copii roz 261167'), ('iarnă', 'Sneakerșii de iarnă'), ('căptușit', 'încălțăminte căptușită'), ('material', 'Partea superioară din piele naturală'),
   ('BioTEX', 'Membrana BioTEX'), ('umezeală', 'blocând umiditatea din exterior'), ('plimbări', 'plimbările de iarnă și joaca în aer liber'),
   ('multistrat', 'Structura multistrat BioTEX permite evacuarea vaporilor de apă'), ('arici', 'Închiderea cu arici'), ('vârf', 'Vârful rotund întărit protejează degetele'),
   ('călcâi', 'Călcâiul întărit'), ('Podology', 'Tehnologia Biomecanics Podology Partnership')],
  {'Model': 'Biomecanics 261167', 'Material': 'piele naturală și sintetic, interior textil', 'Caracteristici': 'de iarnă, căptușiți, membrană BioTEX, arici', 'Cod produs': '261167'})

w(9265,
  f'<p>{GEOX} ASSISTER J56E9B sunt {A("/categorie/adidasi/", "adidași cu luminițe pentru fete")}, bleumarin, din material textil și sintetic, ușor de întreținut. Talpa patentată GEOX Respira™ are membrană, care elimină umezeala și oprește apa să intre, deci merg și pe vreme umedă.</p>'
  '<p>Închiderea cu scai se prinde și se desface repede, de către copil singur, iar călcâiul întărit ține piciorul fix.</p>'
  '<p>Pe scurt:</p>'
  + L(('Luminițe', 'încorporate, vizibile seara.'), ('Talpă', 'plată, din cauciuc.'), ('Interior', 'textil și sintetic.'))
  + '<p>Numerele 28-34 sunt, cu aproximație, pentru copii de 4-11 ani.</p>',
  [('model', 'Geox ASSISTER sneakers pentru copii bleumarin J56E9B.0ASKN'), ('material', 'Partea superioară din material textil și sintetic'),
   ('întreținere', 'este ușoară și ușor de întreținut'), ('Respira', 'Tehnologia GEOX Respira'), ('membrană', 'Membrana microporoasă din talpă elimină eficient umezeala'),
   ('apă', 'Talpa patentată protejează împotriva pătrunderii apei în interior'), ('scai', 'Sistemul practic de închidere cu scai'), ('călcâi', 'Călcâi întărit'),
   ('luminițe', 'Luminițele încorporate'), ('talpă', 'Talpa plată din cauciuc'), ('interior', 'Interiorul din material textil și sintetic')],
  {'Model': 'Geox ASSISTER J56E9B', 'Material': 'textil și sintetic, talpă din cauciuc', 'Caracteristici': 'luminițe, scai, GEOX Respira™ cu membrană', 'Cod produs': 'J56E9B.0ASKN'})

w(9267,
  f'<p>{PRIM} PPE GTX 89344 sunt {A("/categorie/unisex-incaltaminte-ghete-cizme/", "cizme de zăpadă unisex")}, albastre, izolate, din material textil și piele ecologică, cu membrana GORE-TEX®, impermeabilă și rezistentă la vânt. Partea de sus are rezistență crescută la înmuiere.</p>'
  '<p>Se închid cu scai, deci se încalță repede, chiar și cu mănuși, iar căptușeala textilă e moale. Partea de sus e rigidizată și ține piciorul.</p>'
  '<p>Pentru zăpadă:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Absorbție', 'talpa absoarbe șocurile.'), ('Interior', 'textil, moale.'))
  + '<p>Numerele 24-29 se potrivesc copiilor de pe la 2 până pe la 5 ani.</p>',
  [('model', 'Primigi Cizme de iarnă copii PPE GTX 89344'), ('zăpadă', 'Cizme de zăpadă pentru copii'), ('izolat', 'Model Izolat'), ('material', 'combinația materialului textil cu pielea ecologică'),
   ('GORE-TEX', 'Model cu membrana GORE-TEX®, care este extrem de subtire si 100% impermeabila, rezistenta la vant'), ('înmuiere', 'Partea superioară cu rezistență crescută la înmuiere'),
   ('scai', 'Închiderea cu velcro'), ('căptușeală', 'căptușeală moale din material textil'), ('rigidizat', 'Partea superioară rigidizată'), ('talpă', 'Talpa exterioară din cauciuc'),
   ('absorbție', 'Absorbtia socului'), ('culoare', 'albastru')],
  {'Model': 'Primigi PPE GTX 89344', 'Material': 'textil și piele ecologică, căptușeală textilă, talpă din cauciuc', 'Caracteristici': 'izolate, GORE-TEX®, scai', 'Cod produs': '89344'},
  notes=['Titlul de pe site nu are culoare; magazinul arată albastru.'])

w(9269,
  f'<p>{GEOX} SPRINTYE B454UC sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")}, albaștri, din material textil și piele ecologică, ușori și făcuți pentru purtat zilnic, cu sistemul Geox Respira în talpă.</p>'
  '<p>Deschiderea e largă, iar vârful rotund, ușor rigid, lasă degetele să stea liber. Șireturile elastice cu închidere cu cârlig se strâng fără nod, iar bucla de la spate ajută la încălțat.</p>'
  '<p>Mai au:</p>'
  + L(('Călcâi', 'contor rigid.'), ('Interior', 'textil.'), ('Profil', 'sub gleznă.'))
  + '<p>Numerele 20-27 se potrivesc copiilor de aproximativ 1-4 ani.</p>',
  [('model', 'Sneakers pentru copii SPRINTYE B454UC.01454'), ('material', 'combinația materialului textil cu pielea ecologică'), ('zilnic', 'ideal pentru purtarea zilnică'),
   RESPIRA, ('deschidere', 'Deschidere larga'), ('vârf', 'Degetul rotund, ușor rigid'), ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('buclă', 'Bucla de la spate'),
   ('călcâi', 'Contorul de călcâi rigid'), ('interior', 'Interiorul textil'), ('profil', 'Pantoful de sub gleznă'), ('culoare', 'albastru')],
  {'Model': 'Geox SPRINTYE B454UC', 'Material': 'textil și piele ecologică, interior textil', 'Caracteristici': 'Geox Respira, deschidere largă, șireturi elastice', 'Cod produs': 'B454UC.01454'},
  notes=['Titlul de pe site nu are culoare; magazinul arată albastru.'])

w(9270,
  f'<p>{GEOX} WASHIBA J45LQA sunt {A("/categorie/baieti-incaltaminte-adidasi/", "adidași pentru băieți")} bleumarin, din piele întoarsă, ușori și făcuți pentru purtat zilnic. Au profil scurt și sistemul Geox Respira în talpă.</p>'
  '<p>Șireturile elastice și închiderea cu cârlig se strâng fără nod, iar vârful rotund, ușor rigid, lasă degetele să stea liber în pantof. Profilul scurt lasă glezna liberă, iar interiorul textil e ușor de ținut curat.</p>'
  '<p>Construcția:</p>'
  + L(('Călcâi', 'contor rigidizat.'), ('Talpă', 'exterioară, din cauciuc.'), ('Interior', 'textil.'))
  + '<p>Numerele 24-35 sunt pentru copii de cam 2-11 ani.</p>',
  [('model', 'Sneakers pentru copii WASHIBA culoarea bleumarin, J45LQA.000BC'), ('material', 'confecționat din piele întoarsă'), ('zilnic', 'ideal pentru purtarea zilnică'),
   ('profil', 'Înălțime: mic de statură'), RESPIRA, ('închidere', 'Șireturile elastice și închiderea cu cârlig'), ('vârf', 'Degetul rotund, ușor rigid'),
   ('degete', 'degetele se pot aranja liber'), ('călcâi', 'Contorul de călcâi rigidizat'), ('talpă', 'Talpa exterioară din cauciuc'), ('interior', 'Interiorul textil este confortabil pentru picior și facilitează păstrarea pantofilor curați')],
  {'Model': 'Geox WASHIBA J45LQA', 'Material': 'piele întoarsă, interior textil, talpă din cauciuc', 'Caracteristici': 'Geox Respira, șireturi elastice cu cârlig, profil scurt', 'Cod produs': 'J45LQA.000BC'})

w(9271,
  f'<p>{GEOX} IUPIDOO sunt {A("/categorie/bebe-incaltaminte-adidasi/", "adidași pentru bebeluși")} verzi, din material textil, piele întoarsă și piele naturală, ușori, de purtat zilnic. Interiorul e din piele naturală, cu finisaj antibacterian, care previne mirosurile.</p>'
  '<p>Branțul are sistemul Light Flexy, pentru un pas liber, iar aricii fac încălțatul rapid. Profilul e scurt, sub gleznă, iar branțul din piele previne frecarea la mers.</p>'
  '<p>Mai au:</p>'
  + L(('Geox Respira', 'talpă în trei straturi.'), ('Branț', 'din piele.'), ('Interior', 'piele naturală, antibacterian.'))
  + '<p>Numerele 18-26 se potrivesc în general copiilor de 1-4 ani.</p>',
  [('model', 'Sneakers pentru copii IUPIDOO culoarea verde, B3555D.02214'), ('material', 'combinație de material textil, piele întoarsă și piele naturală'),
   ('zilnic', 'ideal pentru purtarea zilnică'), ('interior', 'Interiorul: Piele naturala'), ('antibacterian', 'Finisajul antibacterian din interiorul încălțămintei'),
   ('Light Flexy', 'Light Flexy Sistem de brant'), ('arici', 'Închiderea cu velcro'), ('profil', 'Înălțime: mic de statură'), RESPIRA, ('branț', 'Brantul din piele este confortabil pentru picior si previne frecarea')],
  {'Model': 'Geox IUPIDOO', 'Material': 'textil, piele întoarsă și piele naturală', 'Caracteristici': 'Light Flexy, finisaj antibacterian, arici, Geox Respira', 'Cod produs': 'B3555D.02214'})

up(9283, [
    ('Pe site apar numerele de la 24 până la 35, potrivite orientativ copiilor între 2 și 11 ani.</p>',
     'Pe site apar numerele de la 24 până la 35, potrivite în general copiilor între 2 și 11 ani; vârful rotund lasă loc degetelor.</p>'),
])

w(9287,
  f'<p>{PRIM} PROGT 88666 sunt {A("/categorie/ghete-cizme/", "cizme de zăpadă pentru fete")}, negre, izolate, din material textil și piele întoarsă, cu membrana GORE-TEX® și interior din lână. Sunt făcute pentru zăpadă și ger.</p>'
  '<p>Cutia degetelor e lată, cu loc pentru un picior mai plinuț, iar partea de sus urcă pe gleznă. Se închid cu șiret și fermoar lateral, deci se încalță ușor fără să desfaci șiretul.</p>'
  '<p>Pentru iarnă, mai au:</p>'
  + L(('Talpă', 'exterioară, din cauciuc.'), ('Absorbție', 'talpa absoarbe șocurile.'), ('Interior', 'lână, cu termoreglare.'))
  + '<p>Numerele 25-40 acoperă copii de la aproximativ 2 ani până la adolescenți.</p>',
  [('model', 'Primigi Cizme de iarna copii culoarea negru, PROGT 88666'), ('zăpadă', 'Cizme de zapada pentru copii'), ('izolat', 'Izolare: izolat'),
   ('material', 'combinatia materialului textil cu pielea intoarsa'), ('GORE-TEX', 'Model cu membrana GORE-TEX'), ('lână', 'Un model cu interior din lână'),
   ('cutie lată', 'Cutia lată a degetelor'), ('gleznă', 'Partea superioară ridicată'), ('închidere', 'Model cu siret cu fermoar lateral'),
   ('talpă', 'Talpa exterioară din cauciuc'), ('absorbție', 'Absorbtia socului'), ('termoreglare', 'proprietăților sale mari de termoreglare')],
  {'Model': 'Primigi PROGT 88666', 'Material': 'textil și piele întoarsă, interior din lână, talpă din cauciuc', 'Caracteristici': 'izolate, GORE-TEX®, interior din lână, șiret și fermoar lateral', 'Cod produs': '88666'})
print('lot 18 scris')
