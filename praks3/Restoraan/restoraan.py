class Restoraan:
    def __init__(self, restoraani_nimi, soogi_tyyp, teenindatud_kylastajad = "0"):
        self.restoraani_nimi = restoraani_nimi
        self.soogi_tyyp = soogi_tyyp
        self.teenindatud_kylastajad = teenindatud_kylastajad

    def määra_teenindatud_kylalised(self):

    def suurenda_teenindatud_kylalised(self):

    #functions
    def kirjelda_restoraan(self, restoraani_nimi, soogi_tyyp):
        print("Restoraan " + str(self.restoraani_nimi) + " pakub " + str(self.soogi_tyyp))

    def ava_restoraan(self, restoraani_nimi):
        print("Restoraan" + str(self.restoraani_nimi) + " on avatud!")

    #def info(self):
    #    print(self.restoraani_nimi)
    #    print(self.soogi_tyyp)