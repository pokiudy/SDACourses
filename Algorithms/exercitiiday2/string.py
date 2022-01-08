string1 = "salutariSdaAcademy"
string2 = "SalutariSdaAcademy"
string3 = "salutarisdaacademy"

def upper_case(text):                   #subprogramul
    for x in range(len(text)):          #se ia literara cu litera din cuvantul nostru
        if str(text[x]).isupper():      #verificam daca este litera mare
            return f"Litera {text[x]} a fost gasita in pozitia {x}"     #Daca gasim o litera mare atunci spunem care este si pe ce pozitie se afla
    return "Nu a fost gasita nicio litera"      #Daca nu se gaseste ,iese din for si returneaza acest mesaj

print(upper_case(string1))
print(upper_case(string2))
print(upper_case(string3))



#recursiv




def first_upper_recursive(string,index):
    if index<len(string):
        if string[index].isupper():
            print(f"I have found the first upper character at the index postion {index} and the uppercharacter is {string[index]} ")
            return string[index]
        else:
            return first_upper_recursive(string,index+1)
    else:
        print("We didn't find any uppercase character in the given string")
        return 0



def first_upper_recursive(string,index):
    #verificam daca s-a ajuns la capatul stringului sau nu
    if index<len(string): #daca inca nu s-a ajuns la capatul stringului

        #verificam daca litera parcursa, rand pe rand, de la indexul 0 este un caracater mare
        if string[index].isupper():#verifica daca pe pozitia pe care is , exista o litera mare

            #afisam pe ecran acest mesaj
            print(f"I have found the first upper character at the index postion {index} and the uppercharacter is {string[index]} ")

            #dar si returnam litera mare
            return string[index]

            #altfel, daca litera parcursa, cea de la indexul curent, la care nu suntem acum, nu este mare, reapelam functia dar de la o pozitie de indice cu +1
        else:
            #echivalent ca si cum as trece la urmatoarea iteratie din for  ex: in loc sa fac for x in range(len(sir))-----> in loc de x , pasul de iteratie, o sa fie functia mea recursiva in sine
            #care se tot reapeleaza ----> f(string,0)-f(string,1)-f(string,2).....f(string,ultimulindex)
            return first_upper_recursive(string,index+1)#aici ma duc cu un indice in dreapta #aici se reapeleaza dar se itereaza prin tot sirul
    else:

        #daca totusi am parcurs tot sirul si nu s-au gasit litere mari, returnez 0 si afisez pe ecran mesajul urmator
        print("We didn't find any uppercase character in the given string")
        return 0


#principiul de functionare al functiei mele recursive:
#pas 1) este sa incepem parcurgerea sirului----> dar putem efectua acest pas, doar daca indexul curent (primul index=0) este obligatoriu < decat capatul sirului
#pas 2) for i in range(3) ----> 0, 1 , 2 :corect?! dar in recursivitate se intampla la fel deoarece pornesti functia pe indice 0 si se reapeleaza pana la indicele final, ca in for

STring_1="facprobe"
print(first_upper_recursive(STring_1,0))