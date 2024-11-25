# Everything a node class will need
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# Everything a Doubly Linked List will need to get started on functionality
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
    #Append
    def append(self, value):
        # Create a new node variable along with the node instance that will contain the value.
        new_node = Node(value)
        # If statement to check if the list is empty of if the _length is 0
        if not self._length:
            # Assign the head and the tail of the list to the new node.
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        # Increment the list once the new node has been assigned.
        self._length += 1
        return self
    # Prepend
    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.previous = self.tail
            self.head = new_node
        self._length += 1
        return self
    # Pop Left
    def pop_left(self):
        if not self._length:
            raise Exception("List is empty")
        former_head = self.head
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = former_head.next
            former_head.next = None
        self.head.previous = None
        self._length -= 1
        return former_head.value
    # Pop Right
    def pop_right(self):
        if not self._length:
            raise Exception("List is empty")
        former_tail = self.tail
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = former_tail.previous
            former_tail.previous = None
            former_tail.next = None
        self._length -= 1
        return former_tail.value
    # Remove
    def remove(self,value):
        if not self._length:
            raise Exception("List is empty!")
        if self.head.value == value:
            return self.pop_left()
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise  ValueError("item not in list")
        if current_node.next is None:
            return self.pop_right()
        previous_node.next.previous = current_node
        previous_node.next = current_node.next
        current_node.next = None
        current_node.previous = None
        self._length -= 1
        return current_node.value
