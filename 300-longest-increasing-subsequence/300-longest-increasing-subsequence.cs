public class Solution {
    public int LengthOfLIS(int[] nums) {
        var dp = new int[nums.Length];
        Array.Fill(dp, 1);
        for(var i = 0; i < nums.Length; i++)
        {
            for(var j = 0; j < i; j++)
            {
                if(nums[i] > nums[j])
                {
                    dp[i] = Math.Max(dp[i], 1 + dp[j]);
                }
            }
        }

        return dp.Max();
    }
}