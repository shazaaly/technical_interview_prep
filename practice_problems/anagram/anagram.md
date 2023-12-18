<h2>Anagram</h2>
<p>An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word "listen" is an anagram of "silent." In coding interviews, an anagram-related problem might involve determining if two strings are anagrams of each other, which generally requires checking if they have the same characters in the same quantities, regardless of order.</p>
<br>
<a>https://www.youtube.com/watch?v=nh2VMSRIimI</a>

<p>Let's dive into a Python example to determine if two strings are anagrams using a hash method. The hash method involves creating a frequency map (or count) of each character in both strings and then comparing these maps.</p>

<p>Certainly! Let's dive into a Python example to determine if two strings are anagrams using a hash method. The hash method involves creating a frequency map (or count) of each character in both strings and then comparing these maps.

### Methodology:
1. **Initialize Frequency Maps**: For each string, we create a dictionary where each key is a character, and its value is the number of times it appears in the string.

2. **Iterate through the Strings**: For each character in each string, increment its count in the respective frequency map.

3. **Compare the Frequency Maps**: If the frequency maps are identical, the strings are anagrams; otherwise, they are not.

### Example:
Let's take two strings: `"listen"` and `"silent"`.

#### Step 1: Initialize Frequency Maps
We will create two empty dictionaries, `freq_map1` and `freq_map2`.

```python
freq_map1 = {}
freq_map2 = {}
```

#### Step 2: Iterate through the Strings and Populate Frequency Maps
- For `"listen"`:
  - `l`: freq_map1 becomes `{ 'l': 1 }`
  - `i`: freq_map1 becomes `{ 'l': 1, 'i': 1 }`
  - `s`: freq_map1 becomes `{ 'l': 1, 'i': 1, 's': 1 }`
  - `t`: freq_map1 becomes `{ 'l': 1, 'i': 1, 's': 1, 't': 1 }`
  - `e`: freq_map1 becomes `{ 'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1 }`
  - `n`: freq_map1 becomes `{ 'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1 }`

- For `"silent"`:
  - The process is similar, and freq_map2 will also become `{ 's': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1 }` at the end.

#### Step 3: Compare the Frequency Maps
We compare `freq_map1` and `freq_map2`. If they are the same, then `"listen"` and `"silent"` are anagrams.

### Implementation in Python:
Here's how you would implement this in Python:

```python
def are_anagrams(str1, str2):
    # Step 1: Initialize frequency maps
    freq_map1 = {}
    freq_map2 = {}

    # Step 2: Populate the frequency maps
    for char in str1:
        freq_map1[char] = freq_map1.get(char, 0) + 1

    for char in str2:
        freq_map2[char] = freq_map2.get(char, 0) + 1

    # Step 3: Compare frequency maps
    return freq_map1 == freq_map2

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  # This will print True
```

This code will return `True` for the strings `"listen"` and `"silent"` since they are anagrams. It is a straightforward and efficient way to check for anagrams in coding interviews.</p>