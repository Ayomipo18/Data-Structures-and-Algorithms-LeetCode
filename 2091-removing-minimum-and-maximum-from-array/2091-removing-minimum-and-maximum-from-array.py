# class Solution:
#     def minimumDeletions(self, nums: List[int]) -> int:
#         min_index = 0
#         max_index = 0
#         min_num_of_deletions = 0
#         for i in range(1, len(nums)):
#             if nums[min_index] < nums[i]:
#                 min_index = i
#             if nums[max_index] > nums[i]:
#                 max_index = i
        
#         mid = (len(nums) - 1) // 2
#         if max(min_index, max_index) <= mid:
#             min_num_of_deletions = max(min_index, max_index) + 1
            
#         else:
#             min_num_of_deletions = min(min_index + 1, len(nums) - min_index) + min(max_index + 1, len(nums) - max_index)
        
#         return min_num_of_deletions
        
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a=nums.index(max(nums))
        i=nums.index(min(nums))
        if a>=i:
            return(min(a+1,len(nums)-i,len(nums)-a+i+1))
        else:
            return(min(i+1,len(nums)-a,len(nums)-i+a+1))