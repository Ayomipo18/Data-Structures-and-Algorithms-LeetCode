public class Solution {
    public int FindPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        Dictionary<(int Row, int Col, int Moves), int> memo = new ();
        int mod = 1000000007;
        
        return Solve(startRow, startColumn, 0);
        
        int Solve(int row, int col, int move) {
            if (move > maxMove) return 0;
            if (row < 0 || row >= m || col < 0 || col >= n) return 1;
            if (memo.TryGetValue((row, col, move), out var memoizedResult)) return memoizedResult;
            
            int up = Solve(row - 1, col , move + 1), right = Solve(row, col + 1, move + 1), down = Solve(row + 1, col, move + 1), left = Solve(row, col - 1, move + 1);
            int res = (((up + right) % mod) + ((down + left) % mod)) % mod;
            memo[(row, col, move)] = res;
            return res;
        }
    }
}