class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            hashmap[target - nums[i]] = i
            
            # for j in range(i + 1, len(nums)):
            #     if(nums[i] + nums[j] == target):
            #         return [i, j]
        
#go through the nums array