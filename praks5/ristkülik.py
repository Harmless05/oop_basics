class Ristkulik:
    def __init__(self, l, k, s):
        self.laius = l
        self.korgus = k
        self. symbol = s

    def __str__(self):
        ruutu_read = []
        for rea_number in range(self.korgus):
            rida = self.symbol * self.laius
            ruutu_read.append(rida)
        ruutu_read = "\n". join(ruutu_read)
        return ruutu_read

    def __add__(self, teine_ristkulik):
        self.laius = self.laius + teine_ristkulik.laius
        self.korgus = self.korgus + teine_ristkulik.korgus
        if symbol_valik == 1:
            self.symbol = self.symbol
        else:
            self.symbol = teine_ristkulik.symbol
        return self
    print()