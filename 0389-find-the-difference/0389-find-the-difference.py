class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = {}
        
        for val in s:
            if val not in s_map:
                s_map[val] = 0
            s_map[val] += 1
            
        for val in t:
            if val not in s_map or s_map[val] < 1:
                return val
            s_map[val] -= 1
            
        return ""