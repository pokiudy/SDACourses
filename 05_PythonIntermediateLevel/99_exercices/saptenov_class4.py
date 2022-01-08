
from datetime import datetime


def run_between_hours(start_hour, stop_hour):
    def dec(func): # decoratorul va primi o functie oarecare, denumita generic "func"
        # pentru functia func, definim un wrapper cu ce se va intampla
        def wrapper():
            t = datetime.now()
            if t.hour >= start_hour and t.hour <=stop_hour:
                func()
            else:
                print(f"Functia nu poate fi apelata decat in intervalul orar: {start_hour} - {stop_hour}")
        return wrapper
    return dec


@run_between_hours(8, 10)
def hello():
    print("Hello World!")


@run_between_hours(15, 20)
def hello_special():
    print("This is a special hello!")


if __name__ == "__main__":
    hello()
    hello_special()