```python
# Frequency counter for characters in a string
def frequency_counter(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

string = 'datascience'
print('Character Frequencies:', frequency_counter(string))
```