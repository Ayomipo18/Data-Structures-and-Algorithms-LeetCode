class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curMin = nums[0]
        
        for i in range(1, len(nums)):
            val = nums[i]
            while stack and val >= stack[-1][0]:
                stack.pop()
            if stack and val > stack[-1][1]:
                return True
            
            stack.append([val, curMin])
            curMin = min(curMin, val)
            
        return False