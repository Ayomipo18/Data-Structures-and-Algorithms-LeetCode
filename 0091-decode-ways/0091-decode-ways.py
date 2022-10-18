class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                
            if (i + 1 < len(s) and (s[i] =="1" or s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        
        return dp[0]
            
        #return self.ways_to_decode(s, 0, dp)
    
    def ways_to_decode(self, s, i, dp):
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
        res = self.ways_to_decode(s, i + 1, dp)
        if (i + 1 < len(s) and (s[i] =="1" or s[i] == "2" and s[i + 1] in "0123456")):
            res += self.ways_to_decode(s, i + 2, dp)
        dp[i] = res
        return res
        