public class Solution {
    public int ShortestPathLength(int[][] graph) {
        if(graph.Length == 1) return 0;
        
        int finalState = (1 << graph.Length) - 1;
        
        Queue<int[]> queue =  new Queue<int[]>();
        
        for(int i = 0; i < graph.Length; i++) {
            queue.Enqueue(new int[] {i, 1 << i});
        } // O(n) - time; O(n) - space where n is the number of nodes, which is also the graph length
        
        int[,] visited = new int[graph.Length, finalState + 1]; // O(n^2) - space
        
        int shortestPath = 0;
        
        while(queue.Count > 0) {
            int size = queue.Count; // 4
            shortestPath++; // 1
            for(int i = 0; i < size; i++) { //O(n + edges)
                int[] head = queue.Dequeue(); // [[0, 1]]
                int nodeId = head[0];
                int visitedNodeBitState = head[1];
                
                foreach(int neighbour in graph[nodeId]) {
                    int newVisitedNodeBitState = visitedNodeBitState | (1 << neighbour); //1 | 2^1 = 3
                    if(visited[neighbour, newVisitedNodeBitState] == 1) continue;
                    visited[neighbour, newVisitedNodeBitState] = 1;
                    if(newVisitedNodeBitState == finalState) return shortestPath;
                    queue.Enqueue(new int[]{neighbour, newVisitedNodeBitState});
                }
            }
        }
        
        return -1;
    }
}