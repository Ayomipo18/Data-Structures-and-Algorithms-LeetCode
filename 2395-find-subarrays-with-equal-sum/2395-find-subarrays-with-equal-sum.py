class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return False
        
        nums_set = set()
        
        for i in range(len(nums)-1):
            curr_sum = nums[i] + nums[i+1]
            if curr_sum in nums_set:
                return True
            else:
                nums_set.add(curr_sum)
        
        return False
                