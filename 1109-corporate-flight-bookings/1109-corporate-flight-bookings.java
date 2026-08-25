class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        /*
        - Difference array
        - Line sweep
        - Time and Space - O(n)
        */

        int[] result = new int[n];
        int[] diffArr = new int[n+1];

        for(int i=0; i<diffArr.length; i++) {
            diffArr[i] = 0;
        }

        for(int i=0; i<bookings.length; i++) {
            int first = bookings[i][0];
            int last = bookings[i][1];
            int seat = bookings[i][2];
            diffArr[first-1] += seat;
            diffArr[last] -= seat;
        }

        int lineSweepValue = 0;

        for(int i=0; i<n; i++) {
            lineSweepValue += diffArr[i];
            result[i] = lineSweepValue;
        }

        return result;
    }
}