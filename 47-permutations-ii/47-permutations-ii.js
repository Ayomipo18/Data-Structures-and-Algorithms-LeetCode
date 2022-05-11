/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    const res = [];
    const length = nums.length;
    const visited = new Array(length).fill(0);
    const memo = new Set();
    traverse(nums, res, [], length, visited, memo);
    return res;
};

const traverse = (nums, res, temp, length, visited, memo) => {
    if (temp.length === length) {
        res.push([...temp]);
        return;
        
    }
    
    for (let i = 0; i < length; i++) {
        if (visited[i]) continue;
        visited[i] = 1;
        temp.push(nums[i]);
        if (memo.has(temp.join(''))) {
            temp.pop();
            visited[i] = 0;
            continue;
        }
        memo.add(temp.join(''));
        traverse(nums, res, temp, length, visited, memo);
        temp.pop();
        visited[i] = 0;
    }
}