def array_product(arr):
    total = 1
    for n in arr:
        total *= n
    return total

arr= [1,2,3,4,5,6,7,8,9,10]
print(array_product(arr))