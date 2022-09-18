public class Solution {
    //where n = length of matrix
    //time - O(log(max - min) * n)
    //space - O(1)
    public int KthSmallest(int[][] matrix, int k)
    {
        int n = matrix.Length;
        int min = matrix[0][0];
        int max = matrix[n-1][n-1];
        
        while(min != max) { //log(max - min) * n
            int mid = min + ((max - min) / 2);
            int count = countLessOrEqual(mid, matrix);
            
            if(count < k) {
                min = mid + 1;
            } else {
                max = mid;
            }
        }
        
        return min;
    }
    
    private int countLessOrEqual(int mid, int[][] matrix) {
        int row = 0;
        int col = matrix.Length - 1;
        int count = 0;
        
        while(col >= 0 && row < matrix.Length) { //O(n)
            if(matrix[row][col] <= mid) {
                count += col + 1;
                row++;
            } else {
                col--;
            }
        }
        
        return count;
    }
}

//take middle of lowest number(cell 0, 0) and the highest number(cell n-1, n-1) in the matrix
//while(min != max)
//mid = (1 + 15) = 8 - (9+15) = 12 = (12 + 15) = 13
//start at the top right
    //while(col >= 0 && row < n)
        //col = 2 - 2 - 1 - 0 - 1
        //row = 0 - 1 - 2 - 2 - 3
        //count = 0 - 3 - 5 - 6 - //3 - 6 - 8
        //if the value we are on is less or equal to than middle, count += col + 1; row++
        //else, col--
        //return count;
//     2     8
//     6     8
//if count < k
    //left = mid + 1
//else right = mid //13 