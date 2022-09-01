public class Solution {
    //time - O(n)
    //space - O(n) where n is the number of pixels
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        int row = image.Length;
        int col = image[0].Length;
        Queue<int[]> queue = new();
        bool [,] visited = new bool[row, col];
        IList<int[]> directions = new List<int[]>();
        //int[,] directions = new int[,]{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        
        queue.Enqueue(new int[]{sr, sc});
        directions.Add(new int[]{-1,0}); //up
        directions.Add(new int[]{0,1}); //right
        directions.Add(new int[]{1,0}); //down
        directions.Add(new int[]{0,-1}); //left
        
        while(queue.Count > 0) {
            int[] currCell = queue.Dequeue();
            int currRow = currCell[0];
            int currCol = currCell[1];
            int currColor = image[currRow][currCol];
            visited[currRow, currCol] = true;
            image[currRow][currCol] = color;
            
            foreach(var direction in directions) {
                int nextRow = currRow + direction[0];
                int nextCol = currCol + direction[1];
                if(nextRow < 0 || nextRow >= row || nextCol < 0 || nextCol >= col || visited[nextRow, nextCol] == true || image[nextRow][nextCol] != currColor) {
                    continue;
                }
                queue.Enqueue(new int[]{nextRow, nextCol});
            }
        }
        return image;
    }
}

//we can do dfs or bfs
//i want to do bfs
//so create a queue
//create a matrix with length image
//create directions data structure
//so push the sr and sc as the starting coordinate into the queue
//while queue.Count > 0
//dequeue the current coordinate
//set it to visited
//change it's colour
//then foreach direction in direction
    //if direction x and y is invalid, don't push into queue
    //invalid coordinates are out of bound, that coordinate color not being equal to the current Color or we have visited that coordinate previously
    //else push into queue