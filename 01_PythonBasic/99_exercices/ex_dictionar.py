# 6. Scrieti o aplicatie command line care tine un dictionar de cuvinte engleza -> romana.
# Dictionarul este populat initial cu 3 traduceri: eye=ochi, nose=nas, ear=ureche
# a) Optiuni de implementat pentru utilizator: cautare traducere, adaugare traducere, iesire din program
# b) Implementati si schimbarea unei traduceri gresite, respectiv stergerea unei traduceri din dictionar


dictionary_en_ro = {'eye': 'ochi', 'nose': 'nas', 'ear': 'ureche'}

import sys


if len(sys.argv) > 1:
    print(sys.argv)
    language = sys.argv[1]
else:
    # print(f'Please select a language')
    language = input(f'Please select a language ')

if language == 'english':
    input_cmd_msg = "Please input a letter: "
    a_chosen_msg = "You chose: a"
else:
    input_cmd_msg = "Introduceti o comanda: "
    a_chosen_msg = "Ati ales: a"

command = input(input_cmd_msg)


while command != 'quit':
   if command == 'eye':
       word_eng = input("Introduce word in english: ")
       ro_translation = input("Introduceti traducere romana: ")
       dictionary_en_ro[word_eng] = ro_translation
   elif command == 'continue':
        word_eng = input("Introduce word in english: ")
        print(dictionary_en_ro.get(word_eng, '(no translation)'))