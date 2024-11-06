class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def popLeft(self):
        if not self._length:
            raise Exception("List is empty")
        else:
            former_head = self.head
            self.head = former_head.next
            former_head.next = None
        self._length -= 1
        if not self._length:
            self.tail = None

my_list = SinglyLinkedList()

