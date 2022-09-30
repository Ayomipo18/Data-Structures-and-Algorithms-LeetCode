class Solution:
    #time - O(n)
    #space - O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] * len(nums)
        suffix = [nums[-1]] * len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
            
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
            
        for i in range(len(nums)):
            if i == 0:
                nums[i] = suffix[i+1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i-1]
            else:
                nums[i] = prefix[i-1] * suffix[i+1]
        
        return nums
        