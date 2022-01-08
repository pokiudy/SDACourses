def print_hi(name):
    if True:
        print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Udy')

print("Hello, Klaudia!")

print('Hello, World!')

print("What a beautiful day")

print("What", "a" "beautiful", "day")

print(3)

print(3, 4, 5)

print("1", "2", 3, 4, 5)

print("What", "a" "beautiful", "day", sep=",")

# I am practicing coding

import this

a: int = 4
b = 6
print(a / b)

a = "This is getting interesting."
b = "Sometimes I'm lost, but..."
ex = a
a = b
b = ex
print(a, b)


def my_function():
    my_variable = "my safari crashed"
    print(my_variable)
    return my_variable


a = my_function()
print(a)


def my_f():
    var = "I don't really get it"
    return var


y = my_f()
print(y)

r1 = 3
r2 = 6
p1 = 10
p2 = 12


def circle_area_to_price(r, p):
    pi = 3.14
    area = pi * r * r
    return area / p


print(circle_area_to_price(r1, p1))
print(circle_area_to_price(r2, p2))

import requests

btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(btc.json())
print(btc.json()['bpi']['EUR']['description'])
print(btc.json()['bpi']['EUR']['rate'])




# Shallow, Deepcopy

b = [1, [22] ]
print(b[1])

list_shallow_copy = list(b)
print(list_shallow_copy)

b[1] = []
print(b)


list2 = ['a', 'b', 'c', 'd']

print(list2.pop())

print(list2)

print(list2.pop(2))


print(list2)



print(list)

list3 = ['r', 'm', 34, 3.4]

print(list3.pop())
print(list3)


# Shallow copy

name1 = [0, 5, 'euro' , 'dolari', 0.5]
nume2 = list(name1)

name1[0] = 'sambata'


print(name1)

print(nume2)


# Shallow copy nu merge cu liste in liste

import copy

name11 = [0, 5, 'euro' , 'dolari', 0.5, ['soare', 'copac']]
nume22 = list(name11)

name11[5][1] = 'zambet'


print(name11)

print(nume22)



# Deep copy

tabel = [1, 2, 'trei', 'patru', ['copac', 'frunza']]
tabel2 = copy.deepcopy(tabel)
tabel[4][1] = 'creanga'

print(tabel)
print(tabel2)


organigram = {
    "john": {
        "age": 35,
        "title": "CEO"
    },
    "Michael": {
        "age": 30,
        "title": "Director"
    }
}
print(organigram)


organigram["Adi"] = {
    "age": 32,
    "title": "senior engineer"
}

print(organigram)
print(organigram["Adi"])
print(organigram.keys())
x = list(organigram.items())
print(x[0])

print(organigram.values())

del organigram["Adi"]
print(organigram)

# exercitiu

one = {
    "dog": {
        "age": 7,
        "breed": "teckel"
    }
}



#print("Hello.")
#user_name = input("Please say your name: ")
#print(f"Hi, {user_name}!")

#user_age = input("How old are you?")
#print(f"I am, {user_age} old")
#next_year_age = int(user_age) + 1
#print(f"Next year I'll be: {next_year_age} ")

x = 0
y = 3

if x > y:
    print(f"{x} is greater than {y}")
if x < y:
    print(f"{x} is less than {y}")
elif x == 3:
    print(f"{x} is equal {y}")
else:
    print(f"{x} is less than {y}")

    print("This line will always be displayed again")



n = 3
while n < 9:
    n += 1
    print(n)

print("It's done!")

# Execute until n is lower than 5
n = 0
while n < 50:
    n += 1  # increment n in every next loop

    if n == 10:  # if n is equal 1, start new iteration
        print("n is 4")
        break
    if n == 1:  # if n is equal 4 break loop
        print("n is 1")

    print(n)

animals = ["Dog", "Cat", "Fish"]
i = 0  # i-ul ne da indexul
for x in animals:
    i = i + 1
    if i == 1:
        break
        print(i)


#1st
first_list = [3,34,5,6,78,56,55]
odd_list = [x for x in first_list if x % 2 != 0]
print(odd_list)

#2nd
animals = ['dog', 'cat', 'horse', 'cow']
print("Original list: ", animals)
animals = [x for col in animals for x in ('red', col)]
print("Changed list: ", animals)

#3rd
animals = [['dog'], ['cat'], ['horse'], ['cow']]
for a in animals:
    print(a)


#4th















