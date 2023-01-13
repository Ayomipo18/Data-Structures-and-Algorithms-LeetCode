class Solution:
    '''
    - time: #O(m*n)
    - space: #O(m*n)
    - start at at the four borders
    - start at the top border and bottom moving inwards doing dfs, try and see if you can get to the oceans from there, if you can, add it to their corresponding sets.
    - start at the left and right border moving inwards doing dfs, try and see if you can get to the oceans from there, if you can, add it to their corresponding sets.
    - then go through each cell in our grid and check if a cell are both in pacific and atlantic sets. if it can, add to output array
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set() #O(m*n)
        self.result = [] #O(m*n)
        
        #top and bottom
        for col in range(cols): #O(n)
            self.dfs(heights, 0, col, heights[0][col], pac) #O(m*n) 
            self.dfs(heights, rows-1, col, heights[rows-1][col], atl) #O(m*n)
        
        #left and right
        for row in range(rows): #O(m)
            self.dfs(heights, row, 0, heights[row][0], pac) #O(m*n)
            self.dfs(heights, row, cols-1, heights[row][cols-1], atl) #O(m*n)
            
        for r in range(rows): #O(m*n)
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    self.result.append([r,c])

        return self.result

    def dfs(self, heights, row, col, height, visit):
        if ((row, col) in visit or row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]) or heights[row][col] < height):
            return
        visit.add((row, col))
        self.dfs(heights, row+1, col, heights[row][col], visit)
        self.dfs(heights, row, col+1, heights[row][col], visit)
        self.dfs(heights, row-1, col, heights[row][col], visit)
        self.dfs(heights, row, col-1, heights[row][col], visit)