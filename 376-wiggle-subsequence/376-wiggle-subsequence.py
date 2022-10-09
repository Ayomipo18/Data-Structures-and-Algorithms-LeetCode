class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        
        up, down = 1, 1
        
        for i in range(length - 1):
            if nums[i] < nums[i+1]:
                up = down + 1
            elif nums[i] > nums[i+1]:
                down = up + 1
        
        return max(up, down)
            