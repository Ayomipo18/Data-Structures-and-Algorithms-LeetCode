class Solution:
    #where n = length of nums
    #time - O(n)
    #space - O(1)
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = 0
        max_index = 0
        length = len(nums)
        for i in range(1, len(nums)):
            if nums[min_index] < nums[i]:
                min_index = i
            if nums[max_index] > nums[i]:
                max_index = i
        
        return min(max(min_index, max_index) + 1, max(length - min_index, length - max_index), min_index + 1 + length - max_index, max_index + 1 + length - min_index)