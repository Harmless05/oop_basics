from praks9.koodi_dokumenteerimine import AknadUksed, Tuba

print("Ruumi mõõdud: ")
p = float(input("Pikkus: "))
l = float(input("Laius: "))
k = float(input("Kõrgus: "))

tuba = Tuba(p, l, k)

vastus = input("Kas olemas on aknad/usked? (jah/ei) ")
while vastus == "jah":
    l = float(input("Akna/Ukse laius "))
    k = float(input("Akna/Ukse kõrgus "))
    aken_uks = AknadUksed(l, k)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas olemas aknad/uksed? (jah/ei) ")

print("Tapeedi rulli mõõtud: ")
tl = float(input("Tapeedi rulli laius "))
tp = float(input("Tapeedi rulli pikkus "))

print("Tapeedid on vaja kleepida " + str(tuba.tooPind()) + " ruutmeetrile")
print("Tapeedi rullida arv " + str(tuba.tapeedid(tp, tl)))