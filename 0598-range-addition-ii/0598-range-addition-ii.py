class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row, min_col = m, n
        
        for r,c in ops:
            min_row, min_col = min(min_row, r), min(min_col, c)
        return min_row * min_col