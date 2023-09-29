class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increasing = True
            elif nums[i] < nums[i-1]:
                decreasing = True
        
        if increasing == False and decreasing == False:
            return True
        return increasing != decreasing