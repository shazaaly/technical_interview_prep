Intuition
When presented with a sorted array and the task of finding a specific target value, binary search is an intuitive choice. This is because binary search efficiently narrows down the search space by comparing the target with the middle element of the array and then deciding which half of the array to continue searching in. This process is repeated, each time halving the search space, making it much faster than a linear search, especially for large arrays.

Approach
Initialize Pointers: Set left to 0 (start of the array) and right to length - 1 (end of the array).
Iterate While left <= right: The search continues as long as left is less than or equal to right.
Calculate Middle Index: In each iteration, find the middle index med using Math.floor((left + right) / 2).
Compare and Narrow Down:
If nums[med] equals the target, return med (the index).
If nums[med] is less than the target, narrow the search to the right half by setting left to med + 1.
If nums[med] is greater than the target, narrow the search to the left half by setting right to med - 1.
Return -1 if Not Found: If the loop ends without returning, it means the target is not in the array. Return -1 in this case.
Complexity
Time Complexity: The time complexity is O(log⁡n)O(\log n)O(logn), where n is the number of elements in the array. This logarithmic complexity arises because the algorithm splits the search space in half with each iteration.
Space Complexity: The space complexity is O(1)O(1)O(1), as the algorithm uses a constant amount of space for the pointers and variables, irrespective of the input array size.