import time

start_time = time.time()

def f(x):
    for i in range(100000):
        y = x**x
    return y

if __name__=="__main__":
    print(f(5))
    end_time = time.time()-start_time
    print(f"Durata de executie a programului este {end_time}")