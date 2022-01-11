class Restoraan():
    #atributes
    restoraani_nimi = "Sirp"
    soogi_tyyp = "Good soup"

    #functions
    def kirjelda_restoraan(self, restoraani_nimi, soogi_tyyp):
        print("Restoraan " + str(self.restoraani_nimi) + " pakub " + str(self.soogi_tyyp))

    def ava_restoraan(self, restoraani_nimi):
        print("Restoraan" + str(self.restoraani_nimi) + " on avatud!")

    def info(self):
        print(self.restoraani_nimi)
        print(self.soogi_tyyp)