/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    if (!candidates || candidates.length == 0) return [];
    let res = [];
    candidates.sort((a,b) => a-b);
    var helper = function(curSum, cur, index){
        if (curSum == target){
            res.push([...cur]);
            return;
        }
        for(let i = index; i < candidates.length; i++){
            if (i != index && candidates[i] == candidates[i-1]) continue;
            if (curSum > target) return;
            cur.push(candidates[i]);
            helper(curSum+candidates[i], cur, i+1);
            cur.pop();
        }
    }
    helper(0, [], 0);
    return res;
};