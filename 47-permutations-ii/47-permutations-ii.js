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
        if(!memo.has(currArray.toString())) {
           memo.add(currArray.toString());
           result.push([...currArray]);
           return;
        }
        return;
    }
    
    for(let i=index; i<nums.length; i++) {
        if(used[i]) continue;
        currArray.push(nums[i]);
        used[i] = true;
        traverse(nums, index, currArray, result, used, memo);
        currArray.pop();
        used[i] = false;
    }
}



// var permuteUnique = function(nums) {
//     const res = [];
//     const length = nums.length;
//     const visited = new Array(length).fill(0);
//     const memo = new Set();
//     traverse(nums, res, [], length, visited, memo);
//     return res;
// };/

// const traverse = (nums, res, temp, length, visited, memo) => {
//     if (temp.length === length) {
//         res.push([...temp]);
//         return;
        
//     }
    
//     for (let i = 0; i < length; i++) {
//         if (visited[i]) continue;
//         visited[i] = 1;
//         temp.push(nums[i]);
//         if (memo.has(temp.join(''))) {
//             temp.pop();
//             visited[i] = 0;
//             continue;
//         }
//         memo.add(temp.join(''));
//         traverse(nums, res, temp, length, visited, memo);
//         temp.pop();
//         visited[i] = 0;
//     }
// }