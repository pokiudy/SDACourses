"""
Sa se creeze o clasa de baza Loger ce va primi un mesaj
    ----\\----------      WithLevel ce va adauga in fata mesajului string-ul[info], sau [debug], sau[error]
                        WithTimestamp ce va aduga in fata mesajului momentul zilei de azitazi
"""

import time


class Loger:
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class WithLevel:
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "[info]: " + str(self.msg)


class WithTimestamp:
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(time.ctime()) + str(self.msg)


Bruna = Loger("Pătrunjel")

print(Bruna)

Coco = WithLevel(Bruna)
print(Coco)

Lucas = WithTimestamp(Coco)
print(Lucas)

Bruna2 = WithTimestamp(WithLevel(Loger("Telina")))
print(Bruna2)