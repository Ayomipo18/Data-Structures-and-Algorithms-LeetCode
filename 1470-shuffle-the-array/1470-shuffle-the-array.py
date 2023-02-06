class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left_partition, right_partition = 0, n
        output = []
        
        while right_partition < len(nums):
            output.append(nums[left_partition])
            output.append(nums[right_partition])
            left_partition += 1
            right_partition += 1
            
        return output