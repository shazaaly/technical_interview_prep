<a>https://www.youtube.com/watch?v=xvWFo2ZCRDY&list=PL0x1zsLFiXsxrXKSmI7YDScIqMZD86uSX&index=7</a> <span>min 7:50</span>

<p>A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). Examples include "madam", "racecar", and "12321".

When checking if a string is a palindrome in a programming context, the typical approach is to compare characters from the beginning and end of the string, <strong>moving towards the center</strong>. If all corresponding pairs of characters are equal, the string is a palindrome.</p>

<p>Methodology:
1- Normalize the String: Convert the string to a standard format, usually by lowercasing all letters and removing non-alphanumeric characters, to ignore case and punctuation.

2-Two-Pointer Approach: Use two pointers, one starting at the beginning of the string (left) and the other at the end (right).

3- Iterate and Compare: Move left towards the right and right towards the left, comparing the characters at these pointers. If at any point characters don't match, the string is not a palindrome.

4-Termination Condition: If the entire string is traversed (i.e., left and right meet or cross each other) without finding any mismatch, the string is a palindrome.

Example:
Let's take the string "Racecar".

Step 1: Normalize the String
Convert to lower case: "racecar"
(In this case, there are no non-alphanumeric characters to remove)

Step 2 and 3: Two-Pointer Approach and Iterate
Initialize left at the start (index 0: 'r') and right at the end (index 6: 'r').
Compare left and right. If they are the same, move left one step right and right one step left.
Continue this process. The comparisons will be 'r' == 'r', 'a' == 'a', 'c' == 'c', etc.

Step 4: Termination Condition
If left and right pointers meet or cross without finding any mismatch, we conclude it's a palindrome.
Implementation in Python:
Here's how you would implement a palindrome check in Python:

```python
def is_palindrome(s):
    # Step 1: Normalize the string
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Step 2: Two-pointer approach
    left, right = 0, len(s) - 1

    # Step 3: Iterate and compare
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1

    # Step 4: Termination condition
    return True

```
<p>
Example:
Let's consider the string s = "Hello, World!".

Iterating over s, the characters are checked for being alphanumeric. The characters "H", "e", "l", "l", "o", "W", "o", "r", "l", and "d" pass this check.
Each of these characters is then converted to lowercase: "h", "e", "l", "l", "o", "w", "o", "r", "l", "d".
These characters are then joined together to form a new string: "helloworld".
</p>
# Example usage
print(is_palindrome("Racecar"))  # This will print True
This function will correctly identify "Racecar" as a palindrome. The normalization step ensures the function is robust against case and non-alphanumeric characters, making it applicable to a wide range of inputs.
</p>