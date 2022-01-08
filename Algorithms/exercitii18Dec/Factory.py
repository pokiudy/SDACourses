'''
Factory - O clasa ce creeaza alte clase in functie de o conditie data
Important, clasele ce sunt folosite in Factory sa aibe cel putin o metoda comuna
Clasa Factory, are o singura metoda numita la alegere (build) si trebuie
obligatoriu sa aibe decoratorul @staticmethod
'''

class Student:
    def __init__(self, name):
        self.name = name

    def common_method(self):
        print(f"Buna sunt {self.name} si sunt student")


class Teacher:
    def __init__(self, name):
        self.name = name

    def common_method(self):
        print(f"Buna sunt {self.name} si sunt profesor")

class Factory:
    @staticmethod
    def build(tip_de_clasa, name):
        if tip_de_clasa == "Student":
            return Student(name)
        elif tip_de_clasa == "Teacher":
            return Teacher(name)
        else:
            return "Tipul selectat este invalid"


if __name__ == "__main__":

    angajat = Factory.build("Teacher", "Florin")
    # va fi echivalentul lui angajat = Student()
    angajat.common_method()