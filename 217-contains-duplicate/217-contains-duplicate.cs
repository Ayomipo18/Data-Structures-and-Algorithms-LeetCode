public class Solution {
    //time - O(n)
    //space - O(n) where n = nums.Length
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> hashset = new();
        for(int i = 0; i < nums.Length; i++) {
            if(hashset.Contains(nums[i])) {
                return true;
            }
            hashset.Add(nums[i]);
        }
        return false;
    }
}

//create a hashset
//start at the first index
//if nums[index] is in the hashset, return true
//returns false by default