class Kasutaja():
    def __init__(self, ees_nimi, pere_nimi, sugu):
        self.eesnimi = ees_nimi
        self.perenimi = pere_nimi
        self.sugu = sugu

    def kirjelda_kasutaja(self):
        print("Eesnimi: " + str(self.eesnimi) + ", Perenimi: " + str(self.perenimi) + ", Sugu: " + str(self.sugu))

    def tervita_kasutaja(self):
        print(str(self.eesnimi) + " " + str(self.perenimi) + ", Tere jälle!")