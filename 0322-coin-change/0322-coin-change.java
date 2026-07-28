class Solution {
    /*
    top down recursive approach without memoization
    - N - coins.length
    - S - amount
    - time - O(N^S)
    - Space - O(S)

    top down recursive approach with memoization
    - N - coins.length
    - S - amount
    - time - O(NxS)
    - Space - O(S)
    */
    public int coinChange(int[] coins, int amount) {
        int[] memo = new int[amount+1];
        for(int i=0; i<memo.length; i++) {
            memo[i] = -1;
        }

        int ans = dp(coins, amount, memo);
        if (ans == Integer.MAX_VALUE) {
            return -1;
        }
        return ans;
    }

    public int dp(int[] coins, int amount, int[] memo) {
        int result = Integer.MAX_VALUE;
        if (amount == 0) return 0;
        if (amount < 0) return Integer.MAX_VALUE;

        if(memo[amount] != -1) return memo[amount];

        for (int i=0; i<coins.length; i++) {
            int dp_result = dp(coins, amount-coins[i], memo);
            if (dp_result != Integer.MAX_VALUE) {
                result = Math.min(result, 1 + dp_result);
            }
        }
        memo[amount] = result;
        return memo[amount];
    }
}