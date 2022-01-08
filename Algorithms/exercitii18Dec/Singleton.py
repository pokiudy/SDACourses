'''
Singleton - se foloseste atunci cand se doreste BLOCAREA creeri mai multor instante
ale aceeleasi clasa. UNA si GATA!

Tradus ca:
    IF (clasa a fost folosita o data = None)
        creaza!
    ELSE (ignora restul)
        BYE, BYE(ignora restul)

'''
class Singleton:

    _am_fost_creata_o_data = None

    def __init__(self, name):
        print(f"Am facut o instanta pentru obiectul {name}")

    def __new__(cls, *args, **kwargs):
        if cls._am_fost_creata_o_data is None:
            print("Cream o instanta")
            cls._am_fost_creata_o_data = object.__new__(cls) #asa se creeaza clasele in spate
            return cls._am_fost_creata_o_data


# primul lucru, e sa se apeleze functia __new__
# in interiorul functiei se verifica daca varibila private "_am_fost_creata_o_data"
# are sa nu o valoare, daca nu are, si este None, inseamna ca suntem la prima creere
# creem instanta prin intermediul lui "object.__new__(cls)" si asignam valaorea lui
# la variabila "_am_fost_creata_o_data" pentru ca data viitoare sa nu mai fie goala.
# returnam variabila.

if __name__ == "__main__":
    s1 = Singleton("SDA Academy");
    s2 = Singleton("It School");
    s3 = Singleton("Politehnica");

    # vrem ca S2 sa returneze tot SDA Academy
    # vrem ca S3 sa retunreze tot SDA Academy