public class Solution {
    //time - O(n)
    //space - O(1)
    public int MinStartValue(int[] nums) {
        int sum = 0;
        int minValue = Int32.MaxValue;
        
        for(int i = 0; i < nums.Length; i++) {
            sum += nums[i];
            minValue = Math.Min(sum, minValue);
        }
        
        return minValue < 0 ? Math.Abs(minValue) + 1 : 1;
    }
}
