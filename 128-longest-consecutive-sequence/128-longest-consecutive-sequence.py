class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        
        for value in nums:
            if value - 1 not in nums_set:
                curr_value = value
                curr_result = 0
                while curr_value in nums_set:
                    curr_value += 1
                    curr_result += 1
                result = max(result, curr_result)
            
        return result