public class Solution {
    public int ShortestPathBinaryMatrix(int[][] grid) {
        if(grid == null || grid.Length == 0) return -1;
        int n = grid.Length;
        
        Queue<int[]> queue = new Queue<int[]>();
        queue.Enqueue(new int[]{0,0});
        
        if(grid[0][0] == 1) return -1;
        
        bool[,] visited = new bool[n,n];
        visited[0,0] = true;
        
        int level = 0;
        List<(int x, int y)> directions = new List<(int x, int y)>();
        directions.Add((0,1));
        directions.Add((1,1));
        directions.Add((1,0));
        directions.Add((1,-1));
        directions.Add((0,-1));
        directions.Add((-1,-1));
        directions.Add((-1,0));
        directions.Add((-1,1));
        //{{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0},{-1,1}};
        while(queue.Count > 0) {
            int count = queue.Count;
            level++;
            for(int i = 0; i < count; i++) {
                int[] curr = queue.Dequeue();
                int currX = curr[0];
                int currY = curr[1];
                if(currX == n-1 && currY == n-1) return level;
                foreach(var dir in directions) {
                    int x = currX + dir.x;
                    int y = currY + dir.y;
                    if(x < 0 || x > n-1 || y < 0 || y > n-1 || visited[x,y] || grid[x][y] > 0) continue;
                    queue.Enqueue(new int[]{x,y});
                    visited[x,y] = true;
                }
            }
        }
        
        return -1;
    }
    //so count = 1;
    //start 0,0
    //how do I go? top, diag, diag, right, down, diag, left
    //so bfs
    //queue = [[0,1],[1,0]]
    //while(queue.Count > 0)
    //dequeue = [0,1]
    //for(length of dequeue)
    //if(dequeue[i] == 0) increase path count and change it to 1;
    //if it's 1, skip it
    //how can bfs help me find shortest path
    //so basically, just check each internal array and in the first array, make sure that 0 starts from 0,0
    //and the last array, make sure the last zero is on the last right
}