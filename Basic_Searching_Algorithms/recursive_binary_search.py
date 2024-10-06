def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2
    
    if arr[mid] == target:
        return f'Element found at index: {mid}'
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target) # search in the right half
    else:
        return recursive_binary_search(arr, low, mid - 1, target) # search in the left half
        
        
arr = [23, 35, 67, 89, 92, 126]
low, high, target = 0, len(arr) - 1, 23
print(recursive_binary_search(arr, low, high, target))