'''
time complexity - O(nlogn)
space complexity - O(n)
'''
class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        
    def union(self, x, y):
        pX, pY = self.find(x), self.find(y)
        self.parents[pY] = pX
        
    def find(self, val):
        if self.parents[val] == val:
            return val
        self.parents[val] = self.find(self.parents[val])
        return self.parents[val]
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n+1)
        
        for edge in edges:
            if dsu.find(edge[0]) == dsu.find(edge[1]):
                return edge
            dsu.union(edge[0], edge[1])
            
        return [0,0]