class Raamat:
    def __init__(self, pealkiri, autor, hind, rating):
        self.p = pealkiri
        self.a = autor
        self.h = hind
        self.r = rating


class Raamatupood:
    def __init__(self, nimi, rating):
        self.n = nimi
        self.r = rating

    def saan_lisada_raamat(self, Raamat):
        saablisada = input("Lisa raamat: ")
        if Raamat.p == saablisada:
            print("Raamat on juba poes olemas nimega " + saablisada)
        else:
            print("Raamat lisati raamatupoodi!")


    def lisa_raamat(self, Raamat):
        print("Lisasid raamatu")

    def saan_eemaldada_raamat(self, Raamat):
        print("Saan eemaldada raamat")

    def eemalda_raamat(self, Raamat):
        del Raamat.p
        del Raamat.r
        del Raamat.a
        del Raamat.h
        print("Eemaldasid raamatu")

    def naita_koik_raamatud(self):
        print("Näita kõik raamatud")

    def naita_raamatud_hinna_jargi(self):
        print("Näita raamatud hinna järgi")

    def naita_koige_populaarsem_raamat(self):
        print("Kõige populaarsem raamat on " + str(self.n) + " " + str(self.r))