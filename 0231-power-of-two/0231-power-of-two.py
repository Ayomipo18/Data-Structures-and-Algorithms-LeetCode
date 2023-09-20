class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n_initial = n
        n = abs(n)
        if n_initial == 0: 
            return False
        if n_initial == 1:
            return True
        
        
        rem = 0
        while n > 1 and rem < 1:
            rem = n % 2
            n = n // 2
            
        return True if rem == 0 and n_initial > 0 else False