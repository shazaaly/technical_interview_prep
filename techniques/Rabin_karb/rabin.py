
def rabin_karp(text, pattern):
    text_length = len(text)  # Length of the text
    pattern_length = len(pattern)  # Length of the pattern
    pattern_hash = get_hash(pattern)
    current_hash = get_hash(text[:pattern_length])

    for i in range(0, text_length - pattern_length + 1):
        if pattern_hash == current_hash:
            # When hashes match, check for actual equality
            if text[i:i + pattern_length] == pattern:
                return i  # Pattern found at index i

		# cgeck if sufficient substring left.
        if i < text_length - pattern_length:
            # Calculate hash value for next window: Remove leading char, add trailing char
            current_hash = (current_hash - ord(text[i])) // 101
            current_hash += ord(text[i + pattern_length]) * (101 ** (pattern_length - 1))

    return -1  # Pattern not found

