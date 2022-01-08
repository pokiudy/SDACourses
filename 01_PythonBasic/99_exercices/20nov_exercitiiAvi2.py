import json


# json este un obiect serializat

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


vehicle = Vehicle('Toyota', '2.5L', 32000)
print(vehicle.__dict__)
# json.dumps(vehicle.__dict__)  # json.dumbs a primit ca parametru dict ob vehicle
# print(json.dumps(vehicle.__dict__))   # am afisat ce a returnat json.dumbs(vehicle.__dict__ ramane intact)
x = json.dumps(vehicle.__dict__)  #serializare - python object -> json
#in x am salvat ce am primit de mai sus, adica obiectul de tip json

with open('data.json', 'w') as f:
    data = f.write(x)  #am aruncat obiectul json intr-un fisier data.json

with open('data.json', 'r') as f:
    data = f.read()   #am citit fisierul json
# print(type(data), data)
y = json.loads(data)  #operatia opusa serializarii json -> python object
#am descarcat fisierul json intr-un obiect de tip dictionar
print(y['name'], y['engine'], y['price'])
for k,v in y.items():
    print(f'{k}: {v}')