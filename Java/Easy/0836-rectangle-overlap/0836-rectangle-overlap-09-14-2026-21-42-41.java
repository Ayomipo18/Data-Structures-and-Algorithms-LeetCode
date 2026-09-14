class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        /*
        - overlapping edges , like intervals
        - basically have a start, end for each rect
        - Compare with other rect
        - if the x axis overlaps fine, else the y can't
        - rect 1 - (0, 2) (0, 2)
        - rect 2 - (1, 3) (1, 3) - true
        */

        Boolean xOverLap = Math.max(rec1[0], rec2[0]) < Math.min(rec1[2], rec2[2]);
        Boolean yOverLap = Math.max(rec1[1], rec2[1]) < Math.min(rec1[3], rec2[3]);
        return xOverLap && yOverLap;
    }
}