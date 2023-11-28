class Solution:
    def decodeString(self, s: str) -> str:
        '''
        - have a stack to store your useful values (all letters of the alphabet, [, digits) 
        - if i see an end bracket in my string, that's a cue to go to my stack and process the characters until i see [
        - then gather all the digits after and multiply by the string processed.
        - push the procesed string back into the stack.
        
        For, s = 10[ab10[cd]]10[ef], 
        Time complexity would be roughly equivalent to 10∗cd∗10∗ab+10∗2 = 10^2∗2
        Hence, for an encoded pattern of form maxK[nmaxK[n]], the time complexity to decode the pattern can be given as, O((maxK^countK)⋅n)
        
        Space Complexity: O(sum((maxK^countK)⋅n)), where maxK is the maximum value of k, countK is the count of nested k values and n is the maximum length of encoded string.
        The maximum stack size would be equivalent to the sum of all the decoded strings in the form maxK[nmaxK[n]]
        '''
        
        stack = []
        
        for val in s:
            if val == ']':
                
                cur_val = ''
                while stack and stack[-1] != '[':
                    cur_val = stack.pop() + cur_val
                    
                stack.pop()
                
                digit = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                    
                new_str = cur_val * int(digit)
                stack.append(new_str)
                
            else:
                stack.append(val)
            
        return "".join(stack)