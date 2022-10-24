class Solution:
    #time - O(n * m)
    #space - O(n * m)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[-1 for i in range(m)] for j in range(n)]
        self.dfs(0, 0, matrix, dp)
        
        result = float('-inf')
        
        for i in range(n):
            for j in range(m):
                result = max(dp[i][j], result)
                
        return result * result
        
    def dfs(self, row, col, matrix, dp):
        if row >= len(matrix) or col >= len(matrix[0]):
            return 0
        
        if dp[row][col] != -1:
            return dp[row][col]
        
        right = self.dfs(row, col+1, matrix, dp)
        diag = self.dfs(row+1, col+1, matrix, dp)
        down = self.dfs(row+1, col, matrix, dp)
        
        dp[row][col] = int(matrix[row][col]) + min(right, diag, down) if int(matrix[row][col]) > 0 else 0
        
        return dp[row][col]