// public class Solution {
//     public bool SearchMatrix(int[][] matrix, int target) {
//         int row = 0;
//         int col = matrix[0].Length-1;
        
//         while(col >= 0 && row < matrix.Length) {
//             if(matrix[row][col] == target) return true;
//             else if(matrix[row][col] > target) col--;
//             else if(matrix[row][col] < target) row++;
//         }
        
//         return false;
        
//     }
// }

public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        foreach(int[] arr in matrix) {
            if(binarySearch(arr, target)) return true;
        }
        
        return false;
    }
    
    public bool binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.Length-1;
        while(left <= right) {
            int middle = (left + right)/2;
            if(arr[middle] == target) return true;
            else if(arr[middle] > target) right = middle-1;
            else if(arr[middle] < target) left = middle+1;
        }
        return false;
    }
    
}