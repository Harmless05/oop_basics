class Kasutaja():
    #atributes
    eesnimi = ""
    perenimi = ""
    vanus = ""
    sugu = ""
    kasutaja_nimi = ""

    def kirjelad_kasutaja(self):
        print("Kasutaja andmed: ")
        print("Eesnimi: " + str(self.eesnimi))
        print("Perenimi: " + str(self.perenimi))
        print("Vanus: " + str(self.vanus))
        print("Sugu: " + str(self.sugu))
        print("Kasutaja nimi: " + str(self.kasutaja_nimi))

    def tervita_kasutaja(self):
        print("Tere tulemast " + str(self.eesnimi) + " " + str(self.perenimi) + str(", teie vanus on " + str(self.vanus)))
        #print("Tere, {0} {1}".format(self.eesnimi, self.perenimi))
        #print("Teretulemast kasutajasse", str(self.kasutaja_nimi))

    def __del__(self):
        print("Kasutaja on kustutatud")