
import time
import functools


def cronometru(func): # cronometru este un decorator care cronometreaza o functie oarecare denumita "func"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # "*args, *kwargs" - oricate argumente are functia si oricare ar fi acestea
        # do the magic here
        t1 = time.time() # iau timpul inainte de apelul functiei func
        y = func(*args, **kwargs)
        t2 = time.time() # iau timpul dupa apelul functiei func
        print(f"A durat {t2 - t1} secunde!") # diferenta de timp este cat dureaza functia
        return y
        # until here
    return wrapper


# functia f cu argumentul x
@cronometru
def f(x):
    y = None
    for i in range(10000000):
        y = x ** x
    return y


#functia g cu argumentele x si y
@cronometru
def g(x, y):
    z = None
    for i in range(10000000):
        z = x ** y + 2*x
    return z


if __name__ == "__main__":
    f(10)  # x=10
    g(10, 5)  # x=10, y=5
    #f(10)
    #t1 = time.time()
    #f(13)
    #t2 = time.time()
    #print(f"A durat {t2 - t1} secunde!")