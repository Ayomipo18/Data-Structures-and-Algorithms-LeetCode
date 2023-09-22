class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        - while t < len(t)
        - use an index to go thru s and move the index only when it maces the val in t
        - then return true if index == len(s) else false
        '''
        tIndex, sIndex = 0, 0
        
        while tIndex < len(t) and sIndex < len(s):
            if s[sIndex] == t[tIndex]:
                sIndex += 1
            tIndex += 1
                
        return True if sIndex == len(s) else False