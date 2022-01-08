# 230V
class PrizaEU:
    def __init__(self):
        pass

    def line(self):
        return 230

    def null(self):
        return 0
# Adaptor
# Altereaza functia line() dar returneaza aceasi functie null()


class Adaptor:
    def __init__(self, priza):
        self.priza = priza

    def line(self):
        return 110

    def null(self):
        return self.priza.null()
# De la varu' din America: 110V


class AparatDeCafea:
    def __init__(self, priza):
        self.priza = priza

    def fa_o_cafea(self):
        if self.priza.line() > 110:
            print("Am ars aparatul!")
        else:
            print("Cafeaua este servita!")


if __name__ == "__main__":

    prizaEU = PrizaEU()
    adaptor = Adaptor(prizaEU)
    aparatDeCafea = AparatDeCafea(adaptor)
    aparatDeCafea.fa_o_cafea()