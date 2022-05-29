public class Solution {
    public int Jump(int[] nums) {
        int[] dp = new int[nums.Length];
        dp[0] = 1;
        for(int i = 1; i < nums.Length; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[j] + j >= i) {
                    if(dp[i] > 0) dp[i] = Math.Min(dp[i], dp[j] + 1);
                    else dp[i] = dp[j] + 1;
                }
            }
        }
        return dp[nums.Length - 1] - 1;
    }
}