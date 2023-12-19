class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res =  0
        left = 0
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            res = max(right - left + 1 , res)
        return res




# Example usage
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
