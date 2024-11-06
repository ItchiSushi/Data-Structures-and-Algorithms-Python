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

my_list = SinglyLinkedList()
my_list.append(3)
my_list.append(5)
my_list.append(10)
print(my_list)
print(my_list.head.value)
print(my_list.tail.value)
print(my_list._length)
