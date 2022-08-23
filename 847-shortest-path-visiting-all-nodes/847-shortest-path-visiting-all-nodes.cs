public class Solution {
    //Time - O(number of nodes^2 * 2^number of nodes)
    //Space - O(number of nodes * 2^number of nodes)
    public int ShortestPathLength(int[][] graph) {
        if(graph.Length == 1) return 0;
        
        int finalState = (1 << graph.Length) - 1; // 1 << 4 = 16 - 1 = 15
        
        Queue<int[]> queue =  new Queue<int[]>(); //[]
        
        for(int i = 0; i < graph.Length; i++) {
            queue.Enqueue(new int[] {i, 1 << i}); //[[0,1], [1,2], [2,4], [3,8]]
        } // O(n) - time; O(n) - space where n is the number of nodes, which is also the graph length
        
        int[,] visited = new int[graph.Length, finalState + 1]; // O(n * 2^n) - space visited = int[4, 16]
        
        int shortestPath = 0; // 0
        
        while(queue.Count > 0) { // 6
            int size = queue.Count; // 6
            shortestPath++; // 2
            for(int i = 0; i < size; i++) { //O(n + edges) i(0 -> 1 -> 2 -> 3)
                int[] head = queue.Dequeue(); // [0,1] [1,2] [2,4] [3,8] [1,3] [2,5] [3,9] [0,3]
                int nodeId = head[0]; // 0 1 2 3 1 2 3 0
                int visitedNodeBitState = head[1]; // 1 2 4 8 3 5 9 3
                
                //              1            [1,2,3] -> [0,1]
                //              2            [1,2,3] -> [0,1]
                //              3            [1,2,3] -> [0,1]
                //              0            [0] -> [1,2]
                //              0            [0] -> [2,4]
                //              0            [0] -> [3,8]
                //              0            [0] -> [1,3]
                //              0            [0] -> [2,5]
                //              0            [0] -> [3,9]
                //              1            [1,2,3] -> [0,3]
                //              2            [1,2,3] -> [0,3]
                foreach(int neighbour in graph[nodeId]) {
                    //          3                   1                |      2^1
                    //          5                   1                |      2^2(5)
                    //          9                   1                |      2^3(8)
                    //          3                   2                |      2^0(1)
                    //          5                   4                |      2^0(1)
                    //          9                   8                |      2^0(1)
                    //          3                   3                |      2^0(1) -> [1,3]
                    //          5                   5                |      2^0(1) -> [2,5]
                    //          9                   9                |      2^0(1) -> [3,9]
                    //          3                   3                |      2^1(2) -> [0,3]
                    //          7                   3                |      2^2(4) -> [0,3]
                    int newVisitedNodeBitState = visitedNodeBitState | (1 << neighbour);
                    //visited[1,3]
                    //visited[2,5]
                    //visited[3,9]
                    //visited[0,3]
                    //visited[0,5]
                    //visited[0,9]
                    //visited[0,3] yes continue
                    //visited[0,5] yes continue
                    //visited[0,9] yes continue
                    //visited[1,3] yes continue
                    //visited[2,7]
                    if(visited[neighbour, newVisitedNodeBitState] == 1) continue;
                    //visited[1,3] = 1
                    //visited[2,5] = 1
                    //visited[3,9] = 1
                    //visited[0,3] = 1
                    //visited[0,5] = 1
                    //visited[0,9] = 1
                    //visited[2,7] = 1
                    visited[neighbour, newVisitedNodeBitState] = 1;
                    //3 == 15 ? no
                    //5 == 15 ? no
                    //9 == 15 ? no
                    //3 == 15 ? no
                    //5 == 15 ? n0
                    //9 == 15 ? no
                    //7 == 15 ? no
                    if(newVisitedNodeBitState == finalState) return shortestPath;
                    //[[0, 5], [0,9], [2,7]]
                    queue.Enqueue(new int[]{neighbour, newVisitedNodeBitState});
                }
            }
        }
        
        return -1;
    }
}