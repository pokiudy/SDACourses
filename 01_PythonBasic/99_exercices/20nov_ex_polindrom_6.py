# o metoda care verifica daca un string este palindrom (se citeste la fel: 131 - 131)
# aba = True
# abcba = True
# abc = False
# list_1 = ['a', 'b', 'c']
# len(list_1) ----> 3
# list_1[0] ----> a
#list_1[2] ----> c

def is_palindrom(x):
    list_of_chr = []
    invers_list = []
    for chr in x:
        list_of_chr.append(chr)
            # print(len(list_of_chr))

    print("==================")

    for i in range(len(list_of_chr)-1, -1, -1):
        # print(i)
        # print(list_of_chr[i])
        invers_list.append(list_of_chr[i])
    # if list_of_chr == invers_list:
    #     return True
    # else:
    #     return False

    return True if list_of_chr == invers_list else False  #varianta scurta a liniilor 23-26



print(is_palindrom('abc'))
print(is_palindrom('aba'))
print(is_palindrom('abcba'))

#alta varianta mai scurta a liniilor 10-34

def is_palindrom_short(x):
    return True if x == x[::-1] else False
print(is_palindrom_short('abcba'))
print(is_palindrom_short('aba'))
print(is_palindrom_short('abc'))