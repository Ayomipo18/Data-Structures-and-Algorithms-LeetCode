class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        - start at the edges of the grid
            - if you see a valu 1 in a cell, run dfs from there and set the cell to 0
            - in the dfs, run in all directions and if you see an out of bounds or a 0, just return, else go to set it to zero and run dfs in 4 directions
        - go through each value, if you see a count, do a count += 1
        '''
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            if grid[i][0] == 1:
                self.dfs(i, 0, grid)
                
        for i in range(m):
            if grid[i][n-1] == 1:
                self.dfs(i, n-1, grid)
                
        for i in range(n):
            if grid[0][i] == 1:
                self.dfs(0, i, grid)
                
        for i in range(n):
            if grid[m-1][i] == 1:
                self.dfs(m-1, i, grid)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    
        return count
    
    def dfs(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return
        
        grid[row][col] = 0
        
        self.dfs(row-1, col, grid)
        self.dfs(row+1, col, grid)
        self.dfs(row, col-1, grid)
        self.dfs(row, col+1, grid)