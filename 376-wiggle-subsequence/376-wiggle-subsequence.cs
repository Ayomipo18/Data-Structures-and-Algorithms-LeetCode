public class Solution {
    public int WiggleMaxLength(int[] nums) {
        
        int count = 1;
        int prevDifference = 0;
        int difference;
        
        if(nums.Length == 1) return count;
        
        for(int i = 1; i < nums.Length; i++) {
            difference = nums[i] - nums[i-1];
            if((difference > 0 && prevDifference <= 0) ||(difference < 0 && prevDifference >= 0)) {
                count++;
                prevDifference = difference;
            }
        }
        
        return count;
    }
}