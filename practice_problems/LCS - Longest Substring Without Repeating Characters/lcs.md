<p>

Implementation of the `lengthOfLongestSubstring` method uses a sliding window approach to find the length of the longest substring without repeating characters. Let's break down how it works:

### Code Breakdown:

- `res`: This variable stores the result, which is the length of the longest substring without repeating characters found so far.
- `left`: This is the starting index of the current window (substring) being considered.
- `charSet`: A set used to store characters that are currently in the window. It helps in quickly checking whether a character is repeating in the current window.

### Iteration Through the String:

- We iterate through the string using a variable `right` which represents the ending index of the current window.

### Checking for Repeated Characters:

- Inside the loop, there is a `while` loop: `while s[right] in charSet`. This loop checks if the character at the current `right` index is already in the `charSet`. If it is, this means we have a repeating character, and we need to adjust the window.
- We remove characters from the set starting from the `left` index and move `left` forward until the character at `right` is no longer in the set. This step ensures that the substring `s[left:right+1]` has all unique characters.

### Updating `res`:

- After adjusting the `left` index (if necessary), we add the character at `right` to `charSet` and calculate the length of the current window (substring) as `right - left + 1`.
- We update `res` with the maximum of the current window's length and the previous value of `res`.

### Returning the Result:

- After the loop completes, `res` contains the length of the longest substring without repeating characters, and it is returned.

### Example Usages:

1. `"abcabcbb"`:
   - The longest substring without repeating characters is `"abc"`, which has a length of 3.

2. `"bbbbb"`:
   - The longest substring without repeating characters is just `"b"`, as all characters are the same. So, the length is 1.

3. `"pwwkew"`:
   - The longest substring without repeating characters is `"wke"`, which has a length of 3.

The sliding window approach efficiently manages the checking of substrings by dynamically adjusting the window size as it encounters repeating characters. This approach is particularly effective for this type of problem, as it minimizes the need to repeatedly scan the entire string, leading to an overall time complexity of O(N), where N is the length of the string.
</p>