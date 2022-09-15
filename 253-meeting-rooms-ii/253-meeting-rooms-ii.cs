public class Solution {
    //where n = intervals.Length
    //time - O(nlogn)
    //space - O(n)
    public int MinMeetingRooms(int[][] intervals) {
        Array.Sort(intervals, (a,b) => a[0].CompareTo(b[0]));
        PriorityQueue<int, int> pq = new();
        int count = 1;
        pq.Enqueue(intervals[0][1], intervals[0][1]);
        for(int i = 1; i < intervals.Length; i++) {
            int prevEndTime = pq.Dequeue();
            int currStartTime = intervals[i][0];
            int currEndTime = intervals[i][1];
            if(currStartTime < prevEndTime) {
                count++;
                pq.Enqueue(prevEndTime, prevEndTime);
            }
            pq.Enqueue(currEndTime, currEndTime);
        }
        return count;
    }
}

//so we are basically concerned with each end time of prev and starting time of current
//create a min heap [8,12]
//count = 1
//push 4 into it
//start for loop at 1
    //prev = pq.dequeue //4
    //      7             < 4
    //if curr value start < prev count++ //2
        //push prev into heap also
    //push end time into heap

//return count;

//create a min heap [20,30]
//count = 1
//push 30 into it
//start for loop at 1
    //prev = pq.dequeue //10
    //      15             < 10
    //if curr value start < prev count++ //2
        //push prev into heap also
    //push end time into heap

//return count;