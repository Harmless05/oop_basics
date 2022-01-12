class Kasutaja():
    #atributes
    def __init__(self, k_eesnimi, k_perenimi, k_vanus, k_sugu, k_kasutaja_nimi):
        self.eesnimi = k_eesnimi
        self.perenimi = k_perenimi
        self.vanus = k_vanus
        self.sugu = k_sugu
        self.kasutaja_nimi = k_kasutaja_nimi

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