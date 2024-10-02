# Create a function that will parse a list to be used in the function.
def function(list_of_numbers):
    # Create a for loop that will loop for the amount of items inside the list
    for i in range(len(list_of_numbers)):
        # Create value variable and multiply the index inside the list by 2.
        value = list_of_numbers[i] * 2
        # Display the value.
        print(str(value))
# Create a list to store integers.
numbers = [5, 6]
# Call the function
function(numbers)