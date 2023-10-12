class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        dfs
        - start at the edges of the grid
            - if you see a valu 1 in a cell, run dfs from there and set the cell to 0
            - in the dfs, run in all directions and if you see an out of bounds or a 0, just return, else go to set it to zero and run dfs in 4 directions
        - go through each value, if you see a count, do a count += 1
        time - O(m*n)
        space - O(m*n)
        
        run bfs solution
        - run the same implementation so far, just replace dfs with bfs
        - for bfs, push the cell that is a land(1) into the queue
            - then, while there is a val in the queue, pop it out and set that value 0
            - also, check the remaining adj sides of the cell and if it is not out of bounds or it is a 1, push it to the queue
        '''
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            if grid[i][0] == 1:
                self.bfs(i, 0, grid)
                
        for i in range(m):
            if grid[i][n-1] == 1:
                self.bfs(i, n-1, grid)
                
        for i in range(n):
            if grid[0][i] == 1:
                self.bfs(0, i, grid)
                
        for i in range(n):
            if grid[m-1][i] == 1:
                self.bfs(m-1, i, grid)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    
        return count
    
#     def dfs(self, row, col, grid):
#         if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
#             return
        
#         grid[row][col] = 0
        
#         self.dfs(row-1, col, grid)
#         self.dfs(row+1, col, grid)
#         self.dfs(row, col-1, grid)
#         self.dfs(row, col+1, grid)
        
    def bfs(self, row, col, grid):
        q = collections.deque()
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        q.append((row, col))
        grid[row][col] = 0
        
        while q:
            r, c = q.popleft()
            
            for dir in dirs:
                if r + dir[0] < 0 or r + dir[0] >= len(grid) or c + dir[1] < 0 or c + dir[1] >= len(grid[0]) or grid[r+dir[0]][c+dir[1]] == 0:
                    continue
                q.append((r+dir[0], c+dir[1]))
                grid[r+dir[0]][c+dir[1]] = 0