public class Solution {
    //time - O(n)
    //space - O(1)
    public int MinStartValue(int[] nums) {
        int sum = 0; // 0 - (-3) -  (-1) - (-4) - 0 - 2
        // 0 - 1 - 3
        int minValue = 0; //278654535467 - (-3) - (-4)
        //0
        
        for(int i = 0; i < nums.Length; i++) {
            sum += nums[i];
            minValue = Math.Min(sum, minValue);
        }
        
        return -minValue + 1;
    }
}
