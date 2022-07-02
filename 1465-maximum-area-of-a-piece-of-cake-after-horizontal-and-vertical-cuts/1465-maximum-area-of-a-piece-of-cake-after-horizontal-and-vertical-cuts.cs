public class Solution {
    public int MaxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        
        horizontalCuts = horizontalCuts.Append(h).ToArray();
        Array.Sort(horizontalCuts);
        long maxHeight = horizontalCuts[0];
        for(int i = 1; i < horizontalCuts.Length; i++) {
            maxHeight = Math.Max(maxHeight, horizontalCuts[i] - horizontalCuts[i-1]);
        }
        
        verticalCuts = verticalCuts.Append(w).ToArray();
        Array.Sort(verticalCuts);
        long maxWidth = verticalCuts[0];
        for(int i = 1; i < verticalCuts.Length; i++) {
            maxWidth = Math.Max(maxWidth, verticalCuts[i] - verticalCuts[i-1]);
        }
        
        return (int)(maxHeight * maxWidth % 1000000007);
    }
}