def a(n):
    if n <= 1:
        return
    a(n - 1)

print(a(6))

def b(n):
    if n <= 1:
        return
    b(n -2)

print(b(3))