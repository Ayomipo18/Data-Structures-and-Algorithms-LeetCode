public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        int[] result = new int[k];
        PriorityQueue<int, int> pQueue = new PriorityQueue<int, int>();
        Dictionary<int, int> dictionary = new Dictionary<int, int>();
        
        for(int i = 0; i < nums.Length; i++) {
            if(dictionary.ContainsKey(nums[i]) == true) {
                dictionary[nums[i]]++;
            } else {
                dictionary.Add(nums[i], 1);
            }
        }
        
        foreach(KeyValuePair<int, int> element in dictionary) {
            pQueue.Enqueue(element.Key, -element.Value);
        }
        
        for(int i = 0; i < k; i++) {
            result[i] = pQueue.Dequeue();
        }
        
        return result;
    }
}