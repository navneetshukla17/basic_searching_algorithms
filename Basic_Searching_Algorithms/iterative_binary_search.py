def iterative_binary_search(arr, target):
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return f'Element present at index: {mid}'
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return 'Element is not present in the array !'
    

arr = [10, 14, 32, 56, 76, 96, 400]
target = 32
print(iterative_binary_search(arr, target))