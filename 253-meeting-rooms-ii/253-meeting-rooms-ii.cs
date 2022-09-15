public class Solution {
    //where n = intervals.Length
    //time - O(nlogn)
    //space - O(n)
    public int MinMeetingRooms(int[][] intervals) {
        Array.Sort(intervals, (a,b) => a[0].CompareTo(b[0])); //O(nlogn)
        PriorityQueue<int, int> pq = new();
        int count = 1;
        pq.Enqueue(intervals[0][1], intervals[0][1]);
        for(int i = 1; i < intervals.Length; i++) { //O(n)
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

//create a min heap [[0,30], [5,10], [15,20]]
//heap = [20,30]
//count = 1
//push 30 into it
//start for loop at 1
    //prev = pq.dequeue //10
    //      15             < 10
    //if curr value start < prev count++ //2
        //push prev into heap also
    //push end time into heap

//return count;