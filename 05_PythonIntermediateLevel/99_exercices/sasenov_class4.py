from abc import abstractmethod
from abc import ABC

class Fruct(ABC):
    def __init__(self, nume, tip, culoare ):
        self.nume = nume
        self.tip = tip
        self.culoare = culoare

    def __str__(self):
        return f"{self.nume} este un fruct tip {self.tip} de culoare {self.culoare}, delicios!"

    @abstractmethod
    def val_nutritive(self):
        pass

class Banan(Fruct):
    temperatura_oxidare = 10

    def __init__(self, nume, tip, culoare, continut_zahar):
        super().__init__(nume, tip, culoare)
        self.continut_zahar = continut_zahar

    def iradiatii(self):
        return f"Nivelul de radiatie este: {self.continut_zahar * 3}"

    def val_nutritive(self):
        print(f"Valorile nutritive la {self.nume} sunt foarte bune.")
    @staticmethod
    def origine():
        print("Bananele sunt din import")

    @classmethod
    def oxidare(cls):
        return f"Banana s-a innegrit la {cls.temperatura_oxidare} grade"


class Mar(Fruct):
    def __init__(self, nume, tip, culoare, masa):
        super().__init__(nume, tip, culoare)
        self.masa = masa

    def energie_cinetica(self, viteza):
        return f"The boys are messing around with this number: {self.masa * viteza *viteza / 2} mJ, thanks Newton!"

    def val_nutritive(self):
        print("Merele de Baia Mare au valori nutritive mari")

a = Mar("Marul", "Ionatan", "rosie", 75)
print(a)
print(a.energie_cinetica(2))

print("+++++++++++++++++++++++++++++++++++++")
b = Banan("Banana", "Dole", "galben", 12.23 )

print(b)
print(b.iradiatii())

print("+++++++++++++++++++++++++++++++++++++")

Banan.origine()
Banan.oxidare()
print(Banan.oxidare())

print("+++++++++++++++++++++++++++++++++++++")

b.val_nutritive()
a.val_nutritive()
