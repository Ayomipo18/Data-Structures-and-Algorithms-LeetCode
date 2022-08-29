public class Solution {
    public int MinimumEffortPath(int[][] heights) {
        PriorityQueue<int[], int> pq = new();
        int[,] efforts = new int[heights.Length, heights[0].Length];
        IList<int[]> directions = new List<int[]>();
        
        pq.Enqueue(new int[]{0, 0, 0}, 0);
        directions.Add(new int[]{-1,0});
        directions.Add(new int[]{0,1});
        directions.Add(new int[]{1,0});
        directions.Add(new int[]{0,-1});
        
        for(int i = 0; i<heights.Length; i++) {
            for(int j = 0; j < heights[0].Length; j++) {
                efforts[i,j] = Int32.MaxValue;
            }
        }
        
        while(pq.Count > 0) {
            int[] min = pq.Dequeue();
            int row = min[0];
            int col = min[1];
            int dist = min[2];
            if(dist > efforts[row, col]) continue;
            if(row == heights.Length-1 && col == heights[0].Length-1) return dist;
            
            foreach(var direction in directions) {
                int nextRow = row + direction[0];
                int nextCol = col + direction[1];
                if(nextRow < 0 || nextRow > heights.Length-1 || nextCol < 0 || nextCol > heights[0].Length-1) {
                    continue;
                }
                int diff = Math.Abs(heights[row][col] - heights[nextRow][nextCol]);
                int newDist = Math.Max(dist, diff);
                if(newDist < efforts[nextRow, nextCol]) {
                    efforts[nextRow, nextCol] = newDist;
                    pq.Enqueue(new int[]{nextRow, nextCol, newDist}, newDist);
                }
            }
            
        }
        
        return 0;
    }
}

//have a min heap(min priority queue) which takes ((row, col), effort)
//have an efforts matrix with all values initialized to the max integer value
//we'll start from 0,0, check which part is minimum and follow that path
//when we get to the last cell in our heights matrix, we basically want to return the efforts in that cell

//[[1,2,2],[3,8,2],[5,3,5]]
//so we start with row = 0, col = 0, effort = 0 into the priority queue
//so we dequeue from the priority queue
//we try various direction to see which is valid
//so when we see a direction that is valid, we basically calculate the effort to get to that cell;
//effort = Math.Abs(dequeue cell value, dequeue cell value - next cell value)
//so we check if the currentEffort we have calculated is less than the cell effort in our effort matrix. if it is, we update the value of our effort matrix
//we then push both next cells into the priorityQueue

//next iteration, we dequeue from the pq
//then calculate effort for all valid paths connected to our curr Dequeue
//then push the valid paths into the pq

//so at any point, if we see that our value in the effort matrix is less than the curr Effort value we just calculated, don't update the matrix