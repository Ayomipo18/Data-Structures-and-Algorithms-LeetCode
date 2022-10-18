class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        if n == 1:
            return triangle[0][0]
        
        for i in range(n-1, 1, -1):
            triangle[i-1][0] += min(triangle[i][0], triangle[i][1])
            for j in range(1, i-1):
                triangle[i-1][j] += min(triangle[i][j], triangle[i][j+1])
            triangle[i-1][i-1] += min(triangle[i][i-1], triangle[i][i])
            
        return triangle[0][0] + min(triangle[1][0], triangle[1][1])
                