/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    const length = nums.length
    let left = 0
    let right = length - 1
    let med;

    while (left <= right) {
        med = Math.floor((right + left) / 2)
        if (nums[med] === target) {
            return med;
        }
        else if (nums[med] < target) {
            left = med + 1
        } else {
            right = med - 1
        }

    }
    return -1;
};