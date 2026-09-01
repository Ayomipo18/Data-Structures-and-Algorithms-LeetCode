class Solution {
    public int maxProfit(int[] prices) {
        /*
        - Single pass variable tracking (running min)
        - max profit by buying and selling stock
        - it's a two pointer and getting min price while using each price seen as the max price
        - also these prices should not cross eah other
        - [7,2,1,5,3,8,6]
        */
        if (prices == null || prices.length == 0) return 0;
        int minPrice = prices[0];
        int maxProfit = 0;

        for(int i=1; i<prices.length; i++) {
            if(minPrice <= prices[i]) {
                maxProfit = Math.max(maxProfit, prices[i] - minPrice);
            }
            minPrice = Math.min(prices[i], minPrice);
        }

        return maxProfit;
    }
}