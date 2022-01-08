'''
Anagrame:

- sunt cuvinte ca prin rearanjarea literelor lor rezulta cuvinte noi (citibil)
s1 = "fairy tales"
s2 = "rail safety"

Ex: se se creeze o functie ce primeste ca parametrii cele doua string-uri, s1 - s2 si
sa se verifice daca sunt sau nu anagrame.
'''

s1 = "fairy tales"
s2 = "rail safety"
def doua_stringuri(string1,string2):
    string1 = string1.lower()                       #functia .lower le face litere mici
    string2 = string2.lower()
    string1 =string1.replace(" ",'')                #tai spatiul dintre ele
    string2 = string2.replace(" ", '')
    if len(string1)!=len(string2):                  #verific daca lungimea lor
        return "Nu exista"

    if sorted(string1) == sorted(string2) :         #verific daca cele 2 variabile sortate sunt anagrame
        return "Sunt anagrame "
    else:                                           #daca nu sunt anagrame intra pe cazul else
        return "Nu sunt anagrame"

s1 = "fairy tales"
s2 = "rail safety"
print (doua_stringuri(s1,s2))