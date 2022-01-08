# +---+---------------+
# | 8 | 0x0007 (node) |
# +---+---------------+
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.__head = None

    #insereaza un element la inceput
    def insert_at_begining(self, data):
        new_head = Node(data, self.__head)
        self.__head = new_head

    #printarea listei
    def print(self):
        iterator = self.__head
        buffer = ""
        while iterator is not None:
            buffer += str(iterator.data) + "-->"
            if isinstance(iterator.next, Node):
                iterator = iterator.next
            else:
                iterator = None

        print(buffer)


# 67 -> 255 -> 99
if __name__ == "__main__":

    ll = LinkedList()
    ll.insert_at_begining(67)
    ll.insert_at_begining(68)
    ll.insert_at_begining(69)
    ll.print()