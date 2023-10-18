class Solution:
    def numTrees(self, n: int) -> int:
        '''
        so numTrees will calculate the tress from base which are 0 and 1, then expand all the way with formular
        numTrees[x] = numTrees[left] * numTrees[right]
        '''
        numTrees = [1] * (n + 1)
        
        for node in range(2, n+1):
            total = 0
            for root in range(1, node+1):
                left = root - 1
                right = node - root
                total += numTrees[left] * numTrees[right]
            numTrees[node] = total
            
        return numTrees[n]