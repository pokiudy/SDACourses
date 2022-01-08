class Person:

    obj_list=[]
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.obj_list.append(self)


    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

if __name__=="__main__":
    os1=Person("john",54)
    os2=Employee("jack",36,20,30)
    for x in Employee.obj_list:
        print(x)

    print(Employee.obj_list)