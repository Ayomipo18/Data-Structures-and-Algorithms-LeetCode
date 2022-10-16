class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = []
        left = [1] * length
        right = [1] * length
        
        for i in range(1, length):
            if nums[i] <= nums[i-1]:
                left[i] += left[i-1]
                
        for i in range(length - 2, -1, -1):
            if nums[i] <= nums[i+1]:
                right[i] += right[i+1]
        
        print(left)
        print(right)
        for i in range(k, length-k):
            if left[i-1] >= k and right[i+1] >= k:
                result.append(i)
        
        return result