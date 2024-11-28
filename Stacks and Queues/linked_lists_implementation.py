class Node:
    def __init__(self, value):
        self.head = value
        self.Next = None

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
        self._max_allowed_size = 10

    def __len__(self):
        return self._size

    def push(self, value):
        if self._max_allowed_size == self._size:
            raise Exception("stack size limit exceeded")
        new_element = Node(value)
        new_element.next = self._top
        self._top = new_element
        self._size += 1
        return self

    def pop(self):
        if not self._size:
            raise Exception("stack is empty")
        former_top = self._top
        self._top = former_top.next
        former_top.next = None
        self._size -= 1
        return former_top.value

    def peek(self):
        return self._top.value if self._top else None

    def clear(self):
        self._top = None
        self._size = 0
        return self

my_stack = Stack()

my_stack.push('google')
print(my_stack.peek())
print(len(my_stack))