# Time Complexity: O(1)
my_list = [10,15,20]
my_list.append(25)
print(my_list)
# Everything in the list shifts up to add a new element at the given index
# Complexity: O(n)
my_list.insert(0,5)
print(my_list)
# Removes the element at given index
# Complexity: O(n)
my_list.pop(2)
my_list.insert(2, 50)
print(my_list)
# Print specific element at given index
# Complexity: O(1)
print(my_list[3])
