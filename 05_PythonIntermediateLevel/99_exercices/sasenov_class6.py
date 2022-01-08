from abc import abstractmethod, ABC
from math import pi


class FiguraGeometrica(ABC):

    @abstractmethod
    def perimetru(self):
        pass

    @abstractmethod
    def arie(self):
        pass


class Patrat(FiguraGeometrica):

    def __init__(self, lat):
        self.lat = lat

    def perimetru(self):
        return 4 * self.lat

    def arie(self):
        return self.lat ** 2


class Cerc(FiguraGeometrica):
    def __init__(self, raza):
        self.raza = raza

    def perimetru(self):
        return 2 * pi * self.raza

    def arie(self):
        return pi * self.raza * self.raza

if __name__ == "__main__":

    #f = FiguraGeometrica()
    #print(f.perimetru())

    p = Patrat(2)
    print(f"Aria patratului: {p.arie()}")

    c = Cerc(5)
    print(f"Aria cercului: {c.arie()}")
    print(f"Perimetrul cercului: {c.perimetru()}")