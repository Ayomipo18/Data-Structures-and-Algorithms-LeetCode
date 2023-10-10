class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        explanation
        - BFS
        - involves mainly using a queue
        - so as usual if i see a land('1'), i put it in my queue
        
        
        - DFS
        - i want to go through all the values in the grid
            - if i see a 1(land), i want to call a recursive recursive(dfs which checks horizontally to the right and left of the given cell and vertically to the top and botton of the given cell) from there
            - this dfs calls until the matrix is out of bouns or it comes accross 0(water)
            - anytime i also see a land(1), set it to 0, which is water.
            - so how do i return the number of islands
             - anytime i see a 1(which is land), i immediately count it as an island, then the dfs function goes to set all its surroudning neigbour to water.
        
        - count = 0 -> 1
        start 0,0
        
        - time complexity - O(m*n) + O(m*n)
        - space - O(m*n)
        '''
        
#         m = len(grid)
#         n = len(grid[0])
#         count = 0
        
#         for i in range(m): #O(m*n)
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     count += 1
#                     self.dfs(i, j, grid)
                    
#         return count
                    
                    
#     def dfs(self, row, col, grid):
#         if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
#             return
        
#         grid[row][col] = '0'
        
#         self.dfs(row-1, col, grid)
#         self.dfs(row+1, col, grid)
#         self.dfs(row, col-1, grid)
#         self.dfs(row, col+1, grid)

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc
                    if (r in range(m) and c in range(n) and grid[r][c] == 
                       '1' and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands