/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    const result = [];
    
    const backTrack = function(index, currArr) {
        if(currArr.length === k) {
            result.push([...currArr]);
            //return;
        }
        for(let i = index; i<=n; i++) {
            currArr.push(i);
            backTrack(i+1, currArr);
            currArr.pop();
        }
    }
    
    backTrack(1, []);
    
    return result;
};