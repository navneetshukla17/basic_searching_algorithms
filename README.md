# Search Algorithms in Python

This repository contains implementations of three fundamental search algorithms in Python:

1. **Linear Search**
2. **Iterative Binary Search**
3. **Recursive Binary Search**

These algorithms are designed to search for a target element in a list or array. Each file includes a simple Python script that demonstrates how the corresponding search algorithm works.

## Files Included

- **`linear_search_algorithm.py`**: 
  - Implements the **Linear Search** algorithm.
  - Linear Search scans through each element in the array one by one until the target element is found or the end of the array is reached.
  - Time complexity: O(n).
  
- **`iterative_binary_search.py`**:
  - Implements the **Iterative Binary Search** algorithm.
  - Binary Search works only on **sorted arrays**. It repeatedly divides the search space in half until the target is found.
  - Time complexity: O(log n).

- **`recursive_binary_search.py`**:
  - Implements the **Recursive Binary Search** algorithm.
  - This is a recursive version of the Binary Search, where the function calls itself with a smaller search range until the target is found.
  - Time complexity: O(log n), space complexity is also O(log n) due to recursion.

## How to Use

Each Python file can be run individually to test the search algorithms. You can modify the list/array and target element directly in the script or integrate these functions into your own projects.

### Example Usage:
```bash
python linear_search_algorithm.py
python iterative_binary_search.py
python recursive_binary_search.py
