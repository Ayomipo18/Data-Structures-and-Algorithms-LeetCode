public class Solution {
    //time - O(n * m * 4 * m * n) 
    //space - O(n*m)
    private IList<int[]> directions = new List<int[]>();
    
    public int NumDistinctIslands(int[][] grid) {
        int n = grid.Length;
        int m = grid[0].Length;
        bool[,] visited = new bool[n,m];
        HashSet<string> hashset = new();
        
        directions.Add(new int[]{-1,0}); //up
        directions.Add(new int[]{0,1}); //right
        directions.Add(new int[]{1,0}); //down
        directions.Add(new int[]{0,-1}); //left
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(visited[i,j] != true && grid[i][j] == 1) {
                    StringBuilder sb = new StringBuilder();
                    dfs(i, j, grid, visited, sb, i, j);
                    
                    string key = sb.ToString();
                    hashset.Add(key);
                }
            }
        }
        
        return hashset.Count;
    }
    
    private void dfs(int row, int col, int[][] grid, bool[,] visited, StringBuilder sb, int row0, int col0) {
        int n = grid.Length;
        int m = grid[0].Length;
        visited[row, col] = true;
        string key = $".{row-row0}.{col-col0}";
        sb.Append(key);
        
        foreach(var direction in directions) {
            int nextRow = row + direction[0];
            int nextCol = col + direction[1];
            if(nextRow < 0 || nextRow >= n || nextCol < 0 || nextCol >= m || visited[nextRow, nextCol] == true || grid[nextRow][nextCol] == 0){
                continue;
            }
            dfs(nextRow, nextCol, grid, visited, sb, row0, col0);
        }
    }
}