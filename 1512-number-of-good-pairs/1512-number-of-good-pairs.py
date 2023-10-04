class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        [1, 1, 1, 1, 1]
        '''
        result = 0
        nums.sort()
        nums.append(101)
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if count > 1:
                    result += (math.factorial(count) // (math.factorial(2) * math.factorial(count-2)))
                count = 1
            else:
                count += 1
        return result