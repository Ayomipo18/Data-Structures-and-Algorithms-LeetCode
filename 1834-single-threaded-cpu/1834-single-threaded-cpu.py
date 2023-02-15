class Solution:
    '''
    - [[1,2,0], [2,4,1], [3,2,2], [4,1,3]]
    - i = 0 -> 1 -> 2 -> 3
    - time = 1 -> 3 -> 6 -> 7 -> 11
    - pq = []
    - CPU = [0, 2, 3, 1]
    - create the task and add their indexes
    - sort the tasks
    - go thru the tasks and take the current i
    - time = tasks[0][0]
    - while tasks[0][0] >= time:
        - append tasks that are available for processing to pqueue
        - we are sorting by processingtime
    - There are two things,
        - if there's something in our queue, meaning there's something up for processing, so pick the one with min processing time
        - else if there's nothing there, pick the next time and set it as the next time.
        time - O(nlogn)
        space - O(n)
        where n is the length of tasks array
    '''
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        minHeap = []
    
        for index, task in enumerate(tasks):
            task.append(index)
            
        tasks.sort()
        i = 0
        time = tasks[0][0]
        
        while i < len(tasks) or minHeap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
                    
            if minHeap:
                proc_time, index = heapq.heappop(minHeap)
                time += proc_time
                res.append(index)
            else:
                time = tasks[i][0]
                
        return res