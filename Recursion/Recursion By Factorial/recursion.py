def factorial(n):
    # Base case. Tells us when the recursion should stop. This is a must-have.
    if n== 0:
        return 1
    # Use the recursive case to recall the base case until the recursion stops.
    return n * factorial(n-1)
print(factorial(5))