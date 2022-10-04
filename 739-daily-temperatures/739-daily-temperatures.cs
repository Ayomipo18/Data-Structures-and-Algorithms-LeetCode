public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int length = temperatures.Length;
        int[] result = new int[length];
        Stack<int> stack = new();
        
        for(int i = 0; i < length; i++) {
            while (stack.Count > 0 && temperatures[stack.Peek()] < temperatures[i]) {
                int index = stack.Peek();
                result[index] = i - index;
                stack.Pop();
            }
            stack.Push(i);
        }
        return result;
    }
}

// class Solution:
//     #time - O(n)
//     #space - O(n)
//     #where n is the length of temperatures
//     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
//         from collections import deque
        
//         result = [0] * len(temperatures)
//         stack = deque()
        
//         for i in range(len(temperatures)):
//             while stack and temperatures[stack[-1]] < temperatures[i]:
//                 index = stack[-1]
//                 result[index] = i - index
//                 stack.pop()
//             stack.append(i)
        
//         return result