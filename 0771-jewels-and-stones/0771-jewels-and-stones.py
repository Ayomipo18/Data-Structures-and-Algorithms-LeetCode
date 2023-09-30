class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_map = {}
        result = 0
        
        for val in stones:
            if val not in stones_map:
                stones_map[val] = 0
            stones_map[val] += 1
            
        for val in jewels:
            if val in stones_map:
                result += stones_map[val]
                
        return result