public class Solution {
    public int WiggleMaxLength(int[] nums) {
        
        int count = 1;
        int prevNumber;
        int prevDifference = 0;
        int difference;
        
        if(nums.Length == 1) return count;
        
        for(int i = 1; i < nums.Length; i++) {
            prevNumber = nums[i-1];
            if(nums[i] == prevNumber) continue;
            else {
                difference = nums[i] - prevNumber;
                if((difference > 0 && prevDifference <= 0) ||(difference < 0 && prevDifference >= 0)) {
                    count++;
                    prevDifference = difference;
                }
                else continue;
            }
        }
        
        return count;
    }
}