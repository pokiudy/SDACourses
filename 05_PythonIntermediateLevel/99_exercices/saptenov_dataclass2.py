from dataclasses import dataclass

@dataclass
class Triunghi:
    a: int
    b: int
    c: int

    def perimetru(self):
        return self.a + self.b + self.c

if __name__ == "__main__":
    t = Triunghi(3, 4, 5)

    print(t)
    print(t.perimetru())


