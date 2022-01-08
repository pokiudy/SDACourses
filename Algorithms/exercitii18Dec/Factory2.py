"""
sa se modifice ex anterior a.i. tipul de clasa (Student) sau (Teacher) sa se citeasca de la tastatura prin intermediul
f-tiei input.

"""
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
            print("Tipul selectat este invalid")



if __name__ == "__main__":
    tip = input("give class type: ")
    nume = input("give instance name: ")

    angajat = Factory.build(tip, nume)
    #va fii echivalentul lui angajat = Sudent()

    angajat.common_method()