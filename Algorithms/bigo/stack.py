class Stack():
    def __init__(self):
        self.__stack = []

    # functia ce adauga un element la inceputul listei
    def push(self, item):
        self.__stack.insert(0, item)

    # functie de returneaza (scoate complet) primul element din lista
    def pop(self):
        if self.empty() == True:
            return None
        else:
            pop = self.__stack[0]
            self.__stack = self.__stack[1:]
            return pop


    # returneaza daca lista este goala sau nu
    def empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False


    # returneaza lungimea listei
    def size(self):
        return len(self.__stack)

    # returneaza primul element din lista
    def top(self):
        if self.empty() == True:
            return None
        else:
            return self.__stack[0]



    def print(self):
        print(self.__stack)


if __name__ == "__main__":
    S1 = Stack()
    print(S1.empty())
    S1.push(4)
    S1.push(6)
    S1.push(9)
    S1.push(7)
    print(S1.size())
    S1.print()
    print(S1.pop())
    S1.print()
    print(S1.top())
    S1.print()
