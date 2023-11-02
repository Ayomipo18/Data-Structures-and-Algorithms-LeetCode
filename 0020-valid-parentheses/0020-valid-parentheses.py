class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        
        if len(s) < 2:
            return False
        
        for val in s:
            if val in stack_map and stack and stack[len(stack)-1] == stack_map[val]:
                stack.pop()
            else:
                stack.append(val)
                
        return len(stack) == 0