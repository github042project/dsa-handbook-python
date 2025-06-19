```python
# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = 7
print(f'Fibonacci sequence up to {n} terms:')
for i in range(n):
    print(fibonacci(i), end=' ')
```