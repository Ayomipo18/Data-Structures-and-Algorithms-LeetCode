class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.grid = [[0] * (m+1) for i in range(n+1)]
        
        for i in range(n):
            prefix = 0
            for j in range(m):
                prefix += matrix[i][j]
                above = self.grid[i][j+1]
                self.grid[i + 1][j + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.grid[row2+1][col2+1]
        above = self.grid[row1][col2+1]
        left = self.grid[row2+1][col1]
        top_left = self.grid[row1][col1]
        return bottom_right - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)