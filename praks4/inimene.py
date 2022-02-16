class Inimene():
    jk = 0

    def __init__(self):
        self.id = Inimene.jk + 1
        Inimene.jk += 1

    def info(self):
        print("Inimese id = " + str(self.id))
        print()