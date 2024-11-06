class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self._length += 1
        return self

my_list = SinglyLinkedList()
my_list.prepend(4)
my_list.prepend(7)
my_list.prepend(15)
my_list.prepend(13)
print(my_list)
print(my_list.head)
print(my_list.tail)
print(my_list._length)