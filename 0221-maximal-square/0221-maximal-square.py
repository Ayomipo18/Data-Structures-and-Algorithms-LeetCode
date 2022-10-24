class Solution:
    #time - O(n * m)
    #space - O(n * m)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        max_length = 0
        
        dp = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            dp[i][m-1] = int(matrix[i][m-1])
            max_length = max(max_length, dp[i][m-1])
            
        for i in range(m):
            dp[n-1][i] = int(matrix[n-1][i])
            max_length = max(max_length, dp[n-1][i])
            
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if matrix[i][j] != "0":
                    dp[i][j] = int(matrix[i][j]) + min(dp[i][j+1], dp[i+1][j+1], dp[i+1][j])
                    max_length = max(max_length, dp[i][j])
        return max_length * max_length
                
#         self.dfs(0, 0, matrix, dp)
        
#         result = float('-inf')
        
#         for i in range(n):
#             for j in range(m):
#                 result = max(dp[i][j], result)
                
#         return result * result
        
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