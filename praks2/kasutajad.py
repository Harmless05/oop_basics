from praks2.kasutaja import Kasutaja

#Kasutajad = str(input("Palun sisestage failinimi: "))
#(Kasutajad)

kasutaja1 = Kasutaja()
kasutaja1.eesnimi = "John"
kasutaja1.perenimi = "Doe"
kasutaja1.vanus = "30"
kasutaja1.sugu = "Male"
kasutaja1.kasutaja_nimi = "Johnny"
kasutaja1.kirjelad_kasutaja()
kasutaja1.tervita_kasutaja()

print("")

kasutaja2 = Kasutaja()
kasutaja2.eesnimi = "Enar"
kasutaja2.perenimi = "Jõesaar"
kasutaja2.vanus = "16"
kasutaja2.sugu = "Male"
kasutaja2.kasutaja_nimi = "Enar123"
kasutaja2.kirjelad_kasutaja()
kasutaja2.tervita_kasutaja()

print("")

kasutaja3 = Kasutaja()
kasutaja3.eesnimi = "Kristjan"
kasutaja3.perenimi = "Kruus"
kasutaja3.vanus = "16"
kasutaja3.sugu = "Male"
kasutaja3.kasutaja_nimi = "Kris"
kasutaja3.kirjelad_kasutaja()
kasutaja3.tervita_kasutaja()

#print(kasutaja1.kirjelad_kasutaja())
#print(kasutaja1.tervita_kasutaja())
