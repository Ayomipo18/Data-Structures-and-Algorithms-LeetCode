class Solution:
    #time - 2^len(s3)
    #space - len(s3)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}
        return self.dfs(s1, s2, s3, 0, 0, 0, memo)
    
    def dfs(self, s1, s2, s3, s1_ptr, s2_ptr, s3_ptr, memo):
        if s1_ptr + s2_ptr == len(s3):
            return True
        
        key = str(s1_ptr) + str(s2_ptr)

        if key in memo:
            return memo[key]

        if s1_ptr < len(s1) and s1[s1_ptr] == s3[s3_ptr]:
            if self.dfs(s1, s2, s3, s1_ptr + 1, s2_ptr, s3_ptr + 1, memo):
                return True
        
        if s2_ptr < len(s2) and s2[s2_ptr] == s3[s3_ptr]:
            if self.dfs(s1, s2, s3, s1_ptr, s2_ptr + 1, s3_ptr + 1, memo):
                return True
        
        memo[key] = False
        return memo[key]