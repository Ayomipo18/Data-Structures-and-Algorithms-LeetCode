class Solution:
    '''
    - have two pointers l, r = 0
    - have an array of length 26 or hashmap
    - while r < len(s)
    - take count of current char and put in array
    - then, check is (r - l + 1, current window)-max value in array less than k
    - if it is not, just do maxvalue result
    - else shift l
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = r = 0
        maxfreq = 0
        
        while r < len(s):
            count[s[r]] += 1
            #maxfreq = max(maxfreq, count[s[r]])
            
            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                
            # if (r-l+1) - maxfreq > k:
            #     count[s[r]] -= 1
            #     l += 1
            
            res = max(res, r-l+1)
            r += 1
        
        return res
            