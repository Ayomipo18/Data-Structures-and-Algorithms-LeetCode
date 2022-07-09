public class Solution {
    public int MaxResult(int[] nums, int k) {
        int[] dp = new int[nums.Length];
        var queue = new PriorityQueue<int, int>(Comparer<int>.Create((x,y) => y.CompareTo(x)));
        
        dp[0] = nums[0];
        
        queue.Enqueue(0, dp[0]);
        
        for(int i = 1; i < nums.Length; i++) {
            while(queue.Count > 1 && i - queue.Peek() > k) queue.Dequeue();
            dp[i] = nums[i] + dp[queue.Peek()];
            queue.Enqueue(i, dp[i]);
        }
        
        return dp[nums.Length - 1];
    }
}