class Solution:
    def decodeString(self, s: str) -> str:
        '''
        - have a stack to store your useful values (all letters of the alphabet, [, digits) 
        - if i see an end bracket in my string, that's a cue to go to my stack and process the characters until i see [
        - then gather all the digits after and multiply by the string processed.
        - push the procesed string back into the stack.
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