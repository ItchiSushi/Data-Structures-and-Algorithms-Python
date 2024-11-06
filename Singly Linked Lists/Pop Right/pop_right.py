class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def popRight(self):
        if not self._length:
            raise Exception("list is empty")
        tail_value = self.tail.value
        if self._length == 1:
                self.head = self.tail = None
        else:
            temp_node = self.tail
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self._length -= 1
        return tail_value

