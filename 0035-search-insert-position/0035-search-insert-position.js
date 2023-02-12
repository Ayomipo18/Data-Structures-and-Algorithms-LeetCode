/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let pivot, left = 0, right = nums.length - 1;
    while (left <= right) {
      pivot = left + Math.floor((right - left) / 2);
      if (nums[pivot] == target) return pivot;
      if (target < nums[pivot]) right = pivot - 1;
      else left = pivot + 1;
    }
    return left;
};