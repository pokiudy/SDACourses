import math
import os
import pickle


# writing to a file
# example_dict = {1: "6", 2: "2", 3: "f"}
# file_out = open("dict.pickle", "wb")
# pickle.dump(example_dict, file_out)
# file_out.close()
#
# # reading from a file
# file_in = open("dict.pickle", "rb")
# example_dict = pickle.load(file_in)
# file_in.close()
#
# # writing to a file using a context manager (to be studied at Python Intermediate)
# example_dict = {1: "6", 2: "2", 3: "f"}
# with open("dict.pickle", "wb") as file_out:
#     pickle.dump(example_dict, file_out)
#
# # reading from a file using a context manager (to be studied at Python Intermediate)
# with open("dict.pickle", "rb") as file_in:
#     example_dict = pickle.load(file_in)


def is_prime(num):
    for x in range(2, int(math.sqrt(num) + 1)):
        if num % x == 0:
            return False
    return True


def generez_primele_100_nr_prime(lista_nr_prime, initial_number):
    nr = initial_number
    pas = 0
    while pas < 100:
        if (is_prime(nr)):
            lista_nr_prime: list = lista_nr_prime
            lista_nr_prime.append(nr)
            pas += 1
        nr += 1

    return lista_nr_prime

if os.path.isfile('numere.pickle'):
    with open("numere.pickle", "rb") as file_in:  ##Citirea din fisier
        lista_nr_prime = pickle.load(file_in)
        print(lista_nr_prime)
else:
    lista_nr_prime = []
# Verificarea fisierului si generarea de numere prime
if len(lista_nr_prime) == 0 :
    lista_nr_prime = generez_primele_100_nr_prime(lista_nr_prime, 2)
else:
    lista_nr_prime = generez_primele_100_nr_prime(lista_nr_prime, lista_nr_prime[-1])

# Scrierea "dump-ul" in fisierul nostru
with open("numere.pickle", "wb") as file_out:
    pickle.dump(lista_nr_prime, file_out)