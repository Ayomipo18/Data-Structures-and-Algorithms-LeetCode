class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        - Get pattern
        - use pattern to check string
        '''
        length = len(s)
        
        for i in range(length//2, 0, -1):
            if length % i == 0:
                repeats = length // i
                sub_str = s[0:i]
                new_str = sub_str * repeats
                if new_str == s:
                    return True
                
        return False
                
    