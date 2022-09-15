public class Solution {
    
    //time - O(nlogn)
    //space - O(1)
    public bool CanAttendMeetings(int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
        for(int i = 1; i < intervals.Length; i++) {
            if(intervals[i][0] < intervals[i - 1][1]) {
                return false;
            }
        }
        return true;
    }
}

//solution 1
//sort by starting time
//then do a for loop through the intevals, start at index 1
//if curr start time < prev end time, return false