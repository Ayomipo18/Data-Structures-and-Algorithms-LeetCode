class Solution {
    /*
    n is the lentgh of the nums array
    Time - O(n)
    Space - O(1)
    */
    public int maxSubArray(int[] nums) {
        if (nums.length == 0) return 0;

        int current_max_sum = nums[0];
        int total_max_sum = nums[0];

        for (int i=1; i<nums.length; i++) {
            current_max_sum = Math.max(nums[i], nums[i]+current_max_sum);
            total_max_sum = Math.max(total_max_sum, current_max_sum);
        }

        return total_max_sum;
    }
}