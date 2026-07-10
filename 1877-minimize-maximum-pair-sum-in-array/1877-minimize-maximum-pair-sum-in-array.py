class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        '''
        - sort nums and form pair sum from each ends
        time - O(nlogn)
        space -O(n)
        '''
        ans = 0
        nums.sort()

        for i in range(len(nums)//2):
            curr_sum_pair = nums[i] + nums[len(nums)-1-i]
            ans = max(ans, curr_sum_pair)

        return ans