def array_product(arr):
    if not arr:
        return 1
    return arr[0] * array_product(arr[1:])

arr= [1,2,3,4,5,6,7,8,9,10]
print(array_product(arr))