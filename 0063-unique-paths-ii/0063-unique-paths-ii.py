class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        return self.dfs(0, 0, obstacleGrid, memo)
        
    def dfs(self, row, col, obstacleGrid, memo):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if row >= n or col >= m or obstacleGrid[row][col] == 1:
            return 0
        
        if row == n-1 and col == m-1:
            return 1
            
        key = str(row) + "-" + str(col)
        
        if key in memo:
            return memo[key]
            
        memo[key] = self.dfs(row, col+1, obstacleGrid, memo) + self.dfs(row+1, col, obstacleGrid, memo)
        
        return memo[key]