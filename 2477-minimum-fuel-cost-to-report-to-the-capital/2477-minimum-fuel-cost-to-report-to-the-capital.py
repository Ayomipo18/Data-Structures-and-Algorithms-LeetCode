class Solution:
    '''
    {3: [1, 2], 1: [3, 0 ], 2: [3], 0: [1, 4, 5], 4: [0, 6], 5: [0], 6: [4]}
    '''
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjlist = defaultdict(list)
        self.res = 0
        for src, dst in roads:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        
        self.dfs(0, 0, adjlist, seats)
        
        return self.res
    
    def dfs(self, node, parent, adjlist, seats):
        passengers = 0
        
        for child in adjlist[node]:
            if child != parent:
                p = self.dfs(child, node, adjlist, seats)
                passengers += p
                self.res += int(ceil(p / seats))
        return passengers + 1