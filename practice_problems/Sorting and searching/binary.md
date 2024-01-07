
# Binary Search in Sorted Array

## Intuition
When faced with the task of finding a specific target value in a sorted array, binary search is an intuitive and efficient choice. This algorithm narrows down the search space by halving it with each iteration, making it significantly faster than a linear search for large arrays.

## Approach
1. **Initialize Pointers**: Set `left` to the start of the array (0) and `right` to the end (`length - 1`).
2. **Iterate While `left` <= `right`**: Continue the search as long as the `left` pointer is less than or equal to the `right` pointer.
3. **Calculate Middle Index**: In each iteration, find the middle index `med` using `Math.floor((left + right) / 2)`.
4. **Compare and Narrow Down**:
   - If `nums[med]` equals the target, return `med` (the index).
   - If `nums[med]` is less than the target, move the `left` pointer to `med + 1` to search the right half.
   - If `nums[med]` is greater than the target, move the `right` pointer to `med - 1` to search the left half.
5. **Return -1 if Not Found**: If the loop concludes without finding the target, return -1, indicating the target is not in the array.
