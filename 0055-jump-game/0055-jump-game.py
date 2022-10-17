class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums) - 1
        
        jump = length
        for i in range(length, -1, -1):
            if i + nums[i] >= jump:
                jump = i
            
        return jump == 0