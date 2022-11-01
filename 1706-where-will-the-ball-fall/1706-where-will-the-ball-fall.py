class Solution:
        
    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        self.result = []
        
        for i in range(len(grid[0])):
            self.result.append(self.recurse(0, i))
        
        return self.result
    
    def recurse(self, row, col):
        if row == len(self.grid):
            return col
        
        if self.grid[row][col] == 1 and col < len(self.grid[0]) - 1:
            if self.grid[row][col+1] == - 1:
                return -1
            return self.recurse(row+1, col+1)
        elif self.grid[row][col] == -1 and col > 0:
            if self.grid[row][col-1] == 1:
                return -1
            return self.recurse(row+1, col-1)
        
        return -1