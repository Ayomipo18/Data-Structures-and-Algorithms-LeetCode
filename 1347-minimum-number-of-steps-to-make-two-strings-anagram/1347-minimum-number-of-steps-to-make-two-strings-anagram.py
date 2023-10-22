class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_map = {}
        count = 0
        
        for val in s:
            if val not in char_map:
                char_map[val] = 0
            char_map[val] += 1
            
        for val in t:
            if val not in char_map or char_map[val] < 1:
                count += 1
            else:
                char_map[val] -= 1
            
        return count