class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        time - O(n)
        space - O(n)
        where n is the length of string s
        '''
        if len(s) == 0:
            return 0
        
        l = 0
        count = 1
        char_set = set()
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.discard(s[l])
                l += 1
            
            char_set.add(s[r])
            count = max(count, r-l+1)
                
        return count