public class Solution {
    //time - O(m*n)
    //space - O(m*n)
    private List<int[]> directions = new(){new int[]{-1,0}, new int[]{0,1}, new int[]{1,0}, new int[]{0,-1}};
    public void Solve(char[][] board) {
        int row = board.Length;
        int col = board[0].Length;

        for(int i = 0; i < col; i++) { //O(n)
            if(board[0][i] == 'O') {
                dfs(0, i, board); //O(m*n)
            }
            if(board[row - 1][i] == 'O') {
                dfs(row - 1, i, board); //O(1)
            }
        }

        for(int j = 0; j < row; j++) { //O(m)
            if(board[j][0] == 'O') {
                dfs(j, 0, board); //O(1)
            }
            if(board[j][col - 1] == 'O') {
                dfs(j, col - 1, board);
            }
        }

        for(int i = 0; i < row; i++) {
            for(int j = 0; j < col; j++) {
                if(board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if(board[i][j] == 'Z') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    private void dfs(int row, int col, char[][] board) {
        if(row < 0 || row >= board.Length || col < 0 || col >= board[0].Length || board[row][col] != 'O') {
            return;
        }
        board[row][col] = 'Z';
        foreach(var direction in directions) {
            int nextRow = row + direction[0];
            int nextCol = col + direction[1];
            dfs(nextRow, nextCol, board);
        }
        return;
    }
}

// [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]

//if i see a cell that can be flipped, don't flip yet, just store it
//have  visited array

//if a zero doesn't have a top and bottom as x, we can't flip

/*
//traverse through the borders basically and mark 0s that should not be flipped
//second iteration - if you see my mark, convert to O else if it's o, convert to x
*/