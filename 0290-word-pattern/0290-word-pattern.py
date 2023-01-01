class Solution:
    '''
    time - O(n)
    space - O(m)
    where n is the length of pattern
    m is the number of unique words in s
    '''
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split(' ')
        if len(pattern) != len(s_arr):
            return False 
            
        pattern_map = {}
        s_map = {}
    
        for i in range(len(pattern)):
            pattern_val = pattern[i]
            s_val = s_arr[i]

            if not pattern_val in pattern_map:
                pattern_map[pattern_val] = s_val
            if not s_val in s_map:
                s_map[s_val] = pattern_val
            if pattern_map[pattern_val] != s_val or s_map[s_val] != pattern_val:
                return False

        return True