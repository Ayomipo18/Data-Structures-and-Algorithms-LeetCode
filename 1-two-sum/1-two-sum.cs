public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int, int>(); // 10, 0 10, 1
        for(int i = 0; i< nums.Length; i++){ // i 0 1
            if(dict.ContainsKey(nums[i])) return new int[]{i, dict[nums[i]]};
            if(dict.ContainsKey(target - nums[i])) continue;
            dict.Add(target - nums[i], i);
        }
        return new int[2];
    }
}

//[1,2,3,4] t=6
//output array
//for(int i = 0; i< nums.Length; i++)
//i = 0 nums[i] = 3
//for(int j = i + 1; j < nums.Length; j++)
//j = 1 nums[j] = 3
//if(nums[i] + nums[j] == t) return new int[]{i,j};
//return new int[2];