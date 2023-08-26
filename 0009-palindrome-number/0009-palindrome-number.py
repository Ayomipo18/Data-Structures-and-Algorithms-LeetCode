class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = 0
        initial_x = x
        
        while x > 0:
            rem = x % 10
            new_x = (new_x + rem) * 10 if x // 10 > 0 else (new_x + rem)
            x = x // 10
            
        return True if initial_x == new_x else False