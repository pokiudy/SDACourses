from datetime import datetime


def disable_at_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper


@disable_at_night
def say_something():
    print("Hello!!")


say_something()