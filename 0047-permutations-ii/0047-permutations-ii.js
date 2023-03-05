/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function (nums) {
    const result = [];
    const memo = new Set();
    const used = new Array(nums.length).fill(false);
    traverse(nums, 0, [], result, used, memo);
    return result;
}

var traverse = function (nums, index, currArray, result, used, memo) {
    if(currArray.length === nums.length) {
        result.push([...currArray]);
        return;
    }
    
    for(let i=index; i<nums.length; i++) {
        if(used[i]) continue;
        currArray.push(nums[i]);
        used[i] = true;
        if(memo.has(currArray.toString())) {
            currArray.pop();
            used[i] = false;
            continue;
        }
        memo.add(currArray.toString());
        traverse(nums, index, currArray, result, used, memo);
        currArray.pop();
        used[i] = false;
    }
}
