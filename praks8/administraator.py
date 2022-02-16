from praks8.kasutaja import Kasutaja

#print("test")
#Kristjan = Kasutaja("Kristjan", "Kruus", "kriss", "kekw")

#print(Kristjan.tervita_kasutaja())
#print("")
#print(Kristjan.kirjelda_kasutaja())
#print()

class Admin(Kasutaja):
    def __init__(self, e, p, kn, passw):
        super().__init__(e, p, kn, passw)
        self.roll = "administraator"
        self.privileegid = Privileegid()



class Privileegid():
    def __init__(self):
        self.privileegid = ["lubatud lisada kasutajad", "lubatud eemaldada kasutajad", "lubatud blokeerida kasutajad"]

    def naita_privileegid(self):
        print("Admini privileegid")
        for privileeg in self.privileegid:
            print(privileeg)

#Enar = Admin("Enar", "Joesaar", "EnarJoe", "qwerty")
#print(Enar.tervita_kasutaja())
#print("")
#print(Enar.kirjelda_kasutaja())
#print()