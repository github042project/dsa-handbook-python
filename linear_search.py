```python
# Linear Search Implementation in Python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 23, 45, 70, 11]
target = 70
result = linear_search(arr, target)
print(f'Target found at index: {result}' if result != -1 else 'Target not found')
```