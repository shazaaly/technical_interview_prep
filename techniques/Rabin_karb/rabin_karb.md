The Rabin-Karp algorithm is a string searching algorithm that uses hashing to find any one of a set of patterns in a string.

The basic idea of the Rabin-Karp algorithm is to use a hash function to compute a fingerprint for each substring of the text.

The Rabin-Karp algorithm is a very efficient string searching algorithm.
It runs in O(n+m) time, where n is the length of the text and m is the length of the pattern. The algorithm is also very easy to implement.

Here is a more detailed description of the Rabin-Karp algorithm:

1. Choose a hash function.
The hash function should be chosen so that it is easy to compute
and so that it is unlikely to produce the same hash value for two different substrings.

2. Compute the fingerprint for the first m characters of the text.

3. Compute the fingerprints for the patterns.

4. Compare the fingerprints of the substrings of the
text to the fingerprints of the patterns.
 If the fingerprint of a substring and a pattern match,
 the algorithm reports that the pattern has been found in the text.

5. If the algorithm has not reported that the pattern
has been found in the text, it shifts the window of m characters
to the right by one character and repeats the process from step 2.


<h3>Further Reading :</h3>
The function rabin_karp(text, pattern) takes two arguments: text and pattern.
text is the string where we want to search for the pattern.
The lengths of the text and pattern are stored in text_length and pattern_length respectively.

The function get_hash() is used to calculate the hash value of the pattern and the first substring of text of length equal to pattern_length.
These hash values are stored in pattern_hash and current_hash respectively.

The main part of the function is a loop that iterates over the text string.
 For each iteration, it first checks if the hash of the current substring of text matches the hash of the pattern. If the hashes match, it then checks if the actual strings are equal. If they are, it returns the index i where the pattern starts in the text.

If the hashes or the strings do not match, the function checks if there is a sufficient substring left in the text for the next iteration. If there is, it calculates the hash value for the next substring by removing the hash of the leading character and adding the hash of the trailing character. This is done using the properties of the hash function.

If the loop completes without finding a match, the function returns -1 to indicate that the pattern was not found in the text.