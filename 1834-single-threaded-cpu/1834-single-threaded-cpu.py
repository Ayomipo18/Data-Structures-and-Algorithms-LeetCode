class Solution:
    '''
    time - O(nlogn)
    space - O(n)
    '''
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()
        
        ans, min_heap, time, i = [], [], tasks[0][0], 0
        
        while i < n or min_heap:
            while i < n and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not min_heap:
                time = tasks[i][0]
            else:
                process_time, index = heapq.heappop(min_heap)
                ans.append(index)
                time += process_time

        return ans