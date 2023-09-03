class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        index = 1
        start from i = 1 and go through the nums array
        if nums[i] == nums[i-1], continue moving
        else do nums[index] = nums[i], then do index += 1
        time - O(n)
        space - O(1)
        where n is the length of nums
        '''
        
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
                
        return index