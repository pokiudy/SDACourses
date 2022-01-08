
result = None


try:
    # incearca sa citeasca 2 numere si sa le imparta
    a = int(input("a="))
    b = int(input("b="))
    result = a/b
except ZeroDivisionError: # ZeroDivisionError este eroare predefinita in Python
    # aici intra cand b = 0
    print("b este 0 si nu putem imparti!")
except ValueError: #ValueError este predefinita in Python
    # aici intra cand a sau b nu se pot converti la int
    print("Unul din numere (a sau b) nu poate fi convertit la int!")
except:
    # aici intra cand apare orice alta eroare in afara de ZeroDivisionError si ValueError
    print("O eroare necunoscuta(diferita de ZeroDivisionError si ValueError) a fost aruncata!")


print(f"impartirea = {result}")

print("Programul continua cu alte instructiuni....")
# .....