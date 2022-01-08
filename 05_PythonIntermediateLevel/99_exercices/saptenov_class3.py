
from datetime import datetime


def disable_at_night(func):
    # func este un alias generic pentru orice functie pe care se va aplica decoratorul

    def wrapper(): # spun ce face "disable_at_night"
        t = datetime.now() # retinem cat este timpul acum
        if t.hour >= 8 and t.hour <= 9: # daca este pe timp de zi
            func()  # chem functia la care a fost utilizat decoratorul
        else:
            # altfel, dam un mesaj care sa ne spuna ca functia nu poate fi rulata
            print("It's night! Function cannot be run!")
    return wrapper


@disable_at_night
def hello():
    print("Hello World!")


if __name__ == "__main__":
    hello()