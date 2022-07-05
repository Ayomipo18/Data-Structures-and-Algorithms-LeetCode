public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> hashset = new HashSet<int>(nums);
        int max = 0;
        
        for(int i = 0; i<nums.Length; i++){
            int currMax = 1;
            int currNumber = nums[i];
            if(!hashset.Contains(currNumber - 1)) {
                currNumber = nums[i] + 1;
                while(hashset.Contains(currNumber)) {
                    currMax++;
                    currNumber += 1;
                }
                max = Math.Max(max, currMax);   
            }
        }
        
        return max;
    }
}