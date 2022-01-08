class Queue():
    def __init__(self):
        self.__queue = []

    # returneaza daca lista este goala sau nu
    def empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False

    # returneaza lungimea listei
    def size(self):
        return len(self.__queue)

    # adauga un element la coada
    def enqueue(self, item):
        self.__queue.append(item)

    # scoate primul element:
    def dequeue(self):
        pop = self.__queue[0]
        self.__queue = self.__queue[1:]
        return pop

    # returneaza elemtul din coada
    def rear(self):
        return self.__queue[-1]

    # returneaza primul element
    def front(self):
        return self.__queue[0]

    def print(self):
        print(self.__queue)

if __name__ == "__main__":
    q1 = Queue()
    print(q1.empty())
    q1.enqueue(2)
    q1.enqueue(5)
    q1.enqueue(7)
    q1.print()
    print(q1.dequeue())
    q1.print()
    print(q1.dequeue())
    q1.print()
    q1.enqueue(11)
    print(q1.rear())
    q1.print()
    print(q1.front())