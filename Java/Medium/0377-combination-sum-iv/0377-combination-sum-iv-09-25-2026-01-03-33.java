class Solution {
    public int combinationSum4(int[] nums, int target) {
        /*
        - possible combinations that add up to target
        - combinations - dp
        - state - target
        - basecase - dp[0] = 1
        - mathematical expression -> dp[4] = dp[4-num] + dp[4]
        - Time - O(targetxnum)
        - Space - O(target)
        */
        int[] dp = new int[target+1];
        dp[0] = 1;

        for(int i=1; i<=target; i++) {
            for(int num : nums) {
                if(i-num >= 0) {
                    dp[i] += dp[i-num];
                }
            }
        }

        return dp[target];
    }
}