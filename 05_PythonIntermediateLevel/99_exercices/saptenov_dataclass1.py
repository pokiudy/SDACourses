# dataclass - este o metoda de a scrie mai simplu definirea unei clase


class Triunghi:
    def __init__(self, a:int, b:int, c:int):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"{self.a}, {self.b}, {self.c}"

    def __eq__(self, other):
        return isinstance(other, Triunghi) and (self.a, self.b, self.c) == (other.a, other.b, other.c)

    def perimetru(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    t = Triunghi(3, 4, 5)
    t2 = Triunghi(3, 4, 5)

    a = [t]


    print(a)
    print("=============================================")
    print(t)
    print("=============================================")
    print(t.__eq__(t2))
    print("=============================================")
    print(t == t2)
    print("=============================================")
    print(t.perimetru())
