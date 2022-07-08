 public class Solution
    {
        public int MinCost(int[] houses, int[][] cost, int m, int n, int target)
        {
            checked
            {
                long[,,] dp = new long[m + 1,target + 1, n];


                for (int i = 1; i <= m; i++)
                {
                    for (int j = 1; j <= target; j++)
                    {
                        for (int k = 0; k < n; k++)
                        {

                            dp[i, j, k] = int.MaxValue;

                            if (j > i)
                            {
                                continue;
                            }

                            if (j == 1)
                            {
                                if (houses[i - 1] == 0)
                                {
                                    if (dp[i - 1, j, k] < int.MaxValue)
                                    {
                                        dp[i, j, k] = Math.Min(dp[i, j, k], dp[i - 1, j, k] + cost[i - 1][k]);
                                    }
                                }
                                else
                                {
                                    if (houses[i - 1] == k + 1)
                                    {
                                        dp[i, j, k] = Math.Min(dp[i, j, k], dp[i - 1, j, k]);
                                    }
                                }


                                continue;
                            }


                            if (houses[i - 1] != 0)
                            {
                                if (houses[i - 1] == k + 1)
                                {
                                    dp[i, j, k] = Math.Min(dp[i, j, k], dp[i - 1, j, k]);


                                    for (int l = 0; l < n; l++)
                                    {
                                        if (l != k)
                                        {
                                            dp[i, j, k] = Math.Min(dp[i, j, k], dp[i - 1, j - 1, l]);
                                        }
                                    }

                                }

                                continue;
                            }

                            for (int l = 0; l < n; l++)
                            {
                                if (l != k)
                                {
                                    dp[i, j, k] = Math.Min(dp[i, j, k], dp[i - 1, j - 1, l] + cost[i - 1][k]);
                                }
                                else
                                {
                                    dp[i, j, k] = Math.Min(dp[i, j, k], dp[i - 1, j, k] + cost[i - 1][k]);
                                }
                            }
                        }
                    }
                }


                long res = int.MaxValue;

                for (int i = 0; i < n; i++)
                {
                    res = Math.Min(res, dp[m, target, i]);
                }

                if (res >= int.MaxValue)
                {
                    return -1;
                }

                return (int)res;
            }
        }
    }