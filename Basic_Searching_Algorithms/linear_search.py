def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f'Element found at index: {i}'
    return 'Element is not present in the array !'


arr = [2, 5, 7, 19, 20, 33, 56, 78]
target = 20
print(linear_search(arr, target))
