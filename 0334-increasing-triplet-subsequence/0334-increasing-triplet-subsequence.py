class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float('inf'), float('inf')
        for index, num in enumerate(nums):
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False