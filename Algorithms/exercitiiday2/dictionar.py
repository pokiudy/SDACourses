
s1="fairy tales"
s2="rail safety"
import pprint
def verific_anagrame(s1,s2):
    dictionar_anagrame={

    }
    for char in s1:
        if char not in dictionar_anagrame:
            dictionar_anagrame[char] = 1
        else:
            dictionar_anagrame[char] += 1

    for char in s2:
        if char not in dictionar_anagrame:
            dictionar_anagrame[char] = 1
        else:
            dictionar_anagrame[char] -= 1



    for key in dictionar_anagrame:
        if dictionar_anagrame[key] != 0:
            return False
    return True


print(verific_anagrame(s1,s2))