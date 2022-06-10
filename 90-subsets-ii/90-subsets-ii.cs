public class Solution {
    public IList<IList<int>> SubsetsWithDup(int[] nums) {
        List<IList<int>> result = new List<IList<int>>();
        Array.Sort(nums);
        BackTrack(0, new List<int>());
        
        void BackTrack(int index, List<int> currArr) {
            result.Add(new List<int>(currArr));
            if(index >= nums.Length) 
                return;
            for(int i=index; i<nums.Length; i++) {
                if(i>index && nums[i-1] == nums[i])
                    continue;
                currArr.Add(nums[i]);
                BackTrack(i+1, currArr);
                currArr.Remove(nums[i]);
            }
        }
        
        return result;
    }
}