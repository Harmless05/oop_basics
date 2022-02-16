class Konto:
    def __init__(self, nimi, saldo):
        self.s = saldo
        self.n = nimi

    def ylekanne(self, kogus):
        self.s = int(self.s) - kogus

    def deposiit(self, kogus):
        self.s = int(self.s) + kogus

    def naita_saldo(self):
        return str(self.n) + ", sul on kontol " + str(self.s) + " eurot"

    def naita_nimi(self):
        print("Sinu konto nimi on " + str(self.n))
