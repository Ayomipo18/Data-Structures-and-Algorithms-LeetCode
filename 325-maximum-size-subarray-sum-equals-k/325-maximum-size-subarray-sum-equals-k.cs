public class Solution {
    //time - O(n) where n = nums.Length
    //space - O(n)
    public int MaxSubArrayLen(int[] nums, int k) {
        int sum = 0;
        int maxLength = 0;
        int prevSum;
        Dictionary<int, int> history = new(){{sum, -1}};
        
        for(int i = 0; i < nums.Length; i++) {
            sum += nums[i];
            prevSum = sum - k;
            if(history.ContainsKey(prevSum)) {
                maxLength = Math.Max(maxLength, i - history[prevSum]);
            }
            if(!history.ContainsKey(sum)) {
                history.Add(sum, i);
            }
        }
        return maxLength;
    }
}

//sum variable
//history dictionary
//maxLength variable
//sum all the values of the array
//while summing, we basically want to check if sum - k exists in the history dictionary
//if it exists, we want to do current index - index in dictionary and update our maxLength variable if it's greater;
//then add our sum and index to history dictionary
//we do this until till the end of our array


