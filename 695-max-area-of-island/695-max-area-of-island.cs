public class Solution {
    public int MaxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        int currArea = 0;
        
        for(int i = 0; i < grid.Length; i++) {
            for(int j = 0; j < grid[0].Length; j++) {
                if(grid[i][j] == 1) {
                    currArea = dfs(grid, i, j);
                    maxArea = Math.Max(maxArea, currArea);
                }
            }
        }
        
        return maxArea;
    }
    
    private int dfs(int[][] grid, int i, int j) {
        int count = 0;
        if(i < 0 || i >= grid.Length || j < 0 || j >= grid[0].Length || grid[i][j] == 0) {
            return 0;
        }
        grid[i][j] = 0;
        return (1 + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i+1, j) + dfs(grid, i, j-1));
    }
}