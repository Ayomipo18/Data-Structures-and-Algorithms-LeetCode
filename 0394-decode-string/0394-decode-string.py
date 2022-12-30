class Solution:
    '''
    time - O((maxk^countk)⋅n)
    space - O(sum((maxk^countk)⋅n))
    '''
    def decodeString(self, s: str) -> str:
        from collections import deque
        stack = deque()

        for val in s:
            if val == ']':
                cur_str = ""
                while stack[-1] != '[':
                    val = stack.pop()
                    cur_str = val + cur_str

                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    val = stack.pop()
                    k = val + k
                
                stack.append(int(k) * cur_str)
            else:
                stack.append(val)

        return "".join(stack)