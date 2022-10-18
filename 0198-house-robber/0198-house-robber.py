class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]

        x = nums[0]
        y = nums[1]

        for index in range(2, n):
            
            temp = max(x, y)
            y = max(y, nums[index] + x)
            x = temp

        return max(x, y)