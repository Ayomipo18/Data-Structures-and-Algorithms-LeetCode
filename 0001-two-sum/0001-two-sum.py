class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        result = []
        
        for i in range(len(nums)):
            num = nums[i]
            number_to_find = target - num
            if number_to_find in nums_map:
                return [nums_map[number_to_find], i]
            
            nums_map[num] = i
            
        return result