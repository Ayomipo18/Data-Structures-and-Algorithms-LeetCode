class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        memo = {}
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                
                key = str(i) + "-" + str(j)
                
                if i == n-1 and j == m-1 and obstacleGrid[i][j] != 1:
                    memo[key] = 1
                    continue
                
                right_key = str(i) + "-" + str(j+1)
                bottom_key = str(i+1) + "-" + str(j)
                
                if obstacleGrid[i][j] == 1:
                    memo[key] = 0
                else:
                    memo[key] = (memo[right_key] if right_key in memo else 0) + (memo[bottom_key] if bottom_key in memo else 0)
                    
        return memo["0-0"]
                    
        #return self.dfs(0, 0, obstacleGrid, memo)
        
#     def dfs(self, row, col, obstacleGrid, memo):
#         n = len(obstacleGrid)
#         m = len(obstacleGrid[0])
#         if row >= n or col >= m or obstacleGrid[row][col] == 1:
#             return 0
        
#         if row == n-1 and col == m-1:
#             return 1
            
#         key = str(row) + "-" + str(col)
        
#         if key in memo:
#             return memo[key]
            
#         memo[key] = self.dfs(row, col+1, obstacleGrid, memo) + self.dfs(row+1, col, obstacleGrid, memo)
        
#         return memo[key]