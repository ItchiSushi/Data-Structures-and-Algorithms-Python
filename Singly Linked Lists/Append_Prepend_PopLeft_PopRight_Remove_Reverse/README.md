<h1>Append</h1>

<h2>Description</h2>

<p align="Justify">This subsection will focus on writing efficient code to append an array with Head and Tail nodes in a Singly Linked List.</p>

<p>Notes:</p>

 - The time complexity of the append function is O(1) because there is only one function being used continuously to append a new node to the list.
 - The Space complexity is O(1) because the function will always behave the same way regardless of the size of the list.

<h1>Prepend</h1>

<h2>Description</h2>

<p>This subsection will focus on the prepend function that will add a node to front of the head node in a list. This will make the new prepended node the head node of the list.</p>

<p>Notes:</p>

 - The Time Complexity of prepend is very similar to append as it is just moving to the previous node. So this is O(1)
 - The Space Complexity is the same because append because the only thing changing is the size of the list. So this is also O(1)

<h1>Pop Left</h1>

<h2>Description</h2>

<p align="Justify">In this subsection, we want to the remove the left most node from the list, and to do so, we need to understand that we cant just remove the head from the list. We have to assign the head to the next node and then disconnect previous node from the newly assigned head. Now the node can be removed from the list. </p>

<p>Notes</p>

 - The Time Complexity and Space Complexity is O(1)

<h1>Pop Right</h1>

<h2>Description</h2>

<p align="justify">This function focuses on removing an element to the right most side of the list. This Tail node is assigned to the previous node and the last node is disconnected and removed.</p>

- Time complexity for this is O(n) because it uses a for loop to cycle through the entire list to find the node before the tail node. This is not beneficial for large lists
- The Space complexity is O(1) as memory is decreasing as elements are removed from the list.

<h1>Remove</h1>

<h2>Description</h2>

<p>This function allows the remove of a node in a list by assigning a head and tail. When we want to remove a target node, we need to look at its preceding/previous node and make that node point to the node that the target node is pointing to. Then set the target node to none so that it gets removed from the list.</p>

- Time complexity for this function is O(n)
- Space Complexity is O(1)