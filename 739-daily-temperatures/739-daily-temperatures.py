class Solution:
    #time - O(n)
    #space - O(n)
    #where n is the length of temperatures
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        
        result = [0] * len(temperatures)
        stack = deque()
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack[-1]
                result[index] = i - index
                stack.pop()
            stack.append(i)
        
        return result