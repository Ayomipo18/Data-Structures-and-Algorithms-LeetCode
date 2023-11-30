class Solution:
    def numSquares(self, n: int) -> int:
        '''
        - time - O(n * n^1/2)
        - space - O(n)
        '''
        dp = [n] * (n+1)
        dp[0] = 0
        
        for target in range(1, n+1):
            for s in range(1, target + 1):
                square = s * s
                if square > target:
                    break
                    
                dp[target] = min(dp[target], 1 + dp[target-square])
        return dp[n]