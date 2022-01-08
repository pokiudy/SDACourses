import math


def is_prime(num):
    for index in range(2, int(math.sqrt(num)) + 1):
        if num % index == 0:
            return False
        return True


def generez(n):
    contor = 0
    pas = 0
    while contor < n:
        if is_prime(pas):
            print(pas)
            contor += 1
        pas += 1


if __name__ == '__main__':
    n = int(input("Dati n: "))
    generez(n)

