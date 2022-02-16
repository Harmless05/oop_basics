class AknadUksed:
    def __init__(self, laius, korgus):
        self.pindala = laius * korgus

class Tuba:
    def __init__(self, p, l, k):
        self.pikkus = p
        self.laius = l
        self.korgus = k
        self.aknad_uksed = []

    def LisaAkkenUks (self, laius, korgus):
        self.aknad_uksed.append(AknadUksed(laius, korgus))

    def taisPind(self):
        return 2 + self.korgus * (self.pikkus + self.laius)

    def tooPind (self):
        uus_pindala = self.taisPind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala
    def tapeedid(self, tp, tl):
        return int(self.tooPind() / (tp * tl)) + 1

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