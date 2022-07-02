public class Solution {
    public int MaxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        
        long maxHeight = 0, maxWidth = 0, lastCutIndex = 0;
        
        Array.Sort(horizontalCuts);
        Array.Sort(verticalCuts);
        
        for(int i = 0; i < horizontalCuts.Length; i++) {
            maxHeight = Math.Max(maxHeight, horizontalCuts[i] - lastCutIndex);
            lastCutIndex = horizontalCuts[i];
        }
        maxHeight = Math.Max(maxHeight, h - lastCutIndex);
        
        lastCutIndex = 0;
        for(int i = 0; i < verticalCuts.Length; i++) {
            maxWidth = Math.Max(maxWidth, verticalCuts[i] - lastCutIndex);
            lastCutIndex = verticalCuts[i];
        }
        maxWidth = Math.Max(maxWidth, w - lastCutIndex);

        return (int)(maxHeight * maxWidth % 1000000007);
    }
}