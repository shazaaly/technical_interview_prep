def canConstruct(ransomNote: str, magazine: str) -> bool:
    hash = {}
    for char in magazine:
        if char in hash:
            hash[char] += 1
        else:
            hash[char] = 1

    for char in ransomNote:
        if char in hash and hash[char] >= 1:
            hash[char] -= 1
        else:
            return False

    return True
# print(canConstruct("aa", "ab"))