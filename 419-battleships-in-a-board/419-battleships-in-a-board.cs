public class Solution {
    //time - O(n^2)
    //space - O(1)
    public int CountBattleships(char[][] board) {
        int numBattleShips = 0;
        for(int i = 0; i < board.Length; i++) {
            for(int j = 0; j < board[0].Length; j++) {
                if(board[i][j] == 'X') {
                    numBattleShips++;
                    dfs(board, i, j);
                }
            }
        }
        return numBattleShips;
    }
    
    private void dfs(char[][] board, int row, int col) {
        if(row < 0 || row >= board.Length || col < 0 || col >= board[0].Length || board[row][col] != 'X') {
            return;
        }
        
        board[row][col] = '.';
        dfs(board, row-1, col);
        dfs(board, row, col+1);
        dfs(board, row+1, col);
        dfs(board, row, col-1);
    }
}

//go through the matrix, if we see X, increase battleship and do dfs
//inside our dfs, if we see that the adjacent values of our cell is X, we want to change it to .
//else just return if my cell adjacent values are . or out of bounds