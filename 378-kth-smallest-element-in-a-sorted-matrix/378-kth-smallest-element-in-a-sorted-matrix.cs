public class Solution {
    public int KthSmallest(int[][] matrix, int k)
    {
        if (matrix == null) return 0;

        int row = matrix.Length;
        int col = matrix[0].Length;
        int left = matrix[0][0];
        int right = matrix[row - 1][col - 1];

        while (left < right)
        {
            int mid = left + (right - left) / 2;
            int count = 0;

            for (int i = 0; i < row; i++)
                for (int j = col - 1; j >= 0; j--)
                    if (matrix[i][j] <= mid)
                        count++;

            if (count < k)
                left = mid + 1;
            else
                right = mid;
        }

        return left;
    }
}