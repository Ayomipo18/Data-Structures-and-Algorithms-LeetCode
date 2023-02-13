class Solution:
    '''
    0, 1, 2, 3, 4, 5, 6, 7
    3, 4, 5, 6, 7
    '''
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        
        if length % 2 == 0:
            return length // 2
        else:
            return (length // 2) + (low % 2)
                