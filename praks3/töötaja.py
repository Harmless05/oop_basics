class Inimene:
    def __init__(self, k_eesnimi="nimi", k_perenimi="perenimi", k_kutsekvalifikatsioon="1"):
        self.eesnimi = k_eesnimi
        self.perenimi = k_perenimi
        self.kutsekvalifikatsioon = k_kutsekvalifikatsioon

    def tutvustus(self):
        print("Tere, olen " + str(self.eesnimi) + " " + str(self.perenimi) + "!")

    def __del__(self):
        print("Kõike head, " + str(self.eesnimi) + ", " + str(self.perenimi) + "!")

    def vallandatud(self):
        if self.kutsekvalifikatsioon == 0:
            print("\n" + str(self.eesnimi) + " " + str(self.perenimi) + " sa oled vallandatud, kuna sinu kutsekvalifikatsioon "
                                                           "on madalam kui 1\n")
