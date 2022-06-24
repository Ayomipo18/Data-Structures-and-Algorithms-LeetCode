public class Solution {
    public string[] FindRelativeRanks(int[] score) {
        
        // build max=heap
        var pq = new PriorityQueue<int, int>();
        foreach(var s in score) {
            pq.Enqueue(s, -s);
        }
        
        Hashtable sortedTable = new Hashtable();
        int index =1;
        while(pq.Count>0) {
            int highest = pq.Dequeue();
            sortedTable.Add(highest, index);
            index++;
        }

        
        var res = score.ToList().Select(s => {
            var place = (int)sortedTable[s];
            if(place == 1) {
                return "Gold Medal";
            } else if(place ==2) {
                return "Silver Medal";
            } else if(place == 3) {
                return "Bronze Medal";
            } else return $"{place}";
        }).ToArray();
        return res;
    }
}