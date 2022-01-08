class Animal:

    def __init__(self, name, age, colour, breed):
        self.name = name  # default value for he variable name from the class Animal
        self.age = age
        self.colour = colour
        self.breed = breed

    def print_details(self):  # method, that displays the object state
        print(f"Name: {self.name}, age: {self.age}, colour: {self.colour}, breed: {self.breed}")


my_dog = Animal("Sherlock", 7, "light brown", "teckel")
my_dog.print_details()

