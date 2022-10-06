class Solution:
    #time - O(n)
    #space - O(1) or O(n)
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ''
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(res)
                res = ''
            elif char == ')':
                res = stack.pop() + res[::-1]
            else:
                res += char
                
        return res
        
#use a stack
#res = ''
#loop thru every element in s,
    #if you see '(', push res into our stack, meaning push the value before (, then make res =''
    #else if you see ')', pop from our stack and add the popped value to the curr reverse res
    #else res += curr element
    
#so, i can either get all index to reverse with and do it with the string chars in a list or
#i push each string in a stack and form my string on the go