class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        ans = 0
        prefix_sum = []
        
        for i in range(m):
            inner_arr = []
            for j in range(n):
                inner_arr.append(0)
            prefix_sum.append(inner_arr)
        
        for i in range(m):
            for j in range(n):
                prefix_sum[i][j] = grid[i][j] + (prefix_sum[i][j-1] if j > 0 else 0)
        
        max_sum = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                curr_sum = grid[i][j]
                diff = prefix_sum[i-1][j+1] - (prefix_sum[i-1][j-2] if j-2 >= 0 else 0) + prefix_sum[i+1][j+1] - (prefix_sum[i+1][j-2] if j-2 >= 0 else 0)
                max_sum = max(max_sum, diff + curr_sum)
                
        return max_sum