from sasenov_class import Animal


# clasa Mammal mosteneste clasa Animal
class Mammal(Animal):

    def __init__(self, name, age, color, weight):
        super().__init__(name, age, color)
        self.weight = weight

    def run(self):
        print(f"Mammal named {self.name} is running! Its weight is {self.weight} kg!")

    def eat(self, treat):
        #print(f"< Mammal {self.name} eats treat {treat} and weighs {self.weight}! >")
        super().eat(treat)
        print(f"This animal is a mammal and weighs {self.weight} kg!")

    def move(self):
        super().move()
        self.position += 2


if __name__ == "__main__":

    m = Mammal("Leo", 4, "yellow", 150)
    m.run()

    print("\n=====================\n")

    m.eat("meat")

    print("\n=====================\n")

    m.move()
    print(f"Position after first move is: {m.position}")

    m.move()
    print(f"Position after second move is: {m.position}")


print(isinstance(m, Mammal)) # este m de tip Mammal? DA, pt ca m este instantiat ca Mammal
print(isinstance(m, Animal)) # este m de tip Animal? Da, pt ca Mammal mosteneste Animal

print(issubclass(Mammal, Animal)) # este Mammal o subclasa a lui Animal? DA, pt ca Mammal mosteneste Animal