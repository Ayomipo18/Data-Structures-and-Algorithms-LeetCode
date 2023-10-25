class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        - get the diff of costTocityB - costToCityA
        - store this diff and store the original values of both array
        - [[10,10,20],[170,30,200],[-350,400,50],[-10,30,20]]
        - sort by the first value
        - [[-350,400,50],[-10,30,20],[10,10,20],[170,30,200]]
        - then pick first n for B
        - then the remaining n values for A
        n = len(costs)
        time - O(nlogn)
        space - O(n)
        '''
        
        diffs = []
        #O(n)
        for c1, c2 in costs:
            diffs.append([c2-c1, c1, c2])
            
        #O(nlogn)
        diffs.sort(key = lambda x:x[0])
        res = 0
        #O(n)
        for i in range(len(diffs)):
            if i >= len(diffs)//2:
                res += diffs[i][1]
            else:
                res += diffs[i][2]
            
        return res
        
        