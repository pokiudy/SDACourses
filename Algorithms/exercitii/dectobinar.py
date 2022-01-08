"""3. Exercitiu

Sa se faca un fisier nou numti convertor ce va contine doua functii:
1. dec2bin si va primii un numar in baza 10 pe care il va converti in binar:
def dec2bin(dec):
    return bin
2. bin2dec si va primii un numar in baza 2 pe care il va converti in decimal
def bin2dec(bin):
    return dec """

'''
121 / 2 = 60 rest 0.5 ----> 1
60 / 2 = 30 rest ---------> 0
30 / 2 = 15 rest ---------> 0
15 / 2 = 7 rest 0.5 ------> 1
7 / 2 = 3 rest 0.5 -------> 1
3 / 2 = 1 rest 0.5 -------> 1
1 / 2 = 0 rest 0.5 -------> 1
'''

def dec2bin(num):
    # facem o lsita goala in care bagam rand pe rand resturile impartitilor la 2
    lista = []
    while num > 0:
        # cat timp numarul este mai mare sau egal cu 1, il prelucram

        # bagam aici in lsita restul impartirii numarului initial la 2
        rest = num % 2
        print(f"Restul impartirii lui: {num} % 2 este: -------> {rest}")
        lista.append(rest)
        # apoi aici impartim numarul la 2, pt ca atunci cand convertim in baza 2, trebuie sa tot impartim la 2
        num = num // 2
        print(f"Rezultatul impartirii: {num}")

        # apoi afisam lista invers
    print(lista[::-1])


print(dec2bin(121))

