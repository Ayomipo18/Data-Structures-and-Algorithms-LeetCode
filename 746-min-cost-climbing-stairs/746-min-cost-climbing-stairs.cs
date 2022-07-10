public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        
        if(cost.Length == 1) return cost[0];
            
        int dpPrev = cost[0];
        int dpCurr = cost[1];
        
        for(int i = 2; i < cost.Length; i++) {
            int temp = dpCurr;
            dpCurr = Math.Min(dpCurr, dpPrev) + cost[i];
            dpPrev = temp;
        }
        
        return Math.Min(dpCurr, dpPrev);
    }
}