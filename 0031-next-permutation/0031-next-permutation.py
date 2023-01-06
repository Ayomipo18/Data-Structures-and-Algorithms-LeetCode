class Solution:
    '''
    [1,2,3] - 
    [3,2,1] - 
    [2,1,3] -
    - find the rightmost peak value
    - when found, check if there is a value immediatley after rightmost value till the end of aray that is in between rightmost peak index and righmost peak index - 1
    - if there is, swap the value and value at righmost peak index - 1
    - else swap the value at rightmost peak index and righmost peak index - 1
    - then  sort the string from rightmost index till end of array
    time - O(nlogn)
    space - O(n), due to sorting
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        peak, i = -1, 1
        n = len(nums)
        
        if n == 1:
            return nums
        
        while i < n:
            if nums[i] > nums[i-1]:
                peak = i
            i += 1
        
        if peak == -1:
            start, end = 0, n-1
            while start < end:
                self.swap(nums, start, end)
                start += 1
                end -= 1
            return nums
        
        index = peak
        for i in range(peak+1, n):
            if nums[i] > nums[peak-1] and nums[i] < nums[peak]:
                index = i
            i += 1
        
        self.swap(nums, peak-1, index)
        nums[peak:] = sorted(nums[peak:])
        
        return nums
        
        
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
#         i = len(nums) - 2
#         while i >= 0 and nums[i+1] <= nums[i]:
#             i -= 1
#         print(i)
#         if i >= 0:
#             j = len(nums) - 1
#             while nums[j] <= nums[i]:
#                 j -= 1
#             print(j)
#             self.swap(nums, i, j)
#         self.reverse(nums, i+1)


#     def reverse(self, nums, index):
#         start, end = index, len(nums)-1
#         while start < end:
#             self.swap(nums, start, end)
#             start += 1
#             end -= 1