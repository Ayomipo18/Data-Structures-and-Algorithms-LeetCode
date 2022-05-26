/**
 * @param {number[]} nums
 * @return {number}
 */

var maxSubArray = function(nums) {
    let maxSub = nums[0];
    let currSum = 0;
    for(let i=0; i < nums.length; i++) {
        if(currSum < 0) currSum = 0;
        currSum += nums[i];
        maxSub = Math.max(currSum, maxSub);
    }
    return maxSub;
}



// var maxSubArray = function(nums) {
//     let maxSub = nums[0];
//     let currentSum = 0;
//     for(i=0; i<nums.length; i++) {
//         if(currentSum < 0) currentSum = 0;
//         currentSum += nums[i];
//         maxSub = Math.max(maxSub, currentSum)
//     }
//     return maxSub;
// };