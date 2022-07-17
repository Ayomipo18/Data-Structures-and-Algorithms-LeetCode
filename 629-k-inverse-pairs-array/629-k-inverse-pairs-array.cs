public class Solution 
{
    public int KInversePairs(int n, int k) 
    {
        int[,] dp = new int[n + 1,k + 1];
        for (int row = 1; row <= n; row++) 
        {
            dp[row,0] = 1;
            int pRow = row - 1;
            for (int col = 1; col <= k; col++) 
            {
                for (int pCol = col; pCol > col - row; pCol--)
                {
                    if (pCol < 0)
                    {
                        break;
                    }
                    dp[row,col] = (dp[row,col] + dp[pRow,pCol]) % 1000000007;
                }
            }
        }
        return dp[n,k];
    }
}