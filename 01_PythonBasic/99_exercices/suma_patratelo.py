# Sa se scrie o functie care sa calculeze suma patratelor numerelor date

def add_squares(*args):
    print(args)
    result = 0
    for arg in args:
        result = result + arg ** 2
    return result



print(add_squares(1, 2, 3))
print(add_squares(1, 2, 3, 4, 5, 6))


