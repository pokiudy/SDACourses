
# 3 capabilitati: zbor, alergare, inot

# peste: inot
# caine: alergare, inot
# rata: zbor, alergare, inot
from abc import abstractmethod


class Zburator:
    @abstractmethod
    def zboara(self):
        pass


class Alergator:
    @abstractmethod
    def alearga(self):
        pass


class Inotator:
    @abstractmethod
    def inoata(self):
        pass


class Caine(Alergator, Inotator):

    def __init__(self, nume):
        self.nume = nume

    def alearga(self):
        print(f"Cainele {self.nume} alearga afara!")

    def inoata(self):
        print(f"Cainele {self.nume} cainele inoata in lac!")


class Rata(Alergator, Inotator, Zburator):

    def __init__(self, rasa):
        self.rasa = rasa

    def alearga(self):
        print(f"Rata de tip {self.rasa} alearga grabita!")

    def inoata(self):
        print(f"Rata de tip {self.rasa} inoata in balta!")

    def zboara(self):
        print(f"Rata de tip {self.rasa} zboara la 10 m inaltime!")


if __name__ == "__main__":
    c = Caine("Azorel")

    c.alearga()
    c.inoata()

    print("===================")
    r = Rata("abc")
    r.alearga()
    r.inoata()
    r.zboara()