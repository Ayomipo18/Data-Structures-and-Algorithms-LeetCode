class Solution {
    //time - O(n)
    //Space - (1)
    public void moveZeroes(int[] nums) {
        int last_write_index = -1;
        for (int i=0; i<nums.length; i++) {
            if (nums[i] != 0) {
                last_write_index += 1;
                int temp = nums[last_write_index];
                nums[last_write_index] = nums[i];
                nums[i] = temp;
            }
        }
        return;
    }
}