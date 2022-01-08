# # Safely open the file  ##Acest exercitiu mi-a creat fisierul hello.txt in folderul Recapiturare_Avi_Finkel
# file = open("hello.txt", "w")
#
# try:
#     file.write("Hello, World!")
#
# except Exception as x:
#     print("Error is", x)
#
# finally:
#     # Make sure to close the file after using it
#     file.close()

file = open("test.txt", "r")
for line in file.readlines():
    print(line, end="")  # Acest `end=""` elimina un `/n` si scoate spatiile dintre randuri. Gen in fisier noi am scris propozitie sub propozitie.
                         # Scriind atfel, e ca si cu am pus deja `/n`, chiar daca nu l-am pus fizic, el se pune automat cand tastam `enter`.
                         # Programul va pune si el automat un `/n`. Deci, daca eu am pus unul cand am dat `enter` si programul pune si el unul, rezulta ca am doua `/n`.
                         # Cand printez, el va scrie unul sub altul plus un spatiu aditional. Deci ca sa scot spatiul aditional, voi pune `end=""`.
file.close()