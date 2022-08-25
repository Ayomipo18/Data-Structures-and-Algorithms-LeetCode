public class Solution {
    public string Convert(string s, int numRows) {
        if(numRows == 1) return s;
        StringBuilder sb = new();
        int steps = (numRows - 1) * 2;

        for(int row = 0; row < numRows; row++) {
            int index = row;

            while(index < s.Length) {
                sb.Append(s[index]);
                int tempStep = (numRows - (row + 1)) * 2;
                int tempIndex = index + tempStep;
                if(row > 0 && row < numRows-1 && tempIndex < s.Length) {
                sb.Append(s[tempIndex]);
                }
                index += steps;
            }
        }

        return sb.ToString();
    }
}