# define a function that will perform a quadratic time example.
def function(list_of_numbers):
    # Use a nested for loop to print each number. (Should be avoided)
    for numbers in list_of_numbers:

        for each in list_of_numbers:
            print(each)
# Create a list to store integers.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Call the function()
function(number_list)