def binary_search(arr, x):
    left =  8
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

    if arr[mid] == x:
        return mid

    if arr[mid] < x:
        left = mid + 1
    else:
        right = mid - 1 
    return -1 

arr = [2, 4, 6, 8, 10, 12]
x = 10
result = binary_search(arr, x)

if result != -1:
    print("Element found at index", result)
else:
    print("element not found")