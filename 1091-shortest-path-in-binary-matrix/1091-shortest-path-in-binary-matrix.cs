public class Solution 
{
    public int ShortestPathBinaryMatrix(int[][] grid) 
    {
        int l = grid.Length;
        
        if (l == 1 && grid[0][0] == 0)
        {
            return 1;
        }
        if (grid[0][0] == 1 || grid[l - 1][l - 1] == 1)
        {
            return -1;
        }
        
        grid[0][0] = 1;
        int res = 1;
        
        Queue<int[]> q = new();
        q.Enqueue(new int[]{0, 0});
        
        int[][] dirs = new int[8][]
        {
            new int[]{1, 0},
            new int[]{-1, 0},
            new int[]{0, 1},
            new int[]{0, -1},
            new int[]{-1, -1},
            new int[]{-1, 1},
            new int[]{1, -1},
            new int[]{1, 1}
        };
        
        while (q.Count != 0)
        {
            int size = q.Count;
            res ++;
            
            for (int i = 0; i < size; i ++)
            {
                int[] curr = q.Dequeue();
                
                foreach (int[] dir in dirs)
                {
                    int x = curr[0] + dir[0];
                    int y = curr[1] + dir[1];
                    
                    if (x < 0 || x >= l || y < 0 || y >= l || grid[x][y] == 1)
                    {
                        continue;
                    }
                    if (x == l - 1 && y == l - 1)
                    {
                        return res;
                    }
                    
                    q.Enqueue(new int[]{x, y});
                    
                    grid[x][y] = 1;
                }
            }
        }
        
        return -1;
    }
}