class Solution:
    def romanToInt(self, s: str) -> int:
        symbols_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        
        for i in range(1, len(s)):
            if symbols_map[s[i]] > symbols_map[s[i-1]]:
                result -= symbols_map[s[i-1]]
            else:
                result += symbols_map[s[i-1]]
                
        return result + symbols_map[s[len(s)-1]]