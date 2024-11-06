# Everything a node class will need
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# Everything a Singly Linked List will need to get started on functionality
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0