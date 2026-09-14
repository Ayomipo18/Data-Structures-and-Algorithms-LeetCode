class Solution {
    public int numIslands(char[][] grid) {
        /*
        - traverse a 2d grid while checking all valid cells
        - valid cells can be connected or not
        - when to use bfs nd dfs
        - bfs - shortest path
        - dfs - reach all nodes traversal
        - normal traversal
        - valid cells - not out of bounds, has not been seen, it's a 1
        */

        int noOfIslands = 0;
        int rows = grid.length;
        int cols = grid[0].length;

        for(int i=0; i<rows; i++) {
            for(int j=0; j<cols; j++) {
                if (grid[i][j] == '1') {
                    noOfIslands += 1;
                    dfs(i, j, grid);
                }
            }
        }

        return noOfIslands;
    }

    public void dfs(int row, int col, char[][] grid) {
        if(row < 0 || row > grid.length-1 ||  col < 0 || col > grid[0].length-1) {
            return;
        }

        if (grid[row][col] == '0') {
            return;
        }

        grid[row][col] = '0';

        dfs(row+1, col, grid);
        dfs(row-1, col, grid);
        dfs(row, col+1, grid);
        dfs(row, col-1, grid);

    }
}