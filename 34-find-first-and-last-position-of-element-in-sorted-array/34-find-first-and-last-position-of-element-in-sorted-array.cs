public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int[] result = new int[]{-1, -1};
        
        if(nums.Length == 0) return result;
        
        int firstPos;
        int lastPos;
        
        firstPos = BinarySearch(nums, target, 'l');
        
        if(firstPos == -1) {
            return result;
        }
        
        lastPos = BinarySearch(nums, target, 'r');
        
        result[0] = firstPos;
        result[1] = lastPos;
        
        return result;
    }
    
    public int BinarySearch(int[] nums, int target, char type) {
        int left = 0;
        int right = nums.Length - 1;
        int index = -1;
        
        while(left <= right) {
            int middle = (left + right)/2;
            if(nums[middle] == target) {
                index = middle;
                if(type == 'l') {
                    right = middle - 1;
                } else {
                    left = middle + 1;
                }
            }
            else if(nums[middle] < target) left = middle + 1;
            else right = middle - 1;
        }
        
        return index;
    }
}