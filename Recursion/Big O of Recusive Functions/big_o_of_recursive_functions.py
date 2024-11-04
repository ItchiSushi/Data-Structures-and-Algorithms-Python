# Time: O(n)
# Space: O(n)
def a(n):
    if n <= 1:
        return
    a(n - 1)

print(a(6))
# Time: O(n/2) -> O(n)
# Space: O(n/2) -> O(n)
def b(n):
    if n <= 1:
        return
    b(n - 2)

print(b(2))
# Time: O(logn)
# Space: O(logn)
def c(n):
    if n <= 1:
        return
    c(n / 2)

print(c(6))
# Time: O(2^n)
# Space: O(n)
def d(n):
    if n <= 1:
        return
    d(n - 1)
    d(n - 1)

print(d(6))
# Time: O(n^2) -> O(n)
# Space: O(n)
def f(n):
    if n <= 1:
        return
    for _ in range(n):
        f(n - 1)

items = [1,2,3,4,5,6,7,8,9,10]

print(f(7))
# Time: O(nlogn)
# Space: O(logn)
def g(n):
    if n <= 1:
        return
    for _ in range(n):
        g(n / 2)
