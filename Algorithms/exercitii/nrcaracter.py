'''
Se da string-ul:
string = "salutariSdaAcademy!"

Sa se numere si returneze numarul de caractere!
Fara sa folositi len()
Sa se rezolva recursiv si iterativ
'''

string = "salutariSdaAcademy!"

def counter(string):
    numarator = 0
    while numarator < len(string):
        numarator += 1
    return numarator

print(counter(string))
print(len(string))


string = "SalutariSdaAcademy"
def numarator_caractere(string):
    print("string nou dupa slice:", string)
    if string == "":
        return 0
    return 1 + numarator_caractere(string[1:])

print(numarator_caractere(string))