class Animal:
    def __init__(self, name="Rex", age=2):
        self.__name = name
        self.__age = age


dog_a = Animal()
dog_b = dog_a
print(my_dog_a.name)  # Return "Rex"
print(dog_b.name)  # Return "Rex"

dog_a.name = "Pongo"
print(my_dog_a.name)  # Return "Pongo"
print(dog_b.name)  # Return "Pongo"