class AknadUksed:
    """Klass akna või ukse objekti kirjeldamiseks"""
    def __init__(self, laius, korgus):
        self.pindala = laius * korgus
        """
        Aken või ukse objekti loomiseks vajalik 
        Aken või uks määratakse pindalaga tema mõõtudest lähtuvalt
        """


class Tuba:
    """Klass tuba kirjeldamiseks"""
    def __init__(self, p, l, k):
        """Annab tähtsuse pikkusele, laiusele, kõrgusele ja sellele, kas on olemas aknad ja uksed."""
        self.pikkus = p
        self.laius = l
        self.korgus = k
        self.aknad_uksed = []

    def LisaAkkenUks (self, laius, korgus):
        """Lisab akna või ukse"""
        self.aknad_uksed.append(AknadUksed(laius, korgus))

    def taisPind(self):
        """Arvutab täispinna. 2 + kõrgus * (pikkus + laius)"""
        return 2 + self.korgus * (self.pikkus + self.laius)

    def tooPind (self):
        """Toob välja mitu ruutmeetrit tapeeti on vaja kleepida"""
        uus_pindala = self.taisPind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala

    def tapeedid(self, tp, tl):
        """Arvutab mitu tapeedi rulli läheb vaja"""
        return int(self.tooPind() / (tp * tl)) + 1