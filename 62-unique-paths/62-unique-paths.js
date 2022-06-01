/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const dp = new Array(m).fill(0).map(() => new Array(n).fill(0));
    
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(i===0 && j===0) dp[i][j] = 1;
            else {
                if(i - 1 < 0) dp[i][j] = dp[i][j-1];
                else if (j - 1 < 0) dp[i][j] = dp[i-1][j];
                else dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }
    return dp[m-1][n-1];
};