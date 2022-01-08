a = 26

b = 26.0

c = "I am learning"

d = True

person_age = 25

D = a - b
print(D)

print(a * b)

print(person_age / b)

print(b ** a)

print(person_age)
print(type(person_age))

print(int(4.3))

print(int("45"))

print("Hello, Klaudia!")

e = 4.5
f = 5.6

P = e * f
print(P)

L = 2 * e + 2 * b
print(L)

r = 34

pi = 3.14
P2 = pi * int(r ^ 2)
print(P2)

L2 = 2 * pi * r
print(L2)

# Conditions

variable = 38
if variable / 7:
    print(True)


# Write a program that checks if a given number is preceded by a prime number.

import math

def num_is_prime(nxt):
    before = nxt - 1

    if before == 2:
        return True
    if before % 2 == 0 or nxt <= 1:
        return False

    sqr = int(math.sqrt(before)) + 1

    for divisor in range(5, sqr, 2):
        if before % divisor == 0:
            return False
    return True
print(num_is_prime(25))

# Write a function (or program) that will calculate the zeros of the given square function. For this purpose, you can use the formulas presented here.

def find_roots(a, b, c):

    if a == 0:
        print("Input incorrect")
        return

    delta = b * b - 4 * a * c
    sqrt_delta = math.sqrt(abs(delta))

    if delta > 0:
        print("two solutions")
        print(f'x_1 = {(-b + sqrt_delta) / (2 * a)}')
        print(f'x_2 = {(-b - sqrt_delta) / (2 * a)}')

    elif delta == 0:
        print("one solution")
        print(-b / (2 * a))

    elif delta < 0:
        print("no solution")

find_roots(1, -2, 1)





















