class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        stack = []
        
        for character in s:
            if character in dict:
                if stack and dict[character] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
                
        return len(stack) == 0