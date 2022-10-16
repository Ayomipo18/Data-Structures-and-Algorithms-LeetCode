class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = [0] * 60
        count = 0
        
        for val in time:
            remainder[val % 60] += 1
            
        for i in range(1, 30):
            count += remainder[i] * remainder[60 - i]
        
        if remainder[0] > 0:
            count += (remainder[0] * (remainder[0] - 1)) // 2
    
        if remainder[30] > 0:
            count += (remainder[30] * (remainder[30] - 1)) // 2
        
        return count