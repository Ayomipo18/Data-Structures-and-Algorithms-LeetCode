public class Solution {
    //Time complexity - O(n^2 * logn)
    //SPace - O(n+v)
    public int MinCostConnectPoints(int[][] points) {
        int length = points.Length;
        
        IList<IList<int[]>> graph = new List<IList<int[]>>();
        /*
        graph = {
        0: [[4,1], [13,2], [7,3], [7,4]]
        1: [[4,0], [9,2], [3,3], [7,4]]
        2: [[13,0], [9,1], [10,3], [14,4]]
        3: [[7,0], [3,1], [10,2], [4,4]]
        4: [[7,0], [7,1], [14,2], [4,3]]
        }
        */
        
        for(int i = 0; i < length; i++) {
            graph.Add(new List<int[]>());
        }
        
        for(int i = 0; i < length; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for(int j = i+1; j < length; j++) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                int dist = Math.Abs(x1-x2) + Math.Abs(y1-y2);
                graph[i].Add(new int[] {dist, j});
                graph[j].Add(new int[] {dist, i});
            }
        }
        
        int result = 0;
        HashSet<int> visited = new();
        PriorityQueue<int[], int> pq = new();
        pq.Enqueue(new int[]{0,0}, 0);
        
        while(visited.Count < length) {
            int[] path = pq.Dequeue();
            if(visited.Contains(path[1])) continue;
            result += path[0];
            visited.Add(path[1]);
            foreach(int[] neighbour in graph[path[1]]) {
                if(!visited.Contains(neighbour[1])) {
                    pq.Enqueue(neighbour, neighbour[0]);
                }
            }
        }
        
        return result;
    }
}