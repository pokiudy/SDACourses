class Animal(object):  # Inheritence example: 'object'
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # getter - get variable value
    def age(self):
        return self.__age

    @age.setter  # setter - set variable new value
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter  # deleter - remove variable
    def age(self):
        del self.__age


my_dog = Animal("Max", 45)
# my_dog.age = 3  # Set age - using setter
print(my_dog.age)  # read age - using getter
del my_dog.age  # Remove variable - using deleter
