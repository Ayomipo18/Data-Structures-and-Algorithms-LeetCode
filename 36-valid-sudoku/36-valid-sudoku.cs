public class Solution {
    //time - O(n^2)
    //space - O(n^2)
    public bool IsValidSudoku(char[][] board) {
        HashSet<char>[] rows = new HashSet<char>[9];
        HashSet<char>[] cols = new HashSet<char>[9];
        HashSet<char>[] subBoxes = new HashSet<char>[9];

        
        for(int i = 0; i < board.Length; i++) {
            HashSet<char> row = new();
            HashSet<char> col = new();
            HashSet<char> subBox = new();
            rows[i] = row;
            cols[i] = col;
            subBoxes[i] = subBox;
        }

        for(int i = 0; i < board.Length; i++) {
            for(int j = 0; j < board[0].Length; j++) {
                char cell = board[i][j];
                if(cell != '.') {
                    int subBoxIndex = (Convert.ToInt32(i / 3) * 3) + (Convert.ToInt32(j / 3) * 1);
                    if(rows[i].Contains(cell) || cols[j].Contains(cell) || subBoxes[subBoxIndex].Contains(cell)) {
                        return false;
                    }
                    rows[i].Add(cell);
                    cols[j].Add(cell);
                    subBoxes[subBoxIndex].Add(cell);
                }
            }
        }
        return true;
    }
}

//if i see a ., continue
//hashset for each row, col and sub box
//List<hashset> rows
//List<hashset> cols
//List<hashset> subboxes
//rows[0].Contain
//if col 3 - 5
//col 3 / 3 level = 1 * 1, 2 * 1
//row 3 / 3 level  = 1 * 3 , 2 * 3