public class Solution {
    public int MinDistance(string word1, string word2) {
        int word1Length = word1.Length;
        int word2Length = word2.Length;
        int [,] dp = new int [word1Length + 1, word2Length + 1];
        
        for(int i = 0; i < word1Length + 1; i++) {
            dp[i,0] = i;
        }
        
        for(int i = 0; i < word2Length + 1; i++) {
            dp[0,i] = i;
        }
        
        for(int i = 1; i < word1Length + 1; i++) {
            for(int j = 1; j < word2Length + 1; j++) {
                if(word1[i-1] == word2[j-1]) {
                    dp[i, j] = dp[i-1, j-1];
                } else {
                    dp[i, j] = Math.Min(Math.Min(dp[i, j-1], dp[i-1, j-1]), dp[i-1, j]) + 1;
                }
            }
        }
        return dp[word1Length, word2Length];
    }
}