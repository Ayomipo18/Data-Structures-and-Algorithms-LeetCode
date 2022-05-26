/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSub = nums[0];
    let currentSum = 0;
    for(i=0; i<nums.length; i++) {
        if(currentSum < 0) currentSum = 0;
        currentSum += nums[i];
        maxSub = Math.max(maxSub, currentSum)
    }
    return maxSub;
};