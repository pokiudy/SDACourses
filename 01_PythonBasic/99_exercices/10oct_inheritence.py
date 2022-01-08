class Human:
    def __str__(self):
        return f"Name:{self.__name}, \n Height: {self.__height}, \n Weight: {self.__weight}"
    def __repr__(self):
        return str(self)

    def __init__(self, name, height, weight = 50):
        self.__name = name
        self.__height = height
        self.__weight = weight
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weigth = weight


class Programmer(Human):
    def __init__(self, name, height, weight, languages):
        super().__init__(name, height, weight)
        self.languages = languages
    def __str__(self):
        return f"Name:{self.name}, \n Height: {self.height}, \n Weight: {self.weight}, \n Languages: {self.languages} "

om = Human('Lisia', 164, 46)
programator = Programmer('Lavinia', 162, 45, ["Python", 'C++', 'Java'])
print(programator.name)
print(om.name, om.weight, om.height)
print(om)

oameni = [om, programator]
print(oameni)
print(programator)
# Access to the inherited Human class name attribute