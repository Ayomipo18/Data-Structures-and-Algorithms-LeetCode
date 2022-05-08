/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const numsMap = {};
    for(i=0; i<nums.length; i++) {
        if(numsMap[nums[i]] >=0 ) return [numsMap[nums[i]], i];
        else {
            let numberToFind = target - nums[i];
            numsMap[numberToFind] = i;
        }
    }
    return null;
};
