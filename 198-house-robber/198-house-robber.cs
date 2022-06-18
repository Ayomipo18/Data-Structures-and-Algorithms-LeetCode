public class Solution {
    public int Rob(int[] nums) {
        int [] dp = new int [nums.Length];
        
        if(nums.Length == 1) return nums[0];
        
        dp[0] = nums[0];
        
        dp[1] = nums[1];
        
        int max = 0;
        for(int i = 2; i < nums.Length; i++) {
            for(int j = 0; j < i - 1; j++) {
                if(dp[j] > max) max = dp[j];
            }
            dp[i] = max + nums[i];
        }
        
        return Math.Max(dp[nums.Length - 1], dp[nums.Length - 2]);
    }
}