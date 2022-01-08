class Students:
    def __init__(self):
        self.list_of_names = []  #Work from home: use set instead of list
        self.student_attributes = ("diligent", "tired", "lost", "curious")


    def add_student(self, name):
        self.list_of_names.append(name)

    def print_first_attribute(self):
        print(self.student_attributes[1])

    def get_unique_list_of_names(self):
        temporary_list = []
        for name in self.list_of_names:
            if name not in temporary_list:  #Nu este foarte optim sa folosim aceasta funtie cu liste
                temporary_list.append(name)

        return temporary_list


student_object = Students()  #self tine locul instantei

student_object.add_student("John")
student_object.add_student("Gabi")
student_object.add_student("Simina")
student_object.add_student("Simina")

student_object.print_first_attribute()

print(student_object.list_of_names)
print(student_object.get_unique_list_of_names())
