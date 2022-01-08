"""
Diferenta dintre decorator si clase este faptul ca decoratorii au
functia __call__(self...etc)
"""

import time


class Withlevel:
    def __init__(self, func):
        self.func   = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return "[info]" + str(result)


class Withtimestamp:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return str(time.ctime()) + str(result)


class Upercase:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return str(result).upper()


@Withlevel
@Withtimestamp
@Upercase

#functia sa fie sub decoratori
def prepare_log(msg):
    return msg


if __name__ == "__main__":

    print(prepare_log("patrunjel"))