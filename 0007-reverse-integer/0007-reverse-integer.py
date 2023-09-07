class Solution:
    def reverse(self, x: int) -> int:
        '''
        - store the sign
            - check if the x < 0, if it is, set isNegative to True
        - do rem = x % 10
        - if x < 10, result += rem, return result
        - then do result += rem * 10
        - set x = x // 10
        '''
        
        result = 0
        isNeg = False
        
        if x < 0:
            isNeg = True
            
        x = abs(x)
        while x > 0:
            if x < 10:
                result = (result * 10) +  x
                break
            rem = x % 10
            x //= 10
            result = (result * 10) + rem
            
        result = result if isNeg == False else -result
        result = result if result > (math.pow(-2, 31)) and result < (math.pow(2, 31) - 1) else 0
        
        return result
        