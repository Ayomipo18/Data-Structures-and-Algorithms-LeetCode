class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        new_nums = sorted(nums_set, reverse=True)
        return new_nums[2] if len(new_nums) > 2 else new_nums[0]