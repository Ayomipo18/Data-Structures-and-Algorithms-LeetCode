class Solution:
    #time - O(n^2)
    #space - O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return result
    
#[-1, 0, 1, 2, -1, -4]
#[-4, -1, -1, 0, 1, 2]