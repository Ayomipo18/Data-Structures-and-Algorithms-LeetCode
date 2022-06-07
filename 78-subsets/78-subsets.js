/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const result = [];
    const length = nums.length;
    const backTrack = function(index, currArr) {
        result.push([...currArr]);
        if(currArr[currArr.length-1] === nums[length-1]) return;
        for(let i = index; i<nums.length; i++) {
            currArr.push(nums[i]);
            backTrack(i+1, currArr);
            currArr.pop();
        }
    }
    backTrack(0, []);
    return result;
};