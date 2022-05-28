public class Solution {
    public bool CanJump(int[] nums) {
        int jump = nums.Length-1;
        for(int i = nums.Length-2; i >= 0; i--) {
            if(i + nums[i] >= jump) jump = i;
        }
        return jump == 0;
    }
}