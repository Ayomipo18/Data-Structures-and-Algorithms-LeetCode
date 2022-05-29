/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    const dp = [1];
    for(let i = 1; i < nums.length; i++) {
        for(let j = 0; j < i; j++) {
            if(nums[j] + j >= i) {
                if(dp[i]) dp[i] = Math.min(dp[i], dp[j] + 1);
                else dp[i] = dp[j] + 1;
            }
        }
    }
    return dp[nums.length - 1] - 1; 
};