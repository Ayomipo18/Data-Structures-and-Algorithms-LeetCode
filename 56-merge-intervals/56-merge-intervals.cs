public class Solution {
    public int[][] Merge(int[][] intervals) {
        //time - O(nlogn)
        //space - O(logn) or O(1)
        List<int[]> result = new();

        Array.Sort(intervals, (a,b) => a[0].CompareTo(b[0]));
        result.Add(intervals[0]);

        for(int i = 1; i < intervals.Length; i++) {
            int length = result.Count;
            int prevEnd = result[length - 1][1];
            if (prevEnd >= intervals[i][0]) {
                result[length - 1][1] = Math.Max(prevEnd, intervals[i][1]);
            } else {
                result.Add(intervals[i]);
            }
        }

        return result.ToArray();
    }
}

//[[1,3],[2,6], [5, 6], [8,10],[15,18] [2,5]]
//[1,6] [8,10] [10,15]
//[[1,3], [2,5], [2,6], [5, 6], [8,10],[15,18]]

//sort array by first index
//add array[0] to stack
//stack = [[1,6], [8,10], [15,18]]

// result = [[1, 3]]
//loop thru array, i = 1 -> 2 -> 3
//peek at the top value in my stack, is it the 2nd index value >= my currArray[i][1] value
    //yes? pop from my stack and push 1, max of two values i am comparing
    //push the curr value into stack;

//whule stack.length > 0, pop all the values and  add it to my result array.