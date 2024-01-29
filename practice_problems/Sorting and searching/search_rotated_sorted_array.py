class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1

        while first <= last:
            middle = first + (last - first) // 2
            if nums[middle] == target:
                return middle

            if nums[first] <= nums[middle]:
                if nums[first] <= target < nums[middle]:
                    last = middle - 1

                else:
                    first = middle + 1
            else:
                if nums[middle] <  target <= nums[last]:
                    first = middle + 1
                else:
                    last = middle - 1

        return -1



