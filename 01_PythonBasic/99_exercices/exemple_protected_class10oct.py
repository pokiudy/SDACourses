class Animal:
    def __init__(self, name="Rex", age=2):
        self._name = name
        self._age = age


my_dog = Animal()
print(my_dog._name)
print(my_dog._age)
# it works, will print value of name variable, from my_dog object


