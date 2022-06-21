public class Solution {
    public int FurthestBuilding(int[] heights, int bricks, int ladders) {
        //minheap
        PriorityQueue<int, int> pQueue = new PriorityQueue<int, int>();
        
        int difference;
        
        for(int i = 0; i < heights.Length-1; i++) {
            
            difference = heights[i+1] - heights[i];
            
            if(difference <= 0) continue;
            
            pQueue.Enqueue(difference, difference);
            
            if(pQueue.Count > ladders) bricks -= pQueue.Dequeue();
            
            if(bricks < 0) return i;
        }
        
        return heights.Length-1;
    
        //reverse minheap(maxheap strategy)
//         PriorityQueue<int, int> pQueue = new PriorityQueue<int, int>();

//         int difference;

//         for(int i = 0; i < heights.Length-1; i++) {

//             difference = heights[i+1] - heights[i];
            
//             if(difference <= 0) continue;
                
//             bricks -= difference;

//             pQueue.Enqueue(difference, -difference);

//             if(bricks < 0) {
//                 bricks += pQueue.Dequeue();
//                 if(ladders > 0) ladders--;
//                 else return i;
//             }
//         }

//         return heights.Length-1;
    }
}