public class Solution {
    //time - O(m+n)
    //space - O(1)
    public bool SearchMatrix(int[][] matrix, int target) {
        int row = 0;
        int col = matrix[0].Length - 1;
        
        while(row < matrix.Length && col >= 0) {
            if(matrix[row][col] == target) return true;
            else if(matrix[row][col] < target) {
                row++;
            } else {
                col--;
            }
        }
        
        return false;
    }
}

// public class Solution {
//time - O(mlogm)
//space - O(1)
//     public bool SearchMatrix(int[][] matrix, int target) {
//         foreach(int[] arr in matrix) {
//             if(binarySearch(arr, target)) {
//                 return true;
//             }
//         }
//         return false;
//     }
    
//     private bool binarySearch(int[] arr, int target) {
//         int start = 0;
//         int end = arr.Length;
//         while(start <= end) {
//             int mid = (start + end) / 2;
//             if(arr[mid] == target) return true;
//             else if(arr[mid] < target) {
//                 start = mid + 1;
//             } else {
//                 end = mid - 1;
//             }
//         }
//         return false;
//     }
// }

//1st solution, start from the last col and first row(number 15)
//if the value at that cell is == target , return
//else if(cell < target) row++
//else if(cell > target) col--

//2nd solution, do binary search on each row, if any returns true, rteurn true else return false