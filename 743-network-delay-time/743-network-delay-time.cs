public class Solution {
    public int NetworkDelayTime(int[][] times, int n, int k) {
        var dict = new Dictionary<int, List<(int child, int time)>>();
        var visited = new HashSet<int>();
        var pQueue  = new PriorityQueue<(int node, int time), int>();
        int totalTime = 0;
        
        for(int i = 0; i < times.Length; i++) {
            if(!dict.ContainsKey(times[i][0])) {
                dict.Add(times[i][0], new List<(int child, int time)>());
            }
            
            dict[times[i][0]].Add((times[i][1], times[i][2]));
        }
        
        if(!dict.ContainsKey(k)) {
            return -1;
        }
            
        pQueue.Enqueue((k, 0), 0);
        
        while(pQueue.Count != 0) {
            var minNode = pQueue.Dequeue();
            if (visited.Contains(minNode.node)) continue;
            totalTime = Math.Max(minNode.time, totalTime);
            n--;
            if(dict.ContainsKey(minNode.node)) {
                foreach(var node in dict[minNode.node]) {
                    pQueue.Enqueue((node.child, minNode.time + node.time), minNode.time + node.time);
                }
            }
            visited.Add(minNode.node);
        }
        
        return n==0 ? totalTime : -1;
    }
}