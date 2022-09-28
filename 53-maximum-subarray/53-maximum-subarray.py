class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_total = nums[0]
        
        for value in nums:
            if total < 0:
                total = 0
            total += value
            max_total = max(total, max_total)
                
        return max_total