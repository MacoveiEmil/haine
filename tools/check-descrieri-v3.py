import io,json,re,sys
d=json.load(io.open(sys.argv[1],encoding='utf-8'))
black=["intră în gama","face parte din","fac parte din","se încadrează în","aparține gamei","este inclus în categoria","îl găsești în secțiunea","e o alegere solidă","e o alegere bună","nu stă locului","nu stau o clipă locului","sunt genul de","e gândită pentru","sunt făcuți pentru","e o alegere caldă","este perfect pentru","ține de cald fără să fie greoaie","pe cât de ușoară","încălzește fără să adauge volum","fără să limiteze mișcarea","se asortează ușor","confort și stil","must-have","nu va dezamăgi","ore în șir","compar","cel mai bun","perfect","ideal","extraordinar","premium","revoluționar","vă oferim","recomandăm","în concluzie","așadar","în plus,","de asemenea"," preț"," lei","stoc","answear","sportisimo","fashion days","fashiondays","various"," acum"]
valid={"/categorie/incaltaminte-baieti/","/categorie/incaltaminte-fete/","/categorie/imbracaminte-baieti/","/categorie/imbracaminte-fete/","/categorie/imbracaminte-bebe/"}
for x in d:
    txt=" ".join(x["paragrafe"])
    plain=re.sub(r"\[\[(cat|brand):([^\]]+)\]\]",r"\2",txt)
    words=len(plain.split()); p1=len(re.sub(r"\[\[(cat|brand):([^\]]+)\]\]",r"\2",x["paragrafe"][0]).split())
    links=re.findall(r"\[\[(cat|brand):",txt); low=plain.lower(); issues=[]
    for c,n in (("—","em-dash"),("!","exclamație"),("?","întrebare")):
        if c in txt: issues.append(n)
    issues+=["listă neagră: "+b.strip() for b in black if b in low]
    if sorted(links)!=["brand","cat"]: issues.append("linkuri: "+str(links))
    if x["interlink_categorie"]["url_slug"] not in valid: issues.append("slug invalid")
    if "orientativ" not in low: issues.append("fără orientativ")
    if not 180<=words<=260: issues.append(f"lungime {words}")
    if not 45<=p1<=70: issues.append(f"P1 {p1} cuv")
    if x["gen_text"].startswith("neutru") and re.search(r"\b(fetița|fetiței|băiatul|băiatului|cea mică)\b",low): issues.append("gen ne-neutru")
    if x["gen_text"].startswith("feminin") and re.search(r"\b(băiatul|cel mic)\b",low): issues.append("gen amestecat")
    print(x["id"], words, "cuv,", len(x["paragrafe"]), "par. |", "; ".join(issues) if issues else "OK")
