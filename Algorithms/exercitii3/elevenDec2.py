str_1 = "abcdef"
str_2 = "abcdefa"

def is_Unique(text):
    list = []
    for char in text:
        if char not in list:
            list.append(char)
        else:
            return False
    return True



    print(list)

print(is_Unique(str_2))
print(is_Unique(str_1))




"""
is_Unique

unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

- Faceti o functie ce verificata daca un caracter a aparut de mai multe
ori in string-ul dat.
- La prima aparitie dubla functia va returna False, altfel va returna True
"""

# primul = input("Care este primul sir de caracter?")
# al_doilea = input("Care este al doilea sir de caracter")
unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

def string(sir_de_caractere,i=0,j=1):       #i este pozitia de inceput ,j este a doua pozitie

    while(i<len(sir_de_caractere)):         #cat timp i este mai mic decat lungime sirului
        if j==len(sir_de_caractere):        #daca j ajunge sa fie egal cu lungimea sirului
            return string(sir_de_caractere,i+1,i+2)     #ATUNCI crestem i-ul si j-ul
        if sir_de_caractere[i] != sir_de_caractere[j]:  #daca caracterul de pe pozitia i este diferita fata de cea de pe j
            return string(sir_de_caractere,i,j+1)       #atunci crestem j-ul
        else :
            return False                                #altfel returnez fals
    return True                                         #in caz ca nu intra pe cazul de fals atunci returneaza true

print(string(unique_str))
print((string(non_unique_str)))