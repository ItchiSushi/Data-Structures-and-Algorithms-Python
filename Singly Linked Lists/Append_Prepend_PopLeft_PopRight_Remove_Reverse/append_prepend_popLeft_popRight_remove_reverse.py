# Adding new elements at the end of the list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
    # append function
    # Time Complexity: O(1)
    # Space Complexity: O(1)
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
    # prepend function
    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1
        return self
    # pop_left function
    def pop_left(self):
        if not self._length:
            raise Exception("List is empty")
        else:
            former_head = self.head
            self.head = former_head.next
            former_head.next = None
        self._length -= 1
        if not self._length:
            self.tail = None
    # pop_right function
    def pop_right(self):
        if not self._length:
            raise Exception("list is empty")
        tail_value = self.tail.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self._length -= 1
        return tail_value
    # remove function
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
            previous_node.next = current_node.next
            current_node.next = None
            self._length -= 1
            return current_node.value