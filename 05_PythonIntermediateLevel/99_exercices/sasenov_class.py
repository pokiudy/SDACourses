import time

class Animal:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.position = 0

    def eat(self, treat):
        print(f"Animal {self.name} eats treat {treat} !")

    # o metoda statica nu depinde de o anumita
    # instanta in nici un fel (deci nu punem argumentul "self")
    @staticmethod
    def present():
        print("Aceasta este o metoda statica dintr-o clasa care reprezinta un animal!")

    def move(self):
        self.position += 1


if __name__ == "__main__":
    a = Animal("Zoro", 5, "yellow")

    a.eat("fruit")

    treats_list = ["mango", "milka", "carrot", "mancare la plic", "taintei de Baia Mare"]

    i = 0
    while i < len(treats_list):
        a.eat(treats_list[i])
        i += 1
        time.sleep(1)

    print("Zoro is finished eating his treats")

