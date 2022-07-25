public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.Length - 1;
        int firstPos;
        int lastPos;
        int leftPos = -1;
        int rightPos = -1;
        int partitionIndex = -1;
        
        while(left <= right) {
            int middle = (left + right)/2;
            if(nums[middle] == target) {
                partitionIndex = middle;
                break;
            }
            else if(nums[middle] > target) right = middle - 1;
            else if(nums[middle] < target) left = middle + 1;
        }
        
        if(partitionIndex > -1) {
            leftPos = BinarySearchLeft(nums, 0, partitionIndex - 1, target);
            rightPos = BinarySearchRight(nums, partitionIndex + 1, nums.Length - 1, target);
        }
        
        firstPos = (leftPos == -1) ? partitionIndex : leftPos;
        lastPos = (rightPos == -1) ? partitionIndex : rightPos;
        
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
        }
        return (index == -1) ? -1 : index;
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
        }
        return (index == -1) ? -1 : index;
    }
}