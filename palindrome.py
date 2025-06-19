```python
# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

string = 'madam'
print(f'{string} is a palindrome' if is_palindrome(string) else f'{string} is not a palindrome')
```