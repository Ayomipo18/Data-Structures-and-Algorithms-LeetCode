class Solution:
    '''
    - Initialy, the idea is
    - start from time 1, if the task at the moment is at the time to process it and computer is idle, then i process it
    - [[1,2],[2,4],[3,2],[4,1]]
    - time - 1 -> 2 -> 3 -> 4 -> 5 -> 6
    - [[1,2],[8,4],[9,2],[10,1]]
    - time1 - 1 -> 8 -> 9 -> 10
    - to_process = [2(2), 3(1)]
    - CPU1 - 0(1-3) -> 1(8-12)
    - CPU - 0(1-3) -> 2(3-5) -> 3(5-6) -> 1(6-10)
    [(2,0)]
    - time - O(nlogn)
    - space - O(nlogn)
    '''
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result, minHeap = [], []
        
        for i, task in enumerate(tasks):
            task.append(i)
        
        tasks.sort(key = lambda x : x[0])
        
        i, time = 0, tasks[0][0]
        
        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
                
            if not minHeap:
                time = tasks[i][0]
            else:
                proc_time, index = heapq.heappop(minHeap)
                result.append(index)
                time += proc_time
                
        return result