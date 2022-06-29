public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        
        Dictionary<int, int> dictionary = new Dictionary<int, int>();
        
        for(int i = 0; i < nums.Length; i++) {
            if(dictionary.ContainsKey(nums[i]) && (i - dictionary[nums[i]]) <=k ) {
                return true;
            }
            dictionary[nums[i]] = i;
        }
        
        return false;
    }
}