class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        first_position = self.binarySearch(nums, target, 'l')
        if(first_position == -1):
            return [-1, -1]
        
        last_position = self.binarySearch(nums, target, 'r')
        
        return [first_position, last_position]
        
    def binarySearch(self, nums: List[int], target: int, char_type: chr) -> int:
        left = 0
        right = len(nums) - 1
        pos = -1
        
        while(left <= right):
            mid = left + ((right - left) // 2)
            if(nums[mid] == target):
                pos = mid
                if(char_type == 'l'):
                    right = mid - 1
                else:
                    left = mid + 1
            
            elif(nums[mid] > target):
                right =  mid - 1
            else:
                left = mid + 1
        
        return pos
#do a binary search left to find the first value target in nums, if we see that target value, then move left and continue our binary search until we see the lowest index of target. if we don't see any value, return -1.
#do a binary search right to find the first value target in nums, if we see that target value, then move right and continue our binary search until we see the highest index of target. if we don't see any value, return -1.