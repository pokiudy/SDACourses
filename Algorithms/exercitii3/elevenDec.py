"""
is_Unique

unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

- Faceti o functie ce verificata daca un caracter a aparut de mai multe
ori in string-ul dat.
- La prima aparitie dubla functia va returna False, altfel va returna True
"""

unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

def string(sir_de_caractere):

    for i in range(len(sir_de_caractere)):

          for j in range(i+1, len(sir_de_caractere)):
            if sir_de_caractere[i] == sir_de_caractere[j]:
                return False

    return True

print(string(unique_str))
print(string(non_unique_str))



def is_unique(chars):
    lista = []  # initializam o lista goala
    for i in chars:     # iteram prin fiecare caracter din sirul dat
        if i not in lista:      # verificam daca al nostru caracter este in lista (prima aparitie nu ar trebui sa fie)
            lista.append(i)     # daca nu este in lista, il adaugam, ca atunci cand il mai gaseste o data, sa se opreasca
        else:
            return False     # daca i este in sirul dat, returneaza false

    return True     # daca toate caracterele sunt unice, returneaza True


if __name__ == "__main__":
    unique_str = "AbCDefG"
    non_unique_str = "non Unique STR"

    print(is_unique(unique_str))
    print(is_unique(non_unique_str))