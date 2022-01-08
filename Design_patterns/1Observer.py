"""
1. clasa ce observa
2. clasa observata

- Un mod de lucru ce aduna functiile in interior si le cheama pe toate deodata.
-Cine aduna functiile? Observator!
- In ce e aduna? Intr-o lista.

1. -Observer de baza => cand folosim functii ce nu au un "return".
2. -Observer complex => cand folosim functii ce au un "return".
"""

# 1. clasa ce observa
# - Cine aduna functiile? Observator!
# - In ce le aduna? Intr-o lista.


class Observator:
    def __init__(self):
        self.observati = []
    # functia ce adauga functii intr-o lsita


    def inregistreaza(self, functie):
        self.observati.append(functie)

    # functia ce intereaza prin lista si cheama fiecare functie pe rand
    def apeleaza_tot(self):
        for fn in self.observati:
            fn()


# 2. clasa observata
class CelObservat:
    def __init__(self):
        pass

    def adunare(self):
        print(5 + 5)

    def scadere(self):
        print(5 - 5)


if __name__ == "__main__":

    observator = Observator()
    celObservat = CelObservat()

    observator.inregistreaza(celObservat.adunare) # nu se adauga parantezele functiei!
    observator.inregistreaza(celObservat.adunare) # nu se adauga parantezele functiei!
    observator.inregistreaza(celObservat.adunare) # nu se adauga parantezele functiei!
    observator.inregistreaza(celObservat.scadere) # nu se adauga parantezele functiei!
    observator.inregistreaza(celObservat.scadere) # nu se adauga parantezele functiei!
    observator.inregistreaza(celObservat.scadere) # nu se adauga parantezele functiei!
    observator.apeleaza_tot()







