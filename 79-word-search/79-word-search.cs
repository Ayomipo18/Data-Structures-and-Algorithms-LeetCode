public class Solution {
    public bool Exist(char[][] board, string word) {
        int index = 0;
        bool found = false;
        for(int i = 0; i < board.Length; i++) {
            for(int j = 0; j < board[0].Length; j++) {
                if(board[i][j] == word[index]) {
                    found = dfs(board, word, i, j, index);
                    if(found) return true;
                }
            }
        }
        return false;
    }
    
    public bool dfs(char[][] board, string word, int row, int col, int index) {
        if(index == word.Length) {
            return true;
        }
        if(row < 0 || row >= board.Length || col < 0 || col >= board[0].Length) {
            return false;
        }
        if(board[row][col] != word[index]) {
            return false;
        }
        board[row][col] = '.';
        bool found = dfs(board, word, row, col + 1, index + 1) ||
            dfs(board, word, row + 1, col, index + 1) ||
            dfs(board, word, row, col - 1, index + 1) ||
            dfs(board, word, row - 1, col, index + 1);
        board[row][col] = word[index];
        return found;
    }
}
