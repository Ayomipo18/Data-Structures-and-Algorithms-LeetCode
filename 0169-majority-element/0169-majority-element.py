class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = {}
        
        for i in range(len(nums)):
            if nums[i] not in nums_map:
                nums_map[nums[i]] = 0
            nums_map[nums[i]] += 1
            
            if nums_map[nums[i]] > (len(nums)//2):
                return nums[i]
            
        return 0