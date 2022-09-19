public class Solution {
    //time - O(m * n)
    //space - O(m * n)
    public IList<int> SpiralOrder(int[][] matrix) {
        List<int> result = new();

        int top = 0, right = matrix[0].Length, bottom = matrix.Length, left = 0;
        /*
        //top = 0 1
        //right = 2 - 1
        bottom = 0
        left = 0
        result = [6, 9, 7]

        [[6,9,7]]
        */
        while(top < bottom && left < right) {
            for(int i = left; i < right; i++) {
                result.Add(matrix[top][i]);
            }
            top++;

            for(int i = top; i < bottom; i++) {
                result.Add(matrix[i][right-1]);
            }
            right--;

            if(top >= bottom || left >= right) {
                break;
            }

            for(int i = right-1; i >= left; i--) {
                result.Add(matrix[bottom-1][i]);
            }
            bottom--;

            for(int i = bottom-1; i >= top; i--) {
                result.Add(matrix[i][left]);
            }
            left++;
        }

        return result;
    }
}

//top = 0, right = matrix[0].length(2), bottom = 2 and left = 0
//a while loop, top <= bottom && left <= right
    //for(left to right), add every cell you see, left++
    //top++ = 1

    //for(top to bottom), add every cell you see, top++
    //right-- = 1

    //for(right to left), add every cell you see, right--
    //bottom-- = 1

    //for(bottom to top), add every cell you see, bottom++
    //left++ = 1


