public class Solution {
    public bool IsInterleave(string s1, string s2, string s3) {
        int l1 = s1.Length, l2 = s2.Length;
        if (l1 + l2 != s3.Length) return false;
        
        bool[,] dp = new bool[l1 + 1, l2 + 1];

        dp[0, 0] = true;

        for (int i = 0; i < l2; i++)
            
            dp[0, i + 1] = (s2[i] == s3[i]) && dp[0, i];

        for (int i = 0; i < l1; i++)
            
            dp[i + 1, 0] = (s1[i] == s3[i]) && dp[i, 0];

        for (int r = 1; r <= l1; r++)
            for (int c = 1; c <= l2; c++)
                if ((s3[-1 + r + c] == s1[r - 1] && dp[r - 1, c]) || (s3[-1 + r + c] == s2[c - 1] && dp[r, c - 1]))
                    dp[r, c] = true;

        return dp[l1, l2];
    }
}