class Solution:
    #time - O(nlogn)
    #space - O(n)
    def minGroups(self, intervals: List[List[int]]) -> int:
        from queue import PriorityQueue
        
        pq = PriorityQueue()
        
        intervals.sort(key = lambda x:x[0])
        
        for i, interval in enumerate(intervals):
            if not pq.empty() and pq.queue[0] < interval[0]:
                pq.get()
            pq.put(interval[1])
                
        return pq.qsize()
            
        #[1, 3] [4,5] [6, 8]
        #[[1,5],[5,10],[2,3],[5,10],[6,8]]