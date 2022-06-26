public class Solution {
    public int MaxScore(int[] cardPoints, int k) {
        int sum = 0, max = 0;
        
        if( cardPoints.Length == k) {
            foreach(int point in cardPoints) {
                max += point;
            }
            return max;
        }
        
        for(int i = 0; i< k; i++) {
            sum += cardPoints[i];
        }
        
        max = sum;
        
        int left = k-1, right = cardPoints.Length-1;
        
        for(int i = left; i >= 0; i--) {
            sum -= cardPoints[i];
            sum += cardPoints[right];
            right--;
            max = Math.Max(max, sum);
        }
        
        return max;
    }
}