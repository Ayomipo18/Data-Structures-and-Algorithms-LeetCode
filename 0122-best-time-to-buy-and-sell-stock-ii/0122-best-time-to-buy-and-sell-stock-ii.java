class Solution {
    public int maxProfit(int[] prices) {
        /*
        - Mental Model: Accumulate every upward price slope (greedy approach).
        - Multiple transactions allowed, so add (prices[i] - prices[i-1]) whenever prices[i] > prices[i-1].
        - Time: O(N), Space: O(1)
        */
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            // If today's price is higher than yesterday's, harvest the profit
            if (prices[i] > prices[i - 1]) {
                maxProfit += prices[i] - prices[i - 1];
            }
        }

        return maxProfit;
    }
}