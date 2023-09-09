class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        - carry = 0
        - go to the end of the array
        - add 1
        - if the value > 9 store rem in carry and move forward
        - all these is while inddex >= 0
        - before we resturn, check if carry > 0, if it is, add it to the front of the array
        '''
        
        index = len(digits) - 1
        carry = 0
        
        while index >= 0:
            val = digits[index] + carry
            carry = 0
            if index == (len(digits) - 1):
                val = digits[index] + 1
            if val > 9:
                carry = val // 10
                val %= 10
            digits[index] = val
            index -= 1
            
        return digits if carry == 0 else [carry] + digits