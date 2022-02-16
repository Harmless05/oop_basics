from praks9.koodi_dokumenteerimine import AknadUksed, Tuba

# Küsib ruumi/toa mõõtusid
print("Ruumi mõõdud: ")
p = float(input("Pikkus: "))
l = float(input("Laius: "))
k = float(input("Kõrgus: "))

tuba = Tuba(p, l, k)

# Küsib kas on olemas aknad või uksed
vastus = input("Kas olemas on aknad/usked? (jah/ei) ")

# Kui "jah", siis küsib akna või ukse laiust ja kõrgust
while vastus == "jah":
    l = float(input("Akna/Ukse laius "))
    k = float(input("Akna/Ukse kõrgus "))
    aken_uks = AknadUksed(l, k)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas olemas aknad/uksed? (jah/ei) ")

# Küsib tapeedi rulli mõõte
print("Tapeedi rulli mõõtud: ")
tl = float(input("Tapeedi rulli laius "))
tp = float(input("Tapeedi rulli pikkus "))

# Väljastab mitu ruutmeetrit tapeeti on vaja kleepida seinale
print("Tapeedid on vaja kleepida " + str(tuba.tooPind()) + " ruutmeetrile")

# Väljastab mitu tapeedi rulli läheb vaja
print("Tapeedi rullida arv " + str(tuba.tapeedid(tp, tl)))