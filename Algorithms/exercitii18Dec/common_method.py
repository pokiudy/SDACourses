'''
Dat fiind JSON-ul. Sa se parseze si sa se extraga din el proprietatile
FIRST_NAME si GENEDER.

Sa se creeze doua clase MALE si FEMALE care sa aibe o metoda comuna
(Exact ca la exercitiul anterior)

Veti intera prin toate cele 5 dictionare din JSON
pentru fiecare iterare, FIRST_NAME extras din JSON va reprezenta numele
pe care il vom pasa metodei Factory.build(_, nume). Iar Gender
var reprezenta tipul clasei ex: Factory.build("Male", "Pentru").

Sa se modifice metoda build pentru putea face selectia dintre Male si Female.

ex de PSEUDOCOD:

primul dictionar din JSON:

for i in JSON
    {
        "id": 1,
        "first_name": "Jenn",
        "last_name": "Wince",
        "gender": "Female",
        "email": "jwince0@mediafire.com",
        "job_title": "Recruiting Manager"
    },

    instanta = Factory.build("Female", "Jenn")
    instanta.common_method

'''
import json


class Female:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"I am a woman and my name is: {self.name}")


class Male:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"I am a man and my name is: {self.name}")


class Factory:
    @staticmethod
    def build(class_type, name):
        if class_type == "Female":
            return Female(name)
        elif class_type == "Male":
            return Male(name)
        else:
            print("The selected type is not valid")


if __name__ == "__main__":
    data = []

    with open('example.json') as json_file:
        data = json.load(json_file)

    for dict in data:
        gender = dict["gender"]
        name = dict["first_name"]
        instanta = Factory.build(gender, name)
        instanta.print_name()














