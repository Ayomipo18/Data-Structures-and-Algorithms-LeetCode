public class Solution {
    public int MaxProfit(int[] prices) {
        int max = 0, min = prices[0];
        for(int i = 1; i < prices.Length; i++)   {
		
            if(min < prices[i])
                max = Math.Max(prices[i]-min, max);
            else
                min = prices[i];
        }
        return max;
    }
}