class Solution:
    #time - O(n)
    #space - O(n)
    #where n = length of nums
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        result[0] = 1
        
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * right
            right *= nums[i]
        
        return result
        