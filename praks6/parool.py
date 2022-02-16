class Kasutaja():
    def __init__(self, e, p, sk = 0):
        self.eesnimi = e
        self.perenimi = p
        self.sisse_katse = sk

    def setandmed(self, em, v):
        self.email = em
        self.vanus = v

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1}, vanus on {2} ja email on {3}".format(self.eesnimi, self.perenimi, self.vanus, self.email))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}, sisselogimised: {1}".format(self.eesnimi, self.sisse_katse))

    def suurenda_sisselogimiskatsed(self):
        self.sisse_katse += 1

    def reset_sisselogimiskatsed(self):
        self.sisse_katse = 0

class Andme_muutja:
    def __init__(self):
        self.parool = "qwerty"