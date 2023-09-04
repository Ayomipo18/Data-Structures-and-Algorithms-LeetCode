/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let climb = new Array(n+1);
    climb[1] = 1, climb[2] = 2;
    for(let i = 3; i <= n; i++) {
        climb[i] = climb[i-1] + climb[i-2];
    }
    return climb[n];
};