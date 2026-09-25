class Solution {
    public int minCostClimbingStairs(int[] cost) {
        /*
        - min cost to reach top
        - dp
        - state - step
        - basecase - dp[0] =0, dp[1] = 0
        - maths - dp[step] = Math.min(dp[step-2], dp[step-1])
        */

        int n = cost.length;
        int[] dp = new int[n+1];

        for(int i=2; i<n+1; i++) {
            dp[i] = Math.min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]);
        }

        return dp[n];
    }
}