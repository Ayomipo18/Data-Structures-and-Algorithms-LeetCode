public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.Length - 1;
        int firstPos;
        int lastPos;
        
        firstPos = BinarySearchLeft(nums, left, right, target);
        lastPos = BinarySearchRight(nums, left, right, target);
        
        int[] result = new int[]{firstPos, lastPos};
        return result;
    }
    
    public int BinarySearchLeft(int[] nums, int left, int right, int target) {
        int index = -1;
        while(left <= right) {
            int middle = (left + right)/2;
            if(nums[middle] == target) {
                index = middle;
                right = middle - 1;
            }
            else if(nums[middle] < target) left = middle + 1;
            else right = middle - 1;
        }
        return index;
    }
    
    public int BinarySearchRight(int[] nums, int left, int right, int target) {
        int index = -1;
        while(left <= right) {
            int middle = (left + right)/2;
            if(nums[middle] == target) {
                index = middle;
                left = middle + 1;
            }
            else if(nums[middle] > target) right = middle - 1;
            else left = middle + 1;
        }
        return index;
    }
}