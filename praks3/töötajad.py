from praks3.töötaja import Inimene

kristjan = Inimene()
kristjan.__init__("Kristjan", "Kruus", 1)
kristjan.tutvustus()
kristjan.vallandatud()

enar = Inimene()
enar.__init__("Enar", "Jõesaar", 0)
enar.tutvustus()
enar.vallandatud()

martin = Inimene()
martin.__init__("Martin", "Kõivik", 1)
martin.tutvustus()
martin.vallandatud()

#kristjan.__del__()
#kristjan.info()
#kristjan.setPerson("Kristjan", 16)
#kristjan.info()
#aa = input("sss")
