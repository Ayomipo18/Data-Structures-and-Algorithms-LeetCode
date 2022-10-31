class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * len(s)
        dict_set = set(wordDict)
        return self.recursive(dp, s, 0, dict_set)
        
    def recursive(self, dp, s, index, dict_set):
        if index == len(s):
            return True
        
        if dp[index] > -1:
            return dp[index]
        
        for i in range(index + 1, len(s) + 1):
            if s[index: i] in dict_set and self.recursive(dp, s, i, dict_set):
                dp[index] = 1
                return True
        
        dp[index] = 0
        return False